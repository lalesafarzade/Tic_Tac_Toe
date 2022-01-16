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

player1=screen.textinput(title="player1",prompt="Player_1!please put your name")  
player2=screen.textinput(title="player2",prompt="Player_2! it's your turn!pleaseput your name")

def choose_first():
    if random.randint(0, 1) == 0:
        return player1
    else:
        return player2

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
    
    turn=choose_first()
    play_game=screen.textinput(title="starting",prompt=f"{turn} I randomly choose you for the start!Are you ready to play? Enter y/n.")
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
                t1=turtle.Turtle()
                t1.hideturtle()
                t1.penup()
                t1.goto(df.iloc[int(position)-1,1],df.iloc[int(position)-1,2])
                t1.color('deep pink')
                t1.write(player_1_marker,font=('Courier', 30, 'bold'))
                if win_check(player_1_marker,board):
                    print(f'Congratulation {player1}!You won the game!')
                    t2=turtle.Turtle()
                    t2.hideturtle()
                    t2.penup()
                    t2.goto(-300,300)
                    t2.color('deep pink')
                    t2.write('Congratulation!You won the game!',font=('Courier', 40, 'bold'))
                    game_on=False
                else:
                    if len(filled_position)==9:
                        print('The game is a draw!')
                        t3=turtle.Turtle()
                        t3.hideturtle()
                        t3.penup()
                        t3.goto(-300,300)
                        t3.color('deep pink')
                        t3.write('The game is a draw!',font=('Courier', 40, 'bold'))
                        break
                    else:
                        turn=player2
        else:
            position = screen.textinput(title=f"{player_2_marker}",prompt= "Choose your next position: (1-9) ")
            if int(position) in board:
                filled_position.append(int(position))
                board[int(position)]=player_2_marker
                t4=turtle.Turtle()
                t4.hideturtle()
                t4.penup()
                t4.goto(df.iloc[int(position)-1,1],df.iloc[int(position)-1,2])
                t4.color('deep pink')
                t4.write(player_2_marker,font=('Courier', 30, 'bold'))
                if win_check(player_2_marker,board):
                    print(f'Congratulation {player_2_marker}!You won the game!')
                    t5=turtle.Turtle()
                    t5.hideturtle()
                    t5.penup()
                    t5.goto(-300,300)
                    t5.color('deep pink')
                    t5.write(f'Congratulation {player2} !You won the game!',font=('Courier', 40, 'bold'))
                    game_on=False
                else:
                    if len(filled_position)==9:
                        print('The game is a draw!')
                        t6=turtle.Turtle()
                        t6.hideturtle()
                        t6.penup()
                        t6.goto(-300,300)
                        t6.color('deep pink')
                        t6.write('The game is a draw!',font=('Courier', 40, 'bold'))
                        break
                    else:
                        turn=player1
    
    if not reply():
        break
    




screen.exitonclick()


