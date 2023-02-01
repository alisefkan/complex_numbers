from math import sin, cos, tan, sqrt

class ComplexNumber():
    def __init__(self,a,b,rep='cartesian') -> None:
        assert (type(a) is float) and (type(b) is float), "Inputs a and b have to be floats."
        assert (rep in ('cartesian','polar')), "Please provide one of the following for representation: cartesian , polar"
        if type is 'cartesian':
            self.real = a
            self.img = b
            self.abs = sqrt(a**2 + b**2)
            self.phase = tan(b/a)
        if type is 'polar':
            self.abs = a
            self.phase = b
            self.real = a*cos(b)
            self.img = b*sin(b)
    def __add__(self,x):
        return ComplexNumber(self.real + x.real, self.img + x.img)
    def __sub__(self,x):
        return ComplexNumber(self.real - x.real, self.img - x.img)
    def __mul__(self,x):
        return ComplexNumber(self.abs*x.abs,self.phase+x.phase,'polar')
    def __truediv__(self,x):
        return ComplexNumber(self.abs/x.abs,self.phase-x.phase,'polar')
    def __pow__(self,x): 
        raise NotImplementedError #this would require an approximation
    def __invert__(self): #conjugation
        self.img = -self.img