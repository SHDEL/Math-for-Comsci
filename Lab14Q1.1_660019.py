import random as rd

def er_cor():
    pos = 11 - er_p
    if bit_list[pos] == 1:
        bit_list[pos] = 0
    else:
        bit_list[pos] = 1
    print("Corrected code :", *bit_list, sep="")

def detec():
    pos = 0
    for i in range(4):
        pos += check(2 ** i) * (2 ** i)
    print("error position :", pos)
    return pos

def rd_error():
    pos = rd.choice([0, 1, 2, 4, 5, 6, 8])
    if bit_list[pos] == 1:
        bit_list[pos] = 0
    else:
        bit_list[pos] = 1

def check(i):
    x = 11 - i
    sum = 0
    cnt = 0
    while x >= 0:
        if cnt == i:
            x -= i
            cnt = 0
            continue
        sum += bit_list[x]
        cnt += 1
        x -= 1
    return sum % 2

def hamming():
    bit_list.insert(3, 0)
    bit_list.insert(7, 0)
    bit_list.insert(9, 0)
    bit_list.insert(10, 0)
    bit_list[3] = check(8)
    bit_list[7] = check(4)
    bit_list[9] = check(2)
    bit_list[10] = check(1)
    print("Code :", * bit_list, sep="")
    

code = rd.randint(0,127)
binary_code = str(format(code, 'b'))

print(code)
print(binary_code)

bit_list = [0] * 7
for i in range(len(binary_code)):
    bit_list[i] = int(binary_code[i])

bit_list.reverse()
print(bit_list)

hamming()
rd_error()
er_p = detec()
er_cor()