shape = input("What shape would you like to draw? A) circle B) square or C)triangle?:  ")
amt=int(input("How many do you want to make? "))
if shape == "A":
    import turtle
    t=turtle.Pen()
   
    for i in range (1,amt):
        t.circle (100)
        t.up()
        t.right (90)
        t.forward(200)
        t.left(90)
        t.down()
        t.circle(100)

elif shape =="B":
    import turtle
    t=turtle.Pen()
    
    for i in range(1,amt):
       t.forward (100)
       t.left(90)
       t.forward(200)
       t.left(90)
       t.forward(200)
       t.left(90)
       t.forward(200)
       t.left(90)
       t.forward(100)
       t.right (90)
       t.up()
       t.forward(225)
       t.left(90)
       t.down()
       t.forward (100)
       t.left(90)
       t.forward(200)
       t.left(90)
       t.forward(200)
       t.left(90)
       t.forward(200)
       t.left(90)
       t.forward(100)

elif shape == "C":
    import turtle
    t=turtle.Pen()
    t.forward(100)
    t.backward(200)
    t.left(45)
    t.forward (140)
    t.right(90)
    t.forward(140)
    t.up()
    for i in range (1,amt):
        t.right(135)
        t.forward (100)
        t.left(90)
        t.forward(200)
        t.left(90)
        t.down()
        t.forward(100)
        t.backward(200)
        t.left(45)
        t.forward (140)
        t.right(90)
        t.forward(140)
        t.up()

else:
    print("Sorry you did not pick a vaild choice or you did not use a capital letter")


       
       
