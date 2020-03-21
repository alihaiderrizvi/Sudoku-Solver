import tkinter as tk
import time
import random
import copy

# this function finds an empty space on the board to fill numbers
def find_space(board):
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 0:
                return (x,y)
    return False

# this function checks if the number inserted is valid according to the game rules
def validity(board, num, row, col):

    # checking row
    for x in range(len(board)):
        if board[row][x] == num and col != x:
            return False

    # checking column
    for y in range(len(board)):
        if board[y][col] == num and row != y:
            return False

    # checking box
    box_row, box_col = row // 3, col // 3

    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_col * 3, box_col * 3 + 3):
            if board[i][j] == num and (i,j) != (row,col):
                return False

    return True

# this function generates a board to start solving
def generate_board():

    board = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]
    count = 0
    filled_boxes = 12 # the number of boxes to be filled in the start
    while count < filled_boxes:
        row_index = random.randrange(0,9)
        col_index = random.randrange(0,9)
        number = random.randrange(1,10)
        if board[row_index][col_index] == 0:
            if validity(board,number, row_index, col_index):
                board[row_index][col_index] = number
                count += 1
    return board




# this function solves the given board using the backtracking algorithm
def solve_board(board):

    global solution
    space = find_space(board)
    if space == False:
        return True
    else:
        row, col = space

    for attempt in range(1,10):
        if validity(board, attempt, row, col):
            board[row][col] = attempt
            a = copy.deepcopy(board)
            solution.append(a)

            if solve_board(board):
                return True
            board[row][col] = 0
            a = copy.deepcopy(board)
            solution.append(a)

    return False





# this function displays the steps followed by the algorithm to solve the board
def show_sol():
    global solution
    for start in solution:
        canvas.itemconfig(b1, text = start[0][0])
        canvas.itemconfig(b2, text=start[0][1])
        canvas.itemconfig(b3, text=start[0][2])
        canvas.itemconfig(b4, text=start[0][3])
        canvas.itemconfig(b5, text=start[0][4])
        canvas.itemconfig(b6, text=start[0][5])
        canvas.itemconfig(b7, text=start[0][6])
        canvas.itemconfig(b8, text=start[0][7])
        canvas.itemconfig(b9, text=start[0][8])

        canvas.itemconfig(b10, text=start[1][0])
        canvas.itemconfig(b11, text=start[1][1])
        canvas.itemconfig(b12, text=start[1][2])
        canvas.itemconfig(b13, text=start[1][3])
        canvas.itemconfig(b14, text=start[1][4])
        canvas.itemconfig(b15, text=start[1][5])
        canvas.itemconfig(b16, text=start[1][6])
        canvas.itemconfig(b17, text=start[1][7])
        canvas.itemconfig(b18, text=start[1][8])

        canvas.itemconfig(b19, text=start[2][0])
        canvas.itemconfig(b20, text=start[2][1])
        canvas.itemconfig(b21, text=start[2][2])
        canvas.itemconfig(b22, text=start[2][3])
        canvas.itemconfig(b23, text=start[2][4])
        canvas.itemconfig(b24, text=start[2][5])
        canvas.itemconfig(b25, text=start[2][6])
        canvas.itemconfig(b26, text=start[2][7])
        canvas.itemconfig(b27, text=start[2][8])

        canvas.itemconfig(b28, text=start[3][0])
        canvas.itemconfig(b29, text=start[3][1])
        canvas.itemconfig(b30, text=start[3][2])
        canvas.itemconfig(b31, text=start[3][3])
        canvas.itemconfig(b32, text=start[3][4])
        canvas.itemconfig(b33, text=start[3][5])
        canvas.itemconfig(b34, text=start[3][6])
        canvas.itemconfig(b35, text=start[3][7])
        canvas.itemconfig(b36, text=start[3][8])

        canvas.itemconfig(b37, text=start[4][0])
        canvas.itemconfig(b38, text=start[4][1])
        canvas.itemconfig(b39, text=start[4][2])
        canvas.itemconfig(b40, text=start[4][3])
        canvas.itemconfig(b41, text=start[4][4])
        canvas.itemconfig(b42, text=start[4][5])
        canvas.itemconfig(b43, text=start[4][6])
        canvas.itemconfig(b44, text=start[4][7])
        canvas.itemconfig(b45, text=start[4][8])

        canvas.itemconfig(b46, text=start[5][0])
        canvas.itemconfig(b47, text=start[5][1])
        canvas.itemconfig(b48, text=start[5][2])
        canvas.itemconfig(b49, text=start[5][3])
        canvas.itemconfig(b50, text=start[5][4])
        canvas.itemconfig(b51, text=start[5][5])
        canvas.itemconfig(b52, text=start[5][6])
        canvas.itemconfig(b53, text=start[5][7])
        canvas.itemconfig(b54, text=start[5][8])

        canvas.itemconfig(b55, text=start[6][0])
        canvas.itemconfig(b56, text=start[6][1])
        canvas.itemconfig(b57, text=start[6][2])
        canvas.itemconfig(b58, text=start[6][3])
        canvas.itemconfig(b59, text=start[6][4])
        canvas.itemconfig(b60, text=start[6][5])
        canvas.itemconfig(b61, text=start[6][6])
        canvas.itemconfig(b62, text=start[6][7])
        canvas.itemconfig(b63, text=start[6][8])

        canvas.itemconfig(b64, text=start[7][0])
        canvas.itemconfig(b65, text=start[7][1])
        canvas.itemconfig(b66, text=start[7][2])
        canvas.itemconfig(b67, text=start[7][3])
        canvas.itemconfig(b68, text=start[7][4])
        canvas.itemconfig(b69, text=start[7][5])
        canvas.itemconfig(b70, text=start[7][6])
        canvas.itemconfig(b71, text=start[7][7])
        canvas.itemconfig(b72, text=start[7][8])

        canvas.itemconfig(b73, text=start[8][0])
        canvas.itemconfig(b74, text=start[8][1])
        canvas.itemconfig(b75, text=start[8][2])
        canvas.itemconfig(b76, text=start[8][3])
        canvas.itemconfig(b77, text=start[8][4])
        canvas.itemconfig(b78, text=start[8][5])
        canvas.itemconfig(b79, text=start[8][6])
        canvas.itemconfig(b80, text=start[8][7])
        canvas.itemconfig(b81, text=start[8][8])
        m.update()
        time.sleep(0.01)






board = generate_board() # creating the board
solution = [] # this list contains all the steps followed by the algorithm. It stores all the states of the board.
solution.append(copy.deepcopy(board))
solve_board(board) # solving the board



for i in range(len(solution)):
    for j in range(len(solution[0])):
        for k in range(len(solution[0][0])):
            if solution[i][j][k] == 0:
                solution[i][j][k] = ''

start = solution[0]




m = tk.Tk()
m.title('Sudoku Solver')
m.geometry("470x520")
canvas = tk.Canvas(m, width = 470, height = 470)
canvas.pack()

# drawing bold lines
canvas.create_line(160,10,160,460, width = 4)
canvas.create_line(310,10,310,460, width = 4)
canvas.create_line(10,160,460,160, width = 4)
canvas.create_line(10,310,460,310, width = 4)

#first row
canvas.create_rectangle(10,10,60,60)
canvas.create_rectangle(60,10,110,60)
canvas.create_rectangle(110,10,160,60)
canvas.create_rectangle(160,10,210,60)
canvas.create_rectangle(210,10,260,60)
canvas.create_rectangle(260,10,310,60)
canvas.create_rectangle(310,10,360,60)
canvas.create_rectangle(360,10,410,60)
canvas.create_rectangle(410,10,460,60)

#second row
canvas.create_rectangle(10,60,60,110)
canvas.create_rectangle(60,60,110,110)
canvas.create_rectangle(110,60,160,110)
canvas.create_rectangle(160,60,210,110)
canvas.create_rectangle(210,60,260,110)
canvas.create_rectangle(260,60,310,110)
canvas.create_rectangle(310,60,360,110)
canvas.create_rectangle(360,60,410,110)
canvas.create_rectangle(410,60,460,110)

#third row
canvas.create_rectangle(10,60,60,160)
canvas.create_rectangle(60,60,110,160)
canvas.create_rectangle(110,60,160,160)
canvas.create_rectangle(160,60,210,160)
canvas.create_rectangle(210,60,260,160)
canvas.create_rectangle(260,60,310,160)
canvas.create_rectangle(310,60,360,160)
canvas.create_rectangle(360,60,410,160)
canvas.create_rectangle(410,60,460,160)

#fourth row
canvas.create_rectangle(10,60,60,210)
canvas.create_rectangle(60,60,110,210)
canvas.create_rectangle(110,60,160,210)
canvas.create_rectangle(160,60,210,210)
canvas.create_rectangle(210,60,260,210)
canvas.create_rectangle(260,60,310,210)
canvas.create_rectangle(310,60,360,210)
canvas.create_rectangle(360,60,410,210)
canvas.create_rectangle(410,60,460,210)

#fifth row
canvas.create_rectangle(10,60,60,260)
canvas.create_rectangle(60,60,110,260)
canvas.create_rectangle(110,60,160,260)
canvas.create_rectangle(160,60,210,260)
canvas.create_rectangle(210,60,260,260)
canvas.create_rectangle(260,60,310,260)
canvas.create_rectangle(310,60,360,260)
canvas.create_rectangle(360,60,410,260)
canvas.create_rectangle(410,60,460,260)

#sixth row
canvas.create_rectangle(10,60,60,310)
canvas.create_rectangle(60,60,110,310)
canvas.create_rectangle(110,60,160,310)
canvas.create_rectangle(160,60,210,310)
canvas.create_rectangle(210,60,260,310)
canvas.create_rectangle(260,60,310,310)
canvas.create_rectangle(310,60,360,310)
canvas.create_rectangle(360,60,410,310)
canvas.create_rectangle(410,60,460,310)

#seventh row
canvas.create_rectangle(10,60,60,360)
canvas.create_rectangle(60,60,110,360)
canvas.create_rectangle(110,60,160,360)
canvas.create_rectangle(160,60,210,360)
canvas.create_rectangle(210,60,260,360)
canvas.create_rectangle(260,60,310,360)
canvas.create_rectangle(310,60,360,360)
canvas.create_rectangle(360,60,410,360)
canvas.create_rectangle(410,60,460,360)

#eightth row
canvas.create_rectangle(10,60,60,410)
canvas.create_rectangle(60,60,110,410)
canvas.create_rectangle(110,60,160,410)
canvas.create_rectangle(160,60,210,410)
canvas.create_rectangle(210,60,260,410)
canvas.create_rectangle(260,60,310,410)
canvas.create_rectangle(310,60,360,410)
canvas.create_rectangle(360,60,410,410)
canvas.create_rectangle(410,60,460,410)

#ninth row
canvas.create_rectangle(10,60,60,460)
canvas.create_rectangle(60,60,110,460)
canvas.create_rectangle(110,60,160,460)
canvas.create_rectangle(160,60,210,460)
canvas.create_rectangle(210,60,260,460)
canvas.create_rectangle(260,60,310,460)
canvas.create_rectangle(310,60,360,460)
canvas.create_rectangle(360,60,410,460)
canvas.create_rectangle(410,60,460,460)


# creating button
button = tk.Button(m, text="Solve", command = show_sol) # the button shows the solution when pressed
button.place(x=215, y=480, in_= m)



# displaying the starting board
b1 = canvas.create_text(35,35, text = start[0][0], font=("calibri", 30))
b2 = canvas.create_text(85,35, text = start[0][1], font=("calibri", 30))
b3 = canvas.create_text(135,35, text = start[0][2], font=("calibri", 30))
b4 = canvas.create_text(185,35, text = start[0][3], font=("calibri", 30))
b5 = canvas.create_text(235,35, text = start[0][4], font=("calibri", 30))
b6 = canvas.create_text(285,35, text = start[0][5], font=("calibri", 30))
b7 = canvas.create_text(335,35, text = start[0][6], font=("calibri", 30))
b8 = canvas.create_text(385,35, text = start[0][7], font=("calibri", 30))
b9 = canvas.create_text(435,35, text = start[0][8], font=("calibri", 30))


b10 = canvas.create_text(35,85, text = start[1][0], font=("calibri", 30))
b11 = canvas.create_text(85,85, text = start[1][1], font=("calibri", 30))
b12 = canvas.create_text(135,85, text = start[1][2], font=("calibri", 30))
b13 = canvas.create_text(185,85, text = start[1][3], font=("calibri", 30))
b14 = canvas.create_text(235,85, text = start[1][4], font=("calibri", 30))
b15 = canvas.create_text(285,85, text = start[1][5], font=("calibri", 30))
b16 = canvas.create_text(335,85, text = start[1][6], font=("calibri", 30))
b17 = canvas.create_text(385,85, text = start[1][7], font=("calibri", 30))
b18 = canvas.create_text(435,85, text = start[1][8], font=("calibri", 30))


b19 = canvas.create_text(35,135, text = start[2][0], font=("calibri", 30))
b20 = canvas.create_text(85,135, text = start[2][1], font=("calibri", 30))
b21 = canvas.create_text(135,135, text = start[2][2], font=("calibri", 30))
b22 = canvas.create_text(185,135, text = start[2][3], font=("calibri", 30))
b23 = canvas.create_text(235,135, text = start[2][4], font=("calibri", 30))
b24 = canvas.create_text(285,135, text = start[2][5], font=("calibri", 30))
b25 = canvas.create_text(335,135, text = start[2][6], font=("calibri", 30))
b26 = canvas.create_text(385,135, text = start[2][7], font=("calibri", 30))
b27 = canvas.create_text(435,135, text = start[2][8], font=("calibri", 30))


b28 = canvas.create_text(35,185, text = start[3][0], font=("calibri", 30))
b29 = canvas.create_text(85,185, text = start[3][1], font=("calibri", 30))
b30 = canvas.create_text(135,185, text = start[3][2], font=("calibri", 30))
b31 = canvas.create_text(185,185, text = start[3][3], font=("calibri", 30))
b32 = canvas.create_text(235,185, text = start[3][4], font=("calibri", 30))
b33 = canvas.create_text(285,185, text = start[3][5], font=("calibri", 30))
b34 = canvas.create_text(335,185, text = start[3][6], font=("calibri", 30))
b35 = canvas.create_text(385,185, text = start[3][7], font=("calibri", 30))
b36 = canvas.create_text(435,185, text = start[3][8], font=("calibri", 30))


b37 = canvas.create_text(35,235, text = start[4][0], font=("calibri", 30))
b38 = canvas.create_text(85,235, text = start[4][1], font=("calibri", 30))
b39 = canvas.create_text(135,235, text = start[4][2], font=("calibri", 30))
b40 = canvas.create_text(185,235, text = start[4][3], font=("calibri", 30))
b41 = canvas.create_text(235,235, text = start[4][4], font=("calibri", 30))
b42 = canvas.create_text(285,235, text = start[4][5], font=("calibri", 30))
b43 = canvas.create_text(335,235, text = start[4][6], font=("calibri", 30))
b44 = canvas.create_text(385,235, text = start[4][7], font=("calibri", 30))
b45 = canvas.create_text(435,235, text = start[4][8], font=("calibri", 30))


b46 = canvas.create_text(35,285, text = start[5][0], font=("calibri", 30))
b47 = canvas.create_text(85,285, text = start[5][1], font=("calibri", 30))
b48 = canvas.create_text(135,285, text = start[5][2], font=("calibri", 30))
b49 = canvas.create_text(185,285, text = start[5][3], font=("calibri", 30))
b50 = canvas.create_text(235,285, text = start[5][4], font=("calibri", 30))
b51 = canvas.create_text(285,285, text = start[5][5], font=("calibri", 30))
b52 = canvas.create_text(335,285, text = start[5][6], font=("calibri", 30))
b53 = canvas.create_text(385,285, text = start[5][7], font=("calibri", 30))
b54 = canvas.create_text(435,285, text = start[5][8], font=("calibri", 30))


b55 = canvas.create_text(35,335, text = start[6][0], font=("calibri", 30))
b56 = canvas.create_text(85,335, text = start[6][1], font=("calibri", 30))
b57 = canvas.create_text(135,335, text = start[6][2], font=("calibri", 30))
b58 = canvas.create_text(185,335, text = start[6][3], font=("calibri", 30))
b59 = canvas.create_text(235,335, text = start[6][4], font=("calibri", 30))
b60 = canvas.create_text(285,335, text = start[6][5], font=("calibri", 30))
b61 = canvas.create_text(335,335, text = start[6][6], font=("calibri", 30))
b62 = canvas.create_text(385,335, text = start[6][7], font=("calibri", 30))
b63 = canvas.create_text(435,335, text = start[6][8], font=("calibri", 30))


b64 = canvas.create_text(35,385, text = start[7][0], font=("calibri", 30))
b65 = canvas.create_text(85,385, text = start[7][1], font=("calibri", 30))
b66 = canvas.create_text(135,385, text = start[7][2], font=("calibri", 30))
b67 = canvas.create_text(185,385, text = start[7][3], font=("calibri", 30))
b68 = canvas.create_text(235,385, text = start[7][4], font=("calibri", 30))
b69 = canvas.create_text(285,385, text = start[7][5], font=("calibri", 30))
b70 = canvas.create_text(335,385, text = start[7][6], font=("calibri", 30))
b71 = canvas.create_text(385,385, text = start[7][7], font=("calibri", 30))
b72 = canvas.create_text(435,385, text = start[7][8], font=("calibri", 30))


b73 = canvas.create_text(35,435, text = start[8][0], font=("calibri", 30))
b74 = canvas.create_text(85,435, text = start[8][1], font=("calibri", 30))
b75 = canvas.create_text(135,435, text = start[8][2], font=("calibri", 30))
b76 = canvas.create_text(185,435, text = start[8][3], font=("calibri", 30))
b77 = canvas.create_text(235,435, text = start[8][4], font=("calibri", 30))
b78 = canvas.create_text(285,435, text = start[8][5], font=("calibri", 30))
b79 = canvas.create_text(335,435, text = start[8][6], font=("calibri", 30))
b80 = canvas.create_text(385,435, text = start[8][7], font=("calibri", 30))
b81 = canvas.create_text(435,435, text = start[8][8], font=("calibri", 30))



m.mainloop()
