from vpython import *
vc = vector

#arrow(pos=b.pos, axis=vc(1,0,0))

#redbox=box(pos=vc(4,2,3),
#           size=vc(8,4,6),color=color.red)

list = [box(pos=vc(i, j, k), size=vc(0.75, 0.75, 0.75)) for k in range(3) for j in range(3) for i in range(3) if i!=1 or j!=1 or k!=1]

for b in list:
    print(b.pos)

while 1:
    pass
