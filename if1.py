items=int(input("How many items?"))
discQty=int(input("How many needed for discount?"))
print(items, "Items,", discQty, "to get discount")
saleStatus=input("Is this on sale? (y/n)")
ci=input("Is this an important customer?(y/n)")

if (items >= discQty and saleStatus =="n")or \
   (ci == "y"):
   print("You get the discount.")
   print("blah blah blah discount")
else:
    print("No discount.")

if discQty == items and saleStatus =="n":
        print("You barely qualified for the discount.")

if discQty != items:
    print("The item qty is different from disc qty.")

    
#29min  on video.
