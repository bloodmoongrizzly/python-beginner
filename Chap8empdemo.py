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

     

        
Luke=Employee("Luke",2000)
Luke.displayEmployee()
Han=Employee("Han",3000)
Han.displayEmployee()

Darth=Manager ("Darth", 4500,"Death Star")
Darth.displayEmployee()
Darth.displayManager()
