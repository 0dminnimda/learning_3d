from vpython import *
from time import time as t
from math import sin, cos, tau
import os


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
            color.blue, color.orange, color.white,], size=0.7)
        cubl.visible = False

        # aray with 
        self.pts = [
            vec(i, j, k)
            for k in range(3) for j in range(3) for i in range(3)]
            #if i!=1 or j!=1 or k!=1]

        # array with cublits
        self.parts = [
            cubl.clone(pos=st_pt + pt)
            for pt in self.pts]

        self.pos = self.parts[0].pos
        self.st_pt = st_pt

        del cubl

        self.range = range(len(self.parts))

        inds = [i for i in range(27)]

        # F, S, B,   U, E, D,   L, M, R
        # referring to https://en.wikipedia.org/wiki/Rubik%27s_Cube
        # section: Solutions: Move notation
        nms = "F S B U E D L M R".split(" ")
        self.sides = {
            nms[0]:inds[-9:],
            nms[1]:inds[9:-9],
            nms[2]:inds[:9],
            nms[3]:inds[6::9] + inds[7::9] + inds[8::9],
            nms[4]:inds[3::9] + inds[4::9] + inds[5::9],
            nms[5]:inds[::9] + inds[1::9] + inds[2::9],
            nms[6]:inds[::3],
            nms[7]:inds[1::3],
            nms[8]:inds[::-3],
        }

    def set_pos(self, pos=None, x=0, y=0, z=0, ind=None):
        if ind is None:
            nums = self.range
        else:
            nums = ind
        for i in nums:
            if pos is not None:
                self.parts[i].pos = self.pts[i] + pos + self.st_pt
            else:
                self.parts[i].pos = self.pts[i] + vec(x, y, z) + self.st_pt

    def move(self, bias=None, x=0, y=0, z=0, ind=None):
        if bias is not None:
            self.set_pos(self.pos+bias, ind=ind)
        else:
            self.set_pos(self.pos+vec(x, y, z), ind=ind)

    def get(self):
        return compound(self.parts)

    def rot(self, ang=0, ind=None, axis=vec(0, 0, 1), origin=None):
        if ind is None:
            nums = self.rng
        else:
            nums = ind
        for i in nums:
            if origin is not None:
                self.parts[i].rotate(ang, axis=axis, origin=origin)
            else:
                self.parts[i].rotate(ang, axis=axis)

    def rot_side(self, name, ang=0, axis=vec(0, 0, 1)):
        nums = self.sides[name.upper()]
        mid = self.parts[nums[4]]
        for i in nums:
            self.parts[i].rotate(ang, axis=axis, origin=mid.pos)


def circ(ang, r=1):
    va = ang * tau
    x = r * cos(va)
    y = r * sin(va)
    return x, y

if os.name == "posix":
    canvas(width=950, height=1870, ambient = color.white)
else:
    canvas(width=1500, height=690, ambient = color.white)

st = vec(-1, -1, -1)
cu = Cube(st)
rot_ang = 0.005

for i in cu.range:
   label(pos=cu.parts[i].pos, text=f'{i}')


while 1:
    # rate(100)
    cu.rot_side("f", (radians(rot_ang)))

    #ob.rotate(radians(c))#, axis=vec(0, 0, 1), origin=vector(xo,yo,zo))
    pass
