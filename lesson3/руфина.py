flags = {
    'ru': ['red', 'blue', 'white'],
    'kg': ['red', 'yellow', 'красный'],
    'ua': ['red', 'blue', 'красный', 'синий'],
    'uk': ['желтый', 'синий'],
    'kz': ['blue', 'yellow', 'синий'],
    "sp" : ["yellow", "red"], 
    "sp" : ["yellow", "red"],
    "usa" : ["white", "red", "blue"],
    "arg" : ["blue", "white"]
}

while True:
    pop = input("Введите цвет флага ( введите exit чтобы выйти) ")
    
    if pop == "exit":
        print('Вы вышли из программы')
        break
    
    for key, value in flags.items():
        if pop in value:
            print(key)