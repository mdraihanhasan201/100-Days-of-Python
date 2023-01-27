print("welcome to pizza order system!")

order=input("whis type of pizza you want to>> small , medium or large?")
bill=0
if order == "small":
    bill=10
    print(f" you have to pay { bill} $ ")
elif order== "medium":
    bill=15
    print(f" you have to pay {bill} $ ")
elif order=="large":
    bill=20
    print(f" you have to pay {bill} $ ")
else:
    print("pleased give us right input")
    breakpoint()

add_pepperoni=input("you want to add extra pepperoni? yes or no...")
if add_pepperoni=="yes":
    bill+=5
    print(f" now you have to pay {bill} $ ")
elif add_pepperoni=="no":

    print(" enjoy your food sir ")

add_extra_cheeese=input("you want extra cheese?! yes or no")
if add_extra_cheeese=="yes":
    bill+=10
    print(f" your final bill {bill} $ enjoy your food sir ")
elif add_extra_cheeese=="no":
    print(f" enjoy your food sir ")

