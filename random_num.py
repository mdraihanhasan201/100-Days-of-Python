import random
in_name=input(" enter some random name\n")
name=in_name.split(",")
len=len(name)

random_choice=random.randint(0 , len-1)
chossen_person=name[random_choice]
print(f"today billl going to pay {chossen_person} ")
