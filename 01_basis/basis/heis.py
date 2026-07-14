# Enkelt program som tar inn en verdi og skriver ut etasjenummeret. 
# Heisen går ikke til 13 etasjen. 

def etasje ():

    panel_etasje = int(input("Angi etasje: "))

    if panel_etasje >= 13 :
        til_etasje = panel_etasje - 1
    else :
        til_etasje = panel_etasje
        
    # Skriver resultatet
    print("Heisen vil gå til: ", til_etasje)
    
etasje()
    

