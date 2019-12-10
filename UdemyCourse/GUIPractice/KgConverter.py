from tkinter import *

#Creates GUI window
window = Tk()

#Function to convert kg to g,lb, and oz
def kgConvert():
    #Finds the conversion value, deletes the previous value from the text widgets
    grams = float(entryValue.get())*1000
    g.delete("1.0",END)
    g.insert(END, grams)

    pounds = float(entryValue.get())*2.20462
    lb.delete("1.0",END)
    lb.insert(END, pounds)

    ounces = float(entryValue.get())*35.274
    oz.delete("1.0",END)
    oz.insert(END, ounces)



#Creates execute button and dictates its location
btn1 = Button(window, text="Convert", command=kgConvert)
btn1.grid(row=0,column=0)

#Creates variable for entry value
entryValue = StringVar()

#Creates the entry widget and dictates its location
entry = Entry(window, textvariable=entryValue)
entry.grid(row=0,column=1)

#Creates a text widget for gs,lbs,ozs and dictates their location and size
g = Text(window,height=1,width=20)
g.grid(row=1,column=0)

lb = Text(window, height=1,width=20)
lb.grid(row=1,column=1)

oz = Text(window, height=1,width=20)
oz.grid(row=1,column=2)

window.mainloop()