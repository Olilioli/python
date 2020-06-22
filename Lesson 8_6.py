# Задание 6 (Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.)

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

    # @staticmethod
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

        print(f"Ввод - Enter / Выход - Q")
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f"Весь склад -\n {self.my_store_full}")
            return f"Выход"
        else:
            return Warehouse.reception(self)


class Printer(Warehouse):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(Warehouse):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(Warehouse):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


unit_1 = Printer("HP", 10, 20, 30)
unit_2 = Scanner("Brother", 30, 40, 50)
unit_3 = Copier("XEROX", 50, 60, 70)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_2.to_scan())
print(unit_3.to_copier())
