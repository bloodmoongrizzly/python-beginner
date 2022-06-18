worker={}

name=input("Enter a name: ")
number=int(input("Enter a phone number for %s: " % name))
worker[name]=number
print(worker)

name=input("Enter a name: ")
number=int(input("Enter a phone number for %s: " % name))
worker[name]=number
print(worker)

name=input("Enter a name: ")
number=int(input("Enter a phone number for %s: " % name))
worker[name]=number
print(worker)

lookingFor=(input("\n\nEnter Name of person to look up: "))
print("%s's phone number is %s." % (lookingFor,worker[lookingFor]))






