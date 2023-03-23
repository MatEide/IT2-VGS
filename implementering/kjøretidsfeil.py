# try:
#     alder = int(input("ALder: "))
#     fødselsår = 2022 - alder
#     print(f"Fødselsår: {fødselsår}")
# except:
#     print("Feil: alder må være et heltall")

# print("koden fortsetter")

while True:
    try:
        alder = int(input("ALder: "))
        assert alder >=0
        break 
    except:
        print("Feil: alder må være et heltall")

fødselsår = 2022 - alder
print(f"Fødselsår: {fødselsår}")
        
