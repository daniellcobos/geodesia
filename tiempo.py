import math
import rotacion


def dtohms(time):
    hours = int(time)
    minutes = (time * 60) % 60
    seconds = (time * 3600) % 60
    return "%d:%02d.%02d" % (hours, minutes, seconds)


def fj(year, month, day):
    a = math.floor(year/100)
    b = 2-a + math.floor(a/4)
    jd = math.floor(365.25*(year+4716)) + math.floor(30.6001*(month+1)) + day + b - 1524.5
    print( 'Dia juliano:' + str(jd))
    return jd


def tu(dayfraction):
    dfhours = dayfraction * 24
    tudf= dfhours * 1.002737909
    print('tu:' + str(dtohms(tudf)))
    return tudf


def tsg(year, month, day, dayfraction):
    pd = fj(year, month, day)
    tsg0 = 6.697374556 + (2400.051337*((pd-2451545)/36525))
    ph = tu(dayfraction)
    tsgt = tsg0 + ph
    today = tsgt - (int(tsgt/24) * 24) + ph
    angle = math.radians(today * 15)
    print('tsg0' + str(dtohms(tsg0)) )
    print('t: ' + str((pd-2451545)/36525))
    print('tiempo: ' + str(dtohms(today)))
    print('angulo: ' + str(dtohms(today*15)))
    return angle



