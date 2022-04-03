# создаем список вручную

my_list = [71.02, 78.15, 89.90, 41.21, 56.08, 31.02, 156.05, 34.87, 67.12, 16.77, 20.22, 19.19]

# вывод цен через запятую в одну строку в формате ХХ руб. УУ. коп.

rub_list = []
for i in my_list:
    i = str(int(i // 1))
    rub_list.append(i)

cop_list = []
for i in my_list:
    i = str(round((i - i // 1) * 100))
    if len(i) < 2:
        i = ("0" + i)
    cop_list.append(i)

price_list = []
for i in range(len(rub_list)):
    price_list.append(rub_list[i] + " руб. " + cop_list[i] + " коп.")
print(price_list)

# вывод цен,отсортированных по возрастанию (без создания нового списка)

my_list.sort()
print(my_list)

# отсортировать по убыванию с созданием нового списка

declining_list = my_list
declining_list.sort(reverse=True)
print(declining_list)

# вывести цены пяти самых дорогих товаров

print(declining_list[0:5])