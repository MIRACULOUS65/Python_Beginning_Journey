class Employee:
    company = "Google"  # class variable

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        #instance method (default)
    def print_info(self):
        info= f"The name is {self.name} and salary is {self.salary}"
        print(info)
#static method (without self)
    @staticmethod
    def sum(a,b):
        return a+b
    
    # class method (cls is used instead of self)
    @classmethod
    def print_company(cls):
        print(f"The company name is {cls.company}")

    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company
        
e1 = Employee("Jack",10000)
e2 = Employee("John",20000)
# print(e1.company)
# print(e2.company)
# print(Employee.company)

e1.print_info()
e2.print_info()

# e2.sum(5,6)  # this will give error coz even though self is not used it is still an instance method that is why it will expect an instance to be passed
# print(Employee.sum(5,6))  # this will work fine

#but now if we want to make sum method a static method we can do that by using @staticmethod decorator means without using self we can call it using class name or instance name
# static method

# print(e2.sum(50,6))  # this will work fine too

print(e1.company)
e1.print_company()
e1.change_company("Amazon")
print(e1.company)
print(Employee.company)