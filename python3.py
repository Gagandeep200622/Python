# Strings in python can be created using single quotes, double quotes, or triple quotes.


str1 = "thise is a string. \n we are creating it in python"
print(str1)

str2 = '''this is a string.\t We are creatining it in python'''
print(str2)

str3 = 'this is a string .'
print(str3)

# Concatenation of strings
str1 = "Gagandeep R "
str2 = "Naik"
final_str = str1 + str2
print(final_str) #Gagandeep R Naik


#length of string

str1 = "Gagandeep R Naik"
len1 = len(str1)
print(len1) #16
str2 = "Karnataka"
len2 = len(str2)
print(len2)#9

final_str = str1 + "  " + str2
print(final_str) #Gagandeep R Naik Karnataka

#indexing 
str = "Davanagre"
char= str[3]
print(char) #a

# #slicing
str = "Karnataka"
print(str[ :5])
print(str[5:])
print(str[1:6])
print(str[ : ]) #Karnataka
print(str[0:len(str)])

#slicing negative index
str = "Gagandeep R NAik"
print(str[-3:-1])
print(str[-4:-1])
print(str[-16:-11])
