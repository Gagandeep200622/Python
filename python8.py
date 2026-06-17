# loops in python
#for loop
nums = [1, 2, 3, 4, 5, ]

for val in nums:
    print(val)

veggies =("potato", "brijal", "ladyfinger", "cucumber")

for val in veggies:
    print(val)

str = "Gagandeep R Naik"

for char in str:
    print(char)
else:
    print("end")

#print the element of the following list using loop: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for val in nums:
    print(val)

# search for a number in this tuple using loop: (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100 , 49)

x = 49

idx = 0
for el in nums:
    if(el == x):
        print("numbers found at idx", idx)
        

    idx += 1



# range () in python

for i in range(10): # range(stop )
    print(i)


for i in range(1, 5): # range(start and stop )

    print(i)


for i in range(2, 10, 2): #range(start, stop, step)
    print(i)

# print the even numbers from 2 to 100 :

for i in range(2, 101, 2):
    print(i)

#print the numbers from 1 to 100

for i in range(1, 101):
    print(i)


# print from 100 to 1

for i in range(100, 0, -1):
    print(i)

# print the multiplicatrion. table of a number n.

n = int(input("enter a number : "))

for i in range(1, 11):
    print(n * i)

# pass statement

for i in range(10):
    pass

if i > 5:
    pass

print("hi Gagandee R Naik")

# write a programs to find the sum of first natural numbers( using while loop)


n = 10

sum = 0
i = 1
while i <= n:

    sum += i
    i += 1

print("total sum :" ,sum)

# write a program to find the factorial of first n numbers(using for)

n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
    print("factorial = " ,fact)



