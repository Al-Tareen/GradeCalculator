from tkinter import *

window = Tk()

#Window Settings
window.title("Calculate Average/Letter Grade")
window.geometry('400x300')

#Labels
instruction = Label(window, text="Enter the scores for the following assignments and exams: ")
instruction.grid(column=0, row=0, columnspan=2)

discussion = Label(window, text="Discussions (5% of Total): ")
discussion.grid(column=0, row=1)

quiz = Label(window, text="Quizzes (15% of Total): ")
quiz.grid(column=0, row=2)

project = Label(window, text="Programs/Project (15% of Total): ")
project.grid(column=0, row=3)

myLabs = Label(window, text="MyLabs (15% of Total): ")
myLabs.grid(column=0, row=4)

exam1 = Label(window, text="Exam1 (10% of Total): ")
exam1.grid(column=0, row=5)

exam2 = Label(window, text="Exam2 (10% of Total): ")
exam2.grid(column=0, row=6)

finalExam = Label(window, text="Final Exam (30% of Total): ")
finalExam.grid(column=0, row=7)

#Textbox's / Entrybox's
totalDiscussion = Entry(window, width=10)
totalDiscussion.grid(column=1, row=1)

totalQuiz = Entry(window, width=10)
totalQuiz.grid(column=1, row=2)

totalProject = Entry(window, width=10)
totalProject.grid(column=1, row=3)

totalMyLab = Entry(window, width=10)
totalMyLab.grid(column=1, row=4)

totalExam1 = Entry(window, width=10)
totalExam1.grid(column=1, row=5)

totalExam2 = Entry(window, width=10)
totalExam2.grid(column=1, row=6)

totalFinalExam = Entry(window, width=10)
totalFinalExam.grid(column=1, row=7)

#Output Labels
average = Label(window, text="Average: ")
average.grid(column=0, row=10, sticky=E)

letter =  Label(window, text="Letter Grade: ")
letter.grid(column=0, row=11, sticky=E)

#Linebreak between entry box's / buttons
linebreak=Label(window, text=" ")
linebreak.grid(column=1, row=8)

#Output Labels
averageCalculate=Label(window, text=" ")
averageCalculate.grid(column=1, row=10)

letterCalculate=Label(window, text=" ")
letterCalculate.grid(column=1, row=11)

#Function to calculate Average of all inputs and display Letter Grade
def calculateAverage():

    averageCalculate.configure(text= ( ( ( int(totalDiscussion.get())/ 100 ) * 5 ) + \
                                       ( ( int(totalQuiz.get())/ 100 ) * 15 )  + \
                                       ( ( int(totalProject.get())/ 100 ) * 15 ) + \
                                       ( ( int(totalMyLab.get())/ 100 ) * 15 )  + \
                                       ( ( int(totalExam1.get())/ 100 ) * 10 )  + \
                                       ( ( int(totalExam2.get())/ 100 ) * 10 )  + \
                                       ( ( int(totalFinalExam.get())/ 100 ) * 30 ) ) )

    if averageCalculate["text"] >= 89.45:
        letterCalculate.configure(text="A")
        
    elif averageCalculate["text"] < 89.45 and averageCalculate["text"] > 79.45 :
        letterCalculate.configure(text="B")

    elif averageCalculate["text"] < 79.45 and averageCalculate["text"] > 69.45:
        letterCalculate.configure(text="C")

    elif averageCalculate["text"] < 69.45 and averageCalculate["text"] > 59.45:
        letterCalculate.configure(text="D")

    elif averageCalculate["text"] < 59.45:
        letterCalculate.configure(text="F")

#Buttons                                                                                                     
btn = Button(window, text="Calculate Average/Letter Grade ", command=calculateAverage)
btn.grid(column=0, row=9, columnspan=2)

btn = Button(window, text="Quit", command=quit)
btn.grid(column=1, row=9)

window.mainloop()
