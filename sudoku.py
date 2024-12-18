from tkinter import *
from logic import sudokuSolver

root = Tk()
root.title("Sudoku Solver")
root.geometry("526x743")
root.configure(bg="#91abc6")
root.resizable(False,False)

label = Label(root,text="Sudoku Solver", font=('DreamlandStd' , 34), bg="#91abc6")
label.place(x = 0 , y = 10, width = 526)

# Error label
# errLabel = Label(root,text="",fg="red")
# errLabel.grid(row=1,column=1,columnspan=10,pady=5)

# Success label
# solvedLabel = Label(root,text="",fg="green")
# solvedLabel.grid(row=1,column=1,columnspan=10,pady=5)

# Create a label that display success or error message of a program
label = Label(root,text="", fg = "#1e54a4" , bg = "#91abc6", font=('TkDefaultFont', 14))
label.place(x = 0 , y = 92, width = 526)

cells = {} # Dictionary to store the entry input grid

def ValidateNumber(P):
    # Check if the input is a number
    out = (P.isdigit() or P == "") and len(P) < 2
    return out

# register the above function with the entry widget
reg = root.register(ValidateNumber)

# Now divide the soduko into 9by9 grid into 3by3 grids
# def draw3x3Grid(row,column,bgcolor):
#     for i in range(3):
#         for j in range(3):
#             e = Entry(root,width=5,bg=bgcolor, justify="center", validate = "key" , validatecommand = (reg, "%P"))
#             e.grid(row = row+i+1, column=column+j+1 , sticky="nsew",padx=1,pady=1,ipady=5)
#             cells[( row+i+1 , column+j+1)] = e

# # Now draw an 9 x9 grid 
# def draw9x9Grid():
#     color = "#D0ffff"
#     for rowNo in range(1,10,3):
#         for colNo in range(0,9,3):
#             draw3x3Grid(rowNo,colNo,color)
#             if color == "#D0ffff":
#                 color = "#ffffd0"
#             else:
#                 color = "#D0ffff"

# rewriting the above code to into one function for grids
def drawGrid():
    frame = Frame(root , bg = "#91abc6")
    frame.place(x = 42, y=151, width=442, height=443)
    font = ('TkTextFont', 14)

    for i in range(9):
        for j in range(9):
            entry = Entry(frame, bg="#fff" , fg="#000", font= font, borderwidth=5,
                          highlightbackground="#000" , relief=FLAT , justify="center", validate = "key" , validatecommand = (reg, "%P"))
            entry.place(x= i*49 , y = j*49 , width = 48 , height = 48)
            cells [ (i+2,j+1)] = entry

    # border in 3by3 grid
    for i in range(-1 , 9 , 3):
        Frame(frame, bg="#000", width=441).place(x = 0, y =(i+1)*49, height = 2)
    for j in range(-1 , 9 , 3):
        Frame(frame, bg="#000", width=2).place(x = (j+1)*49, y = 0, height = 441)


# create a clear value function which will clear all the values in the grid
def clearValues():
    label.config(text="")
    for row in range(2,11):
        for col in range(1,10):
            cell = cells[(row,col)]
            cell.delete(0,"end")

# Now create a function get value function
def getValues():
    board = [] # Create a list to store the values of each cell
    label.config(text="")
    for row in range(2 ,11):
        rows = []
        for col in range(1,10):
            val = cells[(row,col)].get()
            if val == "":
                rows.append(0)
            else:
                rows.append(int(val))
        board.append(rows)
    updateValues(board)

# Create a button
btn = Button(root,command=getValues, text="Solve" , width=10, font=('TkTextFont', 14))
btn.place(x = 25 , y = 650)

btn = Button(root,command=clearValues, text="Clear" , width=10 , font=('TkTextFont', 14))
btn.place(x = 198 , y = 650)

btn = Button(root,command=root.destroy, text="Exit" , width=10 , font=('TkTextFont', 14))
btn.place(x = 370 , y = 650)

# Draw grid
drawGrid()

# Animation for the sudoku while solution been populated
def updateValueOnBoard(row, col, value):
    cells[(row,col)].insert(0,value)


# function which will update the cell and display the solved sudoku
def updateValues(s):
    sol = sudokuSolver(s)
    if sol != "No":
        for rows in range(2 ,11):
            for cols in range(1, 10):
                cells[(rows,cols)].delete(0,"end")
                # cells[(rows,cols)].insert(0,sol[rows-2][cols-1])
                # This excute a fun in set time interval

                root.after((rows+cols)*50 , updateValueOnBoard, rows, cols, sol[rows-2][cols-1])
        label.config(text="Sudoku solved!")
    else:
        label.config(text="No solution exists for this suduko")    


# Now for luanching sudoku solver
root.mainloop()
