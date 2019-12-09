#Programme for Spline interpolation....
#Name: Sagar Dam, Dept: DNAP

from scipy.interpolate import *
import matplotlib.pyplot as plt
import numpy as np

#inputing data points
x=[0,1,2,3,4,5]
y=[1.0,2.0,1.0,0.5,4.0,8.0]

#interpolating data and showing...
#interpolating linear spline
spl=InterpolatedUnivariateSpline(x,y,k=1)
plt.plot(x,y,'ro',ms=5)
xs = np.linspace(-0, 5, 1000)
plt.plot(xs, spl(xs), 'g', lw=3, alpha=0.7)
plt.title('Interpolation LINEAR Spline')
plt.show()

#interpolating quadratic spline
spl=InterpolatedUnivariateSpline(x,y,k=2)
plt.plot(x,y,'ro',ms=5)
xs = np.linspace(-0, 5, 1000)
plt.plot(xs, spl(xs), 'y', lw=3, alpha=0.7)
plt.title('Interpolation QUADRATIC Spline')
plt.show()

#interpolating cubic spline
spl=InterpolatedUnivariateSpline(x,y,k=3)
plt.plot(x,y,'ro',ms=5)
xs = np.linspace(-0, 5, 1000)
plt.plot(xs, spl(xs), 'b', lw=3, alpha=0.7)
plt.title('Interpolation CUBIC Spline')
plt.show()

#Lagrange Interpolation
poly = lagrange(x, y)
plt.plot(x,y,'b+',ms=20)
xs = np.linspace(-0, 5, 1000)
plt.plot(xs, poly(xs), 'r-', lw=3)
plt.title('Interpolation Lagrange')

plt.show()

#I have sent all the plots in a single graph after which I have modified the code to show them separately