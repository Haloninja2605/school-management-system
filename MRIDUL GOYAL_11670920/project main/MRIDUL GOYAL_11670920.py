# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 16:39:34 2021

@author: mridu
"""

import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from captcha.image import ImageCaptcha
import random as ra
import pickle
import csv
import datetime
import os
from tkcalendar import Calendar
import datetime

queue=[]
# defining window geometry
window3=tk.Tk()
window3.geometry("1920x1080")
window3.title("User Sign In")

#________________________admin window__________________
def adminwindow():
    window1=tk.Toplevel()
    window1.geometry("1920x1080")
    window1.title("Database")
    
    #creating images
    img1=ImageTk.PhotoImage(file="teacher.png")
    img2=ImageTk.PhotoImage(file="student.png")
    img3=ImageTk.PhotoImage(file="summary.png")
    img4=ImageTk.PhotoImage(file="out.png")
    img5=ImageTk.PhotoImage(file="Logo.jpg")
    
    # creating image canvas
    bg= ImageTk.PhotoImage(file="OIP.png")
    canvas=tk.Canvas(window1,width=1920, height=1080)
    canvas.pack(expand=True)
    
    
    # add image to a canvas
    canvas.create_image(0,0,image=bg, anchor="nw")
    
    #adding canvas for signup
    canvas1=tk.Canvas(window1,width=220, height=735)
    canvas1.place(x=50,y=30)
    canvas12=tk.Canvas(window1,width=1100, height=735)
    canvas12.place(x=350,y=30)
    
    def teacher():
    
        canvas12=tk.Canvas(window1,width=1100, height=735)
        canvas12.place(x=350,y=30)
        canvas3=tk.Canvas(window1,width=1080, height=100,bg="#f6cd61")
        canvas3.place(x=360,y=40)
        
        def date():
            cal = Calendar(window1,font="Arial 14", selectmode='day',cursor="hand1", year=2000, month=2, day=5)
            cal.place(x=650,y=310)
            canvasbtn=tk.Canvas(window1)
            canvasbtn.place(x=800, y=550)
            def newbtn():
                global date
                date=str(cal.get_date())
                lst=date.split("/")
                if int(lst[0])<10:
                    month="0"+lst[0]
                else:
                    month=lst[0]
                if int(lst[1])<10:
                    day="0"+lst[1]
                else:
                    day=lst[1]
                if int(lst[2])>21:
                    year="19"+lst[2]
                else:
                    year="20"+lst[2]
                date=day+"-"+month+"-"+year
                labeldate=tk.Label(window1,text=date, font="helvetica 15 bold")
                return cal.destroy(), canvasbtn.destroy(),labeldate.place(x=800,y=290), date
        
            btn1=tk.Button(canvasbtn, text="ok", height=2, width=3, bg="sky blue", command=newbtn)
            btn1.pack()
            
        def datejoin():
            cal = Calendar(window1,font="Arial 14", selectmode='day',cursor="hand1", year=2021, month=2, day=5)
            cal.place(x=700,y=450)
            canvasbtn=tk.Canvas(window1)
            canvasbtn.place(x=850, y=690)
            def newbtn():
                global datej
                lst=[]
                datej=str(cal.get_date())
                lst=datej.split("/")
                if int(lst[0])<10:
                    month="0"+lst[0]
                else:
                    month=lst[0]
                if int(lst[1])<10:
                    day="0"+lst[1]
                else:
                    day=lst[1]
                if int(lst[2])>21:
                    year="19"+lst[2]
                else:
                    year="20"+lst[2]
                datej=day+"-"+month+"-"+year
            
                labeldate=tk.Label(window1,text=datej, font="helvetica 15 bold")
                return cal.destroy(), canvasbtn.destroy(),labeldate.place(x=800,y=570),datej
    
            btn1=tk.Button(canvasbtn, text="ok", height=2, width=3, bg="sky blue", command=newbtn)
            btn1.pack()
            
        #drop down____________
        def callback(selection):
            global gender
            gender=selection
        options=["Select Gender","Male","Female"]
        clicked=tk.StringVar()
        clicked.set("Select Gender")
        drop=tk.OptionMenu(window1, clicked, *options, command=callback)
        drop.place(x=650,y=210)
        
        # labels_______________
        label1=tk.Label(window1,text="Teacher window",font="helvetica 25 bold underline",bg="#f6cd61")
        label1.place(x=775,y=65)
        
        label2=tk.Label(window1,text="Name :", font="helvetica 15 bold")
        label2.place(x=400,y=170)
        
        label3=tk.Label(window1,text="Gender :", font="helvetica 15 bold")
        label3.place(x=400,y=210)
        
        label4=tk.Label(window1,text="Father Name :", font="helvetica 15 bold")
        label4.place(x=400,y=250)
        
        label5=tk.Label(window1,text="Date Of Birth :", font="helvetica 15 bold")
        label5.place(x=400,y=290)
        
        label6=tk.Label(window1,text="Address :", font="helvetica 15 bold")
        label6.place(x=400,y=330)
        
        label7=tk.Label(window1,text="Mob No. :", font="helvetica 15 bold")
        label7.place(x=400,y=370)
        
        label8=tk.Label(window1,text="Aadhar UIN :", font="helvetica 15 bold")
        label8.place(x=400,y=410)
        
        label19=tk.Label(window1,text="PAN No. :", font="helvetica 15 bold")
        label19.place(x=400,y=450)
        
        label20=tk.Label(window1,text="Teaching Subject :", font="helvetica 15 bold")
        label20.place(x=400,y=490)
        
        label21=tk.Label(window1,text="Class Incharge :", font="helvetica 15 bold")
        label21.place(x=400,y=530)
        
        label22=tk.Label(window1,text="Date Of Joining :", font="helvetica 15 bold")
        label22.place(x=400,y=570)
        
        label23=tk.Label(window1,text="Username :", font="helvetica 15 bold")
        label23.place(x=1000,y=410)
        
        label24=tk.Label(window1,text="Password :", font="helvetica 15 bold")
        label24.place(x=1000,y=450)
        
        # entries
        entry1=tk.Entry(window1,width=45)
        entry1.place(x=650,y=170)
        
        entry2=tk.Entry(window1,width=45)
        entry2.place(x=650,y=250)
        
        entry4=tk.Entry(window1,width=45)
        entry4.place(x=650,y=330)
        
        entry5=tk.Entry(window1,width=45)
        entry5.place(x=650,y=370)
        
        entry6=tk.Entry(window1,width=45)
        entry6.place(x=650,y=410)
        
        entry7=tk.Entry(window1,width=45)
        entry7.place(x=650,y=450)
        
        entry8=tk.Entry(window1,width=45)
        entry8.place(x=650,y=490)
        
        entry10=tk.Entry(window1,width=45)
        entry10.place(x=1150,y=410)

        entry11=tk.Entry(window1,width=45)
        entry11.place(x=1150,y=450)
        
        def clasel(selection):
            global classt
            classt=selection
        options=["Select Class","I","II","III","ÏV","V","VI","VII","VIII","IX","X"]
        class2=tk.StringVar()
        class2.set("Select Class")
        dropc=tk.OptionMenu(window1, class2, *options, command=clasel)
        dropc.place(x=650,y=530)
        
        def classstud2(selection1):
                global teachclasssec
                teachclasssec=selection1
        options=["Select Section","A","B"]
        section=tk.StringVar()
        section.set("Select Section")
        dropsec=tk.OptionMenu(window1, section, *options, command=classstud2)
        dropsec.place(x=800,y=530)
        
        # --------------Button Functions------------
        def add_details():
            f=open("D:/project_data/data_teacher/teacher.csv","a")
            try:
                global date
                d=date
            
                global datej
                doj=datej
                
                global gender
                g=gender
                global classselection
                classselection=classt
                
                global sectionselection
                sectionselection=teachclasssec
                flagnn1=0
            except:
                flagnn1=1
                
                
            nm=(entry1.get()).upper()
            fname=(entry2.get()).upper()
            
            address=(entry4.get()).upper()
            mobno=entry5.get()
            if len(mobno)==10:
                flag1=0
            else:
                flag1=1
            aadhar=entry6.get()
            if len(aadhar)==8 and aadhar.isdigit():
                flag2=0
            else:
                flag2=1
            pan=(entry7.get()).upper()
            global flag3
            flag3=0
            if len(pan)==10:
                count=1
                for i in pan:
                    if count<=5 or count==10:
                        if i.isalpha()==True:
                            flag3=0
                        else:
                            flag3=1
                            break
                    elif count>=6 and count<=9:
                        if i.isdigit()==True:
                            flag3=0
                        else:
                            flag3=1
                            break
                    count+=1
            else:
                flag3=1
                
                    
                    
            
            user=(entry10.get()).lower()
            if len(user)!=0:
                flag4=0
            else:
                flag4=1
            passwor=entry11.get()
            if len(passwor)==0:
                flag5=1
            else:
                flag5=0
                
            flagmain=0
            if flag1==1 or flag2==1 or flag3==1 or flag4==1 or flag5==1 :
                flagmain=1
        
            
            
            def added():
                
                if flagmain==0:
                    flagus=1
                    lst=[nm,gender,fname,d,address,mobno,aadhar,doj,classselection, sectionselection,user,passwor,pan]
                    wr=csv.writer(f)
                    wr.writerow(lst)
                    f.close()
                    f1=open("D:/project_data/admin/user.dat","rb")
                    f2=open("D:/project_data/admin/user.dat","ab")
                    try:
                        while True:
                            lst=pickle.load(f1)
                            if lst==[user,passwor]:
                                flagus=0
                    except EOFError:
                        f1.close()
                        if flagus!=0:
                            pickle.dump([user,passwor], f2)
                        f2.close()
                    
                    labelcommand=tk.Label(window1,text="RECORD ADDED", font="bold 15 underline", fg="red")
                    labelcommand.place(x=800,y=600)
                    labelcommand.after(1000,lambda:teacher())
                else:
                    global flag3
                    if flagnn1==1:
                        labelcommand=tk.Label(window1,text="ENTER DETAILS", font="bold 15 underline", fg="red")
                        labelcommand.place(x=800,y=600)
                        labelcommand.after(1000,lambda:labelcommand.destroy())
                    elif flag1==1:
                        labelcommand=tk.Label(window1,text="INVALID MOBILE NO.", font="bold 15 underline", fg="red")
                        
                        labelcommand.place(x=800,y=600)
                        labelcommand.after(1000,lambda:labelcommand.destroy())
                    elif flag2==1:
                        
                        labelcommand=tk.Label(window1,text="INVALID AADHAR(LENGTHSHOULD BE 8)", font="bold 15 underline", fg="red")
                        labelcommand.place(x=800,y=600)
                        labelcommand.after(1000,lambda:labelcommand.destroy())
                    elif flag3==1:
                        
                        labelcommand=tk.Label(window1,text="INVALID PAN", font="bold 15 underline", fg="red")
                        labelcommand.place(x=800,y=600)
                        labelcommand.after(1000,lambda:labelcommand.destroy())
                    elif flag4==1:
                        
                        labelcommand=tk.Label(window1,text="INVALID USERNAME", font="bold 15 underline", fg="red")
                        labelcommand.place(x=800,y=600)
                        labelcommand.after(1000,lambda:labelcommand.destroy())
                    elif flag5==1:
                        
                        labelcommand=tk.Label(window1,text="INVALID password", font="bold 15 underline", fg="red")
                        labelcommand.place(x=800,y=600)
                        labelcommand.after(1000,lambda:labelcommand.destroy())
                        
                    
                    
            return added()
        
        
        #buttons____
        buttonlogo=tk.Button(window1,image=img5)
        buttonlogo.place(x=1150, y=170)
        
        buttonadd=tk.Button(window1,text="Add", font="helvetica 25 bold",bg="#0057e7",command=add_details)
        buttonadd.place(x=700,y=650)
        
        def updatefun():
            os.startfile("D:/project_data/data_teacher/teacher.csv")
            
        buttonup=tk.Button(window1,text="Update", font="helvetica 25 bold", bg="#0057e7",command=updatefun)
        buttonup.place(x=900,y=650)
        
        buttondob=tk.Button(window1,text="Select date", font="helvetica 10 bold",command=date)
        buttondob.place(x=650,y=290)
        
        buttondob=tk.Button(window1,text="Select date", font="helvetica 10 bold",command=datejoin)
        buttondob.place(x=650,y=570)
        
    def student():
        canvas12=tk.Canvas(window1,width=1100, height=735)
        canvas12.place(x=350,y=30)
        canvas3=tk.Canvas(window1,width=1080, height=100,bg="#f6cd61")
        canvas3.place(x=360,y=40)
            
        def dob():
            cal = Calendar(window1,font="Arial 14", selectmode='day',cursor="hand1", year=2000, month=2, day=5)
            cal.place(x=650,y=330)
            canvasbtn=tk.Canvas(window1)
            canvasbtn.place(x=800, y=550)
            def newbtn():
                global dob
                dob=cal.get_date()
                lst=dob.split("/")
                if int(lst[0])<10:
                    month="0"+lst[0]
                else:
                    month=lst[0]
                if int(lst[1])<10:
                    day="0"+lst[1]
                else:
                    day=lst[1]
                if int(lst[2])>21:
                    year="19"+lst[2]
                else:
                    year="20"+lst[2]
                dob=day+"-"+month+"-"+year
                labeldate=tk.Label(window1,text=dob, font="helvetica 15 bold")
                return cal.destroy(), canvasbtn.destroy(),labeldate.place(x=800,y=330)
            btn1=tk.Button(canvasbtn, text="ok", height=2, width=3, bg="sky blue", command=newbtn)
            btn1.pack()
        
        def dojstud():
            cal = Calendar(window1,font="Arial 14", selectmode='day',cursor="hand1", year=2021, month=2, day=5)
            cal.place(x=650,y=450)
            canvasbtn=tk.Canvas(window1)
            canvasbtn.place(x=800, y=690)
            def newbtn():
                global dojstu
                dojstu=cal.get_date()
                lst=dojstu.split("/")
                if int(lst[0])<10:
                    month="0"+lst[0]
                else:
                    month=lst[0]
                if int(lst[1])<10:
                    day="0"+lst[1]
                else:
                    day=lst[1]
                if int(lst[2])>21:
                    year="19"+lst[2]
                else:
                    year="20"+lst[2]
                dojstu=day+"-"+month+"-"+year
                labeldate=tk.Label(window1,text=dojstu, font="helvetica 15 bold")
                return cal.destroy(), canvasbtn.destroy(),labeldate.place(x=800,y=490)
            btn2=tk.Button(canvasbtn, text="ok", height=2, width=3, bg="sky blue", command=newbtn)
            btn2.pack()
            
        #drop down____________
        def callback1(selection):
                global gende
                gende=selection
        options=["Select Gender","Male","Female"]
        clicked=tk.StringVar()
        clicked.set("Select Gender")
        drop=tk.OptionMenu(window1, clicked, *options, command=callback1)
        drop.place(x=650,y=250)
        
        def classstud2(selection1):
                global classsec
                classsec=selection1
        options=["Select Section","A","B"]
        section=tk.StringVar()
        section.set("Select Section")
        dropsec=tk.OptionMenu(window1, section, *options, command=classstud2)
        dropsec.place(x=1150,y=450)
        
        def classstud1(selection2):
            global classsel
            classsel=selection2
        options=["Select Class","I","II","III","ÏV","V","VI","VII","VIII","IX","X"]
        class1=tk.StringVar()
        class1.set("Select Class")
        drop=tk.OptionMenu(window1, class1, *options,command=classstud1)
        drop.place(x=1150,y=410)
        
        
        # labels_______________
        label1=tk.Label(window1,text="Student window",font="helvetica 25 bold underline",bg="#f6cd61")
        label1.place(x=775,y=65)
        
        label2=tk.Label(window1,text="Reg No. :", font="helvetica 15 bold")
        label2.place(x=400,y=170)
        
        label3=tk.Label(window1,text="Name :", font="helvetica 15 bold")
        label3.place(x=400,y=210)
    
        label4=tk.Label(window1,text="Gender :", font="helvetica 15 bold")
        label4.place(x=400,y=250)
        
        label5=tk.Label(window1,text="Father Name :", font="helvetica 15 bold")
        label5.place(x=400,y=290)
        
        label6=tk.Label(window1,text="Date Of Birth :", font="helvetica 15 bold")
        label6.place(x=400,y=330)
        
        label7=tk.Label(window1,text="Address:", font="helvetica 15 bold")
        label7.place(x=400,y=370)
        
        label8=tk.Label(window1,text="Mob No. :", font="helvetica 15 bold")
        label8.place(x=400,y=410)
        
        label19=tk.Label(window1,text="Aadhar UIN:", font="helvetica 15 bold")
        label19.place(x=400,y=450)

        
        label21=tk.Label(window1,text="Date Of Joining :", font="helvetica 15 bold")
        label21.place(x=400,y=490)
        
        
        label23=tk.Label(window1,text="Class :", font="helvetica 15 bold")
        label23.place(x=1000,y=410)
        
        label24=tk.Label(window1,text="Section :", font="helvetica 15 bold")
        label24.place(x=1000,y=450)
        
        
        # entries
        entry1=tk.Entry(window1,width=45)
        entry1.place(x=650,y=170)
        
        entry2=tk.Entry(window1,width=45)
        entry2.place(x=650,y=210)
        
        entry3=tk.Entry(window1,width=45)
        entry3.place(x=650,y=290)
        
        
        entry5=tk.Entry(window1,width=45)
        entry5.place(x=650,y=370)
        
        entry6=tk.Entry(window1,width=45)
        entry6.place(x=650,y=410)
        
        entry7=tk.Entry(window1,width=45)
        entry7.place(x=650,y=450)
        
        
        
        
        
        def add_detailsstud(): 
            flagnn=0
            try:
                global gende
                genstud=str(gende)
                
                global classsel
                classin=str(classsel)
                
                global dob
                date=str(dob)
            
                global classsec
                classin1=str(classsec)
                
                global dojstu
                datejstud=str(dojstu)
                
                
            except:
                flagnn=1
            regno=str((entry1.get()).upper())
            if len(regno)==0:
                flagstud=1
            else:
                flagstud=0
            name=str((entry2.get()).upper())
            

            
            fnam=str((entry3.get()).upper())
            address=str((entry5.get()).upper())
            mobno=str(entry6.get())
            if len(mobno)==10:
                flagstud1=0
            else:
                flagstud1=1
            aadharstud=entry7.get()
            if len(aadharstud)==8 and aadharstud.isdigit():
                flagstud2=0
            else:
                flagstud2=1
      
            
            flagmain=0
            if flagstud==1 or flagstud1==1 or flagstud2==1 :
                flagmain=1
        
            
            
            def added():
                try:
                    f=open("D:/project_data/data_student/stud.csv","r")
                    count=1
                    n=regno
                    lst=csv.reader(f)
                    
                    global flagus
                    flagus=0
                    count=1
                    try:
                        for i in lst:
                            if count!=1:
                                if n==int(i[0]):
                                    flagus=1
                                    break
                                else:
                                    flagus=0
                            count+=1
                    except IndexError:
                        f.close()
                
                    f=open("D:/project_data/data_student/stud.csv","r")
                    lstteach=[]
                    count=1
                    lst12=csv.reader(f)
                    try:
                        for j in lst12:
                            if count!=1:
                                lstteach+=[j[0]]
                            count+=1
                    except IndexError:
                        f.close()
                except EOFError:
                    pass
                if flagmain==0 and flagus==0:
                    f=open("D:/project_data/data_student/stud.csv","a")
                    lstfinal=[regno,name,gende,fnam,date,address,mobno,aadharstud,datejstud,classin,classin1]
                    wr=csv.writer(f)
                    wr.writerow(lstfinal)
                    f.close()
                    filename=classin+"_"+classin1+".csv"
                    filestring="D:\project_data\data_student"+"\class"+filename
                    flagfile=0
                    try:
                        f=open(filestring,"r")
                        f.close()
                    except FileNotFoundError:
                        flagfile=1
                        if flagfile==1:
                            f=open(filestring,"w")
                            f.close()
                    fin=open(filestring,"a")
                    swriter=csv.writer(fin)
                    lstmark=[regno,name]
                    swriter.writerow(lstmark)
                    fin.close()
                    labelcommand=tk.Label(window1,text="RECORD ADDED", font="bold 15 underline", fg="red")
                    labelcommand.place(x=800,y=600)
                    labelcommand.after(1000,lambda:student())
                else:
                    if flagnn==1:
                        labelcommand=tk.Label(window1,text="ENTER DETAILS", font="bold 15 underline", fg="red")
                        labelcommand.place(x=800,y=600)
                        labelcommand.after(1000,lambda:labelcommand.destroy())
                    elif flagstud==1:
                        labelcommand=tk.Label(window1,text="ENTER REGISTRATION NO.", font="bold 15 underline", fg="red")
                        labelcommand.place(x=800,y=600)
                        labelcommand.after(1000,lambda:labelcommand.destroy())
                    elif flagus==1:
                        labelcommand=tk.Label(window1,text="ENTER VALID REGISTRATION NO.", font="bold 15 underline", fg="red")
                        labelcommand.place(x=800,y=600)
                        labelcommand.after(1000,lambda:labelcommand.destroy())
        
                    elif flagstud1==1:
                        
                        labelcommand=tk.Label(window1,text="INVALID MOBILE NO.", font="bold 15 underline", fg="red")
                        labelcommand.place(x=800,y=600)
                        labelcommand.after(1000,lambda:labelcommand.destroy())
                    elif flagstud2==1:
                        labelcommand=tk.Label(window1,text="INVALID AADHAR", font="bold 15 underline", fg="red")
                        labelcommand.place(x=800,y=600)
                        labelcommand.after(1000,lambda:labelcommand.destroy())
        
            return added()
    
    
    
        #buttons____
        buttonlogo=tk.Button(window1,image=img5)
        buttonlogo.place(x=1150, y=170)
        buttondob=tk.Button(window1,text="Select date", font="helvetica 10 bold",command=dob)
        buttondob.place(x=650,y=330)
        
        buttondob=tk.Button(window1,text="Select date", font="helvetica 10 bold",command=dojstud)
        buttondob.place(x=650,y=490)
        
        buttonadd=tk.Button(window1,text="Add", font="helvetica 25 bold", bg="#0057e7",command=add_detailsstud)
        buttonadd.place(x=700,y=650)
        
        def updatefunstud():
            os.startfile("D:/project_data/data_student/stud.csv")
            
        buttonup=tk.Button(window1,text="Update", font="helvetica 25 bold", bg="#0057e7",command=updatefunstud)
        buttonup.place(x=900,y=650)
        
    def summary():
        canvas12=tk.Canvas(window1,width=1100, height=735)
        canvas12.place(x=350,y=30)
        canvas3=tk.Canvas(window1,width=1080, height=100,bg="#f6cd61")
        canvas3.place(x=360,y=40)
        
        
        #drop down____________
        options=["Select Table","Teachers","Students"]
        clicked1=tk.StringVar()
        clicked1.set("Select Table")
        drop=tk.OptionMenu(window1, clicked1, *options)
        drop.place(x=600,y=170)
        
        def show2():
            filename=classselection+"_"+sectionselection+".csv"
            filestring="D:\project_data\data_student"+"\class"+filename
            flagfile=0
            try:
                f=open(filestring,"r")
                f.close()
            except FileNotFoundError:
                flagfile=1
            if flagfile==1:
                f=open(filestring,"w")
                f.close()
            os.startfile(filestring)
            return summary()
    
        def show():
            if clicked1.get()=="Students":
                labelstud=tk.Label(window1,text="select class and section")
                def selclass(sel1):
                    global classselection
                    classselection=sel1
                options=["Select Class","I","II","III","ÏV","V","VI","VII","VIII","IX","X"]
                class2=tk.StringVar()
                class2.set("Select Class")
                drop1=tk.OptionMenu(window1, class2, *options, command=selclass)
                def selsec(sel2):
                    global sectionselection
                    sectionselection=sel2
                options=["Select Class","I","II","III","ÏV","V","VI","VII","VIII","IX","X"]
                sections=tk.StringVar()
                sectionoptions=["Select section","A","B"]
                sections.set("Select section")
                drop2=tk.OptionMenu(window1, sections, *sectionoptions,command=selsec)
                buttonb=tk.Button(window1,text="show",command=show2,bg="#0057e7",fg="white")
                global buttona
                return buttona.destroy(), labelstud.place(x=800,y=170),drop1.place(x=950,y=170),buttonb.place(x=1300,y=170),drop2.place(x=1100,y=170),
            elif clicked1.get()=="Teachers":
                return os.startfile("D:/project_data/data_teacher/teacher.csv"),summary()
        
    
        # labels_______________
        label1=tk.Label(window1,text="Summary",font="helvetica 25 bold underline",bg="#f6cd61")
        label1.place(x=775,y=65)
        label2=tk.Label(window1,text="Select table",font="helvetidca 15 bold")
        label2.place(x=400, y=170)
    
    
        # buttons
        global buttona
        buttona=tk.Button(window1,text="show",command=show,bg="#0057e7",fg="white")
        buttona.place(x=800,y=170)
        
    def log_out():
        return window1.destroy()
    #buttons
    button1=tk.Button(window1,text="Teacher",image=img1, compound="top",width=180,height=160, command=teacher)
    button1.place(x=70,y=40)
    
    button2=tk.Button(window1,text="Student",image=img2, compound="top",width=180,height=160, command=student)
    button2.place(x=70,y=230)
    
    button3=tk.Button(window1,text="Summary",image=img3, compound="top",width=180,height=160, command=summary)
    button3.place(x=70,y=400)
    
    button1=tk.Button(window1,text="Log out",image=img4, compound="top",width=180,height=160, command=log_out)
    button1.place(x=70,y=590)
            
        
        
    window1.mainloop()
        
        
        
#_________________________________GENERATING CAPTCHA_______________________
def randnumb():
    lst=["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    l=len(lst)
    s=""
    for i in range(5):
        a=ra.randint(0,l-1)
        s+=lst[a]
        b=s
    return b


captch=ImageCaptcha()
rd1=randnumb()
captch.write(rd1,"1.png")
captch=tk.PhotoImage(file="1.png")

# creating image canvas
bg= ImageTk.PhotoImage(file="colour.png")
canvas=tk.Canvas(window3,width=1920, height=1080)
canvas.pack(expand=True)



# add image to a canvas
canvas.create_image(0,0,image=bg, anchor="nw")

#adding canvas for signup
canvas1=tk.Canvas(window3,width=800, height=700)
canvas1.place(x=350,y=60)

# adding labels to signup window
label=tk.Label(window3,text="Welcome user", font=("bold 25 underline"), fg="black",)
label.place(x=645,y=90)

label1=tk.Label(window3,text="User Sign In", font=("bold 25 underline"), fg="blue",)
label1.place(x=655,y=170)

label2=tk.Label(window3,text="Username", font=("bold",15), fg="black",)
label2.place(x=475,y=230)

label3=tk.Label(window3,text="password", font=("bold",15), fg="black",)
label3.place(x=475,y=270)

label4=tk.Label(window3,text="Security code", font=("bold",15), fg="black",)
label4.place(x=475,y=310)

label5=tk.Label(window3,text="admin login", font=("bold",15), fg="black",)
label5.place(x=475,y=500)

label6=tk.Label(window3,text="New User ID and password will be assigned by the admin only", font=("bold",15), fg="black",)
label6.place(x=475,y=600)

label7=tk.Label(window3,text="Note: forgot password, contact admin", font=("bold",15), fg="black",)
label7.place(x=575,y=640)



#enty logs
entry=tk.Entry(window3, width=50)
entry.place(x=630,y=235)

entry1=tk.Entry(window3, width=50)
entry1.place(x=630,y=275)

entry2=tk.Entry(window3, width=20)
entry2.place(x=630,y=315)


#________________________log function________________________________
def logbook(entry1,entry2):
    def openfile(stringfile):
        flagfile=0
        try:
            f=open(stringfile,"r")
            f.close()
        except FileNotFoundError:
            flagfile=1
        if flagfile==1:
            f=open(stringfile,"w")
            f.close()
        os.startfile(stringfile)

    dict1={}
    fin =open("D:\project_data\data_teacher/teacher.csv","r")
    lst=list(csv.reader(fin))
    for i in lst:
        if i[-3]==entry1 and i[-2]==entry2:
            dict1[i[0]]=(i[8],i[9])
            stringfile="D:\project_data\data_student\class"+i[8]+"_"+i[9]+".csv"
            openfile(stringfile)
            break
    
# _______________________check __ Function___________________________
def check():
    f=open("D:/project_data/admin/user.dat","rb")
    flag=0
    try:

        while True:
            lat1=pickle.load(f)
            st1=lat1[0]
            st2=lat1[1]
            if st1==entry.get() and st2==entry1.get():
                   flag=1
    except EOFError:
        f.close()
    if flag!=0:
        if entry2.get()==rd1:
            labelcommand=tk.Label(window3,text="Welcome", font="bold 15 underline", fg="red")
            labelcommand.place(x=475,y=450)
            logbook(st1, st2)
            logbook(entry.get(), entry1.get())
            labelcommand.after(1000,lambda:labelcommand.destroy())
        else:
            labelcommand=tk.Label(window3,text="invalid CAPTCHA", font="bold 15 underline", fg="red")
            labelcommand.place(x=475,y=450)
            labelcommand.after(1000,lambda:labelcommand.destroy())
    else:
        labelcommand=tk.Label(window3,text="invalid user id or password", font="bold 15 underline", fg="red")
        labelcommand.place(x=475,y=450)
        labelcommand.after(1000,lambda:labelcommand.destroy())
        


#___________________________________ADMIN WINDOW LAYOUT_________________________
def admin():
    window2=tk.Toplevel()
    window2.geometry("1920x1080")
    window2.title("Admin Log In")
    
    # creating image canvas
    bg= ImageTk.PhotoImage(file="loginbg.png")
    canvaswin=tk.Canvas(window2,width=1920, height=1080)
    canvaswin.pack(expand=True)

        

    # add image to a canvas
    canvaswin.create_image(0,0,image=bg, anchor="nw")
    
    #adding canvas for Admin login
    canvaswin1=tk.Canvas(window2,width=800, height=700)
    canvaswin1.place(x=350,y=30)
    
    #___________Adminwindow LABELS____________
    labelwin=tk.Label(window2,text="Welcome Admin", font=("bold 25 underline"), fg="black",)
    labelwin.place(x=645,y=90)

    labelwin1=tk.Label(window2,text="Admin Sign In", font=("bold 25 underline"), fg="blue",)
    labelwin1.place(x=655,y=170)
    
    labelwin2=tk.Label(window2,text="Username", font=("bold",15), fg="black",)
    labelwin2.place(x=475,y=230)
    
    labelwin3=tk.Label(window2,text="password", font=("bold",15), fg="black",)
    labelwin3.place(x=475,y=270)
    
    labelwin4=tk.Label(window2,text="Security code", font=("bold",15), fg="black",)
    labelwin4.place(x=475,y=310)
    
    labelwin6=tk.Label(window2,text="New admin User ID and password will be assigned by the school authorities only", font=("bold",15), fg="black",)
    labelwin6.place(x=400,y=550)
    
    labelwin7=tk.Label(window2,text="Note: forgot password, contact school authorities", font=("bold",15), fg="black",)
    labelwin7.place(x=500,y=590)
    
    
    #enty logs
    entrywin=tk.Entry(window2, width=50)
    entrywin.place(x=630,y=235)
    
    entrywin1=tk.Entry(window2, width=50)
    entrywin1.place(x=630,y=275)
    
    entrywin2=tk.Entry(window2, width=20)
    entrywin2.place(x=630,y=315)
    
    # CAPTCHA_____________________________________
    
    captchwin=ImageCaptcha()
    rd2=randnumb()
    captchwin.write(rd2,"2.png")
    captchwin=tk.PhotoImage(file="2.png")
    
    
    def checkwin():
        f=open("D:/project_data/admin/admin.txt","r")
        st1=(f.read()).split("\t")
        t=[entrywin.get(),entrywin1.get()]
        
        if t==st1:
            if entrywin2.get()==rd2:
                labelcommand=tk.Label(window2,text="Welcome", font="bold 15 underline", fg="red")
                labelcommand.place(x=475,y=450)
                labelcommand.after(1000,lambda:labelcommand.destroy())
                return adminwindow()
                
            else:
                labelcommand=tk.Label(window2,text="invalid CAPTCHA", font="bold 15 underline", fg="red")
                labelcommand.place(x=475,y=450)
                labelcommand.after(1000,lambda:labelcommand.destroy())
        else:
            labelcommand=tk.Label(window2,text="invalid user id or password", font="bold 15 underline", fg="red")
            labelcommand.place(x=475,y=450)
            labelcommand.after(1000,lambda:labelcommand.destroy())
            
    
    #buttons
    buttonwin1=tk.Button(window2,height=1,width=10,text="log in",fg="white",bg="#4285F4",font="Roboto",command=checkwin)
    buttonwin1.place(x=750,y=370)
    
    buttonwin3=tk.Button(window2,image=captchwin)
    buttonwin3.place(x=475,y=365)

    window2.mainloop()

#buttons
button1=tk.Button(window3,height=1,width=10,text="Sign in",fg="white",bg="#4285F4",font="Roboto",command=check)
button1.place(x=750,y=370)

button1=tk.Button(window3,height=1,width=10,text="Log in",fg="white",bg="#4285F4",font="Roboto",command=admin)
button1.place(x=750,y=500)

button3=tk.Button(image=captch)
button3.place(x=475,y=380)



# closing loop
window3.mainloop()