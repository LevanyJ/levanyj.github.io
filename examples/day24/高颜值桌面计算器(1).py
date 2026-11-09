import tkinter as tk
import math

class AdvancedCalculator:
    def __init__(self):
        # 主窗口配置
        self.root = tk.Tk()
        self.root.title("多功能计算器")
        self.root.geometry("390x600")
        self.root.config(bg="#f5f1fb")
        self.root.resizable(False, False)  # 固定窗口大小

        # 显示框变量
        self.input_var = tk.StringVar()
        self.input_var.set("")  # 初始为空

        # 显示输入框
        self.create_display()

        # 按钮布局
        self.create_buttons()

        self.root.mainloop()

    def create_display(self):
        """创建显示区域"""
        display = tk.Entry(
            self.root,
            textvariable=self.input_var,
            font=("微软雅黑", 26),
            width=17,
            justify="right",
            bd=8,
            relief=tk.FLAT
        )
        display.pack(pady=20, padx=15)

    def click(self, value):
        """按钮点击核心逻辑"""
        current = self.input_var.get()

        # 清空所有
        if value == "C":
            self.input_var.set("")

        # 删除最后一位
        elif value == "←":
            self.input_var.set(current[:-1])

        # 计算结果
        elif value == "=":
            try:
                # 替换自定义符号，支持平方/立方/根号
                expression = current.replace("²", "**2").replace("³", "**3").replace("√", "math.sqrt(")
                # 根号自动补全括号
                if "math.sqrt(" in expression and not expression.endswith(")"):
                    expression += ")"
                result = str(eval(expression))
                self.input_var.set(result)
            except:
                self.input_var.set("输入错误")

        # 平方根
        elif value == "√":
            self.input_var.set(current + "√")

        # 平方
        elif value == "x²":
            self.input_var.set(current + "²")

        # 三次方
        elif value == "x³":
            self.input_var.set(current + "³")

        # 正负取反
        elif value == "+/-":
            if current:
                if current[0] == "-":
                    self.input_var.set(current[1:])
                else:
                    self.input_var.set("-" + current)

        # 百分号
        elif value == "%":
            try:
                num = float(current)
                self.input_var.set(str(num / 100))
            except:
                self.input_var.set("错误")

        # 普通数字和符号
        else:
            self.input_var.set(current + value)

    def create_buttons(self):
        """创建所有按钮"""
        # 按钮文本（新增了大量功能键）
        button_texts = [
            "C", "←", "√", "/",
            "x²", "x³", "%", "*",
            "7", "8", "9", "-",
            "4", "5", "6", "+",
            "1", "2", "3", "+/-",
            "0", ".", "="
        ]

        # 按钮框架
        btn_frame = tk.Frame(self.root, bg="#f5f1fb")
        btn_frame.pack()

        row = 0
        col = 0
        for text in button_texts:
            # 特殊按钮配色
            bg_color = "#d4b8f5" if text in ["C", "←", "√", "x²", "x³", "%", "+/-"] else "#e9dff5"
            if text in ["=", "/", "*", "-", "+"]:
                bg_color = "#c498e8"

            btn = tk.Button(
                btn_frame,
                text=text,
                font=("微软雅黑", 15),
                width=6,
                height=2,
                bg=bg_color,
                activebackground="#b988e0",
                relief=tk.FLAT,
                command=lambda t=text: self.click(t)
            )
            btn.grid(row=row, column=col, padx=4, pady=4)

            col += 1
            if col > 3:
                col = 0
                row += 1

if __name__ == "__main__":
    AdvancedCalculator()