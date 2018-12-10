
def creeer_wereld (hoogte,breed):
    list= []
    wereld_afmetingen = (hoogte>=0, breed>=0)
    list.append (wereld_afmetingen)
    #Ik geef hier een standaardformaat in zodat er al tuppels zijn met 3 elementen
    standaardformaat = ("x-co", "y-co", "aantal")
    list.append(standaardformaat)
    return list

def geef_aantal_overvallen (wereld):
    #Telt de lengte van de wereld en verwijdert de eerste rij omdat hier de groootte van de wereld in zit
    al_ingevoerd = len(wereld) - 2
    return (al_ingevoerd)

def geef_aantal_overvallen_op_positie (wereld, x, y):
    #door gegeven nemen we aan dat de combinatie (x,y) juist is
    gevonden = False 
    a = 0
    while gevonden == False:
       # Er kunnen meerdere overvallen op dezelfde plaats zijn en dit moeten we aangeven
        if x == wereld[a][0] and y == wereld[a][1] :
            gevonden = True
            tijdelijkeopslag = wereld[a]
        else:
            if a in range(x*y):
                a = a+1
        aantal_overvallen_op_positie = wereld [a][2]
    return(aantal_overvallen_op_positie)
def er_is_een_overval_gebeurd_op_positie (wereld, x, y):
    gevonden = False
    while gevonden == False:
        a = 0
        if x == wereld[a][0] and y == wereld[a][1] :
            gevonden = True
            tijdelijkeopslag = wereld[a]
        else:
            a = a+1
    return(gevonden)
def meeste_overvallen_in_regio (wereld):
    max_gevonden =  False
    c = 2
    max = wereld[c][2]
    while max_gevonden == False:
        if max == wereld[c+1][2]:
            max  = wereld[c+1][2]
        else: 
            max_gevonden = True
            max = wereld[c][2]
    return (max)

def voeg_overval_toe (wereld, x, y):
    Binnen_grenzen = True
    if wereld[0][0] <= 0 or wereld[0][1]<=0:
        Binnen_grenzen = False
    elif 0 >= x or x > wereld[0][0] or 0>=y or y > wereld[0][1]:
       Binnen_grenzen = False           
    else: 
        Binnen_grenzen = True
        overvaltoevoegen = (x,y,1)
        wereld.append(overvaltoevoegen)
    return Binnen_grenzen
