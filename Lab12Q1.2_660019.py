
import random as rd

thaigoal_rate = 0.02
brazilgoal_rate = 0.10

thailost = 0
thaiwin = 0
thaipoint1 = 0
thailost_point1 = 0

for match in range(100000):
    thaigoals = 0
    brazilgoals = 0
    for min in range(90): 
        if (rd.random() < thaigoal_rate):
            thaigoals += 1
        if (rd.random() < brazilgoal_rate):
            brazilgoals += 1

    if (thaigoals >= 1):
        thaipoint1 += 1
    if (thaigoals > brazilgoals):
        thaiwin += 1
    if (thaigoals < brazilgoals):
        thailost += 1
    if (thaigoals >= 1 and thaigoals < brazilgoals):
        thailost_point1 += 1

print("-----------------match ", match + 1, "---------------------")
print("ทีมชาติไทยชนะทีมบราซิล: ", thaiwin, " ครั้ง")
print("ทีมชาติไทยแพ้ทีมบราซิล: ", thailost, " ครั้ง")
print("ทีมชาติไทยยิงประตูได้อย่างน้อย 1 ลูก: ", thaipoint1, " ครั้ง")
print("ทีมชาติไทยยิงประตูได้อย่างน้อย 1 ลูกแต่แพ้ทีมชาติบราซิล: ", thailost_point1, " ครั้ง \n")
print("สรุปโอกาส: ทีมชาติไทยแพ้ทีมบราซิล > ทีมชาติไทยยิงประตูได้อย่างน้อย 1 ลูก > ทีมชาติไทยยิงประตูได้อย่างน้อย 1 ลูกแต่แพ้ทีมชาติบราซิล >\n ทีมชาติไทยชนะทีมบราซิล")
