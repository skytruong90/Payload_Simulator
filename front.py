import tkinter as tk
from tkinter import messagebox

# Import the main application
import main


def display_result():
    username = username_entry.get()
    password = password_entry.get()

    if username == 'admin' and password == 'password':  # replace with your desired credentials
        result_label.config(text="Login successful!")
        root.destroy()  # This will close the login window
        main.create_main_app()  # This will open the main application window
    else:
        messagebox.showerror("Error", "Incorrect username or password")


root = tk.Tk()

# Create a label and entry field for Username
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Create a label and entry field for Password
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create a button that will call the display_result function when clicked
login_button = tk.Button(root, text="Login", command=display_result)
login_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
