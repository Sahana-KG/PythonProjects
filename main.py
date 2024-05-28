from turtle import *
from turtle import Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title= "Make a bet!",prompt="Choose a turtle that will win: ").lower()

colors_list =["red","blue","green","yellow","purple","orange"]
y_pos = [180,130,80,30,-20,-70]
speed = [100,75,50,25,10,150]
all_turtles =[]

for turtle in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors_list[turtle])
    tim.penup()
    tim.goto(x=-230,y=y_pos[turtle])
    all_turtles.append(tim)

if user_bet:
    is_race_on =True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! {winning_color} turtle is the winner")
                is_race_on = False
            else:
                print(f"You lost! {winning_color} turtle is the winner")
                is_race_on = False
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)






screen.exitonclick()