from tkinter import *

window = Tk()
window.title("Simple Interest Calculator")
window.geometry("400x400")

principle = Label(window, text="Principle Amount: ")
principle.entry = Entry(window)
rate = Label(window, text="Rate of Interest:")
rate.entry = Entry(window)
time = Label(window, text="Time Period in Years: ")
time.entry = Entry(window)

def calculate():
    p = float(principle.entry.get())
    r = float(rate.entry.get())
    t = float(time.entry.get())
    si = (p * r * t) / 100
    result_label.config(text=f"Simple Interest: {si}")

calculate_button = Button(window, text="Calculate", command=calculate)
result_label = Label(window, text="Simple Interest: ")

principle.pack()
principle.entry.pack()
rate.pack()
rate.entry.pack()
time.pack()
time.entry.pack()


calculate_button.pack()
result_label.pack()


window.mainloop()