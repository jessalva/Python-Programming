import array

arr=array.array('i',[1,2,3,4,5])
arrappend=array.array('i',[1,2,23])
#printing the typecode
print("DataType(typecode):"+str(arr.typecode))
#printing the itemsize
print("Size(itemsize):"+str(arr.itemsize))
#printing the buffer info
print("Buffer Info:"+str(arr.buffer_info()))



#counting number of occurences
print("The number of occurences of a number")
print(arr.count(1))

#modifying an Array
print("Modified array")
arr.extend(arrappend)
for i in range(0,8):
    print(arr[i],end=" ")

#using tolist and fromlist
print("\nPrinting the array by appending the list to the array")

li=[1,2,67]
arr.fromlist(li)
for i in range(0,11):
    print(arr[i],end=" ")

print("\nPrint the list formed by converting the array to list")
listfromarray=arr.tolist()
for i in listfromarray:
    print(i,end=" ")
print("\n")
