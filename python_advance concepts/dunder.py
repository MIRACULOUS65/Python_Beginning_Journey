class Employee:
    company = "Google"  # class variable

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"The name is {self.name} and salary is {self.salary}"
    
    def __repr__(self):
        return f"Employee:'{self.name}'\nSalary:{self.salary})"
    
    def __len__(self):
        return len(self.name)

e=Employee("Jack",10000)
print(e.name,e.salary)
print(str(e))  # this will print the memory location of the object
# but if we want to print the info of the object in a more readable format we can override the __str__ method
# __str__ method is a dunder method (double underscore method) it is a special method that is used to define the string representation of an object
# when we print an object it will call the __str__ method and return the string representation of the object

print(repr(e))  # this will print the memory location of the object
# but if we want to print the info of the object in a more detailed format we can override the __repr__ method
# __repr__ method is a dunder method (double underscore method) it is a special method that is used to define the official string representation of an object
# when we call repr() function it will call the __repr__ method and return the official string representation of the object
# __repr__ method is used for debugging and development purpose
print(len(e))  # this will print the length of the name of the employee
# but if we want to get the length of the name of the employee we can override the  __len__ method
# __len__ method is a dunder method (double underscore method) it is a special method that is used to define the length of an object
# when we call len() function it will call the __len__ method and return the length of the object