from vpython import *
vc = vector

class Cubie:
    def __init__(self):
        pass

#compound

a = vertex( pos=vec(0,0,0), color=color.blue)
b = vertex( pos=vec(1,0,0), color=color.red)
c = vertex( pos=vec(1,1,0), color=color.red)
d = vertex( pos=vec(0,1,0), color=color.red)
Q = quad( vs=[a,b,c,d])

#arrow(pos=b.pos, axis=vc(1,0,0))

#redbox=box(pos=vc(4,2,3),
#           size=vc(8,4,6),color=color.red)

'''list = [box(pos=vc(i, j, k), size=vc(0.75, 0.75, 0.75)) for k in range(3) for j in range(3) for i in range(3) if i!=1 or j!=1 or k!=1]

for b in list:
    print(b.pos)

while 1:
    pass'''
