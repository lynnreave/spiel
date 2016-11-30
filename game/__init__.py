################################################################################
#
# Author(s): Sephone Slattery (based off "Invent with Python" example,
#   https://inventwithpython.com/chapter10.html)
# Summary: A module including methods for executing the tic-tac-toe game.
#
################################################################################

################################################################################
# Import #######################################################################
################################################################################
################################################################################

import random

################################################################################
# Globals ######################################################################
################################################################################
################################################################################

################################################################################
# Game #########################################################################
################################################################################
################################################################################


class Game:
    """ Submodule for executing the tic-tac-toe game """

    def __init__(self):
        """
        """

        return

    def choose_random_move_from_list(self, board, moves_list):
        """ Return a valid move from the passed list on the passed board.
        :param board: a list of 10 strings representing the board
            (ignores index 0).
        :param moves_list:
        :return: an int representing board space (index)
            or None if no valid move available.
        """

        possibleMoves = []
        for i in moves_list:
            if self.is_space_free(board, i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    def draw_board(self, board):
        """ Print out the board.
        :param board: a list of 10 strings representing the board
            (ignores index 0).
        """

        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')

        return

    def get_computer_move(self, board, computer_letter):
        """ Given a board and the computer's letter, determine where to move
            and return that move.
        :param board: a list of 10 strings representing the board
            (ignores index 0).
        :param computer_letter:
        :return: an int representing board space (index)
            or None if no valid move available.
        """

        if computer_letter == 'X':
            playerLetter = 'O'
        else:
           playerLetter = 'X'
        # Here is our algorithm for our Tic Tac Toe AI:
        # First, check if we can win in the next move
        for i in range(1, 10):
             copy = self.get_board_copy(board)
             if self.is_space_free(copy, i):
                 self.make_move(copy, computer_letter, i)
                 if self.is_winner(copy, computer_letter):
                     return i

        # Check if the player could win on their next move, and block them.
        for i in range(1, 10):
            copy = self.get_board_copy(board)
            if self.is_space_free(copy, i):
                self.make_move(copy, playerLetter, i)
                if self.is_winner(copy, playerLetter):
                    return i

        # Try to take one of the corners, if they are free.
        move = self.choose_random_move_from_list(board, [1, 3, 7, 9])
        if move != None:
            return move

        # Try to take the center, if it is free.
        if self.is_space_free(board, 5):
            return 5

        # Move on one of the sides.
        return self.choose_random_move_from_list(board, [2, 4, 6, 8])

    def get_board_copy(self, board):
        """ Make a duplicate of the board list and return.
        :param board: a list of 10 strings representing the board
            (ignores index 0).
        :return: a duplicate board list.
        """

        dupeBoard = []

        for i in board:
            dupeBoard.append(i)

        return dupeBoard

    def get_player_move(self, board):
        """ Let the player type in their move.
        :param board: a list of 10 strings representing the board
            (ignores index 0).
        :return: int representing board space (index in list, starting with 1).
        """

        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or \
                not self.is_space_free(board, int(move)):
            print('What is your next move? (1-9)')
            move = raw_input()
        return int(move)

    def input_player_letter(self):
        """ Lets the player type which letter they want to be.
        :return: a list with the player's letter as the first item, and the
            computer's letter as the second.
        """

        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want to be X or O?')
            letter = raw_input().upper()

        # the first element in the list is the player's letter,
        #   the second is the computer's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def is_board_full(self, board):
        """ Determine if the board is full or not.
            Otherwise return False.
        :param board: a list of 10 strings representing the board
            (ignores index 0).
        :return: True if every space on the board has been taken, otherwise False.
        """

        for i in range(1, 10):
            if self.is_space_free(board, i):
                return False
        return True

    def is_space_free(self, board, move):
        """ Determine whether specified board space is free or not.
        :param board: a list of 10 strings representing the board
            (ignores index 0).
        :param move: the board space (index starting with 1) to place letter on.
        :return: True if the space is free, False if not.
        """

        return board[move] == ' '

    def is_winner(self, bo, le):
        """ Given a board and a player's letter, determine if the player has won.
        :param bo: a list of 10 strings representing the board
            (ignores index 0).
        :param le: the letter of the player.
        :return: True if specified letter/player has one, False if not.
        """

        return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

    def make_move(self, board, letter, move):
        """ Commit player move.
        :param board: a list of 10 strings representing the board
            (ignores index 0).
        :param letter: the letter of the player.
        :param move: the board space (index starting with 1) to place letter on.
        """

        board[move] = letter

    def play_again(self):
        """ Ask the player to play again or not.
        :return: a boolean expressing True to play again, False if not.
        """

        print('Do you want to play again? (yes or no)')

        return raw_input().lower().startswith('y')

    def play(self):
        """ Run the main loop to play the game.
        """
        print('Welcome to Tic Tac Toe!')

        while True:
            # Reset the board
            theBoard = [' '] * 10
            playerLetter, computerLetter = self.input_player_letter()
            turn = self.who_goes_first()
            print('The ' + turn + ' will go first.')
            gameIsPlaying = True

            while gameIsPlaying:
                if turn == 'player':
                    # Player's turn.
                    self.draw_board(theBoard)
                    move = self.get_player_move(theBoard)
                    self.make_move(theBoard, playerLetter, move)
                    if self.is_winner(theBoard, playerLetter):
                        self.draw_board(theBoard)
                        print('Hooray! You have won the game!')
                        gameIsPlaying = False
                    else:
                        if self.is_board_full(theBoard):
                            self.draw_board(theBoard)
                            print('The game is a tie!')
                            break
                        else:
                            turn = 'computer'

                else:
                    # Computer's turn.
                    move = self.get_computer_move(theBoard, computerLetter)
                    self.make_move(theBoard, computerLetter, move)

                    if self.is_winner(theBoard, computerLetter):
                        self.draw_board(theBoard)
                        print('The computer has beaten you! You lose.')
                        gameIsPlaying = False
                    else:
                        if self.is_board_full(theBoard):
                            self.draw_board(theBoard)
                            print('The game is a tie!')
                            break
                        else:
                            turn = 'player'

            if not self.play_again():
                break

        return

    def who_goes_first(self):
        """ Randomly choose who goes first.
        :return: the string name of the first player.
        """

        if random.randint(0, 1) == 0:
            return 'computer'
        else:
            return 'player'