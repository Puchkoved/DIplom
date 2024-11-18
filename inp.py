import math


def check_f(f_func):
    """
    Функция преобразовывает данные, введеные пользователем, в данные, читаемые интерпретатором
    :param f_func: str, функция, полученная от пользователя
    :return: new_func: str, данные, читаемые интерпретатором
             coefficient: dict, ключи - параметры функции, значение - значение параметра функции
                                (если параметр участвует в умножении или делении, то значение 1,
                                иначе 0)
            info: str, данные об ошибке
    """
    f_coefficient = {}
    new_func = ''
    info = ''
    i = 0
    while i < len(f_func):
        if f_func[i] == '^':
            new_func += '**'
            i += 1
            continue
        elif f_func[i: i + 2].lower() == 'tg':
            new_func += 'math.tan'
            i += 2
            continue
        elif f_func[i: i + 3].lower() == 'ctg':
            new_func += '1/math.tan'
            i += 3
            continue
        elif f_func[i: i + 1].lower() in ('e',):
            new_func += 'math.' + f_func[i: i + 1].lower()
            i += 1
            continue
        elif f_func[i: i + 2].lower() in ('pi',):
            new_func += 'math.' + f_func[i: i + 2].lower()
            i += 2
            continue
        elif f_func[i: i + 3].lower() in ('cos', 'sin', 'log', 'tan', 'exp'):
            new_func += 'math.' + f_func[i: i + 3].lower()
            i += 3
            continue
        elif f_func[i: i + 4].lower() in ('sqrt', 'acos', 'asin', 'atan', 'log2'):
            new_func += 'math.' + f_func[i: i + 4].lower()
            i += 4
            continue
        elif f_func[i: i + 5].lower() in ('log10',):
            new_func += 'math.' + f_func[i: i + 5].lower()
            i += 5
            continue
        elif f_func[i: i + 8].lower() in ('factorial',):
            new_func += 'math.' + f_func[i: i + 9].lower()
            i += 9
            continue
        new_func += f_func[i]
        if f_func[i].isalpha():
            if ((i != len(f_func) - 1 and (f_func[i + 1].isalpha() or f_func[i + 1] in ('/', '*'))) or
                    (i != 0 and (f_func[i - 1].isalpha() or f_func[i - 1] in ('/', '*')))):
                f_coefficient[f_func[i]] = 1
            else:
                f_coefficient[f_func[i]] = 0
        if (i != len(f_func) - 1 and f_func[i].isalpha() and
                (f_func[i + 1].isalpha() or f_func[i + 1].isdigit() or f_func[i + 1] == '(')):
            new_func += '*'
        elif (i != len(f_func) - 1 and f_func[i].isdigit() and
              (f_func[i + 1].isalpha() or f_func[i + 1] == '(')):
            new_func += '*'
        i += 1
    try:
        eval(replacement_coefficient(new_func, f_coefficient))
    except SyntaxError:
        f_coefficient = {}
        info = 'Упс, что то пошло не так... Проверьте функцию.'
    except:
        pass
    return new_func, f_coefficient, info


def replacement_coefficient(func, r_coefficient):
    """
    Заменяет коэффициенты на числовые значения
    :param func: str: введенная функция
    :param r_coefficient: dict: коэффициенты
    :return: func: str: измененная функция
    """
    coefficient = r_coefficient.copy()
    for i in coefficient:
        func = func.replace(i, str(coefficient[i]))
    return func


if __name__ == '__main__':
    check_f('kx+b')
