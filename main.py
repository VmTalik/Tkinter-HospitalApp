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


class MainWindow(Base, MainFrames):
    def __init__(self):
        Base.__init__(self)
        MainFrames.__init__(self)
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        w = w // 2
        h = h // 2
        w = w - 600
        h = h - 450
        self.geometry('1200x800+{}+{}'.format(w, h))
        self.put_label()
        tk.Button(self.ButtonFrame, text="Добавить пациента", width=20, command=self.open_add_patient_window).pack(
            side=tk.LEFT,
            padx=15)
        tk.Button(self.ButtonFrame, text="Просмотр пациентов", width=30, command=self.open_view_patient_window).pack(
            side=tk.LEFT, padx=10)
        tk.Button(self.ButtonFrame, text="Осмотры врача", width=20, command=self.open_doctor_examination_window).pack(
            side=tk.LEFT,
            padx=15)
        tk.Button(self.ButtonFrame, text="Заболевания", width=20, command=self.disease).pack(
            side=tk.LEFT,
            padx=15)
        tk.Button(self.ButtonFrame, text="Больничный лист", width=20, command=self.sicklist).pack(
            side=tk.LEFT,
            padx=15)
        tk.Button(self.ButtonFrame, text="Смены", width=20, command=self.shift).pack(
            side=tk.LEFT,
            padx=15)

    @staticmethod
    def put_label():
        lbltitle = tk.Label(bd=20, relief=tk.RIDGE, text="ИАС Диагностика",
                            fg='cyan', bg='blue', font=('times new roman', 50, 'bold'))
        lbltitle.pack(side=tk.TOP, fill=tk.X)

        img = ImageTk.PhotoImage(Image.open('media\medais.ico'))
        imglabel = tk.Label(image=img)
        imglabel.image = img

    @staticmethod
    def open_add_patient_window():
        AddPatientWindow()

    @staticmethod
    def open_view_patient_window():
        ViewPatientInfo()

    @staticmethod
    def open_doctor_examination_window():
        DoctorExamination()

    @staticmethod
    def disease():
        Disease()

    @staticmethod
    def sicklist():
        SickList()

    @staticmethod
    def shift():
        Shift()


class AddPatientWindow(Base):
    def __init__(self):
        super().__init__()
        self.title("ИАС Диагностика")
        self.iconbitmap('media\drug.ico')
        self.fio = tk.Entry(self, width=30)
        self.fio.grid(row=1, column=1, padx=20)
        self.birth_date = tk.Entry(self, width=30)
        self.birth_date.grid(row=2, column=1)
        self.phone_number = tk.Entry(self, width=30)
        self.phone_number.grid(row=3, column=1)
        self.home_address = tk.Entry(self, width=30)
        self.home_address.grid(row=4, column=1)
        self.policy = tk.Entry(self, width=30)
        self.policy.grid(row=5, column=1)
        self.sector = tk.Entry(self, width=30)
        self.sector.grid(row=6, column=1)
        self.fio_label = tk.Label(self, text="ФИО")
        self.fio_label.grid(row=1, column=0)
        self.birth_date_label = tk.Label(self, text=" Дата рождения")
        self.birth_date_label.grid(row=2, column=0)
        self.phone_number_label = tk.Label(self, text="Телефон")
        self.phone_number_label.grid(row=3, column=0)
        self.home_address_label = tk.Label(self, text="Адрес")
        self.home_address_label.grid(row=4, column=0)
        self.policy_label = tk.Label(self, text="Полис")
        self.policy_label.grid(row=5, column=0)
        self.sector_label = tk.Label(self, text="Участок")
        self.sector_label.grid(row=6, column=0)
        tk.Button(self, text="Добавить пациента", width=40, command=self.insert_data_patient).grid(row=7, column=0)

    def insert_data_patient(self):
        a = self.fio.get()
        b = self.birth_date.get()
        c = self.phone_number.get()
        d = self.home_address.get()
        e = self.policy.get()
        f = self.sector.get()
        self.cursor.execute(insert_into_add_patient, (a, b, c, d, e, f))
        self.conn.commit()
        self.destroy()


class ViewPatientInfo(Base, MainFrames):
    def __init__(self):
        Base.__init__(self)
        MainFrames.__init__(self)
        self.card_number = None
        self.enter_patient_window()

    def enter_patient_window(self):
        self.card_number = tk.Entry(self, width=30)
        self.card_number.grid(row=1, column=1, padx=20)
        self.label_card_number = tk.Label(self, text="Номер карты пациента")
        self.label_card_number.grid(row=1, column=0)
        tk.Button(self, text="Ввести", width=40, command=self.submit).grid(row=7, column=0)
        pass

    def submit(self):
        self.patient_id = self.card_number.get()
        self.cursor.execute(select_patient_data.format(self.patient_id))
        rows = self.cursor.fetchall()
        print(rows)
        row = rows[0]
        self.destroy()
        tk.Label(self.DataFrameLeft, text=f"ФИО: {row[0]}\n"
                                          f"Дата рождения: {row[1]}",
                 font=('times new roman', 12, 'bold'), padx=2, pady=6).grid()
        tk.Label(self.DataFrameRight, text=f"Полис: {row[4]}\n"
                                           f"Подразделение: {row[5]}\n",
                 font=('times new roman', 12, 'bold'), padx=2, pady=6).grid()
        tk.Label(self.DetailsFrame, text=f"Телефон: {row[2]}\n"
                                         f"Домашний адрес: {row[3]}",
                 font=('times new roman', 12, 'bold'), padx=2, pady=6).grid()


class DoctorExamination(ViewPatientInfo):
    def __init__(self):
        ViewPatientInfo.__init__(self)

    def submit(self):
        a = self.card_number.get()
        self.cursor.execute(select_doctor_examination.format(a))
        rows = self.cursor.fetchall()
        self.destroy()
        self.med_examination_id = rows[0][0]
        for i in rows:
            tk.Label(self.DetailsFrame, text=f"Дата визита: {i[1]}\n\n "
                                             f"Цель визита: {i[2]}\n\n"
                                             f"Жалобы: {i[3]}",
                     font=('times new roman', 12, 'bold'), padx=2, pady=6).grid()
        print(rows)


class Disease(Base, MainFrames):
    def __init__(self):
        Base.__init__(self)
        MainFrames.__init__(self)
        self.cursor.execute(select_disease)
        rows = self.cursor.fetchall()
        for i in rows:
            tk.Label(self.DataFrameLeft, text=f"Тип заболевания: {i[1]}\n"
                                              f"Травма: {i[2]} ",
                     font=('times new roman', 12, 'bold'), padx=2, pady=6).grid()
        self.destroy()


class SickList(ViewPatientInfo):
    def __init__(self):
        ViewPatientInfo.__init__(self)

    def submit(self):
        a = self.card_number.get()
        self.cursor.execute(select_sick_list.format(a))
        rows = self.cursor.fetchall()
        row = rows[0]
        tk.Label(self.DataFrameLeft, text=f"Номер карты пациента: {a}\n",
                 font=('times new roman', 12, 'bold'), padx=2, pady=6).grid()

        tk.Label(self.DetailsFrame, text=f"Начало даты больничного: {row[2]}\n"
                                         f"Конец даты больничного: {row[3]}\n"
                                         f"Статус: {row[4]}\n"
                                         f"Диагноз:{row[5]}\n",
                 font=('times new roman', 12, 'bold'), padx=2, pady=6).grid()
        self.destroy()


class Shift(Base, MainFrames):
    def __init__(self):
        Base.__init__(self)
        MainFrames.__init__(self)
        self.enter_doctor_window()

    def enter_doctor_window(self):
        self.doctor_id = tk.Entry(self, width=30)
        self.doctor_id.grid(row=1, column=1, padx=20)
        self.label_card_number = tk.Label(self, text="Введите идентификатор доктора")
        self.label_card_number.grid(row=1, column=0)
        tk.Button(self, text="Ввести", width=40, command=self.submit).grid(row=7, column=0)

    def submit(self):
        self.patient_id = self.doctor_id.get()
        self.cursor.execute(select_shift.format(int(self.patient_id)))
        rows = self.cursor.fetchall()
        row = rows[0]
        self.destroy()

        tk.Label(self.DetailsFrame, text=f"ФИО: {row[2]}\n"
                                         f"Должность: {row[3]}\n"
                                         f"Дата смены: {row[0]}\n"
                                         f"Время смены: {row[1]}\n",
                 font=('times new roman', 12, 'bold'), padx=2, pady=6).grid()


if __name__ == "__main__":
    app = LoginIN()
    app.mainloop()
