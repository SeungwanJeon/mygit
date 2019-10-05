import numpy as np
np.seterr(divide='ignore', invalid='ignore')
from numpy.fft import fft,ifft,fftshift
from scipy import signal
from scipy.fftpack import dct,idct
from scipy.interpolate import interp1d

import time


class Beamformer:
    def __init__(self, Fs, ld, Ne, c, p, depth, dx, theta_apo, wintype, Nt_rf):
        self.Fs = Fs                                # Center frequency [Hz]
        self.ld = ld                                # Rx line density
        self.Ne = Ne                                # number of elelments
        self.c = c                                  # speed of sound [m/s]
        self.depth = depth                          # depth [m]
        self.wintype = wintype                      # window type 'rect' or 'hann'
        self.dx = dx                                # pitch size [m]
        self.p = p                                  # p value for nonlinear beamforming
        self.theta_apo = np.radians(theta_apo)      # acceptance angle [deg->rad]
        self.Nt_rf=Nt_rf                            # RF size along t
        # dependent variables
        self.dz = self.c/self.Fs                    # z pixelsize [m]
        self.Nt = round(self.depth/self.dz)         # pixel number in temporal axis
        self.Sl = self.ld*self.Ne                   # Scanline in BF image
        # Axis for display [unit: cm]
        self.extent=[-self.Ne*self.dx/2*100, self.Ne*self.dx/2*100, self.depth*100, 0]
        # call the function to calculate delay
        self._Calculate_delay()

    def _Calculate_delay(self):
        pass

    def _NonlinearScale(self,data_rf):
        Nt_rf=data_rf.shape[0]
        data_rf_scaled=np.zeros_like(data_rf);
        for idx in range(data_rf.shape[1]):
            f,t,rf_stft=signal.stft(data_rf[:,idx], nperseg=128)
            t,aline_scaled=signal.istft(np.exp(1j*np.angle(rf_stft))*abs(rf_stft)**(1/self.p))
            data_rf_scaled[:,idx]=aline_scaled[:Nt_rf]
        return data_rf_scaled

    def PerformBF(self,data_rf):
        pass


class Beamformer_DAS(Beamformer):
    def _Calculate_delay(self):
        Ne_margin = (1-1/self.ld)/2                 # required margin for Rx line density
        self.delay = np.zeros((self.Nt, self.Sl, self.Ne),dtype='float32')
        self.win = np.zeros((self.Nt, self.Sl, self.Ne),dtype='float32')
        aperture = np.zeros((self.Nt, self.Sl, self.Ne),dtype='float32')
        zi = np.reshape(np.arange(self.Nt), [-1,1])
        xi = np.linspace(0-Ne_margin, self.Ne-1+Ne_margin, self.Sl)
        for idx in range(self.Ne):
            self.delay[:,:,idx] = np.sqrt(((xi-idx)*self.dx)**2+(zi*self.dz)**2)/self.dz
            aperture[:,:,idx] = abs(xi-idx)*self.dx / (zi*self.dz)
        # self.aperture[0,:,:] = 0
        aperture=np.minimum(aperture/np.tan(self.theta_apo),1)
        self.delay = self.delay.astype('int')
        if self.wintype=='rect':
            self.win=np.less_equal(aperture,1)
        elif self.wintype=='hann':
            self.win=np.cos(aperture/2*np.pi)**2
        else:
            print('Error: Check the wintype')

    def PerformBF(self, data_rf):
        if self.p != 1:
            data_rf=super()._NonlinearScale(data_rf)
        img_bf = np.zeros((self.Nt, self.Sl),dtype='float32')
        for idx in range(1,self.Ne):
            rf_vec = data_rf[:,idx]
            img_bf = img_bf+rf_vec[self.delay[:,:,idx]]*self.win[:,:,idx]
        return img_bf

class Beamformer_Fourier(Beamformer):
    def _Calculate_delay(self):
        Pad_factor=2
        self.Ne_pad=self.Ne*Pad_factor
        self.w = np.arange(self.Nt_rf)/self.Nt_rf*self.Fs*np.pi
        kx=(np.arange(self.Ne_pad)-self.Ne_pad/2)/(self.Ne_pad)/self.dx*2*np.pi
        kz=np.reshape(np.arange(self.Nt_rf)/self.Nt_rf/self.dz*np.pi,[-1,1])
        self.wi_mat = np.sqrt(kx**2 + kz**2)
        self.Coeff_mat = kz/self.wi_mat
        self.Coeff_mat[np.isnan(self.Coeff_mat)]=0

    def PerformBF(self, data_rf):
        if self.p != 1:
            data_rf=super()._NonlinearScale(data_rf)
        P_kx_w=fftshift(fft(dct(data_rf,norm='ortho',axis=0),self.Ne_pad,axis=1),axes=1)
        # P_kx_w -> P_kx_kz
        P_kx_kz = np.zeros([self.Nt_rf, self.Ne_pad],dtype=complex)
        for idx in range(self.Ne_pad):
            f = interp1d(self.w,P_kx_w[:,idx],axis=0,bounds_error=0,fill_value=0)
            P_kx_kz[:,idx]=f(self.wi_mat[:,idx]*self.c)
        P_kx_kz = self.c*self.Coeff_mat*P_kx_kz
        # Rx line density (zero padding)
        P_kx_kz_pad=np.pad(P_kx_kz,((0,0),(round(self.Ne_pad/2*(self.ld-1)),
                    round(self.Ne_pad/2*(self.ld-1)))),'constant',constant_values=0)
        # P_kx_kz -> P_x_z
        P_x_z=np.real(idct(ifft(fftshift(P_kx_kz_pad,axes=1),axis=1),norm='ortho',axis=0))
        return P_x_z[:self.Nt,:self.Sl]
