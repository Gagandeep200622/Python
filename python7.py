# loops in python
count = 1
while count <= 5 :
    print("hello")
    count += 1

print(count)

i = 1
while i<= 100000:
    print("Gagandeep",i)
    i += 1


# print numbers from 1 to 5

i = 1
while i<=5 :
    print(i)
    i += 1
   
print("loop ended")

i = 5
while i >= 1:
    print(i)
    i -= 1


# print numbers from 1 to 100

i = 1
while i <= 100:
    print(i)
    i +=  1

print("code ended")

#print numbers from 100 to 1

i = 100
while i >= 1:
    print(i)
    i -= 1

print( " executed successfully")


#print the multiplication table of a number n :

i = 1
n = int(input("enter a number :"))
while i <= 10 :
    print(n * i)
    i += 1

# print the elements of the following list using a loop [1,4,16,25,36,49,64,81,100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0
while idx < len(nums) :

    print(nums[idx])
    idx += 1

heros = ["Gagan", "Ramcharan", "Yash","Darshan","Sudeep"]# travers

idx = 0
while idx < len(heros):
    print(heros[idx])
    idx += 1


# search for a number x in this tuple using loop [1,4,16,25,36,49,64,81,100]

nums = (1,4,16,25,36,49,64,81,100)

x = 36
i = 0
while i < len(nums):
        if(nums[i] == x):
                print("found at idx",i )

        else:
                print("findimg")
  
        
        i += 1

i = 1
while i <= 5:
    print(i)
    if( i == 3):
        break
    i += 1

print("end of loop")

i = 0 
while i <= 5:
    
    if(i == 3):
        i += 1
        continue #. skip
    print(i)
    i += 1








