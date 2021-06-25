# https://github.com/PdxCodeGuild/class_pandaaaa/blob/master/1%20Python/labs/13%20Tic%20Tac%20Toe.md
# Theo and Brea
# Lab 13: Tic Tac Toe

class Game:
    def __init__(self,board={'x':[],'y':[]},x=3,y=3) -> None:
        self.board = board
        self.x = x
        self.y = y
        for i in range(x):
            board['x'].append(' ')
        for i in range(y):
            board['y'].append(' ')

    def __str__(self) -> str:
        output = ''
        for y in self.board['y']:                   #Rows
            for x in range(len(self.board['x'])):   #Colums
                output += self.board['x'][x]
                if x != len(self.board['x'])-1:
                    output += '|'
            output += '\n'
        str(output)
        return output

    def __repr__(self) -> str:
        return f'Game({self},{self.board},{self.x},{self.y})'

board = Game()
print(board)