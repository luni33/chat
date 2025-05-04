from customtkinter import *

window = CTk()

resuit = CTkEntry(window, height=30)
resuit. pack(fill="x" )

frame = CTkFrame(window)
frame . pack()

button_1 = CTkButton(frame, text="1" , width=80, height=80)
button_1.grid(row=0,column=0)

button_2 = CTkButton(frame, text="2")
button_2.grid(row=0,column=1)

button_3 = CTkButton(frame, text="3")
button_3.grid(row=0,column=2)

button_4 = CTkButton(frame, text="/")
button_4.grid(row=0,column=3)

window.mainloop()