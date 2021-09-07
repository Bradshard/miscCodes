# task 1:8
class Vector:
    """Represent a vector in a multidimensional space."""
# task 8    
    def __init__(self, d):
        """Create n-dimensional vector of zeros."""
        if type(d)==int:
            self._coords = [0] * d
        else:
            try:
                self._coords = [0] * len(d)
                for i in range(len(d)):
                    self._coords[i] = d[i]
            except:
                raise TypeError("Please enter a sequence of numbers or integer.")
    
    def __len__(self):
        """ Return the dimension of the vector."""
        return len(self._coords)
    
    def __getitem__(self,j):
        """ Return jth coordinate of vector. """
        return self._coords[j]
    
    def __setitem__(self,j,val):
        """Set jth coordiante of vector to given value. """
        self._coords[j] = val
        
    def __add__(self, other):
        """ Return sum of two vectors."""
        if len(self) != len(other):             # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))              # start with vector of zeros.
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
# task 4
    def __radd__(self, other): # add is not enough for editing rvalues so that we used radd to edit rvalue as stated in the question and made __radd__ operator overloading.
        """ Return sum of two vectors."""
        if len(self) != len(other):             # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))              # start with vector of zeros.
        for j in range(len(self)):
            result[j] = other[j] + self[j]
        return result
# task 2
    def __sub__(self, other):
        """ Return substraction of two vectors."""
        if len(self) != len(other):             # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))              # start with vector of zeros.
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result
# task 3    
    def __neg__(self):
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = -(self[i])
        return result
# task 5 - 7   
    def __mul__(self,other):
        if(type(self)!=type(other)):
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = other*self[i]
            return result

        else:
            if(len(self) == len(other)):
                result = Vector(len(self))
                for i in range(len(self)):
                    result[i] = self[i]*other[i]
                return sum(result)
            
# task 6
    def __rmul__(self,other): # __mul__ doesn't satisfy right multiplications so we overload right by __rmul__.
        if(type(self)!=type(other)):
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = other*self[i]
            return result

        else:
            if(len(self) == len(other)):
                result = Vector(len(self))
                for i in range(len(self)):
                    result[i] = self[i]*other[i]
                return sum(result)
    
    def __eq__(self, other):
        """ Return True if vector has same coordinates as other. """
        return self._coords == other._coords
    
    def __ne__(self, other):
        """ Return True if vector differs from other. """
        return not self == other                 # rely on existing __eq__ definition
    
    def __str__(self):
        """ Produce string representation of vector. """
        return '<' + str(self._coords)[1:-1] + '>'    # adapt list representation.