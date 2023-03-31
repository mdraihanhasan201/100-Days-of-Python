# print("hey dude");
#
# print("hello"+" "+ "rayhan");
# name= input("wahat is your name")
# print("my nam is: ",name)
#
#
#
print("welcome to trip calculator");
total_bill= float(input("what was the total bill:"));
presentage=int(input("what percentage would you like to give? $10,$12,$15:"));
split=int(input("how many people to split the bill "));
persentage_bill=presentage/100;
each_person=(total_bill*persentage_bill)+total_bill;


print("ach person should pay:",each_person/split);