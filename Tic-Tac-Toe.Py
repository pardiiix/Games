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
def initialize():
    global player, win, matrix
    player=1
    win=False
    matrix=[[0,0,0] for i in range(3)]
def print_emptyboard():
    for i in range(3):
        print('-------')
        row='| | | |'
        print(row)
    print('-------')
    print('Player 1')
def print_board():
    global matrix
    for i in range(len(matrix)):
        print('-------')
        row='|'
        for j in range(len(matrix[i])):
            if matrix[i][j]==0:
                row+=' |'
            elif matrix[i][j]==2:
                row+='O|'
            else:
                row+='X|'
        print(row)
    print('-------')  
def check_winner():
    global matrix,win
    for i in range(len(matrix)):
        s1=s2=d1=d2=1
        for j in range(len(matrix[i])):
            s1*=matrix[i][j]
            s2*=matrix[j][i]
        if s1==1 or s1==8 or s2==1 or s2==8:
            print('player',player, 'wins')
            win=True
    for i in range (len(matrix)):
        for j in range(len(matrix)):
            if i==j:
                d1*=matrix[i][j] 
            elif i+j==2:
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
