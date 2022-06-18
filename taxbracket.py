agi=int(input("What is your Adjusted Gross Income?: $ "))
ms=input("What is your filing status (M)arried or (S)ingle?:  ")

if ms == "S" or "s":
    if agi <  10275:
        print("Your Single rate is at 10 %")
   

if ms =="S" or "s":
    if agi > 10275:
        print("Your Single rate is at 12 %")


   
