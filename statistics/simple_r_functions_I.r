
# Function

dice <- 1:6
dice

mean(dice)

sample(x = dice, size = 1)

args(sample)
?sample

sample(dice, 10, replace = FALSE)
#this doesn't happen because there are less than 10 values.

sample(dice, 10, replace = TRUE)

dice <- 1:6
dice <- sample(dice,2, replace = TRUE)
sum(dice)

# my_function() <- function(){}

rolldice <- function(){
  dice <- 1:6
  dices <- sample(dice, 2, replace = TRUE)
  sum(dices)
}
rolldice()

rolldices <- function(){
  dice <- 1:6
  dices <- sample(dice, 2, replace = TRUE)
  print(dices)
  sum(dices)
}
rolldices()

# Arguments

rolldice2 <- function(){
  dices <- sample(dices, 2, replace = TRUE)
  sum(dices)
}
rolldice2() # We didn't define dices yet

rolldice3 <- function(dices){
  dices <- sample(dices, 2, replace = TRUE)
  sum(dices)
}
rolldice3(dices = 1:6) #You can change it's value

#You can go furthermore

rolldice4 <- function(dices, x, y, z){
  dices <- sample(dices, 2, replace = TRUE)
  x <- sample(x, 2, replace = TRUE)
  y <- sample(y, 2, replace = TRUE)
  z <- sample(z, 2, replace = TRUE)
  sum(dices,x,y,z)
}
rolldice4(dices = 1:6, x = 2:4, y = 4:6, z = 5:10)

f <- function(x, y = 1, z = 2){x + y + z}
f()

f.formals <- formals(f)
f.formals

pizza <- formals(f)
pizza

f.formals$y <- 3
f.formals <- formals(f)
args(f)


addTheLog <- function(first, second){
  first + log(second)
}

addTheLog(second = exp(4), first = 1)

addTheLog(s = exp(4), f = 1)

addTheLog(1, exp(4))

# Example

# Fibonacci : 1, 1, 2, 3, 5, 8, 13, 21, ..., 150(if it passes 150 stop.)

myfib <- function(){
fib.a <- 1
fib.b <- 1
repeat{
  temp <- fib.a + fib.b
  fib.a <- fib.b
  fib.b <- temp
  cat(fib.a, "," , sep = "")
  if (fib.b > 150){
    cat("Break Now! \n")
    break
  }
}
}

myfib()


myfib2 <- function(thresh){
  fib.a <- 1
  fib.b <- 1
  cat(fib.a, "," , fib.b, "," , sep = "")
  repeat{
    temp <- fib.a + fib.b
    fib.a <- fib.b
    fib.b <- temp
    cat(fib.b, "," , sep = "")
    if (fib.b > thresh){
      cat("Break Now! \n")
      break
    }
  }
}

myfib2(thresh = 100000000)


dummy1 <- function(){
  aa <- 2.5
  bb <- "string me alone"
  cc <- "corona get out of here!"
  dd <- 4:8
  dd
}
dummy1()

dummy2 <- function(){
  aa <- 2.5
  bb <- "string me alone"
  cc <- "corona get out of here"
  dd <- 4:8
  return(dd)
}

dummy2()

fib <- function(thresh){
  thresh = scan()
  fib.a <- 1
  fib.b <- 1
  cat(fib.a, ",", fib.b, ",", sep = "")
  repeat{
    temp <- fib.a + fib.b
    fib.a <- fib.b
    fib.b <- temp
    cat(fib.b, "," , sep = "")
    if (fib.b > thresh){
      cat("Break Now! \n")
      break
    }
  }
}

fib(thresh)

dummy3 <- function(){
  aa <- 2.5
  bb <- "corona, I hate you!"
  return(aa)
  cc <- "hello corona"
  dd <- 4:8
  return(dd)
}
foo1 <- dummy3()
foo1

?scan

