class Employee:
    def __init__(self, newName, newSalary):
        self.name=newName
        self.salary=newSalary

    def displayEmployee(self):
        print("Name:", self.name,"Salary:$",self.salary)

class Manager(Employee):
    def __init__(self, newName, newSalary, newDept):
        self.department=newDept
        Employee.__init__(self, newName, newSalary)

    def displayManager(self):
        self.displayEmployee()
        print(self.name,"manages",self.department)

     ##New class for Stormtrooper
class Trooper(Employee):
    def __init__(self, newName, newSalary, newDept, newLine, newStatus):
        self.department=newDept
        self.line=newLine
        self.status=newStatus
        Employee.__init__(self,newName,newSalary)

    def displayTrooper(self):
        self.displayEmployee()        
        print(self.name, "Trooper in", self.department, self.line, self.status)

        
Luke=Employee("Luke",2000)
Luke.displayEmployee()
Han=Employee("Han",3000)
Han.displayEmployee()

Darth=Manager ("Darth", 4500,"Death Star")
Darth.displayEmployee()
Darth.displayManager()
## Our poor StormTroopers
George=Trooper("Trooper 4983,", 750, "501st Legion,","*These are not the droids we are looking for*,", "Fired")
George.displayEmployee()
George.displayTrooper()

Lucus=Trooper("Trooper 6658,",400,"501st Legion,","**Move along**,", "Probation")
Lucus.displayEmployee()
Lucus.displayTrooper()
