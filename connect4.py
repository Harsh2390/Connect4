import random
import os
#dimensions of our board
BOARD_COLS = 7
BOARD_ROWS = 6

# I'm using oop class it is really helpful while accessing the things in bunch of the code
class connect4():

    def __init__(self):
        self.board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]#creating the board
        #here I'm creating a list to chose the turn randomly from random library
        TU = [0, 1]
        self.turns = random.choice(TU) #I use random.choice method to select an element randomly from the list
        self.last_move = [-1, -1] # [r, c]

    def print_board(self):
        print("\n")
        # mark the columns separately to keep it cleaner
        for r in range(BOARD_COLS):
            col_no  = chr(r+65)
            print('    ' + col_no , end=' ')
        print("\n +" + "-----+" * BOARD_COLS)

        # Print the slots of the game board
        for r in range(BOARD_ROWS):
            print(' |', end="")
            for c in range(BOARD_COLS):
                print(f"  {self.board[r][c]}  |", end="")
            print("\n +"+"-----+"*BOARD_COLS)
     # below line will print the margin
        print(f"{'-' * 44}\n")
#players list or their character's list
    def which_turn(self):
        
        players = ['X', 'O']
        return players[self.turns % 2]

    def in_bounds(self, r, c):
        return (r >= 0 and r < BOARD_ROWS and c >= 0 and c < BOARD_COLS)

    def turn(self, column):
        # Search bottom up for an open slot
        for i in range(BOARD_ROWS-1, -1, -1):
            if self.board[i][column] == ' ':
                self.board[i][column] = self.which_turn()
                self.last_move = [i, column]

                self.turns += 1
                return True

        return False

    def check_winner(self):
        last_row = self.last_move[0]
        last_col = self.last_move[1]
        last_letter = self.board[last_row][last_col]

        # [r, c] direction, matching letter count, locked boolean
        directions = [[[-1, 0], 0, True],
                      [[1, 0], 0, True],
                      [[0, -1], 0, True],
                      [[0, 1], 0, True],
                      [[-1, -1], 0, True],
                      [[1, 1], 0, True],
                      [[-1, 1], 0, True],
                      [[1, -1], 0, True]]
     #
        # Search outwards looking for matching pieces
        for a in range(4):
            for d in directions:
                r = last_row + (d[0][0] * (a+1))
                c = last_col + (d[0][1] * (a+1))

                if d[2] and self.in_bounds(r, c) and self.board[r][c] == last_letter:
                    d[1] += 1
                else:
                    # Stop searching in this direction
                    d[2] = False

        # Check possible direction pairs for '4 pieces in a row'
        # here also we can change the costant according to the number of rows and column
        for i in range(0, 7, 2):
            if (directions[i][1] + directions[i+1][1] >= 3):
                self.print_board()
                print(f"congratulations {last_letter} is the winner!")
                return last_letter

        #if this block of code Did not find any winners
        return False

def play():
    # Initialize the game board
    game = connect4()

    game_over = False
    while not game_over:
        #os.system("cls") for windows
        os.system("clear") #clean the terminal to show the next board
        game.print_board()

        # Ask the user for input, but only accept valid inputs Betweeen A and
        valid_move = False
        while not valid_move:
            user_move1 = input(f"{game.which_turn()}'s Turn - pick a column (A-G): ")

            user_move = ord(user_move1)-65
            try:
                valid_move = game.turn(int(user_move))
            except:
                print(f"invalid input \n Please choose a letter Between A and G")#change the letters according to the no. of columns

        #we have to End the game if there is a winner
        game_over = game.check_winner()

        #plus we have to End the game if there is a tie
        if not any(' ' in x for x in game.board):
            print("Both of the player got equal points")
            return


play()
