import random

from game.board import Board, BoardException
from game.point import Point
from game.ai import AI


class UserInterface:
    def __init__(self, r, c, m, t):
        self._board = Board(r, c)
        self._board.create_board()

        self._mode = m
        self._ai_turn = t
        self._running = True

    def print_board(self):
        print(self._board)

    def print_turn(self):
        print(f"\nPlayer {self._board.side_to_move} to move.\n")

    @staticmethod
    def get_input():
        x = int(input("The X coordinate: "))
        y = int(input("The Y coordinate: "))

        return Point(x, y)

    def start(self):
        while self._running:
            self.print_board()
            self.print_turn()

            try:
                if mode.strip().lower() == "computer" and self._board.side_to_move == self._ai_turn:
                    input_point = AI.get_input(self._board)
                else:
                    input_point = UserInterface.get_input()

                t_side = self._board.side_to_move
                self._board.execute_move(input_point)
                if not self._board.available_moves:
                    self._running = False

                    print(self._board)
                    print(f"Player {t_side} wins")
            except ValueError:
                print("Invalid move")
            except BoardException as be:
                print(be)


if __name__ == "__main__":
    rows = None
    columns = None
    while rows is None:
        try:
            rows = int(input("Introduce number of rows: "))
        except ValueError as e:
            print("Invalid input")

    while columns is None:
        try:
            columns = int(input("Introduce number of columns: "))
        except ValueError as e:
            print("Invalid input")
    with open("settings.properties", "r") as f:
        mode = f.readline().split(" ")[2]
    ui = UserInterface(rows, columns, mode, 1)
    ui.start()
