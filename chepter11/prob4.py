# wa class 'complex' to repersent complex number, along with overloaded operators '+' and '*'
                    #A complex number is a number that has two parts:
                    # a real part and an imaginary part.

class complex:
     def __init__(self, real, imag):
        self.real = real
        self.imag = imag

     def __add__(self, other):
        return complex(self.real + other.real, self.imag + other.imag)
     def __mul__(self, other):                       #formula : (a+bi)(c+di)=ac+adi+bci+bdi2
        real_part = self.real * other.real - self.imag * other.imag  
        imag_part = self.real * other.imag + self.imag * other.real
        return complex(real_part, imag_part)
     def __str__(self):
        return f"{self.real} + {self.imag}i"

c = complex(1, 2)
c1 = complex(2,3)       
print(c +c1)      #output is : <__main__.complex object at 0x703af61384a0>  so we need to define __str__ method
print(c * c1)




