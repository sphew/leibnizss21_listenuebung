


# Eine kleine Wiederholung zu Listen (siehe Kapitel 7)

namensliste = ["Kathrin", "Kilian", "Luzie", "Gabriel", "Johannes", "Claire", "Simeon", "Helene", "Lukas"]

print("namensliste =", namensliste)




#1) Iterieren 

# 1a) Sage jedem Hallo!
print("1a)")




# 1b) baue neue Listen  
eine_liste = [5, 42, 13, 17, 34, 65]
print("eine_liste =", eine_liste)

# die neue_liste soll jedes Element der eine_listei + 3 enthalten 
neue_liste = [] 
# ...
print("1b)", neue_liste)


# 1c) das gleiche einmal mit list comprehension
neuere_liste = []

print("1c)", neuere_liste)





    
# 2. Indexing 
"""
 0   1   2   3   4   5
 |   |   |   |   |   |
[5, 42, 13, 17, 34, 65]
 |   |   |   |   |   |
-6  -5  -4  -3  -2  -1 
"""

# 2a) Was ist das 2. Element (----> Index 1 !)
zweites = None
print("2a) 2. Element (Index 1):", zweites)

# 2b) Was ist das letzte Element?
letztes = None
print("2b) letztes Element:", letztes)

# 2c) Multipliziere Element mit Index 4 mit 6
#
print("2c)", eine_liste)

print("/_!_\ Die Liste ist jetzt veraendert.")
print("eine_liste =", eine_liste)






# 3. Slicing

# 3a) gib die ersten drei Elemente (Index 0, 1, 2.) aus
print("3a)") # /_!_\ Index 3 nicht enthalten

# 3b) Index 2 bis 4 
print("3b)")











# 4. Die Liste veraendern
print("/_!_\ Hier wird die Liste jedes Mal veraendert!")

# 4a) hinten anhaengen (Wert 15).
print("4a)", eine_liste)

# 4b) vorne anhaengen (Wert 6)
print("4b)", eine_liste)

# 4c) in der Mitte einfuegen (Wert 14 an 5. Stelle)
print("4c)", eine_liste)

# 4d) entferne das erste Element = behalte nur die letzten!
print("4d)", eine_liste)




# 5) Listen in Listen

zeile0 = [14, 56, 43, 65]
zeile1 = [62, 71, 20, 13]
zeile2 = [63, 54, 23, 90]

tabelle = [zeile0,  zeile1, zeile2]
print("tabelle =", tabelle)



# 5a) Greife auf Zeile 1 zu (aus der tabelle):
print("5a)") 


# 5b) Gib Wert 20 ueber seinen Index aus
zeile = 0    # zeilenwert anpassen
spalte = 0   # spaltenwert anpassen
print("5b)", tabelle[zeile][spalte])


# 5c) Ersetze den Wert an Position zeile = 2, spalte = 1 durch 42 (54 ---> 42)
print("5c)", tabelle)


# 5d) Erhalte Werte der Spalte 3
spalte3 = []
print("5d)", spalte3)

# 5d.2) Das ist der Grund, warum "echte" Matrizen oft geschickter sind.
import numpy as np
matr = np.array(tabelle)

#print(matr)
print("5d.2)", matr[:, 3])


# 6. Wir machen weiter mit numpy arrays (zweidimensional)
# In unserem Index geben wir jetzt Werte für Zeile und Spalte an, die wir wollen. 

# 6a) Greife auf Wert 13 zu. Zeileindex 1, Spaltenindex 3
print("6a)") 

# 6b) jetzt auf die ganze Zeile 1. 
print("6b)")

# 6c) Spalte 1
print("6c)")

# 6d) ersetze die rechteste Spalte durch 1, 2, 3
#print("6d)\n", matr)


# Breite und Hoehe sind jetzt festgelegt.
# 6e) So koennen wir sie uns geben lassen.

print("6e)", "(Hoehe, Breite) = ", matr.shape)


# 7) Iterieren. Wenn wir jedes Feld besuchen wollen, muessen wir jede Zeile und spalte ablaufen.
anzahl_zeilen = matr.shape[0]
anzahl_spalten = matr.shape[1]

#for zeile in range(anzahl_zeilen) :
#    for spalte in range(anzahl_spalten) :
#        print("Zeile=", zeile, "Spalte=", spalte, "Wert=", matr[zeile, spalte])
#
# 7b) Gib dazu noch aus, ob der Wert durch gerade oder ungerade ist.
print("7b)")

# 7c) Jetzt wollen wir g oder u (fuer gerade/ungerade) ausgeben - Zeilenweise
#print(matr)
print("7c)")


# 8) Machen wir eine neue Tabelle, mit Strings

feld = np.array(
        [["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"]])

#print(feld)

# 8a) Funktion, die uns das ein bisschen huebscher macht.
# so soll das aussehen
#|| - | - | - | - | - ||
#|| - | - | - | - | - ||
#|| - | - | - | - | - ||
#|| - | - | - | - | - ||
#|| - | - | - | - | - ||
#|| - | - | - | - | - ||
#|| - | - | - | - | - ||

def prettyprint(feld) :
    #todo
    print(feld)

#prettyprint(feld)
 



# 9) Listen von Indizes
print("Erinnerung : eine_liste =", eine_liste)


# 9a) Setze die Werte von Index 2, 5, und 6 auf 0
# (wenn hier ein Fehler kommt, wurden die vorherigen Aufgaben nicht bearbeitet)
indexliste = [2, 5, 6]

print("9a)", eine_liste)


# und jetzt zweidimensional!
# 9b) Ersetze - durch x an den gegebenen Positionen
positionen = [(2, 1), (2, 2), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4)]
for (y, x) in positionen :
   pass


print("9b)")
#prettyprint(feld)








