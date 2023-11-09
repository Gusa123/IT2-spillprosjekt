import pygame
from pygame.locals import *

#klasser:
fugl

#1. oppsett

pygame.init()
BREDDE=864
HOIDE=836#jeg har tatt høyden ned 100 i forhold til vidoen
FPS= 60
vindu= pygame.display.set_mode((BREDDE, HOIDE)) #lager vinduet
pygame.display.set_caption("Flappy bird") #lager en overskrift til psillet
klokke=pygame.time.Clock()

#definere spill variabler:
bakke_skroll= 0
skroll_speed= 4


#bilder
bakgrunn= pygame.image.load("bilder/bg.png")
bakke= pygame.image.load("bilder/bakke.png")

while True:
#2. hånter input
    for hendelse in pygame.event.get():
        if hendelse.type== pygame.QUIT:
            pygame.quit()
            raise SystemExit
            #vinduet forsvinner når du trykker kryss

    #tegne bakgrunn:
    vindu.blit(bakgrunn, (0,0))#legger inn bakrunnsbildet fra og med punkt 0,0 som er toppen vesntre hjørne
    #tegne og skrolle bakken:
    vindu.blit(bakke, (bakke_skroll,668))
    bakke_skroll -=skroll_speed
    if abs(bakke_skroll)>35: #hvis absoluttverdien til absolutt_skroll er 35, så reasetter vi bakken.
        bakke_skroll=0


#3. oppdater spill
   
#4. tegn

    pygame.display.flip() #oppdaterer spillet for alt som er skrevet over
    klokke.tick(FPS)
