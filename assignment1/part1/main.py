import sys

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]
def compute_cipher(n) :
    ciphered = []
    for i in range(26):
        ciphered.append(alphabet[i-n])

    return ciphered

def encrypt_char(alphabet, cipher,  ch) :
    if ch.islower():

        if ch.upper() in alphabet:
            i = alphabet.index(ch.upper())
            return(cipher[i].lower())
        else:
            return(ch)
    else:
        if ch in alphabet:
            i = alphabet.index(ch)
            return(cipher[i])
        else:
            return(ch)


def encrypt_str(alphabet, cipher, s) :
    ss = ""

    for i in range(len(s)):
        ss += encrypt_char(alphabet, cipher, s[i])
    return ss

def decrypt_str(alphabet, cipher, s):

    return encrypt_str(cipher,alphabet, s)

def encrypt_file(filename, alphabet, n):
    file1 = open(filename, "r+")
    cipher = compute_cipher(n)
    return encrypt_str(alphabet, cipher, file1.read())

def decrypt_file(filename, alphabet, n):
    file1 = open(filename, "r+")
    cipher = compute_cipher(n)
    return decrypt_str(alphabet, cipher, file1.read())

if(sys.argv[1] == "encrypt"):
    print(encrypt_file(sys.argv[2], alphabet, int(sys.argv[3])))
elif(sys.argv[1] == "decrypt"):
    print(decrypt_file(sys.argv[2], alphabet, int(sys.argv[3])))

