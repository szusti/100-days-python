import turtle
from states import State
from text import Text

test_states = State()
image = "day-25/us_states/blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)

text = Text()

# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)
game_on:bool = True
guessed_states:int = 0

while game_on:
    answer_state = screen.textinput(title=f"Guess the State. {guessed_states}/50",prompt="Gib mi anoder stejt").capitalize()
    if answer_state == "Exit":
        break
    check_answer = test_states.get_coordinates(answer_state)
    if check_answer != False:
        text.write_state(check_answer,answer_state)
        guessed_states =+ 1
    if guessed_states == 50:
        game_on = False


