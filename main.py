import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S States Game")
picture = "blank_states_img.gif"
screen.addshape(picture)
data = pandas.read_csv("50_states.csv")
states_name = data["state"].to_list()
game_is_on = True
turtle.shape(picture)
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct"
                               , prompt="What's another state's name(Re-adjust this dialog box to your liking)").title()
    if answer_state == "Exit":
        missing_states = []
        for states in states_name:
            if states not in guessed_state:
                missing_states.append(states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states_name:
        guessed_state.append(answer_state)
        tom = turtle.Turtle()
        tom.hideturtle()
        tom.penup()
        state_data = data[data["state"] == answer_state]
        tom.goto(state_data.x.item(), state_data.y.item())
        tom.write(answer_state)


