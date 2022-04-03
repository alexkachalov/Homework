
list_a = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
'была', '+5', 'градусов']

list_b = []

for i in list_a:
    if i.isdigit():
        if len(i) < 2:
            i = ("0" + i)
    elif i == "+5":
            i = "+05"
    else:
        i = i
    list_b.append(i)

#добавляем нули к числам
print(list_b)

#составляем список из номеров чисел

list_с = []

for j in list_b:
    if 1 < len(j) < 4:
        list_с.append(list_b.index(j))

print(list_с)

#добавляем кавычки

list_b.insert(list_с[0], '"')
list_b.insert(list_с[0]+2 , '"')
list_b.insert(list_с[1]+2, '"')
list_b.insert(list_с[1]+4, '"')
list_b.insert(list_с[2]+4, '"')
list_b.insert(list_с[2]+6, '"')

print(list_b)

#объединяем

full_list = ' '.join(list_b)
print(full_list)

