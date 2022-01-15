import turtle
import os
import random
import pandas as pd

screen=turtle.Screen()
screen.title("Welcome to Tic Tac Toe game!")
image=os.path.join("images","t_board.GIF")
num_csv=os.path.join("Resources","numbers.csv")
df=pd.read_csv(num_csv)
numbers=df.number.to_list()

screen.addshape(image)
turtle.shape(image)

for i in range(len(numbers)):
    t=turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(df.iloc[i,1],df.iloc[i,2])
    t.write(str(i+1))

player1=screen.textinput(title="player1",prompt="Player_1! put your name")  
player2=screen.textinput(title="player2",prompt="Player_2! it's your turn!put your name")


def player_input():
    player_1_marker = ''
    while not (player_1_marker == 'X' or player_1_marker == 'O'):
        player_1_marker=screen.textinput(title=f"{player1}",prompt=f"{player1} !put your marker?X/O")

    if player_1_marker.upper() == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def player_choice():
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not position in filled_position:
        position = screen.textinput(title="positioning",prompt= "Choose your next position: (1-9) ")
        filled_position.append(int(position))
    return position

filled_position=[]    
while True:
    player_1_marker,player_2_marker= player_input()
    turn=player1
    play_game=screen.textinput(title="starting",prompt=f"{player1} Are you ready to play? Enter y/n.")
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn==player1:
            position=player_choice()
    




#player_1_marker=screen.textinput(title="player1",prompt=f"{player1}!put your marker?X/O")


#def player_input():

screen.exitonclick()