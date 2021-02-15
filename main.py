import turtle
import pandas
from playsound import playsound


screen = turtle.Screen()
screen.title("US States Quiz")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
data = pandas.read_csv("50_states.csv")
state_names = data.state.to_list()  #Stroing state names in list for ease
#print(state_names)
user_choice = ""
playsound('null.mp3',False)
correct_states = []



def get_user_input():
    global user_choice
    global correct_states
    user_choice = screen.textinput(title="Guess the State", prompt = f"{len(correct_states)}/50 states correct Whats another state?")

def add_to_map(state):
    global data
    info_column = data[data.state == state]
    x = int(info_column.x)
    y = int(info_column.y)
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    t.setposition(x-5,y)
    t.write(state)

def exit_game():
    print("******************************\n")
   # print(state_names)
    new_data = pandas.DataFrame(state_names)
    print(new_data)
    new_data.to_csv('missing.csv')
    exit(0)


while len(correct_states) < 50:
    get_user_input()
    if user_choice.title() == "Exit":
        exit_game()
    if user_choice.title() in state_names:
        print(f"User choice found: {user_choice}")
        add_to_map(user_choice.title())
        correct_states.append(user_choice)
        state_names.remove(user_choice.title())

turtle.mainloop()


