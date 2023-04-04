
# STAT291 Lecture 2

10 + 7

getwd()

#setwd("/anything") sets directory to desired directory to work in.

# Basic Operations in R

pi
print(pi)
print(pi, "equals", 3.14)
print(pi); print("equals"); print(3.14)
cat(pi, "equals", 3.14, "\n") # cant print matrix etc.

cat(matrix(1:9, 3)) # see from the example no dimensions
print(matrix(1:9, 3)) # print is much better for one matrix visual

fib <- c(1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)
cat("My name is Fibonacci: ", fib, "...\n", "new line")
cat("My name is Fibonacci: ", fib, "...", "new line")

1:100

c(1, 1, 2, 3, 5, 8, 13, 21)

c(1*pi, 10*pi)
c("I", "love", "this", "course!")
c(TRUE, FALSE, FALSE, FALSE)

A <- c(1:3)
A
b <- c(4:6)
b
e <- c(A,b)
mode(e)


b <- c("O","D", "T", "U")
b
d <- c(A,b)
d

mode(d)
mode(pi)
mode(fib)

# Basic Operations in R

c(1, 0, 1, 2) + c(0,1,2,3)

c(1,0,1,2)*c(0,1,2,3)

c(1,0,1,2) - c(0,1,2,3)

c(1,2,3,4) + 1

c(1,2,3,4) + c(1,1,1,1)

1 / c(1,2,3,4)

c(1,2,3,4) + c(10,100)

c(1,2,3,4) + c(10,100,10,100)

v1 <- c(1:5)
v2 <- c(10:15)
v1 + v2

v1^v2

c("I love this course!", "R is a love at first sight!")

min(3,6,9)


# Setting, Listing and Deleting Variables

a <- 7
a
b <- 3
b
d <- sqrt(a^2 + b^2)
d

8 -> a # Do Not Prefer. Not that common. Regularly vector than object.
a

a = 9
a

ls()
ls.str()


rm(a)
ls()

ls()
rm(list = ls()) #Removes all.
ls()

# Sequence

#n:m >>> n, n+1, n+2, ... m

1:10

seq(from=1, to =5, by = 2) #from a starting point to a point by step size.

seq(1,5,2) #this also works
seq(1,100,20)

rep(1, times= 10) # repeat a point x times in this case 10 times.
rep(1,10)

rep(2,100)

10:0
10:20
v <- 3.5:9.5
v

seq(from = 0, to = 100, length.out = 5) # how many equal distanced items in a from to sequence

seq(from = 1, to = 2, length.out = 5)

seq(1,2,length.out = 5)#from to may not be used but can be.
# length.out needs to be specified since the regular order of
# sequence function is from to by ...

seq(2, 10, by = 2, length.out = 5) # Won't work too many arguments.

#Comparing Vectors

# ==, != , <, > returns boolean (True,False)


#ex
a <- 3
a == pi
a != pi
a < pi
a <= pi
a >= pi
a > pi

b <- c(3,pi,4)
d <- c(pi,pi,pi)
b == d
b != d
b < d
b <= d

b == pi

any(b == pi) # if any value in b equals then returns true.
all(b == pi) # iff all values are equal returns true.

# Sorting

v <- c(10:1, 5, 2.2, 3.5) # c is combine
v
sort(v)
sort(v, decreasing = TRUE) # makes decreasing sorting 
#data types in R

# character
# numeric (real or decimal)
# integer
# logical
# complex
# raw

# ----------

x <- "datamine"
x
class(x)
typeof(x)
attributes(x)
#attr get specific attribute of an object

y <- 1:20
y

typeof(y)
length(y)
z <- as.numeric(y)
typeof(z)
class(z) # look at the difference of typeof and class

# Data Structures

# atomic vector
# list
# matrix
# data frame
# factors

# Computing Basic Statistics

# mean(x)
# median(x)
# sd(x)
# var(x)
# cor(x, y) correlation
# cov(x, y) covariance

fib <- c(1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)
mean(fib)
median(fib)
sd(fib)
var(fib)

bif <- fib^2
bif
cor(fib, bif) # shows - checks is there correlation
cov(fib, bif) # shows - checks covariance value

v1 <- 1:5
v2 <- 10:15

mean(v1)
v1 - mean(v1)

fibbif <- c(fib, NA
            )
fibbif

mean(fibbif)# since we addedd na we should remove all na to look at mean

mean(fibbif, na.rm= TRUE) # as given here
fibbif # but we still do have na in the system for our convenience.

# Missing Data

a <- c(1:3, NA, 7)
a
b <- c(TRUE, FALSE, NA, FALSE)
b

is.na(a) #checks if its na and returns boolean.
anyNA(b) #checks if there exist any NA in the set
# returns boolean, if exist true and at not false.

1/0 # Inf == infinity
0/0 # NaN

# Some Help in R

help.start() # start help

help(sd) # for specific help 

args(mean) #shows arguments of that function
args(sd) #shows arguments of that function
example(mean) # gives example about the function
