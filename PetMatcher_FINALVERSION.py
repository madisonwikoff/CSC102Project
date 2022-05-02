# -- Import libraries
from tkinter import *
import RPi.GPIO as GPIO
from datetime import datetime
from time import sleep
# import files
from newQuiz import *

# -- Quiz Section (change backgrounds to the tkinter default if pictures not working on Pi)
# paste classes and other content for quiz here

# add function for result page to return to PM homepage using withdraw() function and then call homepage()
def quizhome():
    quizHome.withdraw()
    homepage()
    #(name of quiz window AKA global variable name from quiz_setup()).withdraw()
    #homepage()

def quiz_setup():
    #home.withdraw()
    quizHome()
    #paste the lines that call the quiz here
    # use "global [variable name]" for name of quiz window to use in other functions, see other function in routine section for reference

# -- GPIO Section
GPIO.setwarnings(False)

# -- Set the GPIO pin numbers
red = 6
yellow = 13
blue = 19
green = 21

GPIO.setmode(GPIO.BCM)

GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

# -- Functions for GPIO visual alarm (NOT FUNCTIONAL)
def dogalarm():
    # -- Collect the time
    red_hour1 = dogfeed1[0:2]
    red_min1 = dogfeed1[3:5]
    red_period1 = dogfeed1[9:]
    
    red_hour2 = dogfeed2[0:2]
    red_min2 = dogfeed2[3:5]
    red_period2 = dogfeed2[9:]
    
    yellow_hour = bath[0:2]
    yellow_min = bath[3:5]
    yellow_period = bath[9:]
    
    blue_hour = dogplay[0:2]
    blue_min = dogplay[3:5]
    blue_period = dogplay[9:]
    
    green_hour1 = walk1[0:2]
    green_min1 = walk1[3:5]
    green_period1 = walk1[9:]
    
    green_hour2 = walk2 [0:2]
    green_min2 = walk2[3:5]
    green_period2 = walk2[9:]
    
    # -- Alarm
    while True:
        now = datetime.now()

        current_hour = now.strftime("%I")
        current_min = now.strftime("%M")
        current_period = now.strftime("%p")

        if red_period1 == current_period:
            if red_hour1 == current_hour:
                if red_min1 == current_min:
                    GPIO.output(red, True)
                    sleep(0.5)
                    GPIO.output(red, False)
                    sleep(0.5)
        
        if red_period2 == current_period:
            if red_hour2 == current_hour:
                if red_min2 == current_min:
                    GPIO.output(red, True)
                    sleep(0.5)
                    GPIO.output(red, False)
                    sleep(0.5)
        
        if yellow_period == current_period:
            if yellow_hour == current_hour:
                if yellow_min == current_min:
                    GPIO.output(yellow, True)
                    sleep(0.5)
                    GPIO.output(yellow, False)
                    sleep(0.5)
        
        if blue_period == current_period:
            if blue_hour == current_hour:
                if blue_min == current_min:
                    GPIO.output(blue, True)
                    sleep(0.5)
                    GPIO.output(blue, False)
                    sleep(0.5)
        
        if green_period1 == current_period:
            if green_hour1 == current_hour:
                if green_min1 == current_min:
                    GPIO.output(green, True)
                    sleep(0.5)
                    GPIO.output(green, False)
                    sleep(0.5)
        
        if green_period2 == current_period:
            if green_hour2 == current_hour:
                if green_min2 == current_min:
                    GPIO.output(green, True)
                    sleep(0.5)
                    GPIO.output(green, False)
                    sleep(0.5)

def catalarm():
    # -- Collect the time
    red_hour1 = catfeed1[0:2]
    red_min1 = catfeed1[3:5]
    red_period1 = catfeed1[9:]
    
    red_hour2 = catfeed2[0:2]
    red_min2 = catfeed2[3:5]
    red_period2 = catfeed2[9:]
    
    yellow_hour = cleanlitter[0:2]
    yellow_min = cleanlitter[3:5]
    yellow_period = cleanlitter[9:]
    
    blue_hour = catplay[0:2]
    blue_min = catplay[3:5]
    blue_period = catplay[9:]
    
    # -- Alarm
    while True:
        now = datetime.now()

        current_hour = now.strftime("%I")
        current_min = now.strftime("%M")
        current_period = now.strftime("%p")

        if red_period1 == current_period:
            if red_hour1 == current_hour:
                if red_min1 == current_min:
                    GPIO.output(red, True)
                    sleep(0.5)
                    GPIO.output(red, False)
                    sleep(0.5)
        
        if red_period2 == current_period:
            if red_hour2 == current_hour:
                if red_min2 == current_min:
                    GPIO.output(red, True)
                    sleep(0.5)
                    GPIO.output(red, False)
                    sleep(0.5)
        
        if yellow_period == current_period:
            if yellow_hour == current_hour:
                if yellow_min == current_min:
                    GPIO.output(yellow, True)
                    sleep(0.5)
                    GPIO.output(yellow, False)
                    sleep(0.5)
        
        if blue_period == current_period:
            if blue_hour == current_hour:
                if blue_min == current_min:
                    GPIO.output(blue, True)
                    sleep(0.5)
                    GPIO.output(blue, False)
                    sleep(0.5)

def birdalarm():
    # -- Collect the time
    red_hour1 = birdfeed1[0:2]
    red_min1 = birdfeed1[3:5]
    red_period1 = birdfeed1[9:]
    
    red_hour2 = birdfeed2[0:2]
    red_min2 = birdfeed2[3:5]
    red_period2 = birdfeed2[9:]
    
    yellow_hour = cleancage[0:2]
    yellow_min = cleancage[3:5]
    yellow_period = cleancage[9:]
    
    blue_hour = birdplay[0:2]
    blue_min = birdplay[3:5]
    blue_period = birdplay[9:]
    
    # -- Alarm
    while True:
        now = datetime.now()

        current_hour = now.strftime("%I")
        current_min = now.strftime("%M")
        current_period = now.strftime("%p")

        if red_period1 == current_period:
            if red_hour1 == current_hour:
                if red_min1 == current_min:
                    GPIO.output(red, True)
                    sleep(0.5)
                    GPIO.output(red, False)
                    sleep(0.5)
        
        if red_period2 == current_period:
            if red_hour2 == current_hour:
                if red_min2 == current_min:
                    GPIO.output(red, True)
                    sleep(0.5)
                    GPIO.output(red, False)
                    sleep(0.5)
        
        if yellow_period == current_period:
            if yellow_hour == current_hour:
                if yellow_min == current_min:
                    GPIO.output(yellow, True)
                    sleep(0.5)
                    GPIO.output(yellow, False)
                    sleep(0.5)
        
        if blue_period == current_period:
            if blue_hour == current_hour:
                if blue_min == current_min:
                    GPIO.output(blue, True)
                    sleep(0.5)
                    GPIO.output(blue, False)
                    sleep(0.5)

def fishalarm():
    # -- Collect the time
    red_hour1 = fishfeed1[0:2]
    red_min1 = fishfeed1[3:5]
    red_period1 = fishfeed1[9:]
    
    red_hour2 = fishfeed2[0:2]
    red_min2 = fishfeed2[3:5]
    red_period2 = fishfeed2[9:]
    
    yellow_hour = cleantank[0:2]
    yellow_min = cleantank[3:5]
    yellow_period = cleantank[9:]
    
    # -- Alarm
    while True:
        now = datetime.now()

        current_hour = now.strftime("%I")
        current_min = now.strftime("%M")
        current_period = now.strftime("%p")

        if red_period1 == current_period:
            if red_hour1 == current_hour:
                if red_min1 == current_min:
                    GPIO.output(red, True)
                    sleep(0.5)
                    GPIO.output(red, False)
                    sleep(0.5)
        
        if red_period2 == current_period:
            if red_hour2 == current_hour:
                if red_min2 == current_min:
                    GPIO.output(red, True)
                    sleep(0.5)
                    GPIO.output(red, False)
                    sleep(0.5)
        
        if yellow_period == current_period:
            if yellow_hour == current_hour:
                if yellow_min == current_min:
                    GPIO.output(yellow, True)
                    sleep(0.5)
                    GPIO.output(yellow, False)
                    sleep(0.5)

def repalarm():
    # -- Collect the time
    red_hour1 = repfeed1[0:2]
    red_min1 = repfeed1[3:5]
    red_period1 = repfeed1[9:]
    
    red_hour2 = repfeed2[0:2]
    red_min2 = repfeed2[3:5]
    red_period2 = repfeed2[9:]
    
    yellow_hour = cleanrep[0:2]
    yellow_min = cleanrep[3:5]
    yellow_period = cleanrep[9:]
    
    # -- Alarm
    while True:
        now = datetime.now()

        current_hour = now.strftime("%I")
        current_min = now.strftime("%M")
        current_period = now.strftime("%p")

        if red_period1 == current_period:
            if red_hour1 == current_hour:
                if red_min1 == current_min:
                    GPIO.output(red, True)
                    sleep(0.5)
                    GPIO.output(red, False)
                    sleep(0.5)
        
        if red_period2 == current_period:
            if red_hour2 == current_hour:
                if red_min2 == current_min:
                    GPIO.output(red, True)
                    sleep(0.5)
                    GPIO.output(red, False)
                    sleep(0.5)
        
        if yellow_period == current_period:
            if yellow_hour == current_hour:
                if yellow_min == current_min:
                    GPIO.output(yellow, True)
                    sleep(0.5)
                    GPIO.output(yellow, False)
                    sleep(0.5)

def rodalarm():
    # -- Collect the time
    red_hour1 = rodfeed1[0:2]
    red_min1 = rodfeed1[3:5]
    red_period1 = rodfeed1[9:]
    
    red_hour2 = rodfeed2[0:2]
    red_min2 = rodfeed2[3:5]
    red_period2 = rodfeed2[9:]
    
    yellow_hour = cleanrod[0:2]
    yellow_min = cleanrod[3:5]
    yellow_period = cleanrod[9:]
    
    # -- Alarm
    while True:
        now = datetime.now()

        current_hour = now.strftime("%I")
        current_min = now.strftime("%M")
        current_period = now.strftime("%p")

        if red_period1 == current_period:
            if red_hour1 == current_hour:
                if red_min1 == current_min:
                    GPIO.output(red, True)
                    sleep(0.5)
                    GPIO.output(red, False)
                    sleep(0.5)
        
        if red_period2 == current_period:
            if red_hour2 == current_hour:
                if red_min2 == current_min:
                    GPIO.output(red, True)
                    sleep(0.5)
                    GPIO.output(red, False)
                    sleep(0.5)
        
        if yellow_period == current_period:
            if yellow_hour == current_hour:
                if yellow_min == current_min:
                    GPIO.output(yellow, True)
                    sleep(0.5)
                    GPIO.output(yellow, False)
                    sleep(0.5)

# -- Functions to generate routines (FUNCTIONAL)
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
    dogrout.withdraw()
    
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
    
    #Button(dog_schedule, text = 'Start Day',  font = ('Courier', 12)).grid(row = 4, column = 1, columnspan = 2)
    Button(dog_schedule, text = 'Start Day',  font = ('Courier', 12), command = dogalarm).grid(row = 4, column = 1, columnspan = 2)

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
    catrout.withdraw()
    
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
    
    #Button(cat_schedule, text = 'Start Day',  font = ('Courier', 12)).grid(row = 4, column = 1, columnspan = 2)
    Button(cat_schedule, text = 'Start Day',  font = ('Courier', 12), command = catalarm).grid(row = 4, column = 1, columnspan = 2)

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
    birdrout.withdraw()
    
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
    
    #Button(bird_schedule, text = 'Start Day',  font = ('Courier', 12)).grid(row = 4, column = 1, columnspan = 2)
    Button(bird_schedule, text = 'Start Day',  font = ('Courier', 12), command = birdalarm).grid(row = 4, column = 1, columnspan = 2)

def fishgen():
    global fishfeed1
    global fishfeed2
    global cleantank
    
    fishfeed1 = fishfeed1.get()
    fishfeed2 = fishfeed2.get()
    
    cleantank = cleantank.get()
    
    fish_schedule = Tk()
    fishrout.withdraw()
    
    fish_schedule.title("Your Customized Fish Routine")
    fish_schedule.geometry("800x480")
    
    Label(fish_schedule, text = "Here is your customized schedule! Each activity is\nsignified by a different color LED light, shown\nby the color of the font for each one.", font = ("Courier", 12, "bold")).grid(row = 0, column = 0, columnspan = 2, padx = 40, pady = 20)
    
    Label(fish_schedule, text = "Feeding Time", font = ("Courier", 12, "bold"), bg = "gray", fg = "red").grid(row = 1, column = 0)
    Label(fish_schedule, text = "Clean Tank Time", font = ("Courier", 12, "bold"), bg = "gray", fg = "yellow").grid(row = 1, column = 1)
    
    Label(fish_schedule, text = fishfeed1, font = ("Courier", 12)).grid(row = 2, column = 0)
    Label(fish_schedule, text = fishfeed2, font = ("Courier", 12)).grid(row = 3, column = 0)
    
    Label(fish_schedule, text = cleantank, font = ("Courier", 12)).grid(row = 2, column = 1)
    
    #Button(fish_schedule, text = 'Start Day',  font = ('Courier', 12)).grid(row = 4, column = 1, columnspan = 2)
    Button(fish_schedule, text = 'Start Day',  font = ('Courier', 12), command = fishalarm).grid(row = 4, column = 1, columnspan = 2)

def repgen():
    global repfeed1
    global repfeed2
    global cleanrep
    
    repfeed1 = repfeed1.get()
    repfeed2 = repfeed2.get()
    
    cleanrep = cleanrep.get()
    
    rep_schedule = Tk()
    reptilerout.withdraw()
    
    rep_schedule.title("Your Customized Reptile Routine")
    rep_schedule.geometry("800x480")
    
    Label(rep_schedule, text = "Here is your customized schedule! Each activity is\nsignified by a different color LED light, shown\nby the color of the font for each one.", font = ("Courier", 12, "bold")).grid(row = 0, column = 0, columnspan = 2, padx = 40, pady = 20)
    
    Label(rep_schedule, text = "Feeding Time", font = ("Courier", 12, "bold"), bg = "gray", fg = "red").grid(row = 1, column = 0)
    Label(rep_schedule, text = "Clean Tank Time", font = ("Courier", 12, "bold"), bg = "gray", fg = "yellow").grid(row = 1, column = 1)
    
    Label(rep_schedule, text = repfeed1, font = ("Courier", 12)).grid(row = 2, column = 0)
    Label(rep_schedule, text = repfeed2, font = ("Courier", 12)).grid(row = 3, column = 0)
    
    Label(rep_schedule, text = cleanrep, font = ("Courier", 12)).grid(row = 2, column = 1)
    
    #Button(rep_schedule, text = 'Start Day',  font = ('Courier', 12)).grid(row = 4, column = 1, columnspan = 2)
    Button(rep_schedule, text = 'Start Day',  font = ('Courier', 12), command = repalarm).grid(row = 4, column = 1, columnspan = 2)

def rodgen():
    global rodfeed1
    global rodfeed2
    global cleanrod
    
    rodfeed1 = rodfeed1.get()
    rodfeed2 = rodfeed2.get()
    
    cleanrod = cleanrod.get()
    
    rod_schedule = Tk()
    rodentrout.withdraw()
    
    rod_schedule.title("Your Customized Rodent Routine")
    rod_schedule.geometry("800x480")
    
    Label(rod_schedule, text = "Here is your customized schedule! Each activity is\nsignified by a different color LED light, shown\nby the color of the font for each one.", font = ("Courier", 12, "bold")).grid(row = 0, column = 0, columnspan = 2, padx = 40, pady = 20)
    
    Label(rod_schedule, text = "Feeding Time", font = ("Courier", 12, "bold"), bg = "gray", fg = "red").grid(row = 1, column = 0)
    Label(rod_schedule, text = "Clean Tank Time", font = ("Courier", 12, "bold"), bg = "gray", fg = "yellow").grid(row = 1, column = 1)
    
    Label(rod_schedule, text = rodfeed1, font = ("Courier", 12)).grid(row = 2, column = 0)
    Label(rod_schedule, text = rodfeed2, font = ("Courier", 12)).grid(row = 3, column = 0)
    
    Label(rod_schedule, text = cleanrod, font = ("Courier", 12)).grid(row = 2, column = 1)
    
    #Button(rod_schedule, text = 'Start Day',  font = ('Courier', 12)).grid(row = 4, column = 1, columnspan = 2)
    Button(rod_schedule, text = 'Start Day',  font = ('Courier', 12), command = rodalarm).grid(row = 4, column = 1, columnspan = 2)

# -- Functions for going back to Routine Maker Home Page (FUNCTIONAL)
def doghome():
    dogrout.withdraw()
    routine()

def cathome():
    catrout.withdraw()
    routine()

def birdhome():
    birdrout.withdraw()
    routine()

def fishhome():
    fishrout.withdraw()
    routine()

def rephome():
    reptilerout.withdraw()
    routine()

def rodhome():
    rodentrout.withdraw()
    routine()

# -- Function for Dog Routine Maker (FUNCTIONAL)
def dog_routine():
    global dogrout
    global walk1
    global walk2
    global dogfeed1
    global dogfeed2
    global bath
    global dogplay
    
    dogrout = Tk()
    rout.withdraw()
    
    dogrout.title("Dog Routine Maker")
    dogrout.geometry("800x480")
    
    Label(dogrout, text = "Below, you can set up a routine\nfor you and your dog!\nEnter times in following format:\n[hr 01-12]:[min 00-59]:[00] AM/PM", font = ("Courier", 20, "bold")).grid(row = 0, column = 0, columnspan = 3, padx = 20)
    
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

# -- Founction for Cat Routine Maker (FUNCTIONAL)
def cat_routine():
    global catrout
    global catfeed1
    global catfeed2
    global catplay
    global cleanlitter
    
    catrout = Tk()
    rout.withdraw()
    
    catrout.title("Cat Routine Maker")
    catrout.geometry("800x480")
    
    Label(catrout, text = "Below, you can set up a routine\nfor you and your cat!\nEnter times in following format:\n[hr 01-12]:[min 00-59]:[00] AM/PM", font = ("Courier", 20, "bold")).grid(row = 0, column = 0, columnspan = 3, padx = 20)
    
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

# -- Function for Bird Routine Maker (FUNCTIONAL)
def bird_routine():
    global birdrout
    global birdfeed1
    global birdfeed2
    global birdplay
    global cleancage
    
    birdrout = Tk()
    rout.withdraw()
    
    birdrout.title("Bird Routine Maker")
    birdrout.geometry("800x480")
    
    Label(birdrout, text = "Below, you can set up a routine\nfor you and your bird!\nEnter times in following format:\n[hr 01-12]:[min 00-59]:[00] AM/PM", font = ("Courier", 20, "bold")).grid(row = 0, column = 0, columnspan = 3, padx = 30)
    
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

# -- Function for Fish Routine Maker (FUNCTIONAL)
def fish_routine():
    global fishrout
    global fishfeed1
    global fishfeed2
    global cleantank
    
    fishrout = Tk()
    rout.withdraw()
    
    fishrout.title("Fish Routine Maker")
    fishrout.geometry("800x480")
    
    Label(fishrout, text = "Below, you can set up a routine\nfor you and your fish!\nEnter times in following format:\n[hr 01-12]:[min 00-59]:[00] AM/PM", font = ("Courier", 20, "bold")).grid(row = 0, column = 0, columnspan = 3, padx = 20)
    
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

# -- Function for Reptile Routine Maker (FUNCTIONAL)
def reptile_routine():
    global reptilerout
    global repfeed1
    global repfeed2
    global cleanrep
    
    reptilerout = Tk()
    rout.withdraw()
    
    reptilerout.title("Reptile Routine Maker")
    reptilerout.geometry("800x480")
    
    Label(reptilerout, text = "Below, you can set up a routine\nfor you and your reptile!\nEnter times in following format:\n[hr 01-12]:[min 00-59]:[00] AM/PM", font = ("Courier", 20, "bold")).grid(row = 0, column = 0, columnspan = 3, padx = 20)
    
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

# -- Function for Rodent Routine Maker (FUNCTIONAL)
def rodent_routine():
    global rodentrout
    global rodfeed1
    global rodfeed2
    global cleanrod
    
    rodentrout = Tk()
    rout.withdraw()
    
    rodentrout.title("Rodent Routine Maker")
    rodentrout.geometry("800x480")
    
    Label(rodentrout, text = "Below, you can set up a routine\nfor you and your rodent!\nEnter times in following format:\n[hr 01-12]:[min 00-59]:[00] AM/PM", font = ("Courier", 20, "bold")).grid(row = 0, column = 0, columnspan = 3, padx = 20)
    
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

# -- Function to return to PetMatcher Home Page (FUNCTIONAL)
def routhome():
    rout.withdraw()
    homepage()

# -- Function for Routine GUI (FUNCTIONAL)
def routine():
    global rout
    
    rout = Tk()
    home.withdraw()
    
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
    
    home_rout = Button(rout, text = "PetMatcher Home Page", font = ("Courier", 12, "bold"), command = routhome)
    home_rout.grid(row = 5, column = 0, columnspan = 2, padx = 50, pady = 50)
    
    rout.mainloop()

# -- Item Browsing (FUNCTIONAL)
def d_home():
    dogitems.withdraw()
    browsemain()

def c_home():
    catitems.withdraw()
    browsemain()

def b_home():
    birditems.withdraw()
    browsemain()

def f_home():
    fishitems.withdraw()
    browsemain()

def rep_home():
    repitems.withdraw()
    browsemain()

def rod_home():
    roditems.withdraw()
    browsemain()

def dogbrowse():
    global dogitems
    
    dogitems = Tk()
    browse.withdraw()
    
    dogitems.title("Dog Essentials")
    dogitems.geometry("800x480")
    
    Label(dogitems, text = "Here, you can find a list\nof essentials for your dog.", font = ("Courier", 20, "bold")).grid(row = 0, column = 0, columnspan = 2, padx = 20)
    
    Label(dogitems, text = "Food", font = ("Courier", 12, "bold"), bg = "gray", width = 15).grid(row = 1, column = 0, padx = 20, pady = 20)
    Label(dogitems, text = "Equipment", font = ("Courier", 12, "bold"), bg = "gray", width = 15).grid(row = 1, column = 1)
    
    # -- Food
    Label(dogitems, text = "Available in:\nPuppy/Adult\nSmall/Medium/Large Breed", font = ("Courier", 8, "bold"), bg = "lightblue").grid(row = 2, rowspan = 2, column = 0)
    Label(dogitems, text = "Canine Salmon Recipe", font = ("Courier", 10)).grid(row = 4, column = 0)
    Label(dogitems, text = "Canine Chicken Recipe", font = ("Courier", 10)).grid(row = 5, column = 0)
    Label(dogitems, text = "Canine Lamb Recipe", font = ("Courier", 10)).grid(row = 6, column = 0)
    Label(dogitems, text = "Canine Pumpkin Recipe", font = ("Courier", 10)).grid(row = 7, column = 0)
    Label(dogitems, text = "Canine Sweet Potato Recipe", font = ("Courier", 10)).grid(row = 8, column = 0)
    
    # -- Equipment
    Label(dogitems, text = "All Available In:\nSmall/Medium/Large Size", font = ("Courier", 8, "bold"), bg = "lightblue").grid(row = 2, rowspan = 2, column = 1)
    Label(dogitems, text = "Training & Transport Crate", font = ("Courier", 10)).grid(row = 4, column = 1)
    Label(dogitems, text = "Dog Bed", font = ("Courier", 10)).grid(row = 5, column = 1)
    Label(dogitems, text = "Food & Water Bowl Set", font = ("Courier", 10)).grid(row = 6, column = 1)
    Label(dogitems, text = "Canine Toy Set", font = ("Courier", 10)).grid(row = 7, column = 1)
    
    Button(dogitems, text = "Back", font = ("Courier", 12), width = 25, command = d_home).grid(row = 9, column = 0, columnspan = 2, padx = 20, pady = 20)
    
    dogitems.mainloop()

def catbrowse():
    global catitems
    
    catitems = Tk()
    browse.withdraw()
    
    catitems.title("Cat Essentials")
    catitems.geometry("800x480")
    
    Label(catitems, text = "Here, you can find a list\nof essentials for your cat.", font = ("Courier", 20, "bold")).grid(row = 0, column = 0, columnspan = 2, padx = 20)
    
    Label(catitems, text = "Food", font = ("Courier", 12, "bold"), bg = "gray", width = 15).grid(row = 1, column = 0, padx = 20, pady = 20)
    Label(catitems, text = "Equipment", font = ("Courier", 12, "bold"), bg = "gray", width = 15).grid(row = 1, column = 1)
    
    # -- Food
    Label(catitems, text = "Available in:\nKitten/Adult", font = ("Courier", 8, "bold"), bg = "lightblue").grid(row = 2, rowspan = 2, column = 0)
    Label(catitems, text = "Feline Tuna Recipe", font = ("Courier", 10)).grid(row = 4, column = 0)
    Label(catitems, text = "FelineChicken Recipe", font = ("Courier", 10)).grid(row = 5, column = 0)
    Label(catitems, text = "Feline Beef Recipe", font = ("Courier", 10)).grid(row = 6, column = 0)
    Label(catitems, text = "Feline Vegetable Recipe", font = ("Courier", 10)).grid(row = 7, column = 0)
    
    # -- Equipment
    Label(catitems, text = "Select Items Available In:\nSmall/Medium/Large Size", font = ("Courier", 8, "bold"), bg = "lightblue").grid(row = 2, rowspan = 2, column = 1)
    Label(catitems, text = "Cat Carrier", font = ("Courier", 10)).grid(row = 4, column = 1)
    Label(catitems, text = "Cat Bed", font = ("Courier", 10)).grid(row = 5, column = 1)
    Label(catitems, text = "Food & Water Bowl Set", font = ("Courier", 10)).grid(row = 6, column = 1)
    Label(catitems, text = "Feline Toy Set", font = ("Courier", 10)).grid(row = 7, column = 1)
    Label(catitems, text = "Scratching Post", font = ("Courier", 10)).grid(row = 8, column = 1)
    
    Button(catitems, text = "Back", font = ("Courier", 12), width = 25, command = c_home).grid(row = 9, column = 0, columnspan = 2, padx = 20, pady = 20)
    
    catitems.mainloop()

def birdbrowse():
    global birditems
    
    birditems = Tk()
    browse.withdraw()
    
    birditems.title("Bird Essentials")
    birditems.geometry("800x480")
    
    Label(birditems, text = "Here, you can find a list\nof essentials for your bird.", font = ("Courier", 20, "bold")).grid(row = 0, column = 0, columnspan = 2, padx = 20)
    
    Label(birditems, text = "Food", font = ("Courier", 12, "bold"), bg = "gray", width = 15).grid(row = 1, column = 0, padx = 20, pady = 20)
    Label(birditems, text = "Equipment", font = ("Courier", 12, "bold"), bg = "gray", width = 15).grid(row = 1, column = 1)
    
    # -- Food
    Label(birditems, text = "Available for:\nAll Domesticated Bird Breeds", font = ("Courier", 8, "bold"), bg = "lightblue").grid(row = 2, rowspan = 2, column = 0)
    Label(birditems, text = "Health Seed Mix", font = ("Courier", 10)).grid(row = 4, column = 0)
    Label(birditems, text = "Nutri-Berry Seed Mix", font = ("Courier", 10)).grid(row = 5, column = 0)
    Label(birditems, text = "Variety Seed Mix", font = ("Courier", 10)).grid(row = 6, column = 0)
    Label(birditems, text = "Fruit Blend Seed Mix", font = ("Courier", 10)).grid(row = 7, column = 0)
    
    # -- Equipment
    Label(birditems, text = "Available for:\nAll Domesticated Bird Breeds", font = ("Courier", 8, "bold"), bg = "lightblue").grid(row = 2, rowspan = 2, column = 1)
    Label(birditems, text = "Bird Perch", font = ("Courier", 10)).grid(row = 4, column = 1)
    Label(birditems, text = "Bird Cage", font = ("Courier", 10)).grid(row = 5, column = 1)
    Label(birditems, text = "Cage Decor Set", font = ("Courier", 10)).grid(row = 6, column = 1)
    Label(birditems, text = "Bird Toy Set", font = ("Courier", 10)).grid(row = 7, column = 1)
    
    Button(birditems, text = "Back", font = ("Courier", 12), width = 25, command = b_home).grid(row = 9, column = 0, columnspan = 2, padx = 20, pady = 20)
    
    birditems.mainloop()

def fishbrowse():
    global fishitems
    
    fishitems = Tk()
    browse.withdraw()
    
    fishitems.title("Fish Essentials")
    fishitems.geometry("800x480")
    
    Label(fishitems, text = "Here, you can find a list\nof essentials for your fish.", font = ("Courier", 20, "bold")).grid(row = 0, column = 0, columnspan = 2, padx = 20)
    
    Label(fishitems, text = "Food", font = ("Courier", 12, "bold"), bg = "gray", width = 15).grid(row = 1, column = 0, padx = 20, pady = 20)
    Label(fishitems, text = "Equipment", font = ("Courier", 12, "bold"), bg = "gray", width = 15).grid(row = 1, column = 1)
    
    # -- Food
    Label(fishitems, text = "Tropical/Blend Available for:\nFresh/Salt Water Fish", font = ("Courier", 8, "bold"), bg = "lightblue").grid(row = 2, rowspan = 2, column = 0)
    Label(fishitems, text = "Tropical Flakes", font = ("Courier", 10)).grid(row = 4, column = 0)
    Label(fishitems, text = "Blend Flakes", font = ("Courier", 10)).grid(row = 5, column = 0)
    Label(fishitems, text = "Betta Buffet Flakes", font = ("Courier", 10)).grid(row = 6, column = 0)
    
    # -- Equipment
    Label(fishitems, text = "Select Items Available In:\nSmall/Medium/Large Size\nfor Fresh/Salt Water", font = ("Courier", 8, "bold"), bg = "lightblue").grid(row = 2, rowspan = 2, column = 1)
    Label(fishitems, text = "Fish Tank", font = ("Courier", 10)).grid(row = 4, column = 1)
    Label(fishitems, text = "Tank Decor Set", font = ("Courier", 10)).grid(row = 5, column = 1)
    Label(fishitems, text = "Tank Bedding", font = ("Courier", 10)).grid(row = 6, column = 1)
    
    Button(fishitems, text = "Back", font = ("Courier", 12), width = 25, command = f_home).grid(row = 8, column = 0, columnspan = 2, padx = 20, pady = 20)
    
    fishitems.mainloop()

def repbrowse():
    global repitems
    
    repitems = Tk()
    browse.withdraw()
    
    repitems.title("Reptile Essentials")
    repitems.geometry("800x480")
    
    Label(repitems, text = "Here, you can find a list\nof essentials for your reptile.", font = ("Courier", 20, "bold")).grid(row = 0, column = 0, columnspan = 2, padx = 20)
    
    Label(repitems, text = "Food", font = ("Courier", 12, "bold"), bg = "gray", width = 15).grid(row = 1, column = 0, padx = 20, pady = 20)
    Label(repitems, text = "Equipment", font = ("Courier", 12, "bold"), bg = "gray", width = 15).grid(row = 1, column = 1)
    
    # -- Food
    Label(repitems, text = "Available for:\nTurtle/Lizard/Snake\n(Frozen Food in Small/Large)", font = ("Courier", 8, "bold"), bg = "lightblue").grid(row = 2, rowspan = 2, column = 0)
    Label(repitems, text = "Frozen Rat - Snake", font = ("Courier", 10)).grid(row = 4, column = 0)
    Label(repitems, text = "Frozen Mice - Snake", font = ("Courier", 10)).grid(row = 5, column = 0)
    Label(repitems, text = "Lettuce Heads - Turtle", font = ("Courier", 10)).grid(row = 6, column = 0)
    Label(repitems, text = "Grasshoppers - Lizard", font = ("Courier", 10)).grid(row = 7, column = 0)
    Label(repitems, text = "Cricket - Lizard", font = ("Courier", 10)).grid(row = 8, column = 0)
    
    # -- Equipment
    Label(repitems, text = "Enclosures Available In:\nSmall/Medium/Large Size\nfor Turtle/Lizard/Snake", font = ("Courier", 8, "bold"), bg = "lightblue").grid(row = 2, rowspan = 2, column = 1)
    Label(repitems, text = "Reptile Enclosure", font = ("Courier", 10)).grid(row = 4, column = 1)
    Label(repitems, text = "Enclosure Decor Set", font = ("Courier", 10)).grid(row = 5, column = 1)
    Label(repitems, text = "Enclosure Bedding", font = ("Courier", 10)).grid(row = 6, column = 1)
    
    Button(repitems, text = "Back", font = ("Courier", 12), width = 25, command = rep_home).grid(row = 10, column = 0, columnspan = 2, padx = 20, pady = 20)
    
    repitems.mainloop()

def rodbrowse():
    global roditems
    
    roditems = Tk()
    browse.withdraw()
    
    roditems.title("Rodent Essentials")
    roditems.geometry("800x480")
    
    Label(roditems, text = "Here, you can find a list\nof essentials for your rodent.", font = ("Courier", 20, "bold")).grid(row = 0, column = 0, columnspan = 2, padx = 20)
    
    Label(roditems, text = "Food", font = ("Courier", 12, "bold"), bg = "gray", width = 15).grid(row = 1, column = 0, padx = 20, pady = 20)
    Label(roditems, text = "Equipment", font = ("Courier", 12, "bold"), bg = "gray", width = 15).grid(row = 1, column = 1)
    
    # -- Food
    Label(roditems, text = "Brands Available for:\nRat/Mouse/Hamster/Guinea Pig", font = ("Courier", 8, "bold"), bg = "lightblue").grid(row = 2, column = 0)
    Label(roditems, text = "Oxbow Feed", font = ("Courier", 10)).grid(row = 3, column = 0)
    Label(roditems, text = "Kaytee Feed", font = ("Courier", 10)).grid(row = 4, column = 0)
    Label(roditems, text = "Mazuri Feed", font = ("Courier", 10)).grid(row = 5, column = 0)
    
    # -- Equipment
    Label(roditems, text = "Enclosures Available In:\nSmall/Medium/Large Size", font = ("Courier", 8, "bold"), bg = "lightblue").grid(row = 2, column = 1)
    Label(roditems, text = "Rodent Enclosure", font = ("Courier", 10)).grid(row = 3, column = 1)
    Label(roditems, text = "Enclosure Decor Set", font = ("Courier", 10)).grid(row = 4, column = 1)
    Label(roditems, text = "Enclosure Bedding", font = ("Courier", 10)).grid(row = 5, column = 1)
    Label(roditems, text = "Feed Bowl", font = ("Courier", 10)).grid(row = 6, column = 1)
    Label(roditems, text = "Exercise Wheel", font = ("Courier", 10)).grid(row = 7, column = 1)
    Label(roditems, text = "Hanging Water Bottle", font = ("Courier", 10)).grid(row = 8, column = 1)
    
    Button(roditems, text = "Back", font = ("Courier", 12), width = 25, command = rod_home).grid(row = 9, column = 0, columnspan = 2, padx = 20, pady = 20)
    
    roditems.mainloop()

def browsehome():
    browse.withdraw()
    homepage()

def browsemain():
    global browse
    
    browse = Tk()
    home.withdraw()
    
    browse.title("PetMatcher - Browse Items")
    browse.geometry("800x480")
    
    Label(browse, text = "What type of pet are you browsing for?", font = ("Courier", 14, "bold")).grid(row = 0, column = 0, columnspan = 3, padx = 20, pady = 20)
    
    dog = Button(browse, text = "Dog", font = ("Courier", 12), width = 25, command = dogbrowse)
    dog.grid(row = 1, column = 0, padx = 20, pady = 10)
    
    cat = Button(browse, text = "Cat", font = ("Courier", 12), width = 25, command = catbrowse)
    cat.grid(row = 1, column = 1, padx = 20, pady = 10)
    
    bird = Button(browse, text = "Bird", font = ("Courier", 12), width = 25,  command = birdbrowse)
    bird.grid(row = 2, column = 0, padx = 20, pady = 10)
    
    fish = Button(browse, text = "Fish", font = ("Courier", 12), width = 25, command = fishbrowse)
    fish.grid(row = 2, column = 1, padx = 20, pady = 10)
    
    reptile = Button(browse, text = "Reptile", font = ("Courier", 12), width = 25, command = repbrowse)
    reptile.grid(row = 3, column = 0, padx = 20, pady = 10)
    
    rodent = Button(browse, text = "Rodent", font = ("Courier", 12), width = 25, command = rodbrowse)
    rodent.grid(row = 3, column = 1, padx = 20, pady = 10)
    
    home_rout = Button(browse, text = "PetMatcher Home Page", font = ("Courier", 12, "bold"), command = browsehome)
    home_rout.grid(row = 5, column = 0, columnspan = 2, padx = 50, pady = 50)
    
    browse.mainloop()

# -- Home Page (FUNCTIONAL)
def homepage():
    global home
    
    home = Tk()
    home.title("PetMatcher")
    home.geometry(f"{HEIGHT}x{WIDTH}")
    home.config(bg='#E0EEEF')
    
    LabelFrame(home, pady=20).place(height=100, width=650, x=70, y=60)
    Label(home, text = "Welcome to PetMatcher", font = ("Courier", 22, "bold")).place(x=100, y=80)
    
    # create a frame 
    output = LabelFrame(home,
               pady=20, bg='lightgrey', bd=4).place(height=250, width=650, x=70, y=200)
    
    # create buttons
    Button(home, text = "Take the PetMatcher Quiz", font = ("Courier", 12), width = 40, height = 1, command = quiz_setup).place(x=110, y=250)
    Button(home, text = "View Essential Items for your Pet", font = ("Courier", 12), width = 40, height = 1, command = browsemain).place(x=110, y=300)
    Button(home, text = "Make a Custom Routine for your Pet", font = ("Courier", 12), width = 40, height = 1, command = routine).place(x=110, y=350)
    
    home.mainloop()
    
# -- MAIN CODE
HEIGHT = 804
WIDTH = 480
homepage()