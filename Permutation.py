from itertools import permutations,combinations,combinations_with_replacement

#print all possible permutations
print("All possible permutations")
permset=permutations([1,2,3])

for i in list(permset):
	print(i)

#print all permutations taken r at a time
print("All possible permutations taken r at a time")
r=int(input())
permsettakenr=permutations([1,2,3],r)

for i in list(permsettakenr):
	print(i)

#print all possible combinations taken r at a time
print("All possible combinations without repetitions")
print("Enter r")
r=int(input())

combset=combinations([1,1,2,3],r)

for i in list(combset):
	print(i)

#print all possible combinations with repetitions
print("All possible combinations with repetitions")
print("Enter r")
r=int(input())
combset=combinations_with_replacement([1,1,2,3],r)

for i in list(combset):
	print(i)