import math
import rotacion

def fj(year, month, day):
    a = math.floor(year/100)
    b = 2-a + math.floor(a/4)
    jd = math.floor(365.25*(year+4716)) + math.floor(30.6001*(month+1)) + day + b - 1524.5
    return jd


def tu(dayfraction):
    dfhours = dayfraction * 24
    tudf= dfhours * 1.002737909
    return tudf


def tsg(year, month, day, dayfraction):
    pd = fj(year, month, day)
    tsg0 = 6.697374556 + (2400.051337*((pd-2451545)/36525))
    ph = tu(dayfraction)
    tsgt = tsg0 + ph
    today = tsgt - (round(tsgt/24) * 24) + 7.608277778
    angle = math.radians(today * 15)
    print(today)
    return angle

def rotsideral():
    return 'cad'


