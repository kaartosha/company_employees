import tkinter as tk


# Дочернее окно добавить
class ChildWindowAdd(tk.Toplevel):
    def __init__(self, root, application, name):
        super().__init__(root)
        self.view = application
        self.title(name)
        self.geometry('400x200')
        self.resizable(False, False)
        self.grab_set()  # Перехват событий приложения
        self.focus_set()  # Перехват фокуса
        label_name = tk.Label(self, text='ФИО')
        label_phone = tk.Label(self, text='Телефон')
        label_email = tk.Label(self, text='e-mail')
        label_salary = tk.Label(self, text='Зарплата')
        label_name.place(x=60, y=20)
        label_phone.place(x=60, y=50)
        label_email.place(x=60, y=80)
        label_salary.place(x=60, y=110)
        self.entry_name = tk.Entry(self, width='30')
        self.entry_phone = tk.Entry(self, width='30')
        self.entry_email = tk.Entry(self, width='30')
        self.entry_salary = tk.Entry(self, width='30')
        self.entry_name.place(x=150, y=20)
        self.entry_phone.place(x=150, y=50)
        self.entry_email.place(x=150, y=80)
        self.entry_salary.place(x=150, y=110)
        self.btn_ok = tk.Button(self, text='Добавить')
        self.btn_ok.bind('<Button-1>',
                         lambda ev: self.view.record(self.entry_name.get(),
                                                     self.entry_phone.get(),
                                                     self.entry_email.get(),
                                                     self.entry_salary.get()))
        self.btn_ok.place(x=150, y=150)
        btn_close = tk.Button(self, text='Закрыть', command=self.destroy)
        btn_close.place(x=280, y=150)


# Дочернее окно редактировать
class ChildWindowUpdate(tk.Toplevel):
    def __init__(self, root, application, name):
        super().__init__(root)
        self.view = application
        self.title(name)
        self.geometry('400x200')
        self.resizable(False, False)
        self.grab_set()  # Перехват событий приложения
        self.focus_set()  # Перехват фокуса
        label_name = tk.Label(self, text='ФИО')
        label_phone = tk.Label(self, text='Телефон')
        label_email = tk.Label(self, text='e-mail')
        label_salary = tk.Label(self, text='Зарплата')
        label_name.place(x=60, y=20)
        label_phone.place(x=60, y=50)
        label_email.place(x=60, y=80)
        label_salary.place(x=60, y=110)
        self.entry_name = tk.Entry(self, width='30')
        self.entry_phone = tk.Entry(self, width='30')
        self.entry_email = tk.Entry(self, width='30')
        self.entry_salary = tk.Entry(self, width='30')
        self.entry_name.place(x=150, y=20)
        self.entry_phone.place(x=150, y=50)
        self.entry_email.place(x=150, y=80)
        self.entry_salary.place(x=150, y=110)
        self.btn_upd = tk.Button(self, text='Сохранить')
        self.btn_upd.bind('<Button-1>',
                          lambda ev: self.view.upd_record(
                              self.entry_name.get(),
                              self.entry_phone.get(),
                              self.entry_email.get(),
                              self.entry_salary.get()))
        self.btn_upd.bind('<Button-1>',
                          lambda ev: self.destroy(), add='+')
        self.btn_upd.place(x=150, y=150)
        btn_close = tk.Button(self, text='Закрыть', command=self.destroy)
        btn_close.place(x=280, y=150)

    def default_data(self, db):
        id = self.view.tree.set(self.view.tree.selection()[0], '#1')
        row = db.one_data(id)
        self.entry_name.insert(0, row[1])
        self.entry_phone.insert(0, row[2])
        self.entry_email.insert(0, row[3])
        self.entry_salary.insert(0, row[4])


# Дочернее окно Поиск
class ChildWindowSearch(tk.Toplevel):
    def __init__(self, root, application, name):
        super().__init__(root)
        self.view = application
        self.title(name)
        self.geometry('300x100')
        self.resizable(False, False)
        self.grab_set()  # Перехват событий приложения
        self.focus_set()  # Перехват фокуса
        label_name = tk.Label(self, text='ФИО')
        label_name.place(x=50, y=20)
        self.entry_name = tk.Entry(self)
        self.entry_name.place(x=120, y=20)
        btn_close = tk.Button(self, text='Закрыть', width='10',
                              command=self.destroy)
        btn_close.place(x=200, y=60)
        self.btn_ok = tk.Button(self, text='Найти', width='10')
        self.btn_ok.bind('<Button-1>',
                         lambda ev: self.view.search_record(
                             self.entry_name.get()))
        self.btn_ok.bind('<Button-1>',
                         lambda ev: self.destroy(), add='+')
        self.btn_ok.place(x=80, y=60)
