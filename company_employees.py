import DataBase
import MainWindow
import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Список сотрудников компании')
    root.geometry('660x450')
    root.resizable(False, False)
    db = DataBase.DataBase()
    app = MainWindow.MainWindow(root, db)
    app.pack()
    root.mainloop()
