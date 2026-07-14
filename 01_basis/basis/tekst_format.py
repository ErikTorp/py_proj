# Leser inn et tall og kjører et par if setninger.
# Hensikten er å øve på "indent" og "format" av print tekststreng

def format () :
    i = float(input("Skriv beløp kjøpt for: "))
    
    if i > 100.0 :
        rabatt = i * 0.05
        salg = i - rabatt
        print ("Du fikk kr. %.2f i rabatt" % rabatt)
    else :
        diff = 100.0 - i
        if diff < 10.0 :
            print("Kjøp dagens produkt for å få 5% rabatt.")
        else :
            print("Du må kjøpe for kr. %.2f mer for å få rabatt" % diff)
            
format()