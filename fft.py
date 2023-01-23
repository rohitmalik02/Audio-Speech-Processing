from scipy.fft import fft, ifft
from scipy.io import wavfile
import numpy as np
from matplotlib import pyplot as plt

rate, data = wavfile.read('./audio_samples/sample.wav')
N = len(data)
step = N/rate
time = np.linspace(0, step, num=N)

y = fft(data, N)
x = np.linspace(0, rate, num=N)

plt.plot(x[:N//2], np.abs(y[:N//2]))
plt.show()
# print(len(x))
# print(x[:N//2])

filter = np.zeros(N)
for i in range(N//4):
    filter[i] = 1
for i in range(N//2+1, 3*N//4):
    filter[i] = 1
y = y * filter
# plt.plot(x[:N//2], np.abs(y[:N//2]))
# plt.show()
data_new = ifft(y, N)
data_new = np.real(data_new)
data_new = data_new.astype(np.dtype('i2'))
print(data_new)
print(np.abs(data))
plt.plot(time, data_new)
plt.show()
wavfile.write('filtered_wav.wav', rate, data.astype(np.dtype('i2')))