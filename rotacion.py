import numpy as np
import math


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


print(matrotacion((np.pi/4), (np.pi/4), 1, 3))

