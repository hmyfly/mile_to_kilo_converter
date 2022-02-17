from tkinter import *

def button_clicked():
    km_number = int(input.get()) * 1.6
    string_km_number = str(km_number)
    km_number_label.config(text=km_number)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

# Lable
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)


mile_lable = Label(text="Miles")
mile_lable.grid(column=2, row=0)


km_name_label = Label(text="Km")
km_name_label.grid(column=2, row=1)


km_number_label = Label(text=0)
km_number_label.grid(column=1, row=1)

# Entry
input = Entry(width=10)
input.grid(column=1, row=0)


# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()