import turtle
t=turtle.Pen()

t.setposition(0,0)
t.down()
t.left(90)
t.hideturtle()
t.setposition(0,0)

for x in range (20):
    
    t.forward(10)
    t.left(90)
    t.forward (5)
    t.backward(10)
    t.forward(5)
    t.right(90)
##    t.forward(10)
##    t.left(90)
##    t.forward (5)
##    t.backward(10)
##    t.forward(5)
##    t.right(90)

##X axis
t.up()
t.setposition(0,0)
t.down()
t.right(90)

for y in range(15):

        t.forward(8)
        t.left(90)
        t.forward(5)
        t.backward(10)
        t.forward(5)
        t.right(90)

#lettering
t.showturtle()
t.up()
t.setposition (-45,40)
t.write ("Stock \n Index", font=("Arial", 12, "normal"))
t.setposition(4,-25)
t.write("Day's", font=("Arial",12,"normal"))
