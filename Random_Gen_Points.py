import statistics
import random
import math
import utils

x = 0
y = 0
point = []
while x < 100:
    y = 0
    while y < 2:
        a = random.randint(-100, 100)
        b = random.randint(-100, 100)
        point.insert(x, a)
        point.insert(x + 1, b)
        y = y + 1
    x = x + 2
print("Coordinates Generated:", point)
n = len(point)
emvada = []
semvada = []
x = 0
y = 0
z = 0
count = 0
while x < n:
    y = x + 2
    while y < n:
        z = y + 2
        while z < n:
            ab = utils.dis(point[x], point[x + 1], point[y], point[y + 1])
            ac = utils.dis(point[x], point[x + 1], point[z], point[z + 1])
            bc = utils.dis(point[y], point[y + 1], point[z], point[z + 1])
            hmiper = utils.semper(ab, bc, ac)
            Heronas = utils.iro(ab, bc, ac, hmiper)
            if Heronas > 0.0:
                fix = round(Heronas, 2)
                emvada.insert(count, fix)
                count = count + 1
            z = z + 2
        y = y + 2
    x = x + 2

print("Number of Triangles:", count)
n = 0
n = len(emvada)
emvada.sort()
print("Statistics using custom functions (Max: Two decimal places)")
mo = utils.mo(n, emvada)
print("Average:", mo)
diames = utils.diam(n, emvada)
print("Median:", diames)
r = utils.rang(n, emvada)
print("Range:", r)
apoklish = utils.apokl(n, emvada)
print("Standard Deviation:", apoklish)
mo = 0.0
diames = 0.0
r = 0.0
apoklish = 0.0
print("Statistics using the Statistics module (Max: Two decimal places)")
mo = statistics.mean(emvada)
print("Average:", round(mo, 2))
diames = statistics.median(emvada)
print("Median:", round(diames, 2))
apoklish = statistics.stdev(emvada)
print("Standard Deviation:", round(apoklish, 2))

# CODE BY: ELEFTHERIOS CHONDROMATIDIS #
# 2024 #
