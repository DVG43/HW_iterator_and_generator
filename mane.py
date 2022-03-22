nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]
class FlatIterator:
#
#     def __init__(self, some_list):
#         self.some_list = some_list
#
#     def __iter__(self):
#
#         return self
#
#     def __next__(self):
#        for element in self.some_list:
#            for any_element in element:
#                if isinstance(any_element, str):
#                    print(f"'{any_element}'")
#                else:
#                    print(any_element)
#
#        raise StopIteration




    def __init__(self, some_list):
        self.main_list = some_list

    def __iter__(self):
        self.main_list_cursor = 0  # курсор основного списка
        self.nested_list_cursor = 0  # курсор списка вложенного в основной список
        self.counter = 0
        return self

    def __next__(self):
          if self.counter != 0:
               self.nested_list_cursor += 1 # увеличиваем nested_list_cursor

               if self.nested_list_cursor == len(self.main_list[self.main_list_cursor]): #-1:# если во вложенном списке элементы закончились,

                      self.main_list_cursor += 1     # то переходи на следующий список увеличив main_list_cursor

                      self.nested_list_cursor = 0  # и обнуляем nested_list_cursor

               if self.main_list_cursor == len(self.main_list):
                    raise StopIteration
          self.counter += 1
          return self.main_list[self.main_list_cursor][self.nested_list_cursor]



if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print (item)
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

# 'a'
# 'b'
# 'c'
# 'd'
# 'e'
# 'f'
# 'h'
# False
# 1
# 2
# None