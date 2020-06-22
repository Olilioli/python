# Задание 5 (Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.)

class Warehouse:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {"Наименование устройства": self.name, "Цена": self.price, "Количество": self.quantity}

    def __str__(self):
        return f'{self.name} Цена {self.price} Количество {self.quantity}'

    @staticmethod
    def reception(self):
        try:
            unit = input(f"Введите наименование: ")
            unit_price = int(input(f"Введите цену: "))
            unit_quantity = int(input(f"Введите количество: "))
            unique = {"Наименование": unit, "Цена": unit_price, "Количество": unit_quantity}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f"Список: \n {self.my_store}")
        except:
            return f"Ошибка ввода!"


class Printer(Warehouse):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(Warehouse):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(Warehouse):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'
