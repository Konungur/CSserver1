from arrays import Array2D
from lliststack import Stack

class Maze :
    MAZE_WALL = " *"
    PATH_TOKEN = "x"
    TRIED_TOKEN = "o"

    def __init__( self, num_rows, num_cols ):
        self._mazeCells = Array2D( num_rows, num_cols )
        self._startCell = None
        self._exitCell = None

    def num_rows( self ):
        return self._mazeCells.num_rows()

    def num_cols( self ):
        return self._mazeCells.num_cols()

    def setWall( self, row, col ):
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._mazeCells[row, col] = self.MAZE_WALL

    def setStart( self, row, col ):
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._startCell = _CellPosition( row, col )

    def setExit( self, row, col ):
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._exitCell = _CellPosition( row, col )


    def findPath( self ):
        stack_path = Stack()
        stack_path.push(self._startCell) 
        while not stack_path.isEmpty():
            use_cell = stack_path.pop()
            self._markTried(use_cell.row, use_cell.col)
            if use_cell.row == self._exitCell.row and use_cell.col == self._exitCell.col:
                use_cell.path.append(use_cell)
                for i in use_cell.path:
                    self._markPath(i.row, i.col)
                return True
            if self._validMove(use_cell.row + 1, use_cell.col):
                stack_path.push(_CellPosition( use_cell.row + 1, use_cell.col, use_cell ))
            if self._validMove(use_cell.row - 1, use_cell.col):
                stack_path.push(_CellPosition(use_cell.row - 1, use_cell.col, use_cell))
            if self._validMove(use_cell.row, use_cell.col + 1):
                stack_path.push(_CellPosition(use_cell.row, use_cell.col + 1, use_cell))
            if self._validMove(use_cell.row, use_cell.col - 1):
                stack_path.push(_CellPosition(use_cell.row, use_cell.col - 1, use_cell))
        return False

    def reset( self ):
        for i in range(self.num_rows()):
            for j in range(self.num_cols()):
                if self._mazeCells[i, j] == self.TRIED_TOKEN:
                    self._mazeCells[i, j] = None

                elif self._mazeCells[i, j] == self.PATH_TOKEN:
                    self._mazeCells[i, j] = None


    def draw( self ):
        for i in range(self.num_rows()):
            for j in range(self.num_cols()):
                if self._mazeCells[i, j] is None:
                    self._mazeCells[i, j] = "  "
                print(self._mazeCells[i, j], end="")
            print("  ")


    def _validMove( self, row, col ):
        return row >= 0 and row < self.num_rows() \
               and col >= 0 and col < self.num_cols() \
               and self._mazeCells[row, col] is None


    def _exitFound( self, row, col ):
        return row == self._exitCell.row and col == self._exitCell.col


    def _markTried( self, row, col ):
        self._mazeCells[row, col] = self.TRIED_TOKEN

    def _markPath( self, row, col ):
        self._mazeCells[row, col] = self.PATH_TOKEN


class _CellPosition( object ):
    def __init__( self, row, col ):
        self.row = row
        self.col = col
