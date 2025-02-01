import matplotlib.pyplot as plt
import tkinter as ttk
import json
import os 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

win = ttk.Tk()
win.title('Collatz Paradox: Visual')

if os.path.isdir('data'):
    with open('data/config.json') as f:
        win.geometry(json.load(f))
else:
    os.makedirs('data')
    with open('data/config.json', 'w') as f:
        win.geometry('800x600')
        json.dump('800x600',f)

win.minsize(800,600)
win.iconbitmap('3x+1_icon.ico')
plt_frame =  ttk.Frame(win)
plt_frame.pack(side='left', expand='yes', fill='both')

def on_close():
    if os.path.isdir('data'):
        with open('data/config.json', 'w') as f:
            x = win.geometry()
            json.dump(x,f)
    else:
        os.makedirs('data')
        with open('data/config.json'):
            x = win.geometry()
            json.dump(x, f)
    win.destroy()

def build_graph(x):
    global plt_frame
    
    plt_frame.destroy()
    
    plt_frame =  ttk.Frame(win)
    plt_frame.pack(side='left', expand='yes', fill='both')
    try:
        x = int(a.get())
        y = [x]
        while x != 1:
            if x % 2 == 0:
                x = x/2
                y.append(x)
            else:
                x = 3*x +1
                y.append(x)

        fig1 = plt.Figure(figsize=(7,6), dpi=100)
        ax1 = fig1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(fig1,plt_frame)
        bar1.get_tk_widget().pack(side='left', expand='yes', fill='both')
        ax1.plot(y, c ='red', linewidth=4)
        
    except ValueError:
        text1.configure(text='Enter a number please')
    
win.protocol('WM_DELETE_WINDOW', on_close)
win.bind('<Return>', build_graph)

a = ttk.StringVar()

frame = ttk.Frame(win, bg='white')
frame.pack(side='right', fill='both', expand='yes')

text1 =  ttk.Label(frame,text="Enter X and press the 'Plot' button:",width =20 ,
                   font=('helvatica' ,30),bg ='white')
text1.pack(expand='yes', fill='x')

entry = ttk.Entry(frame,width= 20 ,font=('helvatica', 50),
                  bg ='white', textvariable=a, bd=3)
entry.pack(expand='yes', fill='x',pady=75)
entry.focus()

plot_btn = ttk.Button(frame, text='Plot', cursor='hand2',
                      bd=2, bg='white', command=lambda:build_graph(2), font=('helvatica, 25'))
plot_btn.pack(expand='yes', fill='both',pady=125, padx=300)


win.mainloop()