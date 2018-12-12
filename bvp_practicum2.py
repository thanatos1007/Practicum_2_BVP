def creeer_wereld (hoogte,breed):
    list= []
    wereld_afmetingen = (hoogte, breed,"Ametingen wereld")
    list.append (wereld_afmetingen)
    #Ik geef hier een standaardformaat in zodat er al tuppels zijn met 3 elementen
    standaardformaat = ("x-co", "y-co", "aantal")
    list.append(standaardformaat)
    return list

def geef_aantal_overvallen (wereld):
    #Telt de lengte van de wereld en verwijdert de eerste rij omdat hier de groootte van de wereld in zit en de tweede voor het standaardformaat
    i = 2
    totaal = 0
    while i <= len(wereld) - 1:
        totaal = totaal + wereld[i][2]
        i = i + 1
    return (totaal)

def geef_aantal_overvallen_op_positie (wereld, x, y):
    #door gegeven nemen we aan dat de combinatie (x,y) juist is
    a = 2
    de_juiste_koppels = []
    aantal_overvallen_op_positie = 0
    while a<= len(wereld)-1:
       # Er kunnen meerdere overvallen op dezelfde plaats zijn en dit moeten we aangeven:
        if x == wereld[a][0]  and y == wereld[a][1]:
            de_juiste_koppels.append(wereld[a])
            a= a+1
        else:
            a=a+1
    aantal_overvallen_op_positie = len(de_juiste_koppels)
    return(aantal_overvallen_op_positie)

def er_is_een_overval_gebeurd_op_positie (wereld, x, y):
    gevonden = False
    a = 2
    while a <= len(wereld)-1:
        if x == wereld[a][0] and y == wereld[a][1] :
            gevonden = True
            a = a+1
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
            #Als er al een overval in die regio is dan moet je het bij het aantal optellen
        #anders maak je een nieuw element aan


    if Binnen_grenzen == True:
        #zoeken of er al een is met dit koppel. Voeg dan toe aan het juiste koppel.
        toevoegen = (x,y,1)
        wereld.append(toevoegen)
    return Binnen_grenzen
