
def f(items, itm): #функция проверяет нахождения проудкта и выдает либо индекс, либо None
    if itm in items:
        return items_list.index(itm)
    else:
        return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан'] #список продуктов

for find_item in ['банан', 'груша', 'персик']: #проверяет нахождение продукта в списке возвращает продукт и индекс
    index_item = f(items_list, find_item)   # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
