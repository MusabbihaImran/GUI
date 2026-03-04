import tkinter as tk
window=tk.Tk()
window.title("Entry Example")
window.geometry("400x300")
def show_text():
    status.config(text=entry.get())
entry=tk.Entry(window,width=40)
entry.pack()
button=tk.Button(window,text="Show Text",command=show_text)
button.pack()
status=tk.Label(window,text="")
status.pack()
window.mainloop()
