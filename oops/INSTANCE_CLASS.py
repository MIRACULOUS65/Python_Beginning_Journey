class employee:
    company = "Google"  #class attribute

    def __init__(self,salary,name,bond,company):  #constructor method, it is called automatically when an object of the class is created
        #print("Employee object is created")
        self.salary = salary  #instance variable
        self.name = name #instance variable
        self.bond = bond #instance variable
        self.company = company  #instance variable, can also be accessed as class variable



    def get_salary(self): #self is a reference to reference the object of the class which is being created
        return self.salary
    
    def get_name(self):
        return self.name
    
    def get_bond(self):
        return self.bond
    
    def get_info(self):
        print(f"Name of the employee is {self.name}. Salary of the employee is {self.salary} and bond of the employee is {self.bond} years.")
    
emp1 = employee(34000,"Sushovan",4,"Tesla")  #creating an object of the class employee

print(emp1.company)#it will always the instance attribute whenever present 
print(employee.company) #it will always show the class attribute
print(dir(emp1))  #it will show all the attributes and methods of the object emp1