##for x in range (0,5):
##    print("Hello")
##x=0
##while x < 100:
##    print("hello",x,end="")
##    x += 1
##print("done with the loop")


##import time
##x=5
##while x > 0:
##    print ("Hello", x)
##    x -= 1
##    time.sleep(1)
##print("Done with the Loop.")

import time
kaiju=['Godzilla','Mothra','Rhodan','Gamera']

print("\n Run.. It's ",end="")
index=0
while index < len (kaiju):
    print("%s! " % kaiju[index], end="")
    index+=1
    time.sleep (1)
