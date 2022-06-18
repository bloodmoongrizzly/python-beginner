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
for row in stock:#reads the stock "list"
## when row  1 is greater than last price  it will turn the turtle line green
        x=int(row[0])# This will read row 0 in our stockindex
        y=int(row[1])# This will read row 1 in our stockindex
        if (y) > lastprice:# If the last price is greater then the last the line will turn green
                t.color("green")
               
        else:
     
                t.color("red")# if the last price is not greater than the last lne it will turn red
        lastprice = y
        t.setposition (x*4,y)#this moves the turtle along the x axis 4 pixles and y will move what last prices
                                               #number was

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
for x in range(15):

        t.forward(8)
        t.left(90)
        t.forward(5)
        t.backward(10)
        t.forward(5)
        t.right(90)

#lettering

t.up()
t.setposition (-45,40)
t.write ("Stock \n Index", font=("Arial", 12, "normal")) ##This will have turtle print normal typeset font
t.setposition(4,-25)
t.write("Day's", font=("Arial",12,"normal"))
        

        
