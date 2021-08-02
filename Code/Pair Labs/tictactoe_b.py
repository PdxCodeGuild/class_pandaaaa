# https://github.com/PdxCodeGuild/class_pandaaaa/blob/master/1%20Python/labs/13%20Tic%20Tac%20Toe.md
# Theo and Brea
# Lab 13: Tic Tac Toe
class Player:
    def __init__(self,name='default',token=1):
        self.name = name
        self.token = token

class Game:
    def __init__(self,board=[],x=3,y=3) -> None:
        self.board = board
        self.x = x
        self.y = y
        self.board = [
            [7, 7, 7],
            [7, 7, 7],
            [7, 7, 7],
        ]

    def __str__(self) -> str:
        output = ''
        for i in range(self.y):
            for j in range(self.x):
                val = self.board[i][j]
                if val == 1:
                    output += 'X'
                elif val == 2:
                    output += 'O'
                else:
                    output += ' '
                if j != self.x-1:       #Avoids printing Divider over the edge!
                    output += '|'
            output += '\n'
        str(output)
        return output

    def __repr__(self) -> str:
        return self.__str__()
    
    def move(self,x,y,player):
        self.board[x-1][y-1] = player.token
        return self.board
    
    def calc_winner(self):
        total = self.calc_total()
        if total == 3:
            return 1
        elif total == 6:
            return 2
        else:
            return 0

    def calc_total(self):
        total = 0
        for i in range(self.y):             #Horizontal winner
            for j in range(self.x):
                total += self.board[i][j]
            if total  == 3 or total == 6:
                return total
            total = 0
        for i in range(self.x):             #Vertical winner
            for j in range (self.y):
                total += self.board[j][i]
            if total == 3 or total == 6:
                return total
            total = 0
        for i in range (self.x):            #Left-To-Right Diagonal
            total += self.board[i][i]
        if total == 3 or total == 6:
            return total
        total = 0
        
        i = 0
        j = 2
        while i < self.x:
            total +=self.board[i][j]
            i += 1
            j -= 1
        return total
        
    def is_full(self):
        for i in range(self.y):
            for j in range(self.x):
                if self.board[i][j] == 7:
                    return False
        return True


def main():
    p1 = Player('Theo',1)
    p2 = Player('Brea',2)
    board = Game()
    x = 0
    y = 0 

    while board.is_full() == False and board.calc_winner()!= 1 or board.calc_winner() != 2:
        print('Player 1: ')         #Player 1 move
        x = get_x()
        y = get_y()
        board.move(x,y,p1)
        print(board)
        if board.calc_winner() == 1:
            print(f"{p1.name} wins!")
            break
        elif board.is_full() == True:
            print("Stalemate!")    
            break
        print('Player 2: ')         #Player 2 move
        x = get_x()
        y = get_y()        
        board.move(x,y,p2)
        print(board)
        if board.calc_winner() == 2:
            print(f"{p2.name} wins!")
            break
        elif board.is_full() == True:
            print("Stalemate!")    
            break
    exit()

def get_x():
    return int(input("Input row position (1-3):"))

def get_y():
    return int(input("Input column position (1-3):"))

main()