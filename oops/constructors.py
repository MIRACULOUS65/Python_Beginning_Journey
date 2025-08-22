class employee:
    
    def __init__(self,salary,name,bond):  #constructor method, it is called automatically when an object of the class is created
        #print("Employee object is created")
        self.salary = salary  #instance variable
        self.name = name #instance variable
        self.bond = bond #instance variable



    def get_salary(self): #self is a reference to reference the object of the class which is being created
        return self.salary
    
    def get_name(self):
        return self.name
    
    def get_bond(self):
        return self.bond
    
    def get_info(self):
        print(f"Name of the employee is {self.name}. Salary of the employee is {self.salary} and bond of the employee is {self.bond} years.")
    
emp1 = employee(34000,"Sushovan",4)  #creating an object of the class employee
print(emp1.get_salary())  #accessing method using the object
emp1.get_info()