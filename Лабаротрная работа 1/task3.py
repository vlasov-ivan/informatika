players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# Находим индекс середины
middle_index = len(players) // 2

# Произвоим слайсирование по индексу середины
first_team = players[:middle_index]
second_team = players[middle_index:]

#Выводим команды
print(first_team)
print(second_team)
