1 Создаём абстрактный класс Payment
# @abstractmethod
#     def pay(self, amount):
#         pass
абстрактный метод — refund().
    # @abstractmethod
    # def refund(self, amount):
    #     pass
    Создаём класс CreditCardPayment
    # class CreditCardPayment(Payment):
        
далее мы переопределяем метод pay
# def pay(self, amount):
#         print(f"Оплата {amount} сом с кредитной карты прошла успешно.")
        
реализация метода refund
# def refund(self, amount):
#         print(f"Возврат {amount} сом на кредитную карту выполнен.")

Второй класс, который тоже наследует Payment, но работает с криптовалютой.
# class CryptoPayment(Payment):

Реализация метода pay для криптооплаты.
# def pay(self, amount):
#         print(f"Оплата {amount} сом в криптовалюте (Bitcoin) выполнена.")
        
Реализация метода возврата для криптовалюты.
# def refund(self, amount):
#         print(f"Возврат {amount} сом в криптовалюте выполнен.")
        
список из двух объектов:
#     payments = [
#     CreditCardPayment(),
#     CryptoPayment()
# ]




2 Создаем абстрактный класс Course
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
    
Реализуем PythonCourse
# class PythonCourse(Course):
#     def start(self):
#         print("Запуск курса по Python! Добро пожаловать!")

#     def get_materials(self):
#         return ["Основы Python", "ООП в Python", "Работа с файлами", "Модули и пакеты"]

#     def end(self):
#         print("Курс по Python завершён. Молодец!")
        
Реализуем MathCourse
# class MathCourse(Course):
#     def start(self):
#         print("Начинаем курс по математике! Готовьтесь к формулам.")

#     def get_materials(self):
#         return ["Алгебра", "Геометрия", "Тригонометрия", "Статистика"]

#     def end(self):
#         print("Курс по математике окончен. Отличная работа!")
        
конец проверка работы
# python_course = PythonCourse()
# math_course = MathCourse()

# for course in (python_course, math_course):
#     course.start()
#     print("Материалы:", course.get_materials())
#     course.end()
#     print("-" * 30)



# 3 class BankAccount:
#     def __init__(self, owner, balance, pin):
        Приватные (скрытые) поля
        self.__owner = owner      
        # self.__balance = balance   
        # self.__pin = pin          

    Метод для внесения денег
    # def deposit(self, amount, pin):
    #     if pin == self.__pin:  
    #         if amount > 0:
    #             self.__balance += amount
    #             print(f"{amount} сом успешно зачислены на счёт.")
    #         else:
    #             print("Сумма должна быть положительной.")
    #     else:
    #         print("Неверный PIN-код!")

    Метод для снятия денег
    # def withdraw(self, amount, pin):
    #     if pin == self.__pin:
    #         if amount > 0:
    #             if amount <= self.__balance:
    #                 self.__balance -= amount
    #                 print(f"{amount} сом успешно сняты со счёта.")
    #             else:
    #                 print("Недостаточно средств на счёте.")
    #         else:
    #             print("Сумма должна быть положительной.")
    #     else:
    #         print("Неверный PIN-код!")

    Метод для смены PIN-кода
    # def change_pin(self, old_pin, new_pin):
    #     if old_pin == self.__pin:
    #         # if len(str(new_pin)) == 4:   к примеру пин код из 4 цифр
    #             self.__pin = new_pin
    #             print("PIN-код успешно изменён.")
    #         else:
    #             print("Новый PIN должен состоять из 4 цифр.")
    #     else:
    #         print("Неверный старый PIN-код!")

    Метод для проверки баланса (только если введён правильный пин)
    # def check_balance(self, pin):
    #     if pin == self.__pin:
    #         print(f"Баланс: {self.__balance} сом.")
    #     else:
    #         print("Неверный PIN-код!")
    
class UserProfile:
    def __init__(self, email, password):
        self.__email = email  # Приватные поля — скрыты от прямого доступа извне
        self.__password = password
        self._status = "Базовый пользователь"  # Защищённое поле можно изменять только внутри класса или наследниках

    #вход в систему
    def login(self, email, password): 
        if email == self.__email and password == self.__password:
            print("Вход выполнен успешно!")
            return True
        else:
            print("Неверная почта или пароль. Доступ запрещён!")
            return False

    def upgrade_to_premium(self): # Метод для обновления статуса на премиум
        self._status = "Премиум пользователь"
        print(" Аккаунт обновлён до Премиум!")

    def get_info(self):# Метод для получения информации о пользователе
        print(" Информация о пользователе:")
        print(f"Email: {self.__email}")
        print(f"Статус: {self._status}") # Пароль не показываем — только скрываем
        
        
        
        
        class Product:
    def __init__(self, name, price):
        self.name = name              # Название товара
        self.price = price            # Обычная цена
        self.__discount = 0           # Приватное поле: скидка (в процентах)

    # Метод для установки скидки 
    def set_discount(self, discount, is_admin=False):
        if is_admin:
            if 0 <= discount <= 100:
                self.__discount = discount
                print(f"Скидка {discount}% установлена для товара '{self.name}'.")
            else:
                print("Скидка должна быть от 0 до 100%.")
        else:
            print("У вас нет прав для установки скидки (только администратор).")

    # Получаем цену с учётом скидки
    def get_price(self):
        if self.__discount > 0:
            discounted_price = self.price * (1 - self.__discount / 100)
            return round(discounted_price, 2)  # округлим
        return self.price

    #  выведем информацию о товаре
    def info(self):
        print(f"Товар: {self.name}")
        print(f"Цена без скидки: {self.price} сом")
        if self.__discount > 0:
            print(f"Скидка: {self.__discount}%")
            print(f"Цена со скидкой: {self.get_price()} сом")
        else:
            print("Скидка не установлена.")
            
            
    class Product:
        #  def __init__(self, name, price):Этот метод устанавливает скидку на товар
           self.name = name              
           self.price = price             
           self.__discount = 0            

    def set_discount(self, discount, is_admin=False):
        if is_admin:
            if 0 <= discount <= 100:
                self.__discount = discount
                print(f"Скидка {discount}% установлена для товара '{self.name}'.")
            else:
                print("Скидка должна быть от 0 до 100%.")
        else:
            print("У вас нет прав для установки скидки (только администратор).")

#     def get_price(self):Этот метод возвращает текущую цену товара с учётом скидки.
# Если скидка есть (> 0):
# Вычисляем цену со скидкой: price * (1 - discount / 100)
# round(..., 2) — округляем до 2 знаков после запятой.
# Если скидки нет — возвращаем обычную цену.
        if self.__discount > 0:
            discounted_price = self.price * (1 - self.__discount / 100)
            return round(discounted_price, 2)
        return self.price

    def info(self): выводит всю инфу
        print(f"Товар: {self.name}")
        print(f"Цена без скидки: {self.price} сом")
        if self.__discount > 0:
            print(f"Скидка: {self.__discount}%")
            print(f"Цена со скидкой: {self.get_price()} сом")
        else:
            print("Скидка не установлена.")


product1 = Product("Телефон", 30000)
product1.set_discount(10, is_admin=False)
product1.set_discount(15, is_admin=True)
product1.info()
print("Цена с учётом скидки:", product1.get_price(), "сом")



class File:
    def __init__(self, name):
        self.name = name

    def open(self):
        pass  

# Класс для текстовых файлов
class TextFile(File):
    def open(self):
        print(f"Открываем текстовый файл '{self.name}'. Можно читать текст.")

# Класс для изображений
class ImageFile(File):
    def open(self):
        print(f"Открываем изображение '{self.name}'. Можно просматривать картинку.")

# Класс для аудио
class AudioFile(File):
    def open(self):
        print(f"Открываем аудиофайл '{self.name}'. Можно слушать звук.")

# Функция для открытия всех файлов из списка
def open_all(files):
    for file in files:
        file.open()  # Вызываем метод open для каждого объекта
        print("-" * 30)  


# использование
file1 = TextFile("notes.txt")
file2 = ImageFile("photo.jpg")
file3 = AudioFile("song.mp3")

files_list = [file1, file2, file3]

open_all(files_list)


class Car:
    def __init__(self, fuel_efficiency=10, speed=60):
        self.fuel_efficiency = fuel_efficiency
        self.speed = speed

    def move(self, distance):
        time = distance / self.speed
        fuel_used = distance * self.fuel_efficiency / 100
        print(f"Автомобиль проедет {distance} км за {time:.2f} часов, расход топлива {fuel_used:.2f} л.")


car = Car()
car.move(120)



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






