
import numpy as np
import copy
a=np.random.rand(10000,10000);
%timeit b=a[:];
%timeit c=copy.deepcopy(a);
id(a)
id(b)
id(c)



def add(a,b):
    return a+b
def swap(a,b):
    return b,a
add(10,20)
swap(10,20)

add = lambda a,b : a + b
swap = lambda a,b : b,a
add(10,20)
swap(10,20)


def add_list(a):
    sum=0
    for i in range(len(a)):
        sum+=a[i]
    return sum
add_list([1, 2])

sum([1,2])
list(reversed([1,2]))
reversed([1,2])
reversed((1,2))


import random
a=[random.random() for _ in range(5)]
[1,2]+[3,4]
a=(1,3)



d={'kim':1, 'jeon':3}
d['park']=2
d.keys()
d.values()
d.items()
'kim' in d
del d['jeon']
d


sentence='Python is fun!!'



import time
import matplotlib.pyplot as plt
#Compute and Plot FFT
tic = time.clock()
plt.figure(3);
N = N2 #truncate array to the last power of 2
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
yf = fft(x, n = N)
plt.plot(xf, 2.0/N * np.abs(yf[0:np.int(N/2)]))
plt.grid()
plt.xlabel('Frequency (Hz)')
plt.ylabel('Accel (g)')
plt.title('FFT - ' + file_path)
toc = time.clock()
print("FFT Time:",toc-tic)
plt.show()


def my_len(a):
    length=0
    for _ in a:
        length+=1
    return length
my_len('abc')


def count_even_vv(*n):
    cnt = 0
    print(n)
    for v in n:
        if v%2 == 0:
            cnt += 1
    return cnt
count_even_vv(2,3,5,6)

def factorial(n):
    result=1
    for v in range(1,n+1):
        result*=v
    return result
factorial(5)

def pow(n, a):
    return n**a
pow(2,5)

def printName(first, second='lee'): #second 변수 기본값 ‘Lee’
    print('My name is', first, second + '.')
printName('aa','bb')
printName('aa')

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
a=1;b=2
print(add(a,b),sub(a,b),mul(a,b),div(a,b))

def hour_min_sec(second):
    ss=second%60
    mm=second//60
    hh=min//60
    mm=mm%60
    return hh,mm,ss
hour_min_sec(57894)

def abc(a=1,b=2,c=3):
    print (a,b,c)
b=11
abc(b=b)
abc()

import numpy as np
a=np.arange(5)
b=np.arange(6,10)
a[a>=b.shape[0]]=0
b[a]

t = [1, 2, 3]
def test(a):
    a += [4, 5, 6]
test(t)
print(t)

t = {1:'a'}
def test(a):
    a[2] = 'b'
test(t)
print(t)

t = (1, 2, 3)
def test(a):
    a += (4, 5, 6)
test(t)
print(t)
np.arange(2,5)


def get_min_max(l):
    min=l[0];max=l[0];
    for v in l:
        if min>v:
            min=v
        if max<v:
            max=v
    l.remove(min)
    l.remove(max)
    return min, max
l = [3, 5, 9, 1, 2]
min,max=get_min_max(l)
print(min,max,l)

def sparseVectorDotProduct(v1,v2):
    dotval=0
    for key in v1.keys()&v2.keys():
        dotval+=v1[key]*v2[key]
    return dotval

def sparseVectorDotProduct_alter(v1,v2):
    dotval=0
    for key in v1.keys():
        try:
            dotval+=v1[key]*v2[key]
        except:
            pass
    return dotval

def sparseVectorDotProduct_alter1(v1,v2):
    dotval=0
    for key in v1.keys():
        try:
            dotval+=v1[key]*v2[key]
        except KeyError:
            pass
        except ValueError:
            pass
    return dotval

def sparseVectorDotProduct_alter2(v1,v2):
    return sum([v1[k]*v2[k] for k in v1 if k in v2])

sparseVectorDotProduct_alter2(v1,v2)

v1={'a':5}; v2={'a':3, 'b':2}
sparseVectorDotProduct(v1,v2)
sparseVectorDotProduct_alter(v1,v2)
v1={'c':5}; v2={'a':2, 'b':1}
sparseVectorDotProduct(v1,v2)
sparseVectorDotProduct_alter(v1,v2)
v1={'a':5, 'b':4}; v2={'a':-1, 'b':2}
sparseVectorDotProduct(v1,v2)
sparseVectorDotProduct_alter(v1,v2)


import random
random.sample(range(1,45+1),6)



import numbatest
import time
time.time()
print('NumbaCal')
%timeit numbatest.NumbaCal()

print('PurePythonCal')
%timeit numbatest.PurePythonCal()

def letter_dict(s):
    d=dict()
    for k in set(s):
        d[k]=s.count(k)
    return d
def letter_dict_alter(s):
    return {k:s.count(k) for k in set(s)}
def max_letter(d):
    for k in d:
        if d[k]==max(d.values()):
            return k
def comb_dict (d1, d2):
    d3=d1.copy()
    for k in d2:
        if k in d1:
            d3[k]+=d2[k]
        else:
            d3[k]=d2[k]
    return d3
def comb_dict_alter(d1, d2):
    d3=d1.copy()
    d3.update(d2)
    return d3

a = letter_dict_alter('red apple')
b = letter_dict_alter('yellow banana')
c = comb_dict(a, b)
c = comb_dict_alter(a, b)

list(zip(b.keys(),b.values()))

print(max_letter(a))




c = comb_dict(a, b)
max(a.values())
print(c)

def temp(x):
    if ((x%4==0) and (x%100!=0)) or (x%400==0):
        print('윤년')
    else:
        print('평년')
temp(int(input()))
