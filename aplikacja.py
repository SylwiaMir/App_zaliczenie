import tkinter as tk
from class_BazaDanych import *


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
		print("""Sortowanie według:
[1] - miesiąca
[2] - zakresu dat""")
		while True:
			try:
				choice = int(input('Twój wybór: '))
				break
			except ValueError:
				print('Wybrano błędną wartość. Wybierz ponownie. ')
				continue
		if choice == 1:
			sortuj_wg_miesiaca_menu()
		elif choice == 2:
			sortuj_wg_zakresu_dat_menu()
		else:
			print("Wybrano błędną wartość. Wybierz ponownie. ")

	elif choice == 5:
		print("""Suma według:
[1] - miesiąca
[2] - zakresu dat""")
		while True:
			try:
				choice = int(input('Twój wybór: '))
				break
			except ValueError:
				print('Wybrano błędną wartość. Wybierz ponownie. ')
				continue
		if choice == 1:
			suma_z_miesiaca_menu()
		elif choice == 2:
			suma_z_zakresu_menu()
		else:
			print("Wybrano błędną wartość. Wybierz ponownie. ")

	elif choice == 6:
		break
		
	else:
		print("Wybrano błędną wartość. Wybierz ponownie. ")
