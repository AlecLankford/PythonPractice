from tkinter import *

#Creates GUI window
window = Tk()

#Function to convert kg to g,lb, and oz
def kgConvert():
    #Executes conversion and places the values into a string
    grams = float(entryValue.get())*1000

    pounds = float(entryValue.get())*2.20462

    ounces = float(entryValue.get())*35.274

    outputText = ("Grams: " + str(grams) + ", Pounds: " + str(pounds) + ", Ounces: " + str(ounces))

    text.insert(END, outputText)

#Creates execute button and dictates its location
btn1 = Button(window, text="Convert", command=kgConvert)
btn1.grid(row=0,column=0)

#Creates variable for entry value
entryValue = StringVar()

#Creates the entry widget and dictates its location
entry = Entry(window, textvariable=entryValue)
entry.grid(row=0,column=1)

#Creates a text widget and dictates its location and size
text = Text(window,height=1,width=60)
text.grid(row=0,column=2)

window.mainloop()