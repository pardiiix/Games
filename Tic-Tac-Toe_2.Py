# -*- coding: utf-8 -*-
"""
Created on August 24th, 2017

@author: Pardis Ranjbar
E-mail: pardis.ranjbar@gmail.com
#==============================================================================
# This is a code of a Tic-Tac-Toe game.
#==============================================================================
"""
class Game(object):
    def __init__(self): #initializer
        self.player=1 #player 1 starts
        self.win=False #at first there is no winner
        self.matrix=[[0,0,0] for i in range(3)] #an empty square matrix with a size of 3
        self.x=None
        self.y=None
    def print_emptyboard(self): #prints the empty board with no components
        for i in range(3): #three rows and columns are created
            print('-------') 
            row='| | | |'
            print(row)
        print('-------') #prints the 4th line
        print('Player 1') #to indicate that the game starts with player 1
    def print_board(self): #prints the board after a component is given
        for i in range(len(self.matrix)):
            print('-------') #the first line
            row='|' #the first border
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j]==0: #if no input has been given yet
                    row+=' |' #an empty space and it's border should be added to row
                elif self.matrix[i][j]==2: #if player 2 enters a coordinate
                    row+='O|'
                else:
                    row+='X|'
            print(row) # prints a completed row with X's and O's
        print('-------')  
    def check_winner(self):
        for i in range(len(self.matrix)):
            s1=s2=d1=d2=1
            for j in range(len(self.matrix[i])):
                s1*=self.matrix[i][j] #s1 is the multiplication of a row
                s2*=self.matrix[j][i] #s2 is the multiplication of a column
            if s1==1 or s1==8 or s2==1 or s2==8:
                print('player',self.player, 'wins')
                self.win=True
        for i in range (len(self.matrix)):
            for j in range(len(self.matrix)):
                if i==j:
                    d1*=self.matrix[i][j] 
                if i+j==2:
                    d2*=self.matrix[i][j]
        if d1==1 or d1==8 or d2==1 or d2==8:
                print('player',self.player, 'wins')
                self.win=True
    def select_place(self):
        self.x=int(input('enter X position:\n'))
        self.y=int(input ('enter Y position:\n'))
    def set_selected_place(self):
        self.matrix[self.x][self.y]=(self.player)
    def boardisfull(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if (self.matrix[i][j]==0):
                    return False
        return True
        print('Game over')
    def winner(self):
        return self.win
    def switch_player(self):
        self.player=2 if self.player==1 else 1
        print('Player', self.player)

game = Game()
game.print_emptyboard()
while True:
    while not game.boardisfull() and not game.winner():
        game.select_place()
        game.set_selected_place()
        game.print_board()
        game.check_winner()
        game.switch_player()
print('Game Over!\n')
