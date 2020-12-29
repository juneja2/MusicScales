#!/usr/local/bin/python3

import unittest
from scale import Scale

class TestScale(unittest.TestCase):
    def test_major_scales(self):
        c_major = "C, D, E, F, G, A, B, C".split(", ")
        d_major = "D, E, F#, G, A, B, C#, D".split(", ")
        f_sharp_major = "F#, G#, A#, B, C#, D#, F, F#".split(", ")
	
        self.check_cases([c_major, d_major, f_sharp_major],
			Scale.major)

    def test_minor_scales(self):
        a_minor = "A, B, C, D, E, F, G, A".split(", ")
        d_sharp_minor = "D#, F, F#, G#, A#, B, C#, D#".split(", ")
        g_sharp_minor = "G#, A#, B, C#, D#, E, F#, G#".split(", ")

        self.check_cases([a_minor, d_sharp_minor, g_sharp_minor],
			Scale.minor)

    def check_cases(self, test_cases, scale_type):
        for case in test_cases:
            scale_generator = Scale(case[0], scale_type)
            self.assertEqual(case, scale_generator.scale()) 

if __name__ == "__main__":
    unittest.main()
