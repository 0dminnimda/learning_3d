from vpython import *
vc = vector

def make_side(pos_s=[vec(0, 0, 0) for _ in range(4)], col=color.white):
        pts = [
            vertex(pos=pos_s[0], color=col),
            vertex(pos=pos_s[1], color=col),
            vertex(pos=pos_s[2], color=col),
            vertex(pos=pos_s[3], color=col),
        ]
        return quad(vs=pts)

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

    # turn points to "vec" and add start point
    for s in range(len(sides)):
        for p in range(len(sides[s])):
            sides[s][p] = vec(*sides[s][p]) + pos

    # make list of sides
    for s in range(len(sides)):
        sides[s] = make_side(sides[s], col[s])
    
    # compound all sides to one object
    return compound([side for side in sides])

class Cube:
    def __init__(self):
        list = [make_cubelet([color.red, color.blue, color.green, color.purple, color.yellow, color.cyan], pos=vec(i, j, k), size=0.75)
                for k in range(3) for j in range(3) for i in range(3)
                if i!=1 or j!=1 or k!=1]
        pass

#cu = make_cubelet([color.red, color.blue, color.green, color.purple, color.yellow, color.cyan])
cu = Cube()

#while 1:
#    cu.pos.x+=0.000002

#arrow(pos=b.pos, axis=vc(1, 0, 0))
