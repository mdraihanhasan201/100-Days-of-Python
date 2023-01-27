hight=float(input("enter your hight"))
weight=float(input("enter your weight"))


bmi=(weight) / (hight) ** 2
# bmi=33
bmi_int=(int(round(bmi)))


if bmi_int<19:
    print(f"your bmi value is {bmi_int}.  you are underweight!")
elif  bmi_int<25:
    print(f"your bmi value is {bmi_int}.you are normal.")
elif bmi_int<35:
    print(f"your bmi value is {bmi_int}.you are overweight!")
else:
    print(f"your bmi value is {bmi_int}.you are critillay obese!!")




