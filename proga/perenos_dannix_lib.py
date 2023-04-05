import xlsxwriter, csv
from xlsxwriter.utility import xl_rowcol_to_cell, xl_range_abs
def worktable(name_workbook: str, name_worksheet: str, path: str, first: int, last: int, cell: tuple = (2,2)):
    """ Вводим путь, размер графика, название книги, название листа,
             кол-во в строке, кол-во в столбце, номер первого текстого файла, номер последнего тесктого файла,
             ячейку левого верхнего угла с которого все начнется.
        Делает таблицу в эксель с данными, в строках идут значения разных образцов, в столбцах одного образца из разного времени.
     """

    workbook = xlsxwriter.Workbook(path + "\\" + name_workbook + ".xlsx")
    worksheet = workbook.add_worksheet(name_worksheet)
    cell_format01 = workbook.add_format()
    cell_format01.set_align("center")
    cell_format01.set_align("vcenter")
    cell_format01.set_border()
    for j in range(first, last+1):
        pathfile = path + "\\" + str(j) + ".csv"
        with open(pathfile, newline="") as cvsfile:
            reader = csv.reader(cvsfile, delimiter=",")
            s = list(reader)
            s[1] = s[1][1:]
        kolvo_obrazsov = len(s[1])
        if j == first:
            min_y = float(s[1][0])
            max_y = float(s[1][0])
        for i in range(len(s[1])):
            s[1][i] = float(s[1][i])
            min_y = min(min_y, s[1][i])
            max_y = max(max_y, s[1][i])
        for i in range(len(s[1])):
            worksheet.write(j - first + cell[0], i+cell[1], s[1][i], cell_format01)
    return workbook, worksheet, min_y, max_y, kolvo_obrazsov

def worktable_tolko(name_workbook: str, name_worksheet: str, path: str, first: int, last: int, cell: tuple = (2,2)):
    """ Вводим путь, размер графика, название книги, название листа,
             кол-во в строке, кол-во в столбце, номер первого текстого файла, номер последнего тесктого файла,
             ячейку левого верхнего угла с которого все начнется.
        Делает таблицу в эксель с данными, в строках идут значения разных образцов, в столбцах одного образца из разного времени.
     """

    workbook = xlsxwriter.Workbook(path + "\\" + name_workbook + ".xlsx")
    worksheet = workbook.add_worksheet(name_worksheet)
    cell_format01 = workbook.add_format()
    cell_format01.set_align("center")
    cell_format01.set_align("vcenter")
    cell_format01.set_border()
    for j in range(first, last+1):
        pathfile = path + "\\" + str(j) + ".csv"
        with open(pathfile, newline="") as cvsfile:
            reader = csv.reader(cvsfile, delimiter=",")
            s = list(reader)
            s[1] = s[1][1:]
        for i in range(len(s[1])):
            s[1][i] = float(s[1][i])
        for i in range(len(s[1])):
            worksheet.write(j - first + cell[0], i+cell[1], s[1][i], cell_format01)
    workbook.close()

def worktableRGB(name_workbook: str, name_worksheet: str, path: str, first: int, last: int, cell: tuple = (2,2)):
    workbook = xlsxwriter.Workbook(path + "\\" + name_workbook + ".xlsx")
    worksheet = workbook.add_worksheet(name_worksheet)
    cell_format01 = workbook.add_format()
    cell_format01.set_align("center")
    cell_format01.set_align("vcenter")
    cell_format01.set_border()
    for j in range(first, last+1):
        pathfile = path + "\\" + str(j) + ".csv"
        with open(pathfile, newline="") as cvsfile:
            reader = csv.reader(cvsfile, delimiter=",")
            s = list(reader)
            s[1] = s[1][1:]
        if j == first:
            min_y = float(s[1][0])
            max_y = float(s[1][0])
        kolvo_obrazsov = len(s[2])
        for k in range(1,4):
            if k != 1:
                h = 1
            else:
                h = 0
            for i in range(h, len(s[k])):
                s[k][i] = float(s[k][i])
            for i in range(h, len(s[k])):
                worksheet.write(j - first + cell[0], i+cell[1] + kolvo_obrazsov*(k-1), s[k][i], cell_format01)
    workbook.close()

def worktableRGB_tolko(name_workbook: str, name_worksheet: str, path: str, first: int, last: int, cell: tuple = (2,2)):
    workbook = xlsxwriter.Workbook(path + "\\" + name_workbook + ".xlsx")
    worksheet = workbook.add_worksheet(name_worksheet)
    cell_format01 = workbook.add_format()
    cell_format01.set_align("center")
    cell_format01.set_align("vcenter")
    cell_format01.set_border()
    for j in range(first, last+1):
        pathfile = path + "\\" + str(j) + ".csv"
        with open(pathfile, newline="") as cvsfile:
            reader = csv.reader(cvsfile, delimiter=",")
            s = list(reader)
            s[1] = s[1][1:]
        kolvo_obrazsov = len(s[2])
        for k in range(1,4):
            if k != 1:
                h = 1
            else:
                h = 0
            for i in range(h, len(s[k])):
                s[k][i] = float(s[k][i])
            for i in range(h, len(s[k])):
                worksheet.write(j - first + cell[0], i+cell[1] + kolvo_obrazsov*(k-1), s[k][i], cell_format01)
    workbook.close()

def worktable_Lera(name_workbook: str, name_worksheet: str, path: str, first: int, last: int, cell: tuple = (2,2)):
    workbook = xlsxwriter.Workbook(path + "\\" + name_workbook + ".xlsx")
    worksheet = workbook.add_worksheet(name_worksheet)
    cell_format01 = workbook.add_format()
    cell_format01.set_align("center")
    cell_format01.set_align("vcenter")
    cell_format01.set_border()
    kolvo_obrazsov = 0
    RGB = ["R", "G", "B"]
    pislo = ["320", "160", "80"]
    for j in range(first, last+1):
        pathfile = path + "\\" + "(" + str(j) + ")" + ".csv"
        with open(pathfile, newline="") as cvsfile:
            reader = csv.reader(cvsfile, delimiter=",")
            s = list(reader)
            s[1] = s[1][1:]
        kolvo_obrazsov = len(s[2])
        for k in range(1,4):
            if k != 1:
                h = 1
            else:
                h = 0

            for i in range(h, len(s[k])):
                s[k][i] = float(s[k][i])
            for i in range(h, len(s[k])):
                worksheet.write(j - first + cell[0], i+cell[1] + kolvo_obrazsov*(k-1), s[k][i], cell_format01)
    for j in range(1, (last-first+1)//5+1):
        for k in range(0, 3):
            if k != 0:
                h = 1
            else:
                h = 0
            worksheet.write((j - 1) * 3 - first + cell[0] + last + 2 + k, cell[1] - 1, RGB[k] + pislo[j-1], cell_format01)
            for i in range(kolvo_obrazsov - 1):
                worksheet.write_formula((j-1)*3 - first + cell[0] + last + 2 + k, i+cell[1], "=AVERAGE(" +
                                str(xl_rowcol_to_cell(cell[0] + (j-1)*5, i+cell[1] + kolvo_obrazsov*k + h)) + ":" + str(xl_rowcol_to_cell(cell[0] + j*5 -1, i+cell[1] + kolvo_obrazsov*k +h)) + ")", cell_format01)

    workbook.close()

def graph(path, name_workbook,name_worksheet, kolvo_v_stroke, kolvo_v_stolbse, first, last, cell: tuple = (2,2), size = (7,10)):
    """ Вводим путь, размер графика, название книги, название листа,
             кол-во в строке, кол-во в столбце, номер первого текстого файла, номер последнего тесктого файла,
             ячейку левого верхнего угла с которого все начнется.
             Делает таблицу с напечатанными временем, именами образцов (каждому образцу соотвествует контроль, который идет после всех образцов), также строит
             графики, на которых вместе контроль и образец.
             """
    workbook, worksheet, min_y, max_y, kolvo_obrazsov = worktable(name_workbook, name_worksheet, path, first, last, cell)
    kolvo_obrazsov = kolvo_obrazsov//2
    cell_format01 = workbook.add_format()
    cell_format01.set_align("center")
    cell_format01.set_align("vcenter")
    cell_format01.set_border()
    cell_x = xl_range_abs(cell[0], cell[1]-1, cell[0] + last - first, cell[1]-1)
    name = "=" + name_worksheet + "!"
    y = 0
    for i in range(last-first+1):
        x = float(input("Введите время: №" + str(i)))
        worksheet.write(cell[0]+i, cell[1]-1, x, cell_format01)
        y = x
    for i in range(kolvo_obrazsov):
        worksheet.write(cell[0]-1, cell[1]+i, input("Введите имя образца: №" + str(i)), cell_format01)
    for j in range(kolvo_v_stolbse):
        for i in range(kolvo_v_stroke):
            if j*kolvo_v_stroke + i + 1 <= kolvo_obrazsov:
                chart = workbook.add_chart({'type': 'scatter',
                                            'subtype': 'straight_with_markers'})
                cellname = xl_rowcol_to_cell(cell[0]-1, cell[1]+i + j*kolvo_v_stroke, row_abs=True, col_abs=True)
                cell_y = xl_range_abs(cell[0], cell[1] + i + j*kolvo_v_stroke, cell[0] + last - first, cell[1] + i + j*kolvo_v_stroke)
                chart.add_series({
                    'name': name + cellname,
                    'categories': name + cell_x,
                    'values': name + cell_y,
                    "line": {'color': 'gray'},
                    'marker': {
                        'type': 'diamond',
                        'size': 7,
                        'border': {'color': 'orange'},
                        'fill': {'color': 'orange'},
                    }
                })
                kcell_y = xl_range_abs(cell[0], cell[1] + i + kolvo_obrazsov + j * kolvo_v_stroke, cell[0] + last - first, cell[1] + i + kolvo_obrazsov + j * kolvo_v_stroke)
                chart.add_series({
                    'name': "Контроль",
                    'categories': name + cell_x,
                    'values': name + kcell_y,
                    'marker': {
                        'type': 'square',
                        'size': 7,
                        'border': {'color': 'orange'},
                        'fill': {'color': 'orange'},
                    },
                    "line": {'color': 'orange'}
                })
                chart.set_x_axis({
                    'min': 0,
                    'max': y+1,
                                  })
                chart.set_y_axis({'min': min_y//10*10, 'max': max_y//10*10 + 10, "major_gridlines": {'visible': False}})
                chart.set_size({'width': size[1]//0.0264, 'height': size[0]//0.0264})
                chart.set_plotarea({
                    'layout': {
                        'x': 0.1,
                        'y': 0.05,
                        'width': 0.85,
                        'height': 0.85,
                    }
                })
                cell_graph = xl_rowcol_to_cell(cell[0]+last-first+2, cell[1]-1)
                worksheet.insert_chart(cell_graph, chart, {'x_offset': (size[1]//0.0264)*i + 4*i, 'y_offset': (size[0]//0.0264)*j + 4*j})
            else:
                break
    workbook.close()

def graph_odin_kontrol(path, name_workbook, name_worksheet, kolvo_v_stroke, kolvo_v_stolbse, first, last, cell = (2,2), size = (7,10)):
    """  Вводим путь, размер графика, название книги, название листа,
         кол-во графиков в строке, кол-во графиков в столбце, номер первого текстого файла, номер последнего тесктого файла,
         ячейку левого верхнего угла с которого все начнется.
         Делает таблицу с напечатанными временем, именами образцов (контроль первый), также строит
         графики, на которых вместе контроль и образец.
         """
    workbook, worksheet, min_y, max_y,  kolvo_obrazsov = worktable(name_workbook, name_worksheet, path, first, last, cell)
    cell_format01 = workbook.add_format()
    cell_format01.set_align("center")
    cell_format01.set_align("vcenter")
    cell_format01.set_border()
    cell_x = xl_range_abs(cell[0], cell[1]-1, cell[0] + last - first, cell[1]-1)
    name = "=" + name_worksheet + "!"
    y = 0
    for i in range(last-first+1):
        x = float(input("Введите время: №" + str(i)))
        worksheet.write(cell[0]+i, cell[1]-1, x, cell_format01)
        y = x
    for i in range(kolvo_obrazsov):
        worksheet.write(cell[0]-1, cell[1]+i, input("Введите имя образца: №" + str(i)), cell_format01)
    for j in range(kolvo_v_stolbse):
        for i in range(kolvo_v_stroke):
            if j*kolvo_v_stroke + i + 1 <= kolvo_obrazsov:
                chart = workbook.add_chart({'type': 'scatter',
                                            'subtype': 'straight_with_markers'})
                cellname = xl_rowcol_to_cell(cell[0]-1, cell[1]+i + j*kolvo_v_stroke, row_abs=True, col_abs=True)
                cell_y = xl_range_abs(cell[0], cell[1] + i + j*kolvo_v_stroke, cell[0] + last - first, cell[1] + i + j*kolvo_v_stroke)
                chart.add_series({
                    'name': name + cellname,
                    'categories': name + cell_x,
                    'values': name + cell_y,
                    "line": {'color': 'gray'},
                    'marker': {
                        'type': 'diamond',
                        'size': 7,
                        'border': {'color': 'orange'},
                        'fill': {'color': 'orange'},
                    }
                })
                kcell_y = xl_range_abs(cell[0], cell[1], cell[0] + last - first, cell[1])
                chart.add_series({
                    'name': "Контроль",
                    'categories': name + cell_x,
                    'values': name + kcell_y,
                    'marker': {
                        'type': 'square',
                        'size': 7,
                        'border': {'color': 'orange'},
                        'fill': {'color': 'orange'},
                    },
                    "line": {'color': 'orange'}
                })
                chart.set_x_axis({
                    'min': 0,
                    'max': y+1,
                                  })
                chart.set_y_axis({'min': min_y//10*10, 'max': max_y//10*10 + 10, "major_gridlines": {'visible': False}})
                chart.set_size({'width': size[1]//0.0264, 'height': size[0]//0.0264})
                chart.set_plotarea({
                    'layout': {
                        'x': 0.1,
                        'y': 0.05,
                        'width': 0.85,
                        'height': 0.85,
                    }
                })
                cell_graph = xl_rowcol_to_cell(cell[0]+last-first+2, cell[1]-1)
                worksheet.insert_chart(cell_graph, chart, {'x_offset': (size[1]//0.0264)*i + 4*i, 'y_offset': (size[0]//0.0264)*j + 4*j})
            else:
                break
    workbook.close()

def graph_model(worksheet,name, kolvo_obrazsov, kolvo_v_stroke, kolvo_v_stolbse, first, last, min_y, max_y, size = (7,10), cell = (2,2)):
    cell_format01 = workbook.add_format()
    cell_format01.set_align("center")
    cell_format01.set_align("vcenter")
    cell_format01.set_border()
    cell_x = xl_range_abs(cell[0], cell[1]-1, cell[0] + last - first, cell[1]-1)
    name = "=" + name + "!"
    y = 0
    for i in range(last-first+1):
        x = float(input("Введите время: №" + str(i)))
        worksheet.write(cell[0]+i, cell[1]-1, x, cell_format01)
        y = x
    for i in range(kolvo_obrazsov):
        worksheet.write(cell[0]-1, cell[1]+i, input("Введите имя образца: №" + str(i)), cell_format01)
    for j in range(kolvo_v_stolbse):
        for i in range(kolvo_v_stroke):
            if j*kolvo_v_stroke + i + 1 <= kolvo_obrazsov:
                chart = workbook.add_chart({'type': 'scatter',
                                            'subtype': 'straight_with_markers'})
                cellname = xl_rowcol_to_cell(cell[0]-1, cell[1]+i + j*kolvo_v_stroke, row_abs=True, col_abs=True)
                cell_y = xl_range_abs(cell[0], cell[1] + i + j*kolvo_v_stroke, cell[0] + last - first, cell[1] + i + j*kolvo_v_stroke)
                chart.add_series({
                    'name': name + cellname,
                    'categories': name + cell_x,
                    'values': name + cell_y,
                    "line": {'color': 'gray'},
                    'marker': {
                        'type': 'diamond',
                        'size': 7,
                        'border': {'color': 'orange'},
                        'fill': {'color': 'orange'},
                    }
                })
                kcell_y = xl_range_abs(cell[0], cell[1], cell[0] + last - first,
                                      cell[1])
                chart.add_series({
                    'name': "Краситель с бензальдегидом",
                    'categories': name + cell_x,
                    'values': name + kcell_y,
                    "line": {'color': '#00CCCC'},
                    'marker': {
                        'type': 'diamond',
                        'size': 7,
                        'border': {'color': '#00CCCC'},
                        'fill': {'color': '#00CCCC'},
                    }
                })
                mkcell_y = xl_range_abs(cell[0], cell[1] + i + kolvo_obrazsov + j * kolvo_v_stroke, cell[0] + last - first, cell[1] + i + kolvo_obrazsov + j * kolvo_v_stroke)
                chart.add_series({
                    'name': "Модель контроль",
                    'categories': name + cell_x,
                    'values': name + mkcell_y,
                    'marker': {
                        'type': 'square',
                        'size': 7,
                        'border': {'color': 'orange'},
                        'fill': {'color': 'orange'},
                    },
                    "line": {'color': 'orange'}
                })
                kcell_y = xl_range_abs(cell[0], cell[1] + kolvo_obrazsov, cell[0] + last - first,
                                       cell[1]+ kolvo_obrazsov)
                chart.add_series({
                    'name': "Краситель контроль",
                    'categories': name + cell_x,
                    'values': name + kcell_y,
                    "line": {'color': '#99FF66'},
                    'marker': {
                        'type': 'square',
                        'size': 7,
                        'border': {'color': '#99FF66'},
                        'fill': {'color': '#99FF66'},
                    }
                })
                chart.set_x_axis({
                    'min': 0,
                    'max': y+1,
                                  })
                chart.set_y_axis({'min': min_y, 'max': max_y, "major_gridlines": {'visible': False}})
                chart.set_size({'width': size[1]//0.0264, 'height': size[0]//0.0264})
                chart.set_plotarea({
                    'layout': {
                        'x': 0.1,
                        'y': 0.05,
                        'width': 0.85,
                        'height': 0.85,
                    }
                })
                cell_graph = xl_rowcol_to_cell(cell[0]+last-first+2, cell[1]-1)
                worksheet.insert_chart(cell_graph, chart, {'x_offset': (size[1]//0.0264)*i + 4*i, 'y_offset': (size[0]//0.0264)*j + 4*j})
            else:
                break
