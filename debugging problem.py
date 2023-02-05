#before
# def my_function():
#     for i in range(1,20):
#         if i == 20:
#             print("you got it")
# my_function()
#
#




#
# # after solve problem
#
# def my_function():
#     for i in range(1,21):
#         if i == 20:
#             print("you got it")
# my_function()





# before debugging
# from random import randint
# dice_image=["1","2","3","4","5"]
# dice_num=randint(1,5)
# print(dice_image[dice_num])
#



# # after solve the problem
# from random import randint
# dice_image=["1","2","3","4","5"]
# dice_num=randint(1,4)
# print(dice_image[dice_num])


# before
# year = int(input("what is your year of birth"))
# if year > 1980 and year < 1994:
#     print("you are millenial")
# elif year > 1994:
#     print(" you are a gen z.")

# agter solve this
# year = int(input("what is your year of birth"))
# if year > 1980 and year <= 1994:
#     print("you are millenial")
# elif year > 1994:
#      print(" you are a gen z.")






# before
# pages=0
# word_per_page=0
# pages=int(input(" enter the page"))
# word_per_page== int(input("enter number of pages"))
# total_words=pages*word_per_page
# print(f"page={pages}")
# print(f"number of word={word_per_page}")
#
# print(total_words)
#
#
# # agter solve this
# pages=0
# word_per_page=0
# pages=int(input(" enter the page"))
# word_per_page= int(input("enter number of pages"))
# total_words=pages*word_per_page
# print(f"page={pages}")
# print(f"number of word={word_per_page}")
#
# print(total_words)
#
#

def mutate(a_list):
    b_list=[]
    for items in a_list:

     new_item=items*2

    b_list.append(new_item)
    print(b_list)

mutate(a_list=[1,2,3,4,5,6])



