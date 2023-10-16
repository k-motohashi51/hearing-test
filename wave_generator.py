import numpy as np

class WaveGenerator:
    def __init__(self, sample_rate, duration, amplitude):
        self.sample_rate = sample_rate
        self.duration = duration
        self.amplitude = amplitude
    
    def create_sin_wave(self, frequency):
        t = np.linspace(
            start=0,
            stop=self.duration,
            num=int(self.sample_rate * self.duration),
            endpoint=False
        )
        signal = self.amplitude * np.sin(2 * np.pi * frequency * t)
        return signal