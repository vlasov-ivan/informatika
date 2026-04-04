# TODO Напишите функцию find_common_participants
def find_common_participants(s1, s2, symb=','):
    s1 = s1.split(symb)
    s2 = s2.split(symb)
    new = []
    for i in s1:
        if i in s2:
            new.append(i)
    return sorted(new)

participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group))