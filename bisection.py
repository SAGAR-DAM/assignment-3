# root finding programme
# Name: Sagar Dam;  Dept: DNAP
from numpy import *

#defining f(x)
def f(x):
    return (sin(cos(exp(x))))

#bisection methode
#showing the root between +1 and -1:
from scipy import optimize
root = optimize.bisect(f, -1, 1)
print("The Root between +1 and -1 is:   ",root)

#matching with the result
r=sin(cos(exp(root)))
print()
print("The value of sin(cos(exp(",root,"))) is:  ",r)
print()
if r!=0:
    print("No The 2nd result is not zero... ")
    print("The result is not zero but is ~O(10^-12) and that is less than the usual machine precision. Moreover Newton Raphson gives an approximate result upto a particular order approximation. The value of sin(cos(exp(x)))is upto that precision. Using different algorithm to find the root more accurately, we can make this no closer to zero")
else:
    print("The 2nd result is zero")
    
#Newton methode with x(initial)=-0.1
root=optimize.newton(f,-0.1)
print("")
print("Solution with x=-0.1 as guess value is:   ",root)

#Newton methode with x(initial)=-1
root=optimize.newton(f,-1)
print("")
print("Solution with x=-0.1 as guess value is:   ",root)