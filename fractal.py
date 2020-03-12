from vpython import *
import os

if os.name == "posix":
    scene = canvas(width=950, height=1870)
else:
    scene = canvas(width=1500, height=690)

def recu(arr, c):
    arr2 = []
    cl = color.hsv_to_rgb(vec(c/28%1, 1, 1))
    for i in arr:
        arr2.append(box(pos=i.pos-i.axis/2, size=i.size*3/4, color=cl))
        #arr2.append(box(pos=i.axis-i.pos/2, size=i.size/2, color=cl))
    return arr2

fb = [box()]
c = 0

while True:
    ev = scene.waitfor('mousedown mouseup')
    if ev.event == 'mousedown':
        fb = recu(fb, c)
        c += 1