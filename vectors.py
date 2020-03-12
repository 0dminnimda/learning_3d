from vpython import *
import os

if os.name == "posix":
    canvas(width=950, height=1870)
else:
    canvas(width=1500, height=690)

v = vec(1, 0, 0)
v1 = vec(0, 2, 0)

va = v + v1
vs = v - v1
vn = va.norm()

vd = dot(v, v1)
ad = diff_angle(v, v1)

vc = cross(v, v1)
vp = proj(v1, v)
vm = v.mag

print(ad, vm)

arrow(axis=v, color=color.white)
arrow(axis=v1, color=color.white)

arrow(axis=va, color=color.green, shaftwidth=0.09)
label(pos=va, text='1')
arrow(axis=vs, color=color.green, shaftwidth=0.09)
label(pos=vs, text='2')

arrow(axis=vn, color=color.red)
label(pos=vn, text='3')

arrow(axis=vc, color=color.blue)
label(pos=vc, text='4')
#arrow(axis=vp, color=color.blue)
#label(pos=vp, text='5')