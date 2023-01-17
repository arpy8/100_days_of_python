import turtle
from pandas import*

IMAGE = "india.gif"

screen = turtle.Screen() 

screen.title("Indian States Game")
turtle.addshape(IMAGE)
turtle.shape(IMAGE)
turtle.resizemode("auto")

guessed_state = []
            
data = read_csv("states.csv")
all_states = data.state.to_list()


while len(guessed_state) <= 28:    
    answer_state = screen.textinput(title=f"{len(guessed_state)}/28 States Correct", prompt= "What's another state's name? ").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in all_states:
                missing_states.append(state)
        new_data = DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break     

    if answer_state in all_states:
        t = turtle.Turtle()
        t.pu()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        guessed_state.append(answer_state) 

turtle.exitonclick()

