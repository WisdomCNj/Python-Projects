
board = [
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
    
#print(board)

#printing the board in the terminal
def print_board(bo):
    
    for i in range(len(bo)):
        #after the thrid row it is spilt 
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")
        for j in range(len(bo[0])):
            #after every 3rd value it there will be a dash
            if j % 3 == 0 and j != 0:
                    print("|", end="") #end="" doesnt go to a new line
            
            if j == 8:
                 #without the "end="" it will go to the next line
                 print(bo[i][j])
            else:
                 print(str(bo[i][j]) + " ", end="")

print_board(board)

def find_empty(bo):
     #looping through all the values (first loop for the row, then second for the column)
     for i in range(len(bo)):
          for j in range(len(bo[0])):
               if bo[i][j] == 0:
                    return (i, j) #row and column of the empty space (0)
     return None
               
def valid(bo, num, pos):
     #checks the row of the 2D array
     for i in range(len(bo[0])):
          if bo[pos[0]][i] == num and pos[1] != i:
               return False
     for i in range(len(bo)):
          if bo[i][pos[1]] == num and pos[0] != i:
               return False

    #checks what box to use
     box_x = pos[1] // 3
     box_y = pos[0] // 3
     for i in range(box_y*3, box_y*3 + 3):
          for j in range(box_x*3, box_x*3 + 3):
               if bo[i][j] == num and (i,j) != pos:
                    return False
     return True
def solve(bo):
     find = find_empty(bo)
     if not find:
          return True
     else: 
          row, col = find
     for i in range(1,10):
          if valid(bo, i, (row, col)):
               bo[row][col] = i
               if solve(bo):
                    return True
               bo[row][col] = 0 
     return False
solve(board)
print("Solveddd")
print_board(board)               