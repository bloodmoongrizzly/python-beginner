##import turtle
##t=turtle.Pen()
##import time


###Text for Turtle output.
##t.color('blue')
##style = ('Courier', 15, 'bold')
##t.write("Answer me these questions three, ere a python grade i'll see....", font=style, align ='center')
##t.hideturtle()
##time.sleep(5)
##t.clear()
##shape=int(input("What would you like to draw?  (Square),  (T)riangle, (R)ocket, (Q)uit:"))

##import turtle
##angle = 91
##
##turtle.showturtle()
##turtle.shape("turtle")
##turtle.color("red","green","yellow","blue")
##for x in range(10000):
##    turtle.forward(x)
##    turtle.left(angle)
import turtle
import csv
import time
stock=[]
print("Reading file into list....")
time.sleep (1)#makes the "program" pause for one second.
print("\n The data in the list....")
time.sleep(1)
with open ("stockIndex.csv","r") as csvfile: # This make ti so the file is read only
    csvreader=csv.reader (csvfile)


    for row in csvreader:  # this puts the info up into stock=[]
            stock.append(row)
           

    for row in stock:  # this takes the info put into stock=[] and has it print out the info contain with in.
        print("[", row[0], row[1], "]" , end="  " )
print()
####
for i in range (len(stock)):
    print(i, stock [i], end=" ")
print()


