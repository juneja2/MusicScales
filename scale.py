#!/usr/local/bin/python3

# Goal is to print any scale(major or minor)
# given an input of the root note

# c_scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']
# c_minor_scale = ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#', 'C']

class Scale:
    NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 
             'F#', 'G', 'G#', 'A', 'A#', 'B']
 
    MAJOR_DISTS = [0, 2, 2, 1, 2, 2, 2, 1]
    MINOR_DISTS = [0, 2, 1, 2, 2, 1, 2, 2]

    MAJOR, MINOR = 1, 0

    C4 = 261.63 #Frequency of Note C4

    def __init__(self, root, scale_type):
        assert root in self.NOTES
        assert scale_type in [0, 1]
        self.root = root
        self.type = scale_type
        self.OCTAVE = { self.NOTES[i]: self.C4 * pow(2,(i/12)) for i in range(len(self.NOTES))}

    def target_dists(self):
        return self.MAJOR_DISTS if self.type == self.MAJOR \
				 else self.MINOR_DISTS

    def scale(self):
        scale_notes = []
        curr_note_index = self.NOTES.index(self.root)  

        for dist in self.target_dists():
            curr_note_index += dist
            curr_note_index %= len(self.NOTES)
            scale_notes.append(self.NOTES[curr_note_index])
        
        return scale_notes

    def scale_name(self):
        scale_types = ["major", "minor"]
        return f'{self.root} {scale_types[self.type]}'

    def freq(self, note):
        assert note in self.NOTES
        return self.OCTAVE[note]

    def freqs(self):
        freqs = []
        for note in self.scale():
            freqs.append(self.freq(note))

        return freqs


if __name__ == '__main__':
    root = input("Please enter a root note ")
    type = int(input("Type 1 for major, 0 for minor "))
    scale = Scale(root, type)
    print(scale.scale())
    print(scale.freq('A'))

