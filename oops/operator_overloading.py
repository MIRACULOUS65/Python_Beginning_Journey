class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def sum(self,other):  #operator overloading
        return point(self.x + other.x , self.y + other.y)
    
    def print_point(self):
        print(f"Point is ({self.x},{self.y})")

    def __add__(self,other):  #this is a special method in python to overload the + operator
        return point(self.x + other.x , self.y + other.y)


p1=point(2,3)
p2=point(4,5)

#p=p1.sum(p2)  

p=p1+p2 #p1+p2 will also work here because we have overloaded the + operator
p.print_point()