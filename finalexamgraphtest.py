import turtle  #Imports turtle
import csv #imports csv files
import time # Lets you represent time in objects

stock=[]
print("Reading file into list....")
time.sleep (1)#makes the "program" pause for one second.
print("\n The data in the list....")
time.sleep(1)#pauses for 1 second
with open ("stockIndex.csv","r") as csvfile: # This make it so the file is read only
    csvreader=csv.reader (csvfile)


    for row in csvreader:  # this puts the info up into stock=[]
            stock.append(row)
           

    for row in stock:  # this takes the info put into stock=[] and has it print out the info contain with in.
        print("[", row[0], row[1], "]" , end="  " )


#drawing of the data
print ( "\n\nDrawing the data...")

#Setting up Turtle
t=turtle.Pen()
t.up()
t.setposition (0,100)

#Getting ready for stockmarket lines.
lastprice=int(0)
t.down()


###
for row in stock:
        x=int(row[0])
        y=int(row[1])
        if (y) > lastprice:
                t.color("green")
               
        else:
     
                t.color("red")
        lastprice = y
        t.setposition (x*10,y)

## Y axis line
t.color("black") #turns line color back to black
t.up()
t.setposition(0,0)
t.down()
t.left(90)
t.hideturtle()
t.setposition(0,0)

## for the y (stock index) lines I set it up to run a little more than double so the index goes by 10's
for y in range (20):
    
    t.forward(10)
    t.left(90)
    t.forward (5)
    t.backward(10)
    t.forward(5)
    t.right(90)


##X axis
t.up()
t.setposition(0,0)
t.down()
t.right(90)

## For the x (days) lines I set it up to run double the forward length so that way 15 will equal 30
for x in range(30):

        t.forward(10)
        t.left(90)
        t.forward(5)
        t.backward(10)
        t.forward(5)
        t.right(90)

#lettering

t.up()
t.setposition (-80,40)
t.write ("Stock \n Index", font=("Arial", 12, "normal")) ##This will have turtle print normal typeset font
t.setposition(4,-25)
t.write("Day's", font=("Arial",12,"normal"))
##stock index numbers        
t.up()
t.setposition(-30,195)
t.down()
t.color("purple")
t.write("200",font=("Arial",10,"normal"))
t.up()
t.setposition(-30,145)
t.down()
t.write("150",font=("Arial",10,"normal"))
t.up()
t.setposition(-30,90)
t.write("100",font=("Arial",10,"normal"))
t.up()
t.setposition(-30,40)
t.down()
t.write("50",font=("Arial",10,"normal"))
t.up()
t.setposition(-30,-10)
t.down()
t.write("0",font=("Arial",10,"normal"))
##days number
t.up()
t.setposition(300,-30)
t.down()
t.write("30",font=("Arial",10,"normal"))
t.up()
t.setposition(190,-30)
t.down()
t.write("20",font=("Arial",10,"normal"))
t.up()
t.setposition(90,-30)
t.down()
t.write("10",font=("Arial",10,"normal"))
