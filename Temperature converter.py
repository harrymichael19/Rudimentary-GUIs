# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 20:24:46 2021

@author: harry
"""

from tkinter import * 

def calculate():
    temp = int(entry.get())
    temp = 9/5*temp+32 #conversion from celsius to fahrenheit
    output_label.configure(text = "converted: {:.1f}".format(temp))
    entry.delete(0,END) #remove value after entry
    
root = Tk()
message_label = Label(text = "Enter a temperature", font = ("Verdana", 16))
output_label = Label(font = ("Verdana", 16))
entry = Entry(font = ("Verdana", 16), width = 4)
calc_button = Button(text = "Ok", font = ("Verdana" , 16), command = calculate)

message_label.grid(row = 0, column = 0)
entry.grid(row = 0, column = 1)
calc_button.grid(row = 0, column = 2)
output_label.grid(row = 1, column = 0, columnspan = 3)

mainloop()
