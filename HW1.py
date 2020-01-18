import numpy as np
import matplotlib.pyplot as plt


# Function definitions
def g(x):
    return (np.log(x))/(1+x)

def gprime(x):
    return (1+(1/x) - np.log(x))/((1+x)**2)

def bisection(x, a, b, tol):
    num_iterations = 0
    max_iterations = 1000
    a0 = a
    b0 = b
    
    # check the condition holds to continue the loop
    while ((abs(gprime(x)) > tol) and (num_iterations < max_iterations)):
        # check that condition holds for intermediate value theorem
        if gprime(a)*gprime(b) > 0:
            print("Bisection method fails.")
            return
        
        # if this does not fail, then we can test other conditions
        if gprime(a)*gprime(x) <= 0:
            a = a
            b = x
        elif gprime(a)*gprime(x) > 0:
            a = x
            b = b
        else:
            print("Something went wrong!")
            
        x = (a+b)/2;
        num_iterations+=1;
    
    # while loop has broken
    if num_iterations == max_iterations:
        print("Exceeded maximum number of iterations.")
        return
        
    else:
        print("Number of iterations: " + str(num_iterations))
        print("Final solution: " + str(x))
        
        


        
tol = 0.00000000001
bisection(3, 1, 5, tol)
