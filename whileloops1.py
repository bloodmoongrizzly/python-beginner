###This is a For Loop ( is more like a automatic transmission)

##for x in range (0,5):
##    print ("Hello")


###This is a While loop ( is more like a manual transmission )
import time
##x=5
##while x > 0:
##    print("Hello",x)
##    x -=1
##    time.sleep(1)
##   ### if x is less than five but will add 1 to x
##print("done with the loop.")
###If i use end="" to the end of the print "hello",x line it will not do returns it will make it one contunius line text
kaiju=['Godzilla','Mothra','Rhodan','Gamera']
print ("\n RUN... It's ",  end="")
index=0
while index < len (kaiju):
    print("%s! " % kaiju [index])
    index+=1
    time.sleep (1)
          
