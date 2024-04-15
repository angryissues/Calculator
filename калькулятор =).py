from copy import copy  # для копирования списков и других объектов

data = {
    'ноль': 0,
    'один': 1,
    'два': 2,
    'три': 3,
    'четыре': 4,
    'пять': 5,
    'шесть': 6,
    'семь': 7,
    'восемь': 8,
    'девять': 9,
    'десять': 10,
    'одиннадцать': 11,
    'двенадцать': 12,
    'тринадцать': 13,
    'четырнадцать': 14,
    'пятнадцать': 15,
    'шестнадцать': 16,
    'семнадцать': 17,
    'восемнадцать': 18,
    'девятнадцать': 19,
    'двадцать': '20d',
    'тридцать': '30d',
    'сорок': '40d',
    'пятьдесят': '50d',
    'шестьдесят': '60d',
    'семьдесят': '70d',
    'восемьдесят': '80d',
    'девяносто': '90d',
    'плюс': '+',
    'минус': '-',
    'умножить': '*',
    'делить' : '//',
    'скобка1': '(',
    'скобка2': ')'
}

def string_calc(a):  # принимает один аргумент a - строку, содержащую выражение, и возвращает результат вычисления этого выражения
    c = copy(a.split())  # копируем список, полученный из строки a, разбивая ее на слова
    for i in range(len(c)):  # запускаем цикл, который проходит по каждому элементу списка c
        sign = ''  # объявляем переменную sign и присваивает ей пустую строку
        if 'd' in str(data[c[i]]):  # проверяет, содержит ли элемент data[c[i]] символ 'd'.
            if i + 1 == len(c):  # проверяем, является ли число с d последним элементом в строке
                sign = data[c[i]][0:2]  # если да, то выводит десяток без d
            else:  # если число с d стоит не на последнем месте
                sign = data[c[i]][0:2] if str(data[c[i + 1]]) in '+-*//' else data[c[i]][0]
        else:
            sign = data[c[i]]  # если строка стоит без десятков, просто берем число из даты
        c[i] = str(sign)  # преобразует значение sign в строку и присваивает его элементу списка c
    b = ''.join(c)  # объединяем все элементы списка c в одну строку и присваивает ее переменной b
    return eval(b)  # объединяем все слова в выражении в одну строку и вычисляем результат


def get_revers(my_dict, search_val):
    search_cache = search_val
    l_keys = list(my_dict.keys())  # список ключей из словаря my_dict и присваиваем его переменной l_keys
    l_value = list(my_dict.values())  # список значений из словаря my_dict и присваиваем его переменной l_value
    add_data = ''  # объявляем переменную add_data и присваиваем ей пустую строку
    if str(search_val)[0] == '-':  # проверяем, начинается ли строка search_val с символа '-'
        add_data = 'минус '
        search_val = str(search_val)[1:]
    if len(search_val) == 1 or search_val[0] == '1' and len(search_val) <= 2:
        return add_data + l_keys[l_value.index(int(search_val))]
    elif len(search_val) == 2:
        if str(search_val)[1] == '0':
            return add_data + l_keys[l_value.index(search_val + 'd')]
        else:
            return add_data + list(my_dict.keys())[list(my_dict.values()).index(search_val[0] + '0d')] + " " + \
                list(my_dict.keys())[list(my_dict.values()).index(int(search_val[1]))]
    elif str(search_cache)[0] == '-' and len(search_val) >= 3:
            return f'Извините, я не могу перевести в слова число {search_cache}'
    else:
        return f'Извините, я не могу перевести в слова число {search_val}'

print('Привет! Я калькулятор! Я умею складывать, вычитать, делить и умножать, но только до 99(включительно). \nТакже я умею считать отрицательные числа до -99, выстраивать приоритетность операций и считать Ваши примеры со скобками!')

while True:
    string1 = input('Введите выражение словами:\n')
    string = copy(string1).split()
    flag_can_translate = False
    for i in string:
        if not i in data.keys():
            print('В моей библиотеке нет таких слов. Сформулируйте Ваш запрос иначе.')
            flag_can_translate = True
            break
    if flag_can_translate:
        continue
    try:
        value = str(string_calc(string1))
        new_string = get_revers(data, value)
    except Exception:
        print("ПРОЧЬ ИЗ СТРАНЫ")
        continue
    print(new_string)
