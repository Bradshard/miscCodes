# Data Frames

# Append data to vector

v <- c(1, 2, 3)
v
w <- c(5:8)

v <- c(v, w)
v

v[10] <- 10
v

append(1:20, 99, after = 10)

# Create a Factor

f <- factor(c("B", "I", "N", "G", "O", "O", "O"))
f

fgender <- factor(c("F", "M", "M", "M", "F"))
fgender

# Combine Multiple Vectors into One vector and A Factor

v1 <- c(1, 2, 3)
v2 <- c(4, 5, 6)
v3 <- c(7, 8, 9)

mycomb <- stack(list(v1 = v1, v2 = v2, v3 = v3))
mycomb
class(mycomb)

# Select List Elements by Position

years <- list(1881, 1919, 1923, 1938)
years

years[[1]]
years[c(1, 2)]
years[[1]]
years[1]
class(years[[1]])
class(years[1])

# Select List Elements by Name

years <- list(Birth = 1881, Samsun = 1919, Ankara = 1923, Death = 1938)
years
years[["Birth"]]
years$Samsun
years[1]

class(years[["Birth"]])
class(years["Birth"])
class(years[years$Samsun])

# Building a Name/Value Association List

mylist <- list(list(Birth = 1881, Samsun = 1919, Death = 1938))
mylist

mylist2 <- list()
mylist2

mylist2$left <- 0.25
mylist2$mid <- 0.50
mylist2$right <- 0.75
mylist2

values <- pnorm(-2:2)
names <- c("far_left", "left", "mid", "right", "far_right")
mylist3 <- list()
mylist3[names] <- values
mylist3

for (x in names(mylist3)) cat("The", x, "limit is", mylist3[[x]], "\n")

# Remove an element from a list
years <- list(Birth = 1881, Samsun = 1919, Ankara = 1923, Death = 1938)
years

years[[3]] <- NULL
years

years[["Samsun"]] <- NULL
years

years[c("Samsun", "Ankara")] <- NULL
years

# Flatten a list into a vector
mylist3
mean(mylist3)

mean(unlist(mylist))

cat(mylist3, "\n")

cat("Result", unlist(mylist3), "\n")

# Remove NULL elements from a list

mylist4 <- list("Sol", NULL, "Nol")
mylist4

sapply(mylist4, is.null)
mylist4[sapply(mylist4, is.null)]
mylist4[sapply(mylist4, is.null)] <- "Fall"

mylist4[sapply(mylist4, is.null)] <- NULL

# Remove list elements by a condition

mylist5 <- list("Sol", 0, "Nol")
mylist5

mylistt5[mylist5 == 0] <- NULL

mylist6 <- list(1:10, NA, NA, "peceteka")
mylist6

mylist6[is.na(mylist6)] <- NULL
mylist6


# Initializing a data frame from column data

v1 <- rnorm(10)
v2 <- rnorm(10)
v3 <- rnorm(10)
v4 <- rnorm(10)
mydtfrm <- data.frame(v1, v2, v3, v4)
mydtfrm
mydtfrm <- data.frame(var1 = v1, var2 = v2, var3 = v3, var4 = 4)
mydtfrm

v5 <- letters[1:10]
mydtfrm$names <- v5
mydtfrm

mylist8 <- list(var1 = v1, var2 = v2, var3 = v3, var4 = v4, names = v5)
mylist8

as.data.frame(mylist8)
