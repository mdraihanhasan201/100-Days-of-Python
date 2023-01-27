age=int(input("enter your age:"))

constant_age=90 # if you lift untill 90 years old,,

the_age_left=constant_age-age
day=the_age_left *365  #1 year=365 day
month=the_age_left *12  #12 mnt=1 year
week=the_age_left *52  #52 weeks =1 year

print(f" you have left {day} days,   {month} months and {week} weeks.." )
