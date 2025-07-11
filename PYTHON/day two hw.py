#.............................LIST..................
# ordered, mutable (changeable), and allows duplicate elements. 

# Lists are used to store multiple items in a single variable.


#list create
lst=[1,2,3,4,5,6]  

# mix list 
mix_lst=[1,3.14,"Gaurav", True]

#acessing list
print(lst[0])
print(lst[1])
print(lst[3])
print(lst[4])


#adding element

a = []

a.append(10)  
print("After append(10):", a)  

#  inding
a.insert(0, 5)
print("After insert(0, 5):", a) 

# Adding multiple elements  
a.extend([15, 20, 25])  
print("After extend([15, 20, 25]):", a)

# updating element
a = [10, 20, 30, 40, 50]

a[1] = 25 

print(a)


a = [10, 20, 30, 40, 50]

# Removes the first occurrence of 30
a.remove(30)  
print("After remove(30):", a)

# Removes the element at index 1 (20)
popped_val = a.pop(1)  
print("Popped element:", popped_val)
print("After pop(1):", a) 

# Deletes the first element (10)
del a[0]  
print("After del a[0]:", a)

# >>>>>>>>>>TUPLE>>>>>>>>>>>>>>>>>>>>

#A tuple is a built-in Python data structure used to store multiple items in a single variable,
#  just like a list — but tuples are immutable, meaning they cannot be changed after creation.

tpl = (10, 20, 30)   #1st type to creat tuple
_tpl= 40,50,60       #2nd type to creat tuple 

print(tpl)
print(_tpl)

print(len(tpl))
print(type(tpl))
print(tpl.count(10))

#>>>>>>>>>>>>>>>>>>DICTIONARY>>>>>>>>>>>>

# unordered, mutable, and indexed collection of key-value pairs.


student = {
    "name": "Gaurav",
    "age": 21,
    "collage": "Raffles" 
    
}
# Accessing Values
print(student["name"])     
print(student.get("age"))  






