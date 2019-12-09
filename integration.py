#Integration Program
#Name: Sagar Dam; Dept: DNAP
import numpy as np
from scipy import integrate

x= arange(0,1.0,0.00001)
y=exp(x)

#trapezoidal integral
I=np.trapz(y,x)
print("integration result using trapezoidal rule:  ",I)

#simpson integral
S=integrate.simps(y,x)
print("integration result using simpson rule:  ",S)

#Romberg integral
def f(t):
    return exp(t)
R=integrate.romberg(f,0,1)
print("the value of Romberg integral:  ",R)

#Gauss quadrature
G=integrate.fixed_quad(f,0,1,n=5)
print("integration result with 5th order Gauss quarrature:  ",G)