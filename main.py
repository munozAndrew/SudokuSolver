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

test2 = [
    [3,0,5,4,0,2,0,6,0],
    [4,9,0,7,6,0,1,0,8],
    [6,0,0,1,0,3,2,4,5],
    [0,0,3,9,0,0,5,8,0],
    [9,6,0,0,5,8,7,0,3],
    [0,8,1,3,0,4,0,9,2],
    [0,5,0,6,0,1,4,0,0],
    [2,0,0,5,4,9,0,7,0],
    [1,4,9,0,0,7,3,0,6],
]

def solver(brd):
    #base case: exits loop if no more empty cells exist
    find_empty = find_empty_cell(brd)
    if not find_empty:
        return True
    #returns cords for an empty cell
    else:
        row, col = find_empty
    #loops through potential numbers
    for i in range(1,10):
        #inputs value into empty cell
        if valid(brd, i, (row, col)):
            brd[row][col] = i
            
            #recursively call the solver function to fill the next empty cell
            if solver(brd):
                #runs if board is solved
                return True
            #reset cell to 0 if the current value didnt lead to a working solution
            brd[row][col] = 0
    #backtraces and tries a different value if no valid values were found for the current cell
    return False
            
            



def valid(brd, num, cord):
    #check row
    for i in range(len(brd[0])):
        if brd[cord[0]][i] == num and cord[1] != i:
            return False
    #check columm
    for i in range(len(brd)):
        if brd[i][cord[1]] == num and cord[0] != i:
            return False
    
    y_box = cord[0] // 3
    x_box = cord[1] // 3
    #checks 3x3 square by creating a new matrix essentially
    for i in range(y_box * 3, y_box * 3 + 3):
        for j in range(x_box * 3, x_box * 3 + 3):
            if brd[i][j] == num and (i,j) != cord:
                return False 
    return True
                

            

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

def find_empty_cell(brd):
    #loops through rows
    for i in range(len(brd)):
        #loops thorugh columns
        for j in range(len(brd[0])):
            #returns row and column for empty cell
            if brd[i][j] == 0:
                #returns (row, column)
                return (i, j) 
    #returns none if all cells are fill AKA finished the puzzle
    return None


print_board(test2)
print("======================")
solver(test2)
print_board(test2)