import pyautogui
import tkinter as tk
from tkinter import messagebox, filedialog, Toplevel
import time
import os
from datetime import datetime
from PIL import ImageGrab


class ScreenShotTool:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("桌面截图工具")
        self.root.geometry("380x320")
        self.root.resizable(0, 0)
        self.root.config(bg="#e1f5f2")

        self.save_path = tk.StringVar(value=os.getcwd())
        self.start_x = None
        self.start_y = None
        self.rect = None

        tk.Label(self.root, text="Python简易截图工具", font=("微软雅黑", 18),
                 bg="#e1f5f2", fg="#267365").pack(pady=15)

        tk.Label(self.root, text="保存路径：", bg="#e1f5f2", font=("微软雅黑", 11)).pack()
        path_frame = tk.Frame(self.root, bg="#e1f5f2")
        path_frame.pack(pady=5)

        tk.Entry(path_frame, textvariable=self.save_path, width=28,
                 font=("微软雅黑", 11), state="readonly").pack(side=tk.LEFT, padx=5)
        tk.Button(path_frame, text="选择路径", font=("微软雅黑", 11),
                  bg="#78d6c5", command=self.select_path).pack(side=tk.LEFT)

        btn_frame = tk.Frame(self.root, bg="#e1f5f2")
        btn_frame.pack(pady=18)

        tk.Button(btn_frame, text="全屏截图", font=("微软雅黑", 14),
                  bg="#78d6c5", width=10, command=self.full_shot).grid(row=0, column=0, padx=8)
        tk.Button(btn_frame, text="选区截图", font=("微软雅黑", 14),
                  bg="#59c9b8", width=10, command=self.area_shot).grid(row=0, column=1, padx=8)

        tk.Label(self.root, text="📌 选区截图：拖动鼠标框选", bg="#e1f5f2", font=("微软雅黑", 11)).pack()
        tk.Label(self.root, text="📌 文件名：年月日_时分秒.png", bg="#e1f5f2", font=("微软雅黑", 11)).pack(pady=2)

        self.root.mainloop()

    def select_path(self):
        path = filedialog.askdirectory(title="选择截图保存位置")
        if path:
            self.save_path.set(path)

    def get_save_file(self):
        now = datetime.now()
        time_str = now.strftime("%Y%m%d_%H%M%S")
        return os.path.join(self.save_path.get(), f"截图_{time_str}.png")

    def full_shot(self):
        self.root.iconify()
        time.sleep(0.3)
        try:
            img = pyautogui.screenshot()
            save_file = self.get_save_file()
            img.save(save_file)
            messagebox.showinfo("✅ 完成", f"全屏截图保存成功！\n{save_file}")
        except Exception as e:
            messagebox.showerror("❌ 错误", str(e))
        self.root.deiconify()

    # ==================== 修复后的选区截图 ====================
    def area_shot(self):
        self.root.iconify()
        time.sleep(0.3)

        # 创建全屏透明覆盖层，用于框选
        self.canvas = Toplevel()
        self.canvas.attributes('-fullscreen', True, '-alpha', 0.3)
        self.canvas.config(bg='black')
        self.canvas.overrideredirect(True)
        self.canvas.focus_set()

        self.screen = tk.Canvas(self.canvas, bg='black', highlightthickness=0)
        self.screen.pack(fill='both', expand=True)

        # 绑定鼠标事件
        self.screen.bind('<ButtonPress-1>', self.on_press)
        self.screen.bind('<B1-Motion>', self.on_drag)
        self.screen.bind('<ButtonRelease-1>', self.on_release)
        self.canvas.mainloop()

    def on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.screen.create_rectangle(0, 0, 0, 0, outline='red', width=2)

    def on_drag(self, event):
        self.screen.coords(self.rect, self.start_x, self.start_y, event.x, event.y)

    def on_release(self, event):
        self.canvas.destroy()
        try:
            x1, y1 = min(self.start_x, event.x), min(self.start_y, event.y)
            x2, y2 = max(self.start_x, event.x), max(self.start_y, event.y)

            img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
            save_file = self.get_save_file()
            img.save(save_file)
            messagebox.showinfo("✅ 完成", f"选区截图保存成功！\n{save_file}")
        except Exception as e:
            messagebox.showerror("❌ 错误", str(e))
        self.root.deiconify()


if __name__ == "__main__":
    ScreenShotTool()