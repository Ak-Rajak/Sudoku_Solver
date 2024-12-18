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

# Function to return solved sudoku
def sudokuSolver(sudoku):
    if solveSudoku(sudoku,0,0):
        return sudoku
    else:
        return "No"