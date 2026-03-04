import tkinter as tk
window=tk.Tk()
window.title("Binding")
window.geometry("600x500")
def handle_click(event):
    print(f"Button clicked at X={event.x}, Y={event.y}")
    print("Left Click")
    button.config(bg="green")
def handle_right_click(event):
    print(f"Button clicked at X={event.x}, Y={event.y}")
    print("Right Click")
    button.config(bg="red")
def handle_key(event):
    print(f"Key pressed:{event.char}")
button=tk.Button(window, text="Click me")
button.pack()
entry=tk.Entry(window)
entry.pack()
button.bind("<Button-1>",handle_click)
button.bind("<Button-3>",handle_right_click)
entry.bind("<Key>", handle_key)
window.mainloop()
