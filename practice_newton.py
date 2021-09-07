def newton_method(func, derivative_func, x = 100, tolerance = 1.0e-6):
    func_val = func(x) # our function is given to an object.
    i_cout = 0 #iteration counter which should start at 0 since no iterations.
    while abs(func_val) > tolerance and i_cout < 30:
        try:
            dx = - float(func_val)/derivative_func(x) # real formula here step 1
            x = x + dx # real formula here step 2
        except ZeroDivisionError: #Special Exception Handling method.
            print ("Error! - derivative zero for x = ", x)
            sys.exit(1)     # System exit error given.
            # this function works to exit the while loop if there is division error
        func_val = func(x)
        i_cout += 1

    # if function still in iterating and exceeded 30 limit this increases the limit
    # else return the solution.
    if abs(func_val) > tolerance:
        i_cout = -1
    return x, i_cout

def func(x): #to get the function desired for the problem
    return x**4 - 6.4*x**3 + 6.45*x**2 + 20.538*x - 31.752

def derivative_func(x): # derivative of the function
    return 4*x**3 - 19.2*x**2 + 12.90*x + 20.538

real_soln = 4 # can be found by hand.

soln, number_of_i_cout = newton_method(func, derivative_func) # accepted tolerance rate and x value

if number_of_i_cout > 0:    # Solution found
    print ("%d" % (number_of_i_cout), "iterations made." )
    print (("Here is one solution: %f") % (soln))
    print("Ratio of real and found solution:","%", (round(soln,6)/real_soln)*100)
else:
    print ("Can't find a solution")