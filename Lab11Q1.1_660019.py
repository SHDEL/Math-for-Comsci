
print("----------Even or Odd Number--------")
num = 1
while num > 0:
    num = int(input("Enter number: "))
    if num < 0:
        print("Exit Program")
        break;
    elif (num % 2 == 0):
        print(num , "is Even number")
    else:
        print(num, "is Odd number")