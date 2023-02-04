from math import sin, cos, atan, sqrt, pi
import warnings

#This class provides a complex number support for Python.
#The complex number can be defined in cartesian or polar representation.
#Basic operations such as addition, subtraction, multiplication, division, power and conjugation operations are implemented
#Complex power of complex numbers is not implemented

class ComplexNumber():
    def __init__(self,a,b,rep='cartesian') -> None:
        assert (type(a) in (float,int)) and (type(b) in (float,int)), "Inputs a and b have to be floats."
        assert (rep in ('cartesian','polar')), "Please provide one of the following for representation: cartesian , polar"
        if rep == 'cartesian':
            self.real = a
            self.img = b
            self.abs = sqrt(a**2 + b**2)
            if a > 0:
                self.phase = atan(b/a)
            elif a==0:
                self.phase = pi/2 if b > 0 else -pi/2
            else:
                self.phase = atan(b/a) + pi
        if rep == 'polar':
            if a<0:
                warnings.warn('Absolute value cannot be negative. Positive value taken instead.')
                a=abs(a)
            self.abs = a
            if b>0:
                while(b>2*pi):
                    b-=2*pi
            else:
                while(b<-2*pi):
                    b+=2*pi
                
            self.phase = b
            self.real = a*cos(b)
            self.img = a*sin(b)
    def __add__(self,x):
        if type(x) is ComplexNumber:
            return ComplexNumber(self.real + x.real, self.img + x.img)
        elif type(x) in (float,int) :
            return ComplexNumber(self.real + x, self.img)
        else:
            raise TypeError('This operation is not supported with complex number and ' + str(type(x)))
    def __sub__(self,x):
        if type(x) is ComplexNumber:
            return ComplexNumber(self.real - x.real, self.img - x.img)
        elif type(x) in (float,int) :
            return ComplexNumber(self.real - x, self.img)
        else:
            raise TypeError('This operation is not supported with complex number and ' + str(type(x)))
    def __mul__(self,x):
        if type(x) is ComplexNumber:
            return ComplexNumber(abs(self.abs*x.abs),self.phase+x.phase,'polar')
        elif type(x) in (float,int) :
            return ComplexNumber(self.real * x, self.img * x)
        else:
            raise TypeError('This operation is not supported with complex number and ' + str(type(x)))
    def __truediv__(self,x):
        if type(x) is ComplexNumber:
            return ComplexNumber(self.abs/x.abs,self.phase-x.phase,'polar')
        elif type(x) in (float,int) :
            return ComplexNumber(self.real / x, self.img / x)
        else:
            raise TypeError('This operation is not supported with complex number and ' + str(type(x)))
    def __pow__(self,x): 
        if type(x) is ComplexNumber:
            raise NotImplementedError #this would require an approximation
        elif type(x) in (float,int) :
            return ComplexNumber(self.abs ** x, self.phase * x,'polar')
        else:
            raise TypeError('This operation is not supported with complex number and ' + str(type(x)))  
    def __invert__(self): #conjugation
        return ComplexNumber(self.real,-self.img)
    def __eq__(self,x):
        try:
            return abs(self.real - x.real)<1e-12 and abs(self.img - x.img)<1e-12
        except:
            if self.img == 0:
                return self.real == x
            else:
                return False
