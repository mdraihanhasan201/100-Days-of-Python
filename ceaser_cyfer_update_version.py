
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s",
          "t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
          "p","q","r","s","t","u","v","w","x","y","z"]

def ceaser_cyfer(get_text,shift_num,derections):
    end_text=""
    if derections == "decode":
        shift_num *= -1
    for letter in get_text:
        if letter in alphabet:
         positions=alphabet.index(letter)
         new_positions = positions+shift_num
         end_text+=alphabet[new_positions]
        else:
         end_text += letter

    print(f"your {derections} text is \n{end_text}")


from art import logo
print(logo)

should_continue=False
while not should_continue:
    text = input("enter your text\n").lower()
    shift = int(input("enter your shift number\n"))
    derections = input("enter  direction for encryption type 'encode' and for decryptions type 'decode' ")
    shift = shift % 25

    ceaser_cyfer(get_text=text, shift_num=shift, derections=derections)
    restart = input(" if you want to continue enter 'yes ' and if you dont enter 'no '")
    if restart == "no":
        should_continue = True
        print("good bye!")

