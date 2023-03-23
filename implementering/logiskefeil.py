assert 10 > 5 # 10 er større enn 5, derfor gjør denne ingenting

try:    
    assert 10 > 20 # 10 er ikke større enn 20, derfor gir denne en feilemlding
except:
    print("Hei på deg")

# Oppgave: definer en funksjon med navn areal, som tar inn høyde og bredde og returener 
#          arealet av en rektangel med tilsvarende høyde og bredde

def areal(høyde,bredde):
    return høyde * bredde

def omkrets(høyde, bredde):
    return høyde + høyde + bredde + bredde

# Oppgave : test funskjonen areal på tre forskjellige rektangler

assert areal(3,2) == 6
assert areal(3,3) == 9
assert areal(3,4) == 12
assert omkrets(3,2) == 10
assert omkrets(3,3) == 12
assert omkrets(3,4) == 14


print("koden er ferdig")