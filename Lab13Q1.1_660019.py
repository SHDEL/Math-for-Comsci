import random as rd

text = 66050019
m = rd.randint(1,100)
encrypt_list = []
decrypt_list = []

def encryptbyequal(x):
    y = (m * x) + text
    return y

def decrypt(p1 , p2):
    result = (p1[1] * ((-p2[0]) / (p1[0] - p2[0]))) + (p2[1] * ((-p1[0]) / (p2[0] - p1[0])))
    print("Decrypted text: " , result)

for x in range(1, 5):
    encrypt_list.append((x , encryptbyequal(x)))

for p in range(2):
    point = rd.randint(0, 3)
    decrypt_list.append(encrypt_list[point])

print("text to encrypt: " , text)
print("m value = " , m)
print("Encrypt by equal point: " , encrypt_list)
print("Select equal to decrypt: ", decrypt_list)
decrypt(decrypt_list[0], decrypt_list[1])
