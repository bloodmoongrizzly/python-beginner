worker={"Steve":0,"Mike":0,"Pam":0}
print(worker)

worker["Mike"]=3604883126
print(worker)

name=input("Enter a name ")
worker[name]=855168
print(worker)

name=input("Enter a name: ")
number=int(input("Enter a phone number for %s: " % name))
worker[name]=number
print(worker)



##name=input("Enter a Name: ")
##number=int(input("Enter a phone number for  %s " % name))
##phonebook[name]=number
