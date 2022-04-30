# import modules
from tkinter import *

# DOG CLASS
class Dog():
    qualities = ['Affectionate', 'Energetic']
    def __init__(self, counter=0):
        # set attributes
        self._counter = counter
# CAT CLASS
class Cat():
    qualities = ['Cuddly', 'Curious']
    def __init__(self):
        # set attributes
        self._counter = 0
# FISH CLASS
class Fish():
    qualities = ['Child-Friendly', 'Quiet']    
    def __init__(self):
        # set attributes
        self._counter = 0
# REPTILE CLASS
class Reptile():
    qualities = ['Independent']
    def __init__(self):
        # set attributes
        self._counter = 0
        
# BIRD CLASS
class Bird():
    qualities = ['Talkative', 'Care-free']
    def __init__(self):
        # set attributes
        self._counter = 0
# RODENTS CLASS
class Rodents():
    qualities = ['Inteligent']
    def __init__(self):
        # set attributes
        self._counter = 0

def run(widget, num):
    global computation
    # Method: computation()
    def computation():
        # compute user answers
        '''Xcompute answers for question 1'''
        if answers[1] == 'Less Than 5 Hours':
            d._counter += 1 # add to dog counter
            c._counter += 1 # add to cat counter
            r._counter += 1 # add to reptile counter
            b._counter += 1 # add to bird counter
            f._counter += 1 # add to fish counter
            rd._counter += 1 # add to rodent counter
        elif answers[1] == '5-8 Hours':
            c._counter += 1 # add to cat counter
            r._counter += 1 # add to reptile counter
            b._counter += 1 # add to bird counter
            f._counter += 1 # add to fish counter
            rd._counter += 1 # add to rodent counter
        elif answers[1] == '8-10 Hours':
            r._counter += 1 # add to reptile counter
            b._counter += 1 # add to bird counter
            f._counter += 1 # add to fish counter
            rd._counter += 1 # add to rodent counter
        elif answers[1] == '10-15 Hours':
            f._counter += 1 # add to fish counter
            r._counter += 1 # add to reptile counter
            b._counter += 1 # add to bird counter
        '''Xcompute answers for question 2'''
        if answers[2] == 'Not Active':
            f._counter += 1 # add to fish counter
            r._counter += 1 # add to reptile counter
        elif answers[2] == 'Minimally Active':
            b._counter += 1 # add to bird counter
            rd._counter += 1 # add to rodent counter
        elif answers[2] == 'Decently Active':
            c._counter += 1 # add to cat counter
        elif answers[2] == 'Very Active':
            d._counter += 1 # add to dog counter
        '''Xcompute answers for question 3'''
        if question_3_values['Child-Friendly'] == 1:
            # append EXTRA points to fish
            f._counter += 10
            d._counter += 5
        elif question_3_values['Affectionate'] == 1:
            # append EXTRA points to dog
            d._counter += 10
            # append EXTRA points to cat
            c._counter += 5
        elif question_3_values['Energetic'] == 1:
            # append EXTRA points to cat
            c._counter += 5
            # append EXTRA points to dog
            d._counter += 10
            # append EXTRA points to bird
            b._counter += 8
        elif question_3_values['Intelligent'] == 1:
            # append EXTRA points to bird
            b._counter += 10
        if question_3_values['Care-Free'] == 1:
            # append EXTRA points to reptile
            r._counter += 10
        elif question_3_values['Cuddly'] == 1:
            # append EXTRA points to cat
            c._counter += 10
            # append EXTRA points to dog
            # append EXTRA points to rodent
        elif question_3_values['Curious'] == 1:
            # append EXTRA points to rodent
            rd._counter += 10
        elif question_3_values['Independent'] == 1:
            # append EXTRA points to cat
            c._counter += 10
        '''compute answers for question 4'''
        if answers[4] == 'Low Maintenance':
            f._counter += 1 # add to fish counter
            r._counter += 1 # add to reptile counter
            rd._counter += 1 # add to rodent counter
        elif answers[4] == 'Average Maintenance':
            b._counter += 1 # add to bird counter
        elif answers[4] == 'High Maintence':
            d._counter += 1 # add to dog counter
            c._counter += 1 # add to cat counter
        '''Xcompute answers for question 5'''
        if answers[5] == 'Enough For Basic Needs':
            f._counter += 1 # add to fish counter
            rd._counter += 1 # add to rodent counter
        elif answers[5] == 'Enough For Basic Necessities And Inexpensive Recurring Costs':
            r._counter += 1 # add to reptile counter
            b._counter += 1 # add to bird counter
        elif answers[5] == 'Enough For Spoiling & Necessities':
            d._counter += 1 # add to dog counter
            c._counter += 1 # add to cat counter
        '''Xcompute answers for question 6'''
        if answers[1] == 'Small - Not Alot Of Space To Roam; No Yard':
            f._counter += 1 # add to fish counter
            r._counter += 1 # add to reptile counter
            rd._counter += 1 # add to rodent counter
        elif answers[2] == 'Small - With Yard':
            d._counter += 1 # add to dog counter
            c._counter += 1 # add to cat counter
            b._counter += 1 # add to bird counter
            f._counter += 1 # add to fish counter
            r._counter += 1 # add to reptile counter
            rd._counter += 1 # add to rodent counter
        elif answers[3] == 'Average - Some Space To Roam; No Yard':
            d._counter += 1 # add to dog counter
            c._counter += 1 # add to cat counter
            f._counter += 1 # add to fish counter
            r._counter += 1 # add to reptile counter
            rd._counter += 1 # add to rodent counter
        elif answers[4] == 'Average - With Yard':
            d._counter += 1 # add to dog counter
            c._counter += 1 # add to cat counter
            b._counter += 1 # ad to bird counter
            f._counter += 1 # add to fish counter
            r._counter += 1 # add to reptile counter
            rd._counter += 1 # add to rodent counter
        elif answers[4] == 'Big - Lots Of Space To Roam; No Yard':
            d._counter += 1 # add to dog counter
        elif answers[4] == 'Big - With Yard':
            d._counter += 1 # add to dog counter
            c._counter += 1 # add to cat counter
            b._counter += 1 # ad to bird counter
            f._counter += 1 # add to fish counter
            r._counter += 1 # add to reptile counter
            rd._counter += 1 # add to rodent counter
        # assign new pet counters to a variable (int)
        # then append to a petList
        myDog = d._counter
        petDict['Dog'] = d._counter
        myCat = c._counter
        petDict['Cat'] = myCat
        myFish = f._counter
        petDict['Fish'] = myFish
        myRep = r._counter  
        petDict['Reptile'] = myRep
        myBird = b._counter
        petDict['Bird'] = myBird
        myRod = rd._counter
        petDict['Rodent'] = myRod
        # retrieve the max dictionary value from petList
        global maxVal
        maxVal = max(petDict, key=petDict.get)
        global data
        data = sorted(petDict.items(), key=lambda x:x[1], reverse=True)
        data = data[0:3]
        print(data)
    # create dictionary to track pet values
    global petDict
    petDict = {'Dog': 0, 'Cat': 0, 'Fish': 0, 'Reptile': 0,
               'Bird': 0, 'Rodent': 0}
    # create instances of each pet class
    d = Dog()
    c = Cat()
    f = Fish()
    r = Reptile()
    b = Bird()
    rd = Rodents()
    
    # retrieve question entry
    answer = widget.get()
    # add values to dictionary: answers
    if num == 1:
        answers[1] = answer
    elif num == 2:
        answers[2] = answer
    elif num == 3:
        answers[3] = answer
    elif num == 4:
        answers[4] = answer
    elif num == 5:
        answers[5] = answer
    elif num == 6:
        answers[6] = answer
        computation()
    #print(petDict) # print dictionary
    #print(Quiz.answers)
            
            #print(f'Your best matched pet is {maxVal}') # print max val of dictionary
def quizHome():
    def nextPage():
        quizHome.withdraw()
        question1()
    def prevPage():
        quizHome.withdraw()
    global quizHome
    # create a new window
    quizHome = Tk()
    quizHome.geometry(f'{WIDTH}x{HEIGHT}')
    quizHome.title('PetMatcher Quiz')
    quizHome.resizable(False, False)
    quizHome.eval('tk::PlaceWindow . center')
    quizHome.config(bg='#F1FFFF')
    # place everythin in a label frame
    LabelFrame(quizHome, bg="#E3EFEF", bd=4).place(height=380, width=420, x=200, y=60)
    # create a label
    startLabel = Label(quizHome, text='Take The\nPetMatcher Quiz',
                       font = ('Courier', 12),
                        height=2, width=40, padx=5, pady=5,
                       bd=0, bg='#E3EFEF').place(width=300, x=260, y=100)
    # setup buttons
    startButton = Button(quizHome, text="START", font = ('Courier', 10),
                        height=1,width=8, bd=5, padx=20, pady=2, bg='#8E8F8F',
                            command=nextPage).place(x=343, y=270)
    returnButton = Button(quizHome, text="RETURN", font = ('Courier', 10),
                              height=1, width=8, bd=5, padx=20, pady=2,
                              bg='#8E8F8F', command=prevPage).place(x=345,y=340)
    quizHome.mainloop()
def question1():
    def prevPage():
        question1.withdraw()
        quizHome()
    def nextPage():
        question1.withdraw()
        run(clicked, 1)
        question2()
    # create a new window
    question1 = Tk()
    question1.config(bg='#F1FFFF')
    question1.geometry(f'{WIDTH}x{HEIGHT}')
    question1.title('PetMatcher Quiz')
    question1.resizable(False, False)
    question1.eval('tk::PlaceWindow . center')
    
    # place everythin in a label frame
    LabelFrame(question1, bg="#E3EFEF", bd=4).place(height=300, width=400, x=200, y=60)
    # setup question
    questionLabel = Label(question1, text="How Busy Are You\nOn A Daily Basis?",
                          font = ('Courier', 12),
                        height=2, width=40, padx=5, pady=5,
                       bd=0, bg='#E3EFEF')
    questionLabel.place(width=350, x=230,y=100)
    # setup question options
    options = [
            'Less Than 5 Hours', '5-8 Hours',
            '8-10 Hours', '10-15 Hours'
        ]
    clicked = StringVar()
    clicked.set(options[0])
    drop = OptionMenu(question1, clicked, *options)
    drop.config(width=20)
    drop.config(height=2)
    drop.place(x=270, y=160)
    # setup button to continue to previous question
    backButton = Button(question1, text='BACK', font = ('Courier', 10),
                                 height=1, width=8, bd=5, padx=20, pady=2, bg='#8E8F8F',
                                 command=prevPage).place(x=50,y=380)
    # setup button to continue to next question
    nextButton = Button(question1, text='NEXT',  font = ('Courier', 10),
                                 height=1,width=8, bd=5, padx=20, pady=2, bg='#8E8F8F',
                                 command=nextPage)
    nextButton.place(x=640, y=380)
def question2():
    def prevPage():
        question2.withdraw()
        question1()
    def nextPage():
        question2.withdraw()
        run(clicked, 2)
        question3()
    # create a new window
    question2 = Tk()
    question2.config(bg='#F1FFFF')
    question2.geometry(f'{WIDTH}x{HEIGHT}')
    question2.title('PetMatcher Quiz')
    question2.resizable(False, False)
    question2.eval('tk::PlaceWindow . center')
    
    # place everythin in a label frame
    LabelFrame(question2, bg="#E3EFEF", bd=4).place(height=300, width=420, x=200, y=60)
    # setup question image
    questionImageLabel = Label(question2, text="How Active Are You?",
                               font = ('Courier', 12),
                        height=2, width=40, padx=5, pady=5,
                       bd=0, bg='#E3EFEF')
    questionImageLabel.place(width=350, x=230, y=100)
    # setup question options
    options = [
            'Not Active', 'Minimally Active',
            'Decently Active', 'Very Active'
            ]
    clicked = StringVar()
    clicked.set(options[0])
    drop = OptionMenu(question2, clicked, *options)
    drop.config(width=20)
    drop.config(height=2)
    drop.place(x=270, y=160)
    # setup button to continue to previous question
    backButton = Button(question2, text='BACK', font = ('Courier', 10),
                                 height=1, width=8, bd=5, padx=20, pady=2, bg='#8E8F8F',
                                 command=prevPage).place(x=50,y=380)
    # setup button to continue to next question
    nextButton = Button(question2, text='NEXT', font = ('Courier', 10),
                                 height=1,width=8, bd=5, padx=20, pady=2, bg='#8E8F8F',
                                 command=nextPage)
    nextButton.place(x=640, y=380)
def question3():
    def prevPage():
        question3.withdraw()
        question2()
    def nextPage():
        global question_3_values
        question_3_values = {"Child-Friendly": 0,"Affectionate": 0,"Energetic": 0,"Intelligent": 0,
                      "Care-Free": 0,"Cuddly": 0,"Curious": 0,"Independent": 0,}
        # function takes in an entry as input and calculates
        val1 = Checkbutton1.get()
        question_3_values['Child-Friendly'] = val1
        val2 = Checkbutton2.get()
        question_3_values['Affectionate'] = val2
        val3 = Checkbutton3.get()
        question_3_values['Energetic'] = val3
        val4 = Checkbutton4.get()
        question_3_values['Intelligent'] = val4
        val5 = Checkbutton5.get()
        question_3_values['Care-Free'] = val5
        val6 = Checkbutton6.get()
        question_3_values['Cuddly'] = val6
        val7 = Checkbutton7.get()
        question_3_values['Curious'] = val7
        val8 = Checkbutton8.get()
        question_3_values['Independent'] = val8
        computation()
        question3.withdraw()
        question4()
    # create a new window
    question3 = Tk()
    question3.config(bg='#F1FFFF')
    question3.geometry(f'{WIDTH}x{HEIGHT}')
    question3.title('PetMatcher Quiz')
    question3.resizable(False, False)
    question3.eval('tk::PlaceWindow . center')
    
    # place everythin in a label frame
    LabelFrame(question3, bg="#E3EFEF", bd=4).place(height=320, width=640, x=80, y=30)
    # setup question image
    questionLabel = Label(question3, text="What Qualities Are Most Appealing\nTo You In A Pet?",
                               font = ('Courier', 12),
                        height=2, padx=5, pady=5,
                       bd=0, bg='#E3EFEF')
    questionLabel.place(x=160,y=50)
    # setup question options
        
    Checkbutton1 = IntVar() # Fish append more points
    button1 = Checkbutton(question3, text='Child-Friendly', variable=Checkbutton1,
            onvalue=1, offvalue=0, height=2, width=10, padx=20, bg='#D5DFDF').place(x=90, y=150)
    Checkbutton2 = IntVar() # Dog append more points
    button2 = Checkbutton(question3, text='Affectionate', variable=Checkbutton2,
            onvalue=1, offvalue=0, height=2, width=10, padx=20, bg='#D5DFDF').place(x=90, y=250)
    Checkbutton3 = IntVar() # Bird append more points
    button3 = Checkbutton(question3, text='Energetic', variable=Checkbutton3,
            onvalue=1, offvalue=0, height=2, width=10, padx=20, bg='#D5DFDF').place(x=240, y=150)
    Checkbutton4 = IntVar() # Cat append more points
    button4 = Checkbutton(question3, text='Intelligent', variable=Checkbutton4,
            onvalue=1, offvalue=0, height=2, width=10, padx=20, bg='#D5DFDF').place(x=240, y=250)
    Checkbutton5 = IntVar() #
    button5 = Checkbutton(question3, text='Care-Free', variable=Checkbutton5,
            onvalue=1, offvalue=0, height=2, width=10, padx=20, bg='#D5DFDF').place(x=390, y=150)
    Checkbutton6 = IntVar() # Cat append more points
    button6 = Checkbutton(question3, text='Cuddly', variable=Checkbutton6,
            onvalue=1, offvalue=0, height=2, width=10, padx=20, bg='#D5DFDF').place(x=390, y=250)
    Checkbutton7 = IntVar() # Rodent append more points
    button7 = Checkbutton(question3, text='Curious', variable=Checkbutton7,
            onvalue=1, offvalue=0, height=2, width=10, padx=20, bg='#D5DFDF').place(x=540, y=150)
    Checkbutton8 = IntVar() # Reptile append more points
    button8 = Checkbutton(question3, text='Independent', variable=Checkbutton8,
            onvalue=1, offvalue=0, height=2, width=10, padx=20, bg='#D5DFDF').place(x=540, y=250)
    # setup button to continue to previous question
    backButton = Button(question3, text='BACK', font = ('Courier', 10),
                height=1, width=8, bd=5, padx=20, pady=2, bg='#8E8F8F',
                command=prevPage).place(x=50,y=380)
    # setup button to continue to next question
    nextButton = Button(question3, text='NEXT', font = ('Courier', 10),
                height=1,width=8, bd=5, padx=20, pady=2, bg='#8E8F8F',
                command=nextPage).place(x=640,y=380)
def question4():
    def prevPage():
        question4.withdraw()
        question3()
    def nextPage():
        question4.withdraw()
        run(clicked, 4)
        question5()
    # create a window
    question4 = Tk()
    question4.config(bg='#F1FFFF')
    question4.geometry(f'{WIDTH}x{HEIGHT}')
    question4.title('PetMatcher Quiz')
    question4.resizable(False, False)
    question4.eval('tk::PlaceWindow . center')
    
    # place everythin in a label frame
    LabelFrame(question4, bg="#E3EFEF", bd=4).place(height=300, width=420, x=200, y=60)
    # setup question image
    questionLabel = Label(question4, text="What Level of Need Could\nYou Handle In A Pet?",
                          font = ('Courier', 11),
                        height=2, width=30, padx=5, pady=5,
                       bd=0, bg='#E3EFEF')
    questionLabel.place(x=205, y=100)
    # setup question options
    options = [
            'Low Maintenance', 'Average Maintenance','High Maintenance'
            ]
    clicked = StringVar()
    clicked.set(options[0])
    drop = OptionMenu(question4, clicked, *options)
    drop.config(width=20)
    drop.config(height=2)
    drop.place(x=270, y=160)
    # setup button to continue to previous question
    backButton = Button(question4, text='BACK', font = ('Courier', 10),
                    height=1, width=8, bd=5, padx=20, pady=2, bg='#8E8F8F',
                    command=prevPage).place(x=50,y=380)
    # setup button to continue to next question
    nextButton = Button(question4, text='NEXT', font = ('Courier', 10),
                        height=1,width=8, bd=5, padx=20, pady=2, bg='#8E8F8F',
                command=nextPage).place(x=640, y=380)
def question5():
    def prevPage():
        question5.withdraw()
        question4()
    def nextPage():
        question5.withdraw()
        run(clicked, 5)
        question6()
    # create a window
    question5 = Tk()
    question5.config(bg='#F1FFFF')
    question5.geometry(f'{WIDTH}x{HEIGHT}')
    question5.title('PetMatcher Quiz')
    question5.resizable(False, False)
    question5.eval('tk::PlaceWindow . center')

    # place everythin in a label frame
    LabelFrame(question5, bg="#E3EFEF", bd=4).place(height=300, width=500, x=160, y=60)
    # setup question image
    questionLabel = Label(question5, text="What Does Your Budget\nLook Like?",
                          font = ('Courier', 12),
                        height=2, width=40, padx=5, pady=5,
                       bd=0, bg='#E3EFEF')
    questionLabel.place(width=350, x=230,y=100)
    # setup question options
    options = [
        'Enough For Basic Needs', "Enough For Basic Necessities & Inexpensive Recurring Costs",
        'Enough For Spoiling & Necessities'
        ]
    clicked = StringVar()
    clicked.set(options[0])
    drop = OptionMenu(question5, clicked, *options)
    drop.config(width=40)
    drop.config(height=2)
    drop.place(x=180, y=160)
    # setup button to continue to previous question
    backButton = Button(question5, text='BACK', font = ('Courier', 10),
                             height=1, width=8, bd=5, padx=20, pady=2, bg='#8E8F8F',
                             command=prevPage).place(x=50,y=380)
    # setup button to continue to next question
    nextButton = Button(question5, text='NEXT', font = ('Courier', 10),
                             height=1,width=8, bd=5, padx=20, pady=2, bg='#8E8F8F',
                             command=nextPage).place(x=640, y=380)
def question6():
    def prevPage():
        question6.withdraw()
        question5()
    def nextPage():
        question6.withdraw()
        run(clicked, 6)
        userResultsPage()
    # create a window
    question6 = Tk()
    question6.config(bg='#F1FFFF')
    question6.geometry(f'{WIDTH}x{HEIGHT}')
    question6.title('PetMatcher Quiz')
    question6.resizable(False, False)
    question6.eval('tk::PlaceWindow . center')
    
    # place everythin in a label frame
    LabelFrame(question6, bg="#E3EFEF", bd=4).place(height=300, width=500, x=160, y=60)
    # setup question image
    questionLabel = Label(question6, text="What Is Your Living\nAccdomadation Like?",
                          font = ('Courier', 12),
                        height=2, width=40, padx=5, pady=5,
                       bd=0, bg='#E3EFEF')
    questionLabel.place(width=380, x=215,y=100)
    # setup question options
    options = [
        'Small - Not Alot Of Space To Roam; No Yard',
        'Small - With Yard',
        'Average - Some Space To Roam; No Yard',
        'Average - With Yard',
        'Big - Lots Of Space To Roam; No Yard',
        'Big - With Yard'
        ]
    clicked = StringVar()
    clicked.set(options[0])
    drop = OptionMenu(question6, clicked, *options)
    drop.config(width=40)
    drop.config(height=2)
    drop.place(x=180, y=160)
    # setup button to continue to previous question
    backButton = Button(question6, text='BACK', font = ('Courier', 10),
                             height=1, width=8, bd=5, padx=20, pady=2, bg='#8E8F8F',
                             command=prevPage).place(x=50,y=380)
    # setup button to continue to next question
    nextButton = Button(question6, text='FINISH', font = ('Courier', 10),
                             height=1,width=8, bd=5, padx=20, pady=2, bg='#8E8F8F',
                             command=nextPage).place(x=640, y=380)
def userResultsPage():
    def prevPage():
        userResultsPage.withdraw()
        question6()
    def nextPage():
        userResultsPage.withdraw()
    # create a window
    userResultsPage = Tk()
    userResultsPage.config(bg='#F1FFFF')
    userResultsPage.geometry(f'{WIDTH}x{HEIGHT}')
    userResultsPage.title('PetMatcher Quiz')
    userResultsPage.resizable(False, False)
    userResultsPage.eval('tk::PlaceWindow . center')
    # put everythinhg in a frame
    LabelFrame(userResultsPage, bg="#E3EFEF", bd=4).place(height=400, width=420, x=200, y=60)
    # setup canvas
    '''
    
    Display data for top picks of all animals. The leading score is the users 
    most compatible animal the last being the least compatible animal.
    
    
    # create neccessary data for bar graph 
    newData = [x[1]*100 for x in data]
    #print(data)
    cWidth = 250 # canvas width
    cHeight = 200 # canvas height
    # create canvas
    c = Canvas(userResultsPage, width=cWidth, height=cHeight, bg='grey')
    c.place(x=285, y=80)
    # size the bar graph
    # hieghest y value = maxDataValue * yStretch
    yStretch = 25
    # gap between lower canvas edge and x axis
    yGap = 2
    # stretch enough to get all data items in
    xStretch = 20
    xWidth = 20
    # gap between left canvas edge and y axis
    xGap = 70
    
    colors = ['', '', '', '', '', '']
    for x, y in enumerate(newData):
        # calculate rectangle coordinates (intVals) for each bar
        x0 = x * xStretch + x * xWidth + xGap
        y0 = cHeight - (y * yStretch + yGap)
        x1 = x * xStretch + x * xWidth + xWidth + xGap
        y1 = cHeight - yGap
        # draw the bar
        c.create_rectangle(x0, y0, x1, y1, fill='red')
        # put the y value above each bar
        c.create_text(x0+2, y0, anchor=SW, text=str(y))
    '''
    # create a label
    var = StringVar()
    var.set(f'Your Results Are In')
    pckLabel = Label(userResultsPage, text='Your Results Are In',
                     font = ('Courier', 10),
                        height=2, width=30, padx=5, pady=5,
                       bd=0, bg='#E3EFEF').place(x=230, y=250)
    # create a top pick label
    topPick = Label(userResultsPage, text=f"Your Best Matched Pet is A {maxVal}",
                        font = ('Courier', 10),
                        height=2, width=30, padx=5, pady=5,
                       bd=0, bg='#E3EFEF').place(x=230, y=320)
    # setup button to continue to previous question
    backButton = Button(userResultsPage, text='BACK', font = ('Courier', 10),
                             height=1, width=8, bd=5, padx=20, pady=2, bg='#8E8F8F',
                             command=prevPage).place(x=50,y=380)
    # setup button to continue to next question
    nextButton = Button(userResultsPage, text='FINISH', font = ('Courier', 10),
                             height=1,width=8, bd=5, padx=20, pady=2, bg='#8E8F8F',
                             command=nextPage).place(x=640, y=380)
### MAIN CODE ###
# window size
WIDTH = 804
HEIGHT = 480
# quiz answers
# user answers
answers = {1: '', 2: '', 3: '', 4: '', 5: '', 6: ''}
#quizHome()