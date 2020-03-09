from vpython import *
from time import time as t


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
        cubl = make_cubelet([
            color.green, color.red, color.yellow,
            color.blue, color.orange, color.white,], size=0.8)
        cubl.visible = False

        self.pts = [
            vec(i, j, k)
            for k in range(3) for j in range(3) for i in range(3)
            if i!=1 or j!=1 or k!=1]

        self.parts = [
            cubl.clone(pos=st_pt + pt)
            for pt in self.pts]

        del cubl

        self.pos = self.parts[0].pos

    def set_pos(self, pos):
        for cubl in self.parts:
            cubl.pos = pos

    def move(self, bias=None, x=0, y=0, z=0):
        if bias is not None:
            self.set_pos(self.pos+bias)
        else:
            self.set_pos(self.pos+vec(x, y, z))

canvas(width=1500, height=690)

st = vec(-1, -1, -1)
cu = Cube(st)

while 1:
    pass#cu.set_pos(cu)
