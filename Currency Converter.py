from tkinter import *
from tkinter.ttk import LabelFrame
from tkinter import messagebox
from forex_python.converter import CurrencyRates, CurrencyCodes
from time import strftime

cc = CurrencyRates()

cs = CurrencyCodes()

screen = Tk()

screen.title('                                                      Currency Converter')
screen.iconbitmap("cc.ico")

w =500
h =480
sw = screen.winfo_screenwidth()
sh = screen.winfo_screenheight()
x = (sw/2)-(w/2)
y = (sh/2)-(h/2)
screen.geometry("%dx%d+%d+%d" % (w,  h, x, y))
screen.resizable(False, False)



currency_frame = Frame(screen)
currency_frame.pack(fill='both', expand=1)

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)


lbl = Label(currency_frame, font=('rosemary', 12, 'bold'))

lbl.place(x=210)
time()



l = LabelFrame(currency_frame, text='Convert')
l.pack(pady=20)
f = Label(l, text='From...', font=('rosemary', 15, 'bold', 'italic'))
f.pack(pady=10)
f_entry = Entry(l, width=60)
f_entry.pack(pady=10, padx=10)


t = Label(l, text='To...', font=('rosemary', 15, 'bold', 'italic'))
t.pack(pady=10)
t_entry = Entry(l, width=60)
t_entry.pack(pady=10, padx=10)
am = Label(l, text='Amount...', font=('rosemary', 15, 'bold', 'italic'))

am.pack(pady=10)
am_entry = Entry(l, width=60)
am_entry.pack(pady=10, padx=10)

button_frame = Frame(currency_frame)
button_frame.pack(pady=10)





def clear():
    f_entry.delete(0, END)
    t_entry.delete(0, END)
    am_entry.delete(0, END)
    res_out.delete(0, END)


def close():
    screen.destroy()


res = LabelFrame(currency_frame, text='Result...')
res.pack(pady=5)

res_out = Entry(res, width=42, font=('arial', 12, 'bold'), bd=0, bg='systembuttonface')
res_out.pack(pady=10)


def calculate():
    if len(f_entry.get()) == 0:
        messagebox.showwarning('Warning!', '"From" Entry is not filled')
    elif len(t_entry.get()) == 0:
        messagebox.showwarning('Warning!', '"To" Entry is not filled')
    elif len(am_entry.get()) == 0:
        messagebox.showwarning('Warning!', 'Amount is not filled')
    else:
        res_out.delete(0, END)
        amount = am_entry.get()
        amount = float(amount)
        conversion = cc.convert( f_entry.get(), t_entry.get(), amount)
        symbol= t_entry.get()
        s = cs.get_symbol(symbol)
        res_out.insert(0, s)
        res_out.insert(5, string= f" {conversion}")



calc = Button(button_frame, text='Calculate', width=10, command=calculate)
calc.grid(row=1, column=0,padx=10)
Button(button_frame,text='Clear', width=10, command=clear).grid(row=1, column=1, padx=10)

Button(currency_frame,text='Close', width=10, command=close).pack()

screen.mainloop()
