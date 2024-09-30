def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, "w", encoding='utf-8')
    for i, s in enumerate(strings):
        strings_positions[(i+1, file.tell())] = s
        file.write(s)
        file.write('\n')
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)