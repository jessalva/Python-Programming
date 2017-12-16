import array
arr= array.array('i',[1,2,3,4])

#printing the array

for i in range(0,3):
    print(arr[i],end=" ")
print("\n")
#appending a value in the array
arr.append(5)

#printing

for i in range(0,4):
    print(arr[i],end=" ")
print("\n")
#inserting value at a specific location
print("Enter value to be inserted at position 2")
value=int(input())
arr.insert(2,value)
print("\n")
#printing

for i in range(0,5):
    print(arr[i],end=" ")
print("\n")

#popping from an array

print("Array element that is popped at postion 3:")
popval=arr.pop(3)

print(popval)

#remove a the first occurence of a number
print("Removal of first occurence of 1\n")
arr.remove(1)

#printing

for i in range(0,3):
    print(arr[i],end=" ")
print("\n")

#Reversal of an Array

print("Reversal of array")
arr.reverse()

#printing

for i in range(0,3):
    print(arr[i],end=" ")
print("\n")

#index of first occurence
print("Index of first occurence")
print(arr.index(1))
