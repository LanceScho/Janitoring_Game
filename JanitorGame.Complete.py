import pygame, simpleGE

""" JanitorGame.py
    All art sprites by Lance Schoenradt
    
    Music "TheForest" by Wolfgang_ on OpenGameArt.org
    Win and lose Music "And the winner is..." and "Total Fail" by congusbongus on OpenGameArt.org
    

"""



class Tile(simpleGE.SuperSprite):
    totalTileCount = 0

    def __init__(self, scene):
        super().__init__(scene)
        self.janitor = Janitor(self)
        self.images = [
            ("DirtyBrick.png"),
            ("CleanBrick.png"),
            ("DirtyCarpet.png"),
            ("CleanCarpet.png"),
            ("Trash.png"),
            ("TrashBag.png"),
            ("transparent.png"),
            ("Rubble.png"),
            ("transparent.png")
            ]

        self.setSize(32, 32)
        self.DFLOOR = 0
        self.CFLOOR = 1
        self.DRUG = 2
        self.CRUG = 3
        self.TRASH = 4
        self.TRASHBAG = 5
        self.BIGTRASH = 6
        self.RUBBLE = 7
        self.NONMOVABLE = 8
        self.state = self.DFLOOR
        
    
    #this reset just resets the images
    def reset(self, level):
        if level == 2:
            self.images = [
                ("DirtyBrick.png"),
                ("CleanBrick.png"),
                ("DirtyCarpet.png"),
                ("CleanCarpet.png"),
                ("Trash2.jpeg"),
                ("TrashBag.png"),
                ("transparent.png"),
                ("Rubble2.jpeg"),
                ("transparent.png")
                ]
        elif level == 3:
            self.images = [
                ("DirtyBrick.png"),
                ("CleanBrick.png"),
                ("DirtyCarpet.png"),
                ("CleanCarpet.png"),
                ("Trash3.jpeg"),
                ("TrashBag.png"),
                ("transparent.png"),
                ("Rubble3.jpeg"),
                ("transparent.png")
                ]

    def setState(self, state):
        self.state = state
        self.setImage(self.images[state])
        self.setSize(32,32)
   

    def checkEvents(self):
      
        #clean floor
        if self.scene.isKeyPressed(pygame.K_w):
            bruh = False
           #Making sure that no other action command 
           #is being pressed
            if self.scene.isKeyPressed(pygame.K_a):
                bruh = True
            elif self.scene.isKeyPressed(pygame.K_s):
                bruh = True
            elif self.scene.isKeyPressed(pygame.K_d):
                bruh = True
        
            if bruh == False:
                if self.distanceTo(self.janLoc) <= 20:
                    if self.state == 0:
                        self.setState(1)
                        Tile.totalTileCount += 1
                        print(Tile.totalTileCount)
                        if Tile.totalTileCount == 81:
                            print("we got here")
                            self.scene.level += 1
                            self.scene.updateLevel()
        
        #clean rug
        if self.scene.isKeyPressed(pygame.K_a):
            bruh = False
           #Making sure that no other action command 
           #is being pressed
            if self.scene.isKeyPressed(pygame.K_w):
                bruh = True
            elif self.scene.isKeyPressed(pygame.K_s):
                bruh = True
            elif self.scene.isKeyPressed(pygame.K_d):
                bruh = True
            
            if bruh == False:
                if self.distanceTo(self.janLoc) <= 20:
                    if self.state == 2:
                        self.setState(3)
                        Tile.totalTileCount += 1
                        print(Tile.totalTileCount)
                        if Tile.totalTileCount == 81:
                            self.scene.level += 1
                            self.scene.updateLevel()
        
        #clean trash
        if self.scene.isKeyPressed(pygame.K_s):
            bruh = False
           #Making sure that no other action command 
           #is being pressed
            if self.scene.isKeyPressed(pygame.K_w):
                bruh = True
            elif self.scene.isKeyPressed(pygame.K_a):
                bruh = True
            elif self.scene.isKeyPressed(pygame.K_d):
                bruh = True
            
            if bruh == False:
                if self.distanceTo(self.janLoc) <= 20:
                    if self.state == 4:
                        self.setState(5)
                        Tile.totalTileCount += 1
                        print(Tile.totalTileCount)

                        if Tile.totalTileCount == 81:
                            self.scene.level += 1
                            self.scene.updateLevel()

                    if self.state == 7:
                        self.setState(5)
                        Tile.totalTileCount += 1
                        print(Tile.totalTileCount)

                        if Tile.totalTileCount == 81:
                            self.scene.level += 1
                            self.scene.updateLevel()

        #break big trash
        if self.scene.isKeyPressed(pygame.K_d):
            bruh = False
            #Making sure that no other action command 
            #is being pressed
            if self.scene.isKeyPressed(pygame.K_w):
                bruh = True
            elif self.scene.isKeyPressed(pygame.K_a):
                bruh = True
            elif self.scene.isKeyPressed(pygame.K_s):
                bruh = True
                
            if bruh == False:
                if self.distanceTo(self.janLoc) <= 20:
                    if self.state == 6:
                        self.setState(7)
                        


        
class Janitor(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setPosition((145, 250))
        #Set janitor level
        self.moveSpeed = 5
        
        #janLoc means Janitor Location
        Tile.janLoc = [self.x, self.y]
        self.images = [
            ("JanFront1.png"),
            ("JanFront2.png"),
            ("JanFront1.png"),
            ("JanFront3.png"),
            
            ("JanBack1.png"),
            ("JanBack2.png"),
            ("JanBack1.png"),
            ("JanBack3.png"),
            
            ("JanLeft1.png"),
            ("JanLeft2.png"),
            
            ("JanRight1.png"),
            ("JanRight2.png")
            ]
        self.state = 0
        self.setState(0)

    def setState(self,state):
        self.state = state
        self.setImage(self.images[state])
        self.setSize(32,32)
    '''
    139 Can I have the engine run delay before playing
    the next sprite? So my sprite animation will be
    slower?
    '''
    
    '''
    290 Y IS OUT OF BOUNDS
    '''
    def update(self):
        super().update()
        if self.y >= 277:
            if self.scene.isKeyPressed(pygame.K_DOWN):
                self.y = 0
            elif self.scene.isKeyPressed(pygame.K_UP):
                self.y = 278
     
    def checkEvents(self):
        if self.scene.isKeyPressed(pygame.K_h):
            print("X:")
            print(self.x)
            print("Y:")
            print(self.y)
        
            #SPRITES 10, 11
        if self.scene.isKeyPressed(pygame.K_RIGHT):
            self.x += (self.moveSpeed)
            Tile.janLoc = [self.x, self.y]
            if self.state == 10:
                self.setState(11)
            else:
                self.setState(10)
                
            #SPRITES 4,5,6,7
        if self.scene.isKeyPressed(pygame.K_UP):
            self.y -= (self.moveSpeed)
            
            Tile.janLoc = [self.x, self.y]
            
            if self.state == 4:
                self.setState(5)
            elif self.state == 5:
                self.setState(6)
            elif self.state == 6:
                self.setState(7)
            else:
                self.setState(4)
            #SPRITES 0,1,2,3
        if self.scene.isKeyPressed(pygame.K_DOWN):
            self.y += (self.moveSpeed)        
            Tile.janLoc = [self.x, self.y]
            
        
            if self.state == 0:
                self.setState(1)
            elif self.state == 1:
                self.setState(2)
            elif self.state == 2:
                self.setState(3)
            else:
                self.setState(0)
            #SPRITES 8,9
        if self.scene.isKeyPressed(pygame.K_LEFT):
            self.x -= (self.moveSpeed)
            Tile.janLoc = [self.x, self.y]
            if self.state == 9:
                self.setState(8)
            else:
                self.setState(9)
                
                

class BigObject(simpleGE.BasicSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("chandaler.png")
        self.setSize(96,64)
        self.x = 144
        self.y = 128
        
    def updateImage(self):
        if self.scene.level == 2:
            self.setImage("Chair.jpeg")
            self.setSize(288,288)
            self.x = 144
            self.y = 144
        
        else:
            self.setImage("Throne.jpeg")
            self.setSize(288,288)
            self.x = 144
            self.y = 144

class LblTimer(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.timer = simpleGE.Timer()
        self.timeOver = False
        self.font = pygame.font.Font("Onesize2.TTF", 20)
        self.bgColor = ("black")
        self.fgColor = ("red")
        self.size = (288, 30)
        self.hide()
        
    def checkEvents(self):
        self.timeleft = self.timeTic - self.timer.getElapsedTime()
        self.text = f"TIME LEFT : {self.timeleft:.0f}"
        if self.center[0] < 0:
            self.timeleft = 1000
        if self.timeleft < 0:
            self.timeOver = True
            

    def reset(self, level):
        self.timeOver = False
        self.center = (145, 301)
        #changes time based on level
        if level == 1:
            self.timeTic = 40 
        elif level == 2:
            self.timeTic = 35
        elif level == 3:
            self.timeTic = 30 
        self.timer.start()
        

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.set_mode((288, 318))
        self.setCaption("Janitor")
        #init music
        self.music = pygame.mixer.Sound("TheForest.wav")
        self.music.play(-1)
        #init Game() varriables
        self.ROWS = 9
        self.COLS = 9
        self.level = 1
        #setting sprites
        self.tileset = []
        self.janitor=Janitor(self)
        self.chandalear = BigObject(self)
        self.chairs = BigObject(self)
        self.time = LblTimer()
        self.sprites = [self.chandalear,  self.chairs, self.tileset,  self.janitor, self.time,]
        
        #maps
        self.map1 = [
            [0,0,0,2,2,2,0,0,0],  
            [0,0,0,2,2,2,0,4,0],  
            [0,4,0,2,2,2,0,0,0],  
            [2,2,2,6,6,6,2,2,2],  
            [2,2,2,6,6,6,2,2,2],  
            [0,0,0,2,2,2,0,0,4],  
            [4,0,0,2,2,2,0,0,0],  
            [0,0,0,2,2,2,0,4,0],  
            [0,0,0,2,2,2,0,0,0],  
        ]
        self.map2 = [
            [0,2,0,0,4,0,0,2,0],  
            [2,2,2,0,0,0,2,2,2],  
            [0,2,4,8,8,8,4,2,0],  
            [6,6,0,8,8,8,0,6,6],  
            [0,0,0,8,8,8,0,4,0],  
            [0,6,6,8,8,8,0,0,0],  
            [0,2,0,8,8,8,0,2,0],  
            [2,2,2,0,0,0,2,2,2],  
            [0,2,0,0,4,6,6,2,0],  
        ]
        self.map3 = [
            [4,0,0,8,8,8,0,0,0],  
            [6,6,0,8,8,8,4,0,0],  
            [0,0,0,2,2,2,0,6,6],  
            [0,0,4,2,2,2,0,0,0],  
            [0,4,0,2,2,2,0,0,0],  
            [0,0,0,2,2,2,0,4,0],  
            [0,6,6,2,2,2,0,0,0],  
            [0,0,0,2,2,2,0,0,0],  
            [0,0,4,2,2,2,4,6,6],  
        ]
        self.map = self.map1
        self.updateLevel()
        
    def updateLevel(self):
        if self.level == 1:
            self.map = self.map1
            self.loadMap()
            Tile.totalTileCount = 0
            
        elif self.level == 2:
            self.map = self.map2
            self.chairs.updateImage()
            self.resetMap()
            Tile.totalTileCount = 15
        
        elif self.level == 3:
            print("WE GOT HERE 2")
            self.map = self.map3
            self.chairs.updateImage()
            self.resetMap()
            Tile.totalTileCount = 6
        
        elif self.level == 4:
            self.music.stop()
            win = Win()
            win.start()
        

    def update(self):
        super().update()
        if self.time.timeOver == True:
            self.music.stop()
            gameover = GameOver()
            gameover.start()
       
      
            

    def loadMap(self):
        self.tileset = []
        for row in range(self.ROWS):
            self.tileset.append([])
            for col in range(self.COLS):
                currentVal = self.map[row][col]
                self.newTile = Tile(self)
                self.newTile.setState(currentVal)
                xPos = 16+ (32 * col)
                yPos = 16+ (32 * row)
                #newTile.setPosition((xPos, yPos))
                self.newTile.x = xPos
                self.newTile.y = yPos
                self.tileset[row].append(self.newTile)
                
        self.sprites = [self.chandalear,  self.chairs,  self.tileset, self.janitor, self.time,]
        self.time.reset(self.level)
   
   
    ''' RESET MAP CHANGES CURRENT TILESET VALUES
        EVENTUALLY, HAVE RESETMAP AND LOAD MAP THE SAME FUNCTION
    '''
    def resetMap(self):
        print(self.map)
        for row in range(self.ROWS):
            self.tileset.append([])
            for col in range(self.COLS):
                currentVal = self.map[row][col]
                self.newTile = self.tileset[row][col]
                self.newTile.reset(self.level)
                self.newTile.setState(currentVal)
                xPos = 16+ (32 * col)
                yPos = 16+ (32 * row)
                #newTile.setPosition((xPos, yPos))
                self.newTile.x = xPos
                self.newTile.y = yPos
                print(self.newTile.state)
                
        self.sprites = [self.chandalear,  self.chairs, self.tileset, self.janitor, self.time]
        self.janitor.setPosition((145, 250))
        self.time.reset(self.level)

class Intro(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.set_mode((288, 318))
        self.setCaption("Dear sir Janitor...")
        self.backgroundIMG = BackgroundIMG(self)
        self.lblOutput = TransparentLabel()
        
        self.lblOutput.font = pygame.font.Font("Onesize2.TTF", 17)
        self.lblOutput.center = ((146, 140))
        self.lblOutput.fgColor = ("black")
        self.lblOutput.size = (308, 260)

        self.lblOutput.textLines = ["    DEAR SIR JANITOR,", "      Due to a bananza held", "       in my castle halls,", 
                                    "     the castle is in a", "       desperate need for", "       a deep cleaning.","     Thank you.", "    Love,  King Rodger"
                                    ]

        
        self.sprites = [self.backgroundIMG, self.lblOutput]
        self.money = 0
        self.clicked = False
    
class BackgroundIMG(simpleGE.BasicSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Letter.jpeg")
        self.setSize(288, 288)
        self.x = 144
        self.y = 150
        self.clicked = False
        self.active = False
        self.money = 0
        
        
    def checkClick(self):
        #check for clicked and active                
        
        self.clicked = False
    
        #check for mouse input
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.active = True
    
        #check for mouse release
        if self.active == True:
            if pygame.mouse.get_pressed() == (0, 0, 0):
                self.active = False
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.clicked = True

    def checkEvents(self):
        self.checkClick()
        if self.clicked:
            if self.money == 0:
                self.setImage("Instructions.jpeg")
                self.setSize(288, 288)
                self.x = 144  
                self.y = 150
                self.money += 1
                self.scene.lblOutput.hide()
                print(self.money)
            elif self.money == 1:
                game = Game()
                game.start()
                
class TransparentLabel(simpleGE.MultiLabel):
    def __init__(self):
        super().__init__()
    
    def update(self):
        super().update()
        self.image.set_colorkey(self.bgColor)
        

class GameOver(simpleGE.Scene):
    def __init__(self):
        super().__init__()

        self.screen = pygame.display.set_mode((288, 318))
        self.setCaption("GAME OVER!")
        self.music = pygame.mixer.Sound("Lose.wav")
        self.music.play(0)
        self.gameoverIMG = GameOverIMG(self)
        self.btnreset = ResetButton()
        self.btnquit = QuitButton()
        self.sprites = [self.gameoverIMG, self.btnreset, self.btnquit]
    
    def update(self):
        if self.btnreset.clicked:
            game = Game()
            game.start()
        if self.btnquit.clicked:
            self.stop()

class GameOverIMG(simpleGE.BasicSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("GameOver.jpeg")
        self.setSize(288, 288)
        self.x = 144
        self.y = 150


class ResetButton(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.text = "Try Again"
        self.size = (130, 30)
        self.center = (95, 280)
        self.font = pygame.font.Font("Onesize2.TTF", 20)
        self.fgColor = ("green")
        self.bgColor = ("black")

class QuitButton(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.text = "Give Up"
        self.size = (90, 30)
        self.center = (215, 280)
        self.font = pygame.font.Font("Onesize2.TTF", 20)
        self.fgColor = ("red")
        self.bgColor = ("black")

class Win(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.set_mode((288, 318))
        self.setCaption("YOU WIN!!!")
        self.music = pygame.mixer.Sound("Win.wav")
        self.music.play(0)
        self.winIMG = WinIMG(self)
        self.sprites = [self.winIMG]

class WinIMG(simpleGE.BasicSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Win.jpeg")
        self.setSize(288, 288)
        self.x = 144
        self.y = 150


   
        
def main():
    intro = Intro()
    intro.start()
    '''
    game = Game()
    game.start()
    '''
    
if __name__ == "__main__":
    main()