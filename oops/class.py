#class: class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
 
#object: object is an instance of a class. It is created using the class as a template and can have its own unique attributes and methods.

class employee:
    company = "Google"  #class variable

    def get_salary(self): #self is a reference to reference the object of the class which is being created
        return 34000
    
emp1 = employee()  #creating an object of the class employee
print(emp1.company)  #accessing class variable using the object
print(emp1.get_salary())  #accessing method using the object