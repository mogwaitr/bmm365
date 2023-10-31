
class Plugboard:
    def __init__(self):
        self.keys = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I', 'J': 'J', 'K': 'K',
         'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V',
         'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z'}

    def add_plug(self, ch1, ch2):
        self.keys[ch1.upper()] = ch2.upper()
        self.keys[ch2.upper()] = ch1.upper()
