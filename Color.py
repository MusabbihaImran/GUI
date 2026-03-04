import tkinter as tk
window=tk.Tk()
window.geometry("600x500")
window.title("Button")
def change():
    current_bg = button.cget("bg")
    if current_bg=="orange":
        button.config(bg="yellow")
    else:
        button.config(bg="orange")
label=tk.Label(window,text="Initial Text", font=("Arial", 15, "bold"),bg= "purple", fg="pink", padx=10, pady=5)
label.pack()
button=tk.Button(window, text="Enter",font=("Arial", 12, "bold"),bg= "orange", fg="black", padx=10, pady=5, width=20, command=change )
button.pack()
window.mainloop()




