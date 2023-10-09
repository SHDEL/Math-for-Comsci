def key():
    # define p and q
    p = 43
    q = 59
    # define public key and private key
    n = p * q
    A = (p - 1) * (q - 1)
    E = 13
    D = 937
    print("Public Key: ", n, ",", E)
    print("Private key: ", p,"," ,q, ",", D)
    return n , E , D

def encrypt (data):
    print("text before encrypted: ", data)
    print("-----Encypted-----")
    ciphertext = []
    for i in range(len(data)):
        ciphertext.append(str((int(data[i]) ** E) % n))
    print("Cipher text: ",ciphertext)
    return ciphertext

def decrypt (data):
    print("-----Decrypted-----")
    plaintext = []
    for i in range(len(data)):
        plaintext.append(str((int(data[i]) ** D) % n))
    print("Plain text: ",plaintext)
    return plaintext

std_id = str(66050019)
# split
list = []
text = []
i = 0
while i < (len(std_id) - 1):
    list.append(std_id[i] + std_id[i + 1])
    i += 2
print(list)

# RSA process
n, E, D = key()
code = encrypt(list)
text_decrypt = decrypt(code)
