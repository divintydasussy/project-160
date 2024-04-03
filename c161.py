#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 18:56:09 2024

@author: sid
"""

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.minsize(650,650)
root.maxsize(650,650)

open_img = ImageTk.PhotoImage(Image.open ("open_file.png"))
save_img = ImageTk.PhotoImage(Image.open ("save_file.png"))
exit_img = ImageTk.PhotoImage(Image.open ("run.png"))

label_file_name = Label(root, text="File name")
label_file_name.place(relx=0.28,rely=0.03, anchor= CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.46,rely=0.03, anchor= CENTER)

my_text= Text(root,height=35,width=80)
my_text.place(relx=0.5,rely=0.55,anchor= CENTER)



name = ""
def openFile():
    global name
    my_text.delete(1.0,END)
    imput_file_name.delete(0, END)
    text_file = filedialog.askopenfilename(title=" Open text file", filetypes=(("text Files", "*.txt"),))
    print(text_file)
    name = os.path.basename(text_file)
    formated_name = name.split('.')[0]
    imput_file_name.inset(END,formated_name)
    root.title(formated_name)
    text_file = open(name,'r')
    paragraph=text_file.read()
    my_text.insert(end,paragraph)
    text_file.close()
    
def save():
    imput_name = imput_file_name.get()
    file = open(imput_name+".txt", "w")
    data = my_text.get("1.0",END)
    print(data)
    file.write(data)
    imput_file_name.delete(1.0,END)
    message.boxshowinfo("update", "success")
    
def closeWindow():
    root.destroy()

open_button=Button(root,image=open_img,text="openFile",command=openFile)
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)

save_button=Button(root,image=save_img,text="Save File",command=save)
save_button.place(relx=0.11,rely=0.03,ancor=CENTER)

exit_button=Button(root,image=exit_img,text="Exit File",command=closeWindow)
exit_button.place(relx=0.17,rely=0.03,ancor=CENTER)

root.mainloop

