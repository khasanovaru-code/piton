class Animal:
    def __init__(self, name, color, habitat, is_venomous):
        self.name = name
        self.color = color
        self.habitat = habitat
        self.is_venomous = is_venomous

    def __str__(self):
        return f'Название: {self.name}\nЦвет: {self.color}\nСреда обитания: {self.habitat}\nЯдовитое: {self.is_venomous}'


class Mammal(Animal):
    def __init__(self, name, color, habitat, feeds_milk):
        super().__init__(name, color, habitat, False)
        self.feeds_milk = feeds_milk

    def sound(self):
        return f"{self.name} издаёт звуки и кормит детёнышей молоком: {self.feeds_milk}"


class Reptile(Animal):
    def __init__(self, name, color, habitat, is_venomous):
        super().__init__(name, color, habitat, is_venomous)

    def move(self):
        return f"{self.name} ползает. Ядовитое: {self.is_venomous}"

print("данные млекопитающего:")
name1 = input("Название: ")
color1 = input("Цвет: ")
habitat1 = input("Среда обитания: ")
feeds_milk1 = input("Кормит детёнышей молоком? (да/нет): ").lower() == "да"

tiger = Mammal(name1, color1, habitat1, feeds_milk1)

print("\n данные пресмыкающего:")
name2 = input("Название: ")
color2 = input("Цвет: ")
habitat2 = input("Среда обитания: ")
is_venomous2 = input("Ядовитое? (да/нет): ").lower() == "да"

snake = Reptile(name2, color2, habitat2, is_venomous2)

print("\nИнфо животных:\n")
print(tiger)
print(tiger.sound())
print(snake)
print(snake.move())
