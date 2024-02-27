import turtle as t
t.bgcolor("black")
t.pensize(2)
t.speed(10)
for i in range(6):
    for color in ("red","blue","cyan","white","yellow"):
        t.color(color)
        t.circle(100)
        t.left(30)
       

t.hideturtle()
t.mainloop()