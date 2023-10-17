import numpy as np
import matplotlib.pyplot as plt

# Parameters
amplitude = 1.0  # Amplitude of the sine wave
frequency = 1.0  # Frequency of the sine wave (1 cycle per period)
num_samples = 128  # Number of samples in the array
period = 1.0 / frequency  # Period of the sine wave (time for one cycle)

# Generate time values for one period
t = np.linspace(0, period, num_samples, endpoint=False)

# Generate the sine wave
sine = ((amplitude * np.sin(2 * np.pi * frequency * t))+1)*(1023/2)

for i in range(0,len(sine),1):
    sine[i] = int(round(sine[i]))

sawtooth = np.linspace(0,1023,128,dtype=int)
h1 = np.linspace(0,1023,65,dtype=int)
h2 = np.linspace(1023,0,65,dtype=int)
h2 = h2[1:len(h2)]
triangle = np.append(h1,h2)
sine = np.append(sine,512)
sine = sine.astype(np.int32)
print(sine.tolist())
print()
print(sawtooth.tolist())
print()
print(triangle.tolist())

# Plot the sine wave
plt.plot(sine)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('One Period of a Sine Wave')
plt.grid(True)
plt.show()