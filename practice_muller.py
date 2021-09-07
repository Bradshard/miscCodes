import math

""" I recently learned that using * in import can sometimes mess things up if two classes overlap in a function.
For example log function both in numpy and scipy and solver. __name__ error occurs. """

tot_iter = 30
# We limit iterations due to our while loop continues.
  

def func(x): # to get the function
  
    return x**3 -1*x**2 -1*5*x - 3
  
def muller_method(guess_1, guess_2, guess_3): #mnemonic variables give intution
  
    result_of_f = 0
    i = 0
    while True:
      
        # Calculating various constants 
        # required to calculate x3
        func_1 = func(guess_1)
        func_2 = func(guess_2)
        func_3 = func(guess_3)
        d_0 = func_1 - func_3 
        d_1 = func_2 - func_3
        h_1 = guess_1 - guess_3
        h_2 = guess_2 - guess_3
        a_0 = func_3
        a_1 = (((d_1 * h_1**2) -(d_0 * h_2**2)) / ((h_1 * h_2) * (h_1 - h_2)))
        a_2 = (((d_0 * h_2) - (d_1 * h_1)) / ((h_1 * h_2) * (h_1 - h_2)))
        x = ((-2 * a_0) / (a_1 + abs(math.sqrt(a_1 * a_1 - 4 * a_0 * a_2))))
        y = ((-2 * a_0) / (a_1 - abs(math.sqrt(a_1 * a_1 - 4 * a_0 * a_2))))

#I chose the root closer to x2

        if (x >= y):
            result_of_f = x + guess_3
        else:
            result_of_f = y + guess_3
  
# Check x2 vs x3 similarity up to .001 significance
        t = result_of_f * 1000
        z = guess_3 * 1000 # after rounding down it makes equal values.

        t = math.floor(t) # Rounds number down to the neighboring integer.
        z = math.floor(z) # Rounds number down to the neighboring integer.
        if (t == z):
            break
        guess_1 = guess_2
        guess_2 = guess_3
        guess_3 = result_of_f
        if (i > tot_iter):
            print("No root is available to be able to found by Muller's method")
            break
        i += 1
    if (i <= tot_iter):
        print (("A solution is: %f") % (result_of_f))
        print("Ratio between root we found and the real one is ", "%", (round(result_of_f, 6)/root_inclined)*100)
        print(i,"iterations made.")
    return result_of_f
# initial guesses
# Pre-determined intuitively predicted gusses.
x0 = 0
x1 = 1
x2 = 2
root_inclined = 3 # It can be found by hand
muller_method(x0, x1, x2)