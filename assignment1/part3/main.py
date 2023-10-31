import rotor
import reflector
import plugboard
import enigma
import sys

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


rotor1 = rotor.Rotor(alphabet, "EKMFLGDQVZNTOWYHXUSPAIBRCJ", alphabet.index("Q"), 0)
rotor2 = rotor.Rotor(alphabet, "AJDKSIRUXBLHWTMCQGZNPYFVOE", alphabet.index('E'), 0)
rotor3 = rotor.Rotor(alphabet, "BDFHJLCPRTXVZNYEIWGAKMUSQO", alphabet.index('V'), 0)
rotor4 = rotor.Rotor(alphabet, "ESOVPZJAYQUIRHXLNFTGKDCMWB", alphabet.index('J'), 0)
rotor5 = rotor.Rotor(alphabet, "VZBRGITYUPSDNHLXAWMJQOFECK", alphabet.index('Z'), 0)

reflector1 = reflector.Reflector(alphabet, "EJMZALYXVBWFCRQUONTSPIKHGD")
reflector2 = reflector.Reflector(alphabet, "YRUHQSLDPXNGOKMIEBFZCWVJAT")
reflector3 = reflector.Reflector(alphabet, "FVPJIAOYEDRZXWGCTKUQSBNMHL")

plugboard = plugboard.Plugboard()

settings = open(sys.argv[1], "r+")
line = settings.readline().rstrip('\n')
x = line.split("-")

if (x[0] == "I"):
    slow = rotor1
elif(x[0] == "II"):
    slow = rotor2
elif(x[0] == "III"):
    slow = rotor3
elif(x[0] == "IV"):
    slow = rotor4
elif(x[0] == "V"):
    slow = rotor5

if (x[1] == "I"):
    med = rotor1
elif(x[1] == "II"):
    med = rotor2
elif(x[1] == "III"):
    med = rotor3
elif(x[1] == "IV"):
    med = rotor4
elif(x[1] == "V"):
    med = rotor5

if (x[2] == "I"):
    fast = rotor1
elif(x[2] == "II"):
    fast = rotor2
elif(x[2] == "III"):
    fast = rotor3
elif(x[2] == "IV"):
    fast = rotor4
elif(x[2] == "V"):
    fast = rotor5

line = settings.readline().rstrip('\n')
if (line == "A"):
    ref = reflector1
elif(line == "B"):
    ref = reflector2
elif line == "C":
    ref = reflector3

enigma = enigma.Enigma(slow,med,fast, ref, plugboard)

line = settings.readline().rstrip('\n')

enigma.setKeys(alphabet.index(line[0]), alphabet.index(line[1]), alphabet.index(line[2]))

line = settings.readline().rstrip('\n')
x = line.split(",")

enigma.setRings(int(x[0]), int(x[1]), int(x[2]))

line = settings.readline().rstrip('\n')
x = line.split(" ")

enigma.setplugs(x)

settings.close()

messageFile = open(sys.argv[2], "r+")
message = messageFile.read().upper()
print(enigma.encrypt(message))
messageFile.close()