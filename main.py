"""In this project we will apply what we learn about csv and pandas"""
import turtle

import pandas

screen = turtle.Screen()
screen.title("Us_States_Name_Guessing_game")
# Setting image as a shape of turtle
image = "blank_states_img.gif"
screen.addshape(image)

# Now i can load an image
turtle.shape(image)
turtle_text = turtle.Turtle()
turtle_text.hideturtle()
# Now we want a coordinate of states
# we already have a coordinates in csv file so we do not have to spent a time on this task

# def get_mouse_click_coor(x, y):
#     """This function will get a coordinates from a screen where a  mouse click"""
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

total_states = 50
correct_answers = [0, ]
index = 0
score = 0
states_data = pandas.read_csv("50_states.csv")  # getting a data from a file
states_list = states_data["state"].to_list()  # getting a state column and convert it into a  list

is_game_on = True
while is_game_on:
    answer_states = turtle.textinput(prompt="what is another states names? ",
                                     title=f"{correct_answers[index]}/{total_states} State Correct").title()
    for state in states_list:
        if answer_states == state:
            print("state match.")
            score += 1
            correct_answers.append(score)
            index += 1
            row = states_data[states_data["state"] == f"{answer_states}"]
            x_coor = int(row.x)
            y_coor = int(row.y)
            turtle_text.penup()
            turtle_text.goto(x=x_coor, y=y_coor)
            turtle_text.write(arg=f"{answer_states}", font=("Arial", 12, "normal"))
        if score > len(states_list):
            is_game_on = False

# screen.exitonclick()
