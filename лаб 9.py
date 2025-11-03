# 1 задание
# from abc import ABC, abstractmethod

# class Payment(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass

#     @abstractmethod
#     def refund(self, amount):
#         pass


# class CreditCardPayment(Payment):
#     def pay(self, amount):
#         print(f"Оплата {amount} сом с кредитной карты прошла успешно.")

#     def refund(self, amount):
#         print(f"Возврат {amount} сом на кредитную карту выполнен.")


# class CryptoPayment(Payment):
#     def pay(self, amount):
#         print(f"Оплата {amount} сом в криптовалюте (Bitcoin) выполнена.")

#     def refund(self, amount):
#         print(f"Возврат {amount} сом в криптовалюте выполнен.")


# payments = [
#     CreditCardPayment(),
#     CryptoPayment()
# ]

# for method in payments:
#     method.pay(600)
#     method.refund(200)
#     print("-" * 40)


# # 2 задание
# from abc import ABC, abstractmethod

# class Course(ABC):
#     @abstractmethod
#     def start(self):
#         pass

#     @abstractmethod
#     def get_materials(self):
#         pass

#     @abstractmethod
#     def end(self):
#         pass


# class PythonCourse(Course):
#     def start(self):
#         print("Запуск курса по Python! Добро пожаловать!")

#     def get_materials(self):
#         return ["Основы Python", "ООП в Python", "Работа с файлами", "Модули и пакеты"]

#     def end(self):
#         print("Курс по Python завершён. Молодец!")


# class MathCourse(Course):
#     def start(self):
#         print("Начинаем курс по математике! Готовьтесь к формулам.")

#     def get_materials(self):
#         return ["Алгебра", "Геометрия", "Тригонометрия", "Статистика"]

#     def end(self):
#         print("Курс по математике окончен. Отличная работа!")


# python_course = PythonCourse()
# math_course = MathCourse()

# for course in (python_course, math_course):
#     course.start()
#     print("Материалы:", course.get_materials())
#     course.end()
#     print("-" * 30)


# # 3 задание
# class BankAccount:
#     def __init__(self, owner, balance, pin):
#         self.__owner = owner
#         self.__balance = balance
#         self.__pin = pin

#     def deposit(self, amount, pin):
#         if pin == self.__pin:
#             if amount > 0:
#                 self.__balance += amount
#                 print(f"{amount} сом успешно зачислены на счёт.")
#             else:
#                 print("Сумма должна быть положительной.")
#         else:
#             print("Неверный PIN-код!")

#     def withdraw(self, amount, pin):
#         if pin == self.__pin:
#             if amount > 0:
#                 if amount <= self.__balance:
#                     self.__balance -= amount
#                     print(f"{amount} сом успешно сняты со счёта.")
#                 else:
#                     print("Недостаточно средств на счёте.")
#             else:
#                 print("Сумма должна быть положительной.")
#         else:
#             print("Неверный PIN-код!")

#     def change_pin(self, old_pin, new_pin):
#         if old_pin == self.__pin:
#             if len(str(new_pin)) == 4:
#                 self.__pin = new_pin
#                 print("PIN-код успешно изменён.")
#             else:
#                 print("Новый PIN должен состоять из 4 цифр.")
#         else:
#             print("Неверный старый PIN-код!")

#     def check_balance(self, pin):
#         if pin == self.__pin:
#             print(f"Баланс: {self.__balance} сом.")
#         else:
#             print("Неверный PIN-код!")

# # проверка задания
# account = BankAccount("Алина", 1000, 1234)
# account.check_balance(1234)
# account.deposit(500, 1234)
# account.withdraw(300, 1234)
# account.change_pin(1234, 4321)
# account.check_balance(4321)




# # 4 задание
# class UserProfile:
#     def __init__(self, email, password):
#         self.__email = email
#         self.__password = password
#         self._status = "Базовый пользователь"

#     def login(self, email, password):
#         if email == self.__email and password == self.__password:
#             print("Вход выполнен успешно!")
#             return True
#         else:
#             print("Неверная почта или пароль. Доступ запрещён!")
#             return False

#     def upgrade_to_premium(self):
#         self._status = "Премиум пользователь"
#         print("Аккаунт обновлён до Премиум!")

#     def get_info(self):
#         print("Информация о пользователе:")
#         print(f"Email: {self.__email}")
#         print(f"Статус: {self._status}")
        
        
        
# class Product:
#     def __init__(self, name, price):
#         self.name = name              
#         self.price = price             
#         self.__discount = 0            

#     def set_discount(self, discount, is_admin=False):
#         if is_admin:
#             if 0 <= discount <= 100:
#                 self.__discount = discount
#                 print(f"Скидка {discount}% установлена для товара '{self.name}'.")
#             else:
#                 print("Скидка должна быть от 0 до 100%.")
#         else:
#             print("У вас нет прав для установки скидки (только администратор).")

#     def get_price(self):
#         if self.__discount > 0:
#             discounted_price = self.price * (1 - self.__discount / 100)
#             return round(discounted_price, 2)
#         return self.price

#     def info(self):
#         print(f"Товар: {self.name}")
#         print(f"Цена без скидки: {self.price} сом")
#         if self.__discount > 0:
#             print(f"Скидка: {self.__discount}%")
#             print(f"Цена со скидкой: {self.get_price()} сом")
#         else:
#             print("Скидка не установлена.")


# product1 = Product("Телефон", 30000)
# product1.set_discount(10, is_admin=False)
# product1.set_discount(15, is_admin=True)
# product1.info()
# print("Цена с учётом скидки:", product1.get_price(), "сом")



# class File:
#     def __init__(self, name):
#         self.name = name

#     def open(self):
#         pass  


# class TextFile(File):
#     def open(self):
#         print(f"Открываем текстовый файл '{self.name}'. Можно читать текст.")

# class ImageFile(File):
#     def open(self):
#         print(f"Открываем изображение '{self.name}'. Можно просматривать картинку.")

# class AudioFile(File):
#     def open(self):
#         print(f"Открываем аудиофайл '{self.name}'. Можно слушать звук.")

# def open_all(files):
#     for file in files:
#         file.open()  
#         print("-" * 30)  

# file1 = TextFile("notes.txt")
# file2 = ImageFile("photo.jpg")
# file3 = AudioFile("song.mp3")

# files_list = [file1, file2, file3]

# open_all(files_list)



# class Car:
#     def __init__(self, fuel_efficiency=10, speed=60):
#         self.fuel_efficiency = fuel_efficiency
#         self.speed = speed

#     def move(self, distance):
#         time = distance / self.speed
#         fuel_used = distance * self.fuel_efficiency / 100
#         print(f"Автомобиль проедет {distance} км за {time:.2f} часов, расход топлива {fuel_used:.2f} л.")

# car = Car()
# car.move(120)




class Student:
    def access_portal(self):
        print("Студент: может просматривать расписание и свои оценки.")

class Teacher:
    def access_portal(self):
        print("Преподаватель: можно выставлять и редактировать оценки студентов.")

class Administrator:
    def access_portal(self):
        print("Администратор: можно управлять пользователями и настройками документа.")


student1 = Student()
teacher1 = Teacher()
admin1 = Administrator()

users = [student1, teacher1, admin1]

for user in users:
    user.access_portal()
    print("-" * 40)





    
    