# Задание 4 (Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.)

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} поехал"

    def stop(self):
        return f"{self.name} затормозил"

    def turn_left(self):
        return f"{self.name} поворачивает налево"

    def turn_right(self):
        return f"{self.name} поворачивает направо"

    def show_speed(self):
        return f"Скорость {self.name} составляет {self.speed}"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Скорость городской лошадки {self.name} составляет {self.speed}")

        if self.speed > 40:
            return f"Скорость {self.name} стремится к штрафу"
        else:
            return f"Сокрость {self.name} не превышена"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Скорость рабочей лошадки {self.name} составляет {self.speed}")

        if self.speed > 60:
            return f"Скорость {self.name} превышена!"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f"{self.name} доблестная полиция"
        else:
            return f"{self.name} ниразу не полиция"


lamborghini = SportCar(113, "Yellow", "Lamborghini", False)
hyundai = TownCar(61, "Black", "Hyundai", False)
lada = WorkCar(41, "Red", "Lada", True)
vaz = PoliceCar(80, "Red", "Vaz", True)
print(f"Когда {hyundai.turn_right()}, {lamborghini.stop()}")
print(lamborghini.turn_left())
print(f"{lada.name} цвета {lada.color}")
print(f"{lada.name}  полицаи? {lada.is_police}")
print(lamborghini.show_speed())
print(hyundai.show_speed())
print(vaz.police())
print(vaz.show_speed())
