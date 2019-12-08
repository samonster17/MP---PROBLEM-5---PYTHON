#try np.sin(np.pi*3*n/100)
#sin(pi*3*n/100)
import matplotlib.pylab as plt
import numpy as np
from math import sqrt
from math import sin
from math import cos
from math import pi

n=np.linspace(0,198,199)   #Range
def x(n): 
     z=eval(xn)  
     return z 
xn=(input("Input Equation x(n): "))#xn=eq'n  
 
for nn in range(0,200):
     if nn == 0:                                    #1
        yn =(((-1.5)*x(n))+((2)*x(n+1))-((0.5)*x(n+2)))
     elif nn == 199:                                #2
        yn =((1.5)*x(n))-(2*x(n-1))+((0.5)* x(n-2))
     else:                                          #3
        yn = (((0.5) * x(n+1)) - ((0.5)*x(n-1)))

##plot
plt.plot(x(n),color="r")
plt.plot(yn,color="b")
plt.xlabel('x')
plt.ylabel('y')
plt.title('RED = X(n)     BLUE = Y(n)')
plt.show()
