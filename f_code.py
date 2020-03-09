from vpython import *
vc = vector

def make_side(pos_s=[vec(0,0,0) for _ in range(4)], col=color.white):
        pos_s = [vec(*i) for i in pos_s]
        pts = [
            vertex(pos=pos_s[0], color=col),
            vertex(pos=pos_s[1], color=col),
            vertex(pos=pos_s[2], color=col),
            vertex(pos=pos_s[3], color=col),
        ]
        return quad(vs=pts)

def make_cubie(box, col):
    sides = [
        make_side([(0,0,0), (1,0,0), (1,1,0), (0,1,0)], col[0]),
        make_side([(0,0,0), (0,0,1), (0,1,1), (0,1,0)], col[2]),
        make_side([(0,0,0), (1,0,0), (1,0,1), (0,0,1)], col[4]),

        make_side([(0,0,1), (1,0,1), (1,1,1), (0,1,1)], col[1]),
        make_side([(1,0,0), (1,0,1), (1,1,1), (1,1,0)], col[3]),
        make_side([(0,1,0), (1,1,0), (1,1,1), (0,1,1)], col[5]),
    ]
    return compound([side for side in sides])

cu = make_cubie(1, [color.red, color.blue, color.green, color.purple, color.yellow, color.cyan])

while 1:
    cu.pos.x+=0.000001

#compound

#arrow(pos=b.pos, axis=vc(1,0,0))

#redbox=box(pos=vc(4,2,3),
#           size=vc(8,4,6),color=color.red)

'''list = [box(pos=vc(i, j, k), size=vc(0.75, 0.75, 0.75)) for k in range(3) for j in range(3) for i in range(3) if i!=1 or j!=1 or k!=1]

for b in list:
    print(b.pos)

while 1:
    pass'''
