import pygame

class Knapp():
    def __init__(self, x, y, image):
        self.image=image
        self.rect= self.image.get_rect()
        self.rect.topleft= (x,y)

    def draw(self, vindu, ):
        action = False
        
        #fine musens posisjon
        pos= pygame.mouse.get_pos()#gir meg en x og y kordinat for hvor musen er
        #skjeke om musen er over knppen (skjekke retter kolisjon)
        if self.rect.collidepoint(pos): # hvis musen kolliderer/treffer knappen
            if pygame.mouse.get_pressed()[0]==1: #get_pressed returnere listen med de ulike knappene. plass 0 i lista er venstreklikk knappen. hvis den er lik 1 så er den klikket
                action = True #Ja musen har trukket på rektangelet
            
        vindu.blit(self.image, (self.rect.x, self.rect.y))

        return action #vil alltid være false med mindre du trykker på knappen