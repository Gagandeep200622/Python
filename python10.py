# built in function. 

print() 
len()
type()
range()


#default parameters

def cal_pro(a = 2, b = 21):
    print(a * b)
    return a * b

cal_pro()

# wrinte a function to print the lenth of a list

cities = ["Banglore", "Davanagere", "Mysore", "Shanthinagara"]

heros = ["Gagandeep R Naik", "Sudeepa B", "Prajwal R Naik "]

def list_len(cities):
    print(len(cities))

list_len(cities)
list_len(heros)


# write a function to print elements of a list in a single line

cities = ["Banglore", "Davanagere", "Mysore", "Shanthinagara"]

def print_len(list):
    for items in list:
        print(items, end=" ")

print_len(cities)        
print()

# write a function to find the factorial of n


def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
        print(fact)

cal_fact(6)

# write a function to convert USD to INR

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val,"USD  =", inr_val, " INR ")


converter(101)

