# TODO Найдите количество книг, которое можно разместить на дискете
#Если расписывать :)
information_volume = 1.44 #Информационный объем в Мб
number_of_pages = 100 #Количесвто страниц в книге
numbers_of_lines = 50 #Число строк на странице
numbers_of_characters = 25 #Количество символов в строке
symbol_weight = 4 #Вес символа в Байтах

weight_of_one_book = number_of_pages * numbers_of_lines * numbers_of_characters * symbol_weight #Вес 1 книги в байтах
information_byte = information_volume * 2**20
numbers_of_books = round(information_byte/weight_of_one_book)

print("Количество книг, помещающихся на дискету:", numbers_of_books)
#Или
print("Количество книг, помещающихся на дискету:", round((1.44 * 2**20 / (100 * 50 * 25 * 4))))