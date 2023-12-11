import doctest


class Human:
    def __init__(self, name: str, age: int):
        """
        Создание и подготовка к работе объекта "Человек"

        :param name: Имя человека
        :param age: Возраст человека

        Примеры:
        >>> person = Human("Vadim", 18)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя человека должно быть типа str")
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Возраст человека должен быть целым числом")
        if age < 0:
            raise ValueError("Возраст человека не может быть отрицательным числом")
        if age > 130:
            raise ValueError("Возраст человека не может превышать 130 лет")
        self.age = age

    def have_birthday(self) -> None:
        """
        Празднование дня рождения человека.

        Увеличивает возраст на 1.

        Примеры:
        >>> person = Human("Vadim", 18)
        >>> person.have_birthday()
        """
        ...

    def is_adult(self) -> bool:
        """
        Проверка, является ли человек взрослым.

        :return: True, если человек является взрослым, иначе False

        Примеры:
        >>> person = Human("Vadim", 18)
        >>> person.is_adult()
        """
        ...


class Car:
    def __init__(self, year: int, mileage: float):
        """
        Создание объекта "Автомобиль".

        :param year: Год выпуска автомобиля
        :param mileage: Пробег автомобиля

        Примеры:
        >>> car = Car(2020, 15000.5)  # инициализация экземпляра класса
        """
        if not isinstance(year, int):
            raise TypeError("Год выпуска должен быть целым числом")
        if year < 1886:  # первый автомобиль был выпущен в 1886 году
            raise ValueError("Некорректный год выпуска")
        if year > 2024:  # Год выпуска не может быть из будущего
            raise ValueError("Некорректный год выпуска")
        self.year = year

        if not isinstance(mileage, (int, float)):
            raise TypeError("Пробег должен быть числом")
        if mileage < 0:
            raise ValueError("Пробег не может быть отрицательным числом")
        self.mileage = mileage

    def update_mileage(self, new_mileage: float) -> None:
        """
        Обновление пробега автомобиля.

        :param new_mileage: Новый пробег

        :raise ValueError: Если новый пробег меньше текущего, вызываем ошибку

        Примеры:
        >>> car = Car(2020, 15000.5)
        >>> car.update_mileage(16000.8)
        """
        if new_mileage < self.mileage:
            raise ValueError("Новый пробег не может быть меньше текущего")
        self.mileage = new_mileage

    def get_car_info(self) -> str:
        """
        Получение информации о машине.

        :return: Информация о машине

        Примеры:
        >>> car = Car(2020, 15000.5)
        >>> car.get_car_info()
        """
        ...


class Book:
    def __init__(self, title: str, author: str, year: int):
        """
        Создание объекта "Книга".

        :param title: Название книги
        :param author: Автор книги
        :param year: Год выпуска книги

        Примеры:
        >>> book = Book("Python", "Vadim Gamin", 2023)  # инициализация экземпляра класса
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть типа str")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть типа str")
        self.author = author

        if not isinstance(year, int):
            raise TypeError("Год выпуска должен быть типа int")
        if year < 0:
            raise ValueError("Некорректный год выпуска")
        self.year = year

    def change_author(self, new_author: str) -> None:
        """
        Изменение автора книги.

        :param new_author: Новый автор

        :raise ValueError: Если новый автор не является строкой, вызываем ошибку

        Примеры:
        >>> book = Book("Python", "Vadim Gamin", 2023)
        >>> book.change_author("John Smith")
        """
        if not isinstance(new_author, str):
            raise ValueError("Новый автор книги должен быть типа str")
        self.author = new_author

    def get_book_info(self) -> str:
        """
        Получение информации о книге.

        :return: Информация о книге

        Примеры:
        >>> book = Book("Python Crash Course", "Eric Matthes", 2015)
        >>> book.get_book_info()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
