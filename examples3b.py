#Using variables and literals (fixed numbers and strings)
#   to store and update data in maps.
#
#Adding and updating look the same.
#
#Here, we're starting with a simple map
#   using a text key and integer value.

hobbyHrs={"Fred":0, "Scooby":0, "Velma":0}
print (hobbyHrs)

#Update the map.
#   key: quoted text
#    value: integer
hobbyHrs["Fred"]=5

print(hobbyHrs)

#Update the map.
#   key: variable containing text
#   value: integer
name=input("Which name to update?")
hobbyHrs[name]=7

print(hobbyHrs)

#Update the map.
#   key: quoted text
#   value: variable containing an integer
hours=int(input("How many hours for Fred?"))
hobbyHrs["Fred"]=hours

print(hobbyHrs)

#Update the map.
#   key: variable containing text
#   value: variable containing an integer
name=input("Which name to update?")
hours=int(input("How many hours for %s?" % name))
hobbyHrs[name]=hours

print(hobbyHrs)
