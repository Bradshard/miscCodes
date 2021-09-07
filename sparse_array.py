class SparseArray(): # Sparse Array class

    def __init__(self, vals = 0):  # number of items in the array is defined.

        self._val = [0]*vals

    def __setitem__(self, i, x): # j is index and x is value.

        self._val[i] = x

    def __getitem__(self, i): # lets us getting items stored in index i

        return self._val[i] 

    def __str__(self): # use of string for string support

        return str(self._val)