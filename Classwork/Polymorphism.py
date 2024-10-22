
class shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Rectange(shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

def print_area(shape):
    print(f"The area is: {shape.area()}")


Circle = Circle(5)
Rectange = Rectange(4, 5)

print_area(Circle)
print_area(Rectange)