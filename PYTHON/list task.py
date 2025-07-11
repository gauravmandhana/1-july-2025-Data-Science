#task of list program

num = [1, 2, 3, 4, [5, 6, 7], 8, 9]

# 1. Print the element 6 from the nested list.

print(num[4][1])  # Output: 6

#2. Replace the number 3 with 33.
num[2] = 33
print(num)


#3. Append 10 to the end of the list.

num.append(10)
print(num)


#4. Insert 0 at the beginning.
num.insert(0, 0)
print(num)


#5. Count the total number of elements (excluding the nested list as one).
count = len(num) + len(num[5]) - 1


#6. Flatten the list into a single list.

num = [1, 2, 3, 4, [5, 6, 7], 8, 9]
flat_list = num[:4] + num[4] + num[5:]
print(flat_list)  

