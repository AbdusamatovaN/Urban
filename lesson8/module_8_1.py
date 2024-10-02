def add_everything_up(a, b):
    res = 0
    try:
        res = a + b
    except TypeError:
        return str(a) + str(b)
    else:
        return res


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))