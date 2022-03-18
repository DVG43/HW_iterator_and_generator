nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]
class FlatIterator:

    def __init__(self, some_list):
        self.some_list = some_list

    def __iter__(self):

        return self

    def __next__(self):
       for element in self.some_list:
           for any_element in element:
               if isinstance(any_element, str):
                   print(f"'{any_element}'")
               else:
                   print(any_element)

       raise StopIteration


if __name__ == '__main__':
    for item in FlatIterator(nested_list):
       pass
        #print (item)


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