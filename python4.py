#string functions
str = "i am studying from apna college"
print(str.endswith("age"))#True
print(str.endswith("ag"))#False

str = "gagandeep "
print(str.capitalize())#Gagandeep

str = ('karnataka')
str = str.capitalize()
print(str)# changing of original string

str = "I am studying python from apna college"
print(str.replace("o","a"))#I am studying pythan fram apna callege
print(str.replace("python","java"))# I am studying java from apna college

str = ("I am studying python from apnacollege")
print(str.find("from"))#21

str = ("I am studying pyton from apna college")
print(str.count("a"))#3


 #practice qstions
#write a program to input user's first name and print its length
name = input("enter your name : ")
print("length of your name :",len(name))

#write a program to find the occarrence of '$' in a sting
str = " $ bought a laptop of $500"
print(str.count("$"))

#conditional statement
age = 21
if(age>= 18):
    print("can vote and apply for license")#can vote and apply for license

light = "Green"

if(light == "Green"):
    print("go")
elif(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
else:
    print("light is broken")   


num = 5 
if(num > 4):
    print ("True")
if (num > 1):
    print("True")
elif(num < 10):
    print(False)#it will not print because if condition is True .When if is false then only it will check elif statement


age = 17
if(age >= 18):
    print("can vote")#indentation
else:
    print("CANNOT VOTE")# CANNOT VOTE

#grade of student based on marks

marks = int(input(" enter your marks = "))
if(marks >= 90):
    Grade = "A"
elif(marks >= 80 and marks < 90):
    Grade = "B"
elif(marks >= 60 and marks < 90 ):
    Grade = "C"
else:
   Grade = "D"
print("Grade of the student : ",Grade  )   


#nesting
age = 34

if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:print("can drive")    

   
else:
    print("cannot drive ")


#write a program to check if a number is enterd by the user is odd or even 
num = int(input("enter the number : "))
rem = num % 2 
if(rem == 0):
    print("EVEN")
else:
    print("ODD")    
    
#WAP to find a greatest numbers enterd by the user

a = int(input("enter first number :"))
b = int(input("enter second number :"))
c = int(input("enter third number :"))    
if(a >= b and a >= c):
    print("first number is greatest number :",a)
elif(b > c and a < b):
    print("second number is largest number :", b)
else:
    print("third number is the largest number :")


# write a program to check if a number is a multipl of 7 or not 
   
x = int(input("enter a number :"))
if( x % 7 == 0):
    print("multiple of 7")
else:
    print("not a multiple of 7")
    










    


    

            

   
    







