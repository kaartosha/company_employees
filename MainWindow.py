import ChildWindow
import tkinter as tk
from tkinter import ttk


# Главное окно
class MainWindow(tk.Frame):
    def __init__(self, root, db):
        super().__init__(root)
        self.root = root
        # self.app
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
                                 columns=('id', 'name', 'phone',
                                          'email', 'salary'),
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
        self.db.update_data(id, name, phone, email, salary)
        self.view_records()

    # Удаление записи в БД
    def del_record(self):
        for item in self.tree.selection():
            self.db.delete_data(self.tree.set(item, '#1'))
        self.view_records()

    # Поиск записи в БД
    def search_record(self, name):
        for item in self.tree.get_children():
            self.tree.delete(item)
        recs = self.db.search_data(name)
        for item in recs:
            self.tree.insert('', 'end', values=item)

    # Отобразить все данные БД
    def view_records(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        recs = self.db.all_data()
        for item in recs:
            self.tree.insert('', 'end', values=item)

    # Открытие окна добавить
    def open_child_window_add(self):
        ChildWindow.ChildWindowAdd(self.root, self,
                                   'Добавление сотрудника')

    # Открытие окна редактировать
    def open_child_window_update(self):
        wnd = ChildWindow.ChildWindowUpdate(self.root, self,
                                            'Редактирование сотрудника')
        wnd.default_data(self.db)

    # Открытие окна поиск
    def open_child_window_search(self):
        ChildWindow.ChildWindowSearch(self.root, self, 'Поиск сотрудника')
