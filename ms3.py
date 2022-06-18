shape = input("What shape would you like to draw? A) circle B) square or C)triangle?:  ")
amt=int(input("How many do you want to make? "))
if shape == "A":
    for x in range(1,amt):
        import turtle
        t=turtle.Pen()
        t.circle (100)
        t.up()
        t.right (90)
        t.forward(200)
        t.left(90)
        t.down()
        t.circle(100)       
