from tkinter import *
from tkinter import ttk
import pymysql
from PIL import ImageTk
from tkinter import messagebox

petasco = Tk()
petasco.title('AAMUSTED')
petasco.geometry('1370x700+0+0')

img = ImageTk.PhotoImage(file='Pictures/campus.jpg')
img = Label(petasco, image=img)
img.place(x=0, y=0, width=500, height=260)
headerFrame = Frame(petasco,bd=8,relief=GROOVE,bg='#9F000F')
headerFrame.pack(side=TOP, fill=X)
title = Label(headerFrame, text='AAMUSTED Management System',font=('Algerian',35, 'bold'), bg='#9F000F', fg='white')
title.pack(side=TOP, fill=X)
name = Label(headerFrame, text='Akenten Appiah-Menka University of Skills Training & Entrepreneurial Development',font=('consolas',15, 'bold'), bg='#9F000F', fg='black')
name.pack(side=TOP, fill=X,pady=0)


loginFrame = Frame(petasco, bd=0, bg='#B21807')
loginFrame.place(x=450,y=150, width=400, height=500)

headerlbl = Label(loginFrame, text='AAMUSTED MANAGER LOGIN', font=('consolas',15,'bold'), bg='#B21807')
headerlbl.place(x=80, y=100)

usernamelbl = Label(loginFrame, text='Username',bg='#B21807', font=('constantia',15,'bold'), fg='GOLD')
usernamelbl.place(x=100, y=180)
usernameEntry = Entry(loginFrame, bd=0,font=('times new roman',15,'bold'), fg='black', width=20)
usernameEntry.place(x=100, y=215)

passwordlbl = Label(loginFrame, text='Password',bg='#B21807', font=('constantia',15,'bold'), fg='GOLD')
passwordlbl.place(x=100, y=250)
passwordEntry = Entry(loginFrame, bd=0,font=('times new roman',15,'bold'), fg='black', width=20)
passwordEntry.place(x=100, y=285)


# loginpic = ImageTk.PhotoImage(file='Pictures/loginpic.jpg')
loginBtn = Button(loginFrame, text='Login', font=('lato',15,'bold'), width=10, activebackground='green')
loginBtn.place(x=150, y=330, height=32)


icon = ImageTk.PhotoImage(file='Pictures/aamusted-logo.jpg')
petasco.iconphoto(False,icon)
petasco.resizable(False,False)
petasco.mainloop()
