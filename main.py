import tkinter as tk
from PIL import ImageTk, Image


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
        pass


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
