## Programmet regner ut hvor lang tid det tar å doble en investering gitt en rente.

def doble_tid(aar, balanse, RENTE_FOT):
    # Løkke hvor vi regner ut antall år.
    MAAL = balanse * 2
    while balanse < MAAL:
        aar = aar + 1
        rente = balanse * RENTE_FOT / 100
        balanse = balanse + rente
        print("År: ", aar, "Balanse: %.2f" % balanse, "Rente: %.2f" % rente)
    return aar

def main() :

    RENTE_FOT = float(input("Rentefot: "))
    balanse = float(input("Angi sparebeløp: "))

    aar = doble_tid(0, balanse, RENTE_FOT)

    print("Det tar", aar, "år å doble investeringen.")
    
main()