from time import sleep
from datetime import datetime
from threading import Thread


start_time = datetime.now()


def write_words(word_count, file_name):
    for ww in range(word_count):
        with open(file_name, 'a', encoding='UTF-8') as file:
            file.write(f'Какое-то слово № {ww +1}\n')
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


write_words(10, 'exs1')
write_words(30, 'exs2')
write_words(200, 'exs3')
write_words(100, 'exs4')

end_time = datetime.now()
time_res = end_time - start_time
print(time_res)

start_time1 = datetime.now()

a = 10, 'example5.txt'
b = 30, 'example6.txt'
c = 200, 'example3.txt'
d = 100, 'example4.txt'

thr_first = Thread(target=write_words, args=a)
thr_second = Thread(target=write_words, args=b)
thr_third = Thread(target=write_words, args=c)
thr_fourth = Thread(target=write_words, args=d)

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

end_time1 = datetime.now()
time_res1 = end_time1 - start_time1
print(time_res1)
print()
print(f'Быстрее на {time_res - time_res1}')

