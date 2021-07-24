import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

class Envelope:
    SAMPLING_RATE = 44100 # 44.1 KHz
    MAX_AMPLITUDE = 4096
    def __init__(self, duration, percents, sustain_level):

        assert sum(percents) == 100

        for p in percents:
            assert p >= 0

        assert 0 <= sustain_level <= 1
        assert duration > 0

        self.percents      = percents.copy() * duration / 100
        self.sustain_level = sustain_level
        self.duration      = duration

    def attack_time(self):
        return self.percents[0]

    def delay_time(self):
        return self.percents[1]

    def sustain_time(self):
        return self.percents[2]

    def release_time(self):
        return self.percents[3]

    def asdr(self, append_zero=True, debug=False):
        attack = self.linear_amp(0, 1, self.attack_time())
        delay = self.linear_amp(1, 0.4, self.delay_time())
        release = self.linear_amp(0.4, 0, self.release_time())

        # Due to floating point arthimetic, there are small
        # inconsistencies in the total number of samples in
        # each attack, delay and release. In order to resolve
        # this, I'm going to put the samples that are not taken
        # in account by the other in sustain.
        samples_so_far = self.num_samples(self.attack_time()) + \
                         self.num_samples(self.delay_time())  + \
                         self.num_samples(self.release_time())

        total_samples = self.num_samples(self.duration)

        sustain = np.repeat(0.4, total_samples - samples_so_far)

        if debug:
            print("Attack = ", attack)
            print("Delay = ", delay)
            print("Sustain = ", sustain)
            print("Release = ", release)

        zero_array = np.empty(0)
        if append_zero:
            zero_array = np.zeros(1)

        return np.concatenate((attack, delay, sustain, release, zero_array))
    
    def asdr_with_sine_wave(self, freq):
        time = np.linspace(0, self.duration, self.num_samples(self.duration) + 1, endpoint=True)
        sine_wave = np.sin(2 * np.pi * freq * time)
        print(np.shape(sine_wave))
        asdr_sine_wave = self.MAX_AMPLITUDE * self.asdr() * sine_wave
        return asdr_sine_wave

    @classmethod
    def linear_amp(cls, start_amp, end_amp, duration):
        return cls.line(cls.slope(start_amp, end_amp, duration),
                            start_amp, duration)

    @classmethod
    def line(cls, slope, y_intercept, duration):
        return y_intercept + slope * np.linspace(0, duration, 
                                    cls.num_samples(duration), endpoint=False)

    @classmethod
    def slope(cls, start, end, run):
        return (end - start) / run

    @classmethod
    def num_samples(cls, duration):
        return int(cls.SAMPLING_RATE * duration)

if __name__ == "__main__":
    duration = 2
    percents = [10, 10, 65, 15]
    sustain_level = 0.4

    ASDR = Envelope(duration, np.array(percents), sustain_level)
    # To get a full envelope, need to append zero
    # But when playing bunch of notes, then no need to
    # append zero because each notes starts at zero
    # So the effect would be to have 0 appended
    # As far as the last note is concerned. Also,
    # don't need to put a 0 there because the audio would
    # stop playing and effectively the effect would of having 0 audio.
    # There might be a beep which I need to watch out for.
    # I'm just going to have a zero in there because it's doesn't really matter
    # because of short period of time.
    amplitudes = ASDR.asdr()
    time_samples = np.linspace(0, duration, Envelope.num_samples(duration) + 1, endpoint=True)

    print("Amplitudes =", amplitudes)
    print("Time samples =", time_samples)
    # plt.plot(time_samples, amplitudes)
    # plt.show()

    write("A4.wav", Envelope.SAMPLING_RATE, ASDR.asdr_with_sine_wave(440).astype(np.int16))
    plt.plot(time_samples, ASDR.asdr_with_sine_wave(440))
    plt.show()