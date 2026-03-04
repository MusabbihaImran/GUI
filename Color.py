import tkinter as tk
window=tk.Tk()
window.geometry("600x500")
window.title("Button")
label=tk.Label(window,text="Initial Text", font=("Arial", 15, "bold"),bg= "purple", fg="pink", padx=10, pady=5)
label.pack()
button=tk.Button(window, text="Enter",font=("Arial", 12, "bold"),bg= "orange", fg="yellow", padx=10, pady=5, width=20, command=lambda:
print("button pressed"), )
button.pack()
current_bg=button.cget("bg")
def change():
    if current_bg=="orange":
        button.config(bg="yellow")
    else:
        button.config(bg="orange")
window.mainloop()




