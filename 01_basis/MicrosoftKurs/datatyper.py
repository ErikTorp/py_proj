# Matte med nummer
n1 = 6
n2 = 2

print(n1 + n2)
# Huske ** Eksponent
print (n1 ** n2)



# Type convertering
print (str(n1) + ' antall')
# Andre konverteringer
# int float

# Input
s1 = input("Skriv inn et tall: ")

# Togle kommentar ctrl+'

# Datatype dato
# Datetime bibliotek
from datetime import datetime, timedelta

current_date = datetime.now()
print ("Dagens dato: " + str(current_date))

# Mange funksjoner for å arbeide med datoer
en_dag = timedelta(days=1)
i_går = current_date - en_dag
print ("I går var: " + str(i_går))
# For å få datoen i et annet format
print ("I går var: " + i_går.strftime("%d.%m.%Y"))

bursdag = input("Når har du bursdag (dd.mm.yyyy):")
print("Bursdagen din er: " + str(datetime.strptime(bursdag, "%d.%m.%Y")))
# Eller eksplisitt
# print ("Dato i går: " + str(i_går.day))



