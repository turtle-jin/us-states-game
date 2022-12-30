import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=1000, height=1000)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)  # add the image to the screen so that we can load that to turtle

turtle.shape(image)  # load a new image as a new shape

# To get screen coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

# read csv file
data = pandas.read_csv("50_states.csv")

# build a state list
state_list = data.state.to_list()
end_of_game = False
completed_states = []

while len(completed_states) != 50 and not end_of_game:
    user_input = screen.textinput(title=f"{len(completed_states)}/50 States Correct",
                                  prompt="What's another state's name?")
    user_input_titled = user_input.title()

    if user_input_titled not in state_list:
        play_again = screen.textinput(title=f"Wrong Answer!", prompt=f"Your highest score is {len(completed_states)}. "
                                                                     f"\nDo you want to continue playing?"
                                                                     f" Type Yes or No:").lower()
        if play_again == "no":  # save the missing states to a csv when end of game if users choose no
            end_of_game = True
            missing_states = [state for state in state_list if state not in completed_states]

            missing_states_data = pandas.DataFrame(missing_states)
            missing_states_data.to_csv("States_to_learn.csv")
            break

        else:  # continue the game
            user_input = screen.textinput(title=f"{len(completed_states)}/50 States Correct",
                                          prompt="What's another state's name?")
            user_input_titled = user_input.title()

    pull_state = data[data.state == user_input_titled]
    x_cor = int(pull_state.x)
    y_cor = int(pull_state.y)

    if user_input_titled in state_list:
        t = turtle.Turtle()
        t.color("black")
        t.penup()
        t.ht()
        t.goto(x_cor, y_cor)
        t.write(pull_state.state.item())  # item(self) returns the first element of the underlying data
        if user_input_titled not in completed_states:

            completed_states.append(user_input_titled)
        else:
            print("You have already guessed that state!")  # change it to tkinter message box later
