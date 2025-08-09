from tkinter import *

def miles_to_km():
    miles = float(input.get())
    km = miles * 1.609
    label_3.config(text=f"{km}")


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300,height=100)
window.config(padx=20,pady=20)

#entry, labels, button

input = Entry(width=10)
input.grid(column=1,row=0)

label_1 = Label(text="Miles")
label_1.grid(column=2,row=0)

label_2 = Label(text="is equal to")
label_2.grid(column=0,row=1)

label_3 = Label(text="0")
label_3.grid(column=1,row=1)

label_4 = Label(text="Km")
label_4.grid(column=2,row=1)

button = Button(text="Calculate",command=miles_to_km)
button.grid(column=1,row=2)



window.mainloop()