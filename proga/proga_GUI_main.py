import tkinter as tk
import perenos_dannix_lib as per
from tkinter import filedialog as fd


def add():
    lenn = len(times)
    times.insert(lenn,list_time_entry.get())
    list_time_listbox.insert(lenn, "№" + str(len(times)) + ": " + list_time_entry.get())
    print(times)

def rezim(flag, book, name):
    book["rezim"] = flag
    mb["text"] = name

def open_text_file(book):
    filetypes = (('text files', '*.csv'),
                 ('All files', '*.*'))
    f = fd.askopenfile(filetypes=filetypes,
                       initialdir=r"C:\Users\Hipor\Desktop\Шифы ноут")
    name = f.name
    name = name.replace("/", "\\", 8)
    i = 1
    while name:
        if name[-i] != "\\":
            i += 1
        else:
            name = name[:-i]
            break
    root["text"] = name
    book["path"] = name

def vibor_funck(book: dict):
    rezim, path, name_workbook, name_worksheet, kolvo_v_stroke, kolvo_v_stolbse, first, last = book.values()
    first, last = int(first), int(last)
    if kolvo_v_stroke and kolvo_v_stolbse:
        kolvo_v_stroke, kolvo_v_stolbse = int(kolvo_v_stroke), int(kolvo_v_stolbse)
    if rezim == "worktable_tolko":
        per.worktable_tolko(name_workbook, name_worksheet, path, first, last)
    elif rezim == "worktableRGB_tolko":
        per.worktableRGB_tolko(name_workbook, name_worksheet, path, first, last)
    elif rezim == "graph":
        per.graph(path, name_workbook, name_worksheet, kolvo_v_stroke, kolvo_v_stolbse, first, last)
    elif rezim == "graph_odin_kontrol":
        per.graph_odin_kontrol(path, name_workbook, name_worksheet, kolvo_v_stroke, kolvo_v_stolbse, first, last)
    elif rezim == "graph_model":
        per.graph_model(path, name_workbook, name_worksheet, kolvo_v_stroke, kolvo_v_stolbse, first, last)
    elif rezim == "worktable_Lera":
        per.worktable_Lera(name_workbook, name_worksheet, path, first, last)

def pusk(book):
    book["name_workbook"] = name_workbook_entry.get()
    book["name_worksheet"] = name_worksheet_entry.get()
    book["kolvo_v_stroke"] = kolvo_v_stroke_entry.get()
    book["kolvo_v_stolbse"] = kolvo_v_stolbse_entry.get()
    book["first"] = first_entry.get()
    book["last"] = last_entry.get()
    vibor_funck(book)



window = tk.Tk()
window.title("Моя супер прога")
book = {"rezim": "", "path": "", "name_workbook": "", "name_worksheet": "", "kolvo_v_stroke": "", "kolvo_v_stolbse": "", "first": "", "last": ""}
window.geometry("1500x900+200+70")

canvas = tk.Canvas(window, bg= "#FAEBD7")
canvas.place(relwidth=1, relheight=1)

top_frame = tk.Frame(window, bg= "#DEB887")
top_frame.place_configure(relx=0.03, rely= 0.02, relheight=0.1, relwidth=0.94)

mb = tk.Menubutton(top_frame, text="Выбор режима", relief="raised", font=("Calibri", 12))
menu = tk.Menu(mb, tearoff=0)
menu.add_command(label="Контроль для каждого", command=lambda :rezim("graph", book, "Контроль для каждого"))
menu.add_command(label="Один контроль", command=lambda :rezim("graph_odin_kontrol", book, "Один контроль"))
menu.add_command(label="Двойной контроль и образец", command=lambda :rezim("graph_model", book, "Двойной контроль и образец"))
menu.add_command(label="Таблица флуоресценции", command=lambda :rezim("worktable_tolko", book, "Таблица флуоресценции"))
menu.add_command(label="Таблица RGB", command=lambda :rezim("worktableRGB_tolko", book, "Таблица RGB"))
menu.add_command(label="Таблица Леры", command=lambda :rezim("worktable_Lera", book, "Таблица Леры"))
mb["menu"] =  menu
mb.place(relx=0.015, rely=0.2, relheight= 0.6, relwidth= 0.1675)

root = tk.Label(top_frame, font=("Calibri", 10))
root.place(relx=0.24, rely=0.2, relheight= 0.6, relwidth= 0.6)

root_button = tk.Button(top_frame, text="Выбрать первый файл", command=lambda:open_text_file(book), relief="raised", font=("Calibri", 12))
root_button.place(relx=0.85, rely=0.2, relheight=0.6, relwidth= 0.12)

midle_frame = tk.Frame(window, bg= "#DEB887")
midle_frame.place_configure(relx=0.03, rely=0.15, relheight=0.8, relwidth=0.94)

name_workbook = tk.Frame(midle_frame, bg="#DEB887")
name_workbook.place(relx=0.03, rely=0.03, relheight=0.08, relwidth=0.5)
name_workbook_label = tk.Label(name_workbook, text="Имя файла", font=("Calibri", 12))
name_workbook_label.place(relx=0, rely=0, relheight=0.6, relwidth= 0.15)
name_workbook_entry = tk.Entry(name_workbook, bd=3, font=("Calibri", 12))
name_workbook_entry.place(relx=0.2, rely=0, relheight=0.6, relwidth=0.8)

name_worksheet = tk.Frame(midle_frame, bg="#DEB887")
name_worksheet.place(relx=0.03, rely=0.12, relheight=0.08, relwidth=0.5)
name_worksheet_label = tk.Label(name_worksheet, text="Имя листа", font=("Calibri", 12))
name_worksheet_label.place(relx=0, rely=0, relheight=0.6, relwidth= 0.15)
name_worksheet_entry = tk.Entry(name_worksheet, bd=3, justify="center", font=("Calibri", 12))
name_worksheet_entry.place(relx=0.2, rely=0, relheight=0.6, relwidth=0.3)
name_worksheet_entry.insert(0, "Флуоресценция")

first_last = tk.Frame(midle_frame, bg="#DEB887")
first_last.place(relx=0.03, rely=0.25, relheight=0.15, relwidth=0.5)
first_label = tk.Label(first_last, text="Первый", font=("Calibri", 12))
first_label.place(relx=0, rely=0, relheight=0.3, relwidth=0.15)
first_entry = tk.Entry(first_last, bd=3, justify="center", font=("Calibri", 12))
first_entry.place(relx=0.2, rely=0, relheight=0.3, relwidth=0.2)
last_label = tk.Label(first_last, text="Последний", font=("Calibri", 12))
last_label.place(relx=0, rely=0.4, relheight=0.3, relwidth=0.15)
last_entry = tk.Entry(first_last, bd=3, justify="center", font=("Calibri", 12))
last_entry.place(relx=0.2, rely=0.4, relheight=0.3, relwidth=0.2)

kolvo = tk.Frame(midle_frame, bg="#DEB887")
kolvo.place(relx=0.5, rely=0.25, relheight=0.15, relwidth=0.5)
kolvo_v_stroke_label = tk.Label(kolvo, text="Количество образцов в строке", font=("Calibri", 12))
kolvo_v_stroke_label.place(relx=0, rely=0, relheight=0.3, relwidth=0.35)
kolvo_v_stroke_entry = tk.Entry(kolvo, bd=3, justify="center", font=("Calibri", 12))
kolvo_v_stroke_entry.place(relx=0.4, rely=0, relheight=0.3, relwidth=0.2)
kolvo_v_stolbse_label = tk.Label(kolvo, text="Количество образцов в столбце", font=("Calibri", 12))
kolvo_v_stolbse_label.place(relx=0, rely=0.4, relheight=0.3, relwidth=0.35)
kolvo_v_stolbse_entry = tk.Entry(kolvo, bd=3, justify="center", font=("Calibri", 12))
kolvo_v_stolbse_entry.place(relx=0.4, rely=0.4, relheight=0.3, relwidth=0.2)

pusk_button = tk.Button(midle_frame, text="Запуск", command=lambda: pusk(book), relief="raised", bg="#B22222", font=("Times", 25))
pusk_button.place(relx=0.8, rely=0.85, relheight=0.1, relwidth=0.15)

list_frame = tk.Frame(window, bg="#DEB887")
list_frame.place_configure(relx=0.03, rely=0.5, relheight=0.4, relwidth=0.7)

times = []
times_var = tk.Variable(value=times)

list_time_entry = tk.Entry(list_frame, font=("Calibri", 12), bd=3, )
list_time_entry.place(relx=0.33, rely=0.2, relheight=0.1, relwidth=0.1)
list_time_button = tk.Button(list_frame, text="Добавить", command=add, font=("Calibri", 12))
list_time_button.place(relx=0.33, rely=0.35, relheight=0.1, relwidth=0.1)

list_time_listbox = tk.Listbox(list_frame, listvariable=times_var, font=15)
list_time_listbox.place_configure(relx=0.015, rely=0.03, relheight=0.94, relwidth=0.3)

window.mainloop()