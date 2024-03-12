import math


def dis(x1, y1, x2, y2): # Calculates Distance between two points #
    ap = 0.0
    ap = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
    return ap


def semper(x, y, z): # Calculates the Semi-Perimeter #
    pe = 0.0
    ath = 0.0
    ath = x + y + z
    pe = ath / 2.0
    return pe


def iro(x, y, z, per): # Heron's Formula (It also checks for the possibility of the points not forming a proper triangle) #
    ap = 0.0
    pr = 0.0
    fail = -69
    pr = per * (per - x) * (per - y) * (per - z)
    if pr > 0.0:
        ap = math.sqrt(pr)
        return ap
    else:
        return fail 


def diam(megethos, pin): # Calculates Median #
    l = 0
    ll = 0
    med = 0.0
    fmed = 0.0
    modulo = math.remainder(megethos, 2)
    if modulo > 0.0:
        l = megethos / 2
        ll = int(l)
        med = pin[ll]
        return med
    if modulo == 0.0:
        l = megethos / 2
        ll = math.floor(l)
        at = pin[ll - 1] + pin[ll]
        med = at / 2.0
        fmed = round(med, 2)
        return fmed


def mo(megethos, pin): # Calculates Average #
    c = 0
    mesos_oros = 0.0
    c = sum(pin)
    mesos_oros = c / megethos
    fmesos_oros = round(mesos_oros, 2)
    return fmesos_oros


def rang(megethos, pin): # Calculates Range #
    c = 1
    megi = pin[0]
    mikr = pin[0]
    while c < megethos:
        if megi < pin[c]:
            megi = pin[c]

        if mikr > pin[c]:
            mikr = pin[c]
        c = c + 1
    ra = megi - mikr
    return ra


def apokl(megethos, pin): # Calculates Standard Deviation #
    afaireseis = []
    tetr = []
    pr = 0.0
    ap = 0.0
    diair = 0.0
    mesos = 0.0
    pr = sum(pin)
    mesos = pr / megethos
    c = 0
    while c < megethos:
        ka = abs(pin[c] - mesos)
        afaireseis.insert(c, ka)
        c = c + 1

    c = 0
    ka = 0.0
    while c < megethos:
        ka = afaireseis[c] * afaireseis[c]
        tetr.insert(c, ka)
        c = c + 1

    athroi = sum(tetr)
    new_meg = megethos - 1
    diair = athroi / new_meg
    ap = math.sqrt(diair)
    app = round(ap, 2)
    return app

# Code by: Eleftherios Chondromatidis #
