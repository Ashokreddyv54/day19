from turtle import  Turtle,Screen
import random



turtle_move=False
#creating a screen object and set up screen size using the positional arguments
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Place a bet",prompt= "Which Turtle will win the race? Enter your color:")

y_position=[-100,-70,-40,-10,20,50]
colors=["red", "green","yellow","orange","blue","violet"]
all_objects=[]
for turtle_index in range(0,6):
    turtle_object=Turtle(shape="turtle")
    turtle_object.penup()
    turtle_object.color(colors[turtle_index])
    turtle_object.goto(x=-230, y=y_position[turtle_index])
    all_objects.append(turtle_object)

if user_bet:
    turtle_move=True

while turtle_move:
    for turtle in all_objects:
        if turtle.xcor()>230:
            turtle_move=False
            wining_color=turtle.pencolor()
            if wining_color==user_bet:
                print(f"yay! got it right, The color is {wining_color}")
            else:
                print(f"you got it wrong, The wining color is {wining_color}.")
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)



















screen.exitonclick()