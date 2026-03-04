import tkinter as tk
window=tk.Tk()
window.title("Login Page")
window.geometry("500x500")
def dashboard():
    dash=tk.Toplevel()
    dash.title("Dashboard")
    dash.geometry("400x300")
    label=tk.Label(dash,text="Welcome to Dashboard", font=("Times new roman",16,"bold"))
    label.pack()
def clicked():
    if(entry_password.get()=="1234") & (entry_username.get()=="admin"):
        status.config(text="Login Successful!")
        dashboard()
    else:
        status.config(text="Login Failed!")

login=tk.Label(window,text="Welcome, Login", font=("Times new roman", 16, "bold"), bg="light blue" , fg="blue")
login.pack()
username=tk.Label(window,text="Username", font=("Times new roman", 12, "bold"), bg="white" , fg="blue")
username.pack()
entry_username=tk.Entry(window,width=50)
entry_username.pack()
password=tk.Label(window,text="Password", font=("Times new roman", 12, "bold"), bg="white" , fg="blue")
password.pack()
entry_password=tk.Entry(window,width=50)
entry_password.pack()
button=tk.Button(window, text="Login", command=clicked, width=14, font=("Arial",10), bg="light blue", fg="blue")
button.pack()
status=tk.Label(window,text= "")
status.pack()
window.mainloop()
