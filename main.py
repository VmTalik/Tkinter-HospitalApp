import tkinter as tk


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


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
