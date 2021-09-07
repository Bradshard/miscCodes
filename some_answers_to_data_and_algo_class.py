#Task 4***************
def reverseString(s):
    length = len(s)
    answer = ""
    for i in range(length-1,-1,-1):
        answer += s[i]
    return answer


#Task 5***************

#R-1.2
def is_even(k):
    k = abs(k)
    
    while(k > 0):
        k = k - 2
        
    if(k == 0):
        return True
    
    return False #k==-1


#R-1.6
def sumOfSquaresUntill(n):
    result = 0
    for i in range(1,n,2):
        result += i*i
    return result


#R-1.7
def sumOfSquaresWithSum(n):
    my_list = []
    for i in range(1,n,2):
        my_list.append(i**2)
    return sum(my_list)


#R-1.9
#Answer: range(50,81,10)
my_list = range(50,81,10)
for elem in my_list:
    print(elem)

print(" ") #just to get space between answers


#R-1.11
my_list = range(0,9,1)
answer = []
for i in my_list:
    answer.append(2**i)
print(answer)

print(" ") #just to get space between answers


#C-1.19 - I used ASCII codes here
my_list = range(97,123,1)
answer = []
for i in my_list:
    answer.append(chr(i))
print(answer)

print(" ") #just to get space between answers

#C-1.20 
from random import randint

def myShuffle(data):
    private_list = data.copy()
    length = len(private_list)
    answer = []
    while(length>0):
        num = randint(0,length-1)
        answer.append(private_list[num])
        del private_list[num]
        length-=1
    return answer

print(" ") #just to get space between answers

#C-1.28
def norm(v, p=2): #p norm of v, assume p=2 if p is not given
    answer = 0;
    for num in v: 
        answer+= abs(num)**p
    answer = answer ** (1.0/p)
    return answer
#Task 6***************
#P-1.35
from random import randint

my_list = range(5,101,5)

for n in my_list: #experimenting with each n
    #let us denote each day of the year with a single integer from 1 to 365
    birthdays = []
    found = False;
    for _ in range(0,n,1): #giving a random birthday to everyone
        if(found):
            break;
            
        bday = randint(1,365)
        if bday in birthdays: #there is a pair with the same birthday
            print("There was at least one pair of people with the same birthday in our experiment with n=" + str(n) + ".")
            found = True; #go to next experiment
        else:
            birthdays.append(bday)
            
    if(not found):        
        #no matching pair of birthdays were present
        print("There wasn't a pair of people with the same birthday in our experiment with n=" + str(n) + ".")

# e.g for task 7

l1 = [1,2,3,4,5]
l2 = []

while len(l1) != 0:
	l2.insert(len (l2), l1. pop (0))
	print(l2)


""" So the answer is the code takes the first element 
in the l1 list removes it from l1 and inserts it to ith index
in the l2 list, at the end l1 list is empty."""