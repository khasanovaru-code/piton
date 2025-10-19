class Account:
    def __init__(self, account_number, balance, pin):   
        self.__account_number = account_number
        self.__balance = balance
        self.__pin = pin

    def deposit(self, amount, pin):
        if pin == self.__pin:
            if amount > 0:
                self.__balance += amount
                print(f"Счет пополнен на {amount}")
            else:
                print("Сумма должна быть положительной")
        else:
            print("Неверный PIN")

    def withdraw(self, amount, pin):
        if pin == self.__pin:
            if 0 < amount <= self.__balance:
                self.__balance -= amount
                print(f"Снято со счета {amount}")
            else:
                print("Недостаточно средств или некорректная сумма")
        else:
            print("Неверный PIN")

    def get_balance(self, pin):
        if pin == self.__pin:
            print(f'Баланс: {self.__balance}')
            return self.__balance
        else:
            print("Неверный PIN")
            return None
        
acc = Account('6000', 2000, 45678) 

acc.deposit(2000, 45678)  

acc.withdraw(200, 45678) 

acc.get_balance(45678) 




class Product:
    def __init__(self, name, price):
        self.name = name                  
        self.__price = price              
    def set_discount(self, percent):
        if percent < 0:
            print("Скидка не может быть отрицательной.")
            return
        discount_amount = self.__price * (percent / 100)
        new_price = self.__price - discount_amount
        if new_price < 0:
            self.__price = 0
        else:
            self.__price = new_price
        print(f"Для {self.name} применена скидка {percent}%. Новая цена: {self.__price}")

    def final_price(self):
        return self.__price
product1 = Product("Телефон", 13500)
product2 = Product("Книга", 870)
product3 = Product("Чашка", 230)
product4 = Product("Лампа", 950)

product1.set_discount(30)   
product2.set_discount(80)   
product3.set_discount(60)   
product4.set_discount(50)  

print("Финальная цена на телефон:", product1.final_price())
print("Финальная цена на книгу:", product2.final_price())
print("Финальная цена на чашку:", product3.final_price())
print("Финальная цена на лампу:", product4.final_price())


class Course:
    def __init__(self, name, max_seats):
        self.__name = name              
        self.__students = []           
        self.__max_seats = max_seats    

    def add_student(self, name):
        if len(self.__students) < self.__max_seats:
            self.__students.append(name)
            print(f"{name} добавлен в курс.")
        else:
            print("Нет свободных мест!")

    def remove_student(self, name):
        if name in self.__students:
            self.__students.remove(name)
            print(f"{name} удалён из курса.")
        else:
            print(f"{name} нет в списке курса.")

    def get_students(self):
        return self.__students.copy()

my_course = Course("Программирование на Python", 2)

my_course.add_student("Василий")
my_course.add_student("Милана")
my_course.add_student("Нурс")   

print("Студенты курса:", my_course.get_students())

my_course.remove_student("Камилла")
my_course.remove_student("Алтынай")  

print("Обновленный список:", my_course.get_students())


class SmartWatch:
    def __init__(self, battery):
        self.__battery = battery    
    def use(self, minutes):
        used_percent = minutes // 10
        if used_percent > self.__battery:
            used_percent = self.__battery 
        self.__battery -= used_percent
        print(f"Использовано {minutes} минут. Заряд уменьшился на {used_percent}%. Осталось: {self.__battery}%.")

    def charge(self, percent):
        if percent < 0:
            print("Нельзя добавить отрицательный заряд.")
            return
        self.__battery += percent
        if self.__battery > 100:
            self.__battery = 100
        print(f"Заряд увеличен на {percent}%. Теперь: {self.__battery}%.")

    def get_battery(self):
        print(f"Текущий заряд: {self.__battery}%")
        return self.__battery


watch = SmartWatch(100)      

watch.use(35)                
watch.charge(40)             
watch.use(160)              
watch.charge(-20)            

watch.get_battery()

class Transport:
    def __init__(self, speed, capacity):
        self.speed = speed          
        self.capacity = capacity    

    def travel_time(self, distance):
        time = distance / self.speed
        print(f"Поездка на {type(self).__name__}: {time:.2f} часов")
        return time

class Bus(Transport):
    pass    

class Train(Transport):
    pass    

class Airplane(Transport):
    def travel_time(self, distance):
        time = super().travel_time(distance) 
        air_time = time * 0.8                 
        print(f"Поездка на Airplane с учётом ускорения: {air_time:.2f} часов")
        return air_time
    
bus = Bus(speed=40, capacity=50)        
train = Train(speed=100, capacity=300)  
plane = Airplane(speed=600, capacity=200) 

distance = 600  

bus.travel_time(distance)    
train.travel_time(distance)  
plane.travel_time(distance)



class Order:
    def __init__(self, amount):
        self.amount = amount  
    def calculate_total(self):
        return self.amount    

class DineInOrder(Order):
    def calculate_total(self):
        total = self.amount * 1.10
        print(f"Дозаказ в ресторане: {total:.2f} (включая 10% чаевых)")
        return total

class TakeAwayOrder(Order):
    def calculate_total(self):
        total = self.amount * 0.95
        print(f"Заказ навынос: {total:.2f} (включая 5% скидку)")
        return total

class DeliveryOrder(Order):
    def calculate_total(self):
        total = self.amount * 1.10
        print(f"Доставка: {total:.2f} (включая 10% за доставку)")
        return total

dine_in = DineInOrder(1200)      
take_away = TakeAwayOrder(750)   
delivery = DeliveryOrder(1000)   

dine_in.calculate_total()  
take_away.calculate_total()
delivery.calculate_total()  

class Character:
    def __init__(self, name, health, attack):
        self.name = name         
        self.health = health      
        self.attack = attack      
    def attack_method(self):
        pass   
class Warrior(Character):
    def attack_method(self):
        print(f"{self.name} брызгает яд {self.attack} -1умер!")

class Mage(Character):
    def attack_method(self):
        print(f"{self.name} создает ураган {self.attack} почти смерть!")

class Archer(Character):
    def attack_method(self):
        print(f"{self.name} создает гигантов {self.attack} умрешь не умрешь!")

# Примеры персонажей
w = Warrior("Баба Яга", 120, 30)
m = Mage("Кикимора", 80, 50)
a = Archer("Шамаханская царица", 100, 40)

w.attack_method() 
m.attack_method()  
a.attack_method() 

from abc import ABC, abstractmethod
class MediaFile(ABC):
    def __init__(self, title, duration):
        self.title = title
        self.__duration = duration 

    @property
    def duration(self):
        return self.__duration

    @abstractmethod
    def play(self):
        pass
class AudioFile(MediaFile):
    def play(self):
        print(f"Воспроизводится аудиофайл: {self.title} ({self.duration} мин)")

class VideoFile(MediaFile):
    def play(self):
        print(f"Воспроизводится с изображением: {self.title} ({self.duration} мин)")

class Podcast(MediaFile):
    def play(self):
        print(f"Воспроизводится эпизод подкаста: {self.title} ({self.duration} мин)")

media_files = [
    AudioFile("Любимая песня", 2),
    VideoFile("Увлекательный фильм", 90),
    Podcast("Научный подкаст", 50),
    ]
for file in media_files:
    file.play()
    
    
    from abc import ABC, abstractmethod
class PaymentSystem(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentSystem):
    def process_payment(self, amount):
        print(f"Оплата {amount} сом. с кредитной карты проведена успешно")

class CryptoPayment(PaymentSystem):
    def process_payment(self, amount):
        print(f"Переведено {amount} в криптовалюте $")


class BankTransfer(PaymentSystem):
    def process_payment(self, amount):
        print(f"Банковский перевод на сумму {amount} сом. выполнен")

payments = [
    CreditCardPayment(),
    CryptoPayment(),
    BankTransfer()
]

amounts = [1000, 50.0, 35000]  

for p, a in zip(payments, amounts):
    p.process_payment(a)


from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

class Lion(Animal):
    def eat(self):
        print("Лев ловит и ест мясо")
    def sleep(self):
        print("Лев спит в тени")

class Elephant(Animal):
    def eat(self):
        print("Слон ест листья и траву")
    def sleep(self):
        print("Слон спит стоя")

class Snake(Animal):
    def eat(self):
        print("Змея проглатывает добычу целиком")
    def sleep(self):
        print("Змея сворачивается в кольцо и спит")

animals = [
    Lion(),
    Elephant(),
    Snake()
]

for animal in animals:
    animal.eat()
    animal.sleep()
    
    from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def save(self):
        pass

class WordDocument(Document):
    def open(self):
        print("Word-документ открыт")
    def edit(self):
        print("Word-документ: редактирование невозможно")
    def save(self):
        print("Word-документ сохранён")

class PdfDocument(Document):
    def open(self):
        print("PDF-документ открыт")
    def edit(self):
        print("PDF-документ: редактирование невозможно")
    def save(self):
        print("PDF-документ сохранён")

class SpreadsheetDocument(Document):
    def open(self):
        print("Таблица Excel открыта")
    def edit(self):
        print("Таблица Excel редактируется")
    def save(self):
        print("Таблица Excel сохранена")

documents = [
    WordDocument(),
    PdfDocument(),
    SpreadsheetDocument()
]

for doc in documents:
    doc.open()
    doc.edit()
    doc.save()
    
    from abc import ABC, abstractmethod

class Lesson(ABC):
    @abstractmethod
    def start(self):
        pass

class VideoLesson(Lesson):
    def start(self):
        print("Видеоурок начинается. Включите видео.")

class QuizLesson(Lesson):
    def start(self):
        print("Тест начался. Ответьте на вопросы.")

class TextLesson(Lesson):
    def start(self):
        print("Практическая часть урока начинается. Читайте внимательно.")

lessons = [
    VideoLesson(),
    QuizLesson(),
    TextLesson()
]

for lesson in lessons:
    lesson.start()
    
    from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print(f"Отправка письма: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"Отправка SMS: {message}")

class PushNotification(Notification):
    def send(self, message):
        print(f"Push-уведомление: {message}")

notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for n in notifications:
    n.send("Ваша отправка одобрена!")
    
    class Square:
     def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

shapes = [
    Square(5),
    Circle(3),
    Triangle(3, 4, 5)
]

for shape in shapes:
    print("Периметр:", shape.perimeter())
    
    from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def work(self):
        pass

class Manager(Employee):
    def work(self):
        print("Менеджер организует работу команды")

class Developer(Employee):
    def work(self):
        print("Разработчик пишет код")

class Designer(Employee):
    def work(self):
        print("Дизайнер создает дизайн-проекты")

employees = [
    Manager(),
    Developer(),
    Designer()
]


for emp in employees:
    emp.work()
from abc import ABC, abstractmethod

class Spell(ABC):
    @abstractmethod
    def cast(self, target):
        pass

class FireSpell(Spell):
    def cast(self, target):
        print(f"{target}: наносит урон с помощью посоха!")

class IceSpell(Spell):
    def cast(self, target):
        print(f"{target}: замораживает!")

class HealingSpell(Spell):
    def cast(self, target):
        print(f"{target}: благодаря ему живешь!")

spells = [
    FireSpell(),
    IceSpell(),
    HealingSpell()
]

for spell in spells:
    spell.cast("Герой")
    
    
    