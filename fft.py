from scipy.fft import fft
from scipy.io import wavfile
import numpy as np
import math
from matplotlib import pyplot as plt

rate, data = wavfile.read('./sample.wav')
N = len(data)
step = N/rate
time = np.linspace(0, step, num=N)

y = fft(data, N)
x = np.linspace(0, rate, num=N)

plt.plot(x[:N//2], np.abs(y[:N//2]))
plt.show()