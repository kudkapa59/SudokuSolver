"""
This program implements the solution of the well-known puzzle game Sudoku.
Any interested can use his example of not yet unsolved sudoku and try it.
Otherwise, it's possible to use our example of board.
"""

class SudokuSolver():
    """
    This class takes an input of a sudoku board. 
    The board must be in the form of list of lists. Zeros in this matrix will mean 
    numbers the program needs to find.
    """
    def __init__(self,board):
        self.board = board

    def empty_cell(self):
        """
        Returns the position of the first found empty cell.
        Returns None in case of the occupied board.
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return [i,j]
        return None

    def number_check(self,value,loc):
        """
        Checks if a value is valid for this position.
        Looks through the row, the column and 3x3 block of
        given cell.

        Returns: 
                True in case of validity
                False otherwise.
        """
        for i in range(len(self.board[0])): #Check row
            if self.board[loc[0]][i] == value and i != loc[1]:
                return False

        for j in range(len(board)): #Check column
            if self.board[j][loc[1]] == value and j != loc[0]:
                return False

        block_x = loc[1] // 3
        block_y = loc[0] // 3
        for y in range(block_y * 3, block_y * 3 + 3):#Check 3x3 block
            for x in range(block_x * 3, block_x * 3 + 3):
                if self.board[y][x] == value and [y,x] != loc:
                    return False

        return True
    
    def sudoku_show(self):
        """
        Prints the sudoku board.
        """
        for i in range(len(self.board)):
            if i%3 == 0 and i != 0:
                print("- - - - - - - - - -")
            for j in range(len(self.board[i])):
                if j%3 == 0 and j != 0:
                    print("|",end = "")
                if j > 7:
                    print(self.board[i][j])
                else:
                    print(self.board[i][j],end = " ")
    
    def solve(self):
        """
        Attempts to solve the board by inserting into an empty cell
        a digit. If it suits, the function proceeds to find empty cells.
        In case of not solvable situation, it will nullify the original cell
        and assign it a new digit.

        Returns:
                True: all cells are solved rightly.
                False: given value is wrong. Need to backtrack to the original
                cell.
        """
        self.empty = self.empty_cell()
        if not self.empty:
            return True

        res = False
        y,x = self.empty
        nums = list(range(1,10))

        for n in nums:
            if self.number_check(n,[y,x]):
                self.board[y][x] = n
                if self.solve():
                    res = True
                else:
                    self.board[y][x] = 0
                    res = False
        return res


board1 = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
board = [
    [0,7,3,8,0,0,2,9,0],
    [0,0,2,3,0,0,0,0,0],
    [0,0,1,6,0,0,0,0,0],
    [0,6,0,7,0,3,1,8,0],
    [0,0,0,0,0,0,0,0,5],
    [0,3,0,0,0,1,7,2,0],
    [9,1,0,0,0,0,0,5,3],
    [3,8,0,1,0,0,0,7,2],
    [0,0,0,0,3,0,6,0,0]
]


if __name__ == '__main__':
    sud = SudokuSolver(board)
    print('Starting board')
    print('\n')
    sud.sudoku_show()
    print('--------------------')
    print('\n')
    print('Solved board')
    print('\n')
    sud.solve()
    sud.sudoku_show()
