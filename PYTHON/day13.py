class Mathfun():  
    def __init__(self, r, l , b, h):  
        print("Inside init function ")  
        self.r = r  
        self.l = l  
        self.b = b  
        self.h = h  
        self.area_circle()  
        self.area_square()  
    # class functions  
    def area_circle(self):  
        try:  
            out = 3.14 *self.r*self.r  
            print("inside __area_circle", out)  
        except Exception as e: print(e)  
    # class functions  
    def area_square(self):  
        """ area of square function with 3 arguments"""  
        try:  
            out = self.l*self.b*self.h  
            self.__area_circle(7)  
            print("inside area_square",out)  
        except Exception as e:  print(e)  
obj = Mathfun(5,4,3,2)  