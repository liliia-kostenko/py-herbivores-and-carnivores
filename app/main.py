class Animal:
    alive = []  # Глобальний список живих тварин для всіх екземплярів.

    def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)  # Додаємо тварину до списку живих.

    def check_death(self):
        if self.health <= 0:
            print(f"{self.name} has died.")
            self.remove_from_alive()

    @classmethod
    def remove_from_alive(cls, instance):
        """
        Видаляє екземпляр тварини зі списку живих.
        :param instance: Екземпляр тварини для видалення.
        """
        if instance in cls.alive:
            cls.alive.remove(instance)

    @classmethod
    def show_alive(cls):
        """
        Повертає список живих тварин у форматованому вигляді.
        """
        return [f"{animal.name} (Health: {animal.health}, Hidden: {animal.hidden})" for animal in cls.alive]

    def __repr__(self):
        return f"{self.__class__.__name__}(Name: {self.name}, Health: {self.health}, Hidden: {self.hidden})"


    def check_death(self) -> None:
        """
        Перевіряємо, чи здорова тварина.
        Якщо здоров'я = 0, то видаляємо її з Animal.alive.
        """
        if self.health <= 0:
            Animal.alive.remove(self)


# Створюємо клас Herbivore, який наслідується від Animal.
class Herbivore(Animal):
    def hide(self) -> None:
        """
        Метод для зміни статусу "hidden".
        Використовується для того, щоб травоїдні ховалися.
        """
        self.hidden = not self.hidden  # Перемикаємо значення між True і False.


# Створюємо клас Carnivore, який наслідується від Animal.
class Carnivore(Animal):
    def bite(self, herbivore: Animal) -> None:
        """
        Метод "bite" дозволяє хижакові нападати на травоїдну тварину.
        :param herbivore: Об'єкт травоїдної тварини, на яку нападає хижак.
        """
        # Перевіряємо, чи травоїдна тварина не ховається та чи це не хижак.
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            # Зменшуємо здоров'я травоїдної на 50 одиниць.
            herbivore.health -= 50
            # Перевіряємо, чи травоїдна тварина ще жива.
            herbivore.check_death()
