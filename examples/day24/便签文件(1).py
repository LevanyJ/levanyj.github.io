import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog, messagebox
import os
import sys

class NotePad:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("桌面便签")
        self.win.geometry("380x600")
        self.win.config(bg="#fff6d9")
        self.win.attributes("-topmost", True)

        # 自动保存文件路径
        self.auto_save_path = "note_auto_save.txt"

        # 标题
        tk.Label(self.win, text="随身备忘录", font=("微软雅黑", 16),
                 bg="#fff6d9", fg="#c4934a").pack(pady=8)

        # 文本框
        self.text = ScrolledText(self.win, font=("微软雅黑", 12),
                                 width=40, height=22, bg="#fffbe8")
        self.text.pack(pady=5)

        # 按钮区域
        btn_frame = tk.Frame(self.win, bg="#fff6d9")
        btn_frame.pack(pady=6)

        tk.Button(btn_frame, text="导出TXT", font=("微软雅黑", 11),
                  bg="#f9d59b", width=9, command=self.save_file).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="清空重置", font=("微软雅黑", 11),
                  bg="#f2b86f", width=9, command=self.clear_text).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="开启自启", font=("微软雅黑", 11),
                  bg="#a2e8b8", width=9, command=self.set_startup).grid(row=0, column=2, padx=5)

        # 加载上次自动保存内容
        self.load_auto_text()
        # 绑定关闭事件，退出自动保存
        self.win.protocol("WM_DELETE_WINDOW", self.quit_save)
        # 定时自动保存 3秒一次
        self.auto_save_loop()

        self.win.mainloop()

    # 定时自动保存
    def auto_save_loop(self):
        content = self.text.get("1.0", tk.END)
        with open(self.auto_save_path, "w", encoding="utf-8") as f:
            f.write(content)
        self.win.after(3000, self.auto_save_loop)

    # 读取自动保存文件
    def load_auto_text(self):
        if os.path.exists(self.auto_save_path):
            with open(self.auto_save_path, "r", encoding="utf-8") as f:
                data = f.read()
            self.text.insert("1.0", data)

    # 关闭窗口先保存再退出
    def quit_save(self):
        content = self.text.get("1.0", tk.END)
        with open(self.auto_save_path, "w", encoding="utf-8") as f:
            f.write(content)
        self.win.destroy()

    # 手动导出TXT
    def save_file(self):
        content = self.text.get("1.0", tk.END)
        file_path = filedialog.asksaveasfilename(
            title="另存为文本文件",
            defaultextension=".txt",
            filetypes=[("文本文档", "*.txt"), ("所有文件", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                messagebox.showinfo("提示", "导出成功！")
            except:
                messagebox.showerror("错误", "保存失败")

    # 清空内容
    def clear_text(self):
        self.text.delete("1.0", tk.END)

    # 设置Windows开机自启动
    def set_startup(self):
        try:
            # 获取程序绝对路径
            exe_path = os.path.abspath(sys.argv[0])
            # 写入注册表实现开机自启
            import winreg
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                 r"Software\Microsoft\Windows\CurrentVersion\Run",
                                 0, winreg.KEY_WRITE)
            winreg.SetValueEx(key, "DesktopNote", 0, winreg.REG_SZ, exe_path)
            winreg.CloseKey(key)
            messagebox.showinfo("成功", "已设置开机自动启动！")
        except Exception as e:
            messagebox.showerror("失败", f"设置失败：{str(e)}")

if __name__ == "__main__":
    NotePad()