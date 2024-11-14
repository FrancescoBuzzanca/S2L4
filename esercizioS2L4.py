print("il programma calcola il perimetro di alcune figure gemetriche!")
print("premi 1-per quadxrato 2- per cerchio 3- per rettangolo 4- per triangolo: ")


sleta = int(input(">>>"))
scelta = input("inserisi il numero che corrisponde alla figuara: ")
if scelta =="1":
        lato = float(input("inserisci la lunghezza del lato del quadrato: "))
        perimetro = lato * 4
        print(f"il perimetro del quadrato è: {perimetro}")
elif scelta == "2":
        r = float(input("inserisci il valore del raggio"))
        print("il perimetro del cerchio di raggio",r, "è", 2* r* 3.14)
elif scelta == "3":
        base = float(input("inserisci la lunghezza della base: "))
        altezza = float(input("inserisci la lunghezza dell'altezza "))
        perimetro = 2 * (base + altezza)
        print(f"il perimetro del rettangolo è: {perimetro}")
else:
        print("scelta non valida. Riprova")

