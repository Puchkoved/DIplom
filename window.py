import tkinter as tk
import inp
import mplib
import win_menu
import out

func = ''
coefficient = {}
f_argument = ''


def get_func():
    """
    Функция считывает введенную пользователем информацию и запускает механизм ее обработки
    """
    global func, coefficient
    if coefficient != {}:
        del_coefficient()
    func = ent_func.get()
    if not func:
        info('Введите функцию')
    else:
        f = inp.check_f(func)
        coefficient = f[1]
        func = f[0]
        information = f[2]
        if information == '':
            info(func)
            label()
        else:
            info(information)


def info(inf):
    """
    Выводит информационную строку
    :param inf: str, информация для вывода
    """
    lb_info = tk.Label(win, text=f'Информация: {inf}', anchor='w')
    lb_info.grid(row=13, column=0, columnspan=2, sticky='we')


def del_coefficient():
    """
    Функция, удаляющая виджеты кнопок параметров
    """
    global coefficient, f_argument
    for i in coefficient:
        for j in range(1, 4):
            coefficient[i][j].destroy()
    bt_build.grid_remove()
    bt_add_build.grid_remove()
    coefficient = {}
    f_argument = ''


def del_func():
    """
    Функция, очищающая поле ввода
    """
    ent_func.delete(0, 'end')


def label():
    """Функция, добавляющая виджеты параметров"""
    global coefficient
    count = 1
    for i in coefficient:
        coefficient[i] = [coefficient[i],
                          tk.Label(win, text=f'{i}'),
                          tk.Entry(win, validate='key', vcmd=(win.register(validate_entry), '%P')),
                          tk.Radiobutton(win,
                                         text='Решить относительно',
                                         variable=argument,
                                         value=i,
                                         command=select_argument)]
        coefficient[i][1].grid(row=14 + count, column=0)
        coefficient[i][2].grid(row=14 + count, column=1)
        coefficient[i][2].insert(0, f'{coefficient[i][0]}')
        coefficient[i][3].grid(row=14 + count, column=2)
        count += 1
    bt_build.grid(row=14 + count, column=0)
    bt_add_build.grid(row=14 + count, column=1)


def select_argument():
    """
    Функция считывающая аргумент, относительно которого строится график
    """
    global coefficient, f_argument
    if f_argument != '':
        coefficient[f_argument][2].grid()
    f_argument = argument.get()
    coefficient[f_argument][2].grid_remove()
    out_lb_func(f_argument)


def out_lb_func(arg):
    """
    Функция выводит текст f(arg)
    :param arg: : str, агумент относительно которого строится график
    """
    lb_func = tk.Label(win, text=f'f({arg}) =')
    lb_func.grid(row=12, column=0)


def get_coefficient():
    """
    Функция срабатывает при нажатии кнопки Построить и запускает механизм постройки графика
    """
    global coefficient, func
    for i in coefficient:
        coefficient[i][0] = float(coefficient[i][2].get())
    x_y = out.calculate(func, coefficient, f_argument, float(x_max), float(x_min), float(y_min), float(y_max), flag=1)
    mplib.graf(x_y[0], x_y[1], x_y[2], f_argument, win, name_graf, graf_grid, graf_axis, graf_legend)


def get_add_build():
    """
    Функция срабатывает при нажатии кнопки Добавить и запускает механизм постройки графика и добовляет его к имеющимся
    """
    global coefficient, func
    for i in coefficient:
        coefficient[i][0] = float(coefficient[i][2].get())
    x_y = out.calculate(func, coefficient, f_argument, float(x_max), float(x_min), float(y_min), float(y_max), flag=2)
    mplib.graf(x_y[0], x_y[1], x_y[2], f_argument, win,name_graf, graf_grid, graf_axis, graf_legend)


def validate_entry(inp):
    """
    Функция, возвращающая True(являеться inp числом) или False(не являеться inp числом),
    :param inp:входные данные
    :return: True / False
    """
    if inp != '':
        try:
            float(inp)
            return True
        except:
            return False
    else:
        return True


def add_sett():
    """
    Функция срабатывает при нажатии кнопки 'Применить' и считывает настройки графика
    """
    global x_min, x_max, y_min, y_max, name_graf, graf_grid, graf_axis, graf_legend
    x_min = ent_x_min.get()
    x_max = ent_x_max.get()
    y_min = ent_y_min.get()
    y_max = ent_y_max.get()
    if (x_max == '' or x_min == '' or
            y_max == '' or y_min == ''):
        info_set('Не все обязательные поля заполнены')
    elif float(x_max) < float(x_min):
        info_set('x_max < x_min')
    elif float(y_max) < float(y_min):
        info_set('y_max < y_min')
    name_graf = ent_name_graf.get()
    graf_grid = grid_flag.get()
    graf_axis = axis_flag.get()
    graf_legend = legend_flag.get()
    info_set('Настройки сохранены')


def info_set(text):
    """
    Функция выводит информацию связанную с настройкой
    :param text: str, текст информационного сообщения
    """
    info3 = tk.Label(win, text=f'Информация:\n {text}', anchor='w')
    info3.grid(row=11, column=0, columnspan=2, sticky='we')


x_min = 0
x_max = 10
y_min = 0
y_max = 30
name_graf = ''
graf_grid = True
graf_axis = True
graf_legend = True
########## окно ##########
win = tk.Tk()
argument = tk.StringVar()
argument.set(False)
win.title('График-Лаб')
photo = tk.PhotoImage(file='images/BESSELJ_functions.png')
win.iconphoto(False, photo)
win.geometry('1300x650+200+100')
########## Кнопки ##########
bt_del = tk.Button(win, text='Очистить поле', command=del_func)
bt_func = tk.Button(win, text='Проверить', command=get_func)
bt_build = tk.Button(win, text='Построить график', command=get_coefficient)
bt_add_build = tk.Button(win, text='Добавить график', command=get_add_build)
########## Поле ввода ##########
ent_func = tk.Entry(win)
######### Настройки ###########
info1 = tk.Label(win, text='Настройки осей:')
grid_flag = tk.BooleanVar()
axis_flag = tk.BooleanVar()
legend_flag = tk.BooleanVar()
lb_y_min = tk.Label(win, text='*                      ymin = ')
lb_y_max = tk.Label(win, text='*                      ymax = ')
lb_x_min = tk.Label(win, text='*                      xmin = ')
lb_x_max = tk.Label(win, text='*                      xmax = ')
ent_x_min = tk.Entry(win, validate='key', vcmd=(win.register(validate_entry), '%P'))
ent_x_max = tk.Entry(win, validate='key', vcmd=(win.register(validate_entry), '%P'))
ent_y_min = tk.Entry(win, validate='key', vcmd=(win.register(validate_entry), '%P'))
ent_y_max = tk.Entry(win, validate='key', vcmd=(win.register(validate_entry), '%P'))
ent_x_min.insert(0, str(x_min))
ent_x_max.insert(0, str(x_max))
ent_y_min.insert(0, str(y_min))
ent_y_max.insert(0, str(y_max))
info2 = tk.Label(win, text='Настройки графика:')
lb_name_graf = tk.Label(win, text='Название графика:')
ent_name_graf = tk.Entry(win)
grid_flag.set(graf_grid)
axis_flag.set(graf_axis)
legend_flag.set(graf_legend)
ch_grid = tk.Checkbutton(win, text='Сетка', variable=grid_flag, offvalue=False, onvalue=True)
ch_axis = tk.Checkbutton(win, text='Подписи осей', variable=axis_flag, offvalue=False, onvalue=True)
ch_legend = tk.Checkbutton(win, text='Легенда', variable=legend_flag, offvalue=False, onvalue=True)
bt_add = tk.Button(win, text='Применить', command=add_sett)
info1.grid(row=0, column=0)
lb_x_min.grid(row=1, column=0)
lb_x_max.grid(row=2, column=0)
lb_y_min.grid(row=3, column=0)
lb_y_max.grid(row=4, column=0)
ent_x_min.grid(row=1, column=1)
ent_x_max.grid(row=2, column=1)
ent_y_min.grid(row=3, column=1)
ent_y_max.grid(row=4, column=1)
info2.grid(row=5, column=0)
lb_name_graf.grid(row=6, column=0)
ent_name_graf.grid(row=6, column=1)
ch_grid.grid(row=7, column=0)
ch_axis.grid(row=8, column=0)
ch_legend.grid(row=9, column=0)
bt_add.grid(row=10, column=0)
bt_del.grid(row=10, column=1)
info_set('*  -  Обязательные поля')
######################################

out_lb_func(f_argument)
ent_func.grid(row=12, column=1)
bt_func.grid(row=14, column=0)
bt_del.grid(row=14, column=1)
win_menu.add_menu(win)
win.mainloop()
if __name__ == '__main__':
    pass
