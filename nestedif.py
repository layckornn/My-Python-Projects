# Nested If means an If Statement inside an If Statement

height = int(input("What is your height? "))


if height >= 3:

    print("Yes you can ride")

    age = int(input("What is your age? "))

    if age <= 18:

        print("Your Money is 250k") #NestedIf

    else:

        print("Your Money is 500k")

else:

    print("You can't ride")

print("Bye")


