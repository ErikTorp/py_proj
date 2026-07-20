# Skriver ut den høyeste verdien i en liste. 
# Ber brukeren om å angi verdier, og stopper når brukeren skriver inn 0.

def finn_hoyeste():
    
    ferdig = False
    max = 0
    
    while not ferdig :
        neste = float(input("Gi neste tall. Avslutt med 0: "))
        if neste == 0 :
            ferdig = True
        if neste > max :
            max = neste
    return max

def main():

    hoyeste = finn_hoyeste()
    
    print("Største tallet er: " + str(hoyeste))
    
main()