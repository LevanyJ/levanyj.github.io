import tkinter as tk
from time import strftime


class FloatClock:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("悬浮时钟")
        self.win.geometry("260x90")
        self.win.attributes("-topmost", True)
        self.win.attributes("-alpha", 0.85)
        self.win.overrideredirect(True)

        self.label = tk.Label(self.win, font=("微软雅黑", 36), bg="#f8d7e3", fg="#d86b9c")
        self.label.pack(expand=True)

        # 绑定拖动
        self.win.bind("<Button-1>", self.start_move)
        self.win.bind("<ButtonRelease-1>", self.stop_move)
        # 右键点击关闭时钟
        self.win.bind("<Button-3>", self.close_clock)

        self.x = None
        self.y = None
        self.time_refresh()
        self.win.mainloop()

    def start_move(self, event):
        self.x = event.x
        self.y = event.y
        # 左键按下先记录坐标，不直接退出
        self.press_time = event.time

    def stop_move(self, event):
        self.x = None
        self.y = None

    def close_clock(self, event):
        # 鼠标右键点击直接退出
        self.win.destroy()

    def time_refresh(self):
        now = strftime("%H:%M:%S")
        self.label.config(text=now)
        self.label.after(1000, self.time_refresh)


if __name__ == "__main__":
    FloatClock()

    # 右键单击则退出