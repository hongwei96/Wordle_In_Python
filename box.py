import pygame

class CharState:
    INACTIVE = 0
    PENDING = 1
    INCORRECT = 2
    WRONG_POS = 3
    RIGHT_POS = 4

class Box:
    def __init__(self):
        self.myfont = None
        self.fontCol = (255,255,255)
        self.character = ' '
        self.textSurface = None
        self.position = (0,0)
        self.offsetSize = (20,8)
        self.boxSize = (10,10)
        self.bgCol = (255,255,255)
        self.state = CharState.INACTIVE
        self.prevState = CharState.INACTIVE
        self.outlineWidth = 0

    def Config(self, font, fontcol = (255,255,255), pos = (0,0), size = (50, 50), state : CharState = CharState.INACTIVE):
        self.SetFont(font)
        self.SetFontColor(fontcol)
        self.SetPos(pos)
        self.SetSize(size)
        self.SetState(state)

    def SetFont(self, font):
        self.myfont = font
        self.SetChar('')
    
    def SetFontColor(self, col):
        self.fontCol = col

    def SetSize(self, size):
        self.boxSize = size
        self.offsetSize = (size[0] / 2 - self.myfont.get_height() / 4, size[1] / 2 - self.myfont.get_height() / 2.5)

    def SetState(self, state : CharState):
        self.prevState = self.state
        self.state = state
        if self.state == CharState.INACTIVE:
            self.bgCol = (100,100,100) # White
            self.outlineWidth = 1
        elif self.state == CharState.PENDING:
            self.bgCol = (200,200,200) # White
            self.outlineWidth = 2
        elif self.state == CharState.INCORRECT:
            self.bgCol = (200,200,200) # White
            self.outlineWidth = 0
        elif self.state == CharState.WRONG_POS:
            self.bgCol = (204,204,0) # Yellow
            self.outlineWidth = 0
        elif self.state == CharState.RIGHT_POS:
            self.bgCol = (32,204,32) # Green
            self.outlineWidth = 0

    def RevertState(self):
        self.SetState(self.prevState)

    def SetChar(self, char):
        self.character = char
        self.textSurface = self.myfont.render(self.character, False, self.fontCol)

    def SetPos(self, pos):
        self.position = pos

    def Reset(self):
        self.SetChar(' ')
        self.SetState(CharState.INACTIVE)

    def Draw(self, surface):
        pygame.draw.rect(surface, self.bgCol, pygame.Rect(self.position[0], self.position[1], self.boxSize[0], self.boxSize[1]), self.outlineWidth)
        surface.blit(self.textSurface,(self.position[0] + self.offsetSize[0], self.position[1] + self.offsetSize[1]))