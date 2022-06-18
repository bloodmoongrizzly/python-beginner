shape=input("What shape would you like to draw? a)square b) circle c)triangle :  ")
amt=int(input("How many do you want to make? "))
import turtle
import time
t=turtle.Pen()

def draw_square(t,length):
    for i in range (0,4):
        t.forward(length)
        t.right(90)

def draw_t(side_length):
    for i in range (0,3):
         t.forward(side_length)
         t.right (120)

##def suprise (side_lenth):
##    for i in range (0,12):
##        t.left (45)
##        t.forward (50)
##        t.right(90)
##        t.forward(50)
##        t.left(45)
         
    
if shape =="a":
    t.up()
    t.setpos (-100, 0)
    t.down()
    draw_square(t,100)

    for i in range (1,amt):
        t.up()
        t.forward (100)
        t.down()
        draw_square(t,100)

elif shape =="b":
    t.up()
    t.setpos(-200,0)
    t.down ()
    t.circle(100)
    
    for i in range (1,amt):
        t.circle (100)
        t.up()
        t.forward(200)
        t.down()
        t.circle(100)

elif shape=="c":
    t.up()
    t.setpos (-200,0)
    t.down()
    draw_t(100)

    for i in range (1,amt):
        t.up()
        t.forward (100)
        t.down()
        draw_t(100)


    
        
