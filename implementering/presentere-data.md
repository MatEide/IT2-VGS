# Presentere data

Med data mener vi all mulig informasjon, det kan f.eks. være tempraturer, tekst,
bilder, filmer.

I IT2 lærer vi om to forskjellige måter å presentere data på, nemlig ved tegning
av grafer og med nettsider.

## Tegne grafer 

For å tegne grafer i python kan vi bruke bibloteket `matplotlib`.  

> Installere matplotlib: `pip3 install matplotlib`

``` python 

# Nyttige kommandoer:
    title("tekst") # tittel over grafen
    xlabel("tekst") # tittel til x-aksen
    ylabel("tekst") # tittel til y-aksen
    axhline(y=0) # vannrett (horisontal) linje gjennom y-aksen
    axvline(x=0) # Loddrett (vertikal) linje gjennom x-aksen
    grid() # Legger til et rutenett
    xlim(-2, 2) # Bestemmer hvilke x-verdier som skal være synlige i grafen
    ylim(0, 4) #Bestemmer hvilke y-verdier som skal være synlige i grafen
```

## Eksempel

[Plotting av kolsåstoppen](./innhente-data)

## Lage nettsider (HTML/Flask)

