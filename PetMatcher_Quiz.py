# import modules
from tkinter import *


# GUI CLASS
# This class provides optimization to the canvas
class GUI_:
    
    pass

class Pet:
    pass
# DOG CLASS
class Dog(Pet):
    qualities = ['Affectionate', 'Energetic']
    def __init__(self, counter=0):
        # set attributes
        self._counter = counter
# CAT CLASS
class Cat(Pet):
    qualities = ['Cuddly', 'Curious']
    def __init__(self):
        # set attributes
        self._counter = 0
# FISH CLASS
class Fish(Pet):
    qualities = ['Child-Friendly', 'Quiet']    
    def __init__(self):
        # set attributes
        self._counter = 0
# REPTILE CLASS
class Reptile(Pet):
    qualities = ['Independent']
    def __init__(self):
        # set attributes
        self._counter = 0
        
# BIRD CLASS
class Bird(Pet):
    qualities = ['Talkative', 'Care-free']
    def __init__(self):
        # set attributes
        self._counter = 0
# RODENTS CLASS
class Rodents(Pet):
    qualities = ['Inteligent']
    def __init__(self):
        # set attributes
        self._counter = 0
        
# Quiz class
class Quiz(Tk):
    # class variables
    # window size
    WIDTH = 804
    HEIGHT = 480
    # user answers
    answers = {1: '', 2: '', 3: '', 4: '', 5: '', 6: ''}
    # the constructor
    def __init__(self):
        super().__init__()
        self.title("PETMATCHER_PROTYOPE")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.resizable(False, False)
        self.eval('tk::PlaceWindow . center')
        
    # METHOD: exit()
    # End Application
    def exitMe(self):
        exit(0)
    # METHOD: setupGUI()
    # Applications parameters
    def setupGUI(self):
        # transition function
        def clicked():
            #self.myLabel.config(text="You clicked the button...")
            self.question1()
        # setup background
        # add a image file
        self.backGroundImage = PhotoImage(file='Pet_II.png')
        # show image using label
        self.backGroundImageLabel = Label(self, image=self.backGroundImage).place(x=0, y=0)
        
        # image button: currently does not work
        '''
        # create Frame
        self.frame1 = Frame(self).pack(pady=20)
        self.loginBtn = PhotoImage(file='button1.png')

        self.imgLabel = Label(image=self.loginBtn)
        #imgLabel.pack(pady=20)

        self.myButton = Button(self.frame1, image=self.loginBtn, command=clicked, borderwidth=0).pack(pady=20)

        #self.myLabel = Label(self, text='').pack(pady=20)
        '''
        # setup button
        # import image using PhotoImage function
        self.buttonImage = PhotoImage(file='button1.png')
        # create a label for button event
        self.imageLabel = Label(image=self.buttonImage)
        # create a dummy button and pass the image
        self.startButton = Button(self, text="Start",
                        height=1,width=8, bd=5, padx=20, pady=2, bg='teal',
                            command=clicked).place(x=350, y=300)
        
        
    def question1(self):
        def show():
            myLabel = Label(self, text=clicked.get()).place(x=0, y=0)
        def runMe():
            show()
            # function takes in an entry as input and calculates
            self.run(clicked, 1)
            self.question2()
        # setup background image
        self.backGroundImage = PhotoImage(file='Pet_IIB.png')
        self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y=0)
        # setup question image
        self.questionImage = PhotoImage(file='question_1.png')
        self.questionImageLabel = Label(self, image=self.questionImage, borderwidth=0)
        self.questionImageLabel.place(x=250,y=100)
        # setup question options
        options = [
            'Less Than 5 Hours', '5-8 Hours',
            '8-10 Hours', '10-15 Hours'
            ]
        clicked = StringVar()
        clicked.set(options[0])
        self.drop = OptionMenu(self, clicked, *options)
        self.drop.config(width=20)
        self.drop.config(height=2)
        self.drop.place(x=325, y=250)
        # setup button to continue to previous question
        self.backButton = Button(self, text='<\BACK',
                                 height=1, width=8, bd=5, padx=20, pady=2, bg='teal',
                                 command=self.setupGUI).place(x=50,y=380)
        # setup button to continue to next question
        self.nextButton = Button(self, text='NEXT/>', 
                                 height=1,width=8, bd=5, padx=20, pady=2, bg='teal',
                                 command=runMe)
        self.nextButton.place(x=640, y=380)
    def question2(self):
        def show():
            myLabel = Label(self, text=clicked.get()).place(x=0, y=0)
        def runMe():
            show()
            # function takes in an entry as input and calculates
            self.run(clicked, 2)
            self.question3()
        # setup background image
        self.backGroundImage = PhotoImage(file='Pet_IIB.png')
        self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y=0)
        # setup question image
        self.questionImage = PhotoImage(file='question_2.png')
        self.questionImageLabel = Label(self, image=self.questionImage, borderwidth=0)
        self.questionImageLabel.place(x=250,y=100)
        # setuo question options
        options = [
            'Not Active', 'Minimally Active',
            'Decently Active', 'Very Active'
            ]
        clicked = StringVar()
        clicked.set(options[0])
        self.drop = OptionMenu(self, clicked, *options)
        self.drop.config(width=20)
        self.drop.config(height=2)
        self.drop.place(x=325, y=250)
        # setup button to continue to previous question
        self.backButton = Button(self, text='<\BACK',
                                 height=1, width=8, bd=5, padx=20, pady=2, bg='teal',
                                 command=self.question1).place(x=50,y=380)
        # setup button to continue to next question
        self.nextButton = Button(self, text='NEXT/>',
                                 height=1,width=8, bd=5, padx=20, pady=2, bg='teal',
                                 command=runMe)
        self.nextButton.place(x=640, y=380)
    def question3(self):
        def show():
            #myLabel = Label(self, text=Checkbutton1.get()).place(x=0, y=0)
            return
        def runMe():
            show()
            # function takes in an entry as input and calculates
            self.run(Checkbutton1, 3)
            print(Quiz.answers)
            #self.question2()
        # setup background image
        self.backGroundImage = PhotoImage(file='Pet_IIB.png')
        self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y=0)
        # setup question image
        self.questionImage = PhotoImage(file='question_3.png')
        self.questionImageLabel = Label(self, image=self.questionImage, borderwidth=0)
        self.questionImageLabel.place(x=225,y=50)
        # setup question options
        Checkbutton1 = IntVar()
        Checkbutton2 = IntVar()
        Checkbutton3 = IntVar()
        Checkbutton4 = IntVar()
        Checkbutton5 = IntVar()
        Checkbutton6 = IntVar()
        Checkbutton7 = IntVar()
        Checkbutton8 = IntVar()
        self.button1 = Checkbutton(self, text='Child-Friendly', variable=Checkbutton1,
                                   onvalue=1, offvalue=0, height=2, width=10, padx=20).place(x=100, y=200)
        self.button2 = Checkbutton(self, text='Affectionate', variable=Checkbutton2,
                                   onvalue=1, offvalue=0, height=2, width=10, padx=20).place(x=100, y=300)
        self.button3 = Checkbutton(self, text='Energetic', variable=Checkbutton3,
                                   onvalue=1, offvalue=0, height=2, width=10, padx=20).place(x=250, y=200)
        self.button4 = Checkbutton(self, text='Intelligent', variable=Checkbutton4,
                                   onvalue=1, offvalue=0, height=2, width=10, padx=20).place(x=250, y=300)
        self.button5 = Checkbutton(self, text='Care-Free', variable=Checkbutton5,
                                   onvalue=1, offvalue=0, height=2, width=10, padx=20).place(x=400, y=200)
        self.button6 = Checkbutton(self, text='Cuddly', variable=Checkbutton6,
                                   onvalue=1, offvalue=0, height=2, width=10, padx=20).place(x=400, y=300)
        self.button7 = Checkbutton(self, text='Curious', variable=Checkbutton7,
                                   onvalue=1, offvalue=0, height=2, width=10, padx=20).place(x=550, y=200)
        self.button8 = Checkbutton(self, text='Independent', variable=Checkbutton8,
                                   onvalue=1, offvalue=0, height=2, width=10, padx=20).place(x=550, y=300)
        # setup button to continue to previous question
        self.backButton = Button(self, text='<\BACK',
                                 height=1, width=8, bd=5, padx=20, pady=2, bg='teal',
                                 command=self.question2).place(x=50,y=380)
        # setup button to continue to next question
        self.nextButton = Button(self, text='NEXT/>',
                                 height=1,width=8, bd=5, padx=20, pady=2, bg='teal',
                                 command=self.question4).place(x=640,y=380)
    def question4(self):
        def show():
            myLabel = Label(self, text=clicked.get()).place(x=0, y=0)
        def runMe():
            show()
            # function takes in an entry as input and calculates
            self.run(clicked, 4)
            self.question5()
        # setup background image
        self.backGroundImage = PhotoImage(file='Pet_IIB.png')
        self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y=0)
        # setup question image
        self.questionImage = PhotoImage(file='question_4.png')
        self.questionImageLabel = Label(self, image=self.questionImage, borderwidth=0)
        self.questionImageLabel.place(x=250,y=100)
        # setuo question options
        options = [
            'Low Maintenance', 'Average Maintenance','High Maintenance'
                  ]
        clicked = StringVar()
        clicked.set(options[0])
        self.drop = OptionMenu(self, clicked, *options)
        self.drop.config(width=20)
        self.drop.config(height=2)
        self.drop.place(x=325, y=250)
        # setup button to continue to previous question
        self.backButton = Button(self, text='<\BACK',
                                 height=1, width=8, bd=5, padx=20, pady=2, bg='teal',
                                 command=self.question3).place(x=50,y=380)
        # setup button to continue to next question
        self.nextButton = Button(self, text='NEXT/>',
                                 height=1,width=8, bd=5, padx=20, pady=2, bg='teal',
                                 command=runMe).place(x=640, y=380)
    def question5(self):
        def show():
            myLabel = Label(self, text=clicked.get()).place(x=0, y=0)
        def runMe():
            show()
            # function takes in an entry as input and calculates
            self.run(clicked, 5)
            self.question6()
        # setup background image
        self.backGroundImage = PhotoImage(file='Pet_IIB.png')
        self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y=0)
        # setup question image
        self.questionImage = PhotoImage(file='question_5.png')
        self.questionImageLabel = Label(self, image=self.questionImage, borderwidth=0)
        self.questionImageLabel.place(x=250,y=100)
        # setup question options
        options = [
            'Enough For Basic Needs', "Enough For Basic Necessities & Inexpensive Recurring Costs",
            'Enough For Spoiling & Necessities'
            ]
        clicked = StringVar()
        clicked.set(options[0])
        self.drop = OptionMenu(self, clicked, *options)
        self.drop.config(width=20)
        self.drop.config(height=2)
        self.drop.place(x=325, y=250)
        # setup button to continue to previous question
        self.backButton = Button(self, text='<\BACK',
                                 height=1, width=8, bd=5, padx=20, pady=2, bg='teal',
                                 command=self.question4).place(x=50,y=380)
        # setup button to continue to next question
        self.nextButton = Button(self, text='NEXT/>',
                                 height=1,width=8, bd=5, padx=20, pady=2, bg='teal',
                                 command=runMe).place(x=640, y=380)
    def question6(self):
        def choice(option):
            if option == 'yes':
                # continue to next window
                pass
            else:
                # exit pop up window
                # return to question
                pop.destroy()
                pass
                
        def clicker():
            # make pop very acessable
            global pop
            pop = Tk()
            #pop.geometry('250x150')
            pop.eval('tk::PlaceWindow . center')
            
            global img
            img = PhotoImage(file='pop_up.png')
            
            popLabel = Label(pop, text="Would You Like To Proceed?")
            popLabel.place(x=0, y=0)
            
            myFrame = Frame(pop, bg='green').place(x=0, y=0)
            
            pic = Label(pop, image=img, borderwidth=0).place(x=0, y=0)
            
            yes = Button(pop, text="YES", command=lambda: choice('yes'), bg='orange' )
            yes.place(x=0, y=0)
            no = Button(pop, text="No", command=lambda: choice('no'), bg='orange' )
            no.place(x=0, y=0)
        
        def show():
            myLabel = Label(self, text=clicked.get()).place(x=0, y=0)
        def runMe():
            show()
            # function takes in an entry as input and calculates
            self.run(clicked, 6)
            self.userResults()
        # setup background image
        self.backGroundImage = PhotoImage(file='Pet_IIB.png')
        self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y=0)
        # setup question image
        self.questionImage = PhotoImage(file='question_6.png')
        self.questionImageLabel = Label(self, image=self.questionImage, borderwidth=0)
        self.questionImageLabel.place(x=250,y=100)
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
        self.drop = OptionMenu(self, clicked, *options)
        self.drop.config(width=40)
        self.drop.config(height=2)
        self.drop.place(x=235, y=250)
        # setup button to continue to previous question
        self.backButton = Button(self, text='<\BACK',
                                 height=1, width=8, bd=5, padx=20, pady=2, bg='teal',
                                 command=self.question5).place(x=50,y=380)
        # setup button to continue to next question
        self.nextButton = Button(self, text='FINISH/>',
                                 height=1,width=8, bd=5, padx=20, pady=2, bg='teal',
                                 command=runMe).place(x=640, y=380)
    def userResults(self):
        
        # setup background image
        self.backGroundImage = PhotoImage(file='Pet_II.png')
        self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y=0)
        # setup canvas
        '''
        Display data for top picks of all animals. The leading score is the users 
        most compatible animal the last being the least compatible animal.
        '''
        # create neccessary data for bar graph 
        data = [int(petDict['Dog']/100), int(petDict['Cat']/100), int(petDict['Fish']/100),
                int(petDict['Reptile']/100), int(petDict['Bird']/100), int(petDict['Rodent']/100)]
        cWidth = 250 # canvas width
        cHeight = 200 # canvas height
        # create canvas
        c = Canvas(self, width=cWidth, height=cHeight, bg='grey').place(x=350, y=0)
        # size the bar graph
        # hieghest y value = maxDataValue * yStretch
        yStretch = 15
        # gap between lower canvas edge and x axis
        yGap = 20
        # stretch enough to get all data items in
        xStretch = 10
        xWidth = 20
        # gap between left canvas edge and y axis
        xGap = 20
        
        colors = ['', '', '', '', '', '']
        for x, y in enumerate(data):
            # calculate rectangle coordinates (intVals) for each bar
            x0 = x * xStretch + x * xWidth + xGap
            y0 = cHeight - (y * yStretch + yGap)
            x1 = x * xStretch + x * xWidth + xWidth + xGap
            y1 = cHeight - yGap
            # draw the bar
            c.create_rectangle(x0, y0, x1, y1, fill='red')
            # put the y value above each bar
            c.create_text(x0+2, y0, anchor=SW, text=str(y))
        
        var = StringVar()
        var.set("Your Best Matched Pet is A {maxsVal}")
        self.topPick = Label(self, textvariable=var, relief=RAISED).place(x=350, y=200)
        # setup button to continue to previous question
        self.backButton = Button(self, text='<\BACK',
                                 height=1, width=8, bd=5, padx=20, pady=2, bg='teal',
                                 command=self.question6).place(x=50,y=380)
    # METHOD: run()
    # takes a question as a parameter and retrieves the entry
    # further adds the entry to class dictionary 'answers'
    def run(self, widget, num):
        ''' Funtion to compute user results; whats the most logical way to compute
        and display these results '''
        def computation():
            # compute user answers
            '''Xcompute answers for question 1'''
            if Quiz.answers[1] == 'Less Than 5 Hours':
                d._counter += 1 # add to dog counter
                c._counter += 1 # add to cat counter
                r._counter += 1 # add to reptile counter
                b._counter += 1 # add to bird counter
                f._counter += 1 # add to fish counter
                rd._counter += 1 # add to rodent counter
            elif Quiz.answers[1] == '5-8 Hours':
                c._counter += 1 # add to cat counter
                r._counter += 1 # add to reptile counter
                b._counter += 1 # add to bird counter
                f._counter += 1 # add to fish counter
                rd._counter += 1 # add to rodent counter
            elif Quiz.answers[1] == '8-10 Hours':
                r._counter += 1 # add to reptile counter
                b._counter += 1 # add to bird counter
                f._counter += 1 # add to fish counter
                rd._counter += 1 # add to rodent counter
            elif Quiz.answers[1] == '10-15 Hours':
                f._counter += 1 # add to fish counter
                r._counter += 1 # add to reptile counter
                b._counter += 1 # add to bird counter
            '''Xcompute answers for question 2'''
            if Quiz.answers[2] == 'Not Active':
                f._counter += 1 # add to fish counter
                r._counter += 1 # add to reptile counter
            elif Quiz.answers[2] == 'Minimally Active':
                b._counter += 1 # add to bird counter
                rd._counter += 1 # add to rodent counter
            elif Quiz.answers[2] == 'Decently Active':
                c._counter += 1 # add to cat counter
            elif Quiz.answers[2] == 'Very Active':
                d._counter += 1 # add to dog counter
            '''Xcompute answers for question 3'''
            if Quiz.answers[3] == '':
                pass
            elif Quiz.answers[3] == '':
                pass
            elif Quiz.answers[3] == '':
                pass
            elif Quiz.answers[3] == '':
                pass
            '''compute answers for question 4'''
            if Quiz.answers[4] == 'Low Maintenance':
                f._counter += 1 # add to fish counter
                r._counter += 1 # add to reptile counter
                rd._counter += 1 # add to rodent counter
            elif Quiz.answers[4] == 'Average Maintenance':
                b._counter += 1 # add to bird counter
            elif Quiz.answers[4] == 'High Maintence':
                d._counter += 1 # add to dog counter
                c._counter += 1 # add to cat counter
            '''Xcompute answers for question 5'''
            if Quiz.answers[5] == 'Enough For Basic Needs':
                f._counter += 1 # add to fish counter
                rd._counter += 1 # add to rodent counter
            elif Quiz.answers[5] == 'Enough For Basic Necessities And Inexpensive Recurring Costs':
                r._counter += 1 # add to reptile counter
                b._counter += 1 # add to bird counter
            elif Quiz.answers[5] == 'Enough For Spoiling & Necessities':
                d._counter += 1 # add to dog counter
                c._counter += 1 # add to cat counter
            '''Xcompute answers for question 6'''
            if Quiz.answers[1] == 'Small - Not Alot Of Space To Roam; No Yard':
                f._counter += 1 # add to fish counter
                r._counter += 1 # add to reptile counter
                rd._counter += 1 # add to rodent counter
            elif Quiz.answers[2] == 'Small - With Yard':
                d._counter += 1 # add to dog counter
                c._counter += 1 # add to cat counter
                b._counter += 1 # add to bird counter
                f._counter += 1 # add to fish counter
                r._counter += 1 # add to reptile counter
                rd._counter += 1 # add to rodent counter
            elif Quiz.answers[3] == 'Average - Some Space To Roam; No Yard':
                d._counter += 1 # add to dog counter
                c._counter += 1 # add to cat counter
                f._counter += 1 # add to fish counter
                r._counter += 1 # add to reptile counter
                rd._counter += 1 # add to rodent counter
            elif Quiz.answers[4] == 'Average - With Yard':
                d._counter += 1 # add to dog counter
                c._counter += 1 # add to cat counter
                b._counter += 1 # ad to bird counter
                f._counter += 1 # add to fish counter
                r._counter += 1 # add to reptile counter
                rd._counter += 1 # add to rodent counter
            elif Quiz.answers[4] == 'Big - Lots Of Space To Roam; No Yard':
                d._counter += 1 # add to dog counter
            elif Quiz.answers[4] == 'Big - With Yard':
                d._counter += 1 # add to dog counter
                c._counter += 1 # add to cat counter
                b._counter += 1 # ad to bird counter
                f._counter += 1 # add to fish counter
                r._counter += 1 # add to reptile counter
                rd._counter += 1 # add to rodent counter
                
            # assign new pet counters to a variable (int)
            # then append to a petList
            myDog = d._counter
            petDict['Dog'] = myDog
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
            print(petDict) # print dictionary
            # retrieve the max dictionary value from petList
            global maxVal
            maxVal = max(petDict, key=petDict.get)
            print(f'Your best matched pet is {maxVal}') # print max val of dictionary
        
        ## MAIN CODE ##
        # create dictionary to track pet values
        global petDict
        petDict = {'Dog': 0, 'Cat': 0, 'Fish': 0, 'Reptile': 0,
                   'Bird': 0, 'Rodents': 0}
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
            Quiz.answers[1] = answer
        elif num == 2:
            Quiz.answers[2] = answer
        elif num == 3:
            Quiz.answers[3] = answer
        elif num == 4:
            Quiz.answers[4] = answer
        elif num == 5:
            Quiz.answers[5] = answer
        elif num == 6:
            Quiz.answers[6] = answer
            computation()
                    
### MAIN PROGRAM ###
Q = Quiz()
Q.setupGUI()
Q.mainloop()