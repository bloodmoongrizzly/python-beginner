#map
classHrs={"class1":0, "class2":0, "class3":0}

#How I get the information about hours into the map.
##This will ask the user for a number same goes for the other two sets of lines
hours1=int(input("How many hours a week should you spend on your first class?: "))
##This inputs the number up into the map for class1
classHrs['class1']=hours1

hours2=int(input("\nHow many hours a week should you spend on your second class?: "))
classHrs['class2']=hours2

hours3=int(input("\nHow many hours a week should you spend on your third class?: "))
classHrs['class3']=hours3


#This section is to do the math for the Variables.
##This first line will add all the hours up in classHrs.
totalCh=(classHrs["class1"]+classHrs["class2"]+classHrs["class3"])
##This section is for a new variable to be added to the equation.
days=int(input("\n\nHow many days per week do you plan to study?: "))
## This section is the variable to help see if you are putting in enough hours
hrsPi=int(input("\nHow many hours a day do you study?: "))
##This line will averge of the hours per day needed.  The totalCh divides the days
avgHrs=(totalCh/days)
##This will print out what your averge per day should be down to one decimal point
print("\nYou should spend a averge of %.1f a day studying." %(totalCh/days))

#This section is the if/else section if avgHrs is greater thatn the hrsPi (hours put in)
#the else line is for if the totalch is less than the hrsPi
if  avgHrs <= hrsPi:
    print("\n\nYou are probably studying enough")
else:
    print("\n\nYou should probably study some more each day.")

