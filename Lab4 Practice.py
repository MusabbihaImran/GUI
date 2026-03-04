"""
import tkinter as tk
window = tk.Tk()
window.title("Practice")
window.geometry("600x500")
label = tk.Label(window, text="Hello, Tkinter!", fg="blue", bg="yellow", padx=10,
pady=5)
label.pack()
button = tk.Button(window, text="Click Me", width=15, command=lambda:
print("Button clicked!"))
button.pack()
window.mainloop()
"""

import tkinter as tk
window1 = tk.Tk()
window1.title("Practice1")
window1.geometry("600x500")
label = tk.Label(window1, text="Initial Text")
label.pack()
current_text = label.cget("text") # Using cget()
print(f"Current text: {current_text}")
current_bg = label.config()["bg"][-1] # Using config() and dictionary access
print(f"Current background: {current_bg}")
window1.mainloop()