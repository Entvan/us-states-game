import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the state", prompt="What's another state name?").title()

reformatted_data = pandas.read_csv("50_states.csv")
states_list = reformatted_data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break
    if answer_state in states_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = reformatted_data[reformatted_data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state name?").title()














