import numpy as np

class Tictoe:
    def __init__(self, size):
        self.size = size
        self.board = [['.', '.', '.'], 
                      ['.', '.', '.'], 
                      ['.', '.', '.']]        

        self.player_turn = 'O'
        self.win_move = [['O','O','O']]
        self.lose_move = [['X','X','X']]

    
    def draw_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(self.board[i][j]), end=" ")
            print()
        print()

    def get_next_move(self):
        move = []
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == '.':
                    move.append([i,j])
        return move


    def is_full(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == '.':
                    return False
        return True


    def get_board_state(self):
        # horizontal
        for i in range(0, 3):
            if self.board[i] in self.win_move:
                return 'win'
            if self.board[i] in self.lose_move:
                return 'lose'
        # vertical
        for i in range(0, 3):
            row = []
            for j in range(0, 3):
                row.append(self.board[j][i])
            if row in self.win_move:
                return 'win'            
            if row in self.lose_move:
                return 'lose'

        # diagonal
        d1 = []
        d2 = []
        for i in range(0, 3):
            d1.append(self.board[i][i])        
        for i in range(0, 3):
            d2.append(self.board[i][2-i])

        if d1 in self.win_move or d2 in self.win_move:
            return 'win'
        if d1 in self.win_move or d2 in self.lose_move:
            return 'lose'

        if self.is_full():
            return 'tie'

        return 'playing'


def main():
    tictoe = Tictoe(3)
    tictoe.draw_board()
    tictoe.get_board_state()



if __name__ == "__main__":
    main()

