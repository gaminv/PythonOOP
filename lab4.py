if __name__ == "__main__":
    from abc import ABC, abstractmethod


    class Vehicle(ABC):
        """Базовый класс для транспортных средств."""

        def __init__(self, brand: str, model: str, year: int):
            """Инициализация объекта транспортного средства."""
            self.brand = brand
            self.model = model
            self.year = year

        @abstractmethod
        def drive(self) -> str:
            """Абстрактный метод, представляющий действие вождения транспортного средства."""
            pass

        def __str__(self) -> str:
            """Возвращает строковое представление транспортного средства."""
            return f"{self.year} {self.brand} {self.model}"

        def __repr__(self) -> str:
            """Возвращает строковое представление транспортного средства, подходящее для отладки."""
            return f"{self.__class__.__name__}(brand='{self.brand}', model='{self.model}', year={self.year})"


    class Car(Vehicle):
        """Класс, представляющий автомобиль."""

        def __init__(self, brand: str, model: str, year: int, passengers: int):
            """
            Инициализация объекта автомобиля.

            Args:
                passengers: Количество пассажиров, которое может перевозить автомобиль.
            """
            super().__init__(brand, model, year)
            self.passengers = passengers

        def drive(self) -> str:
            """Вождение автомобиля."""
            return f"{self.brand} {self.model} едет с {self.passengers} пассажирами."

        def park(self) -> str:
            """
            Парковка автомобиля.

            Returns:
                Строка, указывающая, что автомобиль припаркован.
            """
            return f"{self.brand} {self.model} припаркован."

        def __repr__(self) -> str:
            """Возвращает строковое представление автомобиля."""
            return f"{self.__class__.__name__}(brand='{self.brand}', model='{self.model}', year={self.year}, passengers={self.passengers})"


    # Пример использования:
    car1 = Car("Toyota", "Camry", 2022, 5)
    print(car1)
    print(car1.drive())
    print(car1.park())
    print(repr(car1))

    pass
