import tkinter as tk
window=tk.Tk()
window.title("Multiple Labels")
window.geometry("400x300")
label1=tk.Label(window,text="Hello Students", font=("Times new roman",16,"bold"), fg="blue")
label1.pack()
label2=tk.Label(window,text="GUI Programming", font=("Arial",14), fg="green")
label2.pack()
label3=tk.Label(window,text="Tkinter Library", font=("Calibri",12,"italic"), fg="red")
label3.pack()

window.mainloop()
