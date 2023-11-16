#spillprosjekt IT 2

prossesen av oppbygningen til spillet:
1. sette opp den generelle formen for en pygame kropp, som er det som får spillet til å funke

2. lage bakgrunn og bakke, og bakken skal bevege seg:
- putte på bakrunnen i en posisjon som etterlater et sort område under som gir plass til bakken.
- bakken putter vi i det sorte området. vi gjør at bakken flytter seg -4 til venstre hele tiden, men fordi bakken bare er et bilde vil strekene på bildet etter hvert slutte å komme og bakken blir til slutt stille. dette fikser vi ved å å si at når bakken når -35 på y-aksen så flytter bildet seg tilbake til start slik at den går evig.

3. lage klassen "fuggl"
- lager en beveg funskjon
- lager en flaks funksjon
- lager en tegn funksjon
- skriver i spill.py at fugl er det samme som Fugl klassen, så aktiverer jeg fuggelens beveg funksjon(den gjør at når jeg trykker på mellombromm så hopper fugglen), deretter tegner jeg fuggelen
- når jeg skal få fuggelen til å flakse lager jeg bare en liste med de tre bildene av fuglene.
- lager en oppdater funksjon. I denen funksjonen hånterer jeg animasjonen av fugleflaksingen. jeg sier noe om hvor fort jeg skal bytte mellom fugl bildene, dertter sier jeg at når indexen har kommet til slutten av listen, så skal den starte listen på nytt.

4. håntere taste input
- skriver at når jeg trykker på mellombromknappen så kjører jeg flaks funksjonen

5. håntere fuglens rotasjoner
- bruker "rotate" funksjonen. jeg ønsker å rotere fugelen i sammenheng med farten. den siste variabelen sier noe om vinkelen på rotasjonen. gangen self.fart med -2 fordi slef.fart er allerede en negativ funksjon, somgjør at om jeg ikke ganget den med -2 ville fuglen rotert motsatt vei av hvilken retning den gikk

6. game_over
- skriver at game_over = false, med mindre fugl har nådd bakken, da blir game_over = True, og da vil bakken slutte å bevege seg. 

7. lager klassen pipe
- vi arver fra klassen "pygame.sprite.sprite", dette er en klasse som pygame allerede har laget for oss. den hjelper deg med å organisere spillobjekter ved å gi en struktur som lar deg oppdatere og tegne dem enkelt. den har oppdater og tegn funksjon allerede i seg som gjør at vi ikke trenger å skrive det hver gang. gjør også at vi ikke trenger bruke "blit" funksjonen
- når vi lager Pipe klassen, gjør vi likt som i Fugl klassenog; tar inn et bilde, lager en boks rundt bildet og gir det en x og y possisjon. deretter lager jeg en pipe Gruppe, og inni denen gruppen legger jeg til bottom_pipe, som skal være pipen som kommer opp fra bakken. Grupper er for sprite objekter. hovedoppgaven er å enklere oppdatere, tegne og fjerne objektene fra spillet. 
- så lager vi øvre pipe. pygame har en funksjon for å flippe bilder. for å gjøre dte enkelt legegr jeg til "position" argumentet inn i INIT. så sier jeg at om possition==1 så skal bildet flippes og det blir topp-pipen, og om position er -1 så står bildet stille og er bunnpipen
- så har jeg definert pipe_gap, og bruker dette når jeg gir en y verdi til begge pipene
- deretter er dte å få pipene til å scrolle sammen med bakken. jeg sier at pipens x-kordinat er lik skroll_speed, så putta jeg skroll_speed inn i pipe_group.update()
- nå vil jeg at pipene skal fortsete å dukke opp så lenge game_over == False. hvis tiden_nå minus siste_pipe er større en pipe-frequensien, betyr det et dte har gått nok tid til at dte er på tide å lage ny pipe

8. lage kollisjoner
- nå skla jeg lage kolisjon mellom fugelen og pipene


