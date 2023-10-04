import array as arr
print("***Welcomer to Binary and Decimal Convert Program***")
print("Press 1 to Convert Binary to Decimal")
print("Press 2 to Convert Decimal to Binary")
print("Press 0 to Exit Program")


def binaryToDecimal():
    print("---------------------------")
    print("Binary to Decimal")
    a = arr.array('i',[])
    d = int(input("Enter number of digits: "))
    for j in range(0, d):
        ele = int(input("Enter 1 or 0: "))
        a.append(ele)
    for i in a:
        print(i, end=" ")
    num = 2**(d-1)
    sum = 0
    for x in a:
        if (x == 1):
            x = num
            sum += x
        num /= 2
    print()
    print("Binary to Decimal is: " , sum)

def decimalToBinary():
    print("---------------------------")
    print("Decimal to Binary")
    
    num = int(input("Enter Decimal number: "))
    bilst = []
    x = len(bilst) - 1
    while num > 0:
        n = num % 2
        if (num == 0):
            break
        elif (n == 1):
            bilst.insert(x,1)
        elif (n == 0):
            bilst.insert(x,0)
        num //= 2
        x-=1
    for x in bilst:
        print(x , end=" ")
    
while True:
    inp = input("Press 1 or 2 or 0 : ")
    if (inp == "1"):
        binaryToDecimal()
        break
    elif (inp == "2"):
        decimalToBinary()
        break
    elif (inp == "0"):
        print("Exit Program...")
        break
    else:
        continue

