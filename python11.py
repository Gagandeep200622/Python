# Recursion

def show(n):
    if(n == 0):
        return
    print(n)
    show(n - 1)

show(6)



def facto(n):
    if(n == 0 or n == 0 ):
        return 1
    return facto(n-1) * n

print(facto(4))


# write a recursive function to calculate the sum of first n natural numbers

def cal_sum(n):
    if(n == 0):
        return 0
    
    return cal_sum(n - 1) + n

sum =  cal_sum(10)

print(sum)


# write a recursive function to print all elements in a list.Hint: use list & index as parameters 


def print_list(list, idx = 0):
    if(idx == len(list)):
        return

    print(list[idx])
    print_list(list, idx + 1)

fruits = ["apple", "banana", "mango"]    

print_list(fruits)

  


