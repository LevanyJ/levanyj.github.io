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

        # ========== 核心修改：替换背景色 ==========
        # 主窗口背景改为柔和的浅米色（可自行调整）
        self.root.config(bg="#f8f5f0")

        # 标题（调整文字颜色适配新背景）
        tk.Label(self.root, text="六合一实用工具中心", font=("微软雅黑", 22, "bold"),
                 bg="#f8f5f0",  # 标题标签背景和主窗口一致
                 fg="#8b5a2b").pack(pady=25)  # 文字改为暖棕色

        # 按钮布局 2行3列（修改框架背景）
        frame = tk.Frame(self.root, bg="#f8f5f0")  # 按钮框架背景和主窗口一致
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
                # ========== 优化按钮样式（可选） ==========
                btn = tk.Button(
                    frame,
                    text=name,
                    font=("微软雅黑", 13),
                    width=14,
                    height=3,
                    bg="#e8d9c5",  # 按钮背景改为浅卡其色
                    fg="#5a3e2b",  # 按钮文字改为深棕色
                    relief=tk.RAISED,  # 按钮样式改为凸起（替换原有的RIDGE）
                    bd=2,  # 按钮边框宽度
                    command=lambda f=filename: self.run_tool(f)
                )
                btn.grid(row=row, column=col, padx=12, pady=12)
                index += 1

        # 底部提示文字（调整背景和文字色）
        tk.Label(self.root, text="点击按钮快速启动对应工具", font=("微软雅黑", 10),
                 bg="#f8f5f0", fg="#665443").pack(pady=15)

        self.root.mainloop()

    def run_tool(self, file_name):
        """运行对应py工具 —— 无黑窗口版"""
        if not os.path.exists(file_name):
            messagebox.showerror("提示", f"未找到 {file_name} 文件\n请将所有工具放在同一文件夹！")
            return

        # 👇 这三行是去掉黑窗口的核心代码
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE

        try:
            # 调用时带上 startupinfo
            subprocess.Popen(["pythonw", file_name], startupinfo=startupinfo)
        except Exception as e:
            messagebox.showerror("启动失败", str(e))


if __name__ == "__main__":
    ToolHomePage()