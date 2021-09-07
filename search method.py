
# Here is the find the biggest value.

def Search_method (values, l, r):
  
    # check whether len of array is bigger than 1.
    if r >= l:
  
        mid = l + r // 2
          
        # Right values
        if (values[mid] > values[mid+1]) and (values[mid] < values[mid-1]):
            return binarySearch(values, l, mid)
   
        # left values
        elif (values[mid] < values[mid+1]) and (values[mid] > values[mid-1]):
            return binarySearch(values, mid, r)

        else:
            return mid
  
    else:
        # For this case there won't be since it's a pseudocode for just this array.
        return False
  
# Our values
values = [12,17,38,54,55,69,68,44,39,19,14,7]


result = Search_method(values, 0, len(values)-1)
  
if True:
    print ("Element you picked is in the {} place, and it's value is {}. ".format(result+1, values[result]))
else:
    print ("No element in the system. ")