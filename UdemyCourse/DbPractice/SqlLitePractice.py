import sqlite3

def createTable():
    #If you DO NOT have a db file this will create one and create the connection
    #If you have an existing db file this will create the connection
    connection = sqlite3.connect("lite.db")

    #Creates cursor object
    cursor = connection.cursor()

    #Creates STORE table if it does not already exist
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

    #Commits changes to db
    connection.commit()

    #Closes connection
    connection.close()

def insertValues(item,quantity,price):
    #If you DO NOT have a db file this will create one and create the connection
    #If you have an existing db file this will create the connection
    connection = sqlite3.connect("lite.db")

    #Creates cursor object
    cursor = connection.cursor()

    #Inserts values into table
    cursor.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
    
    #Commits changes to db
    connection.commit()

    #Closes connection
    connection.close()



def viewData():
    #If you DO NOT have a db file this will create one and create the connection
    #If you have an existing db file this will create the connection
    connection = sqlite3.connect("lite.db")

    #Creates cursor object
    cursor = connection.cursor()

    #Selects all values in table
    cursor.execute("SELECT * FROM store")
    
    #Stores data into rows variable
    rows = cursor.fetchall()

    #Closes connection
    connection.close()

    #Returns data from rows
    return rows

def delete(item):
    #If you DO NOT have a db file this will create one and create the connection
    #If you have an existing db file this will create the connection
    connection = sqlite3.connect("lite.db")

    #Creates cursor object
    cursor = connection.cursor()

    #Deletes values from table
    cursor.execute("DELETE FROM store WHERE item=?", (item,))
    
    #Commits changes to database
    connection.commit()

    #Closes connection
    connection.close()

def update(quantity,price,item):
    #If you DO NOT have a db file this will create one and create the connection
    #If you have an existing db file this will create the connection
    connection = sqlite3.connect("lite.db")

    #Creates cursor object
    cursor = connection.cursor()

    #Updates values from table
    cursor.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity,price,item))
    
    #Commits changes to database
    connection.commit()

    #Closes connection
    connection.close()

#Prints table data
print(viewData())