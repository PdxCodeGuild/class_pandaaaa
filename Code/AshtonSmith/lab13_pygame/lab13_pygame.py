# Ashton Smith
# Zach Watts
# Lab 13: Tic-Tac-Toe
# Tic Tac Toe is a game. Players take turns placing tokens (a 'O' or 'X') into a 3x3 grid. 
# Whoever gets three in a row first wins.

#this version of lab13 uses pygames

import pygame
screen = pygame.display.set_mode((800,600)) #args: height, width
#background
background = pygame.image.load('background.png')

#Title and icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)


w, h = pygame.display.get_surface().get_size()
screen = pygame.display.set_mode((800,600))
tokens_dict = {
    #Symbol : in use?(T/F)
    'X':False,
    '0':False
}



#player has to control a little alien 
#   alien
#   #


###########################GAME####CLASS################################



class game_main():



    player_png = pygame.image.load('player.png')
    player_x = 0
    player_y = 0
    player_x_change = 0
    
    
    
    #initalization    
    def __init__(self):
        background_image = ''

    #this function uses the py gamefunction blit to draw the player
    def background(background_image):
        screen.pygame.blit(background_image)


    #this function uses the py gamefunction blit to draw the player
    #   args: x coordinate, y coordinate 
    def player(player_x, player_y):
        screen.pygame.blit(player_x,player_y)



    #this function draws the background image
    def background(background_image):
        screen.pygame.blit(str(background_image))

    #if player is within region range
    #args: player(x, y) boundary(x,y)
    #the regionswitch is used to determine what to multiply x and y by for the region
    def player_within_region(player_x, player_y, bound_x, bound_y, regionswitch):
        
        #used to determine what to multiply x and y by enorder to not require a function for each region
        region_key = {
            #0:1,#key: 
            1:90,#need to find what to multiply by for each region
            2:180,
            3:270,
            4:360,
        }
        #need to dertmine the paramaters for each region to select that region .. (the place on the screen) = the choice for tictactoe
        option = player_x < bound_x *regionswitch
        something = 'placeholder'
        if option == something:
            return True
        else:
            return False
            



########################################################################



#main
def main():
    my_game = game()
    player_1_name = player_input_name()
    player_1_token = player_input_token()
    player_1 = player(player_1_name,player_1_token) 

    player_2_name = player_input_name()
    player_2_token = player_input_token()
    player_2 = player(player_2_name,player_2_token) 
 
    curr_player = 1
    position_x = ''
    position_y = ''
    result = ''
    is_full = False 
    while not(is_full):
        valid_position = False
        my_game.print_board()
        result = str(my_game.calc_winner())
        if result == 'x':
            print('X Wins')
            break
        elif result == '0':
            print('0 Wins')
            break
        elif curr_player == 1: 
            while not valid_position:
                print('Player 1\nSymbol :' + player_1.token)
                position_y = int(prompt_column())
                position_x = int(prompt_row())        
                valid_position = my_game.move(position_x,position_y,player_1)
            curr_player = 2
        elif curr_player == 2: 
            while not valid_position:
                print('Player 2\nSymbol :' + player_2.token)
                position_y = int(prompt_column())
                position_x = int(prompt_row())
                valid_position = my_game.move(position_x,position_y,player_2)
            curr_player = 1
        is_full = my_game.is_full()
    my_game.print_board()
    return 0



#this function prompts the user for the row and returns it as a string
def prompt_row():
    return str(input('Enter the row: 0-2'))



#this function prompts the user for the column and returns it as a string
def prompt_column():
    return str(input('Enter the column: 0-2'))



#this function returns true if the number is between 0 and 2 else false
def is_valid_num(num):
    try:
        num = int(num)
        if 0 <= num <= 2:
            return True
    except ValueError:
        pass
    return False



#input player name
def player_input_name():
    return input('Enter your name: ')



#input player token
def player_input_token():
    global tokens_dict
    again = True
    token = '' 
    while(again):
        token = str(input('What token do you want to use? X or 0'))
        if(token == 'X' or token == '0'):
            if(tokens_dict[token] == False):
                again = False
                tokens_dict[token] = True 
            else:
                tokens_dict[token] = False
    return token



# You will write a Player class and Game class to model Tic Tac Toe,
#  and a function main that models gameplay taking in user inputs through REPL.
class player():
    def __init__(self, my_name, my_token):
        self.name = my_name 
        self.token = my_token



    #interface for inputting move
    def player_input(self):
        return 0


    #this function returns the token (x/0)
    def get_token(self):
        return self.token


class game():
    def __init__(self):
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] #empty
        self.moves = 0 



    #this function (returns/prints)? a printable version of the board
    def print_board(self):
        for i in self.board: # i each least [[i],[i],[i]]
            z = 0
            for j in i: #j [[j,j,j],[j,j,j],[j,j,j]]
                if z == 2:
                    print(j, end = '')
                else:
                    print (j, end = '|')
                z += 1
            print('')



    #this function will be used for changings 0s to Xs
        # move(x, y, player) Place a player's token character string at a 
        # given coordinate (top-left is 0, 0), x is horizontal position, 
        # y is vertical position.
    def move(self, x, y, player):
        if self.board[x][y] == ' ':
            if player.get_token() == 'X':
                self.board[x][y] = 'X'
            elif player.get_token() == '0':
                self.board[x][y] = '0'
            self.moves += 1
            return True
        else:
            return False
        
    
    
    # calc_winner() What token character string has won or None if no one has.
    #return None = no winner
    #return x = player 1
    #return 0 = player 2
    def calc_winner(self):
        #if there are 5 on the board
        if (self.moves < 5):
            return None 
        
        #if diagnol - first check mid
        diag_counter_0 = 0
        diag_counter_x = 0
        #check middle
        if (self.board[0][0] == self.board[1][1] == self.board[2][2]):
            if(self.board[0][0] == 'X'):
                return 'x'
            elif(self.board[0][0] == '0'):
                return '0'
        if (self.board[2][0] == self.board[1][1] == self.board[0][2]):
            if(self.board[2][0] == 'X'):
                return 'x'
            elif(self.board[2][0] == '0'):
                return '0'
        if(diag_counter_0 == 3):
            return '0'
        if(diag_counter_x == 3):
            return 'x'

        #if horizontal - all in one list are the same
        for i in self.board: #each row
            counter_x = 0
            counter_0 = 0
            for j in i:
                if(j == 'X'): 
                    counter_x += 1
                if(j == '0'):
                    counter_0 += 1
                if counter_x == 3:
                    return 'x'
                elif counter_0 == 3:
                    return '0'

        #if vertical
        for i in range(3):
            counter_x = 0
            counter_0 = 0
            for j in range(3):
                if(self.board[j][i] == 'X'):
                    counter_x += 1
                elif(self.board[j][i] == '0'):
                    counter_0 += 1
                if counter_x == 3:
                    return 'x'
                elif counter_0 == 3:
                    return '0'



        
    #if there is room for another move
    def is_full(self):
        if(self.moves == 9):
            return True



main()