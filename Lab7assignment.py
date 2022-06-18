import turtle
import time
t=turtle.Pen()
t.color('blue')
style = ('Courier', 15, 'bold')
t.write("Answer me these questions three, ere a python grade i'll see....", font=style, align ='center')
t.hideturtle()
time.sleep(5)
t.clear()


shape=input("What would you like to draw?  (S)quare,  (T)riangle, (R)ocket, (Q)uit:")
if shape == "Q":
    quit()
else:
    x=int(input("Where would you like to start on the X axis? Please use -200 to 200: "))
    y=int(input("Where would you like to start on the Y axis? Please use -200 to 200: "))

    def draw_square(length):
        for i in range (0,4):
            t.forward (length)
            t.right (90)
        

    def draw_triangle (side_length):
        for i in range (0,3):
            t.forward (side_length)
            t.right (120)


    
##    def Loop ():
##        r= input("Would you like to restart this program?")
##
##        if r == "yes" or r == "y":
##            print("OK, we'll continue...")
##            time.sleep(1)
##     
##          
##        if r == "no" or r == "n":
##            print ("Program terminating. Good bye. " )
##            time.sleep(1)
##            quit()
##        


while True: 
        if shape == "S":
            t.up()
            t.setpos (x,y)
            t.down()
            draw_square(100)
            
    
        elif shape == "T":
            draw_triangle(200)
            

        else:
            print("You did not press the right key. Please try again")

        r= input("Would you like to restart this program?")

        if r == "yes" or r == "y":
            print("OK, we'll continue...")
            continue
        if r == "no" or r == "n":
            print ("Program terminating. Good bye. " )
            time.sleep(1)
            quit()
