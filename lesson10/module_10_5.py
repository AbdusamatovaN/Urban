import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            all_data.append(line)

#filenames = [f'./file_{number}.txt' for number in range(1, 5)]
filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == "__main__":
    start = datetime.now()
    for i in filenames:
        read_info(i)
    end = datetime.now()
    print(end - start)

    start = datetime.now()
    with (multiprocessing.Pool() as pool):
        pool.map(read_info, filenames)
    end = datetime.now()
    print(end - start)