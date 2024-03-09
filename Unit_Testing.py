import math
import utils
import unittest


def calc():
    p = []
    pinemv = []
    file = open("points.txt", "r") # Reads From File #
    x = 0
    while x < 100:
        firstLine = file.readline()
        p.extend(
            firstLine.split()
        )  # https://stackoverflow.com/questions/55978736/how-do-i-read-in-numbers-separated-with-whitespace-from-a-file#
        x = x + 1

    point = []
    c = 0
    while c < 200:
        ppp = int(p[c])
        point.insert(c, ppp)
        c = c + 1

    n = len(point)
    x = 0
    y = 0
    z = 0
    emvada = []
    semvada = []
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

    n = len(emvada)
    print("Dekta Trigwna:", n)
    semvada = utils.taksin(n, emvada)
    mo = utils.mo(n, semvada)
    print("Mesos oros", mo)
    di = utils.diam(n, semvada)
    print("Diamesos", di)
    ta = utils.apokl(n, semvada)
    print("Typikh apoklish", ta)
    file.close()
    return n, mo, di, ta # Returns Multiple Values #


class Test_C_points(unittest.TestCase):
    def test(self):
        cou, avg, dim, typ = calc() # cou = n, avf = mo, dim = di, typ = ta #
        self.assertEqual(cou, 161673)
        self.assertEqual(avg, 3206.82)
        self.assertEqual(dim, 2392.5)
        self.assertEqual(typ, 2843.25)


if __name__ == "__main__":
    unittest.main()

# Code by: Eleftherios Condromatidis #
