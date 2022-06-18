hobbyHrs={"Fred":0,"Scooby":0,"Velma":0}
print(hobbyHrs)

#name=input("Which name to update to 7?")
#hours=int (input("How many hours for Fred?"))
name=input("Which name to update? ")
hours=int (input("How many hours for %s? " % name))

hobbyHrs[name]=hours
print(hobbyHrs)         

#hobbyHrs["Fred"]=5
#print(hobbyHrs)         
