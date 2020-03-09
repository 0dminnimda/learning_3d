from vpython import *
from time import time as t
vc = vector

def make_side(pos_s=[vec(0, 0, 0) for _ in range(4)], col=color.white):
    return quad(vs=[
            vertex(pos=pos_s[0], color=col),
            vertex(pos=pos_s[1], color=col),
            vertex(pos=pos_s[2], color=col),
            vertex(pos=pos_s[3], color=col),])

def make_cubelet(col, pos=vec(0, 0, 0), size=1):
    # set points of sides
    sides = [
        [[0, 0, 0], [size, 0, 0], [size, size, 0], [0, size, 0]],
        [[0, 0, 0], [0, 0, size], [0, size, size], [0, size, 0]],
        [[0, 0, 0], [size, 0, 0], [size, 0, size], [0, 0, size]],

        [[0, 0, size], [size, 0, size], [size, size, size], [0, size, size]],
        [[size, 0, 0], [size, 0, size], [size, size, size], [size, size, 0]],
        [[0, size, 0], [size, size, 0], [size, size, size], [0, size, size]],
    ]

    for s in range(len(sides)):
        # turn points to "vec" and add start point
        for p in range(len(sides[s])):
            sides[s][p] = vec(*sides[s][p]) + pos

        # make list of sides
        sides[s] = make_side(sides[s], col[s])
    
    # compound all sides to one object
    return compound([side for side in sides])

class Cube:
    def __init__(self, st_pt=vec(0, 0, 0)):
        cubl = make_cubelet([color.green, color.red, color.yellow,
                        color.blue, color.orange, color.white,], size=0.8)
        cubl.visible = False

        self.list = [cubl.clone(pos=st_pt + vec(i, j, k))
                for k in range(3) for j in range(3) for i in range(3)
                if i!=1 or j!=1 or k!=1]

        del cubl

st = vec(-1, -1, -1)
cu = Cube(st)
#print([i.pos for i in cu.list])

#while 1:
#    cu.pos.x+=0.000002

#arrow(pos=b.pos, axis=vc(1, 0, 0))
