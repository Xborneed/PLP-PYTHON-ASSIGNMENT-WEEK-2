#creating an empty list in python
# and appending an empty string to it

my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list) # Output: ['10, 20, 30, 40']

#insert an element at a specific index
#in this case, we are inserting 15 at index 1
my_list.insert(1, 15)
print(my_list) # Output: ['10, 15, 20, 30, 40']



#extend the list with another list
my_list2 = [50, 60, 70]
my_list.extend(my_list2)
print(my_list) # Output: ['10, 15, 20, 30, 40, 50, 60, 70']


#remove the last element from the list
my_list.pop()
print(my_list) # Output: ['10, 15, 20, 30, 40, 50, 60']




#sort the list with numbers in ascending order
#in this case, we are sorting the list in ascending order

my_list.sort()
print(my_list)

#print the index of the value 30 in the list
print(my_list.index(30)) # Output: 3



















