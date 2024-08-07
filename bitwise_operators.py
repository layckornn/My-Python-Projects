#They are used to Operate on Bits The ayre below
# & Bitwise AND
# | Bitwise OR
# ^ Bitwise XOR (If boths bits are same it gives zero)
# Bitwise Compliment ~
# << LeftShift
# >> RightShift

a = 5
b= 4

print(a&b) #This converts both a (0101) and b (0100) into binary before multiplying them together
print(a|b) #This converts both a (0101) and b (0100) into binary before adding them together
print(a^b) #If boths bits are same it gives zero and gives 1 if boths bits are different
print(~a) #If boths bits are same it gives zero and if any of the bit is 1 it gives 1 and you'll do 2's compliments
print(a<<2) #e.g leftshit (We do not loose bit) by 2bits 5= 0101. use short formular (x<<n) = 2^n
print (a>>2) #e.g Rightshift (We loose bits) use short formular (x<<n) =x/2^n

