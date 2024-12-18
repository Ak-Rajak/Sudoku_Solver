N = 9 # Store a numbner in given row or column number initally 9

# Function to check if the number is present in the row or column is safe
def isSafe(sudoku, row, col, num):
    for i in range(9):
        if sudoku[row][i] == num:
            return False
    for i in range(9):
        if sudoku[i][col] == num:
            return False

    # check num present in the 3x3 grid or not
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if sudoku[startRow + i][startCol + j] == num:
                return False
    # If all above condition are checked then return True
    return True

# Solve sudoku function - which assign values to all non assign locations

def solveSudoku(sudoku,startRow,startCol):
    # Base condition for the recursion
    if startRow == N - 1 and startCol == N:
        return True
    
    # Last col is reachjed then go to next row
    if startCol == N:
        startRow += 1
        startCol = 0
    
    # check if Number is assign to current location.
    if sudoku[startRow][startCol] > 0:
        return solveSudoku(sudoku,startRow,startCol+1)
    
    # Check for each number from 1 to 9
    for num in range(1,N+1):
        # Check if number is safe to assign
        if isSafe(sudoku,startRow,startCol,num):
            sudoku[startRow][startCol] = num
            # possibility for next column
            if solveSudoku(sudoku,startRow,startCol+1):
                return True
        
        # If number is not safe then assign 0 to the location
        sudoku[startRow][startCol] = 0
    return False


# Fixed a bug that caused the solver to hang (due to recursion) when an unsolvable/Invalid sudoku was entered, ensuring smoother functionality.
def isValidSudoku(board):
    for i in range(9):
        # create empty dictionaries to keep track of row, column, and block values
        row = {}
        column = {}
        block = {}
        # calculate the starting index of the current 3x3 block
        row_cube = 3 * (i//3)
        column_cube = 3 * (i%3)
        for j in range(9):
            # check if the value in the current cell of the row is valid
            if board[i][j]!=0 and board[i][j] in row:
                return False
            row[board[i][j]] = 1  # add the value to the row dictionary
            
            # check if the value in the current cell of the column is valid
            if board[j][i]!=0 and board[j][i] in column:
                return False
            column[board[j][i]] = 1  # add the value to the column dictionary
            
            # calculate the row and column index of the current cell within the 3x3 block
            rc = row_cube+j//3
            cc = column_cube + j%3
            
            # check if the value in the current cell of the block is valid
            if board[rc][cc] in block and board[rc][cc]!=0:
                return False
            block[board[rc][cc]] = 1  # add the value to the block dictionary
    return True

# Function to return solved sudoku
def sudokuSolver(sudoku):
    if isValidSudoku(sudoku):
        solveSudoku(sudoku,0,0)
        return sudoku
    else:
        return "No"