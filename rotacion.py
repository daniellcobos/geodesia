import numpy as np
import math

def dtohms(time):
    hours = int(time)
    minutes = (time * 60) % 60
    seconds = (time * 3600) % 60

    return "%d:%02d.%02d" % (hours, minutes, seconds)

def rotacion(angle, rot, a, b, c):
    r = np.array([a, b, c])
    r1 = np.array([[1, 0, 0], [0, math.cos(angle), -math.sin(angle)], [0, math.sin(angle), math.cos(angle)]])
    r2 = np.array([[math.cos(angle), 0, -math.sin(angle)], [0, 1, 0], [math.sin(angle), 0, math.cos(angle)]])
    r3 = np.array([[math.cos(angle), -math.sin(angle), 0], [math.sin(angle), math.cos(angle), 0], [0, 0, 1]])
    if rot == 1:
        return r1.dot(r)
    elif rot == 2:
        return r2.dot(r)
    elif rot == 3:
        return r3.dot(r)


def matrotacion(angle1, angle2, r1, r2):
    r1x = np.array([[1, 0, 0], [0, math.cos(angle1), -math.sin(angle1)], [0, math.sin(angle1), math.cos(angle1)]])
    r1y = np.array([[math.cos(angle1), 0, -math.sin(angle1)], [0, 1, 0], [math.sin(angle1), 0, math.cos(angle1)]])
    r1z = np.array([[math.cos(angle1), -math.sin(angle1), 0], [math.sin(angle1), math.cos(angle1), 0], [0, 0, 1]])
    r2x = np.array([[1, 0, 0], [0, math.cos(angle2), -math.sin(angle2)], [0, math.sin(angle2), math.cos(angle2)]])
    r2y = np.array([[math.cos(angle2), 0, -math.sin(angle2)], [0, 1, 0], [math.sin(angle2), 0, math.cos(angle2)]])
    r2z = np.array([[math.cos(angle2), -math.sin(angle2), 0], [math.sin(angle2), math.cos(angle2), 0], [0, 0, 1]])
    if r1 == 1:
        if r2 == 1:
            return r1x.dot(r2x)
        if r2 == 2:
            return r1x.dot(r2y)
        if r2 == 3:
            return r1x.dot(r2z)
    if r1 == 2:
        if r2 == 1:
            return r1y.dot(r2x)
        if r2 == 2:
            return r1y.dot(r2y)
        if r2 == 3:
            return r1y.dot(r2z)
    if r1 == 3:
         
        if r2 == 1:
            return r1z.dot(r2x)
        if r2 == 2:
            return r1z.dot(r2y)
        if r2 == 3:
            return r1z.dot(r2z)


def mat3rotacion(angle, rot, r):
    r1 = np.array([[1, 0, 0], [0, math.cos(angle), -math.sin(angle)], [0, math.sin(angle), math.cos(angle)]])
    r2 = np.array([[math.cos(angle), 0, -math.sin(angle)], [0, 1, 0], [math.sin(angle), 0, math.cos(angle)]])
    r3 = np.array([[math.cos(angle), -math.sin(angle), 0], [math.sin(angle), math.cos(angle), 0], [0, 0, 1]])
    if rot == 1:
        return r.dot(r1)
    elif rot == 2:
        return r.dot(r2)
    elif rot == 3:
        return r.dot(r3)


def rotsliw (sl, i, w):
    row1 = [(math.cos(sl)*math.cos(w)) - (math.sin(sl)*math.sin(w)*math.cos(i)),
            (-math.cos(sl)*math.sin(w))-(math.sin(sl)*math.cos(w)*math.cos(i)),
            (math.sin(sl)*math.sin(i))]
    row2 = [(math.sin(sl)*math.cos(w)) + (math.cos(sl)*math.sin(w)*math.cos(i)),
            (-math.sin(sl)*math.sin(w))+(math.cos(sl)*math.cos(w)*math.cos(i)),
            (-math.cos(sl)*math.sin(i))]
    row3 = [math.sin(w)*math.sin(i), math.cos(w)*math.sin(i), math.cos(i)]
    array = np.array([row1, row2, row3])
    return array


r313 = rotsliw(math.radians(300.2162), math.radians(55.5673), math.radians(285.0081))

xpl = np.array([[2.388334019], [3.410894469], [0]])
xe = r313.dot(xpl)



def matp(t):
    z = math.radians(((2306.2181/3600)*t) + ((1.09468/3600)*(t**2)) + ((0.018203/3600)*(t**3)))
    g = math.radians(((2004.3109/3600)*t) - ((0.42665/3600)*(t**2)) - ((0.041833/3600)*(t**3)))
    e = math.radians(((2306.2181/3600)*t) - ((0.30188/3600)*(t**2)) - ((0.017996/3600)*(t**3)))
    print(dtohms(math.degrees(z)))
    print(dtohms(math.degrees(g)))
    print(dtohms(math.degrees(e)))
    row1 = [(math.cos(z)*math.cos(g)*math.cos(-e)) - (math.sin(z)*math.sin(e)),
            (-math.cos(z)*math.cos(g)*math.sin(e))-(math.sin(z)*math.cos(e)),
            -math.cos(z)*math.sin(g)]
    row2 = [(math.sin(z)*math.cos(e)*math.cos(g)) + (math.cos(z)*math.cos(e)),
            (-math.sin(z)*math.sin(-e)*math.cos(g))+(math.cos(z)*math.cos(e)),
            (-math.sin(z)*math.sin(g))]
    row3 = [math.cos(e)*math.sin(g), math.sin(e)*-math.sin(g), math.cos(g)]
    array = np.array([row1, row2, row3])
    return array


rp = matp(0.20380)
xtrf = rp.dot(xe)
print(xe)
print(rp)
print(xtrf)
print(np.linalg.norm(xtrf))
print(np.linalg.norm(xtrf) * 6378137)




