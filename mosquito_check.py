import wave_generator as wg
import sound_player as sp

class MosquitoCheck:
    def __init__(self):
        self.sample_rate = 44100    # サンプリングレート (Hz)
        self.duration = 1.0         # 再生時間 (sec)
        self.amplitude = 0.5        # 音量（0 ~ 1）

        # 使用するモジュールのインスタンス化
        self.wgi = wg.WaveGenerator(self.sample_rate, self.duration, self.amplitude)
        self.spi = sp.SoundPlayer(self.sample_rate)

        self.freq_min = 1000    # 測定する可聴域の下限 (Hz)
        self.freq_max = 20000   # 測定する可聴域の上限 (Hz)
        self.freq_step = 1000   # 周波数の刻み幅 (Hz)

    def run(self):
        print("可聴域の上限を測定します。")

        print("下限周波数から上限周波数までのsin波を再生します。")
        ans1 = self.measure_audible_up_value()

        print("上限周波数から下限周波数までのsin波を再生します。")
        ans2 = self.measure_audible_down_value()

        print("あなたの可聴域の上限の候補１：" + str(ans1))
        print("あなたの可聴域の上限の候補２：" + str(ans2))

        print("測定を終了します。")

    # 可聴域の上限を測定する(下限周波数から上限周波数までのsin波を再生する)
    def measure_audible_up_value(self):
        result_tmp = 0  # 聞き分けられる周波数

        for frequency in range(self.freq_min, self.freq_max, self.freq_step):
            print('現在の周波数：' + str(frequency) + 'Hz')

            # sin波を生成して再生
            signal = self.wgi.create_sin_wave(frequency)
            self.spi.play_sound(signal)

            # 正しい入力があるまでループ
            while(True):
                print("聞こえましたか？ [y/n]")

                input_char = input()
                if (input_char == 'n'):                        
                    return result_tmp   # 聞き分けられる周波数を返す

                if (input_char == 'y'):
                    result_tmp = frequency  # 聞き分けられる周波数を更新
                    break

                print("yかnで答えてください。")
            
        return self.freq_max
            
    # 可聴域の下限を測定する(上限周波数から下限周波数までのsin波を再生する)
    def measure_audible_down_value(self):
        result_tmp = 0  # 聞き分けられる周波数

        for frequency in range(self.freq_max, self.freq_min - 1, -self.freq_step):
            print('現在の周波数：' + str(frequency) + 'Hz')

            # sin波を生成して再生
            signal = self.wgi.create_sin_wave(frequency)
            self.spi.play_sound(signal)

            # 正しい入力があるまでループ
            while(True):
                print("聞こえましたか？ [y/n]")

                input_char = input()

                if (input_char == 'n'):
                    break

                if (input_char == 'y'):
                    result_tmp = frequency  # 聞き分けられる周波数を更新
                    return result_tmp   # 聞き分けられる周波数を返す

                print("yかnで答えてください。")
            
        return self.freq_min