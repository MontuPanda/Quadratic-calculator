import matplotlib.pyplot as plt
import numpy as np
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
while True:
    a=(input("enter coefficient of x^2:"))
    if not isfloat(a):
        print("Invalid")
        continue
    else:
        a=float(a)
        break
while True:
    b=(input("enter coefficient of x:"))
    if not isfloat(b):
        print("Invalid")
        continue
    else:
        b=float(b)
        break
while True:
    c=(input("enter constant:"))
    if not isfloat(c):
        print("Invalid")
        continue
    else:
        c=float(c)
        break 
dis=(b*b)-(4*a*c)
if dis<0:
    print("No x-intercepts")
elif dis==0:
    rt=dis**(1/2)
    ans=-(b)/(2*a)
    print(f"There is one x-intercept : {ans}")
else:
    rt=dis**(1/2)
    posans=(-(b)+rt)/(2*a)
    negans=(-(b)-rt)/(2*a)
    print(f"There are 2 x=intercepts at : {posans} and {negans}")
x = np.linspace(-10, 10, 1000)
y = a*x**2+b*x+c  
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
