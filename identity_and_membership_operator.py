# This tuttorial is to show that Identity Operator (is, and is not) is not the same as equality operator
#These 2 Identity are used to compare the same objects.

#See example below for "is"

a = 5
b = 5

print(a is b) # Returns true cause a and b belongs to the same container memory

#Proof Below
print(id(a)) #Shows that they are in the same memory (Same Object ID)
print(id(b)) #Shows that they are in the same memory (Same Object ID)


a = 7
b= '8'

print(a is b) # Returns False cause they are not in same container memory (different Object ID)

#Proof Below
print(id(a)) #Shows that they are not in the same memory (different Object ID)
print(id(b)) #Shows that they are not in the same memory (different Object ID)


####Another EXAMPLE

a = 5
print(id(a))
a= 6
print(id(a))

#Assignment

a = 5

print(id(a))

a= 6
print(id(a))

print(a is a)