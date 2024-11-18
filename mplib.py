import matplotlib.pyplot as pl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


def graf(x, y, text, argument, win, name_graf, graf_grid, graf_axis, graf_legend):
    """
    Функуия строит график по заданным параметрам
    :param x: list, список точек по х
    :param y: list, список точек по y
    :param text: list, текст легенды графиков
    :param argument: str, параметр, относительно которого строится график
    :param win: obj, объект окна в котором строится график
    :param name_graf: str, назавание графика
    :param graf_grid: bol, влаг на сетку(вкл/выкл)
    :param graf_axis: bol, влаг на подпись осей(вкл/выкл)
    :param graf_legend: bol, влаг на легенду(вкл/выкл)
    """
    figure = pl.Figure(figsize=(7, 4), dpi=100)
    figure_plot = figure.add_subplot()
    if graf_axis:
        figure_plot.set_ylabel(f'f({argument})')
        figure_plot.set_xlabel(argument)
    if graf_grid:
        figure_plot.grid()
    figure.suptitle(name_graf)
    line = FigureCanvasTkAgg(figure, master=win)
    line.get_tk_widget().grid(row=0, column=3, rowspan=14, sticky='ns')
    toolbar = NavigationToolbar2Tk(line, win, pack_toolbar=False)
    toolbar.grid(row=15, column=3, sticky='we')
    for i in range(len(y)):
        figure_plot.plot(x[i], y[i], label=text[i])
        if graf_legend:
            figure_plot.legend()
