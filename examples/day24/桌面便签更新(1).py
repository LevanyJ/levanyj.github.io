import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog, messagebox  # 必须导入

class NotePad:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("桌面便签")
        self.win.geometry("380x600")
        self.win.config(bg="#fff6d9")
        self.win.attributes("-topmost", True)  # 窗口置顶

        # 标题
        tk.Label(self.win, text="随身备忘录", font=("微软雅黑", 16),
                 bg="#fff6d9", fg="#c4934a").pack(pady=8)

        # 文本编辑区
        self.text = ScrolledText(self.win, font=("微软雅黑", 12),
                                 width=40, height=22, bg="#fffbe8")
        self.text.pack(pady=5)

        # 按钮区域
        btn_frame = tk.Frame(self.win, bg="#fff6d9")
        btn_frame.pack(pady=8)

        # 导出TXT按钮
        tk.Button(btn_frame, text="导出TXT", font=("微软雅黑", 12),
                  bg="#f9d59b", width=10, command=self.save_file).grid(row=0, column=0, padx=8)

        # 清空重置按钮
        tk.Button(btn_frame, text="清空重置", font=("微软雅黑", 12),
                  bg="#f2b86f", width=10, command=self.clear_text).grid(row=0, column=1, padx=8)

        self.win.mainloop()

    def save_file(self):
        """导出内容为TXT文件，自选保存位置"""
        content = self.text.get("1.0", tk.END)

        # 选择保存路径
        file_path = filedialog.asksaveasfilename(
            title="保存便签",
            defaultextension=".txt",
            filetypes=[("文本文档", "*.txt"), ("所有文件", "*.*")]
        )

        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                messagebox.showinfo("成功", "便签导出成功！")
            except Exception as e:
                messagebox.showerror("失败", f"保存出错：{str(e)}")

    def clear_text(self):
        """一键清空内容"""
        self.text.delete("1.0", tk.END)
        # messagebox.showinfo("提示", "内容已清空！")

if __name__ == "__main__":
    NotePad()