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

#for i in range(len(numbers)):
    #t=turtle.Turtle()
    #t.hideturtle()
    #t.penup()
    #t.goto(df.iloc[i,1],df.iloc[i,2])
    #t.write(str(i+1))

player1=screen.textinput(title="player1",prompt="Player_1! put your name")  
player2=screen.textinput(title="player2",prompt="Player_2! it's your turn!put your name")


def player_input():
    player_1_marker = ''
    while not (player_1_marker == 'X' or player_1_marker == 'O'):
        player_1_marker=screen.textinput(title=f"{player1}",prompt=f"{player1} !put your marker?X/O")

    if player_1_marker.lower() == 'x':
        return ('X', 'O')
    else:
        return ('O', 'X')

def win_check(mark,board):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def reply():
    answer=screen.textinput(title="????",prompt= 'Do you want to play again? Enter Yes or No: ')
    return answer.lower().startswith('y')


filled_position=[]    
while True:
    board=["#",
           1,2,3,
           4,5,6,
           7,8,9]
    player_1_marker,player_2_marker= player_input()
    turn=player1
    play_game=screen.textinput(title="starting",prompt=f"{player1} Are you ready to play? Enter y/n.")
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn==player1:
            
            position = screen.textinput(title=f"{player_1_marker}",prompt= "Choose your next position: (1-9) ")
            if int(position) in board:
                filled_position.append(int(position))
                board[int(position)]=player_1_marker
                t=turtle.Turtle()
                t.hideturtle()
                t.penup()
                t.goto(df.iloc[int(position)-1,1],df.iloc[int(position)-1,2])
                t.color('deep pink')
                t.write(player_1_marker,font=('Courier', 30, 'bold'))
                if win_check(player_1_marker,board):
                    print('Congratulation!You won the game!')
                    t=turtle.Turtle()
                    t.hideturtle()
                    t.penup()
                    t.goto(-300,300)
                    t.color('deep pink')
                    t.write('Congratulation!You won the game!',font=('Courier', 40, 'bold'))
                    game_on=False
                else:
                    if len(filled_position)==9:
                        print('The game is a draw!')
                        t=turtle.Turtle()
                        t.hideturtle()
                        t.penup()
                        t.goto(-300,300)
                        t.color('deep pink')
                        t.write('The game is a draw!',font=('Courier', 40, 'bold'))
                        break
                    else:
                        turn=player2
        else:
            position = screen.textinput(title=f"{player_2_marker}",prompt= "Choose your next position: (1-9) ")
            if int(position) in board:
                filled_position.append(int(position))
                board[int(position)]=player_2_marker
                t=turtle.Turtle()
                t.hideturtle()
                t.penup()
                t.goto(df.iloc[int(position)-1,1],df.iloc[int(position)-1,2])
                t.color('deep pink')
                t.write(player_2_marker,font=('Courier', 30, 'bold'))
                if win_check(player_2_marker,board):
                    print(f'Congratulation {player_2_marker}!You won the game!')
                    t.goto(-300,300)
                    t.color('deep pink')
                    t.write(f'Congratulation {player_2_marker} !You won the game!',font=('Courier', 40, 'bold'))
                    game_on=False
                else:
                    if len(filled_position)==9:
                        print('The game is a draw!')
                        t.goto(-300,300)
                        t.color('deep pink')
                        t.write('The game is a draw!',font=('Courier', 40, 'bold'))
                        break
                    else:
                        turn=player1
    t.clear()
    if not reply():
        break





                
        
            
            
    
    

screen.exitonclick()


