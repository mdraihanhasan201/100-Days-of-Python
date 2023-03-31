import random
from turtle import Turtle,Screen
import random


tim=Turtle()
color_n=["blue","forest green","medium sea green","olive","red","green","yellow","black","pink"]


def slides_num(num_of_slides):
    for _ in range (num_of_slides):
         angle=360/num_of_slides
         tim.forward(100)
         tim.right(angle)

for slides_n in range(3,11):
    tim.color(random.choice(color_n))

    slides_num(slides_n)



screen=Screen()
screen.exitonclick()
