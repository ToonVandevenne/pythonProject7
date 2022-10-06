"""getal = 11
if getal < 10:
    print("het getal is kleiner dan 10")
else:
    print("het getal is groter dan 10")"""

"""aantal_liter=float(input("geef het aantal liter in"))
brandstof=(input("Benzine of Diesel, b of d"))
if brandstof == "b":
    print(aantal_liter*1.75)
else:
    print(aantal_liter*1.92)"""

woord=input("schrijf een woord")
if len(woord) < 4:
    print("dit is een heel kort woord")
elif len(woord) <6:
    print("dit is een kort woord")
elif len(woord) <10:
    print("dit is een gemiddeld woord")
else:
    print("dit is een lang woord")