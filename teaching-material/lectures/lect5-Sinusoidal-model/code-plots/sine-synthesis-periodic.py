import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import ifft

f0 = 500.0
fs = 10000.0
A0 = .8 
phi0 = 1.5 
Ns = 64
hNs = Ns/2

mY = np.zeros(hNs)
pY = np.zeros(hNs)
Y = np.zeros(Ns)
yw = np.zeros(Ns)
Y = np.zeros(Ns, dtype=complex)

k = np.int(np.round(Ns*f0/fs))
mY[k] = A0 * Ns
pY[k] = phi0
Y[:hNs] = .5*mY*np.exp(1j*pY)
Y[hNs+1:] = Y[hNs-1:0:-1].conjugate()   

plt.figure(1)
plt.subplot(3,1,1)
plt.plot(np.arange(0, fs/2.0, fs/(float(Ns))), mY, 'ro')
plt.axis([0,fs/2.0,0,Ns])
plt.xlabel('frenquency (Hz)')
plt.ylabel('amplitude')

plt.subplot(3,1,2)
plt.plot(np.arange(0, fs/2.0, fs/(float(Ns))), pY, 'bo')
plt.axis([0,fs/2.0,0,2*np.pi])
plt.xlabel('frenquency (Hz)')
plt.ylabel('phase (radians)')

y = np.real(ifft(Y))     
yw[:hNs-1] = y[hNs+1:] 
yw[hNs-1:] = y[:hNs+1] 

plt.subplot(3,1,3)
plt.plot(np.arange(-hNs/float(fs), hNs/float(fs), 1.0/(fs)), yw, 'r')
plt.axis([-hNs/float(fs), (hNs-1)/float(fs),-1,1])
plt.xlabel('time (seconds)')
plt.ylabel('amplitude')

plt.show()