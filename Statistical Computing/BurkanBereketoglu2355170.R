# Question 1

# Part A 
a <- seq(20,100,20)
print(a)
# Part B
b <- seq(-10, 5,0.5)
print(b)
# Part C
c <- seq(from = 12, to = -6,
         length.out = 7)
print(c)
# Part D 
d <- seq(0.01, 0.09, 0.02)
print(d)
# Part G 
g <- rep(x = seq(10,40,by = 10), times = 4)
print(g)
# Part H
h <- rep(1:3,times = 1,each = 7)
print(h)
# Part I
i <- rep(x = seq(10,60,by = 10),
         times = c(rep(1:2, times = 3 ,each = 1)))
print(i)
# Part J 
j <- rep(1:4,times = 3, each = 2)
print(j)

# Question 2

# Part A
A <- sum(1:50)
print(A)

# Part B
B <- sum(1/(10:20))
print(B)

# Part C
C <- sum((exp(-0.5)*((0.5)**(1:10)))/factorial(1:10))
print(C)

# Part D
D <- sum(((-1)**(1:20))*((1:20)**2))
print(D)

# Question 3

# Part A
matrix <- matrix(c(5,3,7,0,5,1,6,9,5,1,5,3),
                 nrow = 3, ncol= 4,
                 byrow = FALSE,
                 dimnames = list(c("r.1","r.2","r.3"),
                                 c("c.1","c.2","c.3","c.4")))
matrix

# Part B

newRow <- c(5,1,7,0)
matrix <- rbind(newRow, matrix)

print(matrix)

# Part C
fifth_column <- matrix[4,]*(-1)
matrix <- cbind(fifth_column, matrix)

print(matrix)

# extra for q3
rownames(matrix) <- c("r.1","r.2","r.3","r.4")
colnames(matrix) <- c("c.1","c.2","c.3","c.4","c.5")

print(matrix)

# Question 4

# Preliminaries

vec1 <- c(1:10)
vec2 <- seq(10, 60, by= 10)
vec3 <- c("Red", "Blue", "Yellow", "Green", "Black")
vec4 <- c(-1,-2,10,20,-3,-4,30,40,-5,50)

# Part A

q4.a <- c(vec1,vec2)

print(q4.a)

# Part B
q4.b <- vector()
q4.b <- c(q4.a[which((q4.a %% 3) == 0)])
q4.b
# This is the methods taught in the class

## Extra for part B
### This part is extra, but gives same thing.
q4.b <- vector()
q4.b
for(numero in q4.a){
  if(any(numero %% 3 == 0)){
    q4.b <- append(q4.b, numero)
  }
}
q4.b

# Part C
q4.c <- vector()
q4.c <- c(vec4[which(vec4 < 0)],vec3)
q4.c

# Part D
q4.d <- vector()
q4.d <- c(vec1[(seq(1,length(vec1),by =2))],vec3[(seq(2,length(vec3),by =2))])
q4.d

# Part E
length(which(vec3 == "Red"))
# or 
table(vec3[which(vec3 == "Red")])

# Question 5

# Preliminary
matrix_A <- matrix(c(4,3,-5,-1),
                   nrow = 2, ncol = 2)
matrix_B <- matrix(c(8,1,1,-6),
                   nrow = 2, ncol = 2)
matrix_C <- matrix(c(0,-2,1,4),
                   nrow = 2, ncol = 2)
matrix_D <- matrix(c(2,2,1,0),
                   nrow = 2, ncol = 2)

# Part A
det(matrix_C) # so can have inverse
result <- t(matrix_A) + matrix_B %*% solve(matrix_C)
result

# Part B
determinants <- sort(c(det(matrix_A),
                  det(matrix_B),
                  det(matrix_C),
                  det(matrix_D)),
                  decreasing = TRUE)

print(determinants)

# Part C
matrix_E <- matrix(c(cbind(rbind(matrix_A,matrix_B),
                           rbind(matrix_C,matrix_D))),
                   nrow = 4, ncol = 4)
matrix_E

# Part D

result_mean <- mean(matrix_E[,3])
print(result_mean)

# Part E
diag(matrix_E) <- rep(0, times = 4)

matrix_E

###### END ########
