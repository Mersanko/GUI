# final gui
import tkinter
from tkinter import *
import csv
from tkinter import messagebox as ms
from PIL import ImageTk,Image
import main

record = []

def reader():
    with open('record.txt',newline='') as dataa:
        data=csv.reader(dataa,delimiter=',')
        data=data
        for row in data:
            record.append(main.template(row[0],row[1],row[2],row[3],row[4],row[5]))


def writer():
    with open('record.txt','w',newline='') as dataa:
        data=csv.writer(dataa,delimiter=',')
        for a in record:
            data.writerow([a.fname]+[a.mname]+[a.lname]+[a.idnum]+[a.yrlvl]+[a.course])

def home():
    global homescreen
    # homescreen display
    homescreen = Tk()
    homescreen.geometry("360x700")
    homescreen.title("Student Record")
    homescreen.configure(background="light yellow")

    Label(text="", font=("", 40), bg="light yellow").pack()

    # it works only in my laptop because of the path/location of the image; change the location/path to make the image display work
    my_img = ImageTk.PhotoImage(Image.open("/Users/ZM/Desktop/iit.png"))
    my_label = Label(image=my_img,bg="light yellow")
    my_label.pack()

    Label(text="", font=("", 36), bg="light yellow").pack()

    # homescreen toolbar
    Button(text="Login",bg="light yellow",fg="dark red", width="24", height="2", font=(" ", 14), command=log_in).pack()
    Label(text="", font=("", 5), bg="light yellow").pack()

    Button(text="Register",bg="light yellow", fg="dark red", width="24", height="2", font=(" ", 14), command=register).pack()
    Label(text="", font=("", 5), bg="light yellow").pack()

    Button(text="Quit", bg="light yellow",width="27", height="2", font=("Arial", 14),fg="dark red", command=homescreen.destroy).pack()
    Label(text="", font=("",5), bg="light yellow").pack()


    writer()


    homescreen.mainloop()


def log_in():
    global login
    # login page display
    login = Toplevel(homescreen)
    login.title("Login")
    login.geometry('360x700')
    login.configure(background="light yellow")

    global select
    global loginbox
    global logininput
    global loginlabel


    loginbox = StringVar()

    Label(login, text="", font=("", 160), bg="light yellow").pack()


    # login credentials
    loginlabel = Label(login, text="Input ID No. below", bg="light yellow",fg="dark red",font=("Arial",17,"bold")).pack()
    Label(login, text="", font=("", 5), bg="light yellow").pack()
    logininput = Entry(login, bd=3, textvariable=loginbox)
    logininput.pack()

    Label(login, text="", font=("", 10), bg="light yellow").pack()

    Button(login, text="Done", bg="light yellow",padx=21, pady=5, font=("Arial", 13), fg="dark red", command=lambda: input(loginbox)).pack()
    Label(login, text="", font=("",5), bg="light yellow").pack()

    Button(login, text="Cancel", padx=16, pady=5, bg="light yellow", font=("Arial", 13),fg="dark red", command=login.destroy).pack()
    Label(login, text="", font=("",2), bg="light yellow").pack()


def getlist():
    global root
    root = tkinter.Tk()
    root.title("List of Students (Registered)")
    root.configure(background="light yellow")
    with open('record.txt', newline='') as dataa:
        reader = csv.reader(dataa)
        r = 0
        for col in reader:
            c = 0
            for row in col:
                label = tkinter.Label(root,width=10, height=2, text=row, relief=tkinter.RIDGE, fg="dark red", bg="light yellow")
                label.grid(row=r, column=c)
                c += 1
            r += 1
            Button(root, text="Back", width=6, height=2, bg="light yellow", font=("Arial", 13), fg="dark red",
                   command=root.destroy).grid(row=0, column=6)
    root.mainloop()



def input(dd):
    mirror = bool
    entered = loginbox.get()
    for a in record:
        if entered == a.idnum:
            mirror = True
            global studentrecord
            # student record display
            studentrecord = Toplevel(homescreen)
            studentrecord.title("Student Record")
            studentrecord.geometry("400x700")
            studentrecord.configure(background="light yellow")

            Label(studentrecord, text="", font=("", 40), bg="light yellow").pack()

            Label(studentrecord, text="Student No." + "\n" + a.idnum, fg="dark red",font=("Arial",20,"bold"), bg="light yellow").pack()

            Label(studentrecord, text="", font=("", 10), bg="light yellow").pack()

            # student record input details
            Label(studentrecord, text="First Name:",bg="light yellow", width="30", height="1",fg="dark red", font=("Arial", 14)).pack()
            Label(studentrecord, text=a.fname, bg="light yellow", width="30", height="1",fg="dark red", font=("Times", 14, "bold italic")).pack()
            Label(studentrecord, text="", font=("", 1), bg="light yellow").pack()

            Label(studentrecord, text="Middle Name:",bg="light yellow", width="30", height="1",fg="dark red", font=("Arial", 14)).pack()
            Label(studentrecord, text=a.mname, bg="light yellow", width="30", height="1",fg="dark red", font=("Times", 14, "bold italic")).pack()
            Label(studentrecord, text="", font=("", 1), bg="light yellow").pack()

            Label(studentrecord, text="Last Name:",bg="light yellow", width="30", height="1",fg="dark red", font=("Arial", 14)).pack()
            Label(studentrecord, text=a.lname, bg="light yellow", width="30", height="1",fg="dark red", font=("Times", 14, "bold italic")).pack()
            Label(studentrecord, text="", font=("", 1), bg="light yellow").pack()

            Label(studentrecord, text="ID Number:",bg="light yellow", width="30", height="1",fg="dark red", font=("Arial", 14)).pack()
            Label(studentrecord, text=a.idnum, bg="light yellow", width="30", height="1",fg="dark red", font=("Times", 14, "bold")).pack()
            Label(studentrecord, text="", font=("", 1), bg="light yellow").pack()

            Label(studentrecord, text="Year Level:",bg="light yellow", width="30", height="1",fg="dark red", font=("Arial", 14)).pack()
            Label(studentrecord, text=a.yrlvl, bg="light yellow", width="30", height="1",fg="dark red", font=("Times", 14, "bold")).pack()
            Label(studentrecord, text="", font=("", 1), bg="light yellow").pack()

            Label(studentrecord, text="Course:",bg="light yellow", width="30", height="1",fg="dark red", font=("Arial", 14)).pack()
            Label(studentrecord, text=a.course, bg="light yellow", width="30", height="1",fg="dark red", font=("Times", 14, "bold")).pack()

            Label(studentrecord, text="", font=("", 10), bg="light yellow").pack()

            #buttons for student record
            Button(studentrecord, text="Edit", bg="green", width="30", height="2", fg="dark red", font=("Arial", 13),command=lambda: edit(dd)).pack()
            Label(studentrecord, text="",font=("", 2), bg="light yellow").pack()

            Button(studentrecord, text="Delete Record", bg="green", width="30", height="2",fg="dark red", font=("Arial", 13),command=lambda: delete(dd)).pack()
            Label(studentrecord, text="",font=("", 2), bg="light yellow").pack()

            Button(studentrecord, text="See List", bg="light yellow", width="30", height="2", font=("Arial", 13), fg="dark red",command=lambda: getlist()).pack()
            Label(studentrecord, text="", font=("", 5), bg="light yellow").pack()

            Button(studentrecord, text="Back", bg="green", width="30", height="2",fg="dark red", font=("Arial", 13), command=studentrecord.destroy).pack()
            Label(studentrecord, text="",font=("", 2), bg="light yellow").pack()

            writer()


    if mirror != True:
        ms.showerror('Error', 'Record does not exist!')

def register():
    global registration
    # register/create new record display
    registration = Toplevel(homescreen)
    registration.title("Register")
    registration.geometry('400x700')
    registration.configure(background="light yellow")

    global fname
    global mname
    global lname
    global idnum
    global yrlvl
    global course
    global fname_entry
    global mname_entry
    global lname_entry
    global idnum_entry
    global yrlvl_entry
    global course_entry

    fname = StringVar()
    mname = StringVar()
    lname = StringVar()
    idnum = StringVar()
    yrlvl = StringVar()
    course = StringVar()


    Label(registration, text="", font=("", 30), bg="light yellow").pack()


    # register/create new record details
    Label(registration, text="Fill in your info below", bg="light yellow",fg="dark red",font=("Arial",17,"bold")).pack()
    Label(registration, text="",bg="light yellow").pack()

    Label(registration, text="First Name", bg="light yellow",fg="dark red",font=("Arial",14)).pack()
    fname_entry = Entry(registration,bd=3,textvariable=fname)
    fname_entry.pack()
    Label(registration, text="", font=("", 5), bg="light yellow").pack()

    Label(registration, text="Middle Name", bg="light yellow",fg="dark red",font=("Arial",14)).pack()
    mname_entry = Entry(registration,bd=3,textvariable=mname)
    mname_entry.pack()
    Label(registration, text="", font=("", 5), bg="light yellow").pack()

    Label(registration, text="Last Name", bg="light yellow",fg="dark red",font=("Arial",14)).pack()
    lname_entry = Entry(registration,bd=3,textvariable=lname)
    lname_entry.pack()
    Label(registration, text="", font=("", 5), bg="light yellow").pack()

    Label(registration, text="ID Number", bg="light yellow",fg="dark red",font=("Arial",14)).pack()
    idnum_entry = Entry(registration,bd=3,textvariable=idnum)
    idnum_entry.pack()
    Label(registration, text="", font=("", 5), bg="light yellow").pack()

    Label(registration, text="Year Level", bg="light yellow",fg="dark red",font=("Arial",14)).pack()
    yrlvl_entry = Entry(registration,bd=3,textvariable=yrlvl)
    yrlvl_entry.pack()
    Label(registration, text="", font=("", 5), bg="light yellow").pack()

    Label(registration, text="Course",bg="light yellow",fg="dark red",font=("Arial",14)).pack()
    course_entry = Entry(registration,bd=3,textvariable=course)
    course_entry.pack()
    Label(registration, text="", font=("", 5), bg="light yellow").pack()

    Label(registration, text="",font=("", 17), bg="light yellow").pack()
    Button(registration, text="Done",padx=77, pady=5,bg="light yellow",fg="dark red",font=("Arial",13),command=studrecord).pack()

    Label(registration, text="", font=("", 3), bg="light yellow").pack()
    Button(registration, text="Cancel",padx=72, pady=5, bg="light yellow", fg="dark red",font=("Arial",13), command=registration.destroy).pack()
    writer()


# for deleting record
def delete(dd):
    for a in record:
        if loginbox == dd:
            record.remove(a)
            homescreen.destroy()
            home()

def studrecord():
    registration.destroy()
    homescreen.destroy()
    fn = fname.get()
    mn = mname.get()
    ln = lname.get()
    id = idnum.get()
    yr = yrlvl.get()
    cs = course.get()
    record.append(main.template(fn, mn, ln, id, yr, cs))
    home()


def edit(update):
    global registration
    # edit/update record display
    registration = Toplevel(homescreen)
    registration.title("Update Info")
    registration.geometry('400x700')
    registration.configure(background = "light yellow")

    global fname
    global mname
    global lname
    global idnum
    global yrlvl
    global course
    global fname_entry
    global mname_entry
    global lname_entry
    global idnum_entry
    global yrlvl_entry
    global course_entry

    fname = StringVar()
    mname = StringVar()
    lname = StringVar()
    idnum = StringVar()
    yrlvl = StringVar()
    course = StringVar()

    Label(registration, text="",font=("", 34), bg="light yellow").pack()

    # edit/update record details
    Label(registration, text="Fill in your info below", fg="dark red",bg="light yellow",font=("Arial",17,"bold")).pack()
    Label(registration, text="",font=("", 17), bg= "light yellow").pack()

    Label(registration, text="First Name", fg="dark red",bg="light yellow", font=("",14)).pack()
    fname_entry = Entry(registration,bd=3, textvariable=fname)
    fname_entry.pack()
    Label(registration, text="", font=("", 1), bg="light yellow").pack()

    Label(registration, text="Middle Name", fg="dark red",bg="light yellow",font=("",14)).pack()
    mname_entry = Entry(registration,bd=3, textvariable=mname)
    mname_entry.pack()
    Label(registration, text="", font=("", 1), bg="light yellow").pack()

    Label(registration, text="Last Name", fg="dark red",bg="light yellow",font=("",14)).pack()
    lname_entry = Entry(registration,bd=3, textvariable=lname)
    lname_entry.pack()
    Label(registration, text="", font=("", 1), bg="light yellow").pack()

    Label(registration, text="ID Number",fg="dark red",bg="light yellow",font=("",14)).pack()
    idnum_entry = Entry(registration,bd=3, textvariable=idnum)
    idnum_entry.pack()
    Label(registration, text="", font=("", 1), bg="light yellow").pack()

    Label(registration, text="Year Level", fg="dark red",bg="light yellow", font=("",14)).pack()
    yrlvl_entry = Entry(registration,bd=3, textvariable=yrlvl)
    yrlvl_entry.pack()
    Label(registration, text="", font=("", 1), bg="light yellow").pack()

    Label(registration, text="Course", fg="dark red",bg="light yellow",font=("",14)).pack()
    course_entry = Entry(registration, bd=3, textvariable=course)
    course_entry.pack()

    Label(registration, text="", font=("", 20), bg="light yellow").pack()

    Button(registration, text="Save Changes", padx=50, pady=5,fg="dark red", bg="light yellow", command=lambda: save(update)).pack()

    Label(registration, text="", font=("", 2), bg="light yellow").pack()

    Button(registration, text ="Cancel", padx=74, pady=5, fg="dark red",bg="light yellow", command=registration.destroy).pack()


    writer()


# for saving changes
def save(dd):
    for b in record:
        if loginbox == dd:
            b.fname = fname.get()
            b.mname = mname.get()
            b.lname = lname.get()
            b.idnum = idnum.get()
            b.yrlvl = yrlvl.get()
            b.course = course.get()
            registration.destroy()
            studentrecord.destroy()
            homescreen.destroy()
            home()
    writer()


reader()
writer()
home()

