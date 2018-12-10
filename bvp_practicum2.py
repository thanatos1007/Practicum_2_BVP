lijst = []
def creeer_wereld (hoogte,breed):

    lijst.append = [hoogte, breed]
    return lijst
    # deze functie geeft een data-structuur die nog geen
		# informatie van overvallen bevat; hoogte en breedte zijn
		# geldige natuurlijke getallen (> 0)

def geef_aantal_overvallen (wereld):
    al_ingevoerd = len.lijst - 1

    return (al_ingevoerd)
def geef_aantal_overvallen_op_positie (wereld, x, y):
    gevonden = False 
    while gevonden == False:
        a = 0
        if x == lijst[a][0] and y == lijst[a][1] :
            gevonden = True
            tijdelijkeopslag = lijst[a]
        else:
            a = a+1
        aantal_overvallen_op_positie = lijst [a][2]
    return(aantal_overvallen_op_positie)
    # deze functie geeft een geheel getal terug dat aangeeft
    # van hoeveel overvallen informatie in deze wereld
    # is ingevoerd voor de positie (x,y);
    # (x,y) is een geldige positie in de wereld

def er_is_een_overval_gebeurd_op_positie (wereld, x, y):
    gevonden = False
    while gevonden == False:
        a = 0
        if x == lijst[a][0] and y == lijst[a][1] :
            gevonden = True
            tijdelijkeopslag = lijst[a]
        else:
            a = a+1

    return(gevonden)

    # deze functie geeft een Boolean terug die aangeeft
    # of voor de gegeven positie een overval werd ingevoerd;
    # (x,y) is een geldige positie in de wereld
def meeste_overvallen_in_regio (wereld):
    max_gevonden =  False
    c = 0
    max = lijst[c][2]
    while max_gevonden == False:
        if max < lijst[c+1][2]:
            max = lijst[c+1][2]
        else: 
            max_gevonden = True
            max = lijst[c][2]
    return (max)
    # deze functie geeft weer hoeveel overvallen voorkwamen
    # in de ‘gevaarlijkste’ regio, dat is de regio met de
    # meeste overvallen;
def voeg_overval_toe (wereld, x, y):
    lijst.append = (x,y, 1)
    Binnen_grenzen = True
    
    if (0 >= x or x >= lijst[0][0]) and (0>=y or y>=lijst[0][1]):
       Binnen_grenzen =False           
    else: 
        Binnen_grenzen = True
    return Binnen_grenzen
        #is een overval gebeurd op positie (x,y), deze
    # functie voegt die informatie toe aan de wereld en geeft
    # als resultaat True terug; indien (x,y) zich buiten de
    # ‘grenzen’ van de wereld bevindt, geeft de functie
    # False terug;
        hoogte = int(input("Geef de hoogte van de wereld: "))
    breedt = int(input("Geef een breedte van de wereld: "))
    while hoogte <= 0 or breedte <= 0:
        hoogte = int(input("Geef hoogte van de wereld: "))
        breedte = int(input("Geef een breedte van de wereld: ")