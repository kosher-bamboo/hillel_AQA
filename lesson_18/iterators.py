print('Реалізуйте ітератор для зворотного виведення елементів списку.')
class RevertIterator:
    def __init__(self, last):
        self.last_item = last + 1
        self.first_item = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.last_item > self.first_item:
            self.last_item -= 1
            return self.last_item
        else:
            raise StopIteration


revert = RevertIterator(10)
for num in revert:
    print(num)


print("-"*10)
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
