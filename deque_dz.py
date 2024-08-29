from collections import deque

class Mydeque():
    def __init__(self):
        self.deque = deque()

    def __str__(self):
        return self.deque.__str__()

    def add(self, data):
        if data in self.deque:
            print("Элемент уже существует")
        else:
            self.deque.append(data)
            print("Элемент добавлен")

    def delete_data(self, data):
        while data in self.deque:
            self.deque.remove(data)

    def reverse_str(self):
        x = self.deque.copy()
        x.reverse()
        print(x)

    def search_data(self, data):
        if data in self.deque:
            print(f'Значение в списке есть, число повторений {self.deque.count(data)}')
        else:
            print("Значение в списке отсутствует")

    def first_replace(self, data, value):
        if data in self.deque:
            old_data = self.deque.index(data)
            self.deque.remove(data)
            self.deque.insert(old_data, value)
            return self.deque
        

    def all_replace(self, data, value):
        while data in self.deque:
            old_data = self.deque.index(data)
            self.deque.remove(data)
            self.deque.insert(old_data, value)
        return self.deque


my_deque = Mydeque()
my_deque.deque.extend([4, 3, 5, 4, 78, 4, 3])

"""Не поняла немного, как вставить эти функции в свой код(
Саму функцию поняла, что в классе объяснял, не получилось вставить в код, который написала
Принты скорректировала, что говорил"""

# def get_user_num() -> int:
#     while True:
#         num = input("num: ")
#         if num.isdigit():
#             return int(num)
#
# def search_lst(lst: deque):
#     num = get_user_num()
#
#     while num > 0:
#         num -= 1
#         lst.append(get_user_num())

while True:
    print("Меню: \n"
              "1. Добавить новое число в список; \n"
              "2. Удалить все вхождения числа из списка; \n"
              "3. Показать содержимое списка; \n"
              "4. Проверить есть ли значение в списке; \n"
              "5. Заменить значение в списке; \n"
              "6. Выход. \n")
    input_polz = input("Введите номер пункта, который необходимо выполнить: \n")
    if input_polz == "1":
        data = int(input("Введите число, которое необходимо добавить: \n"))
        my_deque.add(data)
        print(my_deque)
    if input_polz == "2":
        data = int(input("Введите число, которое необходимо удалить: \n"))
        my_deque.delete_data(data)
        print(my_deque)

    if input_polz == "3":
        data = input("Введите 1, если список необходимо показать сначала \n"
                         "Введите 2, если список необходимо показать с конца \n")
        if data == "1":
            print(my_deque)
        elif data == "2":
            my_deque.reverse_str()

    if input_polz == "4":
        data = int(input("Введите значение для поиска: \n"))
        my_deque.search_data(data)

    if input_polz == "5":
        old_data = int(input("Введите значение, которое хотите заменить \n"))
        new_data = int(input("Введите новое значение \n"))
        vibor = input("Введите 1, если необходимо заменить только первое вхождение \n"
                      "Введите 2, если необходимо заменить все вхождения \n")
        if vibor == "1":
            my_deque.first_replace(old_data, new_data)
        if vibor == "2":
            my_deque.all_replace(old_data, new_data)

    if input_polz == "6":
        break

