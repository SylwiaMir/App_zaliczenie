from datetime import datetime
import sqlite3
from funkcje import *
from db_sql import *


while True:
	
	main_menu()
	choice = int(input('Twój wybór:'))

	if choice == 1:
		dodaj_wydatek()
			
	elif choice == 2:
		pokaz_wydatki()
		
	elif choice == 3:
		edytuj_wydatki()
		
	elif choice == 4:
		print("opcja4")

	elif choice == 5:
		print("opcja5")
		
	elif choice == 6:
		break
		
	else:
		print("Wybierz ponownie")
