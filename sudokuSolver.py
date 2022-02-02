import numpy as np

#Checks if there are duplicate entries to the new entry in the same box
def checkBox(grid,newEntryRow,newEntryCol,num):
    #Finds the box of the new entry
    if(0<=newEntryRow<3):
        if(0<= newEntryCol <3):
            box=grid[0:3,0:3]
        elif(3<=newEntryCol<6):
            box=grid[0:3,3:6]
        elif(6<=newEntryCol<9):
            box=grid[0:3,6:9]

    elif(3<=newEntryRow<6):
        if(0<= newEntryCol <3):
             box=grid[3:6,0:3]
        elif(3<=newEntryCol<6):
            box=grid[3:6,3:6]
        elif(6<=newEntryCol<9):
            box=grid[3:6,6:9]

    elif(6<=newEntryRow<9):
        if(0<= newEntryCol <3):
            box=grid[6:9,0:3]
        elif(3<=newEntryCol<6):
            box=grid[6:9,3:6]
        elif(6<=newEntryCol<9):
            box=grid[6:9,6:9]
    

    #Checks if there is a duplicate in the box
    for x in range(3):
        for y in range(3):
            if(box[x][y]== num ):
                return False
            
    return True


#Checks if there are duplicate entries to the new entry in the same column
def checkCol(grid,newEntryCol,num):
    for row in range(9):
        if (grid[row][newEntryCol] == num):
            return False
    return True

#Checks if there are duplicate entries to the new entry in the same row
def checkRow(grid,newEntryRow,num):
    for col in range(9):
        if(grid[newEntryRow][col] == num):
            return False
    return True

#Checks if current value entered is valid
def checkValid(grid,newEntryRow,newEntryCol,num):
    return checkBox(grid,newEntryRow,newEntryCol,num) and checkCol(grid,newEntryCol,num) and checkRow(grid,newEntryRow,num)

#Checks the grid first row to last to find empty location
def findEmptyEntry(grid,x):
    for row in range(9):
        for col in range(9):
            if (grid[row][col] == 0):
                x[0] = row
                x[1] = col
                return True
    return False

def solveSudoku(grid):
    x=[0,0]
    if (findEmptyEntry(grid,x) == False):
        return True
    
    newEntryRow=x[0]
    newEntryCol = x[1]

    for num in range(1,10):
    
        if (checkValid(grid, newEntryRow, newEntryCol,num)):

            grid[newEntryRow][newEntryCol]=num
 
            if (solveSudoku(grid)):
                return True
 
            grid[newEntryRow][newEntryCol] = 0
        
    return False

#an intermediate sudoku grid
grid = np.array([[0, 2, 0, 6, 0, 8, 0, 0, 0],
                [5, 8, 0, 0, 0, 9, 7, 0, 0],
                [0, 0, 0, 0, 4, 0, 0, 0, 0],
                [3, 7, 0, 0, 0, 0, 5, 0, 0],
                [6, 0, 0, 0, 0, 0, 0, 0, 4],
                [0, 0, 8, 0, 0, 0, 0, 1, 3],
                [0, 0, 0, 0, 2, 0, 0, 0, 0],
                [0, 0, 9, 8, 0, 0, 0, 3, 6],
                [0, 0, 0, 3, 0, 6, 0, 9, 0]])

if __name__ == '__main__':
 
    
    if(solveSudoku(grid)):
        print(grid)
