import sys
import bvp_practicum2

################################################################################################################################
# TODO:
# 1) PUT THIS FILE IN THE SAME FOLDER AS THE PYTHON FILE CONTAINING YOUR SOLUTION                                              #
# 2) RUN THIS FILE                                                                                                             #
################################################################################################################################

# help functie voor het uitprinten van het resultaat van een test met gegeven nummer en boolean die het succes van de test weergeeft
def print_result(test_nb, succes_boolean):
    test_string = 'Test ' + str(test_nb)+':'
    if succes_boolean:
        print(test_string, 'correct')
    else:
        print(test_string, 'foutief')

# Testen voor de functie creeer_wereld(hoogte, breedte)
def test_creeer_wereld():
    # Test 1
    succes = False
    try:
        wereld = bvp_practicum2.creeer_wereld(1000, 1000)
        size = sys.getsizeof(wereld)
        succes = size < 500
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)

# Testen voor de functie voeg_overval_toe(wereld, x, y)
def test_voeg_overval_toe():
    # Test 1
    succes = False
    try:
        wereld = bvp_practicum2.creeer_wereld(200, 300)
        result = bvp_practicum2.voeg_overval_toe(wereld, -1, 100)
        succes = result == False
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)
    # Test 2
    succes = False
    try:
        wereld = bvp_practicum2.creeer_wereld(200, 300)
        result = bvp_practicum2.voeg_overval_toe(wereld, 100, -1)
        succes = result == False
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(2, succes)
    # Test 3
    succes = False
    try:
        wereld = bvp_practicum2.creeer_wereld(200, 300)
        result = bvp_practicum2.voeg_overval_toe(wereld, 100, 100)
        succes = result == True
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(3, succes)

# Testen voor de functie geef_aantal_overvallen(wereld)
def test_geef_aantal_overvallen():
    # Test 1
    succes = False
    try:
        wereld = bvp_practicum2.creeer_wereld(200, 300)
        result = bvp_practicum2.geef_aantal_overvallen(wereld)
        succes = result == 0
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)
    # Test 2
    succes = False
    try:
        wereld = bvp_practicum2.creeer_wereld(200, 300)
        bvp_practicum2.voeg_overval_toe(wereld,5,5)
        result = bvp_practicum2.geef_aantal_overvallen(wereld)
        succes = result == 1
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(2, succes)
    # Test 3
    succes = False
    try:
        wereld = bvp_practicum2.creeer_wereld(200, 300)
        bvp_practicum2.voeg_overval_toe(wereld, -5, 5)
        result = bvp_practicum2.geef_aantal_overvallen(wereld)
        succes = result == 0
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(3, succes)
    # Test 4
    succes = False
    try:
        wereld = bvp_practicum2.creeer_wereld(200, 300)
        bvp_practicum2.voeg_overval_toe(wereld, 5, 5)
        bvp_practicum2.voeg_overval_toe(wereld, 11, 7)
        bvp_practicum2.voeg_overval_toe(wereld, -5, 120)
        bvp_practicum2.voeg_overval_toe(wereld, 22, 165)
        result = bvp_practicum2.geef_aantal_overvallen(wereld)
        succes = result == 3
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(4, succes)

# Testen voor de functie geef_aantal_overvallen_op_positie(wereld, x, y)
def test_geef_aantal_overvallen_op_positie():
    # Test 1
    succes = False
    try:
        wereld = bvp_practicum2.creeer_wereld(200, 300)
        bvp_practicum2.voeg_overval_toe(wereld, 100, 100)
        result = bvp_practicum2.geef_aantal_overvallen_op_positie(wereld, 100, 200)
        succes = result == 0
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)
    # Test 2
    succes = False
    try:
        wereld = bvp_practicum2.creeer_wereld(200, 300)
        bvp_practicum2.voeg_overval_toe(wereld, 100, 100)
        result = bvp_practicum2.geef_aantal_overvallen_op_positie(wereld, 100, 100)
        succes = result == 1
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(2, succes)
    # Test 3
    succes = False
    try:
        wereld = bvp_practicum2.creeer_wereld(200, 300)
        bvp_practicum2.voeg_overval_toe(wereld, 100, 100)
        bvp_practicum2.voeg_overval_toe(wereld, 100, 200)
        bvp_practicum2.voeg_overval_toe(wereld, 100, 100)
        bvp_practicum2.voeg_overval_toe(wereld, 100, 155)
        bvp_practicum2.voeg_overval_toe(wereld, 100, 100)
        result = bvp_practicum2.geef_aantal_overvallen_op_positie(wereld, 100, 100)
        succes = result == 3
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(3, succes)

# Testen voor de functie er_is_een_overval_gebeurd_op_positie(wereld, x, y)
def test_er_is_een_overval_gebeurd_op_positie():
    # Test 1
    succes = False
    try:
        wereld = bvp_practicum2.creeer_wereld(200, 300)
        bvp_practicum2.voeg_overval_toe(wereld, 100, 100)
        result = bvp_practicum2.er_is_een_overval_gebeurd_op_positie(wereld, 100, 200)
        succes = result == False
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)
    # Test 2
    succes = False
    try:
        wereld = bvp_practicum2.creeer_wereld(200, 300)
        bvp_practicum2.voeg_overval_toe(wereld, 100, 100)
        result = bvp_practicum2.er_is_een_overval_gebeurd_op_positie(wereld, 100, 100)
        succes = result == True
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(2, succes)

# Testen voor de functie meeste_overvallen_in_regio(wereld)
def test_meeste_overvallen_in_regio():
    # Test 1
    succes = False
    try:
        wereld = bvp_practicum2.creeer_wereld(200, 300)
        result = bvp_practicum2.meeste_overvallen_in_regio(wereld)
        succes = result == 0
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)
    # Test 2
    succes = False
    try:
        wereld = bvp_practicum2.creeer_wereld(200, 300)
        bvp_practicum2.voeg_overval_toe(wereld, 100, 100)
        bvp_practicum2.voeg_overval_toe(wereld, 110, 100)
        bvp_practicum2.voeg_overval_toe(wereld, 110, 100)
        result = bvp_practicum2.meeste_overvallen_in_regio(wereld)
        succes = result == 2
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(2, succes)
    # Test 3
    succes = False
    try:
        wereld = bvp_practicum2.creeer_wereld(200, 300)
        bvp_practicum2.voeg_overval_toe(wereld, 100, 100)
        bvp_practicum2.voeg_overval_toe(wereld, 109, 109)
        bvp_practicum2.voeg_overval_toe(wereld, 109, 109)
        result = bvp_practicum2.meeste_overvallen_in_regio(wereld)
        succes = result == 3
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(3, succes)
    # Test 4
    succes = False
    try:
        wereld = bvp_practicum2.creeer_wereld(200, 300)
        bvp_practicum2.voeg_overval_toe(wereld, 100, 100)
        bvp_practicum2.voeg_overval_toe(wereld, 110, 110)
        bvp_practicum2.voeg_overval_toe(wereld, 110, 110)
        bvp_practicum2.voeg_overval_toe(wereld, 100, 200)
        bvp_practicum2.voeg_overval_toe(wereld, 105, 209)
        bvp_practicum2.voeg_overval_toe(wereld, 104, 209)
        result = bvp_practicum2.meeste_overvallen_in_regio(wereld)
        succes = result == 3
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(4, succes)

# Main part of the program: load all test cases and test them on given solution
def run_all_tests():
    print('###')
    print('Testen voor de functie:', 'creeer_wereld(wereld)')
    test_creeer_wereld()
    print('###')
    print('Testen voor de functie:', 'voeg_overval_toe(wereld, x, y)')
    test_voeg_overval_toe()
    print('###')
    print('Testen voor de functie:', 'geef_aantal_overvallen(wereld)')
    test_geef_aantal_overvallen()
    print('###')
    print('Testen voor de functie:', 'geef_aantal_overvallen_op_positie(wereld, x, y)')
    test_geef_aantal_overvallen_op_positie()
    print('###')
    print('Testen voor de functie:', 'er_is_een_overval_gebeurd_op_positie(wereld, x, y)')
    test_er_is_een_overval_gebeurd_op_positie()
    print('###')
    print('Testen voor de functie:', 'meeste_overvallen_in_regio(wereld)')
    test_meeste_overvallen_in_regio()

if __name__ == "__main__":
    run_all_tests()