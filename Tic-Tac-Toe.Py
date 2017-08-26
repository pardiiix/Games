# -*- coding: utf-8 -*-
"""
Created on August 24th, 2017

@author: Pardis Ranjbar
E-mail: pardis.ranjbar@gmail.com
#==============================================================================
# This is a code of a Tic-Tac-Toe game.
#==============================================================================
"""
x=y=None
matrix=[]
player=None
win=None
def initialize(): #This is the first function of the code
    global player, win, matrix #globalizing to be able to use later on
    player=1 #player 1 starts
    win=False #at first there is no winner
    matrix=[[0,0,0] for i in range(3)] #an empty square matrix with a size of 3
def print_emptyboard(): #prints the empty board with no components
    for i in range(3): #three rows and columns are created
        print('-------') 
        row='| | | |'
        print(row)
    print('-------') #prints the 4th line
    print('Player 1') #to indicate that the game starts with player 1
def print_board(): #prints the board after a component is given
    global matrix
    for i in range(len(matrix)):
        print('-------') #the first line
        row='|' #the first border
        for j in range(len(matrix[i])):
            if matrix[i][j]==0: #if no input has been given yet
                row+=' |' #an empty space and it's border should be added to row
            elif matrix[i][j]==2: #if player 2 enters a coordinate
                row+='O|'
            else:
                row+='X|'
        print(row) # prints a completed row with X's and O's
    print('-------')  
def check_winner():
    global matrix,win
    for i in range(len(matrix)):
        s1=s2=d1=d2=1
        for j in range(len(matrix[i])):
            s1*=matrix[i][j] #s1 is the multiplication of a row
            s2*=matrix[j][i] #s2 is the multiplication of a column
        if s1==1 or s1==8 or s2==1 or s2==8:
            print('player',player, 'wins')
            win=True
    for i in range (len(matrix)):
        for j in range(len(matrix)):
            if i==j:
                d1*=matrix[i][j] 
            if i+j==2:
                d2*=matrix[i][j]
    if d1==1 or d1==8 or d2==1 or d2==8:
            print('player',player, 'wins')
            win=True
def select_place():
    global x,y, matrix ,player
    x=int(input('enter X position:\n'))
    y=int(input ('enter Y position:\n'))
def set_selected_place():
    global matrix, player, x, y
    matrix[x][y]=(player)
def boardisfull():
    for i in range (len(matrix)):
        for j in range(len(matrix)):
            if (matrix[i][j]==0):
                return False
    return True
    print('Game over')
def winner():
    return win
def switch_player():
    global player
    player=2 if player==1 else 1
    print('Player', player)
print_emptyboard()
initialize()
while True:
    while not boardisfull() and not winner():
        select_place()
        set_selected_place()
        print_board()
        check_winner()
        switch_player()
print('Game Over!\n')
