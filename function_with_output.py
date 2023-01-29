# def my_function(f_name,l_name):
#     first_name=f_name.title()
#     last_name=l_name.title()
#     # print(f"{first_name} {last_name}")
#     return f"{first_name},{last_name}"
#
# formated_name=my_function(f_name="RAIHAN",l_name="iSlam")
# print(formated_name)


#multiple return values


def my_function(f_name,l_name):
    if f_name=="" or l_name=="":
        print(" you dont't provide any input ")
    first_name=f_name.title()
    last_name=l_name.title()
    # print(f"{first_name} {last_name}")
    return f"{first_name} {last_name}"

formated_name=my_function(input("enter your first name"), input("enter your last name"))
print(formated_name)