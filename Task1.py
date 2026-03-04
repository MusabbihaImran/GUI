import tkinter as tk
window=tk.Tk()
window.title("Temperature Converter")
window.geometry("400x300")
def c_to_f():
    try:
        c=float(entry.get())
        f=(c*9/5)+32
        result.config(text=str(f)+" °F")
    except:
        result.config(text="Invalid Input")
def f_to_c():
    try:
        f=float(entry.get())
        c=(f-32)*5/9
        result.config(text=str(c)+" °C")
    except:
        result.config(text="Invalid Input")
label=tk.Label(window,text="Enter Temperature")
label.pack()
entry=tk.Entry(window,width=30)
entry.pack()
button1=tk.Button(window,text="Celsius to Fahrenheit",command=c_to_f)
button1.pack()
button2=tk.Button(window,text="Fahrenheit to Celsius",command=f_to_c)
button2.pack()
result=tk.Label(window,text="")
result.pack()
window.mainloop()
