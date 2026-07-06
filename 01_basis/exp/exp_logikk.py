# Enkel logikk for exception håndtering.
# Har en funksjon som tar inn en verdi og sjekker om den er gyldig. Hvis ikke, kaster den en exception.
def sjekk_gyldig_verdi(verdi):
    try:
        
        if verdi < 0:
            raise ValueError("Verdien kan ikke være negativ.")
        elif verdi > 100:
            raise ValueError("Verdien kan ikke være større enn 100.")
        else:
            return True 
        
    except ValueError as e:
        print(f"Feil: {e}") 
        
sjekk_gyldig_verdi(-5)  # Dette vil kaste en exception og skrive ut feilmeldingen.s 

