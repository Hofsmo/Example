import csv
import os
a = "../data"
b = "blood_thirsty_janitors.csv"
with open(os.path.join(a, b)) as cf:
    r = csv.DictReader(cf)
    temp_1 = 0
    temp_2 = 0
    temp_3 = 0
    temp_4 = 0
    for rr in r:
        temp_1 += int(rr["beard length"])
        temp_2 += int(rr["churches burned"])
        temp_3 += int(rr["age"])
        temp_4 += 1
a_b_l = temp_1/temp_4
cbl = temp_2/temp_1
aa = temp_3/temp_4
print("Calculations done")
b = "evil_vikings.csv"
with open(os.path.join(a, b)) as cf:
    r = csv.DictReader(cf)
    temp_1 = 0
    temp_2 = 0
    temp_3 = 0
    temp_4 = 0
    for rr in r:
        temp_1 += int(rr["beard length"])
        temp_2 += int(rr["churches burned"])
        temp_3 += int(rr["age"])
        temp_4 += 1
a_b_l = temp_1/temp_4
cbl = temp_2/temp_1
aa = temp_3/temp_4
print("Calculations done")
b = "hungry_crusaders.csv"
with open(os.path.join(a, b)) as cf:
    r = csv.DictReader(cf)
    temp_1 = 0
    temp_2 = 0
    temp_3 = 0
    temp_4 = 0
    for rr in r:
        temp_1 += int(rr["beard length"])
        temp_2 += int(rr["churches burned"])
        temp_3 += int(rr["age"])
        temp_4 += 1
a_b_l = temp_1/temp_4
cbl = temp_2/temp_1
aa = temp_3/temp_4
print("Calculations done")
