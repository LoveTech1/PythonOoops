# importing math module to compute mathematical based terminologies
import math

# polygon class is an abstract class that doesn't contain any constructor
class Polygon:
    
    def get_area():
        raise NotImplementedError("Please provide logic for the get_area() method. ")
    
    def get_side():
        raise NotImplementedError("Please provide logic for the get_side() method. ")
    
    def get_perimeter(self):
        return sum(self.get_side())

# Triangle class inherits from the abstract class polygon
class Triangle(Polygon):
    def __init__(self, side1,side2,side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        
    def get_area(self):
        semiPerimeter = (self.side1 + self.side2 + self.side3) / 2
        
        return  math.sqrt(semiPerimeter * (semiPerimeter - self.side1) * (semiPerimeter - self.side2) * (semiPerimeter - self.side3))
        # return area

    def get_side(self):
        return [self.side1, self.side2, self.side3]        

# Rectangle class inherits from the abstract class Polygon and methods are overwritten
class Rectangle(Polygon):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        
    def get_area(self):
        # formula area = l * b
        return self.width * self.height

    def get_side(self):
        # adding the elements in the list that is initialized in instance and returning it
        length = []
        for i in range(2):
            length.append(self.width)
            length.append(self.height)
        return length
    
    # def get_perimeter(self):
    #     return 2*(self.width + self.height)

# square class is a subclass for the superclass Rectangle that inherits all the properties
class Square(Rectangle):
   def __init__(self,width_length):
       # inheriting all the methods of the super class rectangle
       super().__init__(width_length,width_length)
        
        
        
triangle = Triangle(2,5,6)
print(triangle.get_area())
print(triangle.get_side())   
rectangle = Rectangle(2,5)
print(rectangle.get_area())
print(rectangle.get_perimeter())
print(rectangle.get_side())
square = Square(4)
print(square.get_area())      
print(square.get_perimeter())
print(square.get_side())
print(Polygon.get_perimeter(1))
