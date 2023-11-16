import pygame
import random

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position, pipe_gap):
        pygame.sprite.Sprite.__init__(self) #vi arver vi fra pygame.sprite.sprite
        self.image= pygame.image.load("bilder/pipe.png")
        self.rect=self.image.get_rect() #lager en boks rundt bildet
        #position 1 er fra toppen, -1 er fra bakken
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True) #det er ikke x-aksen jeg vil flippe, det er Y-aksen
            self.rect.bottomleft = [x, y - int(pipe_gap/2 )] #siden bildet er flippet, så ønsker vi at x og y skal være fra nede-venstre
        if position == -1:
            self.rect.topleft=[x,y +int(pipe_gap/2 )] #Dette setter posisjonen til røret ved å tilordne verdien av x og y til topp-venstre hjørne av rektangelet (self.rect). Dermed blir røret plassert på den angitte posisjonen.


    def update(self, skroll_speed):
        self.rect.x -= skroll_speed
        if self.rect.right < 0: #etter pipene har gått borgi kjermen vil de fortsette og forflytte seg og fortsette å bli oppdatert.
            self.kill() #derfor fjerner vi pipene fra gruppen etetr det er fårbi 0 punkt