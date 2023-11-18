import time
'''В данном коде используется объектно-ориентированная парадигма программирования. Класс Stopwatch определяет 
состояние и поведение объекта секундомера. Класс содержит методы для запуска, паузы, возобновления, остановки и 
получения времени работы секундомера. Код также содержит основной блок, который создает экземпляр класса Stopwatch 
и в цикле предоставляет пользователю возможность управлять секундомером.
'''
class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.pause_time_bool = False
        self.pause_start_time = None
        self.total_pause_time = 0

    def start(self):
        if not self.start_time:
            self.start_time = time.time()
        elif self.pause_time_bool:
            self.total_pause_time += time.time() - self.pause_start_time
            self.pause_time_bool = False

    def pause(self):
        if self.start_time and not self.pause_time_bool:
            self.pause_time_bool = True
            self.pause_start_time = time.time()

    def resume(self):
        if self.pause_time_bool:
            self.pause_time_bool = False
            self.total_pause_time += time.time() - self.pause_start_time

    def stop(self):
        self.start_time = None
        self.pause_time_bool = False
        self.pause_start_time = None
        self.total_pause_time = 0

    def get_time(self):
        if self.start_time:
            if self.pause_start_time:
                return self.pause_start_time - self.start_time - self.total_pause_time

            else: time.time() - self.start_time - self.total_pause_time

    def get_time_format(self):
        time = int(self.get_time())
        min = time // 60
        sec = time % 60
        return f"{min:02}:{sec:02}"


if __name__ == "__main__":
    name = Stopwatch()

    while True:
        print("1-start")
        print("2-pause")
        print("3-continue")
        print("4-stop")
        print("5-exit")

        choice = input("выберите действие ")
        if choice == "1":
            name.start()
        elif choice == "2":
            name.pause()
        elif choice == "3":
            name.resume()
        elif choice == "4":
            name.stop()
        elif choice == "5":
            print("выход из программы")
            break

        total = name.get_time_format()
        print("время", total)


