print("welcome to rock_paper_secors\n")


import random

user_choose=int(input(" çhoose 0 for rock,1 for paper and 2 for secores\n"))
computre_chooose= (random.randint(0,3))
print(f"computer coose{computre_chooose}")



if user_choose==0and computre_chooose==1:
 print("you lose")

elif user_choose==1and computre_chooose==2:
 print("you lose")

elif user_choose==2 and computre_chooose==0:
 print("you lose")

elif computre_chooose == 0 and user_choose == 1:
 print("you win")

elif computre_chooose == 1 and user_choose== 2:
 print("you win")

elif computre_chooose == 2 and user_choose == 0:
 print("you win")

elif computre_chooose== user_choose:
 print("its draw")
