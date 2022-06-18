import turtle
t=turtle.Pen()
print ("Drawing program")

def getInfo ():
    length=int (input("Length? (0 to stop): "))
    if length != 0:
         direction=int(input("Direction?: "))
    else:
            direction=0
    return(length, direction)

def drawLine(lngth,direct):
    t.setheading(direct)
    t.forward(lngth)

#get's information
length, direction=getInfo ()
#main program loop
while length != 0:
    #draw a line
    drawLine(length, direction)
    
    #gets infomation 
    length,direction=getInfo ()
