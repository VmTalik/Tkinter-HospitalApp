import tkinter as tk
from PIL import ImageTk, Image
from db import HospitalBase
from sql_queries import insert_into_add_patient


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ИАС Диагностика")
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        w = w // 2
        h = h // 2
        w = w - 600
        h = h - 450
        self.geometry('1200x800+{}+{}'.format(w, h))
        self.put_label()
        self.put_frames()
        tk.Button(self.ButtonFrame, text="Пациенты", width=20, command=self.open_add_patient_window).pack()

    def put_label(self):
        lbltitle = tk.Label(bd=20, relief=tk.RIDGE, text="ИАС Диагностика",
                            fg='cyan', bg='blue', font=('times new roman', 50, 'bold'))
        lbltitle.pack(side=tk.TOP, fill=tk.X)
        self.iconbitmap('media\drug.ico')

        img = ImageTk.PhotoImage(Image.open('media\medais.ico'))
        imglabel = tk.Label(image=img)
        imglabel.image = img

    def put_frames(self):
        # ===== Рамки данных =====
        DataFrame = tk.Frame(bd=20, padx=20, relief=tk.RIDGE)
        DataFrame.place(x=50, y=130, width=1100, height=400)

        DataFrameLeft = tk.LabelFrame(DataFrame, bd=10, relief=tk.RIDGE,
                                      padx=10, font=('arial', 12, 'bold'), text='Информация пациента')
        DataFrameLeft.place(x=10, y=5, width=980, height=350)

        DataFrameRight = tk.LabelFrame(DataFrame, bd=10, relief=tk.RIDGE,
                                       padx=10, font=('arial', 12, 'bold'), text='Информация')
        DataFrameRight.place(x=550, y=5, width=460, height=350)
        # ===== Рамка кнопок =====

        self.ButtonFrame = tk.Frame(bd=20, relief=tk.RIDGE)
        self.ButtonFrame.place(x=0, y=550, width=1420, height=70)

        # ===== Рамка описания =====

        DetailsFrame = tk.Frame(bd=20, relief=tk.RIDGE)
        DetailsFrame.place(x=0, y=600, width=1420, height=190)

        # ===== Левая рамка =====

        lblNameTablet = tk.Label(DataFrameLeft, text="Названия",
                                 font=('times new roman', 12, 'bold'), padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0)

    @staticmethod
    def open_add_patient_window():
        AddPatientWindow()


class AddPatientWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("ИАС Диагностика")
        # w = self.winfo_screenwidth()
        # h = self.winfo_screenheight()
        # w = w // 2
        # h = h // 2
        # self.geometry('1000x700+{}+{}'.format(w, h))

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

        tk.Button(self, text="Добавить пациента", width=40, command=self.submit).grid(row=7, column=0)

    def submit(self):
        a = self.fio.get()
        b = self.birth_date.get()
        c = self.phone_number.get()
        d = self.home_address.get()
        e = self.policy.get()
        f = self.sector.get()
        conn = HospitalBase().connection
        cursor = conn.cursor()

        cursor.execute(insert_into_add_patient, (a, b, c, d, e, f))
        conn.commit()


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
