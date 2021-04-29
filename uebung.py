
def summe(liste):
    menge = 0
    for n in liste:
        menge += n
    return menge

def mittelwert(liste):
    pass

def minmax(liste):
    pass

def spannweite(liste):
    pass

ergebnis = summe([2, 4.3, -1, 9])
print(ergebnis) # Ausgabe: 14.3


ergebnis = mittelwert([2, 4.3, -1, 9])
print(ergebnis) # Ausgabe: 3.575


paar = minmax([8, 3, 10.9, -3, 17, 0])
print(paar) # Ausgabe: (-3, 17)


print(spannweite( [2, 5, 4.3, 9])) # Ausgabe: 7


