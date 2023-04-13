import tkinter as tk

window = tk.Tk()
window.title("Midterm Exam Problem 2")

given_name_label = tk.Label(window, text="Enter Given Name:")
given_name_entry = tk.Entry(window)

middle_name_label = tk.Label(window, text="Enter Middle Name:")
middle_name_entry = tk.Entry(window)

last_name_label = tk.Label(window, text="Enter Last Name:")
last_name_entry = tk.Entry(window)

def show_full_name():
    full_name = given_name_entry.get() + " " + middle_name_entry.get() + " " + last_name_entry.get()
    full_name_entry.delete(0, tk.END)
    full_name_entry.insert(0, full_name)

show_button = tk.Button(window, text="Show Full Name", command=show_full_name)

full_name_label = tk.Label(window, text="My Full Name is:")
full_name_entry = tk.Entry(window)

given_name_label.grid(row=0, column=0)
given_name_entry.grid(row=0, column=1)

middle_name_label.grid(row=1, column=0)
middle_name_entry.grid(row=1, column=1)

last_name_label.grid(row=2, column=0)
last_name_entry.grid(row=2, column=1)

show_button.grid(row=3, column=0)

full_name_label.grid(row=4, column=0)
full_name_entry.grid(row=4, column=1)


window.mainloop()
