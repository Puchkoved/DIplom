import math

out_y = []
out_x = []
out_text = []


def calculate(calculate_func, calculate_coefficient, argument, x_max, x_min, y_min, y_max, flag):
    """
    Функция производит расчеты координат графика
    :param y_max: Максимальный y
    :param y_min: Минимальный y
    :param x_max: Максимальный х
    :param x_min: Минимальный х
    :param calculate_func: str, функция
    :param calculate_coefficient: dict, ключи - параметры функции, значение - значение параметра функци
    :param argument: str, параметр, относительно которого строится график
    :param flag: int, флаг на отработку сценария функции
    :return:x_graf: list, массив координат x
            graphics: list, массив координат y
            text: list, массив с названиями графиков
    """
    global out_y, out_text, out_x
    x_graf = []
    y_graf = []
    steps = 10000
    step = (x_max - x_min) / steps
    calculate_func = replacement_coefficient(calculate_func, calculate_coefficient, argument)
    for i in range(steps+1):
        x_graf.append(x_min + step * i)
        if argument == '':
            y_graf.append(eval(calculate_func))
        else:
            try:
                exec(f'{argument}={x_min + step * i}')
                val = eval(calculate_func)
                if y_min < val < y_max:
                    y_graf.append(val)
                else:
                    y_graf.append(None)
            except:
                y_graf.append(None)
    if flag == 1:
        out_y = []
        out_x = []
        out_text = []
    out_y.append(y_graf)
    out_x.append(x_graf)
    calculate_func = f'f({argument})=' + calculate_func
    out_text.append(calculate_func.replace('math.', ''))
    return out_x, out_y, out_text


def replacement_coefficient(func, r_coefficient, argument):
    """
    Заменяет коэффициенты на числовые значения
    :param argument: str: аргумент, относительно которого строится функция
    :param func: str: введенная функция
    :param r_coefficient: dict: коэффициенты
    :return: func: str: измененная функция
    """
    coefficient = r_coefficient.copy()
    for i in coefficient:
        if i != argument:
            func = func.replace(i, str(coefficient[i][0]))
    return func
