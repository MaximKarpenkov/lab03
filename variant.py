charge = int(input("Введите уровень заряда (0-100): "))

if charge < 0 or charge > 100:
    print("Ошибка диапазона")
elif charge <= 19:
    print("Низкий")
elif charge <= 79:
    print("Средний")
else:
    print("Высокий")
