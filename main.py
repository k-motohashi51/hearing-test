import wave_generator as wg
import sound_player as sp

def main():
    # 再生するsin波のパラメーター
    frequency = 880.0   # 周波数 (Hz)
    duration = 1.0      # 再生時間 (sec)
    sample_rate = 44100 # サンプリングレート (Hz)
    amplitude = 0.5     # 音量（0 ~ 1）

    wgt = wg.WaveGenerator(sample_rate, duration, amplitude)
    spt = sp.SoundPlayer(sample_rate)

    signal = wgt.create_sin_wave(frequency)
    spt.play_sound(signal)

if __name__ == '__main__':
    main()
