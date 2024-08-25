"""Задача 1 (двусвязный список) - добавила еще к задаче, которую делали в классе, несколько
функций - вывод количества элементов, добавление и поиск по индексам, поэкспериментировала по видеоурокам)"""

# from typing import Union
#
# class Node:
#     def __init__(self, data, next_node: Union["Node", None] = None, prevent_node: Union["Node", None] = None):
#         self.data = data
#         self.next_node: Union["Node", None] = next_node
#         self.prevent_node: Union["Node", None] = prevent_node
#
#     def __str__(self):
#         return f'{self.data}'
#
#
# class MyList:
#     def __init__(self):
#         self.lenght = 0
#         self.head: Union["Node", None] = None
#         self.tail: Union["Node", None] = None
#
#
#     def __str__(self):
#         result = "["
#         temp_node = self.head
#         while temp_node is not None:
#             result += f' {temp_node.data}'
#             temp_node = temp_node.next_node
#         result += "]"
#         return result
#
#     def add(self, data):
#         new_node = Node(data)
#         self.lenght += 1
#
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#             return
#
#         old_tail = self.tail
#         old_tail.next_node = new_node
#         new_node.prevent_node = old_tail
#         self.tail = new_node
#
#     def add_left(self, data):
#         new_node = Node(data)
#         self.lenght += 1
#
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#             return
#
#         old_head = self.head
#         old_head.prevent_node = new_node
#         new_node.next_node = old_head
#         self.head = new_node
#
#     def delete_data(self, data):
#         if self.head is None:
#             return
#         if self.head.data == data:
#             new_head = self.head.next_node
#             self.head.next_node = None
#             self.head.prevent_node = None
#             self.head = new_head
#             self.lenght -= 1
#         elif self.tail.data == data:
#             new_tail = self.tail.prevent_node
#             new_tail.next_node = None
#             self.tail.prevent_node = None
#             self.tail = new_tail
#             self.lenght -= 1
#         else:
#             temp_node = self.head.next_node
#             while temp_node.data != data:
#                 if temp_node.next_node is None:
#                     temp_node = None
#                     break
#                 temp_node = temp_node.next_node
#
#             if temp_node is not None:
#                 """Логика удаления"""
#                 prev_node: Node = temp_node.prevent_node
#                 next_node: Node = temp_node.next_node
#                 prev_node.next_node = next_node
#                 next_node.prevent_node = prev_node
#                 self.lenght -= 1
#
#     def get_size(self):
#         return f' Количество элементов: {self.lenght}'
#
#     def check_range(self, index: int) -> bool:
#         if index >= self.lenght or index < 0:
#             return False
#         return True
#
#     def insert(self, index: int, data) -> None:
#         new_data = Node(data)
#         ok: bool = self.check_range(index)
#
#         if not ok:
#             raise IndexError("_")
#         if index == 0:
#             self.add_left(new_data)
#             return
#         elif index == self.lenght - 1:
#             self.add(new_data)
#             return
#
#         node = self.head
#         for i in range(0, index):
#             node = node.next_node
#
#         insert_node = Node(data)
#         insert_node.next_node = node
#         node.prevent_node.next_node = insert_node
#         insert_node.prevent_node = node.prevent_node
#         node.prevent_node = insert_node
#         self.lenght += 1
#
#     def get_index(self, index: int):
#         ok: bool = self.check_range(index)
#         if not ok:
#             raise IndexError("_")
#
#         if index == 0:
#             return self.head.data
#         if index == self.lenght -1:
#             return self.tail.data
#
#         node = self.head
#         for i in range(0, index):
#             node = node.next_node
#         return node.data
#
#
# x = MyList()
# x.add(1)
# x.add(4)
# x.add(5)
# x.add(6)
# x.add(7)
# x.add_left(77)
# x.delete_data(77)
# x.delete_data(7)
# x.delete_data(5)
# x.delete_data(4)
# print(x.get_size())
# print(x.check_range(2))
# x.insert(0, 77)
# x.insert(1, 890)
# x.insert(2, 567)
# x.insert(4, 444)
# print(x)
# print(x.get_size())
# print(x.get_index(4))

"""Задача 2 (реализовать стек)"""

# class Stack:
#     def __init__(self):
#         self.stack = []
#         self.max_len_stack = 3
#
#     @classmethod
#     def valid(cls, data: str):
#         if not isinstance(data, str):
#             raise TypeError("Вводить только строки")
#
#     def __str__(self):
#         return f'{self.stack}'
#
#     def append(self, item: str):
#         self.valid(item)
#         if len(self.stack) == self.max_len_stack:
#             print("Стек содержит максимальное количество элементов, нет возможности добавить новый элемент \n")
#         else:
#             self.stack.append(item)
#
#     def pop(self):
#         if len(self.stack) == 0:
#             return None
#         removed = self.stack.pop()
#         return removed
#
#     def lenght(self):
#         return f'Стек содержит: {len(self.stack)} элемента \n'
#
#     def empty(self):
#         if len(self.stack) == 0:
#             print("Стек пустой \n")
#         else:
#             print(f'Стек содержит: {len(self.stack)} элемента \n')
#
#     def full_stack(self):
#         if len(self.stack) == self.max_len_stack:
#             print(f'Стек полный, содержит: {len(self.stack)} элемента \n'
#                   f'Максимальное количество элементов в стеке: {self.max_len_stack} \n')
#         else:
#             print(f'Стек не заполнен, содержит: {len(self.stack)} элемента \n'
#                   f'Максимальное количество элементов в стеке: {self.max_len_stack} \n')
#
#
# stack = Stack()
# while True:
#     print("Меню: \n"
#           "1. Помещение строки в стек; \n"
#           "2. Выталкивание строки из стека; \n"
#           "3. Подсчет количества строк в стеке; \n"
#           "4. Проверку пустой ли стек; \n"
#           "5. Проверку полный ли стек; \n"
#           "6. Выход. \n")
#     value = input("Введите номер операции, которую необходимо выполнить: \n")
#     if value == "1":
#         string = input("Введите строку для добавления: \n")
#         stack.append(string)
#         print(f'Стек: {stack.__str__()}')
#     if value == "2":
#         stack.pop()
#         print("Строка удалена из стека")
#     if value == "3":
#         print(stack.lenght())
#     if value == "4":
#         stack.empty()
#     if value == "5":
#         stack.full_stack()
#     if value == "6":
#         break
