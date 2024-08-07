heights = input("Enter all heights separated by a space: ")

height_list = heights.split()

count = 0

print(height_list)

for height in height_list:

    count= count+1

for i in range(count):

    height_list[i] = int(height_list[i])

total = 0

for person in height_list:

    total += person

avg = total / count

print(count)
print(avg)



