mango=2 #its a global variable,

def food ():
    mango=10      #   its a local variable
    banana=4
    print(banana)
    print(mango)
food()
print(mango)


banana=200
apple=500
def shop():
    def food():
        banana=500
        print(banana)
        print(apple)
    food()
shop()
print(apple)




gmae_lavel=3
def name():
    llist=["raihan","roman","ria","nodi"]
    if gmae_lavel==3:
        print(llist[0])
name()


enimes=2
def enime_increased():
    return enimes+1
new_enimes=enime_increased()
print(new_enimes)


