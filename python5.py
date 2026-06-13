#lists in python

marks = [94.4, 71.2, 86.9, 96.9, 64.6]
print(marks)
print(type(marks))
print(marks[0])#marks[0]=94.4

student = ["Gagandeep", 85, "Davanagere"]#list can store elements of different types(integer,float ,string,etc)
print(student)
print(student[0])
student[0] = "Rudra naik"
print(student)

# list slicing
marks = [99, 100, 88, 65, 50, 64]
print(marks[ : 4])
print(marks[-4 : -1 ])

#list method
list = [2, 1, 3]
list.append(4)
print(list)

list = [3, 1, 2]
list.sort()
print(list)

list =["banna","apple","mango"]
list.sort(reverse=True)
print(list)

list = ["a","b","c","d"]
list.reverse()
print(list)#["d","c","b","a"]


list = [1, 2, 3, 5]
list.insert(3,4)
print(list)#[1,2,3,4,5]

list = [1,2,3,4,5,5]
list.remove(1)# removes the first occurance of element 
print(list)#[2,3,4,5,5]

list = [1, 2, 3, 4, 8, 5]
list.pop(4)#removes element at index
print(list)#[1, 2, 3, 4, 5]

# Tuples in python
tup = ("gagan",)
print(tup)
print(type(tup))

#slicing of tuple 
tup = (1, 2, 3, 4, 5,)
print(tup[1 : 4])


#methods in touple

tup = (4, 5, 6, 7, 8)
print(tup.index(4))# we have to give elements it will give index 


tup = ("Gagandeep R Naik shanthinagara")
print(tup.count("g"))#2


# WAP to ask the user to enter names of their 3 favorite movies & store them in a list
movies = []
movie1 = str(input("enter the name of first movie : "))
movie2 = str(input("enter the name of second movie : "))
movie3 = str(input("enter the name of third movie : "))


movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print(movies)


# or
movies = []

movies.append(str(input("enter your first movie name")))
movies.append(str(input("enter your second movie name")))
movies.append(str(input("enter your third movie name")))


#WAP to check if a list contains a palindrome of elements .(Hint: use copy()method )

list1 = [1, 2, 2]
list2 = [1, 2, 3,]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("it is a palindrome")

else:
    print ("it is not palindrome")


# WAP to count the number of students with the "A" grade

grade = ("A", "B", "C", "A", "C", "A", "D")
grade.count("A")
print(grade.count("A"))

grade = ["A", "B", "C", "A", "C", "A", "D"]
grade.sort()
print(grade)






