from tkinter import *
from tkinter import messagebox
import os
import sqlite3
#import time
#import RPi.GPIO as GPIO

# -- Functions to start each day for routine (GPIO visual alarm)
def dogtasks():
    pass

def cattasks():
    pass

def birdtasks():
    pass

def fishtasks():
    pass

def reptasks():
    pass

def rodtasks():
    pass

# -- Functions to generate routines
def doggen():
    global walk1
    global walk2
    global dogfeed1
    global dogfeed2
    global bath
    global dogplay
    
    walk1 = walk1.get()
    walk2 = walk2.get()
    
    dogfeed1 = dogfeed1.get()
    dogfeed2 = dogfeed2.get()
    
    bath = bath.get()
    
    dogplay = dogplay.get()
    
    dog_schedule = Tk()
    dogrout.destroy()
    
    dog_schedule.title("Your Customized Dog Routine")
    dog_schedule.geometry("800x480")
    
    Label(dog_schedule, text = "Here is your customized schedule! Each activity is\nsignified by a different color LED light, shown\nby the color of the font for each one.", font = ("Courier", 12, "bold")).grid(row = 0, column = 0, columnspan = 4, padx = 40, pady = 20)
    
    Label(dog_schedule, text = "Feeding Time", font = ("Courier", 12, "bold"), bg = "gray", fg = "red").grid(row = 1, column = 0)
    Label(dog_schedule, text = "Bath Time", font = ("Courier", 12, "bold"), bg = "gray", fg = "yellow").grid(row = 1, column = 1)
    Label(dog_schedule, text = "Play Time", font = ("Courier", 12, "bold"), bg = "gray", fg = "blue").grid(row = 1, column = 2)
    Label(dog_schedule, text = "Walk Time", font = ("Courier", 12, "bold"), bg = "gray", fg = "green").grid(row = 1, column = 3)
    
    Label(dog_schedule, text = dogfeed1, font = ("Courier", 12)).grid(row = 2, column = 0)
    Label(dog_schedule, text = dogfeed2, font = ("Courier", 12)).grid(row = 3, column = 0)
    
    Label(dog_schedule, text = bath, font = ("Courier", 12)).grid(row = 2, column = 1)
    
    Label(dog_schedule, text = dogplay, font = ("Courier", 12)).grid(row = 2, column = 2)
    
    Label(dog_schedule, text = walk1, font = ("Courier", 12)).grid(row = 2, column = 3)
    Label(dog_schedule, text = walk2, font = ("Courier", 12)).grid(row = 3, column = 3)

def catgen():
    global catfeed1
    global catfeed2
    global catplay
    global cleanlitter
    
    catfeed1 = catfeed1.get()
    catfeed2 = catfeed2.get()
    
    catplay = catplay.get()
    
    cleanlitter = cleanlitter.get()
    
    cat_schedule = Tk()
    catrout.destroy()
    
    cat_schedule.title("Your Customized Cat Routine")
    cat_schedule.geometry("800x480")
    
    Label(cat_schedule, text = "Here is your customized schedule! Each activity is\nsignified by a different color LED light, shown\nby the color of the font for each one.", font = ("Courier", 12, "bold")).grid(row = 0, column = 0, columnspan = 3, padx = 40, pady = 20)
    
    Label(cat_schedule, text = "Feeding Time", font = ("Courier", 12, "bold"), bg = "gray", fg = "red").grid(row = 1, column = 0)
    Label(cat_schedule, text = "Clean Litter Box Time", font = ("Courier", 12, "bold"), bg = "gray", fg = "yellow").grid(row = 1, column = 1)
    Label(cat_schedule, text = "Play Time", font = ("Courier", 12, "bold"), bg = "gray", fg = "blue").grid(row = 1, column = 2)
    
    Label(cat_schedule, text = catfeed1, font = ("Courier", 12)).grid(row = 2, column = 0)
    Label(cat_schedule, text = catfeed2, font = ("Courier", 12)).grid(row = 3, column = 0)
    
    Label(cat_schedule, text = cleanlitter, font = ("Courier", 12)).grid(row = 2, column = 1)
    
    Label(cat_schedule, text = catplay, font = ("Courier", 12)).grid(row = 2, column = 2)

def birdgen():
    global birdfeed1
    global birdfeed2
    global birdplay
    global cleancage
    
    birdfeed1 = birdfeed1.get()
    birdfeed2 = birdfeed2.get()
    
    birdplay = birdplay.get()
    
    cleancage = cleancage.get()
    
    bird_schedule = Tk()
    birdrout.destroy()
    
    bird_schedule.title("Your Customized Bird Routine")
    bird_schedule.geometry("800x480")
    
    Label(bird_schedule, text = "Here is your customized schedule! Each activity is\nsignified by a different color LED light, shown\nby the color of the font for each one.", font = ("Courier", 12, "bold")).grid(row = 0, column = 0, columnspan = 3, padx = 40, pady = 20)
    
    Label(bird_schedule, text = "Feeding Time", font = ("Courier", 12, "bold"), bg = "gray", fg = "red").grid(row = 1, column = 0)
    Label(bird_schedule, text = "Clean Cage Time", font = ("Courier", 12, "bold"), bg = "gray", fg = "yellow").grid(row = 1, column = 1)
    Label(bird_schedule, text = "Play Time", font = ("Courier", 12, "bold"), bg = "gray", fg = "blue").grid(row = 1, column = 2)
    
    Label(bird_schedule, text = birdfeed1, font = ("Courier", 12)).grid(row = 2, column = 0)
    Label(bird_schedule, text = birdfeed2, font = ("Courier", 12)).grid(row = 3, column = 0)
    
    Label(bird_schedule, text = cleancage, font = ("Courier", 12)).grid(row = 2, column = 1)
    
    Label(bird_schedule, text = birdplay, font = ("Courier", 12)).grid(row = 2, column = 2)

def fishgen():
    global fishfeed1
    global fishfeed2
    global cleantank
    
    fishfeed1 = fishfeed1.get()
    fishfeed2 = fishfeed2.get()
    
    cleantank = cleantank.get()
    
    fish_schedule = Tk()
    fishrout.destroy()
    
    fish_schedule.title("Your Customized Fish Routine")
    fish_schedule.geometry("800x480")
    
    Label(fish_schedule, text = "Here is your customized schedule! Each activity is\nsignified by a different color LED light, shown\nby the color of the font for each one.", font = ("Courier", 12, "bold")).grid(row = 0, column = 0, columnspan = 2, padx = 40, pady = 20)
    
    Label(fish_schedule, text = "Feeding Time", font = ("Courier", 12, "bold"), bg = "gray", fg = "red").grid(row = 1, column = 0)
    Label(fish_schedule, text = "Clean Tank Time", font = ("Courier", 12, "bold"), bg = "gray", fg = "yellow").grid(row = 1, column = 1)
    
    Label(bird_schedule, text = fishfeed1, font = ("Courier", 12)).grid(row = 2, column = 0)
    Label(bird_schedule, text = fishfeed2, font = ("Courier", 12)).grid(row = 3, column = 0)
    
    Label(bird_schedule, text = cleantank, font = ("Courier", 12)).grid(row = 2, column = 1)

def repgen():
    global repfeed1
    global repfeed2
    global cleanrep
    
    repfeed1 = repfeed1.get()
    repfeed2 = repfeed2.get()
    
    cleanrep = cleanrep.get()
    
    rep_schedule = Tk()
    reptilerout.destroy()
    
    rep_schedule.title("Your Customized Reptile Routine")
    rep_schedule.geometry("800x480")
    
    Label(rep_schedule, text = "Here is your customized schedule! Each activity is\nsignified by a different color LED light, shown\nby the color of the font for each one.", font = ("Courier", 12, "bold")).grid(row = 0, column = 0, columnspan = 2, padx = 40, pady = 20)
    
    Label(rep_schedule, text = "Feeding Time", font = ("Courier", 12, "bold"), bg = "gray", fg = "red").grid(row = 1, column = 0)
    Label(rep_schedule, text = "Clean Tank Time", font = ("Courier", 12, "bold"), bg = "gray", fg = "yellow").grid(row = 1, column = 1)
    
    Label(rep_schedule, text = repfeed1, font = ("Courier", 12)).grid(row = 2, column = 0)
    Label(rep_schedule, text = repfeed2, font = ("Courier", 12)).grid(row = 3, column = 0)
    
    Label(rep_schedule, text = cleanrep, font = ("Courier", 12)).grid(row = 2, column = 1)

def rodgen():
    global rodfeed1
    global rodfeed2
    global cleanrod
    
    rodfeed1 = rodfeed1.get()
    rodfeed2 = rodfeed2.get()
    
    cleanrod = cleanrod.get()
    
    rod_schedule = Tk()
    rodentrout.destroy()
    
    rod_schedule.title("Your Customized Rodent Routine")
    rod_schedule.geometry("800x480")
    
    Label(rod_schedule, text = "Here is your customized schedule! Each activity is\nsignified by a different color LED light, shown\nby the color of the font for each one.", font = ("Courier", 12, "bold")).grid(row = 0, column = 0, columnspan = 2, padx = 40, pady = 20)
    
    Label(rod_schedule, text = "Feeding Time", font = ("Courier", 12, "bold"), bg = "gray", fg = "red").grid(row = 1, column = 0)
    Label(rod_schedule, text = "Clean Tank Time", font = ("Courier", 12, "bold"), bg = "gray", fg = "yellow").grid(row = 1, column = 1)
    
    Label(rod_schedule, text = repfeed1, font = ("Courier", 12)).grid(row = 2, column = 0)
    Label(rod_schedule, text = repfeed2, font = ("Courier", 12)).grid(row = 3, column = 0)
    
    Label(rod_schedule, text = cleanrep, font = ("Courier", 12)).grid(row = 2, column = 1)

# -- Functions for going back to Routine Maker Home Page
def doghome():
    dogrout.destroy()
    routine()

def cathome():
    catrout.destroy()
    routine()

def birdhome():
    birdrout.destroy()
    routine()

def fishhome():
    fishrout.destroy()
    routine()

def rephome():
    reptilerout.destroy()
    routine()

def rodhome():
    rodentrout.destroy()
    routine()

# -- Function for Dog Routine Maker
def dog_routine():
    global dogrout
    global walk1
    global walk2
    global dogfeed1
    global dogfeed2
    global bath
    global dogplay
    
    dogrout = Tk()
    rout.destroy()
    
    dogrout.title("Dog Routine Maker")
    dogrout.geometry("800x480")
    
    Label(dogrout, text = "Below, you can set up a routine\nfor you and your dog!", font = ("Courier", 20, "bold")).grid(row = 0, column = 0, columnspan = 3, padx = 20)
    
    Label(dogrout, text = "                                     ").grid(row = 1, column = 0, columnspan = 3)
    Label(dogrout, text = "Enter times for walks:", font = ("Courier", 12)).grid(row = 2, column = 0, rowspan = 2)
    Label(dogrout, text = "                                     ").grid(row = 4, column = 0, columnspan = 3)
    Label(dogrout, text = "Enter times for feeding:", font = ("Courier", 12)).grid(row = 5, column = 0, rowspan = 2)
    Label(dogrout, text = "                                     ").grid(row = 7, column = 0, columnspan = 3)
    Label(dogrout, text = "Enter time for bath:", font = ("Courier", 12)).grid(row = 8, column = 0)
    Label(dogrout, text = "                                     ").grid(row = 9, column = 0, columnspan = 3)
    Label(dogrout, text = "Enter time for play:", font = ("Courier", 12)).grid(row = 10, column = 0)
    
    walk1 = Entry(dogrout, width = 30)
    walk1.grid(row = 2, column = 1)
    walk2 = Entry(dogrout, width = 30)
    walk2.grid(row = 3, column = 1)
    
    dogfeed1 = Entry(dogrout, width = 30)
    dogfeed1.grid(row = 5, column = 1)
    dogfeed2 = Entry(dogrout, width = 30)
    dogfeed2.grid(row = 6, column = 1)
    
    bath = Entry(dogrout, width = 30)
    bath.grid(row = 8, column = 1)
    
    dogplay = Entry(dogrout, width = 30)
    dogplay.grid(row = 10, column = 1)
    
    Button(dogrout, text = "Back", font = ("Courier", 12), width = 25, command = doghome).grid(row = 11, column = 0)
    Button(dogrout, text = "Generate Routine", font = ("Courier", 12), width = 25, command = doggen).grid(row = 11, column = 1)
    
    dogrout.mainloop()

# -- Founction for Cat Routine Maker
def cat_routine():
    global catrout
    global catfeed1
    global catfeed2
    global catplay
    global cleanlitter
    
    catrout = Tk()
    rout.destroy()
    
    catrout.title("Cat Routine Maker")
    catrout.geometry("800x480")
    
    Label(catrout, text = "Below, you can set up a routine\nfor you and your cat!", font = ("Courier", 20, "bold")).grid(row = 0, column = 0, columnspan = 3, padx = 20)
    
    Label(catrout, text = "                                     ").grid(row = 1, column = 0, columnspan = 3)
    Label(catrout, text = "Enter times for feeding:", font = ("Courier", 12)).grid(row = 2, column = 0, rowspan = 2)
    Label(catrout, text = "                                     ").grid(row = 4, column = 0, columnspan = 3)
    Label(catrout, text = "Enter time for play:", font = ("Courier", 12)).grid(row = 5, column = 0, rowspan = 2)
    Label(catrout, text = "                                     ").grid(row = 7, column = 0, columnspan = 3)
    Label(catrout, text = "Enter time for\ncleaning litter box:", font = ("Courier", 12)).grid(row = 8, column = 0)
    Label(catrout, text = "                                     ").grid(row = 9, column = 0, columnspan = 3)
    
    catfeed1 = Entry(catrout, width = 30)
    catfeed1.grid(row = 2, column = 1)
    catfeed2 = Entry(catrout, width = 30)
    catfeed2.grid(row = 3, column = 1)
    
    catplay = Entry(catrout, width = 30)
    catplay.grid(row = 5, column = 1)
    
    cleanlitter = Entry(catrout, width = 30)
    cleanlitter.grid(row = 8, column = 1)
    
    Button(catrout, text = "Back", font = ("Courier", 12), width = 25, command = cathome).grid(row = 10, column = 0)
    Button(catrout, text = "Generate Routine", font = ("Courier", 12), width = 25, command = catgen).grid(row = 10, column = 1)
    
    catrout.mainloop()

# -- Function for Bird Routine Maker
def bird_routine():
    global birdrout
    global birdfeed1
    global birdfeed2
    global birdplay
    global cleancage
    
    birdrout = Tk()
    rout.destroy()
    
    birdrout.title("Bird Routine Maker")
    birdrout.geometry("800x480")
    
    Label(birdrout, text = "Below, you can set up a routine\nfor you and your bird!", font = ("Courier", 20, "bold")).grid(row = 0, column = 0, columnspan = 3, padx = 30)
    
    Label(birdrout, text = "                                     ").grid(row = 1, column = 0, columnspan = 3)
    Label(birdrout, text = "Enter times for feeding:", font = ("Courier", 12)).grid(row = 2, column = 0, rowspan = 2)
    Label(birdrout, text = "                                     ").grid(row = 4, column = 0, columnspan = 3)
    Label(birdrout, text = "Enter time for play:", font = ("Courier", 12)).grid(row = 5, column = 0, rowspan = 2)
    Label(birdrout, text = "                                     ").grid(row = 7, column = 0, columnspan = 3)
    Label(birdrout, text = "Enter time for\ncleaning the cage:", font = ("Courier", 12)).grid(row = 8, column = 0)
    Label(birdrout, text = "                                     ").grid(row = 9, column = 0, columnspan = 3)
    
    birdfeed1 = Entry(birdrout, width = 30)
    birdfeed1.grid(row = 2, column = 1)
    birdfeed2 = Entry(birdrout, width = 30)
    birdfeed2.grid(row = 3, column = 1)
    
    birdplay = Entry(birdrout, width = 30)
    birdplay.grid(row = 5, column = 1)
    
    cleancage = Entry(birdrout, width = 30)
    cleancage.grid(row = 8, column = 1)
    
    Button(birdrout, text = "Back", font = ("Courier", 12), width = 25, command = birdhome).grid(row = 10, column = 0)
    Button(birdrout, text = "Generate Routine", font = ("Courier", 12), width = 25, command = birdgen).grid(row = 10, column = 1)
    
    birdrout.mainloop()

# -- Function for Fish Routine Maker
def fish_routine():
    global fishrout
    global fishfeed1
    global fishfeed2
    global cleantank
    
    fishrout = Tk()
    rout.destroy()
    
    fishrout.title("Fish Routine Maker")
    fishrout.geometry("800x480")
    
    Label(fishrout, text = "Below, you can set up a routine\nfor you and your fish!", font = ("Courier", 20, "bold")).grid(row = 0, column = 0, columnspan = 3, padx = 20)
    
    Label(fishrout, text = "                                     ").grid(row = 1, column = 0, columnspan = 3)
    Label(fishrout, text = "Enter times for feeding:", font = ("Courier", 12)).grid(row = 2, column = 0, rowspan = 2)
    Label(fishrout, text = "                                     ").grid(row = 4, column = 0, columnspan = 3)
    Label(fishrout, text = "Enter time for\ncleaning the tank:", font = ("Courier", 12)).grid(row = 5, column = 0, rowspan = 2)
    Label(fishrout, text = "                                     ").grid(row = 7, column = 0, columnspan = 3,)
    
    fishfeed1 = Entry(fishrout, width = 30)
    fishfeed1.grid(row = 2, column = 1)
    fishfeed2 = Entry(fishrout, width = 30)
    fishfeed2.grid(row = 3, column = 1)
    
    cleantank = Entry(fishrout, width = 30)
    cleantank.grid(row = 5, column = 1)
    
    Button(fishrout, text = "Back", font = ("Courier", 12), width = 25, command = fishhome).grid(row = 8, column = 0)
    Button(fishrout, text = "Generate Routine", font = ("Courier", 12), width = 25, command = fishgen).grid(row = 8, column = 1)
    
    fishrout.mainloop()

# -- Function for Reptile Routine Maker
def reptile_routine():
    global reptilerout
    global repfeed1
    global repfeed2
    global cleanrep
    
    reptilerout = Tk()
    rout.destroy()
    
    reptilerout.title("Reptile Routine Maker")
    reptilerout.geometry("800x480")
    
    Label(reptilerout, text = "Below, you can set up a routine\nfor you and your reptile!", font = ("Courier", 20, "bold")).grid(row = 0, column = 0, columnspan = 3, padx = 20)
    
    Label(reptilerout, text = "                                     ").grid(row = 1, column = 0, columnspan = 3)
    Label(reptilerout, text = "Enter times for feeding:", font = ("Courier", 12)).grid(row = 2, column = 0, rowspan = 2)
    Label(reptilerout, text = "                                     ").grid(row = 4, column = 0, columnspan = 3)
    Label(reptilerout, text = "Enter time for\ncleaning the enclosure:", font = ("Courier", 12)).grid(row = 5, column = 0, rowspan = 2)
    Label(reptilerout, text = "                                     ").grid(row = 7, column = 0, columnspan = 3)
    
    repfeed1 = Entry(reptilerout, width = 30)
    repfeed1.grid(row = 2, column = 1)
    repfeed2 = Entry(reptilerout, width = 30)
    repfeed2.grid(row = 3, column = 1)
    
    cleanrep = Entry(reptilerout, width = 30)
    cleanrep.grid(row = 5, column = 1)
    
    Button(reptilerout, text = "Back", font = ("Courier", 12), width = 25, command = rephome).grid(row = 8, column = 0)
    Button(reptilerout, text = "Generate Routine", font = ("Courier", 12), width = 25, command = repgen).grid(row = 8, column = 1)
    
    reptilerout.mainloop()

# -- Function for Rodent Routine Maker
def rodent_routine():
    global rodentrout
    global rodfeed1
    global rodfeed2
    global cleanrod
    
    rodentrout = Tk()
    rout.destroy()
    
    rodentrout.title("Rodent Routine Maker")
    rodentrout.geometry("800x480")
    
    Label(rodentrout, text = "Below, you can set up a routine\nfor you and your rodent!", font = ("Courier", 20, "bold")).grid(row = 0, column = 0, columnspan = 3, padx = 20)
    
    Label(rodentrout, text = "                                     ").grid(row = 1, column = 0, columnspan = 3)
    Label(rodentrout, text = "Enter times for feeding:", font = ("Courier", 12)).grid(row = 2, column = 0, rowspan = 2)
    Label(rodentrout, text = "                                     ").grid(row = 4, column = 0, columnspan = 3)
    Label(rodentrout, text = "Enter time for\ncleaning the enclosure:", font = ("Courier", 12)).grid(row = 5, column = 0, rowspan = 2)
    Label(rodentrout, text = "                                     ").grid(row = 7, column = 0, columnspan = 3)
    
    rodfeed1 = Entry(rodentrout, width = 30)
    rodfeed1.grid(row = 2, column = 1)
    rodfeed2 = Entry(rodentrout, width = 30)
    rodfeed2.grid(row = 3, column = 1)
    
    cleanrod = Entry(rodentrout, width = 30)
    cleanrod.grid(row = 5, column = 1)
    
    Button(rodentrout, text = "Back", font = ("Courier", 12), width = 25, command = rodhome).grid(row = 8, column = 0)
    Button(rodentrout, text = "Generate Routine", font = ("Courier", 12), width = 25, command = rodgen).grid(row = 8, column = 1)
    
    rodentrout.mainloop()

# -- Function to return to PetMatcher Home Page
def routhome():
    homepage()
    routine.destroy()

# -- Function for Routine GUI
def routine():
    global rout
    
    rout = Tk()
    home.destroy()
    
    rout.title("PetMatcher - Routine Maker")
    rout.geometry("800x480")
    
    Label(rout, text = "What type of pet do you have or want to have?", font = ("Courier", 14, "bold")).grid(row = 0, column = 0, columnspan = 3, padx = 20, pady = 20)
    
    dog = Button(rout, text = "Dog", font = ("Courier", 12), width = 25, command = dog_routine)
    dog.grid(row = 1, column = 0, padx = 20, pady = 10)
    
    cat = Button(rout, text = "Cat", font = ("Courier", 12), width = 25, command = cat_routine)
    cat.grid(row = 1, column = 1, padx = 20, pady = 10)
    
    bird = Button(rout, text = "Bird", font = ("Courier", 12), width = 25,  command = bird_routine)
    bird.grid(row = 2, column = 0, padx = 20, pady = 10)
    
    fish = Button(rout, text = "Fish", font = ("Courier", 12), width = 25, command = fish_routine)
    fish.grid(row = 2, column = 1, padx = 20, pady = 10)
    
    reptile = Button(rout, text = "Reptile", font = ("Courier", 12), width = 25, command = reptile_routine)
    reptile.grid(row = 3, column = 0, padx = 20, pady = 10)
    
    rodent = Button(rout, text = "Rodent", font = ("Courier", 12), width = 25, command = rodent_routine)
    rodent.grid(row = 3, column = 1, padx = 20, pady = 10)
    
    home_rout = Button(rout, text = "PetMatcher Home Page", font = ("Courier", 12, "bold")) # add a backhome method
    home_rout.grid(row = 5, column = 0, columnspan = 2, padx = 50, pady = 50)
    
    rout.mainloop()

# -- Functions for Search Items Page and DataBase
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

# BUTTON FUNCTIONS #
# -- Search the DataBase
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
    home.destroy()
    
    root.title("PetMatcher")
    root.geometry("800x480")
    root.configure(bg = "light yellow")
    
    Label(root, text = "PetMatcher Item DataBase", font = ("Courier", 20, "bold"), bg = "light yellow", fg = "black", padx = 50, pady = 30).grid(row = 0, column = 0, columnspan = 4)
    
    # SEARCH FRAME #
    outputvar = StringVar()
    totalvar = StringVar()
    
    Label(root, text = "Search by", font = ("Courier", 10), bg = "light yellow").grid(row = 1, column = 0)
    
    menu_list = ["product_type", "product_name", "pet_type", "pet_size", "product_function"]
    menuwidth = len(max(menu_list, key = len))
    
    clicked = StringVar()
    clicked.set(menu_list[0])
    
    search_menu = OptionMenu(root, clicked, *menu_list)
    search_menu.config(width = menuwidth)
    search_menu.grid(row = 1, column = 1)
    
    search_entry = Entry(root, width = 30)
    search_entry.grid(row = 1, column = 2)
    
    Button(root, text = "Search", command = query, font = ("Courier", 10)).grid(row = 1, column = 3)
    
    total = Label(root, textvariable = totalvar, bg = "light yellow").grid(row = 2, columnspan = 4)
    output = Label(root, textvariable = outputvar, bg = "light yellow").grid(row = 3, columnspan = 4)
    
    # CALL THE GUI #
    root.mainloop()

# homepage !!

def homepage():
    global home
    
    home = Tk()
    home.title("PetMatcher")
    home.geometry("800x480")
    
    bg = PhotoImage(file = "PM_GreenBG")
    
    Label(home, image = bg).place(x = 0, y = 0)
    
    Label(home, text = "Welcome to PetMatcher", font = ("Courier", 28, "bold")).grid(row = 0, column = 0, padx = 40, pady = 40)
    
    Button(home, text = "Take the PetMatcher Quiz", font = ("Courier", 12), width = 40, height = 2).grid(row = 1, column =0, padx = 50, pady = 12)
    Button(home, text = "Search for Items for your Pet", font = ("Courier", 12), width = 40, height = 2, command = master).grid(row = 2, column =0, padx = 50, pady = 12)
    Button(home, text = "Make a Custom Routine for your Pet", font = ("Courier", 12), width = 40, height = 2, command = routine).grid(row = 3, column =0, padx = 50, pady = 12)
    
    home.mainloop()

homepage()