name1 = input("What is your name? ") #This takes input and coverts it into lower case
name2 = input("What is his/her name? ")

combine_string = name1+name2

lower_case_string = combine_string.lower()



t = lower_case_string.count ("t") #Count the number of "t" in lower_case_string
r = lower_case_string.count ("r")
u = lower_case_string.count ("u")
e = lower_case_string.count ("e")

l = lower_case_string.count ("l") #Count the number of "l" in the str gname
o = lower_case_string.count ("o")
v= lower_case_string.count ("v")
e = lower_case_string.count ("e")

true = t + r + u + e

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score >90:
    
    print (f"Your Score is {love_score} and you go together like mad")

elif love_score >= 40 and love_score <= 50:

    print (f"Your Score is {love_score} and you are alright together like mad")

else:

    print(f"You love score is {love_score}")

