def insertion_sort(A):
    for k in range(1, len(A)): # from 1 to n-1
        cur = A[k] # current element to be inserted
        j = k # find correct index j for current
        while j > 0 and A[j-1] > cur: # element A[j-1] must be after current
            A[j] = A[j-1]
            j -= 1
        A[j] = cur

def merge(S1, S2, S):
    i = j = 0
    while i+j <len(S):
        if j == len(S2) or (i<len(S1) and S1[i]<S2[j]):
            S[i+j] = S1[i]
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1
def merge_sort(S):
    n = len(S)
    if n<2:
        return
    mid = n//2
    S1 = S[0:mid]
    S2 = S[mid:n]
    merge_sort(S1)
    merge_sort(S2)
    merge(S1,S2,S)


def smart_sort(x):
    from array import array
    try:
        if type(x) == list:
            for i in range(len(x)-1):
                if type(x[i]) != type(x[i+1]):
                    return x
        if(len(x)<50):
            insertion_sort(x)
        else:
            merge_sort(x)
    except:
        return

