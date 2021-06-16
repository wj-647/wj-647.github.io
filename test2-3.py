import os
from thinkdsp import decorate
from thinkdsp import Sinusoid
from thinkdsp import normalize, unbias
import numpy as np
import matplotlib.pyplot as plt
from thinkdsp import SquareSignal


class SawtoothSignal(Sinusoid):
    """Represents a sawtooth signal."""
    
    def evaluate(self, ts):
        """Evaluates the signal at the given times.

        ts: float array of times
        
        returns: float wave array
        """
        cycles = self.freq * ts + self.offset / np.pi / 2
        frac, _ = np.modf(cycles)
        ys = normalize(unbias(frac), self.amp)
        return ys
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

plt.title("方波")
square = SquareSignal(1100).make_wave(duration=0.5, framerate=10000)
wave1=square.make_spectrum()
square.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')
wave = wave1.make_wave()

wave.write(filename="sound2-3.wav")
plt.show()