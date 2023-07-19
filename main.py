import tkinter as tk


def display_result():
    result_text = f"Position: {pos_entry.get()}, Velocity: {vel_entry.get()}, Time: {time_entry.get()}, Time Pass: {tp_entry.get()}"
    result_label.config(text=result_text)


def create_main_app():
    # Make these variables global so they can be accessed in display_result function
    global pos_entry, vel_entry, time_entry, tp_entry, result_label

    root = tk.Tk()

    # Create a label and entry field for Position
    pos_label = tk.Label(root, text="Position:")
    pos_label.pack()
    pos_entry = tk.Entry(root)
    pos_entry.pack()

    # Create a label and entry field for Velocity
    vel_label = tk.Label(root, text="Velocity:")
    vel_label.pack()
    vel_entry = tk.Entry(root)
    vel_entry.pack()

    # Create a label and entry field for Time
    time_label = tk.Label(root, text="Time:")
    time_label.pack()
    time_entry = tk.Entry(root)
    time_entry.pack()

    # Create a label and entry field for Time Pass
    tp_label = tk.Label(root, text="Time Pass:")
    tp_label.pack()
    tp_entry = tk.Entry(root)
    tp_entry.pack()

    # Create a button that will call the display_result function when clicked
    run_button = tk.Button(root, text="Run", command=display_result)
    run_button.pack()

    # Create a label to display the result
    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()
