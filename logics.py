from random import choice

# F, S, B,   U, E, D,   L, M, R
# referring to https://en.wikipedia.org/wiki/Rubik%27s_Cube
# section: Solutions: Move notation
nms = "F S B U E D L M R".split(" ")
add = ["", "'"]

def scramble(num):
    global nms, add
    arr = []
    for i in range(num):
        arr.append(choice(nms)+choice(add))
    return arr



print(scramble(50))