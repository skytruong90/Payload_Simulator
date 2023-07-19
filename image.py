import tkinter as tk

root = tk.Tk()

# Frame to contain the buttons.
button_frame = tk.Frame(root)
# place frame at the center bottom
button_frame.place(relx=0.5, rely=0.9, anchor='center')

# Create a "Zoom In" button
# replace 'command=None' with the actual function you want to call
zoom_in_button = tk.Button(button_frame, text="Zoom In", command=None)
# Button with padding to the left and right
zoom_in_button.pack(side="left", padx=10)

# Create a "Zoom Out" button
# replace 'command=None' with the actual function you want to call
zoom_out_button = tk.Button(button_frame, text="Zoom Out", command=None)
# Button with padding to the left and right
zoom_out_button.pack(side="left", padx=10)

root.mainloop()
