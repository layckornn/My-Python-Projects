import random

l = [1,2,34,5,6,7,8,0]

a = random.randint(1,7) # a<=x<=b

ab= random.randrange (2,7) #a<=x<b

b= random.random() #returns floating point number 0.0 <=x<1.0

c= random.uniform(1,3)

d= random.choice(l)


e= random.shuffle(l)

print(a)
print(b)
print(c)
print(ab)
print(d)
print(l) #Shuffle items in the List