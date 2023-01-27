# test_h=int(input("enter the hight of wall"))
# test_widt=int(input("enter the widt of wall"))
#
# covarage=5
#
# number_of_cans=test_h*test_widt/covarage
# round_num_of_cans=print(round(number_of_cans))

def num_of_cans(hight,widt,cover):
    area=hight*widt
    number_of_cans=round(area/cover)
    print(f"you will need {number_of_cans} of paints")

tsest_h=int(input("enter hight of wall"))
test_wild=int(input("enter widt of wall"))
covarage=5


num_of_cans(hight=tsest_h,widt=test_wild,cover=covarage)
