print("welcome to love score games")
name=input("enter youe name:\n")
your_pratnar_name=input("enter your pratnar name\n")
string_concatinations=name+your_pratnar_name
lower=string_concatinations.lower()

t=lower.count("t")
r=lower.count("r")
u=lower.count("u")
e=lower.count("e")
ture=t+r+u+e

l=lower.count("l")
o=lower.count("o")
v=lower.count("v")
e=lower.count("e")
love=l+o+v+e

love_score=int(str(ture)+str(love))

if (love_score<10) or (love_score>90):
    print(f" your love score is {love_score}%.you go together like coke and mentos!")
elif (love_score>=50) and (love_score<=60):
    print(f"your love score is {love_score}%. you are alright together")
else:
    print(f"your love score is {love_score}% ")





