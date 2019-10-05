import sys
sys.dont_write_bytecode=True

# %matplotlib qt # activate this line if you want to display the figure with hydrogen
import matplotlib.pyplot as plt
from scipy import io
from Beamformer import Beamformer_Fourier

# load RF data
mat_file = io.loadmat('RF_PA.mat')
data_rf=mat_file['DCfilteredData'][:3000,:].astype('float32')

# input parameter
# 'Fs'        Center frequency [Hz]
# 'ld'        Rx line density
# 'Ne'        number of elelments
# 'c'         speed of sound [m/s]
# 'p'         p value for nonlinear beamforming
# 'depth'     depth [m]
# 'dx'        pitch size [m]
# 'theta_apo' acceptance angle
# 'wintype'   window type 'rect' or 'hann'
# 'Nt_rf'     RF size along t
params_dict={'Fs':40e6,
             'ld':3,
             'Ne':128,
             'c':1500,
             'p':1,
             'depth':0.04,
             'dx':300e-6,
             'theta_apo':35,
             'wintype':'hann',
             'Nt_rf':data_rf.shape[0]}

# create beamformer instance
BF_Fourier=Beamformer_Fourier(**params_dict)

# perform beramformer
img_bf=BF_Fourier.PerformBF(data_rf)

# display
titlefont = {'weight': 'bold','size': 12}
labelfont = {'weight': 'bold','size': 10}

plt.figure(1);
plt.subplot(1,2,1);plt.title('RF data',fontdict=titlefont)
img=plt.imshow(data_rf, aspect='auto')
plt.xlabel('Lateral [pixel]',fontdict=labelfont);plt.ylabel('Time [pixel]',fontdict=labelfont)
plt.subplot(1,2,2);plt.title('BF data',fontdict=titlefont)
img=plt.imshow(img_bf, aspect='auto',interpolation='sinc',extent=BF_Fourier.extent)
plt.xlabel('Lateral [cm]',fontdict=labelfont);plt.ylabel('Depth [cm]',fontdict=labelfont)
plt.colorbar()
plt.ylim([4, 2.4])
plt.show()
