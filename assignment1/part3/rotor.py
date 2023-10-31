
class Rotor:
    def __init__(self, alphabet, keys, notch, pos):
        self.alphabet = alphabet
        self.keys = list(keys)
        self.notch = notch
        self.pos = pos

    def rotate(self, n=1):
        self.pos = (self.pos + n) % 26

    def lefttoright(self, i):
        ch = self.keys[(i + self.pos)%26]
        return self.alphabet.index(ch) - self.pos

    def righttoleft(self, i):
        ch = self.alphabet[(i + self.pos)%26]

        return self.keys.index(ch) - self.pos

    def setRing(self, n):
        n -=1
        self.pos -=n


