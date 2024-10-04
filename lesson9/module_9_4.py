from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'
res = list(map(lambda x, y: x == y, first, second))
print(res)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w') as file:
            for i in data_set:
                file.write(str(i))
                file.write('\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self, *args, **kwargs):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())