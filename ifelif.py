shape = input("What shape would you like to draw? A) circle B) square or C)triangle?:  ")

if shape == "A":
    import turtle
    t=turtle.Pen()
    t.circle (100)
elif shape =="B":
    import turtle
    t=turtle.Pen()
    t.forward (100)
    t.backward (200)
    t.left (90)
    t.forward (200)
    t.right (90)
    t.forward (200)
    t.right (90)
    t.forward (200)
    t.up()
    t.forward(200)
elif shape == "C":
    import turtle
    t=turtle.Pen()
    t.forward(100)
    t.backward(200)
    t.left(45)
    t.forward (140)
    t.right(90)
    t.forward(140)
else:
    print("Sorry you did not pick a vaild choice or you did not use the capital letter")
