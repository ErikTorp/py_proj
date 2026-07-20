# Enkelt program med bruk av for løkke
# Viser veksten i en investering over 10 år

from ast import main


def lokke(ant_aar, rente_fot, balanse) :
    
    for i in range(1, ant_aar + 1) :
        okning = balanse * rente_fot / 100
        balanse = balanse + okning
        print("%4d %10.2f" % (i, balanse))
        
def main() :
    ant_aar = int(input("Hvor mange år skal vi regne for? "))
    rente_fot = float(input("Hva er rentefoten? "))
    balanse = float(input("Hva er startbalansen? "))
    
    lokke(ant_aar, rente_fot, balanse)
    
    
    
main()  
