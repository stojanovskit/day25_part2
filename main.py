import turtle
import pandas

# def get_mouse(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse)
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_data = pandas.read_csv("50_states.csv")
states = states_data["state"].to_list()


def get_coordinates(answer):
    x = (states_data["x"].to_list())[states.index(answer_state)]
    y = (states_data["y"].to_list())[states.index(answer_state)]
    turtle2 = turtle.Turtle()
    turtle2.hideturtle()
    turtle2.penup()
    turtle2.setposition(x, y)
    turtle2.write(answer)


points = 0
game_on = True
while game_on:
    answer_state = (screen.textinput(title=f"{points}/{len(states)} Guess The State ",
                                     prompt="Whats another states name? ")).title()
    if answer_state in states:
        points += 1

        get_coordinates(answer_state)
    if points == len(states):
        game_on = False
        turtle.write("You Won!")

# print(answer_state)
turtle.mainloop()

# screen.exitonclick()
