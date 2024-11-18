import tkinter as tk
import menu.about
import menu.help


def add_menu(window):
    """
    Добавляет меню
    :param window: obj: объект главного окна
    """
    main_menu = tk.Menu(window)
    window.config(menu=main_menu)

    help_menu = tk.Menu(main_menu, tearoff=0)
    help_menu.add_command(label="Помощь", command=menu.help.add_help)
    help_menu.add_command(label="О программе", command=menu.about.add_about)

    main_menu.add_cascade(label="Справка", menu=help_menu)
