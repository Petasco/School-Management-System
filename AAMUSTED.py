from tkinter import *
from tkinter import ttk
import pymysql
from PIL import ImageTk
from tkinter import messagebox
# from email_validator import validate_email, EmailNotValidError

petasco = Tk()
petasco.title('AAMUSTED')
petasco.geometry('1370x700+0+0')
petasco.config(bg='#9F000F')
headerFrame = Frame(petasco,bd=8,relief=GROOVE,bg='#9F000F')
headerFrame.pack(side=TOP, fill=X)
title = Label(headerFrame, text='AAMUSTED Management System',font=('Algerian',35, 'bold'), bg='#9F000F', fg='white')
title.pack(side=TOP, fill=X)
name = Label(headerFrame, text='Akenten Appiah-Menka University of Skills Training & Entrepreneurial Development',font=('consolas',15, 'bold'), bg='#9F000F', fg='black')
name.pack(side=TOP, fill=X,pady=0)


# =================================== manage frame ==============================================
manage_frame = Frame(petasco, bd=4, relief=RIDGE, bg='Green')
manage_frame.place(x=10, y=100, width=450, height=590)


# =============================================== Variable declaration ==========================
facultyvar = StringVar()
deptvar = StringVar()
hallvar = StringVar()
levelvar = StringVar()
classvar = StringVar()
indexvar = StringVar()
namevar = StringVar()
emailvar = StringVar()
gendervar = StringVar()
contactvar = StringVar()
dobvar = StringVar()
stypevar = StringVar()

sortvar = StringVar()
searchvar = StringVar()

# ============================================ functions ==================================

def add():
    validate = emailvar.get()
    if facultyvar.get()=='' or deptvar.get()=='' or hallvar.get()=='' or levelvar.get()=='' or classvar.get()=='' or indexvar.get()=='' or namevar.get()=='' or emailvar.get()=='' or gendervar.get()=='' or contactvar.get()=='' or dobvar.get()=='' or stypevar.get()=='':
        messagebox.showerror('Error', 'All fields required!!!')
    elif validate[-10:] != '@gmail.com':
        messagebox.showerror('Email Error', 'Please enter a valid email address !!!')
    elif len(contactvar.get()) != 10:
        messagebox.showerror('Email Error', 'Please enter a valid phone number !!!')
    elif len(indexvar.get()) < 10:
        messagebox.showerror('Email Error', 'Please enter a valid index number !!!')
    else:

        try:
            con = pymysql.connect(host='localhost', user='root',password='Rock1844',database='aamusted')
            cur = con.cursor()
            cur.execute('insert into Students values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(facultyvar.get(), deptvar.get(),
                                                                                            hallvar.get(), levelvar.get(),
                                                                                            classvar.get(),indexvar.get(),
                                                                                            namevar.get(),emailvar.get(),
                                                                                            gendervar.get(), contactvar.get(),
                                                                                            dobvar.get(),stypevar.get()))
            con.commit()
            fatch_data()
            #clear()
            con.close()
            messagebox.showinfo('Success', 'Student Added Successfully !!!')

        except Exception as es:
            messagebox.showerror('Error!', f'Error due to {str(es)} \nPlease check your entries and try again!')

def fatch_data():
    con = pymysql.connect(host='localhost', user='root', password='Rock1844', database='aamusted')
    cur = con.cursor()
    cur.execute('select * from students')
    rows = cur.fetchall()
    if len(rows) != 0:
        student_Table.delete (*student_Table.get_children())
        for row in rows:
            student_Table.insert('', END,values=row)
        con.commit()
    con.close()


def get_cursor(ev):
    cursor_row = student_Table.focus()
    contents = student_Table.item(cursor_row)
    row = contents['values']
    facultyvar.set(row[0])
    deptvar.set(row[1])
    hallvar.set(row[2])
    levelvar.set(row[3])
    classvar.set(row[4])
    indexvar.set(row[5])
    namevar.set(row[6])
    emailvar.set(row[7])
    gendervar.set(row[8])
    contactvar.set(row[9])
    dobvar.set(row[10])
    stypevar.set(row[11])


def update():
    if facultyvar.get()=='' or deptvar.get()=='' or hallvar.get()=='' or levelvar.get()=='' or classvar.get()=='' or indexvar.get()=='' or namevar.get()=='' or emailvar.get()=='' or gendervar.get()=='' or contactvar.get()=='' or dobvar.get()=='' or stypevar.get()=='':
        messagebox.showerror('Error', 'All fields required!!!')

    try:
        con = pymysql.connect(host='localhost', user='root',password='Rock1844',database='aamusted')
        cur = con.cursor()
        cur.execute('update Students set Faculty=%s,Department=%s,Hall=%s,Level=%s,Class=%s,Name=%s,Email=%s,Gender=%s,Contact=%s,dob=%s,stype=%s where indexno=%s',(facultyvar.get(), deptvar.get(),
                                                                                        hallvar.get(), levelvar.get(),
                                                                                        classvar.get(),
                                                                                        namevar.get(),emailvar.get(),
                                                                                        gendervar.get(), contactvar.get(),
                                                                                        dobvar.get(),stypevar.get(),indexvar.get()))
        con.commit()
        fatch_data()
        #clear()
        con.close()
        messagebox.showinfo('Success', 'Data Updated Successfully !!!')

    except Exception as es:
        messagebox.showerror('Error!', f'Error due to {str(es)} \nPlease check your entries and try again!')


def delete():
    if indexvar.get()=='':
        messagebox.showinfo('Error','Enter student index number to be deleted!!!')
    try:
        con = pymysql.connect(host='localhost', user='root',password='Rock1844',database='aamusted')
        cur = con.cursor()
        cur.execute('delete from students where indexno=%s', indexvar.get())
        con.commit()
        con.close()
        fatch_data()
        #clear()
        messagebox.showinfo('Delete', 'Record deleted successfully !!!')

    except Exception as es:
        messagebox.showerror('Error!', f'Error due to {str(es)} \nPlease check your entries and try again!')

def clear():
    facultyvar.set('')
    deptvar.set('')
    hallvar.set('')
    levelvar.set('')
    classvar.set('')
    indexvar.set('')
    namevar.set('')
    emailvar.set('')
    gendervar.set('')
    contactvar.set('')
    dobvar.set('')
    stypevar.set('')
    messagebox.showinfo('Success', 'Cleared Successfully !!!')


'''def sort():
    if sortvar.get() == '':
        messagebox.showinfo('Error', 'Select sort by keyword!!!')
    try:
        con = pymysql.connect(host='localhost', user='root', password='Rock1844', database='aamusted')
        cur = con.cursor()
        cur.execute('select * from students where ',sortvar.get() + "%")
        #cur.execute('select * from students where ' + str(sortvar.get()) + " Like '%")
        rows = cur.fetchall()
        con.commit()
        con.close()
        if len(rows) != 0:
            student_Table.delete(*student_Table.get_children())
            for row in rows:
                student_Table.insert('', END, values=row)
            con.commit()
        con.close()
        messagebox.showinfo('Delete', 'Records sorted successfully !!!')

    except Exception as es:
        messagebox.showerror('Error!', f'Error due to {str(es)} \nPlease check your entries and try again!')'''


def search():
    print(searchvar.get())
    print(sortvar.get())
    try:
        con = pymysql.connect(host='localhost', user='root',password='Rock1844',database='aamusted')
        cur = con.cursor()
        cur.execute('select * from students where '+str(sortvar.get()) +" Like '%"+str(searchvar.get())+"%'")

        rows = cur.fetchall()
        if len(rows)!= 0:
            student_Table.delete(*student_Table.get_children())
            for row in rows:
                student_Table.insert('', END, values=row)
            con.commit()
        con.close()
    #messagebox.showinfo('Delete', 'Record deleted successfully !!!')

    except Exception as es:
        messagebox.showerror('Error!', f'Error due to {str(es)} \nPlease check your entries and try again!')


# ============================ frame title =======================================================
man_frameTitle = Label(manage_frame, text='Manage Students', font=('cambria',25,'bold'), bd=5, bg='#9F000F', fg='white', relief=GROOVE)
man_frameTitle.place(x=10, y=10,width=420)

category = {'Faculty of Applied Sciences & Mathematics': ['Information Technology Education','Mathematics Education'],
            'Faculty of Technical Education': ['Automotive & Mechnical Technology Education', 'Construction & Wood Technology Education',
            'Electrical & Electronic Technology EducaTION'],'Faculty of Business Education': ['Accounting Studies',
                                                                                              'Management Studies'],
            'Faculty of Vocational Education': ['Catering & Hospitality Education', 'Fashion & Textiles Design Education'],
            'Faculty of Education & Communication Sciences': ['Interdisciplinary Studies', 'Languages Education']}


def getUpdateData(event):
    value = facultyvar.get()
    deptvar.set(category[value][0])
    CategoryCombo.config(values=category[value])


faculty = Label(manage_frame, text='Faculty',font=('times new roman',20, 'bold'), bg='green', fg='black')
faculty.place(x=10, y=60)

faculty_values = list(category.keys())
facultyvar.set(faculty_values[0])
AccountCombo= ttk.Combobox(manage_frame,width=21,textvariable=facultyvar,font=('times new roman',16, 'bold'),values=list(category.keys()))
AccountCombo.bind('<<ComboboxSelected>>',getUpdateData)
AccountCombo.place(x=170, y=60)

dept = Label(manage_frame, text='Department',font=('times new roman',20, 'bold'), bg='green', fg='black')
dept.place(x=10, y=100)

deptvar.set(category[faculty_values[0]][0])
CategoryCombo =ttk.Combobox(manage_frame,width=21, textvariable=deptvar,font=('times new roman',16, 'bold'),values=category[faculty_values[0]])
CategoryCombo.bind('<<ComboboxSelected>>',getUpdateData)
CategoryCombo.place(x=170, y=100)

hall = Label(manage_frame, text='Hall',font=('times new roman',20, 'bold'), bg='green', fg='black')
hall.place(x=10, y=140)
hallcombo = ttk.Combobox(manage_frame,width=21, textvariable=hallvar,font=('times new roman',16, 'bold'))
hallcombo['values'] = ('Opoku Ware', 'Autonomy', 'Atwima')
hallcombo.place(x=170, y=140)

level = Label(manage_frame, text='Level',font=('times new roman',20, 'bold'), bg='green', fg='black')
level.place(x=10, y=180)
levelcombo =ttk.Combobox(manage_frame,width=6,textvariable=levelvar, font=('times new roman',16, 'bold'))
levelcombo['values'] = ('100', '200','300','400')
levelcombo.place(x=170, y=180)

klass = Label(manage_frame, text='Class',font=('times new roman',20, 'bold'), bg='green', fg='black')
klass.place(x=260, y=180)
classEntry = Entry(manage_frame, bd=2, width=8,textvariable=classvar, font=('times new roman',16, 'bold'))
classEntry.place(x=330, y=180)

indexNo = Label(manage_frame, text='Index No:', font=('times new roman',20, 'bold'), bg='green', fg='black')
indexNo.place(x=10, y=220)
#indexNoVar = IntVar()
indexNoEntry = Entry(manage_frame,textvariable=indexvar, bd=2,width=23, font=('times new roman',16, 'bold'))
indexNoEntry.place(x=170, y=220)

name = Label(manage_frame, text='Full Name',font=('times new roman',20, 'bold'), bg='green', fg='black')
name.place(x=10, y=260)
nameEntry = Entry(manage_frame,textvariable=namevar, bd=2,width=23, font=('times new roman',16, 'bold'))
nameEntry.place(x=170, y=260)


email = Label(manage_frame, text='Email',font=('times new roman',20, 'bold'), bg='green', fg='black')
email.place(x=10, y=300)
emailEntry = Entry(manage_frame, textvariable=emailvar,bd=2,width=23, font=('times new roman',16, 'bold'))
emailEntry.place(x=170, y=300)

gender = Label(manage_frame, text='Gender',font=('times new roman',20, 'bold'), bg='green', fg='black')
gender.place(x=10, y=340)
gendacombo = ttk.Combobox(manage_frame,width=21, textvariable=gendervar,font=('times new roman',16, 'bold'))
gendacombo['values'] = ('Male', 'Female')
gendacombo.place(x=170, y=340)

contact = Label(manage_frame, text='Contact',font=('times new roman',20, 'bold'), bg='green', fg='black')
contact.place(x=10, y=380)
contactEntry = Entry(manage_frame,textvariable=contactvar, bd=2,width=23, font=('times new roman',16, 'bold'))
contactEntry.place(x=170, y=380)

dob = Label(manage_frame, text='Date of Birth',font=('times new roman',20, 'bold'), bg='green', fg='black')
dob.place(x=10, y=420)
dobEntry = Entry(manage_frame, textvariable=dobvar,bd=2,width=23, font=('times new roman',16, 'bold'))
dobEntry.place(x=170, y=420)

student_type = Label(manage_frame, text='Student Type',font=('times new roman',20, 'bold'), bg='green', fg='black')
student_type.place(x=10, y=460)

stcombo = ttk.Combobox(manage_frame,width=21, textvariable=stypevar,font=('times new roman',16, 'bold'))
stcombo['values'] = ('Regular', 'Evening','Weekends','Sandwich')
stcombo.place(x=170, y=460)

# ================================================== Buttons ==================================================
btnFrame = Frame(manage_frame,bd=3, relief=GROOVE,bg='#9F000F')
btnFrame.place(x=10, y=510, width=420, height=50)

petascolbl = Label(manage_frame, text='Developed by Petasco', font=('lucida calligraphy',12, 'bold italic'),bg='green', fg='black')
petascolbl.place(x=120, y=560)
addbtn = Button(btnFrame, text='Add',command=add,font=('lucida sans',16, 'bold'),bg='red', fg='black', width=6, activebackground='green')
addbtn.place(x=6, y=3)

updatebtn = Button(btnFrame, text='Update', command=update,font=('lucida sans',16, 'bold'),bg='red', fg='black',activebackground='green')
updatebtn.place(x=105, y=3)

delbtn = Button(btnFrame, text='Delete',command=delete, font=('lucida sans',16, 'bold'),bg='red', fg='black', width=6, activebackground='green')
delbtn.place(x=210, y=3)

clearbtn = Button(btnFrame, text='Clear',command=clear,font=('lucida sans',16, 'bold'),bg='red', fg='black', width=6, activebackground='green')
clearbtn.place(x=310, y=3)

# =============================================== Display =======================================================
screenFrame = Frame(petasco,bd=4, relief=RIDGE, bg='Green')
screenFrame.place(x=500, y=100, width=860, height=590)

sortlbl = Label(screenFrame, text='Sort By', font=('times',16, 'bold'),bg='green', fg='black')
sortlbl.place(x=10, y=5)

combo_sort = ttk.Combobox(screenFrame,textvariable=sortvar,font=('lucida sans',15, 'bold'), width=10)
combo_sort['values'] = ('Department', 'Faculty', 'Class','Gender','Level','Hall', 'Student Type')
combo_sort.place(x=90, y=5)


searchlbl = Label(screenFrame,text='Search', font=('times',16, 'bold'),bg='green', fg='black')
searchlbl.place(x=350, y=5)

searchEntry = Entry(screenFrame,textvariable=searchvar, font=('lucida sans',14, 'bold'), width=13)
searchEntry.place(x=430, y=5)

# ========================================= Buttons ================================================
# sortbtn = Button(screenFrame, command=sort,text='Sort',relief=RAISED,font=('lucida sans',14, 'bold'),bg='red', fg='black', width=5, activebackground='green')
# sortbtn.place(x=260, y=5, height=28)

searchbtn = Button(screenFrame,command=search, text='Search',relief=RAISED,font=('lucida sans',14, 'bold'),bg='red', fg='black', width=8, activebackground='green')
searchbtn.place(x=600, y=5, height=30)


refreshbtn = Button(screenFrame,command=fatch_data, text='Refresh',relief=RAISED,font=('lucida sans',14, 'bold'),bg='red', fg='black', width=8, activebackground='green')
refreshbtn.place(x=720, y=5, height=30)

tableFrame = Frame(screenFrame, bd=4, relief=RIDGE, bg='crimson')
tableFrame.place(x=10, y=50, width=830, height=520)

scroll_x = Scrollbar(tableFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(tableFrame,orient=VERTICAL)

student_Table = ttk.Treeview(tableFrame, columns= ("Faculty", "Department","Hall","Level","Class","Index","Name","Email","Gender",
                                                   "Contact","DOB", "StudentType"),yscrollcommand=scroll_x,xscrollcommand=scroll_y)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)

scroll_x.config(command=student_Table.xview)
scroll_y.config(command=student_Table.yview)

student_Table.heading('Faculty', text='Faculty')
student_Table.heading('Department', text='Department')
student_Table.heading('Hall', text='Hall')
student_Table.heading('Level', text='Level')
student_Table.heading('Class', text='Class')
student_Table.heading('Index', text='Index No')
student_Table.heading('Name', text='Full Name')
student_Table.heading('Email', text='Email')
student_Table.heading('Gender', text='Gender')
student_Table.heading('Contact', text='Contact')
student_Table.heading('DOB', text='D.O.B')
student_Table.heading('StudentType', text='Student Type')

student_Table['show'] = 'headings'
student_Table.column("Faculty", width=100)
student_Table.column('Department', width=100)
student_Table.column('Hall', width=100)
student_Table.column('Level', width=100)
student_Table.column('Class', width=100)
student_Table.column('Index', width=100)
student_Table.column('Name', width=100)
student_Table.column('Email', width=100)
student_Table.column('Gender', width=100)
student_Table.column('Contact', width=100)
student_Table.column('DOB', width=100)
student_Table.column('StudentType', width=100)

student_Table.pack(fill=BOTH, expand=1)
student_Table.bind('<ButtonRelease-1>',get_cursor)
fatch_data()


icon = ImageTk.PhotoImage(file='Pictures/aamusted-logo.jpg')
petasco.iconphoto(False,icon)
petasco.resizable(False,False)
petasco.mainloop()
