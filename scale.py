#!/usr/local/bin/python3

# Goal is to print any scale(major or minor)
# given an input of the root note

# c_scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']
# c_minor_scale = ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#', 'C']

class Scale:
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 
             'F#', 'G', 'G#', 'A', 'A#', 'B']
 
    major_dists = [0, 2, 2, 1, 2, 2, 2, 1]
    minor_dists = [0, 2, 1, 2, 2, 1, 2, 2]

    major, minor = 1, 0

    def __init__(self, root, type):
        assert root in self.notes
        assert type in [0, 1]
        self.root = root
        self.type = type

    def target_dists(self):
        return self.major_dists if self.type == self.major \
				 else self.minor_dists

    def scale(self):
        scale_notes = []
        curr_note_index = self.notes.index(self.root)  

        for dist in self.target_dists():
            curr_note_index += dist
            curr_note_index %= len(self.notes)
            scale_notes.append(self.notes[curr_note_index])
        
        return scale_notes

    def scale_name(self):
        scale_types = ["major", "minor"]
        return f'{self.root} {scale_types[self.type]}'

if __name__ == '__main__':
    root = input("Please enter a root note ")
    type = int(input("Type 1 for major, 0 for minor "))
    scale = Scale(root, type)
    print(scale.scale())

