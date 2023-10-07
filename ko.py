n = 2537
e = 13
d = 937


def splitByStep(str, x):
    arr = []
    i = 0
    while i * x < len(str):
        arr.append(str[x * i : min(x * (i + 1), len(str))])
        i += 1

    return arr


def encrypt(it):
    ans_mod = 1
    for i in range(0, e):
        ans_mod = (ans_mod * it) % n
    return ans_mod


def decrypt(it):
    ans_mod = 1
    for i in range(0, d):
        ans_mod = (ans_mod * it) % n
    return ans_mod


stu_id = "741115"

ec = splitByStep(stu_id, 2)
print("เริ่มต้น =>", ec)
dc = []
for i in range(len(ec)):
    ec[i] = encrypt(int(ec[i]))
for i in ec:
    dc.append(decrypt(i))

print("---เข้ารหัส---")
for i in range(len(ec)):
    print("ตัวที่", (i + 1), "=", ec[i])

print("---ถอดรหัส---")
for i in range(len(dc)):
    print("ตัวที่", (i + 1), "=", dc[i])