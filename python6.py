
## dictionary in python

info = {
    "name" : "Gagan",
    "subjects" : ["python","java","c"],
    "topics" : ("dict","set"),
    "age" : 20,
    "is_adult" : True,
    "marks" : 70.0
    
}
print(info)


info = {
    "name" : "Gagan",
    "subjects" : ["python","java","c"],
    "topics" : ("dict","set"),
    "age" : 20,
    "is_adult" : True,
    "marks" : 70.0
}
print(info["name"])
print(info["subjects"])
print(info["topics"])
print(info["is_adult"])
print(info["age"])
print(info["marks"])

info = {
   "name" : "Gagan",
   "subjects" : ["python","java","c"],
   "topics" : ("dict","set"),
   "age" : 20,
   "is_adult" : True,
   "marks" : 70.0
}

null_dict = {}
null_dict["district"] = "DAVANAGERE"
print(null_dict)
info["name"] = "NAIK"
info["subjects"] = "INDIAN ECONOMY", "HISTORY"
info["topics"] = "inflation, " "GDP"
info["village"] = "shanthinagara"
print(info)

# Nested dictionary
student = {
    "name" : "Gagandeep R Naik ",
    "subjects" : {
                "chem" : 88,
                "phy" : 78,
                "maths" : 92

    }
}
print(student)
print(student["subjects"])


# Dictionary Methods
student = {
  "name" : "Gagan",
   "subjects" : ["python","java","c"],
   "topics" : ("dict","set"),
    "age" : 20,
    "is_adult" : True,
    "marks" : 70.0
}

print(student.keys())
print(len(list(student.keys())) )

print(list(student.values()))

pairs =(list(student.items()) )
print(pairs[2])


print(student.get(("subjects")))

student.update({"city" : "Banglore"})
print(student)

student.update({"name" : "Rdra Naik"})
print(student)


    
#set in python ; sets are mutable ,but elements are immutable

nums = {1, 2, 3, 4, "Gagan", "shanthinagara" , 1,"Gagan"}#duplicate items are ignored
print(nums)
print(len(nums))#Total number of items

num = set() #empty set; syntax
print(type(num))

#methods os sets 
collection = set()
collection.add(1)
collection.add("Gagan")
collection.add(3)
collection.add("appa")
collection.add(2)
print(collection)

collection = {1, 2, 3,"Shsnthinagara"}
collection.remove(3)
print(collection)

set = {1, 2, 3, 4, "Gagan" }
set.clear()
print(set)

set = {1, 2, 3, 4, 5,"hello","gagan" }

print(set.pop())
print(set.pop())


collection1 = {"Gagan", "Shanthinagara",1, 2, 3, }
collection2= {"Rudra Naik","Lakshmi Bai" , 1, 2, 3, 4, 5, }
print(collection1.union(collection2))
print(collection1)
print(collection2)

set1 = {"Gagan", 1, 2, 3, 4, "shanthinagara"}
set2 = {5, 6, 7, 8, 9, "Gagan", "shanthinagara"}
print(set1.intersection(set2))

# practice
#store following word meanings in a python dictionary
# table : "a piece of furniture","list of facts & figures"
# cat : "a small animal"

dictionary = {
    "cat" : "a small animal",
     
       "table" :[ "a piece of furniture", "list of facts and figures"]
        
    }

print(dictionary)

## you are given a list of subjects for students. Assume one classroom is required for 1 subject.How many classroom are needed by all students
# #"python","java", "c++", "python", javascript,
# #"java", "python", "java", "c++", "c"

subjects = {"python","java", "c++", "python", "javascript",
            "java", "python", "java", "c++", "c"

}
print(subjects)
print(len(subjects))
    
##write a program to marks of 3 subjects from the user and store in a dictionary .Start with an empty dictionary and add one by one.Use subject name as a key and marks as value
marks = {}
x =int(input("enter marks of physics : "))
marks.update({"pysics" : x })

y = int(input("enter marks of chemistry : "))
marks.update({"chemistry" : y})

z = int(input("enter marks of maths :"))
marks.update({"maths": z})

print(marks)


## Figure out a way to store 9 and 9.0 as separete values in the set .
values = {
    ("float",9.0),
    ("int",9)
}
print(values)
    




