alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s",
          "t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
          "p","q","r","s","t","u","v","w","x","y","z"]


derections=input("type 'encript' to enriptions and type 'decript' to decriptions\n")

text=input("enter your text\n").lower()
shift=int(input("enter your shift number\n"))



def encript(plan_text,shift_number):
 cyber_text=""
 for i in plan_text:
    current_positions=alphabet.index(i)
    new_positions=current_positions+shift_number
    new_latter=alphabet[new_positions]
    cyber_text+=new_latter
 print(f"the incoded text is {cyber_text}")



def decript(cyber_texr,shift_amount):
    plan_text= ""
    for i in cyber_texr:
        current_positions = alphabet.index(i)
        new_positions = current_positions - shift_amount
        new_latter = alphabet[new_positions]
        plan_text += new_latter
    print(f"the decript text is {plan_text}")



if derections=="encript":
    encript(plan_text=text, shift_number=shift)
elif derections=="decript":
    decript(cyber_texr=text,shift_amount=shift)






