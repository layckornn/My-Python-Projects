numbers = input("Enter set of numbers seperated by comma or space: ")

numbers_list = numbers.split() #Convert the numbers taken from Input into List butb they are in strings

print(numbers_list)

count = 0 #Initialize a value to count the number of elements in the list


for number in numbers_list:
    count +=1

print(f"The length of the list is: {number}")

for i in range(count): #For i in range 0 to count
    numbers_list[i] = int(numbers_list[i]) #convert the strings to integer
    print (numbers_list)

maximum_number = numbers_list[0] #Assume that the first mnumber is the maximum number and compare that to every element in that List

for number in numbers_list:
    if number > maximum_number:
        maximum_number = number

print(f"The maximum number is {maximum_number}")


