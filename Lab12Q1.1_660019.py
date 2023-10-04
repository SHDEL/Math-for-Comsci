import random
print("สุ่มโยนเหรียญ 100,000 ครั้ง หาโอกาสจากการทำซ้ำ 3 ครั้ง หาค่าเฉลี่ย")
cntPercent = 0
for i in range (3):
    x = 0
    cntH = 0
    cntT = 0
    cntHT = 0
    toss = 0
    face = ["H", "T"]
    for round in range(100000):
        if (toss == "H"):
            toss = random.choice(face)
            if (toss == "T"):
                cntHT += 1
        else : 
            toss = random.choice(face)
        # print(toss)
        if (toss == "H"):
            cntH += 1
        elif (toss == "T"):
            cntT += 1
        x += 1
        
    print("----------------Rounds ",i + 1,"-------------------")
    print("Head is: ", cntH)
    print("Tail is: ", cntT)
    print("H with T: " , cntHT)
    print("round" , x)
    percentH = (cntHT / cntH) * 100
    print("percent is: %.2f" %(percentH))
    cntPercent += percentH
avgPercent = cntPercent / 3
print("Average Paercent is: %.2f" %(avgPercent))