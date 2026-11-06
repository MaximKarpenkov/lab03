year = int(input("Введите год (1-9999): "))

if year < 1 or year > 9999:
    print("Ошибка: год вне диапазона")
elif year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Да, високосный")
else:
    print("Нет, не високосный")
