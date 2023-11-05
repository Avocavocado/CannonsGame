#===Cannons Project - Pygame===#
'''23 June 2020'''

class Board:
    
    def __init__(self,board):
        if len(board) != 16:
            raise LengthError

        #Colours
        self.BLUE = (65, 105, 225)
        self.RED = (254, 64, 66)
        self.GREEN = (2, 195, 2)
        self.YELLOW = (237, 211, 7)
        self.BLACK = (60, 58, 66)
        
        #Convert into 4x4 matrix
        self.board = [board[i:i+4] for i in range(0,16,4)]

    def move(self):
        
        while True:
            
            try:
                
                #Select From
                from_y,from_x = input("Select starting position:").split()
                from_y,from_x = int(from_y),int(from_x)
                
                #Select To
                to_y,to_x = input("Select ending position:").split()
                to_y,to_x = int(to_y),int(to_x)

                #Quick Check
                if to_y in range(4) and to_x in range(4) and from_y in range(4) and from_x in range(4):
                    if self.board[from_y][from_x] != 0:
                        break
            except:
                pass
            
        #Slingshot
        if self.board[from_y][from_x] == 1:
            #Slingshot Left
            if from_x - 2 == to_x and self.board[from_y][from_x-1] != 0 and self.board[from_y][from_x-2] == 0:
                self.board[from_y][from_x] = 0
                self.board[from_y][from_x-1] = 0
                self.board[from_y][from_x-2] = 1
                    
            #Slingshot Right
            if from_x + 2 == to_x and self.board[from_y][from_x+1] != 0 and self.board[from_y][from_x+2] == 0:
                self.board[from_y][from_x] = 0
                self.board[from_y][from_x+1] = 0
                self.board[from_y][from_x+2] = 1
            #Slingshot Up
            if from_y - 2 == to_y and self.board[from_y-1][from_x] != 0 and self.board[from_y-2][from_x] == 0:
                self.board[from_y][from_x] = 0
                self.board[from_y-1][from_x] = 0
                self.board[from_y-2][from_x] = 1
                    
            #Slingshot Down
            if from_y + 2 == to_y and self.board[from_y+1][from_x] != 0 and self.board[from_y+2][from_x] == 0:
                self.board[from_y][from_x] = 0
                self.board[from_y+1][from_x] = 0
                self.board[from_y+2][from_x] = 1

        #Assassin
        if self.board[from_y][from_x] == 2:
            #Assasin ⭦
            if from_y - 2 == to_y and from_x - 2 == to_x and self.board[from_y-1][from_x-1] != 0 and self.board[from_y-2][from_x-2] == 0:
                self.board[from_y][from_x] = 0
                self.board[from_y-1][from_x-1] = 0
                self.board[from_y-2][from_x-2] = 2

            #Assasin ⭧
            if from_y - 2 == to_y and from_x + 2 == to_x and self.board[from_y-1][from_x+1] != 0 and self.board[from_y-2][from_x+2] == 0:
                self.board[from_y][from_x] = 0
                self.board[from_y-1][from_x+1] = 0
                self.board[from_y-2][from_x+2] = 2

            #Assasin ⭨
            if from_y + 2 == to_y and from_x + 2 == to_x and self.board[from_y+1][from_x+1] != 0 and self.board[from_y+2][from_x+2] == 0:
                self.board[from_y][from_x] = 0
                self.board[from_y+1][from_x+1] = 0
                self.board[from_y+2][from_x+2] = 2

            #Assasin ⭩
            if from_y + 2 == to_y and from_x - 2 == to_x and self.board[from_y+1][from_x-1] != 0 and self.board[from_y+2][from_x2] == 0:
                self.board[from_y][from_x] = 0
                self.board[from_y+1][from_x-1] = 0
                self.board[from_y+2][from_x-2] = 2
                
        #Mortar
        if self.board[from_y][from_x] == 3:
            #Mortar Up-Left
            if from_y - 2 == to_y and from_x - 1 == to_x and (self.board[from_y-1][from_x] != 0 or self.board[from_y-1][from_x-1] != 0) and self.board[from_y-2][from_x-1] == 0:
                self.board[from_y][from_x] = 0
                self.board[from_y-1][from_x] = 0
                self.board[from_y-1][from_x-1] = 0
                self.board[from_y-2][from_x-1] = 3
                
            #Mortar Up-Right
            if from_y - 2 == to_y and from_x + 1 == to_x and (self.board[from_y-1][from_x] != 0 or self.board[from_y-1][from_x+1] != 0) and self.board[from_y-2][from_x+1] == 0:
                self.board[from_y][from_x] = 0
                self.board[from_y-1][from_x] = 0
                self.board[from_y-1][from_x+1] = 0
                self.board[from_y-2][from_x+1] = 3

            #Mortar Right-Up
            if from_y - 1 == to_y and from_x + 2 == to_x and (self.board[from_y][from_x+1] != 0 or self.board[from_y-1][from_x+1] != 0) and self.board[from_y-1][from_x+2] == 0:
                self.board[from_y][from_x] = 0
                self.board[from_y][from_x+1] = 0
                self.board[from_y-1][from_x+1] = 0
                self.board[from_y-1][from_x+2] = 3

            #Mortar Right-Down
            if from_y + 1 == to_y and from_x + 2 == to_x and (self.board[from_y][from_x+1] != 0 or self.board[from_y+1][from_x+1] != 0) and self.board[from_y+1][from_x+2] == 0:
                self.board[from_y][from_x] = 0
                self.board[from_y][from_x+1] = 0
                self.board[from_y+1][from_x+1] = 0
                self.board[from_y+1][from_x+2] = 3

            #Mortar Down-Right
            if from_y + 2 == to_y and from_x + 1 == to_x and (self.board[from_y+1][from_x] != 0 or self.board[from_y+1][from_x+1] != 0) and self.board[from_y+2][from_x+1] == 0:
                self.board[from_y][from_x] = 0
                self.board[from_y+1][from_x] = 0
                self.board[from_y+1][from_x+1] = 0
                self.board[from_y+2][from_x+1] = 3

            #Mortar Down-Left
            if from_y + 2 == to_y and from_x - 1 == to_x and (self.board[from_y+1][from_x] != 0 or self.board[from_y+1][from_x-1] != 0) and self.board[from_y+2][from_x-1] == 0:
                self.board[from_y][from_x] = 0
                self.board[from_y+1][from_x] = 0
                self.board[from_y+1][from_x-1] = 0
                self.board[from_y+2][from_x-1] = 3

            #Mortar Left-Down
            if from_y + 1 == to_y and from_x - 2 == to_x and (self.board[from_y][from_x-1] != 0 or self.board[from_y+1][from_x-1] != 0) and self.board[from_y+1][from_x-2] == 0:
                self.board[from_y][from_x] = 0
                self.board[from_y][from_x-1] = 0
                self.board[from_y+1][from_x-1] = 0
                self.board[from_y+1][from_x-2] = 3

            #Mortar Left-Up
            if from_y - 1 == to_y and from_x - 2 == to_x and (self.board[from_y][from_x-1] != 0 or self.board[from_y-1][from_x-1] != 0) and self.board[from_y-1][from_x-2] == 0:
                self.board[from_y][from_x] = 0
                self.board[from_y][from_x-1] = 0
                self.board[from_y-1][from_x-1] = 0
                self.board[from_y-1][from_x-2] = 3

        #Portal
        if self.board[from_y][from_x] == 4:
            if to_y in range(from_y-1,from_y+2) and to_x in range(from_x-1,from_x+2) and (from_y,from_x) == (to_y,from_x):
                self.board[from_y][from_x],self.board[to_y][to_x] = self.board[to_y][to_x],self.board[from_y][from_x]

        #Crossfire
        if self.board[from_y][from_x] == 5:
            #Crossfire ⭦
            if from_y - 1 == to_y and from_x - 1 == to_x and (self.board[from_y][from_x-1] != 0 or self.board[from_y-1][from_x] != 0) and self.board[from_y-1][from_x-1] == 0:
                self.board[from_y][from_x] = 0
                self.board[from_y][from_x-1] = 0
                self.board[from_y-1][from_x] = 0
                self.board[from_y-1][from_x-1] = 5

            #Crossfire ⭧
            if from_y - 1 == to_y and from_x + 1 == to_x and (self.board[from_y][from_x+1] != 0 or self.board[from_y-1][from_x] != 0) and self.board[from_y-1][from_x+1] == 0:
                self.board[from_y][from_x] = 0
                self.board[from_y][from_x+1] = 0
                self.board[from_y-1][from_x] = 0
                self.board[from_y-1][from_x+1] = 5

            #Crossfire ⭨
            if from_y + 1 == to_y and from_x + 1 == to_x and (self.board[from_y][from_x+1] != 0 or self.board[from_y+1][from_x] != 0) and self.board[from_y+1][from_x+1] == 0:
                self.board[from_y][from_x] = 0
                self.board[from_y][from_x+1] = 0
                self.board[from_y+1][from_x] = 0
                self.board[from_y+1][from_x+1] = 5

            #Crossfire ⭩
            if from_y + 1 == to_y and from_x - 1 == to_x and (self.board[from_y][from_x-1] != 0 or self.board[from_y+1][from_x] != 0) and self.board[from_y+1][from_x-1] == 0:
                self.board[from_y][from_x] = 0
                self.board[from_y][from_x-1] = 0
                self.board[from_y+1][from_x] = 0
                self.board[from_y+1][from_x-1] = 5
                
    #Checks if theres only one piece left
    def check(self):
        ov = 0
        for row in self.board:
            for piece in row:
                if piece != 0:
                    ov += 1
        if ov == 1:
            return True
        else:
            return False

    def show(self):
        for row in self.board:
            print(row)

    def load(self):
        #Background
        screen.blit(bg,(0,0))

        #Draw pieces
        for by,y in enumerate((49,202,357,511)):
            for bx,x in enumerate((49,205,359,514)):
                if self.board[by][bx] == 1:
                    pg.draw.rect(screen,self.BLUE,(x,y,135,135))
                if self.board[by][bx] == 2:
                    pg.draw.rect(screen,self.GREEN,(x,y,135,135))
                if self.board[by][bx] == 3:
                    pg.draw.rect(screen,self.RED,(x,y,135,135))
                if self.board[by][bx] == 4:
                    pg.draw.rect(screen,self.BLACK,(x,y,135,135))
                if self.board[by][bx] == 5:
                    pg.draw.rect(screen,self.YELLOW,(x,y,135,135))
                    
        pg.display.update()

class LengthError(ValueError):
    def __str__(self):
        return "Len(self.board) not equal 16"

blank = Board([0] * 16)
lvl = Board([0,3,0,0,
             5,1,1,1,
             0,0,0,4,
             2,0,0,0])

import pygame as pg
pg.init()

screen = pg.display.set_mode((700,700))
pg.display.set_caption("Cannons")
bg = pg.transform.scale(pg.image.load("2048 Board.png"),(700,700))

lvl.load()
pg.display.update()


    
