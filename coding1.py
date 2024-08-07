currentageyr = int(input("Enter your current age: ")) 
currentagedays = int(input("And How many days plus? "))

yearsleft = currentageyr * 365

ninetyyrs = 90*365

temp0 = yearsleft + currentagedays

nyearsleft = ninetyyrs - temp0

realleftyrs = nyearsleft // 365

print(realleftyrs)

temp1 = currentagedays // 31 #Converting the excess days to months

temp2 = (currentagedays % 31) * 31 #Converting the remainder of the weeks to days

temp3 = temp2// 52 # No of weeks

temp4 = (temp2 % 52)* 52 #No of days



print(f" You have {realleftyrs} years, {temp1} months, {temp3} weeks and {temp4} days to live")