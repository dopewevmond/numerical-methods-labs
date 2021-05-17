# Euler method python program
# function to be solved
import math
def f(x,y):
    myexp = -4*x
    return 2-math.exp(myexp)-(2*y)
# Euler method
def euler(x0,y0,xn,n):
    # Calculating step size
    h = (xn-x0)/n
 
    print('\n-----------SOLUTION-----------')
    print(' ') 
    print('x0\ty0\tslope\tyn')
    print(' ')
    for i in range(n):
        slope = f(x0, y0)
        yn = y0 + h * slope
        print('%.4f\t%.4f\t%0.4f\t%.4f'% (x0,y0,slope,yn) )
        print('------------------------------')
        y0 = yn
        x0 = x0+h 
    print('\n ODE solution after %d iterations: x=%.4f, y=%.4f' %(step,xn,yn))

# Inputs
print('Enter initial conditions:')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))

print('Enter calculation point: ')
xn = float(input('xn = '))

print('Enter number of steps:')
step = int(input('Number of steps = '))

# Euler method call
euler(x0,y0,xn,step)