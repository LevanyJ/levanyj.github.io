import tkinter as tk
from tkinter import messagebox, filedialog
import time
import threading
import pygame
import os
# 第一行就加这个
import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("智能倒计时器")
        self.root.geometry("680x480")
        self.root.resizable(False, False)

        # 初始化音频
        pygame.mixer.init()
        self.sound_file = None
        self.default_sound = True

        # 状态变量
        self.total_seconds = 0
        self.remaining_seconds = 0
        self.running = False
        self.paused = False
        self.timer_thread = None
        self.is_topmost = False
        self.is_fullscreen = False

        # 马卡龙色系配色
        self.themes = {
            "马卡龙粉": {
                "bg": "#FFF0F5",
                "text": "#FF69B4",
                "btn_confirm": "#FFB6C1",
                "btn_reset": "#87CEFA",
                "btn_pause": "#FFA07A",
                "btn_other": "#E6E6FA"
            },
            "马卡龙蓝": {
                "bg": "#E0F7FA",
                "text": "#00BCD4",
                "btn_confirm": "#80DEEA",
                "btn_reset": "#82B1FF",
                "btn_pause": "#FF8A80",
                "btn_other": "#B388FF"
            },
            "马卡龙绿": {
                "bg": "#E8F5E9",
                "text": "#4CAF50",
                "btn_confirm": "#A5D6A7",
                "btn_reset": "#80CBC4",
                "btn_pause": "#FFCC80",
                "btn_other": "#F48FB1"
            }
        }
        self.current_theme = "马卡龙粉"
        self.apply_theme()

        # 顶部设置区域 分+秒双输入
        self.top_frame = tk.Frame(root, bg=self.bg_color)
        self.top_frame.pack(pady=20)

        self.min_label = tk.Label(self.top_frame, text="分钟：", font=("微软雅黑", 16), bg=self.bg_color, fg=self.text_color)
        self.min_label.pack(side="left", padx=5)
        self.min_entry = tk.Entry(self.top_frame, font=("微软雅黑", 16), width=5, justify="center")
        self.min_entry.pack(side="left", padx=5)
        self.min_entry.insert(0, "1")

        self.sec_label = tk.Label(self.top_frame, text="秒钟：", font=("微软雅黑", 16), bg=self.bg_color, fg=self.text_color)
        self.sec_label.pack(side="left", padx=5)
        self.sec_entry = tk.Entry(self.top_frame, font=("微软雅黑", 16), width=5, justify="center")
        self.sec_entry.pack(side="left", padx=5)
        self.sec_entry.insert(0, "30")

        self.confirm_btn = tk.Button(self.top_frame, text="开始计时", font=("微软雅黑", 16), bg=self.btn_confirm_color, fg="white",
                                     command=self.start_timer, width=8)
        self.confirm_btn.pack(side="left", padx=15)

        # 倒计时大屏显示
        self.time_label = tk.Label(root, text="00:00", font=("微软雅黑", 96), bg=self.bg_color, fg=self.text_color)
        self.time_label.pack(pady=35)

        # 基础控制按钮
        self.btn_frame1 = tk.Frame(root, bg=self.bg_color)
        self.btn_frame1.pack(pady=8)

        self.reset_btn = tk.Button(self.btn_frame1, text="重置", font=("微软雅黑", 16), bg=self.btn_reset_color, fg="white",
                                   command=self.reset_timer, width=10)
        self.reset_btn.grid(row=0, column=0, padx=18)

        self.pause_btn = tk.Button(self.btn_frame1, text="暂停/继续", font=("微软雅黑", 16), bg=self.btn_pause_color, fg="white",
                                   command=self.toggle_pause, width=10)
        self.pause_btn.grid(row=0, column=1, padx=18)

        # 拓展功能按钮
        self.btn_frame2 = tk.Frame(root, bg=self.bg_color)
        self.btn_frame2.pack(pady=12)

        self.topmost_btn = tk.Button(self.btn_frame2, text="窗口置顶", font=("微软雅黑", 12), bg=self.btn_other_color, fg="white",
                                      command=self.toggle_topmost, width=8)
        self.topmost_btn.grid(row=0, column=0, padx=10)

        self.fullscreen_btn = tk.Button(self.btn_frame2, text="全屏显示", font=("微软雅黑", 12), bg=self.btn_other_color, fg="white",
                                         command=self.toggle_fullscreen, width=8)
        self.fullscreen_btn.grid(row=0, column=1, padx=10)

        self.theme_btn = tk.Button(self.btn_frame2, text="切换主题", font=("微软雅黑", 12), bg=self.btn_other_color, fg="white",
                                    command=self.switch_theme, width=8)
        self.theme_btn.grid(row=0, column=2, padx=10)

        self.sound_btn = tk.Button(self.btn_frame2, text="设置提示音", font=("微软雅黑", 12), bg=self.btn_other_color, fg="white",
                                    command=self.set_sound, width=8)
        self.sound_btn.grid(row=0, column=3, padx=10)

    def apply_theme(self):
        theme = self.themes[self.current_theme]
        self.bg_color = theme["bg"]
        self.text_color = theme["text"]
        self.btn_confirm_color = theme["btn_confirm"]
        self.btn_reset_color = theme["btn_reset"]
        self.btn_pause_color = theme["btn_pause"]
        self.btn_other_color = theme["btn_other"]
        self.root.config(bg=self.bg_color)

    def switch_theme(self):
        themes = list(self.themes.keys())
        current_idx = themes.index(self.current_theme)
        next_idx = (current_idx + 1) % len(themes)
        self.current_theme = themes[next_idx]
        self.apply_theme()
        self.top_frame.config(bg=self.bg_color)
        self.min_label.config(bg=self.bg_color, fg=self.text_color)
        self.sec_label.config(bg=self.bg_color, fg=self.text_color)
        self.time_label.config(bg=self.bg_color, fg=self.text_color)
        self.btn_frame1.config(bg=self.bg_color)
        self.btn_frame2.config(bg=self.bg_color)

    def toggle_topmost(self):
        self.is_topmost = not self.is_topmost
        self.root.attributes("-topmost", self.is_topmost)
        self.topmost_btn.config(text="取消置顶" if self.is_topmost else "窗口置顶")

    def toggle_fullscreen(self):
        self.is_fullscreen = not self.is_fullscreen
        self.root.attributes("-fullscreen", self.is_fullscreen)
        self.fullscreen_btn.config(text="退出全屏" if self.is_fullscreen else "全屏显示")

    def set_sound(self):
        file_path = filedialog.askopenfilename(title="选择提示音文件", filetypes=[("音频文件", "*.mp3;*.wav")])
        if file_path:
            self.sound_file = file_path
            self.default_sound = False
            messagebox.showinfo("提示", "提示音设置成功！")

    def play_alarm_sound(self):
        try:
            if self.sound_file and os.path.exists(self.sound_file):
                pygame.mixer.music.load(self.sound_file)
                pygame.mixer.music.play()
            else:
                for _ in range(3):
                    self.root.bell()
                    time.sleep(0.3)
        except Exception as e:
            print(f"播放提示音失败: {e}")

    def start_timer(self):
        if self.running:
            messagebox.showinfo("提示", "倒计时正在进行中，请先重置！")
            return
        try:
            minute = int(self.min_entry.get())
            second = int(self.sec_entry.get())
            # 限制秒数范围0-59
            if second < 0 or second >=60 or minute <0:
                raise ValueError
            self.total_seconds = minute * 60 + second
            self.remaining_seconds = self.total_seconds
            self.running = True
            self.paused = False
            self.update_display()
            self.timer_thread = threading.Thread(target=self.countdown_loop, daemon=True)
            self.timer_thread.start()
        except ValueError:
            messagebox.showerror("错误", "请输入合法数值\n分钟≥0 秒钟范围0~59")

    def countdown_loop(self):
        while self.remaining_seconds > 0 and self.running:
            if not self.paused:
                time.sleep(1)
                self.remaining_seconds -= 1
                self.update_display()
            else:
                time.sleep(0.1)

        if self.remaining_seconds <= 0 and self.running:
            self.time_label.config(text="00:00")
            self.play_alarm_sound()
            self.flash_alert()
            messagebox.showinfo("时间到！", "倒计时结束！")
            self.running = False

    def flash_alert(self):
        original_bg = self.bg_color
        flash_color = "#FFB6C1"
        for _ in range(6):
            self.root.config(bg=flash_color)
            self.time_label.config(fg="white")
            self.root.update()
            time.sleep(0.3)
            self.root.config(bg=original_bg)
            self.time_label.config(fg=self.text_color)
            self.root.update()
            time.sleep(0.3)

    def update_display(self):
        minutes = self.remaining_seconds // 60
        seconds = self.remaining_seconds % 60
        self.time_label.config(text=f"{minutes:02d}:{seconds:02d}")

    def toggle_pause(self):
        if not self.running:
            return
        self.paused = not self.paused
        self.pause_btn.config(text="继续" if self.paused else "暂停")

    def reset_timer(self):
        self.running = False
        self.paused = False
        self.remaining_seconds = 0
        self.time_label.config(text="00:00")
        self.pause_btn.config(text="暂停/继续")

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()