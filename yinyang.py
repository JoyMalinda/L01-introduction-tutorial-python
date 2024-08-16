import turtle as t

t.fillcolor('black')
t.begin_fill()
t.circle(120, 180)
t.end_fill()

t.circle(120, 180)

t.fillcolor("white")
t.begin_fill()
t.circle(60, 180)
t.end_fill()

t.penup()
t.right(90)
t.forward(120)
t.left(90)
t.pendown()

t.fillcolor("black")
t.begin_fill()
t.circle(60, 180)
t.end_fill()

t.penup()
t.left(90)
t.forward(40)
t.right(90)
t.pendown()

t.fillcolor("white")
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.right(90)
t.forward(80)
t.right(90)
t.pendown()

t.fillcolor("black")
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.forward(120)

t.exitonclick()