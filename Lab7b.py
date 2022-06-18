import turtle
import time
t=turtle.Pen()

print("Answer me these questions three, era a python grade i'll see...")
shape=input("Which shape would you like to draw? (S)quare, (T)riangle, (R)ocket,(Q)uit: ")
if shape == "Q":
      quit()
else:
    x=int(input("Where would you like to start on the X axis? Please use -200 to 200:"))
    y=int(input("Where would you like to start on the Y axis? Please use -200 to 200:"))
    
def draw_square(length):
    for i in range (0,4):
        t.forward(length)
        t.right(90)

def draw_triangle (side_length):
    for i in range (0,3):
        t.forward (side_length)
        t.right (120)

def loop ():
    r=input ("Would you like to restart this program?")

    if r == "yes" or r == "y":
        print("OK, we'll continue...")
        time.sleep(1)
        t.clear()

    if r == "no" or r == "n":
        print ("Program terminating.  Good Bye.")
        quit()

while True:

    if shape =="S":
        t.up()
        t.setpos(x,y)
        t.down ()
        draw_square(100)
        loop()

    elif shape == "T":
        draw_triangle(200)
        loop()

    elif shape == "R":
        t.up()
        t.setpos(x,y)
        t.down()
    #tip
        t.backward (100)
        t.left(45)
        t.forward(100)
        t.right(90)
        t.forward(100)
        t.left(45)
        t.backward(41)
    #body 
        t.back(100)
        t.right(90)
        t.forward(200)
        t.left(90)
        t.forward(141)
        t.left(90)
        t.forward(200)
    #right fin
        t.backward(200)
        t.right (90)
        t.forward(30)
        t.left(135)
        t.forward(43)
        t.backward(43)
        t.right(135)
    #left fin
        t.backward(201)
        t.left(45)
        t.forward(43)
        t.hideturtle()
        loop()
    else:
        print ("Wrong key pressed.  Please try again")
  
            
