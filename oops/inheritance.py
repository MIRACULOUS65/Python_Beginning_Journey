class animal: #parent class (super class)
    location = "jungle"  #class variable
    def __init__(self,name):
        self.name = name

    def speak(self):
        print("Animal speaks")

class dog(animal): #child class (sub class) this is how inheritance is done in python
    def speak(self):  #overriding the method of the parent class
        super().speak()  #this will call the method of the parent class
        print(f"{self.name} barks")

a=dog("dog")
a.speak()
print(a.location)