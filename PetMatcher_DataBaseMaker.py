# FINAL PROJECT - Pet Matcher
# Madison Wikoff, Devin Mason, Najja Price
# This file contains the code for how we created the file with all of our item data for food, equipment, toys, etc.

from tkinter import * # import everything from tkinter module
from tkinter import messagebox # import messagebox for pop-ups in GUI
import os # for accessing the file path to create the database file
import sqlite3 # for accesing the database we created

# CODE TO CREATE THE DATABASE FILE #
PATH = r"C:\ACADEMICS\2021-2022 SPRING\CSC 102\FINAL PROJECT\PROGRAM FILES" #
os.chdir(PATH)
db_name = "PetMatcher_Data"

def create_table(db_name):
    # Create or Connect to Database, Create Cursor, Create Table (only need to run once) #
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(""" CREATE TABLE essentials(product_type text, product_name text, pet_type text, pet_size text, function text) """)

#create_table(db_name)
    
# MAIN DATA ENTRY GUI #
def master():
    # global variables #
    global root
    global product_type
    global product_name
    global pet_type
    global pet_size
    global product_function
    global query_box
    global clicked
    global search_entry
    global outputvar
    global totalvar
    
    # SET UP GUI #
    root = Tk()
    root.title("PetMatcher")
    root.geometry("800x480")
    root.configure(bg = "light yellow")
    
    Label(root, text = "PetMatcher Item DataBase", font = ("Courier", 20), bg = "light yellow", fg = "black", padx = 20, pady = 30).pack()
    
    # CREATE INFO AND SEARCH FRAMES #
    frame_info = LabelFrame(root, text = "Product Details", font = ("Courier", 10), bg = "light yellow", fg = "black", padx = 5, pady = 10)
    frame_info.pack(side = LEFT, padx = 10, pady = 10)
    
    frame_search = LabelFrame(root, text = "Search For An Item", font = ("Courier", 10), bg = "light yellow", fg = "black", padx = 5, pady = 10)
    frame_search.pack(side = RIGHT, padx = 10, pady = 10)
    
    # DETAIL FRAME #
    # -- Entry Boxes
    product_type = Entry(frame_info, width = 30)
    product_type.grid(row = 0, column = 1, padx =20, pady = (10, 0))
    
    product_name = Entry(frame_info, width = 30)
    product_name.grid(row = 1, column = 1, padx =20, pady = (10, 0))
    
    pet_type = Entry(frame_info, width = 30)
    pet_type.grid(row = 2, column = 1, padx =20, pady = (10, 0))
    
    pet_size = Entry(frame_info, width = 30)
    pet_size.grid(row = 3, column = 1, padx =20, pady = (10, 0))
    
    product_function = Entry(frame_info, width = 30)
    product_function.grid(row = 4, column = 1, padx =20, pady = (10, 0))
    
    # -- Labels & Buttons
    Label(frame_info, text = "Product Type", font = ("Courier", 10), bg = "light yellow").grid(row = 0, column = 0, pady = (10, 0), sticky = W)
    Label(frame_info, text = "Product Name", font = ("Courier", 10), bg = "light yellow").grid(row = 1, column = 0, pady = (10, 0), sticky = W)
    Label(frame_info, text = "Pet Type", font = ("Courier", 10), bg = "light yellow").grid(row = 2, column = 0, pady = (10, 0), sticky = W)
    Label(frame_info, text = "Pet Size", font = ("Courier", 10), bg = "light yellow").grid(row = 3, column = 0, pady = (10, 0), sticky = W)
    Label(frame_info, text = "Product Function", font = ("Courier", 10), bg = "light yellow").grid(row = 4, column = 0, pady = (10, 0), sticky = W)

    enter_button = Button(frame_info, text = "Add Item to DataBase", command = submit, font = ("Courier", 10)).grid(row = 9, column = 0, columnspan = 2, padx = 10, pady = 10)
    Label(frame_info, text = "Item ID", font = ("Courier", 10), bg = "light yellow").grid(row = 10, column = 0, sticky = W)
    
    query_box = Entry(frame_info, width = 30).grid(row = 10, column = 1, padx = 20)
    
    update_button = Button(frame_info, text = "Update DataBase", command = update, font = ("Courier", 10))
    update_button.grid(row = 11, column = 1, padx = 10, pady = 10)
    
    search_button = Button(frame_info, text = "Search DataBase", command = search, font = ("Courier", 10))
    search_button.grid(row = 11, column = 0, padx = 10, pady = 10)
    
    # SEARCH FRAME #
    outputvar = StringVar()
    totalvar = StringVar()
    
    Label(frame_search, text = "Search by", font = ("Courier", 10), bg = "light yellow").grid(row = 0, column = 0)
    
    menu_list = ["product_type", "product_name", "pet_type", "pet_size", "product_function"]
    menuwidth = len(max(menu_list, key = len))
    
    clicked = StringVar()
    clicked.set(menu_list[0])
    
    search_menu = OptionMenu(frame_search, clicked, *menu_list)
    search_menu.config(width = menuwidth)
    search_menu.grid(row = 0, column = 1)
    
    search_entry = Entry(frame_search, width = 30)
    search_entry.grid(row = 0, column = 2)
    
    Button(frame_search, text = "Search", command = query, font = ("Courier", 10)).grid(row = 0, column = 3)
    
    total = Label(frame_search, textvariable = totalvar, bg = "light yellow", height = 4, width = 50, anchor = W).grid(row = 1, columnspan = 4)
    output = Label(frame_search, textvariable = outputvar, bg = "light yellow", height = 20, width = 50, anchor = W).grid(row = 2, columnspan = 4)
    
    # CALL THE GUI #
    root.mainloop()

# BUTTON FUNCTIONS #
# -- Add Item to DataBase
def submit():
    # Connect to Database, Create Cursor #
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Insert Into Table #
    c.execute(""" INSERT INTO essentials VALUES (:product_type, :product_name, :pet_type, :pet_size, :product_function) """,
              {"product_type":product_type.get(),
               "product_name":product_name.get(),
               "pet_type":pet_type.get(),
               "pet_size":pet_size.get(),
               "product_function":product_function.get()})
    
    # Commit Changes #
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Success!", "Item added to DataBase.")
    
    # Clear #
    product_type.delete(0, END)
    product_name.delete(0, END)
    pet_type.delete(0, END)
    pet_size.delete(0, END)
    product_function.delete(0, END)

# -- Search the DataBase
def search():
    # Clear #
    product_type.delete(0, END)
    product_name.delete(0, END)
    pet_type.delete(0, END)
    pet_size.delete(0, END)
    product_function.delete(0, END)
    
    # Connect to Database, Create Cursor #
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    record_id = query_box.get()
    
    c.execute("SELECT * FROM essentials WHERE oid = " + record_id)
    records = c.fetchall()
    if len(records) == 0:
        messagebox.showerror("Warning!", "This item is not in the DataBase.")
    
    # Loop Through Records #
    for record in records:
        product_type.insert(0, record[0])
        product_name.insert(0, record[1])
        pet_type.insert(0, record[2])
        pet_size.insert(0, record[3])
        product_function.insert(0, record[4])

# -- Update Item in the DataBase
def update():
    # Connect to Database, Create Cursor #
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    record_id = query_box.get()
    
    # Insert Into Table #
    c.execute(""" UPDATE essentials SET product_type = :type, product_name = :name, pet_type = :pet, pet_size = :size, product_function = :function WHERE oid = :oid """,
              {"product_type":product_type.get(),
               "product_name":product_name.get(),
               "pet_type":pet_type.get(),
               "pet_size":pet_size.get(),
               "product_function":product_function.get()})
    
    # Commit Changes #
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Success!", "The item information has been updated.")
    
    # Clear #
    product_type.delete(0, END)
    product_name.delete(0, END)
    pet_type.delete(0, END)
    pet_size.delete(0, END)
    product_function.delete(0, END)

# -- Query
def query():
    totalvar.set(" ")
    outputvar.set(" ")
    
    field = clicked.get()
    field_value = search_entry.get()
    print(field, field_value)
    
    # Connect to Database, Create Cursor #
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    execution = f"SELECT rowid, * WHERE {field} = ? "
    c.execute(execution, (field_value, ))
    records = c.fetchall()
    total = len(records)
    
    if total == 0:
        messagebox.showerror("Warning!", "This item does not exist.")
    
    print_records = ""
    
    for rec in records:
        print_records += (str(rec[0]) + "  " + str(rec[1]) + "   " + str(rec[2]) + " " + "\t" + str(rec[8]) + "  " + str(rec[9]) + "\n")
    
    total_records = f"A total of {total} records found."
    totalvar.set(total_records)
    outputvar.set(print_records)

master()