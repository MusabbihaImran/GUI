import tkinter as tk
window=tk.Tk()
window.title("Button Example")
window.geometry("300x200")
def clicked():
    print("Welcome to GUI Programming")
button=tk.Button(window,text="Click Me",command=clicked,width=15)
button.pack()
window.mainloop()
