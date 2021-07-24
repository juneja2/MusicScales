from scale import Scale
from asdr import Envelope
import numpy as np
from scipy.io.wavfile import write

if __name__ == "__main__":
    a_major_scale = Scale('A', Scale.MAJOR)

    duration = 2
    percents = [10, 10, 65, 15]
    sustain_level = 0.4
    asdr = Envelope(duration, np.array(percents), 
                                sustain_level)

    freqs = a_major_scale.freqs()
    print(a_major_scale.scale())
    print(freqs)

    waveform_of_notes = []

    for freq in freqs:
        waveform_of_notes.append(asdr.asdr_with_sine_wave(freq))

    scale_waveform = np.concatenate(tuple(waveform_of_notes))

    write("A4_scale.wav", Envelope.SAMPLING_RATE, scale_waveform.astype(np.int16))

    

    