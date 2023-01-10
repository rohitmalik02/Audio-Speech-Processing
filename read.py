from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import audio_metadata

rate, data = wavfile.read('./sample.wav')
time = np.linspace(0, len(data)/rate, num=len(data))
metadata = audio_metadata.load("./sample.wav")
print(metadata)
# Start, stop, number of points
# stop = number of samples/sample rate
print(f"Rate: {rate}")
print(f"Number of samples: {len(data)}")
print(f"Type: {type(data)}")
plt.figure(1)
plt.plot(time, data)
plt.show()
# audio files might have multiple channels
# i.e data can be a multi-dimensional array