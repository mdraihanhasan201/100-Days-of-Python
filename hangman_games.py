import random

word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
'coyote crow deer dog donkey duck eagle ferret fox frog goat '
'goose hawk lion lizard llama mole monkey moose mouse mule newt '
'otter owl panda parrot pigeon python rabbit ram rat raven '
'rhino salmon seal shark sheep skunk sloth snake spider '
'stork swan tiger toad trout turkey turtle weasel whale wolf '
'wombat zebra ').split()

stages= ['''+---+
| |
O |
/|\ |
/ \ |
|
=========
''']
choosen_word=random.choice(word_list)

display=[]
for _ in range(len(choosen_word)):
 display+="_"
 print(display)



eld_of_games= False
lifes=6

while not eld_of_games:

 guess=input("guess a latter\n").lower()
 if guess in display:
  print(f"you already guessed{guess}")

 for position in range(len(choosen_word)):
   i=choosen_word[position]
   if i==guess:
    display[position]=i
    print(display)

if guess not in choosen_word:
 print(f"you choosed {guess},thats not in the word")
 lifes=lifes-1

if lifes==0:
  eld_of_games=True
  print("you lose")



if "_" not in display:
 eld_of_games=True
 print("y0u win!")

print(stages[lifes])


#hang_man_games