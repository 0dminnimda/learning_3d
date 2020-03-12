from vpython import *
import os

if os.name == "posix":
    scene = canvas(width=950, height=1870)
else:
    scene = canvas(width=1500, height=690)

def recu(boxes, whole, c):
    global ratio
    arr = []
    cl = color.hsv_to_rgb(vec(c/10%1, 1, 1))
    for i in boxes:
        arr.append(box(pos=i.pos-i.axis, size=i.size*ratio, color=cl))
        arr.append(box(pos=i.pos+i.axis, size=i.size*ratio, color=cl))
    comp = compound(boxes)
    boxes.clear()
    return arr, comp

boxes = [box()]
whole = None
c = 0
ratio = 1/2

while True:
    ev = scene.waitfor('mousedown mouseup')
    if ev.event == 'mousedown':
        boxes, whole = recu(boxes, whole, c)
        c += 1
        print(len(boxes) + 1)