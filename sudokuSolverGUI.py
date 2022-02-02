import pygame
import sys
import math
import sudokuSolver


#Initializations for the board 
pygame.mixer.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (75, 119, 190)
WINDOW_HEIGHT = 450
WINDOW_WIDTH = 480

grid_width=50
grid_height=50
grid=sudokuSolver.grid
org_grid=grid.copy()


red=0
blue=0
green=0

#icon = pygame.image.load("icons/thumbnail.png")

#click_sound=pygame.mixer.Sound("sounds/mouse-click.wav")


def main():
    global SCREEN, CLOCK
    pygame.init()
    pygame.display.set_caption("Sudoku")
    #pygame.display.set_icon(icon)
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)
    mousePressed = False
    running=True

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and mousePressed:
                    mousePressed = False
                    deleteFromGrid(row,col)
                    
                if(mousePressed):
                    mousePressed = False
                    pressed_key = event.unicode
                    if pressed_key.isdigit():
                        writeToGrid(row,col,pressed_key,BLUE)

                if event.key == pygame.K_SPACE:
                    showSolution()

            if event.type == pygame.MOUSEBUTTONUP:
                mousePressed = True
                #click_sound.play()
                pos = pygame.mouse.get_pos()
                col = pos[0]
                row = pos[1]
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    showSolution()
                    running=False
        if running:

            ticks=pygame.time.get_ticks()   
            displayTime(ticks)
            CLOCK.tick(60)
        pygame.display.update()



def drawGrid():
    left=0
    top=0
    constantPositions = getConstantGridPos()
    filled=1
    number_font = pygame.font.SysFont( None, 25 )   # default font, size 16
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:

               if (i,j) in constantPositions:
                drawRect(grid[i][j],left,top,BLACK)
                left += 50
               else:
                   drawRect(grid[i][j],left,top,BLUE)
                   left += 50
            else:

                drawRect("",left,top,BLACK)
                left += 50

        left=0
        top+=50

def writeToGrid(row,col,pressed_key,color):
    global attemptsLeft
    rowInGrid=math.floor(row/50)
    colInGrid = math.floor(col/50)

    constantPositions = getConstantGridPos()

    if ((rowInGrid,colInGrid) not in constantPositions):
        left=50 * math.floor(col/50)
        top=50 * math.floor(row/50)

        grid[rowInGrid][colInGrid] = int(pressed_key)


        drawRect(pressed_key,left,top,color)


def deleteFromGrid(row,col):
    rowInGrid=math.floor(row/50)
    colInGrid = math.floor(col/50)

    left=50 * math.floor(col/50)
    top=50 * math.floor(row/50)

    constantPositions = getConstantGridPos()

    if (rowInGrid,colInGrid) not in constantPositions:
        drawRect("  ",left,top,BLACK)
        grid[rowInGrid][colInGrid] = 0



def drawRect(entry,left,top,color):
    number_font = pygame.font.SysFont( None, 25 )   # default font, size 25
    filled=1
    pygame.draw.rect(SCREEN, [red,blue,green], [left, top, grid_width, grid_height], filled)
    # make the number from grid[row][col] into an image
    number_text  = str(entry)
    number_image = number_font.render( number_text, True, color, WHITE )

    # Draw the number image
    SCREEN.blit( number_image, ( left+19, top+19 ) )
    pygame.display.flip()



def showSolution():
    global grid
    sudokuSolver.solveSudoku(org_grid)
    grid = org_grid


def displayTime(ticks):
    #Calculations for displaying time in seconds and minutes
    font = pygame.font.SysFont( None, 25 ) 
    seconds=int(ticks/1000 % 60)
    minutes=int(ticks/60000 % 24)
    out='Time: {minutes:02d}:{seconds:02d}'.format(minutes=minutes, seconds=seconds)

    # Blit to the screen
    text = font.render(out, True, BLACK,WHITE)
    SCREEN.blit(text, [300, 460])

#Saves grids original numbers' indices to a list 
def getConstantGridPos():
    constantGridPositions=[]
    for i in range(9):
        for j in range(9):
            if org_grid[i][j] != 0 :
                constantGridPositions.append((i,j))
    
    return constantGridPositions

if __name__=="__main__":
    main()