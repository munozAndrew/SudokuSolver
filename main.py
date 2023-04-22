# 2d sudoku board that has 0s represent an empty cell
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7],
]


def print_board(brd):
    #loops through rows
    for i in range(len(brd)):
        #print horizontal line after every 3 rows 
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")
        #loops through columns
        for j in range(len(brd[0])):
            #print vertical lines after every 3 columns 
            if j % 3 == 0 and j != 0:
                print(" | " , end="")
            #print value of the cell
            if j == 8:
                print(brd[i][j])
            else:
                print(str(brd[i][j]) + " ", end="")

