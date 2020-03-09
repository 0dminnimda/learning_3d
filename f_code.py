from vpython import *
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
    def __init__(self):
        list = []
        for k in range(3):
            for j in range(3):
                for i in range(3):
                    if i==1 and j==1 and k==1:
                        continue
                    list.append(make_cubelet([color.red, color.blue, color.green,
                        color.purple, color.yellow, color.cyan], pos = vec(i, j, k), size=0.8))

cu = Cube()

#while 1:
#    cu.pos.x+=0.000002

#arrow(pos=b.pos, axis=vc(1, 0, 0))
