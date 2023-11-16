import pygame

class Fugl():
    def __init__(self):
        self.images=[]#lager en tom liste med bilder
        for num in range(1,4):
            img = pygame.image.load(f"bilder/bird{num}.png") #istede for å legge inn manuelt allebildene så blir bilde hva en num er
            self.images.append(img)#legger til img i listen images
            #nå har jeg en liste som vil inneholde alle tre bildene  
        self.index= 0#sier noe om hvilket at bildene i listen som skal vises til hvilken tid. starter med 0 fordi null altid er første punkt i listen
        self.image= self.images[self.index]#self.image vil bli det bilde som indexen indikerer til

        self.rect= self.image.get_rect() #lager en rektanget rundt bildet
        self.rect.center= [150,400] #sier hvor rektangeletskal bli possisjonert
        #dette er nok til å lage basicsene for fugl klassen
        self.fart = 0
        self.tyngdekraft = 0

        #skal gjøre slik at fuggelen flakser gjennom tre ulike bilder:
        self.counter=0 #kontrolerer farten på hvordan animasjonen skal foregå
        self.image= self.images[self.index]#self.image vil bli det bilde som indexen indikerer til
        
       
    def beveg_fugl(self): 
        self.fart += self.tyngdekraft # Opddaterer farten med tyngdeakselerasjonen
        if self.rect.bottom <668: #gjelder kun så lenge fuggelen er over bakken
            self.rect.centery += self.fart # Oppdaterer posisjonen med farten
        
    
    def oppdatere(self):
        #håntere animasjonen
        self.counter += 1
        flap_cooldown= 5 #jo høyere dette tallet er, jo treigere blir flaksingen
        if self.counter>flap_cooldown:
            self.counter=0
            self.index+=1
            if self.index >= len(self.images): #sier at hvis talet i indexen når lengden av listen altså til det siste bilde, så starter den på nytt med første
                self.index = 0
        self.image= self.images[self.index] #oppdaterer fugl bildet
        self.image = pygame.transform.rotate(self.images[self.index], self.fart * -3) #ønsker å rotere fugelen i sammenheng med farten, siste variabelen sier noe om vinkelen på rotasjonen

        #roterer fugelen
        
        

    def flaks(self): #har dette i en egen slik at tyngdekraftn ikke begynner før du har trykket på space knappen
        self.tyngdekraft = 0.4 
        self.fart = -10
        
        

       
    
    def tegn(self, vindu):
        vindu.blit(self.image, self.rect) # TEGNER BILDET PÅ VINDUET