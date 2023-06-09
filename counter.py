class Counter:
    def __init__(self, count=0):
        if count >= 0:
            self.__count = count
        else:
            self.__count = 0

    @propery # декоратор
    def count(self):
        return self.__count

    # использование свойства вместо метода
   # свойство реализуется как метод а обращение к нему происходит как к полю

    def increment(self):
        self.__count += 1

    def decrement(self):
        if self.__count != 0:
            self.__count -= 1

    def reset(self):
        self.__count = 0

    def __str__(self):   # метод вызывается автоматом там где нужен строковый эквивалент
        return "Counter:" + str(self.__count)

