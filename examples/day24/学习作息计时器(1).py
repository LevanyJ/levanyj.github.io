import tkinter as tk
import time
import threading

class StudyTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("学习作息计时器")
        self.root.geometry("400x300")
        self.root.config(bg="#e8f4ea")
        self.sec = 0
        self.run = False
        self.label = tk.Label(self.root,text="00:00",font=("微软雅黑",60),bg="#e8f4ea",fg="#3b8c48")
        self.label.pack(pady=30)
        f=tk.Frame(self.root,bg="#e8f4ea")
        f.pack()
        tk.Button(f,text="开始",command=self.start,bg="#88d89c",font=("微软雅黑",14),width=8).grid(row=0,column=0,padx=10)
        tk.Button(f,text="暂停",command=self.pause,bg="#f9d49c",font=("微软雅黑",14),width=8).grid(row=0,column=1,padx=10)
        tk.Button(f,text="重置",command=self.reset,bg="#f29c9c",font=("微软雅黑",14),width=8).grid(row=0,column=2,padx=10)
        self.root.mainloop()

    def count(self):
        while self.run:
            time.sleep(1)
            self.sec +=1
            m = self.sec//60
            s = self.sec%60
            self.label.config(text=f"{m:02d}:{s:02d}")
    def start(self):
        if not self.run:
            self.run=True
            threading.Thread(target=self.count,daemon=True).start()
    def pause(self):
        self.run=False
    def reset(self):
        self.run=False
        self.sec=0
        self.label.config(text="00:00")

if __name__=="__main__":
    StudyTimer()