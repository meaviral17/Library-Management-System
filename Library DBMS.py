
import sys
from tkinter import *
import tkinter.messagebox as msgBox
import mysql.connector as sql


 

def connection():
    global mydb
    global mycur
    mydb=sql.connect(host="localhost", user="root", passwd="mysql", database="d6")
    mycur=mydb.cursor()
    if not mydb.is_connected():
        msgBox.showinfo("Connection Status","Database Not Connected...")

 

def saveRec():
    it_cd=it_cdTxt.get()
    it_nm=it_nmTxt.get()
    cost=rateTxt.get()
    if it_cd=='' or it_nm=='' or cost=='':
        msgBox.showinfo("Data Error","Required All Data...")
    else:
        mycur.execute("insert into hardware values({},'{}','{}',{})".format(int(it_cd),it_nm,auth_nm,float(cost)))
        mydb.commit()
        msgBox.showinfo("Data Insertion Report", str(mycur.rowcount)+"Record(s) inserted successfully...")
        it_cdTxt.delete(0,'end')
        it_nmTxt.delete(0,'end')
        auth_nmTxt.delete(0,'end')
        rateTxt.delete(0,'end')
        it_cdTxt.focus_set()

 

def deleRec():
    if it_cdTxt.get()=='':
        msgBox.showinfo("Data Error","Item Code Required...")
    else:
        mycur.execute("delete from hardware where it_cd={}".format(int(it_cdTxt.get())))
        mydb.commit()
        msgBox.showinfo("Data Deletion Report", str(mycur.rowcount)+"Record(s) Deleted successfully...")
        it_cdTxt.delete(0,'end')
        it_nmTxt.delete(0,'end')
        auth_nmTxt.delete(0,'end')
        rateTxt.delete(0,'end')
        it_cdTxt.focus_set()

 

def modifyRec():
    it_cd=it_cdTxt.get()
    it_nm=it_nmTxt.get()
    cost=rateTxt.get()
    if it_cd=='' or it_nm=='' or cost=='':
        msgBox.showinfo("Data Error","Required All Data...")
    else:
        mycur.execute("update hardware set it_nm='{}', cost={}, auth_nm='{}' where it_cd={}".format(it_nm,float(cost),auth_nm,int(it_cd)))
        mydb.commit()
        msgBox.showinfo("Data Modification Report", str(mycur.rowcount)+"Record(s) Modified successfully...")
        it_cdTxt.delete(0,'end')
        it_nmTxt.delete(0,'end')
        auth_nmTxt.delete(0,'end')
        rateTxt.delete(0,'end')
        it_cdTxt.focus_set()

 
def searchRec():
    if it_cdTxt.get()=='':
        msgBox.showinfo("Data Error","Item Code Required for Searching Data...")
    else:
        mycur.execute("Select * from hardware where it_cd={}".format(int(it_cdTxt.get())))
    data=mycur.fetchall()
    if mycur.rowcount>0:
        for x in data: 
            #it_cdTxt.insert(0,x[0])
            it_nmTxt.insert(0,x[1])
            auth_nmTxt.insert(0,x[2])
            rateTxt.insert(0,x[3])
    else:
        msgBox.showinfo("Data Error","Record Not Found...")
        

 

def exitWindow():
    mydb.close()
    sys.exit()
    

 

MainWindow = Tk()
MainWindow.geometry("400x200")
MainWindow['background']='antiquewhite2'
MainWindow.title("Library Management System")

 

connection()

 

it_cdLbl=Label(MainWindow, text=" ID: ", bg='antiquewhite2', font=('bold', 13))
it_cdLbl.place(x=20, y=30)
it_cdTxt = Entry()
it_cdTxt.place(x=160, y=30)

 

it_nmLbl=Label(MainWindow, text="Book Name: ", bg='antiquewhite2', font=('bold', 13))
it_nmLbl.place(x=20, y=60)
it_nmTxt = Entry()
it_nmTxt.place(x=160, y=60)


auth_nmLbl=Label(MainWindow, text="Author: ", bg='antiquewhite2', font=('bold', 13))
auth_nmLbl.place(x=20, y=90)
auth_nmTxt = Entry()
auth_nmTxt.place(x=160, y=90)
 

rateLbl=Label(MainWindow, text="Price: ", bg='antiquewhite2', font=('bold', 13))
rateLbl.place(x=20, y=120)
rateTxt = Entry()
rateTxt.place(x=160, y=120)

 

saveBtn=Button(MainWindow, text="Save", font=('bold', 13), bg="SpringGreen2", command=saveRec)
saveBtn.place(x=20, y=150)

 

deleBtn=Button(MainWindow, text="Delete", font=('bold', 13), bg="orange red", command=deleRec)
deleBtn.place(x=80, y=150)

 

modiBtn=Button(MainWindow, text="Modify", font=('bold', 13), bg="deep sky blue", command=modifyRec)
modiBtn.place(x=150, y=150)

 

searchBtn=Button(MainWindow, text="Search", font=('bold', 13), bg="gray55", command=searchRec)
searchBtn.place(x=220, y=150)

 

extBtn=Button(MainWindow, text="Exit", font=('bold', 13), bg="purple2", command=exitWindow)
extBtn.place(x=295, y=150)

 

MainWindow.mainloop()
  
