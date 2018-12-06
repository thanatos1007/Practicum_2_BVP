def creeer_wereld (hoogte,breed):
    lijst = []
    return lijst
def geef_aantal_overvallen (wereld):
    al_ingevoerd = len.lijst
    return (al_ingevoerd)
def geef_aantal_overvallen_op_positie (wereld, x, y):
    gevonden = False
    while gevonden == false:
        a = 0
        if x == lijst[a][0] and y == lijst[a][1] :
            gevonden = true
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
    while gevonden == false:
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
    # er is een overval gebeurd op positie (x,y), deze
    # functie voegt die informatie toe aan de wereld en geeft
    # als resultaat True terug; indien (x,y) zich buiten de
    # ‘grenzen’ van de wereld bevindt, geeft de functie
    # False terug
