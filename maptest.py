#buliding a map

hobbies={
    'Fred':'traps',
    'Velma':'reading',
    'Daphnie':'fashion',
    'Shaggy':'eating',
    'Scooby':'eating'
    }
#print(hobbies['Velma'])

#hobbies['Mike']='Amphib Surverying'

print(hobbies)

#print("Mikes's hobby is", hobbies['Mike'])

inName=input("\n\nEnter a name: ")
inHobby=input("Enter a hobby: ")

hobbies[inName]=inHobby

print("\n\n",hobbies)

inName=input("Enter a name, I'll give you their hobby: ")
print("The hobby of",inName,"is",hobbies[inName])
