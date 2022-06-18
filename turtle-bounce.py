import random
import turtle
t=turtle.Pen()

##while True:
##    t.forward(5)
##    x,y=t.position()
##    z=t.heading()
##    print(x,y,z)
##    if x > 200:
##        t.setheading(180)
##    if x < -200:
##        t.setheading(0)
while True:
    t.forward(5)
    x,y=t.position()
    z=t.heading()
    print(x,y,z)
    if x > 200:
        z=random.randint(110,250)
        t.setheading(z)
    if x < -200:
        z=random.randint(290,430)
        t.setheading(0)
    if y > 200:
     z=random.randint(200,340)
     t.setheading(z)
    if y < -200:
        z=random.randint(20,160)
        t.setheading(0)
 
