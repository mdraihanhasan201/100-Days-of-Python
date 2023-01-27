print("welcome to tip calculator")

total_bil=float(input("enter total bill:\n"))
tip=float(input(" enter tip:\n"))
how_many_members_you_have=int(input("how many members you have"))

new_bill=total_bil+tip

per_person_bil=(new_bill)/how_many_members_you_have
the_final_bill_pp=(per_person_bil)
print(f"the final bill {new_bill}$ and per person have to pay{the_final_bill_pp} $ ")
