import tkinter as tk


def add_about():
    """
    Функция, расказывающая пользователю о приложении
    """
    menu_about = tk.Tk()
    menu_about.title('О программе')
    menu_about.geometry('600x450+200+100')
    text = ('Привет!!!\n'
             '\n'
            'График-Лаб - это мощный инструмент для создания графиков, который поможет вам визуализировать данные'
            'и проанализировать информацию. Независимо от того, являетесь ли вы студентом, ученым или просто хотите'
            'лучше понять свои данные, эта программа станет вашим незаменимым помощником.\n'
            '\n'
            'Ключевые особенности:\n'
            '   1.Интуитивно понятный интерфейс: Создавайте графики всего за несколько кликов, даже без опыта работы с '
            'подобными программами.\n'
            '   2.Гибкость настройки: Подбирайте цвета, стили, метки и другие параметры для создания идеального '
            'графика.\n'
            '   3.Широкий выбор типов графиков(Скоро будет доступна): Линейные, гистограммы, диаграммы рассеяния, '
            'круговые диаграммы и многое другое.\n'
            'созданные графики в различные форматы, включая изображения и векторную графику.\n'
            '\n'
            'График-Лаб - это идеальный инструмент для:\n'
            '   1.Визуализации данных: Представление данных в понятной и наглядной форме\n'
            '   2.Анализа информации: Выявление трендов, закономерностей и аномалий в данных.\n'
            '   3.Создания презентаций: Добавьте профессиональные графики в свои презентации и отчёты.\n'
            '   4.Обучения: Изучите основы построения графиков и научитесь анализировать данные.\n'
            )
    text_box = tk.Text(menu_about, wrap="word", font='Times 12')
    text_box.insert(tk.END, text)
    text_box.configure(state='disabled')
    text_box.pack()



