from tkinter import *

root = Tk()
root.title("Sudoku Solver")
root.geometry("324x550")

label = Label(root,text="Fill in the numbers and click solve").grid(row=0,column=1,columnspan=10)

# Error label
errLabel = Label(root,text="",fg="red")
errLabel.grid(row=1,column=1,columnspan=10,pady=5)

# Success label
solvedLabel = Label(root,text="",fg="green")
solvedLabel.grid(row=1,column=1,columnspan=10,pady=5)

cells = {} # Dictionary to store the entry input grid

def ValidateNumber(P):
    # Check if the input is a number
    out = (P.isdigit() or P == "") and len(P) < 2
    return out

# register the above function with the entry widget
reg = root.register(ValidateNumber)

# Now divide the soduko into 9by9 grid into 3by3 grids
def draw3x3Grid(row,column,bgcolor):
    for i in range(3):
        for j in range(3):
            e = Entry(root,width=5,bg=bgcolor, justify="center", validate = "key" , validatecommand = (reg, "%P"))
            e.grid(row = row+i+1, column=column+j+1 , sticky="nsew",padx=1,pady=1,ipady=5)
            cells[( row+i+1 , column+j+1)] = e

# Now draw an 9 x9 grid 
def draw9x9Grid():
    color = "#D0ffff"
    for rowNo in range(1,10,3):
        for colNo in range(0,9,3):
            draw3x3Grid(rowNo,colNo,color)
            if color == "#D0ffff":
                color = "#ffffd0"
            else:
                color = "#D0ffff"

# create a clear value function which will clear all the values in the grid
def clearValues():
    errLabel.config(text="")
    solvedLabel.config(text="")
    for row in range(2,11):
        for col in range(1,10):
            cell = cells[(row,col)]
            cell.delete(0,"end")

# Now create a function get value function
def getValues():
    board = [] # Create a list to store the values of each cell
    errLabel.config(text="")
    solvedLabel.config(text="")
    for row in range(2 ,11):
        rows = []
        for col in range(1,10):
            val = cells[(row,col)].get()
            if val == "":
                rows.append(0)
            else:
                rows.append(int(val))
        board.append(rows)

# Create a button
btn = Button(root,command=getValues, text="Solve" , width=10)
btn.grid(row = 20 , column = 1, columnspan=5, pady=20)

btn = Button(root,command=clearValues, text="Clear" , width=10)
btn.grid(row = 20 , column = 5, columnspan=5, pady=20)

# Now for luanching sudoku solver
draw9x9Grid()
root.mainloop()
