from game.point import Point


class BoardException(Exception):
    pass


class Board:
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns

        self._board = []
        self._side_to_move = 1

    @property
    def side_to_move(self):
        return self._side_to_move

    @property
    def rows(self):
        return self._rows

    @property
    def columns(self):
        return self._columns

    @property
    def board(self):
        return self._board

    def do_move(self, point):
        if self._side_to_move == 1:
            self._board[point.x][point.y] = 'X'
            self._side_to_move = 2
        else:
            self._board[point.x][point.y] = 'O'
            self._side_to_move = 1

    @property
    def available_moves(self):
        """
        the function that returns the amount of available moves to be made on the board
        :return: c -> number of available moves
        """
        c = 0
        for row in range(self.rows):
            for column in range(self.columns):
                if self._board[row][column] == '.':
                    c += 1
        return c

    def get_move_list(self):
        m = []
        for row in range(self.rows):
            for column in range(self.columns):
                if self._board[row][column] == '.':
                    m.append(Point(row, column))
        return m

    def execute_move(self, point):
        """
        the function that executes a move on the board
        :param point: the move to be executed, represented by its coordinates
        :return: None
        """
        self.validate_move(point)  # might raise a MoveError if the move is not valid
        self.do_move(point)
        self.mark_borders_of_move(point)

    def create_board(self):
        """
        the function that creates the beginning board
        :return: None
        """
        for row in range(self.rows):
            work_list = []
            for column in range(self.columns):
                work_list.append('.')
            self._board.append(work_list)

    def validate_move(self, point):
        """
        function that validates a move to be made
        :param point: the point where the move is intended to be done
        :return: None
        """
        if point.y < 0 or point.y >= self.columns or point.x < 0 or point.y >= self.rows:
            raise BoardException("Not a valid move! (outside the board)")
        if self._board[point.x][point.y] != '.':
            raise BoardException("Not a valid move! (too close to another point)")

    def mark_borders_of_move(self, point):
        """
        function that marks all the bordering squares of an already placed move
        :param point: the point where the move has been done
        :return: None
        """
        # * - occupied
        directions = [
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1)
        ]

        for d in directions:
            if not (point.y + d[1] < 0 or point.y + d[1] >= self.columns or
                    point.x + d[0] < 0 or point.x + d[0] >= self.rows):
                self.board[point.x + d[0]][point.y + d[1]] = "*"

    def __str__(self):
        """
        overriding the initial str to show a beautiful board <3
        :return: the string xD
        """
        s = "\nx\n"
        row_nr = 0
        for r in self._board:
            s += f"{row_nr} "
            for el in r:
                s += f"\t\t{el}"
            s += "\n"
            row_nr += 1
        s += "\n\t"
        for col_nr in range(0, len(self._board[0])):
            s += f"\t{col_nr}\t"
        s += "  y"
        return s
