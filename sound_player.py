import wave_file_controller as wfc

class SoundPlayer:
    def __init__(self, sample_rate):
        self.sample_rate = sample_rate
        self.wfct = wfc.WaveFileController(sample_rate)

    def play_sound(self, signal):
        self.wfct.save_wavefile(signal)
        self.wfct.play_wavefile()
        self.wfct.remove_wavefile()