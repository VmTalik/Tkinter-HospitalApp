import tkinter as tk
from PIL import ImageTk, Image
from db import HospitalBase
from sql_queries import insert_into_add_patient, select_patient_data, select_doctor_examination, select_disease, \
    select_sick_list, select_shift
from users import users_dict
from tkinter import messagebox as mb


class Base(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ИАС Диагностика")
        self.iconbitmap('media\drug.ico')
        self.db = HospitalBase()
        self.conn = self.db.connect()
        self.cursor = self.conn.cursor()


class LoginIN(Base):
    def __init__(self):
        super().__init__()
        self.login_window()

    def login_window(self):
        self.user_login = tk.Entry(self, width=30)
        self.user_login.grid(row=1, column=1, padx=20)
        self.user_password = tk.Entry(self, width=30)
        self.user_password.grid(row=2, column=1)
        self.user_login_label = tk.Label(self, text="Логин")
        self.user_login_label.grid(row=1, column=0)
        self.user_password_label = tk.Label(self, text="Пароль")
        self.user_password_label.grid(row=2, column=0)
        tk.Button(self, text="Войти в систему", width=40, command=self.submit).grid(row=7, column=0)
        pass

    def submit(self):
        a = self.user_login.get()
        b = self.user_password.get()
        try:
            if users_dict[a] == b:
                self.conn = self.db.connect(a, b)
                self.cursor = self.conn.cursor()
                # time.sleep(1)
                self.destroy()
                self.open_main_window()

        except KeyError:
            mb.showerror('Ошибка', 'Неверный пароль или логин')

    @staticmethod
    def open_main_window():
        MainWindow()


class MainFrames:
    def __init__(self):
        # ===== Рамки данных =====
        self.DataFrame = tk.Frame(bd=20, padx=20, relief=tk.RIDGE)
        self.DataFrame.place(x=50, y=130, width=1100, height=400)

        self.DataFrameLeft = tk.LabelFrame(self.DataFrame, bd=10, relief=tk.RIDGE,
                                           padx=10, font=('arial', 12, 'bold'), text='Информация пациента')
        self.DataFrameLeft.place(x=10, y=5, width=980, height=350)

        self.DataFrameRight = tk.LabelFrame(self.DataFrame, bd=10, relief=tk.RIDGE,
                                            padx=10, font=('arial', 12, 'bold'), text='Информация')
        self.DataFrameRight.place(x=550, y=5, width=460, height=350)
        # ===== Рамка кнопок =====

        self.ButtonFrame = tk.Frame(bd=20, relief=tk.RIDGE)
        self.ButtonFrame.place(x=0, y=550, width=1200, height=70)

        # ===== Рамка описания =====

        self.DetailsFrame = tk.Frame(bd=20, relief=tk.RIDGE)
        self.DetailsFrame.place(x=0, y=600, width=1200, height=190)

        # ===== Левая рамка =====

        self.lblNameTablet = tk.Label(self.DataFrameLeft, text="Названия",
                                      font=('times new roman', 12, 'bold'), padx=2, pady=6)
        self.lblNameTablet.grid(row=0, column=0)


class MainWindow:
    pass

if __name__ == "__main__":
    app = LoginIN()
    app.mainloop()
