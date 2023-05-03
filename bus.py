private
public
private

class Bus:
    def __init__(self, brand='no name', price=0, number=0):
        self.__brand = brand # private
        self.__price = price # private
        self.__number = number # private
        # конструктор кот прикрутит соотв поля нашим автобусам

    # def __del__(self):
    #     print(f"destructor for {self.brand}")

    def __str__(self): #метод конвертит все содержимое объекта в строку
        return f"Bus: {self.brand}, price = ${self.price}", \
                f"number = {self.number}"

if __name__ == "__main__":
    bus = Bus()
    bus.number = -10 #public

