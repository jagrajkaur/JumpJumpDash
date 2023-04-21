import pygame

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        restart_the_game = False

        pos = pygame.mouse.get_pos()

        # Import dash_screen locally to avoid the circular import problem
        from jumpjump_dash import screen as dash_screen

        #check if mouse over and clicked
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:     # left mouse click
                restart_the_game = True
                self.clicked = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        # draw the btton
        dash_screen.blit(self.image, self.rect)
        
        return restart_the_game