

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
class Enigma:
    def __init__(self, slow, med ,fast, ref, plugb):
        self.slow = slow
        self.med = med
        self.fast = fast
        self.ref = ref
        self.plugb = plugb

    def setKeys(self, a, b, c ):
        self.slow.rotate(int(a))
        self.med.rotate(int(b))
        self.fast.rotate(int(c))

    def setRings(self, a, b, c):
        self.slow.setRing(a)
        self.med.setRing(b)
        self.fast.setRing(c)

    def setplugs(self, list):
        for ss in list:
            self.plugb.add_plug(ss[0], ss[1])

    def encrypt(self, msg):
        out = ""
        for ch in msg:
            if(ch in alphabet):
                i = alphabet.index(self.plugb.keys[ch])
                if (self.fast.pos == self.fast.notch and self.med.pos == self.med.notch):
                    self.med.rotate()
                    self.slow.rotate()

                elif (self.fast.pos == self.fast.notch):
                    self.med.rotate()

                self.fast.rotate()

                i = self.fast.lefttoright(i)
                i = self.med.lefttoright(i)
                i = self.slow.lefttoright(i)

                i = self.ref.lefttoright(i)

                i = self.slow.righttoleft(i)
                i = self.med.righttoleft(i)
                i = self.fast.righttoleft(i)

                out += self.plugb.keys[alphabet[i]]
            else:
                out += ch

        return out