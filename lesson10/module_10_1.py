from threading import Thread
from time import sleep
from datetime import datetime


def write_words(word_count, file_name):
    file = open(file_name, "a", encoding='utf-8')
    for i in range(1, word_count + 1):
        file.write(f"Какое-то слово № {i}\n")
        sleep(0.1)
    file.close()
    print(f"Завершилась запись в файл {file_name}")

now_1 = datetime.now()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
end_1 = datetime.now()
print(f"Работа потоков {end_1 - now_1}")

now_2 = datetime.now()
thr_1 = Thread(write_words(10, "example5.txt"))
thr_2 = Thread(write_words(30, "example6.txt"))
thr_3 = Thread(write_words(200, "example7.txt"))
thr_4 = Thread(write_words(100, "example8.txt"))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()

end_2 = datetime.now()
print(f"Работа потоков {end_2 - now_2}")
