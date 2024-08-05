print('Реалізуйте ітератор для зворотного виведення елементів списку.')


class RevertIterator:
    def __init__(self, list):
        self.reverce_list = list[::-1]
        self.last_item = len(self.reverce_list) - 1
        self.first_item = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.first_item > self.last_item:
            raise StopIteration
        else:
            self.first_item += 1
            return self.reverce_list[self.first_item - 1]


list_of_items = ['1', '2', 3, 4, 5, None, 'asd']
revert = RevertIterator(list_of_items)
for num in revert:
    print(num)

print("-" * 10)
print('Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.')


class EvenNumberIterator:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current_item = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current_item < self.max_num:
            self.current_item += 1
            if self.current_item % 2 == 0:
                return self.current_item
        raise StopIteration


my_iterator_2 = EvenNumberIterator(20)
for num in my_iterator_2:
    print(num)
