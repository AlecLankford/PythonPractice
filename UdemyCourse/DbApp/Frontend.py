from tkinter import *
import Backend

#Returns row to binding of the list
def getSelectedRow(event):
    #Global variable so event can be accessed outside this funciton
    global selectedTuple
    #Returns index of selected row
    index=list1.curselection()[0]
    #Returns row based on selected index
    selectedTuple = list1.get(index)
    e1.delete(0,END)
    e1.insert(END, selectedTuple[1])
    
    e2.delete(0,END)
    e2.insert(END, selectedTuple[2])
    
    e3.delete(0,END)
    e3.insert(END, selectedTuple[3])
    
    e4.delete(0,END)
    e4.insert(END, selectedTuple[4])

#Inserts data into the list box when the user selects view all
def viewCommand():
    #Ensures the list box is empty before displaying records
    list1.delete(0,END)
    
    #Iterates through records and appends them to list box
    for row in Backend.view():
        list1.insert(END, row)

#Allows a user to search through the database by using various inputs (author,title,year,isbn,etc...)
def searchCommand():
    #Empties list box before search
    list1.delete(0,END)

    #Adds the returned record to the list box
    for row in Backend.search(titleText.get(),authorText.get(),yearText.get(),isbnText.get()):
        list1.insert(END,row)

#Allows a user to insert a record into the database
def insertCommand():
    Backend.insert(titleText.get(),authorText.get(),yearText.get(),isbnText.get())
    list1.delete(0,END)
    list1.insert(END,(titleText.get(),authorText.get(),yearText.get(),isbnText.get()))

#Allows a user to delete a specified row
def deleteCommand():
    Backend.delete(selectedTuple[0])

def updateCommand():
    Backend.update(selectedTuple[0],titleText.get(),authorText.get(),yearText.get(),isbnText.get())


#Creation of the window for GUI
window = Tk()

#Setting the title of the window
window.wm_title("Bookstore")

#Setting the labels for the entry fields
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

#Setting the entry values for the user inputs
titleText = StringVar()
e1 = Entry(window, textvariable=titleText)
e1.grid(row=0, column=1)

authorText = StringVar()
e2 = Entry(window, textvariable=authorText)
e2.grid(row=0, column=3)

yearText = StringVar()
e3 = Entry(window, textvariable=yearText)
e3.grid(row=1, column=1)

isbnText = StringVar()
e4 = Entry(window, textvariable=isbnText)
e4.grid(row=1, column=3)

#Creates the list for the data to be viewed in
list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

#Creates the scrollbar
scrollBar1 = Scrollbar(window)
scrollBar1.grid(row=2, column=2, rowspan=6)

list1.bind('<<ListboxSelect>>',getSelectedRow)

#Connects scrollbar to list, and list to scrollbar
list1.configure(yscrollcommand=scrollBar1.set)
scrollBar1.configure(command=list1.yview)

#Creation of all buttons
b1 = Button(window,text="View all", width=12, command=viewCommand)
b1.grid(row=2, column = 3)

b2 = Button(window,text="Search entry", width=12, command=searchCommand)
b2.grid(row=3, column = 3)

b3 = Button(window,text="Add entry", width=12, command=insertCommand)
b3.grid(row=4, column = 3)

b4 = Button(window,text="Update selected", width=12, command=updateCommand)
b4.grid(row=5, column = 3)

b5 = Button(window,text="Delete selected", width=12, command=deleteCommand)
b5.grid(row=6, column = 3)

b6 = Button(window,text="Close", width=12, command=window.destroy)
b6.grid(row=7, column = 3)

window.mainloop()
