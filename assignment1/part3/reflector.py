

class Reflector:
    def __init__(self, alphabet, keys):
        self.alphabet = alphabet
        self.keys = keys

    def lefttoright(self, i):
        ch = self.keys[i]
        return self.alphabet.index(ch)