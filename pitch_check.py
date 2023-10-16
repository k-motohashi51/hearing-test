import wave_generator as wg
import sound_player as sp
import time

class PitchCheck:
    def __init__(self, freq_base):
        self.freq_base = freq_base  # 基準周波数 (Hz)

        self.sample_rate = 44100    # サンプリングレート (Hz)
        self.duration = 1.0         # 再生時間 (sec)
        self.amplitude = 0.5        # 音量（0 ~ 1）

        # 使用するモジュールのインスタンス化
        self.wgi = wg.WaveGenerator(self.sample_rate, self.duration, self.amplitude)
        self.spi = sp.SoundPlayer(self.sample_rate)

        self.freq_range = 20    # 基準周波数の周囲の範囲 (Hz)
        self.freq_step = 1      # 周波数の刻み幅 (Hz)

        # 基準周波数 +- 20Hz
        self.freq_max = self.freq_base + self.freq_range
        self.freq_min = self.freq_base - self.freq_range
    
    def run(self):
        print("区別可能な音の高さを測定します。")

        print("基準音以上の音を再生します。")
        ans1 = self.measure_pitch_ability_up()

        print("基準音以下の音を再生します。")
        ans2 = self.measure_pitch_ability_down()

        print("あなたが聞き分けられるのは、基準音に対し、" + str(ans1) + "Hz上の音です。")
        print("あなたが聞き分けられるのは、基準音に対し、" + str(ans2) + "Hz下の音です。")

        print("測定を終了します。")

    # 基準音より高い音を降順に再生し、聞き分けられる周波数を測定する
    def measure_pitch_ability_up(self):
        freq_can_hear = 0   # 聞き分けられる周波数

        for freq in range(self.freq_max, self.freq_base - 1, -self.freq_step):
            print("基準音を再生します。")
            signal = self.wgi.create_sin_wave(self.freq_base)
            self.spi.play_sound(signal)

            time.sleep(0.5) # ブランク

            print("基準音より高い音を再生します。：" + str(freq) + "Hz")
            signal = self.wgi.create_sin_wave(freq)
            self.spi.play_sound(signal)

            # 正しい入力があるまでループ
            while(True):
                print("聞き分けられましたか？ [y/n]")

                input_char = input()

                if (input_char == 'n'):
                    return freq_can_hear    # 聞き分けられる周波数を返す

                if (input_char == 'y'):
                    freq_can_hear = freq    # 聞き分けられる周波数を更新
                    break

                print("yかnで答えてください。")

        return freq_can_hear

    # 基準音より低い音を昇順に再生し、聞き分けられる周波数を測定する
    def measure_pitch_ability_down(self):
        freq_can_hear = 0   # 聞き分けられる周波数

        for freq in range(self.freq_min, self.freq_base + 1, self.freq_step):
            print("基準音を再生します。")
            signal = self.wgi.create_sin_wave(self.freq_base)
            self.spi.play_sound(signal)

            time.sleep(0.5) # ブランク

            print("基準音より低い音を再生します。：" + str(freq) + "Hz")
            signal = self.wgi.create_sin_wave(freq)
            self.spi.play_sound(signal)

            # 正しい入力があるまでループ
            while(True):
                print("聞き分けられましたか？ [y/n]")

                input_char = input()

                if (input_char == 'n'):
                    return freq_can_hear    # 聞き分けられる周波数を返す

                if (input_char == 'y'):
                    freq_can_hear = freq    # 聞き分けられる周波数を更新
                    break

                print("yかnで答えてください。")

        return freq_can_hear
