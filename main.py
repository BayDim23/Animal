#1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.
#2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`,
# и `Reptile`, которые наследуют от класса `Animal`. Добавьте специфические атрибуты
# и переопределите методы, если требуется (например, различный звук для `make_sound()`).
#3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
#4. Используйте композицию для создания класса `Zoo`,
# который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
#5. Создайте классы для сотрудников, например, `ZooKeeper`, `
# Veterinarian`, которые могут иметь специфические методы (например, `feed_animal()`
# для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

class Animal():
    def __init__(self, kind_of_animal, name, color):
        self.kind_of_animal = kind_of_animal
        self.name = name
        self.color = color


    def make_sound(self):
        pass

    def favorite_food(self):
        pass

    def eat(self):
        print(f"{self.name} ест")
    def sleep(self):
        print(f"{self.name} спит")

    def walk(self):
        print(f"{self.name} гуляет")

    def info(self):
        print(f"{self.kind_of_animal} - вид животного")
        print(f"{self.name} - имя животного")
        print(f"{self.color} - цвет животного")

class Bird(Animal):

    def favorite_food(self):
        print(f"{self.name} любит есть яйца")

    def make_sound(self):
        print(f"{self.name} - АААААррр")

class Mammal(Animal):

    def make_sound(self):
        print(f"{self.name} - Мяу")

#animal2 = Mammal("Кошачий", "Мурзик", "Серый")

class Reptile(Animal):

    def make_sound(self):
        print(f"{self.name} - Shhhh")

#animal3 = Reptile("Ящер", "Игорь", "зеленый")

mammal = Mammal("Кошачий", "Мурзик", "Серый")
bird = Bird("Птица", "Кеша", "Синий")
reptile = Reptile("Ящер", "Игорь", "зеленый")

#mammal.make_sound()
#bird.make_sound()
#reptile.make_sound()

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")


class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def all_sound(self):
        for animal in self.animals:
            print(animal.make_sound())

zoo = Zoo()

zoo.add_animal(mammal)
zoo.add_animal(bird)
zoo.add_animal(reptile)

employee = Employee("Игорь","Ветеринар")
zoo.add_employee(employee)

employee2 = Employee("Александр","Смотритель")
zoo.add_employee(employee2)

employee.heal_animal(mammal)
employee2.feed_animal(bird)



zoo.all_sound()
bird.favorite_food()

