from List import *
from Queue import *
from Stack import *

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


""" functions and objects to perform task 2 (queue) """

tab_Queue = ttk.Frame(tab_control)
tab_control.add(tab_Queue, text='Очередь')
tab_control.pack(expand=1, fill='both')

# my Queue
queue_number = Queue()


# command to input_q_button
def add_q_element():
    numb = input_q_element.get()

    queue_number.insert(numb)

    input_q_element.delete(0, END)

    q_display.configure(text=queue_number.get_queue())

# command to delete q botton
def delete_q_element():
    queue_number.remove()

    q_display.configure(text=queue_number.get_queue())


# command to start_task
def start_q_task():
    queue_number.task()
    q_display.configure(text=queue_number.get_queue())


# queue display
q_display = Label(tab_Queue, text="Вводите по одному элементу", font=("Arial Bold", 20))
q_display.grid(column=0, row=0)

# input queue
input_q_element = Entry(tab_Queue, width=50, font=("Arial Bold", 20))
input_q_element.grid(column=0, row=1)
input_q_element.focus()

# button input
input_q_button = Button(tab_Queue, text="Добавить в очередь", font=("Arial Bold", 15), command=add_q_element)
input_q_button.grid(column=1, row=1)

# delete element button
delete_q_button = Button(tab_Queue, text="Вытащить последний элемент", font=("Arial Bold", 15), command=delete_q_element)
delete_q_button.grid(column=1, row=2)

# button to task
q_button_task = Button(tab_Queue, text="Добавить в конец из начала", font=("Arial Bold", 15), command=start_q_task)
q_button_task.grid(column=0, row=2)


""" functions and objects to perform task 3 (stack) """

tab_Stack = ttk.Frame(tab_control)
tab_control.add(tab_Stack, text='Стек')
tab_control.pack(expand=1, fill='both')


# my Stack
stack_number = Stack()


# command to input_s_button
def add_s_element():
    numb = input_s_element.get()

    stack_number.push(numb)

    input_s_element.delete(0, END)

    s_display.configure(text=stack_number.get_stack())

# command to delete q botton
def delete_s_element():
    stack_number.pop()

    s_display.configure(text=stack_number.get_stack())


# command to start_task
def start_s_task():
    stack_number.task()
    s_display.configure(text=stack_number.get_stack())


# stack display
s_display = Label(tab_Stack, text="Вводите по одному элементу", font=("Arial Bold", 20))
s_display.grid(column=0, row=0)

# input stack elements
input_s_element = Entry(tab_Stack, width=50, font=("Arial Bold", 20))
input_s_element.grid(column=0, row=1)
input_s_element.focus()

# button input
input_s_button = Button(tab_Stack, text="Добавить в стек", font=("Arial Bold", 15), command=add_s_element)
input_s_button.grid(column=1, row=1)

# delete element button
delete_s_button = Button(tab_Stack, text="Вытащить элемент", font=("Arial Bold", 15), command=delete_s_element)
delete_s_button.grid(column=1, row=2)

# button to task
s_button_task = Button(tab_Stack, text="Добавить в начало из конца", font=("Arial Bold", 15), command=start_s_task)
s_button_task.grid(column=0, row=2)



main_window.mainloop()

