import pygame
from pygame.locals import *
import random

from fugl import Fugl
from pipe import Pipe
from knapp import Knapp
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
game_over= False
game_start= False
pipe_gap= 200
pipe_frequency= 1500#millisekunder #hvor ofte vil jeg at pipene skal dukke opp?
siste_pipe= pygame.time.get_ticks()- pipe_frequency#skjekek når siste pipe ble laget, og sammenligne med tiden. når spillet starter er det ingen piper. så til å starte med er last_pipe er når spilet først starter. tar -pipe frequencu for at dne skal starte med en gang
score= 0



fugl = Fugl()# sier fugl er det samme som Fugl klassen

pipe_group=pygame.sprite.Group() #her oppretter jeg en pipe gruppe




#bilder
bakgrunn= pygame.image.load("bilder/bg.png")
bakke= pygame.image.load("bilder/bakke.png")
restart_img= pygame.image.load("bilder/restart.png")

knapp= Knapp(BREDDE//2 -50, HOIDE//2 -100, restart_img)

def reset_game():
    pipe_group.empty()#fjerner alt i pipe gruppen som gjør at jeg kan starte på nytt
    #setter fuglen tilbake på plass:
    fugl.rect.x= 150
    fugl.rect.y=400
    score = 0
    return score#returner score i min reset funksjon



while True:
#2. hånter input

    
    

    for hendelse in pygame.event.get():
        if hendelse.type== pygame.QUIT:
            pygame.quit()
            raise SystemExit
            #vinduet forsvinner når du trykker kryss
        if hendelse.type == pygame.KEYDOWN: # Sjekker om noen trykker på en knapp
            
            if hendelse.key == pygame.K_SPACE: # Sjekker om de trykker på spacebaren
                game_start = True
                fugl.flaks() # Kjører funksjon for å endre farten (Flakse)

                 #generere nye piper
                time_now= pygame.time.get_ticks() #for å vite hvor mye tid somhargått må jeg vite hva tiden er nå
                pipe_hoide= random.randint(-100,100)
                if time_now -siste_pipe > pipe_frequency: #hvis tiden nå-siste pipe ble laget er større en pipe.frequensien, betyr det et dte har gått nok tid til at dte er på tide å lage ny pipe
                    btm_pipe = Pipe(BREDDE,int(HOIDE/2)+pipe_hoide, -1, pipe_gap,)
                    top_pipe = Pipe(BREDDE,int(HOIDE/2)+pipe_hoide, 1, pipe_gap)
                    pipe_group.add(btm_pipe) #Dette gjør at røret blir en del av gruppen, og det kan nå håndteres og oppdateres sammen med andre rør-objekter som kan bli lagt til senere.
                    pipe_group.add(top_pipe)
                    siste_pipe= time_now

            
                       
            


        


#3. oppdater spill

    if game_start == True and game_over == False :
    #tegne skrolle bakken:
        bakke_skroll -=skroll_speed
        if abs(bakke_skroll)>35: #hvis absoluttverdien til absolutt_skroll er 35, så reasetter vi bakken.
            bakke_skroll=0
        
        #skjekke om det blir kolisjon
        for pipe in pipe_group:
            if fugl.rect.colliderect(pipe.rect) or fugl.rect.top < 0: #hvis fugelen treffer pipe eller går over kkjermen
                game_over=True
             
             #score
            if pipe.passed == False:
        
                if pipe.rect.right < fugl.rect.left:
                    pipe.passed = True
                    

                if pipe.passed == True:
                    score += 0.5
                     
                    


    fugl.beveg_fugl()# aktiverer funksjonen starter tyngdekraften
    # oppdaterer kun fuglen og pipenes x retning mens du fremdeles "lever"
    if game_over == False:
        fugl.oppdatere()
        pipe_group.update(skroll_speed)

   
   
    
   
#4. tegn

    #tegne bakgrunn:
    vindu.blit(bakgrunn, (0,0))#legger inn bakrunnsbildet fra og med punkt 0,0 som er toppen vesntre hjørne


     #skjekk om fuglen har truffet bakken
    if fugl.rect.centery >= 650:
        game_over = True

   
    #tegn pipe
    pipe_group.draw(vindu)

    #tegn bakken:
    vindu.blit(bakke, (bakke_skroll,668)) #"blit" fungerer ved å kopiere pikslene fra kilden (i dette tilfellet, bildet) til destinasjonen (skjermen) på de spesifikke koordinatene du angir. 

    #tegne fugl:
    fugl.tegn(vindu)#skjører funksjonen tegn, og må sende med overflaten jeg skal tegne på

    #skrive scoren øverst i hjørnet
    font = pygame.font.Font(None, 50)
    score_text = font.render(f"Poeng: {int(score)}", True, (255, 255, 255))
    vindu.blit(score_text, (350, 20))
    
    #tegne restart knapp
    if game_over == True:
        if knapp.draw(vindu) == True: #hvis du har trykket på knappen
            game_over= False 
            game_start= False
            fugl.stopp()
            score= reset_game()



    
    pygame.display.flip() #oppdaterer spillet for alt som er skrevet over
    klokke.tick(FPS)
