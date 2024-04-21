import csv

# Функция write_holiday_cities принимает первую букву имени ищет в файле travel-notes.csv
# города, посещенные и желаемые к посещению студентами, чьи имена начинаются с заданной буквы.
def write_holiday_cities(first_letter):
    visited_cities = set()   # Множество для хранения посещенных городов
    desired_cities = set()   # Множество для хранения желаемых к посещению городов
    all_cities = set()       # Множество для хранения всех городов

    # Открываем файл travel-notes.csv для чтения данных
    with open('travel-notes.csv', newline='', encoding='utf8') as csvfile:
        reader = csv.reader(csvfile)
        # Читаем данные из каждой строки файла
        for row in reader:
            name, visited, desired = row
            # Если имя студента начинается с заданной буквы, обновляем множества посещенных и желаемых городов
            if name.startswith(first_letter):
                visited_cities.update(visited.split(';'))
                desired_cities.update(desired.split(';'))

    # Объединяем множества посещенных и желаемых городов, чтобы получить все уникальные города
    all_cities.update(visited_cities)
    all_cities.update(desired_cities)

    # Находим города, в которых студенты не были, вычитая из общего множества посещенных городов
    not_visited = all_cities - visited_cities

    # Находим следующий город для посещения (первый в отсортированном списке не посещенных городов)
    next_city = sorted(not_visited)[0]

    # Открываем файл holiday.csv для записи результатов
    with open('holiday.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Записываем результаты в файл: посещенные города, желаемые к посещению города, города, в которых не были и следующий город
        writer.writerow(['Посетили:', ', '.join(sorted(visited_cities))])
        writer.writerow(['Хотят посетить:', ', '.join(sorted(desired_cities))])
        writer.writerow(['Никогда не были в:', ', '.join(sorted(not_visited))])
        writer.writerow(['Следующим городом будет:', next_city])

# Пример использования функции: вызываем функцию для студентов, имена которых начинаются с 'R'
write_holiday_cities('R')
