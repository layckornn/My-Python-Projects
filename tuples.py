# Tuples are used to store multiple variables 

tuple1 = (10, 1, -1, 15, 20)
tuple2 = ("Lekan", "Busola", "Sholay", "Adesiyan")

tuple3 = (10, "Lekan", True, 10.10)

tuple4 = (10,)

tuple5 = (10) #This is not a tuple, it has to have a comma just like tuple4

print(type(tuple1))
print(type(tuple2))
print(type(tuple3))
print(type(tuple4))
print(type(tuple5))

#Properties of turple

print(tuple1[0])
print(tuple1[-2])
#print(tuple1[-7])  index out of range error
#Elements in Tuple are immutable, can't be changed or replaced or changed order
#Duplicate items allowed unlike sets

print(tuple1[1:4]) #print from index 1 till the lenght = 4
print(tuple1[:4])
print(tuple1[::2])




