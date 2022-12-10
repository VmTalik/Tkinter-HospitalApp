from tkinter import Tk


class Hospital:
    def __init__(self, root):
        root.title("")
        w = root.winfo_screenwidth()
        h = root.winfo_screenheight()
        w = w // 2
        h = h // 2
        w = w - 600
        h = h - 450
        root.geometry('1200x800+{}+{}'.format(w, h))


if __name__ == "__main__":
    root = Tk()
    obj = Hospital(root)
    root.mainloop()
