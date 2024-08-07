weight = input("Enter the Weight in KG: ")
height = input("Enter the height in metres: ")

w = int(weight)
h = float(height)

temp = h ** 2

bmi = w / temp

print(f"Your bmi is, {bmi} m")