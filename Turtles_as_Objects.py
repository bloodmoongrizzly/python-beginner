import turtle
t=turtle.Pen()
yert=turtle.Pen()
t.shape("turtle")
yert.shape("turtle")
t.color("green")
yert.color("blue")
t.up()
yert.up()
yert.back(50)
yert.left(90)  

for x in range (0,180):
    t.circle(100,10)
    yert.circle (100,10)
