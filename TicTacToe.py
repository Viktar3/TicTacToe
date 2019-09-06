import random

class TicTacToe:

    _board =[['-','-','-'],
             ['-','-','-'],
             ['-','-','-']]

    _human = 'X'

    _computer = 'O'


    def do_move(self, player, x, y):
        self._board[x][y] = player

    def has_won(self, player):

        if self._board[0][0] == player and self._board[0][1] == player and self._board[0][2] == player:
            return True
        if self._board[1][0] == player and self._board[1][1] == player and self._board[1][2] == player:
            return True
        if self._board[2][0] == player and self._board[2][1] == player and self._board[2][2] == player:
            return True
        if self._board[0][0] == player and self._board[1][0] == player and self._board[2][0] == player:
            return True
        if self._board[0][1] == player and self._board[1][1] == player and self._board[2][1] == player:
            return True
        if self._board[0][2] == player and self._board[1][2] == player and self._board[2][2] == player:
            return True
        if self._board[0][0] == player and self._board[1][1] == player and self._board[2][2] == player:
            return True
        if self._board[2][0] == player and self._board[1][1] == player and self._board[2][0] == player:
            return True
        else:
            return False


    def do_computer_turn(self):
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        while self._board[x][y] != "-":
            x = random.randint(0, 2)
            y = random.randint(0, 2)

        self.do_move(self._computer, x, y)

    def pretty_print_board(self):
        for x in range(0, len(self._board)):
            pass

        print(self._board[0][0] + " | " + self._board[0][1] + " | " + self._board[0][2])
        print(self._board[1][0] + " | " + self._board[1][1] + " | " + self._board[1][2])
        print(self._board[2][0] + " | " + self._board[2][1] + " | " + self._board[2][2])

        print("\n")


    def print_victory(self, player):

        print("{} has won the battle".format(player))


    def _get_sanitized_input(self):

        while True:
            input_value = input("Please enter a location (example -> A2)\n")

            x = input_value[0].lower()
            y = input_value[1].lower()

            if x not in ['a', 'b', 'c']:
                print('Please try again. Values must be A1-3, B1-3, or C1-3 (i.e. A3)')
                continue
            
            if y.lower() not in ['1', '2', '3']:
                print('Please try again. Values must be A1-3, B1-3, or C1-3 (i.e. A3)')
                continue

            if x == 'a':
                x = 0
            if x == 'b':
                x = 1
            if x == 'c':
                x = 2

            if y == '1':
                y = 0
            if y == '2':
                y = 1
            if y == '3':
                y = 2

            if self._board[x][y] != "-":
                print("Pick an empty location!\n")
                continue

            return x,y

        # Should not get to this point
        return 0,0

    def _reset(self):
        self._board = [['-','-','-'],
                       ['-','-','-'],
                       ['-','-','-']]


    def _start(self):
        self._reset()
        cur_player = self._human
        other_player = self._computer

        self.pretty_print_board()

        while True:
            if cur_player == self._human:
                x,y = self._get_sanitized_input()
                self.do_move(cur_player, x, y)
                
            else:
                self.do_computer_turn()        
            
            self.pretty_print_board()

            if self.has_won(cur_player):
                self.print_victory(cur_player)
                return

            tmp = cur_player
            cur_player = other_player
            other_player = tmp


    def start(self):
        while True:
            input_val = input("You ready to play? (Y/N)\n")
            if input_val.lower() == "y":
                self._start()
            else:
                break

        print("Thanks for playing!")

if __name__ == '__main__':
    ticTacToe = TicTacToe()
    ticTacToe.start()

