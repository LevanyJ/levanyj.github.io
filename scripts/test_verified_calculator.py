import importlib.util,json,hashlib,pathlib,tkinter as tk,time
from PIL import ImageGrab
rootdir=pathlib.Path(__file__).resolve().parents[1];source=rootdir/'scripts/verified_calculator.py'
spec=importlib.util.spec_from_file_location('verified_calc',source);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
root=tk.Tk();app=m.Calculator(root);root.update()
cases=[(['1','2','+','3','0','='],'42'),(['5','x²','='],'25'),(['√','8','1','='],'9'),(['2','0','%'],'0.2'),(['9','/','0','='],'输入错误')]
tests=[]
for keys,expected in cases:
 app.value.set('')
 for key in keys:app.press(key)
 actual=app.value.get();tests.append({'operation':''.join(keys),'expected':expected,'actual':actual,'passed':actual==expected})
app.value.set('');[app.press(k) for k in cases[0][0]];root.update();time.sleep(.15)
x,y=root.winfo_rootx(),root.winfo_rooty();w,h=root.winfo_width(),root.winfo_height()
ImageGrab.grab(bbox=(x,y,x+w,y+h)).convert('RGB').save(rootdir/'verified_calculator.jpg',quality=78,optimize=True)
checks={'test_environment':'Python Tkinter on Linux Xvfb','subject':'Day24 verified calculator revision','source':'scripts/verified_calculator.py','tests':tests,'passed':sum(t['passed'] for t in tests),'total':len(tests),'note':'Real Tk window screenshot from the executed revised code; Windows packaged EXE is not validated.'}
(rootdir/'data/verified_calculator_checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding='utf-8')
print(checks['passed'],checks['total'],(rootdir/'verified_calculator.jpg').stat().st_size)
root.destroy()
