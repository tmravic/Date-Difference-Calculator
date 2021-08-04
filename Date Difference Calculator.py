#!/usr/bin/env python
# coding: utf-8

from datetime import datetime as dt
from tkinter import Frame, Text, Button, Tk, END


class Application(Frame):
    def __init__(self, master):
        '''Initial setup handled here'''
        super().__init__(master)
        self.grid()
        self.create_features()
        self.dates = {'date1' : '',
                      'date2' : ''}
        self.date1 = False 
        self.date2 = False 


    def create_features(self):
        '''Method that creates and places all the features'''
        content = ['Del', 0, 'C', 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for row in range(2,6):
            for col in range(3):
                b = content.pop()
                lbl = Button(self, text=b, bg='black', fg='white',command = lambda inp=b : self.input_feed(inp))
                lbl.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)

        self.textentry = Text(self, width = 26, height=3, bg='blue', fg='white')
        self.textentry.grid(row = 1, column = 0, columnspan=3, sticky = 'w', padx=5, pady=5)

        self.start_button = Button(self, text = 'Find Date Difference', bg='black', fg='white',command = self.date_difference)
        self.start_button.grid(row = 6, column = 0, columnspan = 3)


    def date_difference(self):
        '''Method that subtracts the start date from the end date'''
        if self.date1 and self.date2:
            try:
                start_date = dt.strptime(self.dates['date1'], '%Y-%m-%d')
                end_date = dt.strptime(self.dates['date2'], '%Y-%m-%d')
                output = str((abs(end_date - start_date)).days) + ' days'
            except ValueError:
                output = 'Date format invalid!'
        else:
                output = 'Date Not complete yet!'

        self.textentry.delete(0.0, END)
        self.textentry.insert(0.0, output)
    

    def number_entry(self, arg):
        '''Handles all number key presses. Called by input_feed'''
        if self.date1 == False:
            self.dates['date1'] += arg

            if len(self.dates['date1']) in [4,7]:
                self.dates['date1'] += '-'

            if len(self.dates['date1']) == 10:
                self.date1 = True

            self.textentry.delete(0.0, END)
            self.textentry.insert(0.0, 'Date 1: ' + self.dates['date1'])
            return

        elif self.date2 == False:
            self.dates['date2'] += arg

            if len(self.dates['date2']) in [4, 7]:
                self.dates['date2'] += "-"

            if len(self.dates['date2']) == 10:
                self.date2 = True

            self.textentry.delete(0.0, END)
            self.textentry.insert(0.0, 'Date 1: ' + self.dates['date1'])
            self.textentry.insert(END, '\nDate 2: ' + self.dates['date2'])
            return
        else:
            self.date_difference()

      
    def delete_or_c(self, arg):
        '''Handles any Del or C Key Presses'''
        if arg == 'C':
            self.dates['date1'] = ''
            self.dates['date2'] = ''
            self.date1, self.date2, = False, False

        if self.date1 == False:
            self.dates['date1'] = self.dates['date1'][:-1]
            if len(self.dates['date1']) == 0:
                self.date1 = False

        elif self.date2 == False:
            self.dates['date2'] = self.dates['date2'][:-1]
            if len(self.dates['date2']) == 0:
                self.date2 = False

    
    def input_feed(self, arg):
        '''Receives all inputs from buttons and delegates'''
        if len(self.dates['date1']) == 10:
            self.date1 = True

        if len(self.dates['date2']) == 10:
            self.date2 = True    

        if arg in ['Del', 'C']:
            self.delete_or_c(arg)
        elif arg in list(range(10)):
            self.number_entry(str(arg))
        

root = Tk()
root.title("Date Difference")
root.geometry("240x300")
root = Application(root)
root.mainloop()






