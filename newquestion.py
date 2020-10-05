from tkinter import *
from tkinter import scrolledtext as st
import time


class QuestFrame(Frame):
    def __init__(self, parent, quest, answers, pers, curr, clck):
        Frame.__init__(self, parent)
        self.parent = parent
        self.myquestion = quest
        self.answer = answers
        self.person = pers
        self.num = curr
        self.clock = clck
        self.initUI()
        self.end = False
        self.update_clock()

    def update_clock(self):
        self.now = time.strftime('%M:%S', time.gmtime(self.clock))
        if (self.now == '00:00'):
            self.Top.pack_forget()
            self.Bot.pack_forget()
            self.endF.pack(expand=1)
            Label(self.endF, text='----------------', font='arial 16').pack()
            Label(self.endF, text='Тест завершен', font='arial 16').pack()
            Label(self.endF, text='----------------', font='arial 16').pack()
            self.endB.pack(pady=20)
        else:
            self.clock -= 1
            self.time.configure(text=self.now)
            self.parent.after(1000, self.update_clock)

    def initUI(self):
        self.parent.title("Test")

        self.Top = Frame(self)
        self.Bot = Frame(self, bg='grey', height=10)
        self.endF = Frame(self)
        question = st.ScrolledText(self.Top, width=42, height=4, font='arial 13', wrap=WORD)
        question.insert(INSERT, self.myquestion)
        question.configure(state='disabled')

        self.ansbtn1 = Button(self.Top, text=self.answer[0], bg='grey', fg='black', font='arial 10')
        self.ansbtn2 = Button(self.Top, text=self.answer[1], bg='grey', fg='black', font='arial 10')
        self.ansbtn3 = Button(self.Top, text=self.answer[2], bg='grey', fg='black', font='arial 10')
        self.ansbtn4 = Button(self.Top, text=self.answer[3], bg='grey', fg='black', font='arial 10')
        self.backbtn = Button(self.Top, text='Назад', bg='grey', fg='black', font='arial 10')
        self.endB = Button(self.endF, bg='grey', text='OK', width=6, height=1, font='arial 16')

        Label(self.Bot, bg='grey', text=self.person, font='arial 10').pack(side=LEFT, anchor=SW)
        self.time = Label(self.Bot, bg='grey', text='10:00', font='arial 10')
        Label(self.Bot, bg='grey', text='Вопрос №' + str(self.num + 1), font='arial 10').pack(side=RIGHT, padx=10)

        self.Top.pack(side=TOP)
        question.grid(row=0, column=0, columnspan=10)
        self.ansbtn1.grid(row=1, column=0, pady=5)
        self.ansbtn2.grid(row=2, column=0, pady=5)
        self.ansbtn3.grid(row=3, column=0, pady=5)
        self.ansbtn4.grid(row=4, column=0, pady=5)
        self.backbtn.grid(row=7, column=9, pady=5)

        self.Bot.pack(side=BOTTOM, fill=X)
        self.time.pack(side=RIGHT, anchor=SE, padx=10)
        self.pack(expand=True, fill='both')


class EndFrame(Frame):
    def __init__(self, parent, person, Tanswers, Uanswers):
        Frame.__init__(self, parent)
        self.parent = parent
        self.name = person
        self.myanswers = Uanswers
        self.fine_answers = Tanswers
        self.initUI()

    def initUI(self):
        self.parent.title(self.name )
        i = 0
        count = 0

        Top = Frame(self)
        Left = Frame(Top)
        Right = Frame(Top)
        Bot = Frame(self, bg='grey', height=60)

        Label(Left, text='Ваши ответы:', font='arial 14').grid(row=0, column=0, rowspan=3, columnspan=10)
        Label(Right, text='Правильные ответы:', font='arial 14').grid(row=0, column=12, rowspan=3)
        while(i<10):
            if (self.myanswers[i] == self.fine_answers[i]):
                color = 'green'
                count += 1
            else:
                color = 'red'
            Label(Left, text=self.myanswers[i], fg=color, font='arial 10').grid(row=i+3, column=0, columnspan=5)
            Label(Right, text=self.fine_answers[i], fg='black', font='arial 10').grid(row=i+3, column=12, columnspan=5)
            i+=1

        Label(Bot, text='Ваша оценка: ' + str(count), bg='grey', font='arial 16').pack(side=TOP, pady=5)
        self.endbtn = Button(Bot, text='Завершить тест', bg='grey', fg='black', font='arial 14')
        self.endbtn.pack(side=BOTTOM, pady=5)
        Top.pack(side=TOP)
        Left.pack(side=LEFT, padx=5)
        Right.pack(side=RIGHT, padx=5)
        Bot.pack(side=BOTTOM, fill=X)
        self.pack(expand=True, fill='both')