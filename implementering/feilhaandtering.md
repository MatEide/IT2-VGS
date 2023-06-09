# Vern mot kjøretidsfeil og logiske feil i programmer 

## Kjøretidsfeil

håntering av kjøretidsfeil i Python gjøres med nøkkelordene try og except.
Python forsøker å kjøre kodeblokken som ligger under `try:`, hvis python får en feilmelding, vil den kjøre kodeblokken som ligger under `except:`

``` python 
try:
    alder = int(input("ALder: "))
    fødselsår = 2022 - alder
    print(f"Fødselsår: {fødselsår}")
except:
     print("Feil: alder må være et heltall")

print("koden fortsetter")

```

### Eksperttips 

``` python 
while True:
    try:
        alder = int(input("ALder: "))
        break 
    except:
        print("Feil: alder må være et heltall")
        
fødselsår = 2022 - alder
print(f"Fødselsår: {fødselsår}")

```

## Logiske feil i programmer 

For å oppdage logiske feil i python-programmer kan vi bruke nøkkelordet `assert` for å forsikre 
oss om at koden gir korrekte resultat 

``` python 
assert 10 > 5 # 10 er større enn 5, derfor gjør denne ingenting
assert 10 > 20 # 10 er ikke større enn 20, derfor gir denne en feilemlding
```

Eksempel: test av funksjoner med assert

``` python 
def areal(høyde,bredde):
    return høyde * bredde

def omkrets(høyde, bredde):
    return høyde + høyde + bredde + bredde

assert areal(3,2) == 6
assert areal(3,3) == 9
assert areal(3,4) == 12
assert omkrets(3,2) == 10
assert omkrets(3,3) == 12
assert omkrets(3,4) == 14
```

### Eksperttips: håndtering av kjøretidsfeil og logisk feil

``` python 
while True:
    try:
        alder = int(input("ALder: "))
        assert alder >=0
        break 
    except:
        print("Feil: alder må være et heltall")

fødselsår = 2022 - alder
print(f"Fødselsår: {fødselsår}")
```