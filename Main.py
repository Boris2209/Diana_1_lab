from List import *

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# main window
main_window = Tk()
main_window.title("Лаба 1, Караваева Диана, ИКБО-06-18")
main_window.geometry("1100x1000")

# create tabs
tab_control = ttk.Notebook(main_window)


""" functions and objects to perform task 1 (list) """

tab_List = ttk.Frame(tab_control)
tab_control.add(tab_List, text='Список')
tab_control.pack(expand=1, fill='both')

list_number = List()    # global tab_List

# command to input_button
def new_list():
    # if the list has already been added
    if list_number.length() != 0:
        label.configure(text="Список уже заполнен")
        return
    # else adding new list
    try:
        f = open("Test.txt")
        array_numb = f.read()   # считываем данные из файла
        for i in array_numb:
            list_number.append(i)
        label.configure(text="Успешно добавлено!")

    except Exception:
        messagebox.showinfo('Error', 'Ошибка чтения файла')

# command to length_button
def length_list():
    label.configure(text='В списке '+str(list_number.length())+' элемент(-а)')


# command to delete button
def delete_list():
    if list_number.length() != 0:
        list_number.clear_list()
        label.configure(text="Удален!")
    else:
        label.configure(text="И так пуст")


def get_list():
    label.configure(text=list_number.get_list())




# inform
label = Label(tab_List, text="Нажмите НАЧАТЬ, что бы считать из файла", font=("Arial Bold", 20))
label.grid(column=0, row=0)

input_button = Button(tab_List, text="НАЧАТЬ", font=("Arial Bold", 15), command=new_list)
input_button.grid(column=1, row=1)

# return number elements
length_button = Button(tab_List, text="Количество элементов списка", font=("Arial Bold", 15), command=length_list)
length_button.grid(column=0, row=2)

# delete button
delete_button = Button(tab_List, text="Удалить список", font=("Arial Bold", 15), command=delete_list)
delete_button.grid(column=1, row=2)

# get list button
get_list_button = Button(tab_List, text="Показать список", font=("Arial Bold", 15), command=get_list)
get_list_button.grid(column=0, row=3)




main_window.mainloop()

