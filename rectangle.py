class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def perimeter(self):
        self.p=2*(self.length+self.breadth)
        return self.p
    def area(self):
        self.a=self.length*self.breadth
        return self.a