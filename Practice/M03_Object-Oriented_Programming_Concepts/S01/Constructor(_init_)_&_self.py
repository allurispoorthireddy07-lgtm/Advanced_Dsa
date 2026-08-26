#count no.of objects created for a class
class A:
    count = 0
    def __init__(self,r):
        self.r = r
    def Area(self):
        return 3.14 * self.r * self.r
    def perimeter(self):
        return 2 * 3.14 * self.r
