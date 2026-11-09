import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class NotePad:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("桌面便签")
        self.win.geometry("350x420")
        self.win.config(bg="#fff6d9")
        self.win.attributes("-topmost",True)

        tk.Label(self.win,text="随身备忘录",font=("微软雅黑",16),bg="#fff6d9",fg="#c4934a").pack(pady=8)
        self.text = ScrolledText(self.win,font=("微软雅黑",12),width=38,height=22,bg="#fffbe8")
        self.text.pack()
        self.win.mainloop()

if __name__=="__main__":
    NotePad()