from tkinter import *

#Creates the window
window = Tk()

#Converts kilometers put in by 
def kmToMiles():
    #Equation to convert km to miles
    miles = float(entry1Value.get())*1.6

    #Puts the value entered at the end of the text1 variable
    text1.insert(END, miles)

#Creates a button within the window, assigns its function
btn1 = Button(window, text="Execute", command=kmToMiles)
#Tells the button where to go inside the window
btn1.grid(row=0,column=0)

#Creates variable for entry1 value
entry1Value = StringVar()

#Creates an entry widget
entry1 = Entry(window, textvariable=entry1Value)
#Tells entry widget where to go
entry1.grid(row=0,column=1)

#Creates a text widget
text1 = Text(window, height=1,width=20)
#Tells text widget where to go
text1.grid(row=0,column=2)

window.mainloop()
