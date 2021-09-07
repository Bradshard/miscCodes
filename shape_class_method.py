
from abc import abstractmethod
from math import pi as PI

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._p = (x,y)

class Shape:
    def __init__(self, P):
        self._leftTop = P
        self._plist = [self._leftTop]

    @abstractmethod
    def calculate_points(self):
        pass
    
    @abstractmethod
    def calculate_area(self):
        pass
    
    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

class Circle(Shape):
    def __init__(self,r,leftTop):
        self._r = r
        self._leftTop = leftTop
        super().__init__(leftTop)
        self.calculate_points()
        
    def calculate_points(self):
        bR = Point(self._leftTop._x + 2*self._r, self._leftTop._y + 2*self._r)
        List = [self._leftTop, bR]
        self._plist = List
        
    def calculate_area(self):
        return format((PI*self._r**2),'.2f')
    
    def calculate_perimeter(self):
        return format((2*PI*self._r),'.2f')
    
    def move(self, newlT):
        self._leftTop = newlT
        self.calculate_points()

class Rectangle(Shape):
    def __init__(self, h, w, leftTop):
        self._h = h
        self._w = w
        self._leftTop = leftTop
        super().__init__(leftTop)
        self.calculate_points()
        


    def calculate_points(self):
        my_x = self._leftTop._x
        my_y = self._leftTop._y
        rT = Point(my_x + self._w, my_y)
        bR = Point(rT._x, rT._y + self._h)
        bL = Point(my_x, my_y + self._h)
        List = [self._leftTop, rT, bR, bL]
        self._plist = List

    def calculate_area(self):
        return format((self._h*self._w),'.2f')
    
    def calculate_perimeter(self):
        return format((2*(self._w+self._h)),'.2f')
    
    def move(self,newlT):
        self._leftTop = newlT
        self.calculate_points()
        
while True:
    inp = input("Type of Shape (q for exit ): "'\n''\n')
    if inp =='r':
        inp2 = input("Coordinate height, width and ( leftTop ): ").strip().split()
        inp2 = [int(x) for x in inp2]
        R = Rectangle(inp2[2], inp2[3], Point(inp2[0], inp2[1]))
        print('\n' "--Rectangle--")
        print("Height:", inp2[2])
        print("Width:", inp2[3])
        print("Left Top Point:", (inp2[0],inp2[1]))
        print("Area:", R.calculate_area())
        print("Perimeter: ", R.calculate_perimeter())
        print("Points:", R._plist[0]._p, R._plist[1]._p, R._plist[2]._p, R._plist[3]._p,'\n')

        inp3 = input("Move object to the new coordinate ( leftTop ): ").strip().split()
        inp3 = [int(x) for x in inp3]
        R.move(Point(inp3[0],inp3[1]))
        print('\n' "--Rectangle--")
        print("Height:", inp2[2])
        print("Width:", inp2[3])
        print("Left Top Point:", (inp3[0],inp3[1]))
        print("Area:", R.calculate_area())
        print("Perimeter:", R.calculate_perimeter())
        R.calculate_points()
        print("Points:", R._plist[0]._p, R._plist[1]._p, R._plist[2]._p, R._plist[3]._p,'\n')

    elif inp == 'c':
        inp2 = input("Coordinate ( leftTop ) and radius: ").strip().split()
        inp2 = [int(x) for x in inp2]
        C = Circle(inp2[2], Point(inp2[0], inp2[1]))
        print('\n'"--Circle--")
        print("Radius:", inp2[2])
        print("Left Top Point:", (inp2[0],inp2[1]))
        print("Area:", C.calculate_area())
        print("Perimeter:", C.calculate_perimeter())
        print("Points:", C._plist[0]._p, C._plist[1]._p,'\n')

        inp3 = input("Move object to the new coordinate ( leftTop ): ").strip().split()
        inp3 = [int(x) for x in inp3]
        C.move(Point(inp3[0],inp3[1]))
        print('\n'"--Circle--")
        print("Radius:", inp2[2])
        print("Left Top Point:", (inp3[0],inp3[1]))
        print("Area:", C.calculate_area())
        print("Perimeter: ", C.calculate_perimeter())
        C.calculate_points()
        print("Points:", C._plist[0]._p, C._plist[1]._p,'\n')

    elif inp == 'q':
        break