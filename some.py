from vpython import *

# create and tune canvas
scene = canvas(title='Examples of Tetrahedrons',
     width=1450, height=650,
     center=vector(0,0,0), background=color.cyan)

# activate canvas with box
box()

# create and tune canvas
scene2 = canvas(title='Examples of Tetrahedrons',
     width=1450, height=650,
     center=vector(0,0,0), background=color.cyan)

box()

# choise the current canvas for all subsequent objects
scene.select()

box(pos=vec(0, 2, 0))