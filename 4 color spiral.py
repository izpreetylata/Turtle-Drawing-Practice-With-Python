import turtle
t=turtle.Pen()
turtle.bgcolor('Pink')
colors=['red','black','orange','yellow']
for x in range(150):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(91)
