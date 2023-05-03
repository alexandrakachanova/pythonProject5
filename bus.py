private
public
private

class Bus:
    def __init__(self, brand='no name', price=0, number=0):
        self.__brand = brand # private
        self.__price = price # private
        self.__number = number # private
        # конструктор кот прикрутит соотв поля нашим автобусам

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price > 0:
            self.__price = price

    def get_brand(self):
        return self.__brand

    def set_number(self, number):
        self.__number = number

    def get_number(self):
        return self.__number

    # def __del__(self):
    #     print(f"destructor for {self.brand}")

    def __str__(self): #метод конвертит все содержимое объекта в строку
        return f"Bus: {self.brand}, price = ${self.price}", \
                f"number = {self.number}"

if __name__ == "__main__":
    bus = Bus()
    bus.set_price(12000)
    print(bus.get_price)
    bus.number = -10 #public

