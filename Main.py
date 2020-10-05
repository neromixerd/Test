from tkinter import *
import codecs
import random
import newquestion


def Check_Question(question):
    used = False
    if UsedQuestions == '':
        return used
    for i in range(len(UsedQuestions)):
        if question == UsedQuestions[i]:
            used = True
    return used


def Exit(event):
    app.destroy()
    root.destroy()


def End_test(event):
    global app
    curr = event.widget.cget('text')
    if curr != 'OK':
        UserAnswers[current - 1] = curr
    app.pack_forget()
    app = newquestion.EndFrame(test, person, CurrentAnswers, UserAnswers)
    app.endbtn.bind('<Button-1>', Exit)


def Start_test(event):
    global person
    global app
    global clock
    global current
    global UserAnswers
    root.withdraw()
    answers = []
    test.deiconify()

    if app != newquestion:
        sol = app.now.split(':')
        clock = 60*int(sol[0]) + int(sol[1])

    if(current != 0):
        UserAnswers[current - 1] = event.widget.cget('text')
        if (UserAnswers[current - 1] == 'Назад'):
            current -= 2
        app.pack_forget()
    else:
        name = Enter_name.get()
        group = Enter_group.get()
        person = name + ' ' + group

    for i in range(len(Answerlist[Index[current]])):
        answers += [Answerlist[Index[current]][i]]

    random.shuffle(answers)

    app = newquestion.QuestFrame(test, TestQuestions[current], answers, person, current, clock)
    if (current != 9):
        app.ansbtn1.bind('<Button-1>', Start_test)
        app.ansbtn2.bind('<Button-1>', Start_test)
        app.ansbtn3.bind('<Button-1>', Start_test)
        app.ansbtn4.bind('<Button-1>', Start_test)
    else:
        app.ansbtn1.bind('<Button-1>', End_test)
        app.ansbtn2.bind('<Button-1>', End_test)
        app.ansbtn3.bind('<Button-1>', End_test)
        app.ansbtn4.bind('<Button-1>', End_test)

    if (current == 0):
        app.backbtn['state'] = 'disabled'
    else:
        app.backbtn.bind('<Button-1>', Start_test)

    app.endB.bind('<Button-1>', End_test)
    current += 1


Start = False
fail = True
checkcount = 0
current = 0
clock = 600
person = ''
QuestionList = []
TestQuestions = []
Answerlist = []
CurrentAnswers = []
UsedQuestions = []
Index = []
app = newquestion
UserAnswers = ['', '', '', '', '', '', '', '', '', '', '']
file = codecs.open('Questions.txt', 'r', encoding='utf-8')
List = [line.strip() for line in file]

for i in range(len(List)):
    sol = List[i].split('|')
    QuestionList += [sol[0]]
    Answerlist += [[sol[1], sol[2], sol[3], sol[4]]]
file.close()

root = Tk()
root.title("Test")
root.geometry("300x150+500+300")
root.resizable(width=False, height=False)
root["bg"] = "grey"

test = Toplevel()
test.geometry("400x350+500+300")
test.resizable(width=False, height=False)
test.withdraw()

F_Name = Frame(bg='grey')
Label(F_Name, bg='grey', text='Введите имя:', font='arial 10').pack(side=TOP, pady=10)
Label(F_Name, bg='grey', text='Введите группу:', font='arial 10').pack(side=BOTTOM)

F_Enter = Frame(bg='grey')
Enter_name = Entry(F_Enter, fg='black', width=30)
Enter_name.pack(side=TOP, pady=10, padx=10)
Enter_group = Entry(F_Enter, fg='black', width=30)
Enter_group.pack(side=BOTTOM, padx=10)

F_But = Frame(bg='grey')
buttonStart = Button(F_But, text='Начать тест', bg='black', fg='white', font='arial 12')
buttonStart.pack(pady=20)

F_But.pack(side=BOTTOM)
F_Name.pack(side=LEFT)
F_Enter.pack(side=RIGHT)

while (checkcount != 10):
    index, newQuestion = random.choice(tuple(enumerate(QuestionList)))
    fail = Check_Question(newQuestion)
    if fail == False:
        checkcount += 1
        UsedQuestions += [newQuestion]
        TestQuestions += [newQuestion]
        Index += [index]

for i in range(len(UserAnswers)-1):
    CurrentAnswers += [Answerlist[Index[i]][3]]

buttonStart.bind('<Button-1>', Start_test)
root.mainloop()