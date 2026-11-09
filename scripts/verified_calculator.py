"""Day24 learning exercise: a measured UI/logic revision of the course calculator.

The original course version is preserved separately. This version fixes clipped
buttons and restricts arithmetic instead of evaluating arbitrary Python input.
Run: python scripts/verified_calculator.py
"""
import ast
import math
import tkinter as tk


def arithmetic(expression: str) -> float:
    """Evaluate numbers and +, -, *, /, **, unary signs, sqrt only."""
    tree = ast.parse(expression, mode="eval")
    def step(node):
        if isinstance(node, ast.Expression): return step(node.body)
        if isinstance(node, ast.Constant) and type(node.value) in (int, float): return float(node.value)
        if isinstance(node, ast.UnaryOp) and isinstance(node.op,(ast.UAdd,ast.USub)):
            v=step(node.operand)
            return v if isinstance(node.op,ast.UAdd) else -v
        if isinstance(node, ast.BinOp) and isinstance(node.op,(ast.Add,ast.Sub,ast.Mult,ast.Div,ast.Pow)):
            a,b=step(node.left),step(node.right)
            if isinstance(node.op,ast.Add):return a+b
            if isinstance(node.op,ast.Sub):return a-b
            if isinstance(node.op,ast.Mult):return a*b
            if isinstance(node.op,ast.Div):return a/b
            if isinstance(node.op,ast.Pow):
                if abs(b)>8 or abs(a)>1e6:raise ValueError('power out of bounds')
                return a**b
        if isinstance(node,ast.Call) and isinstance(node.func,ast.Name) and node.func.id=='sqrt' and not node.keywords and len(node.args)==1:
            return math.sqrt(step(node.args[0]))
        raise ValueError('Unsupported expression')
    result=step(tree)
    if not math.isfinite(result):raise ValueError('Non-finite')
    return result


class Calculator:
    def __init__(self, root=None):
        self.root=root or tk.Tk()
        self.root.title('Python Calculator · Verified Revision')
        self.root.geometry('480x610')
        self.root.minsize(420,520)
        self.root.configure(bg='#f2ebfa')
        self.value=tk.StringVar(value='')
        screen=tk.Entry(self.root,textvariable=self.value,font=('Arial',25),justify='right',bd=0,relief='flat')
        screen.pack(fill='x',padx=20,pady=(24,22),ipady=18)
        body=tk.Frame(self.root,bg='#f2ebfa');body.pack(fill='both',expand=True,padx=16,pady=(0,24))
        for i in range(4):body.columnconfigure(i,weight=1,uniform='col')
        for i in range(6):body.rowconfigure(i,weight=1,uniform='row')
        keys=[['C','←','√','/'],['x²','x³','%','*'],['7','8','9','-'],['4','5','6','+'],['1','2','3','+/-'],['0','.','=','']]
        for r,line in enumerate(keys):
            for c,key in enumerate(line):
                if not key:continue
                special=key in ('C','←','√','x²','x³','%','+/-')
                bg='#dac4f2' if special else ('#c6a6ec' if key in ('=','+','-','/','*') else '#f8f4fc')
                tk.Button(body,text=key,font=('Arial',16),bg=bg,relief='flat',command=lambda v=key:self.press(v)).grid(row=r,column=c,sticky='nsew',padx=4,pady=4)
    def press(self,key):
        s=self.value.get()
        if key=='C':self.value.set('');return
        if key=='←':self.value.set(s[:-1]);return
        if key=='√':self.value.set(s+'√');return
        if key=='x²':self.value.set(s+'²');return
        if key=='x³':self.value.set(s+'³');return
        if key=='+/-':self.value.set(s[1:] if s.startswith('-') else '-'+s if s else '-');return
        if key=='%':
            try:self.value.set(str(float(s)/100))
            except(ValueError,ZeroDivisionError):self.value.set('输入错误')
            return
        if key=='=':
            try:
                e=s.replace('²','**2').replace('³','**3').replace('√','sqrt(')
                if 'sqrt(' in e and not e.endswith(')'):e+=')'
                value=arithmetic(e)
                self.value.set(str(int(value)) if value.is_integer() else str(round(value,10)))
            except(Exception):self.value.set('输入错误')
            return
        self.value.set(s+key)

if __name__=='__main__':Calculator().root.mainloop()
