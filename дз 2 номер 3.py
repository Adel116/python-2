month_number = int(input('введите номер месяца'))
season_list = ['зима','весна','лето','осень']
season_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
if month_number == 1 or month_number == 2 or month_number== 12:
    print(season_dict.get(1))
elif month_number == 3 or month_number == 4 or month_number == 5:
    print(season_dict.get(2))
elif month_number == 6 or month_number == 7 or month_number == 8:
    print(season_dict.get(3))
elif month_number == 9 or month_number == 10 or month_number == 11:
    print(season_dict.get(4))
else:
     print('неправильно ввели значение')