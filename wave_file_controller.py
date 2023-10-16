import numpy as np
import simpleaudio as sa
import wave
import os

class WaveFileController:
    def __init__(self, sample_rate):
        self.sample_rate = sample_rate
        self.filename = 'output.wav'

    def save_wavefile(self, signal):
        signal = np.int16(signal/np.max(np.abs(signal)) * 32767)
        with wave.open(self.filename, 'w') as wf:
            wf.setnchannels(1)  # モノラル
            wf.setsampwidth(2)  # 16 bits = 2 bytes
            wf.setframerate(self.sample_rate)
            wf.writeframes(signal.tobytes())

    def play_wavefile(self):
        wave_obj = sa.WaveObject.from_wave_file(self.filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()  # Block until sound has finished playing

    def remove_wavefile(self):
        os.remove(self.filename)