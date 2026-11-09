import tkinter as tk
from tkinter import messagebox
import os
import subprocess

class ToolHomePage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("实用小工具合集")
        self.root.geometry("520x400")
        self.root.resizable(False, False)
        self.root.config(bg="#f0f7ff")

        # 标题
        tk.Label(self.root, text="六合一实用工具中心", font=("微软雅黑", 22, "bold"),
                 bg="#f0f7ff", fg="#2b5b9c").pack(pady=25)

        # 按钮布局 2行3列
        frame = tk.Frame(self.root, bg="#f0f7ff")
        frame.pack()

        # 工具名称 + 对应py文件名
        tool_list = [
            ("多功能计算器", "高颜值桌面计算器.py"),
            ("全屏选区截图", "简易截图工具.py"),
            ("置顶桌面便签", "便签文件.py"),
            ("倒计时小工具", "倒计时小工具.py"),
            ("学习作息计时器", "学习作息计时器.py"),
            ("悬浮时钟", "桌面悬浮时钟.py")
        ]

        index = 0
        for row in range(2):
            for col in range(3):
                name, filename = tool_list[index]
                btn = tk.Button(
                    frame,
                    text=name,
                    font=("微软雅黑", 13),
                    width=14,
                    height=3,
                    bg="#82b1ff",
                    relief=tk.RIDGE,
                    command=lambda f=filename:self.run_tool(f)
                )
                btn.grid(row=row, column=col, padx=12, pady=12)
                index += 1

        tk.Label(self.root, text="点击按钮快速启动对应工具", font=("微软雅黑", 10),
                 bg="#f0f7ff", fg="#666666").pack(pady=15)

        self.root.mainloop()

    def run_tool(self, file_name):
        """运行对应py工具"""
        if not os.path.exists(file_name):
            messagebox.showerror("提示", f"未找到 {file_name} 文件\n请将所有工具放在同一文件夹！")
            return
        try:
            subprocess.Popen(["python", file_name])
        except:
            try:
                subprocess.Popen(["python3", file_name])
            except Exception as e:
                messagebox.showerror("启动失败", str(e))

if __name__ == "__main__":
    ToolHomePage()