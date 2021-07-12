# Lab 13: Tic-Tac-Toe
# Tic Tac Toe is a game. Players take turns placing tokens (a 'O' or 'X') into a 3x3 grid. 
# Whoever gets three in a row first wins.

def main():
    my_game = game()
    player_1 = player('ash','x') 
    #player_2 = player()
    my_game.move(0,1,player_1)

    my_game.print_board()
    return 0


# You will write a Player class and Game class to model Tic Tac Toe,
#  and a function main that models gameplay taking in user inputs through REPL.
class player():
    def __init__(self, my_name, my_token):
        self.name = my_name 
        self.token = my_token
    
    #interface for inputting move
    def player_input(self):
        return 0

    def get_token(self):
        return self.token


class game():
    def __init__(self):
       self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
   
       #[x, y]



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
        #print(self.board)



    #this function will be used for changings 0s to Xs
        # move(x, y, player) Place a player's token character string at a 
        # given coordinate (top-left is 0, 0), x is horizontal position, 
        # y is vertical position.

        # >>> board.move(2, 1, player_1)
        #  | | 
        #  | |X
        #  | |
    def move(self, x, y, player):
        if player.get_token() == 'X':
            self.board[x][y] = 'X'
        elif player.get_token() == '0':
            self.board[x][y] = '0'
    # calc_winner() What token character string has won or None if no one has.
    # X| | 
    # O|X|O
    #  | |X
    # >>> board.calc_winner()
    # X
    def calc_winner(self):
        return 0


    # is_full() Returns true if the game board is full.
    # X|O|X
    # X|X|O
    # O|O|X
    # >>> board.is_full()
    # True
    def is_full():
        return True


    # move(x, y, player) Place a player's token character string at a 
    # given coordinate (top-left is 0, 0), x is horizontal position, 
    # y is vertical position.
    # X|O|
    #  | |X
    #  | |
    # >>> board.is_game_over()
    # False
    def is_game_over():
        return 0

main()