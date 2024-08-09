import threading, random, time


class Bank:
    pause = random.random()

    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        for operation in range(10):
            rand_num = random.randint(50, 500)
            self.balance += rand_num
            time.sleep(self.pause)
            print(f'Пополнение: {rand_num}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

    def take(self):
        for rec in range(10):
            rand_om = random.randint(50, 800)
            print(f'Запрос на {rand_om}')
            if rand_om <= self.balance:
                self.balance -= rand_om
                print(f'Снятие: {rand_om}. Баланс: {self.balance}')
                time.sleep(self.pause)
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()
# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
