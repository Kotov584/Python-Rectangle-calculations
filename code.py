class Rectangle(): 
    def __init__(self, length, width):
        self.length = length
        self.width  = width 
        
    def get_area(self):
        return self.width * self.length
    
    def get_perimeter(self):
        return 2 * (self.width + self.length)
    
    def vertical_orientation(self) -> bool: 
        return self.width > self.length
    
if __name__ == "__main__": 
    rectangle = Rectangle(123, 123)
    print(rectangle.get_area()) 
    
    
