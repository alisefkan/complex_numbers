from math import sin, cos, tan, sqrt, pi

#This class provides a complex number support for Python.
#The complex number can be defined in cartesian or polar representation.
#Basic operations such as addition, subtraction, multiplication, division, power and conjugation operations are implemented
#Complex power of complex numbers is not implemented

class ComplexNumber():
    def __init__(self,a,b,rep='cartesian') -> None:
        assert (type(a) is float) and (type(b) is float), "Inputs a and b have to be floats."
        assert (rep in ('cartesian','polar')), "Please provide one of the following for representation: cartesian , polar"
        if rep is 'cartesian':
            self.real = a
            self.img = b
            self.abs = sqrt(a**2 + b**2)
            if a is not 0:
                self.phase = tan(b/a)
            else:
                self.phase = pi/2 if b > 0 else -pi/2
        if rep is 'polar':
            self.abs = a
            self.phase = b
            self.real = a*cos(b)
            self.img = a*sin(b)
    def __add__(self,x):
        if type(x) is ComplexNumber:
            return ComplexNumber(self.real + x.real, self.img + x.img)
        elif type(x) in (float,int) :
            return ComplexNumber(self.real + x, self.img)
        else:
            print('This operation is not supported with complex number and', type(x))
    def __sub__(self,x):
        if type(x) is ComplexNumber:
            return ComplexNumber(self.real - x.real, self.img - x.img)
        elif type(x) in (float,int) :
            return ComplexNumber(self.real - x, self.img)
        else:
            print('This operation is not supported with complex number and ', type(x))
    def __mul__(self,x):
        if type(x) is ComplexNumber:
            return ComplexNumber(self.abs*x.abs,self.phase+x.phase,'polar')
        elif type(x) in (float,int) :
            return ComplexNumber(self.real * x, self.img * x)
        else:
            print('This operation is not supported with complex number and ', type(x))
    def __truediv__(self,x):
        if type(x) is ComplexNumber:
            return ComplexNumber(self.abs/x.abs,self.phase-x.phase,'polar')
        elif type(x) in (float,int) :
            return ComplexNumber(self.real / x, self.img / x)
        else:
            print('This operation is not supported with complex number and ', type(x))
    def __pow__(self,x): 
        if type(x) is ComplexNumber:
            raise NotImplementedError #this would require an approximation
        elif type(x) in (float,int) :
            return ComplexNumber(self.abs ** x, self.phase + x)
        else:
            print('This operation is not supported with complex number and ', type(x))      
    def __invert__(self): #conjugation
        self.img = -self.img
    def __eq__(self,x):
        try:
            return self.real == x.real and self.img == x.img
        except:
            if self.img == 0:
                return self.real == x
            else:
                return False
