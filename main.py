"""
1. кто играет
2. размер поля
3. кто первый ходит
4. ход оппонента
"""


class TicTacGame:
    def __init__(self):
        self._board = [[0 for _ in range(3)] for i in range(3)]
        self.cur_sign = int
        self._has_winner = bool
        self.tic_tac = {0: ' ', 1: 'x', 2: 'o'}

    def show_board(self):
        print("\nCurrent board:")
        print("  1 2 3")
        for num, i in enumerate(self._board):
            print(f"{num+1} "
                  f"{self.tic_tac[i[0]]} "
                  f"{self.tic_tac[i[1]]} "
                  f"{self.tic_tac[i[2]]}")

    def validate_input(self, user_string: str) -> bool:
        user_lst = user_string.split()
        if len(user_lst) != 2:
            print("You have to enter 2 values.\nTry again")
            return False
        if not user_lst[0].isnumeric() or not user_lst[1].isnumeric():
            print("Both values must be an integer\nTry again")
            return False

        row, col = list(map(int, user_lst))
        if 1 <= row <= 3 and 1 <= col <= 3:
            if self._board[row-1][col-1] == 0:
                return True
            else:
                print("This place is busy, choose another one\n")
                return False
        else:
            print("Number is out of bound!\nTry again")
            return False

    def check_win(self) -> bool:
        win_combo = [self.cur_sign for _ in range(3)]
        for row in self._board:
            if row == win_combo:
                return True
        for i in range(3):
            if [self._board[0][i], self._board[1][i], self._board[2][i]] == win_combo:
                return True
        if [self._board[i][i] for i in range(3)] == win_combo:
            return True
        if [self._board[i][2-i] for i in range(3)] == win_combo:
            return True

        return False

    @staticmethod
    def wrapper_turn(func):
        def wrapper(*args, **kwards):
            self = args[0]
            self.show_board()
            func(*args, **kwards)
            if self.check_win():
                self._has_winner = True
                print(f"\nHey! We have a winner!!!\nPlayer {self.cur_sign}, congratulations!!!")

        return wrapper

    @wrapper_turn
    def user_turn(self):
        turn_text = f"Player {self.cur_sign} your turn: "
        user_input = input(turn_text)
        if self.validate_input(user_input):
            row, col = list(map(int, user_input.split()))
            self._board[row-1][col-1] = self.cur_sign
        else:
            self.user_turn()

    @wrapper_turn
    def comp_turn(self, sign):
        pass

    def next_player(self):
        self.cur_sign = 2 if self.cur_sign == 1 else 1

    def mode_you_you(self):
        print("Nice! Next you need to enter your turn \nas two numbers from 1 to 3 in order 'row column'")
        while not self._has_winner:
            self.user_turn()
            self.next_player()
        print("\nEnd of game. Goodbye!\nHave a good day!")

    def mode_you_computer(self):
        while True:
            self.user_turn(1)
            self.comp_turn(2)

    def mode_comp_comp(self):
        while True:
            self.comp_turn(1)
            self.comp_turn(2)

    def start_game(self):
        hello_text = ("Hello! It's a tic tac game!\nChoose the mode what you want to play\n"
                      "1. You against computer\n"
                      "2. You against your friend\n"
                      "3. Computer against computer\n"
                      "Enter a number of mode: ")
        mode_game = input(hello_text)
        self._has_winner = False
        self.cur_sign = 1

        if mode_game == "1":
            self.mode_you_computer()
        elif mode_game == "2":
            self.mode_you_you()
        elif mode_game == "3":
            self.mode_comp_comp()
        else:
            print("Invalid input!\nLet's try again\n")
            self.start_game()


if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()
