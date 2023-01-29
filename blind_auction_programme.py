from replit import clear

from bid import logo
print(logo)

bids={}

bidding_finisher=False

def highest_bidder(biddting_record):
    highest_bid = 0
    winner=""
    for bidder in biddting_record:
       bid_amount= biddting_record[bidder]

       if bid_amount>highest_bid:
           highest_bid=bid_amount
           winnner=bidder
    print(f" the winner is {winnner},with a bit of {highest_bid} $")







while not bidding_finisher:

    name=input("input your name?:\n")
    bid_price=int(input(" input your bid prize ?: $"))
    bids[name]=bid_price

    should_continue=input(" enter 'yes ' if you want to contunue,and if you can't then enter 'no'")
    if should_continue=="no":
     bidting_finisher=True

     highest_bidder(bids)
     break
    elif should_continue=="yes":
        clear()





