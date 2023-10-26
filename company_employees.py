import tkinter as tk
import sqlite3
from tkinter import ttk


# Главное окно
class Main_window(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.db = db
        # Инициализация виджетов
        toolbar = tk.Frame()
        toolbar.pack(side=tk.TOP, fill=tk.X)
        # Кнопка Добавить
        self.add_img = tk.PhotoImage(file='./img/add.png')
        btn_add = tk.Button(toolbar, text='Добавить',
                            image=self.add_img, bd=0,
                            command=self.open_child_window_add)
        btn_add.pack(side=tk.LEFT)
        # Кнопка Редактировать
        self.upd_img = tk.PhotoImage(file='./img/update.png')
        btn_upd = tk.Button(toolbar, text='Редактировать',
                            image=self.upd_img, bd=0,
                            command=self.open_child_window_update)
        btn_upd.pack(side=tk.LEFT)
        # Кнопка Удалить
        self.del_img = tk.PhotoImage(file='./img/delete.png')
        btn_del = tk.Button(toolbar, text='Удалить',
                            image=self.del_img, bd=0,
                            command=self.del_record)
        btn_del.pack(side=tk.LEFT)
        # Кнопка Поиск
        self.src_img = tk.PhotoImage(file='./img/search.png')
        btn_src = tk.Button(toolbar, text='Поиск',
                            image=self.src_img, bd=0,
                            command=self.open_child_window_search)
        btn_src.pack(side=tk.LEFT)
        # Кнопка Обновить
        self.ref_img = tk.PhotoImage(file='./img/refresh.png')
        btn_ref = tk.Button(toolbar, text='Обновить',
                            image=self.ref_img, bd=0,
                            command=self.view_records)
        btn_ref.pack(side=tk.LEFT)
        # Таблица вывода данных БД
        self.tree = ttk.Treeview(self,
                                 columns=('id', 'name', 'phone', 'email', 'salary'),
                                 show='headings', height=17)
        self.tree.column('id', width=45, anchor=tk.CENTER)
        self.tree.column('name', width=300, anchor=tk.CENTER)
        self.tree.column('phone', width=110, anchor=tk.CENTER)
        self.tree.column('email', width=125, anchor=tk.CENTER)
        self.tree.column('salary', width=60, anchor=tk.CENTER)
        self.tree.heading('id', text='Номер')
        self.tree.heading('name', text='ФИО')
        self.tree.heading('phone', text='Телефон')
        self.tree.heading('email', text='e-mail')
        self.tree.heading('salary', text='Зарплата')
        self.tree.pack()
        # Добавление прокрутки
        scroll = tk.Scrollbar(root, command=self.tree.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scroll.set)
        self.view_records()

    # Добавление записи в БД
    def record(self, name, phone, email, salary):
        self.db.insert_data(name, phone, email, salary)
        self.view_records()

    # Редактирование записи в БД
    def upd_record(self, name, phone, email, salary):
        id = self.tree.set(self.tree.selection()[0], '#1')
        self.db.cursor.execute('''UPDATE users
                               SET name = ?, phone = ?, email = ?, salary = ?
                               WHERE id = ?''',
                               (name, phone, email, salary, id))
        self.db.connection.commit()
        self.view_records()

    # Удаление записи в БД
    def del_record(self):
        for item in self.tree.selection():
            self.db.cursor.execute('DELETE FROM users WHERE id = ?',
                                   (self.tree.set(item, '#1'), ))
        self.db.connection.commit()
        self.view_records()

    # Поиск записи в БД
    def search_record(self, name):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.db.cursor.execute('SELECT * FROM users WHERE name LIKE ? ',
                               ('%' + name + '%', ))
        recs = self.db.cursor.fetchall()
        for item in recs:
            self.tree.insert('', 'end', values=item)

    # Отобразить все данные БД
    def view_records(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.db.cursor.execute('SELECT * FROM users')
        recs = self.db.cursor.fetchall()
        for item in recs:
            self.tree.insert('', 'end', values=item)

    # Открытие окна добавить
    def open_child_window_add(self):
        Child_window_add()

    # Открытие окна редактировать
    def open_child_window_update(self):
        Child_window_update()

    # Открытие окна поиск
    def open_child_window_search(self):
        Child_window_search()


# Дочернее окно добавить
class Child_window_add(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.view = app
        self.title('Добавление сотрудника')
        self.geometry('400x200')
        self.resizable(False, False)
        self.grab_set()  # Перехват событий приложения
        self.focus_set()  # Перехват фокуса
        label_name = tk.Label(self, text='ФИО')
        label_phone = tk.Label(self, text='Телефон')
        label_email = tk.Label(self, text='e-mail')
        label_salary = tk.Label(self, text='Зарплата')
        label_name.place(x=60, y=50)
        label_phone.place(x=60, y=80)
        label_email.place(x=60, y=110)
        label_salary.place(x=60, y=140)
        self.entry_name = tk.Entry(self)
        self.entry_phone = tk.Entry(self)
        self.entry_email = tk.Entry(self)
        self.entry_salary = tk.Entry(self)
        self.entry_name.place(x=220, y=50)
        self.entry_phone.place(x=220, y=80)
        self.entry_email.place(x=220, y=110)
        self.entry_salary.place(x=220, y=140)
        btn_close = tk.Button(self, text='Закрыть', command=self.destroy)
        btn_close.place(x=310, y=170)
        self.btn_ok = tk.Button(self, text='Добавить')
        self.btn_ok.bind('<Button-1>',
                         lambda ev: self.view.record(self.entry_name.get(),
                                                     self.entry_phone.get(),
                                                     self.entry_email.get(),
                                                     self.entry_salary.get()))
        self.btn_ok.place(x=220, y=170)


# Дочернее окно редактировать
class Child_window_update(Child_window_add):
    def __init__(self):
        super().__init__()
        self.title('Редактирование сотрудника')
        self.btn_ok.destroy()
        self.btn_upd = tk.Button(self, text='Сохранить')
        self.btn_upd.bind('<Button-1>',
                     lambda ev: self.view.upd_record(self.entry_name.get(),
                                                     self.entry_phone.get(),
                                                     self.entry_email.get(),
                                                     self.entry_salary.get()))
        self.btn_upd.bind('<Button-1>',
                          lambda ev: self.destroy(), add='+')
        self.btn_upd.place(x=220, y=170)
        self.db = db
        self.default_data()

    def default_data(self):
        id = self.view.tree.set(self.view.tree.selection()[0], '#1')
        self.db.cursor.execute('SELECT * FROM users WHERE id = ?', id)
        row = self.db.cursor.fetchone()
        self.entry_name.insert(0, row[1])
        self.entry_phone.insert(0, row[2])
        self.entry_email.insert(0, row[3])
        self.entry_salary.insert(0, row[4])


# Дочернее окно Поиск
class Child_window_search(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.view = app
        self.title('Поиск сотрудника')
        self.geometry('300x100')
        self.resizable(False, False)
        self.grab_set()  # Перехват событий приложения
        self.focus_set()  # Перехват фокуса
        label_name = tk.Label(self, text='ФИО')
        label_name.place(x=30, y=20)
        self.entry_name = tk.Entry(self)
        self.entry_name.place(x=120, y=20)
        btn_close = tk.Button(self, text='Закрыть', command=self.destroy)
        btn_close.place(x=210, y=60)
        self.btn_ok = tk.Button(self, text='Найти')
        self.btn_ok.bind('<Button-1>',
                         lambda ev: self.view.search_record(self.entry_name.get()))
        self.btn_ok.bind('<Button-1>',
                         lambda ev: self.destroy(), add='+')
        self.btn_ok.place(x=120, y=60)


# База данных
class DataBase:
    def __init__(self):
        self.connection = sqlite3.connect('contacts.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            phone TEXT,
                            email TEXT,
                            salary TEXT)''')
        self.connection.commit()

    # Добавление строки в БД
    def insert_data(self, name, phone, email, salary):
        self.cursor.execute('''INSERT INTO users (name, phone, email, salary)
                            VALUES (?, ?, ?, ?)''', (name, phone, email, salary))
        self.connection.commit()


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Список сотрудников компании')
    root.geometry('660x450')
    root.resizable(False, False)
    db = DataBase()
    app = Main_window(root)
    app.pack()
    root.mainloop()
