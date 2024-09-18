res = 0

def calculate_structure_sum(data):
    global res
    if isinstance(data, list):
        for i in data:
            calculate_structure_sum(i)
    elif isinstance(data, tuple):
        for i in data:
            calculate_structure_sum(i)
    elif isinstance(data, set):
        for i in data:
            calculate_structure_sum(i)
    elif isinstance(data, dict):
        for i, j in data.items():
            d = (i, j)
            calculate_structure_sum(d)
    elif isinstance(data, int):
        res += data
    elif isinstance(data, str):
        res += len(data)
    return res


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
