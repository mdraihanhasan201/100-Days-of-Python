print("welcome to rollercoster games")
height=input("input your hight in cm\n:")
new_hight=int(height)
bill=0

if new_hight>=160:
    print("you can ride(-_-)#3,,yeahhhh!!")

    age=int(input("input your age\n:"))

    if age<12:
        bill=5
        print("you have to pay 5$")
    elif age <=18:
        bill=10
        print("you haveto pay 10$")
    elif age>=50:
        bill=3
        print("you have to pay 3$")
    elif age > 18:
        bill=17
        print("you haveto pade 17$")

    photo_taken=input("did you want to photo take for informations ? give the ans y or n")
    if photo_taken== "y":
        bill+=3
    elif photo_taken=="n":

        print(" have a nice ride")

        print(f"your final bill is {bill} $")


else:
    print("ïf you want to do ride, then you have to grow up ")

