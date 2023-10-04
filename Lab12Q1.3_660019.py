import random

for i in range (3):
    cnt = 0
    cnt2 = 0
    for round in range (100000):
        box_list = ["A", "B", "C"]
        win = random.choice(box_list)
        selectA = "A"
        box_list.remove("A")
        select2 = random.choice(box_list)
        if (selectA == win):
            cnt += 1
        elif (select2 == win):
            # print("change to: " + select2)
            cnt2 += 1
        # print(win)
    print("--------Round",i+1,"------")
    print("Win from select A: ",cnt)
    print("Win rate from select A: %.2f %s" %((cnt / 100000)*100 , "%"))
    print("Win from change box: ", cnt2)
    print("Win rate from change box: %.2f %s" %((cnt2 / 100000)*100 , "%"))
print("จากค่า win rate % ของทั้งหมด จะเห็นว่ามีโอกาสพอๆกัน \n ที่จะถูกรางวัลจากการเลือก A อย่างเดียวและเปลี่ยนกล่อง")


