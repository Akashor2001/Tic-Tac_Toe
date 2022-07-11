#from astar import WHITE, get_clicked_pos, make_grid
import pygame
import math
import time

pygame.init()
WIDTH = 600
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption('Tic-Tac-Toe')
clock = pygame.time.Clock()

class Slot:
    def __init__(self, disp, row, col, width, height ):
        self.disp = disp
        self.row = row
        self.col = col
        self.x = col*width
        self.y = row*height
        self.width = width
        self.height = height

    def isX(self):
        return self.disp == 'x' 
 
    def isO(self):
        return self.disp == 'o'

    def make_X(self):
        self.disp = 'x'

    def make_O(self):
        self.disp = 'o'

    def reset(self):
        self.disp = ' '

    def draw(self, win):
           pygame.draw.rect(win, (250,250,250), (self.x,self.y,self.width,self.height))
        
    def draw_X(self, win):
           pygame.draw.rect(win, (250,250,250), (self.x,self.y,self.width,self.height)) 
           pygame.draw.line(win, (0,0,0), (self.x,self.y), (self.x+self.width, self.y+self.height), 5)
           pygame.draw.line(win, (0,0,0), (self.x+self.width,self.y), (self.x, self.y+self.height), 5)

    def draw_O(self, win):
           pygame.draw.rect(win, (250,250,250), (self.x,self.y,self.width,self.height))
           pygame.draw.circle(win, (0,0,0), (self.x+self.width//2,self.y+self.height//2), self.width//2-5, 2) 

    def __lt__(self, other):
        return False

def get_clicked_pos(pos, rows, width):
	gap = width // rows
	y, x = pos

	row = y // gap
	col = x // gap

	return row, col

WHITE = (255, 255, 255)

def make_grid(rows, width):
    grid = []
    gap = width//rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
           slot = Slot(' ',i,j,gap,gap)
           grid[i].append(slot)
    return grid,gap

def make_grid(rows, width):
    grid = []
    gap = width//rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
           slot = Slot(' ',i,j,gap,gap)
           grid[i].append(slot)
    return grid,gap

def draw_grid(win, rows, width):
    gap = width//rows
    for i in range(rows):
        pygame.draw.line(WIN, (0,0,0), (0, i*gap), (width, i*gap))
        for j in range(rows):
            pygame.draw.line(WIN, (0,0,0), (j*gap, 0), (j*gap, width))

def draw(win, rows, grid, width):
    win.fill((255,255,255))
    pygame.time.delay(50)
    for row in grid:
        for slot in row:
            if slot.disp == ' ':
                slot.draw(win)
            if slot.disp == 'x':
                slot.draw_X(win)
            if slot.disp == 'o':
                slot.draw_O(win) 
    draw_grid(win,rows, width)
    pygame.display.update()

def get_clicked_pos(pos,rows,width):
    gap = width//rows
    x,y = pos
    row = y//gap
    col = x//gap
    return row,col


def tieChecker(grid,rows):
    tie = True
    for i in range(rows):
        for j in range(rows):
            if grid[i][j].disp == ' ':
                tie = False
                
    return tie,'tie'


def diagonal_Winner(grid):
    
    winn = True
    playerWon = ' '
    if grid[1][1].disp == grid[0][0].disp and grid[1][1].disp == grid[2][2].disp and grid[1][1].disp == 'x':
        winn=True 
        playerWon = 'x' 
        return True,'x'
    if grid[1][1].disp == grid[0][0].disp and grid[1][1].disp == grid[2][2].disp and grid[1][1].disp=='o':
        winn=True  
        playerWon = 'o'
        return winn,playerWon
    if grid[1][1].disp == grid[0][2].disp and grid[1][1].disp == grid[2][0].disp and grid[1][1].disp=='x':
        winn=True 
        playerWon = 'x'
        return winn,playerWon 
    if grid[1][1].disp == grid[0][2].disp and grid[1][1].disp == grid[2][0].disp and grid[1][1].disp=='o':
        winn=True  
        playerWon = 'o'
        return winn,playerWon

    return False,' '


def winner(grid, rows):
    winn = False
    playerWon = 'nah'
    for i in range(rows):
    
        if grid[i][0].disp == grid[i][1].disp and grid[i][1].disp == grid[i][2].disp and grid[i][0].disp == 'x' :
                winn = True
                playerWon = 'x'
                return winn,playerWon
        if grid[i][0].disp == grid[i][1].disp and grid[i][1].disp == grid[i][2].disp and grid[i][0].disp == 'o' :
                winn = True
                playerWon = 'o'
                return winn,playerWon
        if grid[0][i].disp == grid[1][i].disp and grid[1][i].disp == grid[2][i].disp and grid[0][i].disp == 'x' :
                winn = True
                playerWon = 'x'
                return winn,playerWon
        if grid[0][i].disp == grid[1][i].disp and grid[1][i].disp == grid[2][i].disp and grid[0][i].disp == 'o' :
                winn = True
                playerWon = 'o'
                return winn,playerWon
    winn,playerWon=diagonal_Winner(grid)
    if not winn:
        return tieChecker(grid,rows)

    return winn,playerWon




def winner_coordinates(grid):
    n = len(grid)
    for i in range(n):
        if grid[i][0].disp == grid[i][1].disp and grid[i][1].disp == grid[i][2].disp and grid[i][0].disp == 'x' :
                return 0,i,2,i
        if grid[i][0].disp == grid[i][1].disp and grid[i][1].disp == grid[i][2].disp and grid[i][0].disp == 'o' :
                return 0,i,2,i
        if grid[0][i].disp == grid[1][i].disp and grid[1][i].disp == grid[2][i].disp and grid[0][i].disp == 'x' :
                return i,0,i,2
        if grid[0][i].disp == grid[1][i].disp and grid[1][i].disp == grid[2][i].disp and grid[0][i].disp == 'o' :
                return i,0,i,2



def draw_winner_text(win,width,player_won):
    font = pygame.font.Font('freesansbold.ttf',45)
    textRun = font.render(player_won + '  has won ba', True, (250,250,240))
    textRect = textRun.get_rect()
    textRect.center = ( width//4-65+(2*width//4+105)//2, width//4+width//4 )
    win.blit(textRun,textRect)


def draw_winner(player_won, grid, win, width):
    
    #win.fill((255,255,255))
    pygame.time.delay(1000)
    pygame.draw.rect(win, (220, 200, 180), (width//4 - 65, width//4, 2*width//4 + 105, 2*width//4))
    draw_winner_text(win,width,player_won)
    pygame.display.update()


def minimax(grid,rows,comp):
    won,playerWon = winner(grid,rows)
    
    if won:
        if playerWon == 'x':
            return 1
        if playerWon == 'o':
            return -1
        if playerWon == 'Tie':
            return 0
    if comp:
        score = -1e7
        bestScore = -1e7
        for i in range(rows):
            for j in range(rows):
                 if grid[i][j].disp == ' ':
                     grid[i][j].disp = 'x'
                     score = minimax(grid,rows,False)
                     grid[i][j].disp = ' '
                     bestScore=max(score,bestScore)
        return bestScore 
        
    if not comp:
        score = 1e7
        bestScore = 1e7
        for i in range(rows):
            for j in range(rows):
                 if grid[i][j].disp == ' ':
                     grid[i][j].disp = 'o'
                     score = minimax(grid,rows,True)
                     grid[i][j].disp = ' '
                     bestScore=min(score,bestScore)
        return bestScore 




def besMov(grid,rows):
    score = -1e7
    bestScore = -1e7
    for row in grid:
        for slot in row:
            if slot.disp == ' ':
                slot.disp = 'x'
                score = minimax(grid,rows,False)
                slot.disp = ' '
                if score>bestScore :
                    bestX = slot.row
                    bestY = slot.col
                    bestScore = score

    return bestX,bestY



def main(win,width):
    ROWS = 3
    grid, gap = make_grid(ROWS, width)
    run = False
    computer = False
    won = False
    grid[0][0].disp = 'x'
    while run is False:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  run = True
        
        if not won:
           draw(win,ROWS,grid,width)
        
        #print(diagonal_Winner(grid))
        won, player_won = winner(grid,ROWS)
        if pygame.mouse.get_pressed()[0] and not won:
            pos = pygame.mouse.get_pos()
            x,y = pos
            row, col = get_clicked_pos(pos, ROWS, width)
            #print('row')
            #print(row)
            #print('col')
            #print(col)
            #print(x)
            slot = grid[row][col]
            #print('self.disp')
            #print(slot.disp)
            
            if slot.disp == ' ':
                   
                #print('slot.x')
                #print(slot.x)
                #print('slot.y')
                #print(slot.y)
                #print('slot.x + slot.width')
                #print(slot.x + slot.width)
                #print('slot.y + slot.height')
                #print(slot.y + slot.height)
                #print('player')
                #print(player)
                
                   slot.make_O()
                   
                   besX,besY = besMov(grid,ROWS)
                   grid[besX][besY].make_X()
                   
                #    slot.make_X()
                #   computer = False
                #besX,besY = besMov(grid,ROWS) 
        

        if pygame.mouse.get_pressed()[2] :
            for row in grid:
                for slot in row:
                     slot.reset()

        if won:
             draw_winner(player_won,grid,win, width)
             #print('fds')
             #textRun = font.render('RUN', True, (250,250,240))
             #textRect = textRun.get_rect()
             #textRect.center = ( ((butStrt.width//2) + butStrt.x), ((butStrt.height//2) + butStrt.y) )
             #win.blit(textRun, textRect)

    pygame.quit()

main(WIN,WIDTH)
