dict_miesiac = {'01':'styczeń', '02':'luty', '03':'marzec', '04':'kwiecień', '05':'maj', '06':'czerwiec','07':'lipiec', '08':'sierpień', '09':'wrzesień', '10':'październik', '11':'listopad', '12':'grudzień'}
def get_nazwa_miesiaca(miesiac):
    return dict_miesiac.get(str(f'{miesiac:02d}'), "Nieznany miesiąc")

def main_menu():
    print("""Opcje:
[1] - Dodaj wydatek
[2] - Wyświetl wydatki
[3] - Edytuj wydatki
[4] - Sortowanie
[5] - Suma wydatków
[6] - Wyjście""")