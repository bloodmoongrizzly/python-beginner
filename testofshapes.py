shape=input("what kind of shape would you like to draw?  circle, square or triangle")
num=int(input("how many would you like to draw? "))
n=1
if shape =="circle":
    import turtle
    t=turtle.Pen()
    for i in range (0,num):
        t.circle(100)
        t.penup
        t.right(90)
        t.forward(100)
        t.left(90)
        t.pendown
        t.circle(100)
        
