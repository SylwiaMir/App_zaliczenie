from datetime import datetime
import sqlite3
from funkcje import *


while True:
	
	main_menu()
	while True:
		try:
			choice = int(input('Twój wybór: '))
			break
		except ValueError:
			print('Wybrano błędną wartość. Wybierz ponownie. ')
			continue

	if choice == 1:
		dodaj_wydatek()
			
	elif choice == 2:
		pokaz_wydatki()
		
	elif choice == 3:
		edytuj_wydatki()
		
	elif choice == 4:
		print("opcja4 - tu ma powstac rozne sortowanie")

	elif choice == 5:
		zaktualizuj_wydatki()
		
	elif choice == 6:
		break
		
	else:
		print("Wybrano błędną wartość. Wybierz ponownie. ")
