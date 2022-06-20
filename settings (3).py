from ast import pattern
from calendar import c
from cgitb import enable, text
from distutils import command
from itertools import count
from pydoc import describe
from secrets import choice
from sqlite3 import enable_callback_tracebacks
import string
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import BOLD
from urllib.parse import parse_qs
from xml.dom.minidom import Entity
from PIL import ImageTk, Image, ImageFile
from matplotlib.font_manager import json_dump
from numpy import choose, empty, place
import pandas as pd
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename
import os
import webbrowser
from pip import main
from tkcalendar import Calendar
from tkcalendar import DateEntry
from datetime import date
from tkinter import filedialog
import subprocess
import mysql.connector
import io
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import shutil
import csv
import json
from tkinter import font,colorchooser
from tkinter import font as tkFont
from _tkinter import TclError
from tkinter.scrolledtext import ScrolledText


fbilldb = mysql.connector.connect(
    host="localhost", user="root", password="", database="fbillingsintgrtd5(3)", port="3306"
)
fbcursor = fbilldb.cursor(buffered=True)

ImageFile.LOAD_TRUNCATED_IMAGES = True

def reset():
  global root
  root.destroy()


# root.title("F-Billing Revolution 2022(FREE version) | Company database:fbillingdb | User:Administrator")
def log():
    global user_name1
    user_name1=username1.get()
    passwd1=password1.get()
    if user_name1=="" or passwd1=="":
        Label(text='Plz enter both username and password',fg='red').place(x=85,y=260)
    else:
        sql='SELECT * FROM users WHERE username=%s AND password=%s'
        val=(user_name1,passwd1,)
        fbcursor.execute(sql,val)
        if fbcursor.fetchone()is not None:
            mainpage()
            if user_name1 != "adminstator":
              tab06.destroy()
            else:
              pass
            root.iconify()
        else:
            messagebox.showinfo('Acess denied','Username Or Password Wrong')

  
sql = "select * from users"
fbcursor.execute(sql)
user_log = fbcursor.fetchall()
if not user_log:
  def lo():
    mainpage()
  root=Tk()
  root.geometry("500x250")
  root.resizable(False, False)
  root.eval('tk::PlaceWindow . center')
  Label(text='Wellocome to F-Billing Revolution 2022',font='arial 13 bold').place(x=100,y=40)
  submitbtn1=Button(text='OPEN NOW', width=20,height=2,command=lo,activeforeground="white",activebackground="black",font='arial 8 bold').place(x=165,y=100)             
else:
    root=Tk()
    root.geometry("500x200")
    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center')
    root.title("F-Billing Revolution 2022")
    p1 = PhotoImage(file = 'images/fbicon.png')
    root.iconphoto(False,p1)
    username1=StringVar()
    password1=StringVar()

    Label(text='Login F-Billing Revolution 2022',font='arial 13 bold').place(x=120,y=15)
    
  
    sql = "select username from users"
    fbcursor.execute(sql)
    user_log_name = fbcursor.fetchall()
    uss1=Label(text='Username').place(x=120,y=65)
    ee1 = ttk.Combobox(textvariable=username1)
    ee1.place(x=220,y=65)
    ee1["values"] = user_log_name

    pss1=Label(text='Password').place(x=120,y=105)
    ee2=Entry(textvariable=password1,show='*',width=23).place(x=220,y=105)
    
    submitbtn1=Button(text='Login', width=15,command=log,activeforeground="white",
                   activebackground="black").place(x=250,y=150)
    
  
invoices= PhotoImage(file="images/invoice.png")
orders = PhotoImage(file="images/order.png")
estimates = PhotoImage(file="images/estimate.png")
recurring = PhotoImage(file="images/recurring.png")
purchase = PhotoImage(file="images/purchase.png")
expenses = PhotoImage(file="images/expense.png")
customer = PhotoImage(file="images/customer.png")
product = PhotoImage(file="images/package.png")
reports = PhotoImage(file="images/report.png")
setting = PhotoImage(file="images/setting.png")
tick = PhotoImage(file="images/check.png")
warnin = PhotoImage(file="images/sign_warning.png")
cancel = PhotoImage(file="images/close.png")
saves = PhotoImage(file="images/save.png")
folder = PhotoImage(file="images/folder-black.png")
photo11 = PhotoImage(file = "images/invoice-pvt.png")
customer = PhotoImage(file="images/customer.png")
smslog = PhotoImage(file = "images/smslog.png")
video = PhotoImage(file = "images/video.png")
mark1 = PhotoImage(file="images/mark.png")
mark2 = PhotoImage(file="images/mark2.png")
photo10 = PhotoImage(file = "images/text-message.png")
addnew = PhotoImage(file="images/plus.png")
delete = PhotoImage(file="images/delete_E.png")

selectall = PhotoImage(file="images/table_select_all.png")
cut = PhotoImage(file="images/cut.png")
copy = PhotoImage(file="images/copy.png")
paste = PhotoImage(file="images/paste.png")

undo = PhotoImage(file="images/undo.png")
redo = PhotoImage(file="images/redo.png")
bold = PhotoImage(file="images/bold.png")

italics = PhotoImage(file="images/italics.png")
underline = PhotoImage(file="images/underline.png")
left = PhotoImage(file="images/left.png")
  
right = PhotoImage(file="images/right.png")
center = PhotoImage(file="images/center.png")
hyperlink = PhotoImage(file="images/hyperlink.png")
color = PhotoImage(file="images/font_color.png")
remove = PhotoImage(file="images/eraser.png")
  
  
photo = PhotoImage(file = "images/plus.png")
photo1 = PhotoImage(file = "images/edit.png")
photo2 = PhotoImage(file = "images/delete_E.png")
photo3 = PhotoImage(file = "images/export-file.png")
photo4 = PhotoImage(file = "images/seo.png")
photo5 = PhotoImage(file = "images/printer.png")
photo6 = PhotoImage(file = "images/gmail.png")
photo7 = PhotoImage(file = "images/priewok.png")
photo8 = PhotoImage(file = "images/refresh_E.png")
photo9 = PhotoImage(file = "images/sum.png")
photo10 = PhotoImage(file = "images/text-message.png")

################ expenses button images ####################
exprefreshIcon = ImageTk.PhotoImage(Image.open("images/refresh.png"))
expsearchIcon = ImageTk.PhotoImage(Image.open("images/search-icon.png"))
expdeleteIcon = ImageTk.PhotoImage(Image.open("images/delete.png"))
expeditIcon = ImageTk.PhotoImage(Image.open("images/edit.png"))
expenseIcon = ImageTk.PhotoImage(Image.open("images/plus.png"))
################ Product service button images ####################
prorefreshIcon = ImageTk.PhotoImage(Image.open("images/refresh.png"))
proexportIcon = ImageTk.PhotoImage(Image.open("images/export-file.png"))
proimportIcon = ImageTk.PhotoImage(Image.open("images/import.png"))
prosearchIcon = ImageTk.PhotoImage(Image.open("images/research.png"))
prodeleteIcon = ImageTk.PhotoImage(Image.open("images/delete.png"))
productIcon = ImageTk.PhotoImage(Image.open("images/plus.png"))
proeditIcon = ImageTk.PhotoImage(Image.open("images/edit.png"))


def mainpage():
  root.iconify()
  main = Toplevel()
  main.geometry("1360x730")
  p1 = PhotoImage(file = 'images/fbicon.png')
  main.iconphoto(False, p1)
  main.title("F-Billing Revolution 2022(FREE version) | Company database:fbillingdb | User:Administrator")
  s = ttk.Style()
  s.theme_use('default')
  s.configure('TNotebook.Tab', background="#999999", width=20, padding=10)
  tabControl = ttk.Notebook(main)
  tab1 = ttk.Frame(tabControl)
  tab2 = ttk.Frame(tabControl)
  tab3=  ttk.Frame(tabControl)
  tab4 = ttk.Frame(tabControl)
  tab5 = ttk.Frame(tabControl)
  tab6=  ttk.Frame(tabControl)
  tab7 = ttk.Frame(tabControl)
  tab8 = ttk.Frame(tabControl)
  tab9 =  ttk.Frame(tabControl)
  tab10=  ttk.Frame(tabControl)
  tabControl.add(tab1,image=invoices,compound = LEFT, text ='Invoices',)
  tabControl.add(tab2,image=orders,compound = LEFT, text ='Orders')
  tabControl.add(tab3,image=estimates,compound = LEFT, text ='Estimates')
  tabControl.add(tab4,image=recurring,compound = LEFT, text ='Recurring')
  tabControl.add(tab5,image=purchase,compound = LEFT, text ='Purchase Orders') 
  tabControl.add(tab6,image=expenses,compound = LEFT, text ='Expenses')
  tabControl.add(tab7,image=customer,compound = LEFT, text ='Customers')
  tabControl.add(tab8,image=product,compound = LEFT, text ='Product/Services')
  tabControl.add(tab9,image=reports,compound = LEFT, text ='Report')
  tabControl.add(tab10,image=setting,compound = LEFT, text ='Settings')
  tabControl.pack(expand = 1, fill ="both")
  
  def check_empty() :
       if entry.get():
           pass     #your function where you want to jump
       else:
          messagebox.showinfo("Information", "Required entry")

  ###########################    Expense Module   ##############################
  
  def add_expense():
      def upload_file():
        import shutil
        global filename,img, b2
        f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
        filename = filedialog.askopenfilename(filetypes=f_types)
        print(filename, 'name')
        #import pdb; pdb.set_trace()
        shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
        image = Image.open(filename)
        resize_image = image.resize((120, 120))
        img = ImageTk.PhotoImage(resize_image)
        b2 = Label(expenselabelframe,image=img, height=120, width=120)
        b2.place(x=450, y=240)
      
      global filename
      filename = ""
      def insert_expenses():# insert expenses data
        expense_amount = expamountval.get()
        date = expdate.get_date()
        vendor = vn.get()
        catagory = cn.get()
        description = expdescriptionentry.get()
        staff_members = expstaffentry.get()
        taxable = checkvarStatus4.get()
        customer = cus.get()
        id_sku = id_sku1.get()
        notes = exptxt.get('1.0', 'end-1c')
        rebill_amount = rebill_amoun.get()
        rebillab = rebill.get()
        recipt = imge.get()
        assign_cus = other.get()
        tax2 = tax2expstr.get()
    
        if filename == "":
          sql='INSERT INTO Expenses (expense_amount,date,vendor,catagory,description,staff_members,taxable,    customer,id_sku,notes,rebill_amount,rebillable,receipt,assign_customer,tax2) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,  %s,  %s,%s,%s,%s,%s,%s)' #adding values into db
          val=(expense_amount,date,vendor,catagory,description,staff_members,taxable,customer,id_sku,notes,    rebill_amount,rebillab,recipt,assign_cus,tax2)
          fbcursor.execute(sql,val)
          fbilldb.commit()
        else:
          shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
          sql='INSERT INTO Expenses (expense_amount,date,vendor,catagory,description,staff_members,taxable,customer,id_sku,notes,rebill_amount,image,rebillable,receipt,assign_customer,tax2) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' #adding values into db
          val=(expense_amount,date,vendor,catagory,description,staff_members,taxable,customer,id_sku,notes,  rebill_amount,filename.split('/')[-1],rebillab,recipt,assign_cus,tax2)
          fbcursor.execute(sql,val)
          fbilldb.commit()
        for record in exp_tree.get_children():
          exp_tree.delete(record)
        count=0
        fbcursor.execute('SELECT * FROM Expenses;')
        for i in fbcursor:
          if True:
            if i[13] == '1':
              e = 'Yes'
            else:
              e = 'No'
            exp_tree.insert(parent='', index='end', iid=i, text='hello', values=(i[0], i[10], i[4], i[6], i[5], i[8], i[7], e , i[14], i[11],i[16],i[3]))
          count += 1
        window.destroy()


    

     
  
      window = Toplevel()  
      
      window.title("Add new Expense")
      window.resizable(0,0)
      p2 = PhotoImage(file = 'images/fbicon.png')
      window.iconphoto(False, p1)
  
      window.geometry("618x449+380+167")
  
      innerexpFrame = Frame(window, relief=GROOVE)
      innerexpFrame.pack(side="top",fill=BOTH)
  
      expenselabelframe = LabelFrame(innerexpFrame,text="Expense Cost",width=580,height=400)
      expenselabelframe.pack(side="top",fill=BOTH,padx=10)
  
      def number_expacount(S,d):
        sql = "select decimalseperator from company"
        fbcursor.execute(sql)
        deci_sgin = fbcursor.fetchone()
        if deci_sgin[0] == '.':
          if d == '1': #insert
            if not S in ['.','0','1','2','3','4','5','6','7','8','9']:
              return False
            return True
        elif deci_sgin[0] == ',':
          if d == '1': #insert
            if not S in ['0','1','2','3','4','5','6','7','8','9',',']:
              return False
            return True
        if d.isdigit():
          return True
        
        
  
      def expaonclick(event):
        sql = "select currencysign,currsignplace from company"
        fbcursor.execute(sql)
        currsymb = fbcursor.fetchone()
        if not currsymb:
          pass
        else:
          if currsymb[1] == "before amount":
            expamountentry.insert (0, currsymb[0])
            expamountnum = (expenselabelframe.register(number_expacount),'%S','%d')
            expamountentry.config(validate='key',validatecommand=(expamountnum),justify='left')
          elif currsymb[1] == "before amount with space":
            expamountentry.insert (0, currsymb[0] + " ")
            expamountnum = (expenselabelframe.register(number_expacount),'%S','%d')
            expamountentry.config(validate='key',validatecommand=(expamountnum),justify='left')
          elif currsymb[1] == "after amount":
            expamountval.set(currsymb[0])
            expamountnum = (expenselabelframe.register(number_expacount),'%S','%d')
            expamountentry.config(validate='key',validatecommand=(expamountnum),justify='right')
          elif currsymb[1] == "after amount with space":
            expamountval.set(" " + currsymb[0])
            expamountnum = (expenselabelframe.register(number_expacount),'%S','%d')
            expamountentry.config(validate='key',validatecommand=(expamountnum),justify='right')
          else:
            pass
          
  
  
  
      expamountval = StringVar(expenselabelframe,)
      expamount=Label(expenselabelframe,text="Expense amount:",pady=10,padx=10)
      expamount.place(x=12,y=0)
      expamountentry = Entry(expenselabelframe,width=15,textvariable=expamountval)
    
      expamountentry.bind("<ButtonRelease>", expaonclick)
      expamountentry.place(x=130,y=10)
  
      
  
  
  
  
      lbl_date=Label(expenselabelframe,text=" Date :",fg='black')
      lbl_date.place(x=380,y=10)
      
      expdate=DateEntry(expenselabelframe)
      expdate.place(x=450,y=12)

      sql = "select dateformat from company"
      fbcursor.execute(sql)
      date_for = fbcursor.fetchone()
     
      if not date_for:
        pass
      else:
        if date_for[0] == "mm-dd-yyyy":
          expdate._set_text(expdate._date.strftime('%m-%d-%Y'))
        elif date_for[0] == "dd-mm-yyyy":
          expdate._set_text(expdate._date.strftime('%d-%m-%Y'))
        elif date_for[0] == "yyy.mm.dd":
          expdate._set_text(expdate._date.strftime('%Y.%m.%d'))
        elif date_for[0] == "mm/dd/yyyy":
          expdate._set_text(expdate._date.strftime('%m/%d/%Y'))
        elif date_for[0] == "dd/mm/yyy":
          expdate._set_text(expdate._date.strftime('%d/%m/%Y'))
        elif date_for[0] == "dd.mm.yyyy":
          expdate._set_text(expdate._date.strftime('%d.%m.%Y'))
        elif date_for[0] == "yyyy/mm/dd":
          expdate._set_text(expdate._date.strftime('%Y/%m/%d'))
        else:
          pass
  
      sql = "select businessname from Customer where customertype =%s or customertype =%s"
      val = ('vendor','both(client,vendor)')
      fbcursor.execute(sql,val)
      pdata = fbcursor.fetchall()
  
      vendor1=Label(expenselabelframe,text="Vendor:",pady=5,padx=10)
      vendor1.place(x=20,y=40)
      vn = StringVar() 
      vendor = ttk.Combobox(expenselabelframe, width = 27, textvariable = vn ) 
        
      # Adding combobox drop down list 
      vendor['values'] = pdata
        
      vendor.place(x=130,y=45) 
      # vendor.current(0)
  
      categoryexp1=Label(expenselabelframe,text="Category:",pady=5,padx=10)
      categoryexp1.place(x=330,y=40)
      cn = StringVar() 
      categorydrop = ttk.Combobox(expenselabelframe, width = 22, textvariable = cn ) 
        
      # Adding combobox drop down list 
      categorydrop['values'] = ('Default' ) 
        
      categorydrop.place(x=400,y=45) 
      categorydrop.current(0)
  
      
  
      expdescription=Label(expenselabelframe,text="Description:",pady=10,padx=10)
      expdescription.place(x=12,y=70)
      expdescriptionentry = Entry(expenselabelframe,width=70)
      expdescriptionentry.place(x=130,y=81)
  
      expstafftval = StringVar(expenselabelframe, value='Administrator')
      expstaff=Label(expenselabelframe,text="Staff member:",pady=10,padx=10)
      expstaff.place(x=12,y=108)
      expstaffentry = Entry(expenselabelframe,width=30,textvariable=expstafftval)
      expstaffentry.place(x=130,y=118)
  
      sql = "select taxtype from company"
      fbcursor.execute(sql)
      taxchoose = fbcursor.fetchone()
      
      
      
      checkvarStatus4=BooleanVar()
    
      Button4 = Checkbutton(expenselabelframe,variable = checkvarStatus4, 
                        text="Taxable Tax1 rate", 
                        onvalue ='1' ,
                        offvalue = '0',
                       )
      
      tax2expstr = BooleanVar()
      tax2exp = Checkbutton(expenselabelframe,variable = tax2expstr, 
                        text="Taxable Tax2 rate", 
                        onvalue ='1' ,
                        offvalue = '0',
                        )
  
      if not taxchoose:
        pass
      elif taxchoose[0] == '1':
        Button4.place_forget()
        tax2exp.place_forget()
      elif taxchoose[0] == '2':
        Button4.place(x=400,y=125)
        tax2exp.place_forget()
      elif taxchoose[0] == '3':
        tax2exp.place(x=400,y=105)
        Button4.place(x=400,y=125)
  
      sql = "select businessname from Customer"
      fbcursor.execute(sql,)
      cusdata = fbcursor.fetchall()
      print(cusdata)
  
      def toggle():
        if other.get():
          ent.place(x=45,y=180)
          button51.place(x=250, y=160)
        else:
          ent.place_forget()
          button51.place_forget()
          button51.deselect()
          ent.delete(0, END)
          id_skuentry.delete(0,END)
          rebill_entry.delete(0,END)
          id_skulabel.place_forget()
          id_skuentry.place_forget()
          rebill_label.place_forget()
          rebill_entry.place_forget()
      other = BooleanVar()
      button5 = Checkbutton(expenselabelframe, text="Assign to customer (optional)", variable=other, 
      command=toggle)
      button5.place(x=40, y=160)
      cus = StringVar()
      ent=ttk.Combobox(expenselabelframe,width=30,textvariable=cus,values=cusdata)
  
      ent.delete(0,'end')
      def toggle():
        id_skuentry.delete(0, END)
        rebill_entry.delete(0, END)
        if rebill.get():
          id_skulabel.place(x=375,y=160)
          id_skuentry.place(x=420,y=160)
          rebill_label.place(x=335,y=180)
          rebill_entry.place(x=420, y=180)
        else:
          id_skulabel.place_forget()
          id_skuentry.place_forget()
          rebill_label.place_forget()
          rebill_entry.place_forget()
      rebill = BooleanVar()

      sql = "select * from users"
      fbcursor.execute(sql)
      rebill_check_user = fbcursor.fetchall()
      
      if not rebill_check_user:
        button51 = Checkbutton(expenselabelframe, text="Rebillable" ,variable=rebill, command=toggle,onvalue   ='Yes' ,offvalue = 'NO')
      else:
        try:
          user_namech = username1.get()
          sql = "select rebill_exprense from users where username = %s"
          val = (user_namech,)
          fbcursor.execute(sql,val)
          disable_rebillabe_exp = fbcursor.fetchone()
          if disable_rebillabe_exp[0] == 1:
            button51 = Checkbutton(expenselabelframe, text="Rebillable" ,variable=rebill, command=toggle,onvalue   ='Yes' ,offvalue = 'NO')
          else:
            pass
        except:
           button51 = Checkbutton(expenselabelframe, text="Rebillable" ,variable=rebill, command=toggle,onvalue   ='Yes' ,offvalue = 'NO')
      
    
      
      id_sku1 = StringVar()
      id_skulabel=Label(expenselabelframe,text="id_sku:")
      id_skuentry = Entry(expenselabelframe,width=15,textvariable=id_sku1)
    
      def number_rebill_amoun(S,d):
        sql = "select decimalseperator from company"
        fbcursor.execute(sql)
        deci_sgin = fbcursor.fetchone()
        if deci_sgin[0] == '.':
          if d == '1': #insert
            if not S in ['.','0','1','2','3','4','5','6','7','8','9']:
              return False
            return True
        elif deci_sgin[0] == ',':
          if d == '1': #insert
            if not S in ['0','1','2','3','4','5','6','7','8','9',',']:
              return False
            return True
        if d.isdigit():
          return True
        
        
        
  
      def rebillamoonclick(event):
        sql = "select currencysign,currsignplace from company"
        fbcursor.execute(sql)
        currsymb = fbcursor.fetchone()
        if currsymb[1] == "before amount":
          rebill_entry.insert (0, currsymb[0])
          rebi_amo = (expenselabelframe.register(number_rebill_amoun),'%S','%d')
          rebill_entry.config(validate='key',validatecommand=(rebi_amo),justify='left')
        elif currsymb[1] == "before amount with space":
          rebill_entry.insert (0, currsymb[0] + " ")
          rebi_amo = (expenselabelframe.register(number_rebill_amoun),'%S','%d')
          rebill_entry.config(validate='key',validatecommand=(rebi_amo),justify='left')
        elif currsymb[1] == "after amount":
          rebill_amoun.set(currsymb[0])
          rebi_amo = (expenselabelframe.register(number_rebill_amoun),'%S','%d')
          rebill_entry.config(validate='key',validatecommand=(rebi_amo),justify='right')
        elif currsymb[1] == "after amount with space":
          rebill_amoun.set(" " + currsymb[0])
          rebi_amo = (expenselabelframe.register(number_rebill_amoun),'%S','%d')
          rebill_entry.config(validate='key',validatecommand=(rebi_amo),justify='right')
  
      rebill_amoun = StringVar()
      rebill_label=Label(expenselabelframe,text="Rebill amount:")
      rebill_entry = Entry(expenselabelframe,width=15,textvariable=rebill_amoun)
      rebill_entry.bind("<ButtonRelease>", rebillamoonclick)
      
  
  
      
      
      def toggle():
        if imge.get():
          browseimg.place(x=40,y=220)
          browsebutton.place(x=350,y=220,height=30,width=50)
          
        else:
          browseimg.place_forget()
          browsebutton.place_forget()
        
      imge = BooleanVar()
      Button6 = Checkbutton(expenselabelframe, text = "Attach receipt image(optional,image will be stored to   the database)",command=toggle,variable=imge)
      Button6.place(x=40, y=200)
      browseimg=Label(expenselabelframe,text="(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
      browsebutton=Button(expenselabelframe,text = 'Browse',command=upload_file)
  
  
      exptext1=Label(expenselabelframe,text="Notes",pady=5,padx=10)
      exptext1.place(x=12,y=246)
      exptxt = scrolledtext.ScrolledText(expenselabelframe, undo=True,width=50,height=5)
      exptxt.place(x=22,y=280)
  
      expokButton = Button(window, text ="Ok",image=tick,width=70,compound = LEFT,command=insert_expenses)
      expokButton.place(x=280,y=415)
  
      window.mainloop()
  

  def add_expense_connection():
    sql = "select * from users"
    fbcursor.execute(sql)
    addexp_check_user = fbcursor.fetchall()
    if not addexp_check_user:
      add_expense()
    else:
      try:
        user_namech = username1.get()
        sql = "select create_expense from users where username = %s"
        val = (user_namech,)
        fbcursor.execute(sql,val)
        disable_create_exp = fbcursor.fetchone()
        if disable_create_exp[0] == 1:
          add_expense()
        else:
          messagebox.showerror("user","user does not have permission to perform this action")
      except:
        add_expense()
        
      
      
  
      
    

  

  

########################VIEW/EDIT EXPENSE#######################################################################



  def edit_expense():

    try:
      itemid = exp_tree.item(exp_tree.focus())["values"][0]
      sql = "select * from Expenses where expensesid = %s"
      val = (itemid, )

      fbcursor.execute(sql, val)
      psdata = fbcursor.fetchone()
      def upload_file1():
        global filename,img, b1
        f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
        filename = filedialog.askopenfilename(filetypes=f_types)
        #import pdb; pdb.set_trace()
        shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
        image = Image.open(filename)
        resize_image = image.resize((120, 120))
        img = ImageTk.PhotoImage(resize_image)
        b1 = Label(expenselabelframe,image=img, height=120, width=120)
        b1.place(x=450, y=240)

      global filename
      filename = ""
      def update_expenses():# Storing values into db (user)
        itemid = exp_tree.item(exp_tree.focus())["values"][0]
        expense_amount = expamountval.get()
        date = expdate.get_date()
        vendor = vn.get()
        catagory = cn.get()
        description = expdescriptionentry.get()
        staff_members = expstafftval.get()
        taxable = checkvarStatus4.get()
        customer = cus.get()
        id_sku = id_sku1.get()
        notes = exptxt.get('1.0', 'end-1c')
        rebill_amount = rebill_amoun.get()
        rebillabe = rebill.get()
        assign_cus = other.get()
        recepit = imge.get()
        tax2 = tax2expstr.get()

        itemid1 = exp_tree.item(exp_tree.focus())["values"][0]
        sq = 'select image from Expenses where expensesid = %s'
        va =(itemid1,)
        fbcursor.execute(sq,va)
        up = fbcursor.fetchone()
        # file = shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
        if filename == "":
          sql='UPDATE Expenses set expense_amount=%s,date=%s,vendor=%s,catagory=%s,description=%s,    staff_members=%s,taxable=%s,customer=%s,id_sku=%s,notes=%s,rebill_amount=%s,rebillable=%s,assign_customer=%s,receipt=%s,tax2=%s where expensesid=%s'
          val=(expense_amount,date,vendor,catagory,description,staff_members,taxable,customer,id_sku,notes,
          rebill_amount,rebillabe,assign_cus,recepit,tax2,itemid)
          fbcursor.execute(sql,val)
          fbilldb.commit()
        else:
          file = shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
          sql='UPDATE Expenses set expense_amount=%s,date=%s,vendor=%s,catagory=%s,description=%s,    staff_members=%s,taxable=%s,customer=%s,id_sku=%s,notes=%s,rebill_amount=%s,image=%s,rebillable=%s,assign_customer=%s,receipt=%s,tax2=%s where expensesid=%s'
          val=(expense_amount,date,vendor,catagory,description,staff_members,taxable,customer,id_sku,notes,
          rebill_amount,filename.split('/')[-1],rebillabe,assign_cus,recepit,tax2,itemid)
          fbcursor.execute(sql,val)
          fbilldb.commit()
        for record in exp_tree.get_children():
            exp_tree.delete(record)
        count=0
        fbcursor.execute('SELECT * FROM Expenses;')
        for i in fbcursor:
            if True:
              if i[13] == '1':
                e = 'Yes'
              else:
                e = 'No'
              exp_tree.insert(parent='', index='end', iid=i, text='hello', values=(i[0], i[10], i[4], i[6], i[5], i[8], i[7], e , i[14], i[11],i[16],i[3]))
            else:
                pass
        count += 1
        window1.destroy()
      
      
      window1 = Toplevel()  
      
      window1.title("Edit Expense")
      p2 = PhotoImage(file = 'images/fbicon.png')
      # recimage= PhotoImage(file= 'images/'+psdata[11])
     
      # image = Image.open(recimage)
      # resize_image = image.resize((120, 120))
      # imga = ImageTk.PhotoImage(resize_image)
      window1.iconphoto(False, p1)
   
      window1.geometry("618x449+380+167")
  
      innerexpFrame = Frame(window1, relief=GROOVE)
      innerexpFrame.pack(side="top",fill=BOTH)
  
      expenselabelframe = LabelFrame(innerexpFrame,text="Expense Cost",width=580,height=400)
      expenselabelframe.pack(side="top",fill=BOTH,padx=10)
  
      def number_expacount(S,d):
        sql = "select decimalseperator from company"
        fbcursor.execute(sql)
        deci_sgin = fbcursor.fetchone()
        if deci_sgin[0] == '.':
          if d == '1': #insert
            if not S in ['.','0','1','2','3','4','5','6','7','8','9']:
              return False
            return True
        elif deci_sgin[0] == ',':
          if d == '1': #insert
            if not S in ['0','1','2','3','4','5','6','7','8','9',',']:
              return False
            return True
        if d.isdigit():
          return True
        
        
  
      def expaonclick(event):
        sql = "select currencysign,currsignplace from company"
        fbcursor.execute(sql)
        currsymb = fbcursor.fetchone()
        if not currsymb:
          pass
        else:
          if currsymb[1] == "before amount":
            expamountentry.delete (0, END)
            expamountentry.insert (0, currsymb[0])
            expamountnum = (expenselabelframe.register(number_expacount),'%S','%d')
            expamountentry.config(validate='key',validatecommand=(expamountnum),justify='left')
          elif currsymb[1] == "before amount with space":
            expamountentry.delete (0, END)
            expamountentry.insert (0, currsymb[0] + " ")
            expamountnum = (expenselabelframe.register(number_expacount),'%S','%d')
            expamountentry.config(validate='key',validatecommand=(expamountnum),justify='left')
          elif currsymb[1] == "after amount":
            expamountentry.delete (0, END)
            expamountval.set(currsymb[0])
            expamountnum = (expenselabelframe.register(number_expacount),'%S','%d')
            expamountentry.config(validate='key',validatecommand=(expamountnum),justify='right')
          elif currsymb[1] == "after amount with space":
            expamountentry.delete (0, END)
            expamountval.set(" " + currsymb[0])
            expamountnum = (expenselabelframe.register(number_expacount),'%S','%d')
            expamountentry.config(validate='key',validatecommand=(expamountnum),justify='right')
          else:
            pass
      expamountval = StringVar()
      expamount=Label(expenselabelframe,text="Expense amount:",pady=10,padx=10)
      expamount.place(x=12,y=0)
      expamountentry = Entry(expenselabelframe,width=15,textvariable=expamountval)
      expamountentry.bind("<ButtonRelease>", expaonclick)
      expamountentry.place(x=130,y=10)
      expamountentry.delete(0,'end')
      expamountentry.insert(0, psdata[3])
  
      lbl_date=Label(expenselabelframe,text=" Date :",fg='black')
      lbl_date.place(x=380,y=10)
      
      
      expdate=DateEntry(expenselabelframe)
      expdate.place(x=450,y=12)
      expdate.delete(0,'end')
      expdate.insert(0, psdata[4])

      sql = "select dateformat from company"
      fbcursor.execute(sql)
      date_for = fbcursor.fetchone()
     
      if not date_for:
        pass
      else:
        if date_for[0] == "mm-dd-yyyy":
          expdate._set_text(expdate._date.strftime('%m-%d-%Y'))
        elif date_for[0] == "dd-mm-yyyy":
          expdate._set_text(expdate._date.strftime('%d-%m-%Y'))
        elif date_for[0] == "yyy.mm.dd":
          expdate._set_text(expdate._date.strftime('%Y.%m.%d'))
        elif date_for[0] == "mm/dd/yyyy":
          expdate._set_text(expdate._date.strftime('%m/%d/%Y'))
        elif date_for[0] == "dd/mm/yyy":
          expdate._set_text(expdate._date.strftime('%d/%m/%Y'))
        elif date_for[0] == "dd.mm.yyyy":
          expdate._set_text(expdate._date.strftime('%d.%m.%Y'))
        elif date_for[0] == "yyyy/mm/dd":
          expdate._set_text(expdate._date.strftime('%Y/%m/%d'))
        else:
          pass
      
      

      sql = "select businessname from Customer where customertype =%s or customertype =%s"
      val = ('vendor','both(client,vendor)')
      fbcursor.execute(sql,val)
      pdat = fbcursor.fetchall()
      vendor1=Label(expenselabelframe,text="Vendor:",pady=5,padx=10)
      vendor1.place(x=20,y=40)
      vn = StringVar() 
      vendor = ttk.Combobox(expenselabelframe, width = 27, textvariable = vn ) 
     
        
      # Adding combobox drop down list 
      vendor['values'] = pdat
        
      vendor.place(x=130,y=45) 
      vendor.delete(0,'end')
      vendor.insert(0, psdata[5]) 
  
      categoryexp1=Label(expenselabelframe,text="Category:",pady=5,padx=10)
      categoryexp1.place(x=330,y=40)
      cn = StringVar() 
      categorydrop = ttk.Combobox(expenselabelframe, width = 22, textvariable = cn ) 
      categorydrop.delete(0,'end')
      categorydrop.insert(0, psdata[6])
   
        
      # Adding combobox drop down list 
      categorydrop['values'] = ('Default') 
        
      categorydrop.place(x=400,y=45)
    
  
      
  
      expdescription=Label(expenselabelframe,text="Description:",pady=10,padx=10)
      expdescription.place(x=12,y=70)
      expdescriptionentry = Entry(expenselabelframe,width=70)
      expdescriptionentry.place(x=130,y=81)
      expdescriptionentry.delete(0,'end')
      expdescriptionentry.insert(0, psdata[7])
  
      expstafftval = StringVar(expenselabelframe, value='Administrator')
      expstaff=Label(expenselabelframe,text="Staff member:",pady=10,padx=10)
      expstaff.place(x=12,y=108)
      expstaffentry = Entry(expenselabelframe,width=30,textvariable=expstafftval)
      expstaffentry.place(x=130,y=118)
      expstaffentry.delete(0,'end')
      expstaffentry.insert(0, psdata[8])


      
      sql = "select taxtype from company"
      fbcursor.execute(sql)
      taxchoose = fbcursor.fetchone()

  
      checkvarStatus4=BooleanVar()
     
      Button4 = Checkbutton(expenselabelframe,variable = checkvarStatus4, 
                        text="Taxable Tax1 rate", 
                        onvalue ='1',
                        offvalue = '0',
                        )
              
      tax2expstr = BooleanVar()
      tax2exp = Checkbutton(expenselabelframe,variable = tax2expstr, 
                        text="Taxable Tax2 rate", 
                        onvalue ='1' ,
                        offvalue = '0',
                        )

      if not taxchoose:
        pass
      elif taxchoose[0] == '1':
        Button4.place_forget()
        tax2exp.place_forget()
      elif taxchoose[0] == '2':
        Button4.place(x=400,y=125)
        tax2exp.place_forget()
      elif taxchoose[0] == '3':
        tax2exp.place(x=400,y=105)
        Button4.place(x=400,y=125)
  
      # Button4.bind("<Button-1>", getBool)
      
      ps = psdata[9]
      if ps == "1":
       Button4.select()
      else:
        Button4.deselect()
      
     
      if psdata[19] == "1":
        tax2exp.select()
      else:
        tax2exp.deselect()
          
      
 
  
      sql = "select businessname from Customer"
      fbcursor.execute(sql,)
      cusdta = fbcursor.fetchall()
      
  
      def toggle():
        if other.get():
          ent.place(x=45,y=180)
          try:
            user_namech = username1.get()
            sql = "select rebill_exprense from users where username = %s"
            val = (user_namech,)
            fbcursor.execute(sql,val)
            disable_rebillabe_exp = fbcursor.fetchone()
            if disable_rebillabe_exp[0] == 1:
              button51.place(x=250, y=160)
            else:
              id_skuentry.place_forget()
              rebill_entry.place_forget()
              button51.place_forget()
          except:
            button51.place(x=250, y=160)
        else:
          button51.deselect()
          ent.place_forget()
          button51.place_forget()
           
          ent.delete(0, END)
          id_skuentry.delete(0,END)
          rebill_entry.delete(0,END)
          id_skulabel.place_forget()
          id_skuentry.place_forget()
          rebill_label.place_forget()
          rebill_entry.place_forget()
      other = BooleanVar()
      button5 = Checkbutton(expenselabelframe, text="Assign to customer (optional)", variable=other, 
      command=toggle)
      button5.place(x=40, y=160)
      cus = StringVar()
      ent=ttk.Combobox(expenselabelframe,width=30,textvariable=cus)
      ent['values'] = cusdta
      ent.delete(0,'end')
      ent.insert(0, psdata[10])
      
      

      def toggle():
        if rebill.get():
          id_skuentry.delete(0,END)
          rebill_entry.delete(0,END)
          id_skulabel.place(x=375,y=160)
          id_skuentry.place(x=420,y=160)
          rebill_label.place(x=335,y=180)
          rebill_entry.place(x=420, y=180)
        else:
          id_skuentry.delete(0,END)
          rebill_entry.delete(0,END)
          id_skulabel.place_forget()
          id_skuentry.place_forget()
          rebill_label.place_forget()
          rebill_entry.place_forget()
      rebill = BooleanVar()
      button51 = Checkbutton(expenselabelframe, text="Rebillable" ,variable=rebill, command=toggle,onvalue=1,offvalue=0)

      
      # sql = "select * from users"
      # fbcursor.execute(sql)
      # rebill_check_user = fbcursor.fetchall()
      
      # if not rebill_check_user:
      #   pass
      # else:
      #   # try:
      #     user_namech = username1.get()
      #     sql = "select rebill_exprense from users where username = %s"
      #     val = (user_namech,)
      #     fbcursor.execute(sql,val)
      #     disable_rebillabe_exp = fbcursor.fetchone()
      #     if disable_rebillabe_exp[0] == 1:
      #       button51.place_forget()
      #     else:
      #       pass
      #   # except:
        #    pass
      
      cns = psdata[17]
      if cns == '1':
        button5.select()
        ent.place(x=45,y=180)
        button51.place(x=250, y=160)
      else:
        button5.deselect()
        try:
          user_namech = username1.get()
          sql = "select rebill_exprense from users where username = %s"
          val = (user_namech,)
          fbcursor.execute(sql,val)
          disable_rebillabe_exp = fbcursor.fetchone()
          if disable_rebillabe_exp[0] == 1:
            pass
          else:
            button51.place_forget()
        except:
          pass
        
      
      
      id_sku1 = StringVar()
      id_skulabel=Label(expenselabelframe,text="id_sku:")
      id_skuentry = Entry(expenselabelframe,width=15,textvariable=id_sku1)
      id_skuentry.delete(0,'end')
      id_skuentry.insert(0, psdata[15])
      
      def number_rebill_amoun(S,d):
        sql = "select decimalseperator from company"
        fbcursor.execute(sql)
        deci_sgin = fbcursor.fetchone()
        if deci_sgin[0] == '.':
          if d == '1': #insert
            if not S in ['.','0','1','2','3','4','5','6','7','8','9']:
              return False
            return True
        elif deci_sgin[0] == ',':
          if d == '1': #insert
            if not S in ['0','1','2','3','4','5','6','7','8','9',',']:
              return False
            return True
        if d.isdigit():
          return True
        
        
        
  
      def rebillamoonclick(event):
        sql = "select currencysign,currsignplace from company"
        fbcursor.execute(sql)
        currsymb = fbcursor.fetchone()
        if currsymb[1] == "before amount":
          rebill_entry.insert (0, currsymb[0])
          rebi_amo = (expenselabelframe.register(number_rebill_amoun),'%S','%d')
          rebill_entry.config(validate='key',validatecommand=(rebi_amo),justify='left')
        elif currsymb[1] == "before amount with space":
          rebill_entry.insert (0, currsymb[0] + " ")
          rebi_amo = (expenselabelframe.register(number_rebill_amoun),'%S','%d')
          rebill_entry.config(validate='key',validatecommand=(rebi_amo),justify='left')
        elif currsymb[1] == "after amount":
          rebill_amoun.set(currsymb[0])
          rebi_amo = (expenselabelframe.register(number_rebill_amoun),'%S','%d')
          rebill_entry.config(validate='key',validatecommand=(rebi_amo),justify='right')
        elif currsymb[1] == "after amount with space":
          rebill_amoun.set(" " + currsymb[0])
          rebi_amo = (expenselabelframe.register(number_rebill_amoun),'%S','%d')
          rebill_entry.config(validate='key',validatecommand=(rebi_amo),justify='right')
      rebill_amoun = StringVar()
      rebill_label=Label(expenselabelframe,text="Rebill amount:")
      rebill_entry = Entry(expenselabelframe,width=15,textvariable=rebill_amoun)
      rebill_entry.bind("<ButtonRelease>", rebillamoonclick)
      rebill_entry.delete(0,'end')
      rebill_entry.delete(0,'end')
      rebill_entry.insert(0, psdata[16])

      reb = psdata[13]
      print(ps)
      if reb == '1':
        button51.select()
        id_skulabel.place(x=375,y=160)
        id_skuentry.place(x=420,y=160)
        rebill_label.place(x=335,y=180)
        rebill_entry.place(x=420, y=180)
      else:
        button51.deselect()
  
  
      
      
      def toggle():
        if imge.get():
          browseimg.place(x=40,y=220)
          browsebutton.place(x=350,y=220,height=30,width=50)
          b2.place(x=450, y=240)

        else:
          browseimg.place_forget()
          browsebutton.place_forget()
          b2.place_forget()
        
      imge = BooleanVar()
      Button6 = Checkbutton(expenselabelframe, text = "Attach receipt image(optional,image will be stored   to the database)",command=toggle,variable=imge)
      Button6.place(x=40, y=200)
      browseimg=Label(expenselabelframe,text="(recommended image type:JPG,size 480x320 pixels) ",  bg='#f5f3f2')
      browsebutton=Button(expenselabelframe,text = 'Browse', command=upload_file1)
     
      try:
        image = Image.open("images/"+psdata[11])
        resize_image = image.resize((120, 120))
        recimage = ImageTk.PhotoImage(resize_image)
        b2 = Button(expenselabelframe,image=recimage, height=120, width=120,)
        b2.photo = recimage
        print(image)
      except:
        pass
      
      
      rec = psdata[18]
      print(rec)
      if rec == '1':
        Button6.select()
        browseimg.place(x=40,y=220)
        browsebutton.place(x=350,y=220,height=30,width=50)
        b2.place(x=450, y=240)
      else:
        Button6.deselect()

  
      exptext1=Label(expenselabelframe,text="Notes",pady=5,padx=10)
      exptext1.place(x=12,y=246)
      exptxt = scrolledtext.ScrolledText(expenselabelframe, undo=True,width=50,height=5)
      exptxt.place(x=22,y=280)
      exptxt.delete('1.0','end')
      exptxt.insert('1.0', psdata[12])

      expokButton = Button(window1, text ="Ok",image=tick,width=70,compound = LEFT,command=update_expenses)
      expokButton.place(x=280,y=415)
    except:
        try:
            window1.destroy()
        except: 
            pass
        messagebox.showerror('F-Billing Revolution', 'Select a record to edit.')
    

  
      
  def file_image(event):
    itemid = exp_tree.item(exp_tree.focus())["values"][0]
    sql = "select * from Expenses where expensesid = %s"
    val = (itemid, )
    fbcursor.execute(sql, val)
    psda = fbcursor.fetchone() 
    if psda[11] is None:
      pass
    else:
      edit_window = Toplevel()
      edit_window.title("Edit the value or cancel")
      edit_window.geometry("700x500")
      
        
        
      image = Image.open("images/"+psda[11])
      resize_image = image.resize((700, 500))
      eximage = ImageTk.PhotoImage(resize_image)
      b2 = Button(edit_window,image=eximage)
      b2.photo = eximage
      b2.pack()
  

######################## DELETE EXPENSE #######################################################################


  def delete_expense():
    # sql = "select * from users"
    # fbcursor.execute(sql)
    # addexp_check_user = fbcursor.fetchall()
    delmess = messagebox.askyesno("Delete Expense", "Are you sure to delete this Expense?")
    if delmess == True:
      itemid = exp_tree.item(exp_tree.focus())["values"][0]
      print(itemid)
      sql = 'DELETE FROM Expenses WHERE expensesid=%s'
      val = (itemid,)
      fbcursor.execute(sql, val)
      fbilldb.commit()
      #selrow = exp_tree.selection()[0]
      exp_tree.delete(exp_tree.selection()[0])
    else:
      pass
  
  def delete_expense_check():
    sql = "select * from users"
    fbcursor.execute(sql)
    delexp_check_user = fbcursor.fetchall()
    if not delexp_check_user:
      delete_expense()
    else:
      try:
        user_namech = username1.get()
        sql = "select delete_expense from users where username = %s"
        val = (user_namech,)
        fbcursor.execute(sql,val)
        disable_del_exp = fbcursor.fetchone()
        if disable_del_exp[0] == 1:
          delete_expense()
        else:
          messagebox.showerror("user","user does not have permission to perform this action")
      except:
        delete_expense()
  

######################## SEARCH EXPENSE ######################################################################
  def close_expenses():
    top.destroy()

  def search_exp():
    query = searchvar.get()
    selections = []
    for child in exp_tree.get_children():
        if query in exp_tree.item(child)['values']:
            print(exp_tree.item(child)['values'])
            selections.append(child)
    exp_tree.selection_set(selections)
  
  
  

  def search_expense():
    global top,searchvar
    top = Toplevel()  
    
    top.title("Find Text")
    
    
    top.geometry("520x200+390+250")
    findwhat1=Label(top,text="Find What:",pady=5,padx=10)
    findwhat1.place(x=5,y=20)
    searchvar = StringVar() 
    findwhat = ttk.Combobox(top, width = 50, textvariable = searchvar ) 
      
    # Adding combobox drop down list 
    
    findwhat.place(x=80,y=25) 
    

    findButton = Button(top, text ="Find next",width=10, command=search_exp)
    findButton.place(x=420,y=20)

    findin1=Label(top,text="Find in:",pady=5,padx=10)
    findin1.place(x=5,y=47)
    n = StringVar() 
    findIN = ttk.Combobox(top, width = 37, textvariable = n ) 
      
    # Adding combobox drop down list 
    findIN['values'] = ('Client',  
                              ' Date', 
                              ' Category', 
                              ' Vendor', 
                              ' Staff Member', 
                              ' Description', 
                              ' Rebillable',
                              'Invoiced',
                              'Image',
                              'Rebill Amount',
                              'Amount',
                        
                              ' <<All>>') 
      
    findIN.place(x=80,y=54) 
    findIN.current(0)

    closeButton = Button(top, text ="Close",width=10,command=close_expenses)
    closeButton.place(x=420,y=50)

    match1=Label(top,text="Match:",pady=5,padx=10)
    match1.place(x=5,y=74)
    n = StringVar() 
    match = ttk.Combobox(top, width = 27, textvariable = n ) 
      
    # Adding combobox drop down list 
    match['values'] = ('From Any part of the field',' Whole Field',  
                              ' From the beginning of the field')
      
    match.place(x=80,y=83) 
    match.current(0)

    search1=Label(top,text="Search:",pady=5,padx=10)
    search1.place(x=5,y=102)
    n = StringVar() 
    search = ttk.Combobox(top, width = 27, textvariable = n ) 
      
    # Adding combobox drop down list 
    search['values'] = ('All', 'up', 
                              ' Down')
      
    search.place(x=80,y=112) 
    search.current(0)


    checkvarStatus4=IntVar()
   
    Button4 = Checkbutton(top,variable = checkvarStatus4, 
                      text="Match Case", 
                      onvalue =1,
                      offvalue = 0,
                      height=3,
                      width = 15)

    Button4.place(x=60,y=141)

    checkvarStatus5=IntVar()
   
    Button5 = Checkbutton(top,variable = checkvarStatus5, 
                      text="Match Format", 
                      onvalue =0 ,
                      offvalue = 1,
                      height=3,
                      width = 15)

    Button5.place(x=270,y=141)







  

######################## FRONT PAGE OF EXPENSE MODULE #######################################################################

    
  expframe = Frame(tab6,relief=GROOVE,bg="#f8f8f2")
  expframe.pack(side="top", fill=BOTH)
  
  expmidFrame=Frame(expframe, height=60,bg="#f5f3f2")
  expmidFrame.pack(side="top", fill=X)

  e = Canvas(expmidFrame, width=1, height=65, bg="#f8f8f2", bd=0)
  e.pack(side="left", padx=(5, 2))
  e = Canvas(expmidFrame, width=1, height=65, bg="#f8f8f2", bd=0)
  e.pack(side="left", padx=(0, 5))
  
  
  expenseLabel = Button(expmidFrame,compound="top", text="Create new\nExpense",relief=RAISED,   command=add_expense_connection, image=expenseIcon,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
  expenseLabel.pack(side="left", pady=3, ipadx=4)
  
  
  expeditLabel = Button(expmidFrame,compound="top", text="Edit/View\nExpense",relief=RAISED,    image=expeditIcon,command=edit_expense,bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
  expeditLabel.pack(side="left")
  
  expdeleteLabel = Button(expmidFrame,compound="top", text="Delete\nSelected", relief=RAISED,    command=delete_expense_check,image=expdeleteIcon,bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
  expdeleteLabel.pack(side="left")
  
  e = Canvas(expmidFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  e.pack(side="left", padx=5)
 
  expsearchLabel = Button(expmidFrame,compound="top", text="Search in\nExpenses",relief=RAISED,   command=search_expense, image=expsearchIcon,bg="#f8f8f2", fg="black", height=55, bd=1, width=55, )
  expsearchLabel.pack(side="left")
  
  
  lbframe = LabelFrame(expmidFrame, height=60, width=200)
  lbframe.pack(side="left", padx=10, pady=0)

  lbl_expdt=Label(lbframe,text="Expense date from:",fg='black')
  lbl_expdt.grid(row=0, column=0, pady=5, padx=(5, 0))
  
  lbl_expdtt=Label(lbframe,text="Expense date to:" , fg='black')
  lbl_expdtt.grid(row=1, column=0, pady=5, padx=(5, 0))

  def daterange_expenses(): # Start and stop dates for range
    var1=expdt1.get_date()
    var2=expdtt2.get_date()
    print(var1,var2)
    for record in exp_tree.get_children():
      exp_tree.delete(record)
    
    
    sqldate='SELECT * FROM Expenses WHERE date BETWEEN %s AND %s'
    valuz=(var1,var2,)
    fbcursor.execute(sqldate,valuz)
    filterdate=fbcursor.fetchall()
    print(filterdate)
    count=0
    for i in filterdate:
      if True:
        if i[13] == '1':
          e = 'Yes'
        else:
          e = 'No'
        exp_tree.insert(parent='', index='end', iid=i, text='hello', values=(i[0], i[10], i[4], i[6], i[5], i [8], i[7], e , i[14], i[11],i[16],i[3]))
      else:
          pass
      count += 1

  
  expdt1=DateEntry(lbframe)
  expdt1.grid(row=0, column=1)
     
  expdtt2=DateEntry(lbframe)
  expdtt2.grid(row=1, column=1)

  sql = "select dateformat from company"
  fbcursor.execute(sql)
  date_for = fbcursor.fetchone()
  
  if not date_for:
    pass
  else:
    if date_for[0] == "mm-dd-yyyy":
      expdtt2._set_text(expdtt2._date.strftime('%m-%d-%Y'))
      expdt1._set_text(expdt1._date.strftime('%m-%d-%Y'))
    elif date_for[0] == "dd-mm-yyyy":
      expdt1._set_text(expdt1._date.strftime('%d-%m-%Y'))
      expdtt2._set_text(expdtt2._date.strftime('%d-%m-%Y'))
    elif date_for[0] == "yyy.mm.dd":
      expdt1._set_text(expdt1._date.strftime('%Y.%m.%d'))
      expdtt2._set_text(expdtt2._date.strftime('%Y.%m.%d'))
    elif date_for[0] == "mm/dd/yyyy":
      expdt1._set_text(expdt1._date.strftime('%m/%d/%Y'))
      expdtt2._set_text(expdtt2._date.strftime('%m/%d/%Y'))
    elif date_for[0] == "dd/mm/yyy":
      expdt1._set_text(expdt1._date.strftime('%d/%m/%Y'))
      expdtt2._set_text(expdtt2._date.strftime('%d/%m/%Y'))
    elif date_for[0] == "dd.mm.yyyy":
      expdt1._set_text(expdt1._date.strftime('%d.%m.%Y'))
      expdtt2._set_text(expdtt2._date.strftime('%d.%m.%Y'))
    elif date_for[0] == "yyyy/mm/dd":
      expdt1._set_text(expdt1._date.strftime('%Y/%m/%d'))
      expdtt2._set_text(expdtt2._date.strftime('%Y/%m/%d'))
    else:
      pass
     
  checkvar1 = IntVar()
  chkbtn1 = Checkbutton(lbframe, text = "Apply filter", variable = checkvar1, onvalue = 1, offvalue =0,     height = 2, width = 8,command=daterange_expenses)
  chkbtn1.grid(row=0, column=2, rowspan=2, padx=(5,5))
  
  exp_mainFrame=Frame(tab6, relief=GROOVE, bg="#f8f8f2")
  exp_mainFrame.pack(side="top", fill=BOTH)
  e = Canvas(exp_mainFrame, width=1, height=55, bg="#b3b3b3", bd=0)
  e.pack(side="left", padx=5)

  def refresh_expenses():
    for record in exp_tree.get_children():
      exp_tree.delete(record)
    count=0
    fbcursor.execute('SELECT * FROM Expenses;')
    for i in fbcursor:
      if True:
        if i[13] == '1':
          e = 'Yes'
        else:
          e = 'No'
        exp_tree.insert(parent='', index='end', iid=i, text='hello', values=(i[0], i[10], i[4], i[6], i[5], i[8], i[7], e , i[14], i[11],i[16],i[3]))
      else:
          pass
    count += 1
  

  
  exprefreshLabel = Button(expmidFrame,compound="top", text="Refresh\nExpense List",relief=RAISED,    image=exprefreshIcon,bg="#f8f8f2", fg="black", height=55, bd=1, width=63,command=refresh_expenses)
  exprefreshLabel.pack(side="left")


  
  invoi1label = Label(expframe, text="Expenses (All)", font=("arial", 18), bg="#f8f8f2")
  invoi1label.pack(side="left", padx=(20,0))

  def fil(event):
    filt = drop123.get()
    for record in exp_tree.get_children():
      exp_tree.delete(record)
  
  
  
  
    sql = "select * from Expenses where catagory = %s"
    val = (filt,)
    fbcursor.execute(sql, val)
    records = fbcursor.fetchall()
  
  
    count=0
    for i in records:
        if True:
          if i[13] == '1':
             e = 'Yes'
          else:
            e = 'No'
          exp_tree.insert(parent='', index='end', iid=i, text='hello', values=(i[0], i[10], i[4], i[6], i[5], i[8], i[7], e , i[14], i[11],i[16],i[3]))
        else:
          pass
    count += 1

  sql = "SELECT DISTINCT catagory FROM Expenses"
  fbcursor.execute(sql,)
  rec = fbcursor.fetchall()
  drop123 = ttk.Combobox(expframe,)
  drop123['values'] = rec
  drop123.pack(side="right", padx=(0,10))
  drop123.bind("<<ComboboxSelected>>", fil)


 
  invoi1label = Label(expframe, text="Category filter", font=("arial", 15), bg="#f8f8f2")
  invoi1label.pack(side="right", padx=(0,10))

# sql= 'SELECT rebillable FROM Expenses '
# fbcursor.execute(sql,)
# c = fbcursor.fetchall()
# print (c[2])
# print(c == 1)
# for e in c:
#   m = e == c
#   m = ("Yes")
#   e != c
#   print("no")
#   else:
#     pass



#table 
  s = ttk.Style()
  s.configure('Treeview.Heading', background='white', State='DISABLE')
  
  
  exp_tree=ttk.Treeview(tab6,selectmode='browse')
  exp_tree.place(x=0,y=105,height=580)
  
  expverticalbar=ttk.Scrollbar(tab6,orient="vertical",command=exp_tree.yview,)
  expverticalbar.place(x=1345,y=102,height=570,)
  expverticalbar.place(x=1345,y=102,height=570)
  exp_tree["columns"]=("1","2","3","4","5","6","7","8","9","10","11","12")
  exp_tree["show"]='headings'
  exp_tree.column("1",width=5,anchor='c')
  exp_tree.column("2",width=130,anchor='c')
  exp_tree.column("3",width=110,anchor='c')
  exp_tree.column("4",width=120,anchor='c')
  exp_tree.column("5",width=120,anchor='c')
  exp_tree.column("6",width=120,anchor='c')
  exp_tree.column("7",width=220,anchor='c')
  exp_tree.column("8",width=120,anchor='c')
  exp_tree.column("9",width=100,anchor='c')
  exp_tree.column("10",width=100,anchor='c')
  exp_tree.column("11",width=100,anchor='c')
  exp_tree.column("12",width=100,anchor='c')
  exp_tree.heading("2",text="Client")
  exp_tree.heading("3",text="Date")
  exp_tree.heading("4",text="Category")
  exp_tree.heading("5",text="Vendor")
  exp_tree.heading("6",text="Staff member")
  exp_tree.heading("7",text="Description")
  exp_tree.heading("8",text="Rebillable")
  exp_tree.heading("9",text="Invoiced")
  exp_tree.heading("10",text="Image")
  exp_tree.heading("11",text="Rebill Amount")
  exp_tree.heading("12",text="Amount")
  exp_tree.bind('<Double-Button-1>',file_image)





  fbcursor.execute('SELECT * FROM Expenses;')

  j = 0
  
  for i in fbcursor:
    if i[13] == '1':
      e = 'Yes'
    else:
      e = 'No'
    exp_tree.insert(parent='', index='end', iid=i, text='hello', values=(i[0], i[10], i[4], i[6], i[5], i[8], i[7], e , i[14], i[11],i[16],i[3]))
    j += 1

############################ END OF Expense Module-############################
############################ ADD PRODUCT SERVICES  ############################
  def add_product_s_connection():
    sql = "select * from users"
    fbcursor.execute(sql)
    addexp_check_user = fbcursor.fetchall()
    if not addexp_check_user:
      adda_product()
    else:
      try:
        user_namech = username1.get()
        sql = "select create_product_service from users where username = %s"
        val = (user_namech,)
        fbcursor.execute(sql,val)
        disable_create_exp = fbcursor.fetchone()
        if disable_create_exp[0] == 1:
          adda_product()
        else:
          messagebox.showerror("user","user does not have permission to perform this action")
      except:
        adda_product()

  def adda_product():
    top = Toplevel()  
    
    top.title("Add a new Product/Service")
    p2 = PhotoImage(file = 'images/fbicon.png')
    top.iconphoto(False, p1)
    top.geometry("600x550+390+125")
    
    
    tabControl = ttk.Notebook(top)
    s = ttk.Style()
    s.theme_use('default')
    s.configure('TNotebook.Tab', background="#999999", width=50, padding=10,bd=0)


    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    
    tabControl.add(tab1,compound = LEFT, text ='Product/Service')
    tabControl.add(tab2,compound = LEFT, text ='Product Image')
    
    tabControl.pack(expand = 1, fill ="both")
    
    innerFrame = Frame(tab1,bg="#f5f3f2", relief=GROOVE, height=490)
    innerFrame.pack(side="top",fill=BOTH)

    Customerlabelframe = LabelFrame(innerFrame,text="Product/Service",width=580,height=475)
    Customerlabelframe.pack(side="top",fill=BOTH,padx=10)
    
    global filename
    filename = ""
    
    def upload_file():
      global filename,img, b2
      f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
      filename = filedialog.askopenfilename(filetypes=f_types)
      shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
      image = Image.open(filename)
      resize_image = image.resize((350, 350))
      img = ImageTk.PhotoImage(resize_image)
      b2 = Button(imageFrame,image=img)
      b2.place(x=130, y=80)
    
    def addproducts():
      global img , filename 
      sku = codeentry.get()
      status = checkvarStatus.get()
      catgory = n.get()
      name = nameentry.get()
      description = desentry.get()
      unitprice = uval.get()
      peices = pcsentry.get()
      cost = costval.get()
      price_cost = priceval.get()
      taxable = checkvarStatus2.get()
      tax2 = checkvarStatustax2.get()
      nostockcontrol = checkvarStatus3.get()
      stock = stockentry.get()
      lowstock = lowentry.get()
      warehouse = wareentry.get()
      pnotes = sctxt.get("1.0",'end-1c')
      entries = [sku,name, unitprice, cost]
      entri = []
      for i in entries:
        if i == '':
          entri.append(i)
      if len(entri) == 0:
        sql = 'select * from Productservice where sku = %s or name = %s'
        val  = (sku, name)
        fbcursor.execute(sql, val)
        fbcursor.fetchall()
        row_count = fbcursor.rowcount
        if row_count == 0:
          if filename == "":
            sql = 'insert into Productservice(sku, category, name, description, status, unitprice, peices, cost, taxable, priceminuscost, serviceornot, stock, stocklimit, warehouse, privatenote,tax2) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)'
            val = (sku, catgory, name, description, status, unitprice, peices, cost, taxable, price_cost, nostockcontrol, stock, lowstock, warehouse, pnotes,tax2)
            fbcursor.execute(sql, val)
            fbilldb.commit()
          else:
            file = shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
            sql = 'insert into Productservice(sku, category, name, description, status, unitprice, peices, cost, taxable, priceminuscost, serviceornot, stock, stocklimit, warehouse, image, privatenote,tax2) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)'
            val = (sku, catgory, name, description, status, unitprice, peices, cost, taxable, price_cost, nostockcontrol, stock, lowstock, warehouse, filename.split('/')[-1], pnotes,tax2)
            fbcursor.execute(sql, val)
            fbilldb.commit()
        else:
          messagebox.showinfo("Alert", "Entry with same name or SKU already exists.\nTry again.")
          top.destroy()
        for record in treeproducts.get_children():
          treeproducts.delete(record)
        fbcursor.execute("select *  from Productservice")
        pandsdata = fbcursor.fetchall()
        countp = 0
        for i in pandsdata:
          if i[6] == '1':
            acti = 'Active'
          else:
            acti = 'Inactive' 
          sql = "select currencysign,currsignplace from company"
          fbcursor.execute(sql)
          currsymb = fbcursor.fetchone()
          if not currsymb: 
            if i[13] > i[14]:
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('green',))
              countp += 1              
            elif i[12] == '1':
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('blue',))
              countp += 1
            else:
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('red',))
              countp += 1
              
          elif currsymb[1] == "before amount":
            if (i[13]) > (i[14]):
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('green',))
              countp += 1
            elif i[12] == '1':
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('blue',))
              countp += 1
            else:
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('red',))
              countp += 1
          elif currsymb[1] == "before amount with space":
            if i[13] > i[14]:
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('green',))
              countp += 1
            elif i[12] == '1':
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('blue',))
              countp += 1
            else:
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('red',))
              countp += 1
          elif currsymb[1] == "after amount":
            if i[13] > i[14]:
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('green',))
              countp += 1
            elif i[12] == '1':
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
              countp += 1
            else:
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('red',))
              countp += 1
          elif currsymb[1] == "after amount with space":
            if i[13] > i[14]:
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('green',))
              countp += 1
            elif i[12] == '1':
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
              countp += 1
            else:
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('red',))
              countp += 1
        top.destroy()
      else:
        messagebox.showinfo("Alert", "Fields name and SKU should not be empty.\nFill out required fields and try again")
        
 
    fbcursor.execute("SELECT * FROM Productservice ORDER BY sku DESC LIMIT 1")
    skuin = fbcursor.fetchone()
    
    
    code1=Label(Customerlabelframe,text="Code or SKU* :",fg="blue",pady=10,padx=10)
    code1.place(x=20,y=0)
    codeentry = Entry(Customerlabelframe,width=35)
    codeentry.place(x=110,y=8)
    # if not skuin == None:
    #   fk=skuin[2]+1
    # else:
    #   fk=1
    # codeentry.insert(0, fk)

    checkvarStatus=IntVar()
    status1=Label(Customerlabelframe,text="Status:")
    status1.place(x=380,y=8)
    Button1 = Checkbutton(Customerlabelframe, 
                      variable = checkvarStatus,text="Active",compound="right",
                      onvalue =1,
                      offvalue = 0,
                      width = 10)

    Button1.place(x=420,y=5)

    category1=Label(Customerlabelframe,text="Category:",pady=5,padx=10)
    category1.place(x=20,y=40)
    n = StringVar() 
    catgory = ttk.Combobox(Customerlabelframe, width = 40, textvariable = n ) 
    catgory.place(x=110,y=45)
    catgory.insert(0, 'Default')


    name1=Label(Customerlabelframe,text="Name* :",fg="blue",pady=5,padx=10)
    name1.place(x=20,y=70)
    nameentry = Entry(Customerlabelframe,width=70)
    nameentry.place(x=110,y=75)

    des1=Label(Customerlabelframe,text="Description :",pady=5,padx=10)
    des1.place(x=20,y=100)
    desentry = Entry(Customerlabelframe,width=70)
    desentry.place(x=110,y=105)

    def prdoucts_cal(S,d):
        if d == '1': #insert
          if not S in ['.','0','1','2','3','4','5','6','7','8','9']:
            return False
          return True
        if d.isdigit():
          return True

    uval = StringVar()
    unit1=Label(Customerlabelframe,text="Unit Price:",fg="blue",pady=5,padx=10)
    unit1.place(x=20,y=130)
    unitentry = Entry(Customerlabelframe,width=20,textvariable=uval)
    unitentry.place(x=110,y=135)
    cal_unit = (Customerlabelframe.register(prdoucts_cal),'%S','%d')
    unitentry.config(validate='key',validatecommand=(cal_unit),justify='right')
    

    # pcsval = IntVar()
    pcs1=Label(Customerlabelframe,text="Pcs/Weight:",fg="blue",pady=5,padx=10)
    pcs1.place(x=320,y=130)
    pcsentry = Entry(Customerlabelframe,width=20)
    pcsentry.place(x=410,y=135)

    costval = StringVar(value="0")
    cost1=Label(Customerlabelframe,text="Cost:",pady=5,padx=10)
    cost1.place(x=20,y=160)
    
    costentry = Entry(Customerlabelframe,width=20,textvariable=costval)
    costentry.place(x=110,y=165)
    cal_cost = (Customerlabelframe.register(prdoucts_cal),'%S','%d')
    costentry.config(validate='key',validatecommand=(cal_cost),justify='right')
    
    def set_label(name, index, mode):
      copr = float(uval.get()) - float(costval.get())
      priceval.set(str(copr))
      
    priceval = StringVar()
    price1=Label(Customerlabelframe,text="(Price-Cost):",pady=5,padx=10)
    price1.place(x=20,y=190)
    priceentry = Entry(Customerlabelframe,width=20,textvariable=priceval,state=DISABLED,disabledbackground="white",disabledforeground="black")
    priceentry.config(justify="right")
    priceentry.place(x=110,y=195)
    
    uval.trace('w', set_label)
    costval.trace('w', set_label)

    sql = "select taxtype from company"
    fbcursor.execute(sql)
    taxchoose = fbcursor.fetchone()

    checkvarStatus2=IntVar()
   
    Button2 = Checkbutton(Customerlabelframe,variable = checkvarStatus2, 
                      text="Taxable Tax1rate",compound="right",
                      onvalue =1 ,
                      offvalue = 0,
                      height=2,
                      width = 12)
    
    checkvarStatustax2=IntVar()
    Buttontax2 = Checkbutton(Customerlabelframe,variable = checkvarStatustax2, 
                      text="Taxable Tax2rate",compound="right",
                      onvalue =1 ,
                      offvalue = 0,
                      height=2,
                      width = 12)
    
    
    if not taxchoose:
      pass
    elif taxchoose[0] == '1':
      Button2.place_forget()
      Buttontax2.place_forget()
    elif taxchoose[0] == '2':
      Button2.place(x=415,y=153)
      Buttontax2.place_forget()
    elif taxchoose[0] == '3':
      Button2.place(x=415,y=153)
      Buttontax2.place(x=415,y=203)

    

    def switch():
      if checkvarStatus3.get():
        stockentry["state"] = DISABLED
        lowentry["state"] = DISABLED
        wareentry["state"] = DISABLED
      else:
        stockentry["state"] = NORMAL
        lowentry["state"] = NORMAL
        wareentry["state"] = NORMAL
    checkvarStatus3=BooleanVar()
    Button3 = Checkbutton(Customerlabelframe,variable = checkvarStatus3,command=switch, 
                      text="This is a service(no stock control)", 
                      onvalue =1 ,
                      offvalue = 0,
                      height=3)

    Button3.place(x=40,y=220)
 
    def stocknum(input):
      if input.isdigit():
        return True
      elif input is "":
        return True
      else:
        return False
    stock1=Label(Customerlabelframe,text="Stock:",pady=5,padx=10)
    stock1.place(x=90,y=260)
    stockentry = Entry(Customerlabelframe,width=15)
    stockentry.place(x=140,y=265)
    sto = Customerlabelframe.register(stocknum)
    stockentry.config(validate="key",validatecommand=(sto, '%S'))


    low1=Label(Customerlabelframe,text="Low Stock Warning Limit:",pady=5,padx=10)
    low1.place(x=280,y=260)
    lowentry = Entry(Customerlabelframe,width=15)
    lowentry.place(x=435,y=265)
    lowsto = Customerlabelframe.register(stocknum)
    lowentry.config(validate="key",validatecommand=(lowsto, '%S'))

   
    ware1=Label(Customerlabelframe,text="Warehouse:",pady=5,padx=10)
    ware1.place(x=60,y=290)
    wareentry = Entry(Customerlabelframe,width=64)
    wareentry.place(x=140,y=295)

    # pnoteval = StringVar()
    text1=Label(Customerlabelframe,text="Private notes(not appears on invoice):",pady=5,padx=10)
    text1.place(x=20,y=320)
    sctxt = scrolledtext.ScrolledText(Customerlabelframe, undo=True,width=62,height=4)
    sctxt.place(x=32,y=358)
    
    okButton = Button(innerFrame, text ="Ok",image=tick,width=70,compound = LEFT, command=addproducts)
    okButton.pack(side=LEFT, padx=(10, 0), pady=(5, 10))
    
    def closetab():
      top.destroy()

    cancelButton = Button(innerFrame,image=cancel,text="Cancel",width=70,compound = LEFT, command=closetab)
    cancelButton.pack(side=RIGHT, padx=(0, 10), pady=(5, 10))

    imageFrame = Frame(tab2, relief=GROOVE,height=580)
    imageFrame.pack(side="top",fill=BOTH)

    
      
    browseimg=Label(imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
    browseimg.place(x=30,y=35)
      
    browsebutton=Button(imageFrame,text = 'Browse',command=upload_file)
    browsebutton.place(x=485,y=30,height=30,width=50)

    removeButton = Button(imageFrame,image=cancel,text="Remove Product Image",width=150,compound = LEFT, command=lambda: b2.destroy())
    removeButton.place(x=410,y=460)

    top.mainloop()
  ##################### import product service ####################
  def import_productservice_check():
    sql = "select * from users"
    fbcursor.execute(sql)
    delexp_check_user = fbcursor.fetchall()
    if not delexp_check_user:
      fileimport_product()
    else:
      try:
        user_namech = username1.get()
        sql = "select 	import_product_service from users where username = %s"
        val = (user_namech,)
        fbcursor.execute(sql,val)
        disable_del_exp = fbcursor.fetchone()
        if disable_del_exp[0] == 1:
          fileimport_product()
        else:
          messagebox.showerror("user","user does not have permission to perform this action")
      except:
        fileimport_product()

  def fileimport_product():

    top=Toplevel()
    top.title("Import items list from Excel(XLS)File")
    top.geometry("785x520+280+100")
    importframe=Frame(top)
    importframe.place(x=0,y=0,height=700,width=785)
    impolbl=Label(importframe,text="Import source Excel(xlsx) File:").place(x=8,y=30)
    impoentry=Entry(importframe,bg="white")
    impoentry.place(x=8,y=50,width=280, height=25)
    previewlbl=Label(importframe,text="Source File preview").place(x=8,y=77)
   
    ###### LISTBOX #####################
    scrollbarx = Scrollbar(importframe, orient=HORIZONTAL)
    scrollbary = Scrollbar(importframe, orient=VERTICAL)
    imptree = ttk.Treeview(importframe, columns=("PRODUCT SERVICE ID","CODE OR SKU","NAME","CATEGORY","DESCRIPTION","QTY UNIT","COST","PRICE","TAX1","TAX2","STOCK","LOW STOCK","LOCATION","ACTIVE","SERVICE"), height=400,     selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=imptree.yview)
    scrollbary.place(x=754,y=100,height=325)
    scrollbarx.config(command=imptree.xview)
    scrollbarx.place(x=0,y=410, width=356)
    imptree.heading('PRODUCT SERVICE ID', text="PRODUCT SERVICE ID", anchor=W)
    imptree.heading('CODE OR SKU', text="CODE OR SKU", anchor=W)
    imptree.heading('NAME', text="NAME", anchor=W)
    imptree.heading('CATEGORY', text="CATEGORY", anchor=W)
    imptree.heading('NAME', text="NAME", anchor=W)
    imptree.heading('DESCRIPTION', text="DESCRIPTION", anchor=W)
    imptree.heading('QTY UNIT', text="QTY UNIT", anchor=W)
    imptree.heading('COST', text="COST", anchor=W)
    imptree.heading('PRICE', text="PRICE", anchor=W)
    imptree.heading('TAX1', text="TAX1", anchor=W)
    imptree.heading('TAX2', text="TAX2", anchor=W)
    imptree.heading('STOCK', text="STOCK", anchor=W)
    imptree.heading('LOW STOCK', text="LOW STOCK", anchor=W)
    imptree.heading('LOCATION', text="LOCATION", anchor=W)
    imptree.heading('ACTIVE', text="ACTIVE", anchor=W)
    imptree.heading('SERVICE', text="SERVICE", anchor=W)
    

    imptree.column('#0', stretch=NO, minwidth=0, width=0)
    imptree.column('#1', stretch=NO, minwidth=0, width=120)
    imptree.column('#2', stretch=NO, minwidth=0, width=100)
    imptree.column('#3', stretch=NO, minwidth=0, width=100)
    imptree.column('#4', stretch=NO, minwidth=0, width=100)
    imptree.column('#5', stretch=NO, minwidth=0, width=100)
    imptree.column('#6', stretch=NO, minwidth=0, width=100)
    imptree.column('#7', stretch=NO, minwidth=0, width=100)
    imptree.column('#8', stretch=NO, minwidth=0, width=100)
    imptree.column('#9', stretch=NO, minwidth=0, width=100)
    imptree.column('#10', stretch=NO, minwidth=0, width=100)
    imptree.column('#11', stretch=NO, minwidth=0, width=100)
    imptree.column('#12', stretch=NO, minwidth=0, width=100)
    imptree.column('#13', stretch=NO, minwidth=0, width=100)
    imptree.column('#14', stretch=NO, minwidth=0, width=100)

 

    imptree.place(x=5,y=100,height=315,width=750)
    
    
    lb1=Label(importframe,text="Select import source XLs file first after build column associations").place(x=8,y=480)

    def export_product_1():
      global Productserviceid,name12,category12,description,peices,cost12,priceminuscost,taxable,stock12,stocklimit,warehouse,status,serviceornot,name
      name = askopenfilename(filetypes=[('CSV', '*.csv',), ('Excel', ('*.xls', '*.xslm', '*.xlsx'))])
      # df = pd.read_csv(name)
      # for i in df:
      #   listbox.insert(END, df)
      with open(name) as f:
        reader = csv.DictReader(f, delimiter=',')
        print(reader)
        for row in reader:
          # "PRODUCT SERVICE ID","NAME","CATEGORY","DESCRIPTION","QTY UNIT","COST","PRICE","TAX1","STOCK","LOW STOCK","LOCATION","ACTIVE","SERVICE"
          Productserviceid = row['PRODUCT SERVICE ID']
          sku = row['CODE OR SKU']          
          name12 = row['NAME']
          category12 = row['CATEGORY']
          
          description = row['DESCRIPTION']
          peices = row['QTY UNIT']
          cost12 = row['COST']
          priceminuscost = row['PRICE']
          taxable = row['TAX1']
          tax2 = row['TAX2']
          stock12 = row['STOCK']
          stocklimit = row['LOW STOCK']
          warehouse = row['LOCATION']
          status = row['ACTIVE']
          serviceornot = row['SERVICE']
        
          imptree.insert("", 0, values=(Productserviceid,sku,name12,category12,description,peices,cost12,priceminuscost,taxable,tax2,stock12,stocklimit,warehouse,status,serviceornot))

      impoentry.delete(0, 'end')
      impoentry.insert(0, name)
      
    def nxtscreen():
      def save_pro_import():
        with open(name) as f:
          reader = csv.DictReader(f, delimiter=',')
          for row in reader:
            Productserviceid = int(row['PRODUCT SERVICE ID'])
            sku = int(row['CODE OR SKU'])  
            name12 = row['NAME']
            category12 = row['CATEGORY']
            description = row['DESCRIPTION']
            peices = int(row['QTY UNIT'])
            cost12 = int(row['COST'])
            unitprice = int(row['PRICE'])
            taxable = int(row['TAX1'])
            tax2 = row['TAX2']
            stock12 = int(row['STOCK'])
            stocklimit = int(row['LOW STOCK'])
            warehouse = row['LOCATION']
            status = int(row['ACTIVE'])
            serviceornot = int(row['SERVICE'])
            min = int(unitprice) - int(cost12)

            sql = 'select * from Productservice where Productserviceid = %s or name = %s or sku=%s'
            val  = (Productserviceid, name12,sku)
            fbcursor.execute(sql, val)
            fbcursor.fetchall()
            row_count = fbcursor.rowcount
            if row_count == 0:
              sql = 'insert into Productservice(Productserviceid,sku,name,category,description,peices,cost,unitprice,taxable,tax2,stock,stocklimit,warehouse,status,serviceornot,priceminuscost) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s)'
              val = (Productserviceid,sku,name12,category12,description,peices,cost12,unitprice,taxable,tax2,stock12,stocklimit,warehouse,status,serviceornot,min)
              fbcursor.execute(sql, val)
              fbilldb.commit()
              topp.destroy()
              for record in treeproducts.get_children():
                treeproducts.delete(record)
              fbcursor.execute("select *  from Productservice")
              pandsdata = fbcursor.fetchall()
              countp = 0
              for i in pandsdata:
                if i[6] == '1':
                  acti = 'Active'
                else:
                  acti = 'Inactive' 
                sql = "select currencysign,currsignplace from company"
                fbcursor.execute(sql)
                currsymb = fbcursor.fetchone()
                if not currsymb: 
                  if i[13] > i[14]:
                    treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('green',))
                    countp += 1              
                  elif i[12] == '1':
                    treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('blue',))
                    countp += 1
                  else:
                    treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('red',))
                    countp += 1
                        
                elif currsymb[1] == "before amount":
                  if (i[13]) > (i[14]):
                    treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('green',))
                    countp += 1
                  elif i[12] == '1':
                    treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('blue',))
                    countp += 1
                  else:
                    treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('red',))
                    countp += 1
                elif currsymb[1] == "before amount with space":
                  if i[13] > i[14]:
                    treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('green',))
                    countp += 1
                  elif i[12] == '1':
                    treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('blue',))
                    countp += 1
                  else:
                    treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('red',))
                    countp += 1
                elif currsymb[1] == "after amount":
                  if i[13] > i[14]:
                    treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('green',))
                    countp += 1
                  elif i[12] == '1':
                    treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
                    countp += 1
                  else:
                    treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('red',))
                    countp += 1
                elif currsymb[1] == "after amount with space":
                    if i[13] > i[14]:
                      treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('green',))
                      countp += 1
                    elif i[12] == '1':
                      treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
                      countp += 1
                    else:
                      treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('red',))
                      countp += 1
              topp.destroy()
            else:
              messagebox.showinfo("Alert", "Entry with same name or SKU already exists.\nTry again.")
            
     
      topp=Toplevel()
      topp.title("Import items list from Excel(XLS)File")
      topp.geometry("785x520+280+100")
      scrollbarx = Scrollbar(topp, orient=HORIZONTAL)
      scrollbary = Scrollbar(topp, orient=VERTICAL)
      nxttree = ttk.Treeview(topp, columns=("PRODUCT SERVICE ID","CODE OR SKU","NAME","CATEGORY","DESCRIPTION","QTY UNIT","COST","PRICE","TAX1","TAX2","STOCK","LOW STOCK","LOCATION","ACTIVE","SERVICE"),height=400,     selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
      scrollbary.config(command=nxttree.yview)
      scrollbary.place(x=768,y=0,height=490)
      scrollbarx.config(command=nxttree.xview)
      scrollbarx.place(x=0,y=470,width=763)
      nxttree.heading('CODE OR SKU', text="CODE OR SKU", anchor=W)
      nxttree.heading('PRODUCT SERVICE ID', text="PRODUCT SERVICE ID", anchor=W)
      nxttree.heading('NAME', text="NAME", anchor=W)
      nxttree.heading('CATEGORY', text="CATEGORY", anchor=W)
      nxttree.heading('NAME', text="NAME", anchor=W)
      nxttree.heading('DESCRIPTION', text="DESCRIPTION", anchor=W)
      nxttree.heading('QTY UNIT', text="QTY UNIT", anchor=W)
      nxttree.heading('COST', text="COST", anchor=W)
      nxttree.heading('PRICE', text="PRICE", anchor=W)
      nxttree.heading('TAX1', text="TAX1", anchor=W)
      nxttree.heading('TAX2', text="TAX2", anchor=W)
      nxttree.heading('STOCK', text="STOCK", anchor=W)
      nxttree.heading('LOW STOCK', text="LOW STOCK", anchor=W)
      nxttree.heading('LOCATION', text="LOCATION", anchor=W)
      nxttree.heading('ACTIVE', text="ACTIVE", anchor=W)
      nxttree.heading('SERVICE', text="SERVICE", anchor=W)
  
      nxttree.column('#0', stretch=NO, minwidth=0, width=0)
      nxttree.column('#1', stretch=NO, minwidth=0, width=120)
      nxttree.column('#2', stretch=NO, minwidth=0, width=100)
      nxttree.column('#3', stretch=NO, minwidth=0, width=100)
      nxttree.column('#4', stretch=NO, minwidth=0, width=100)
      nxttree.column('#5', stretch=NO, minwidth=0, width=100)
      nxttree.column('#6', stretch=NO, minwidth=0, width=100)
      nxttree.column('#7', stretch=NO, minwidth=0, width=100)
      nxttree.column('#8', stretch=NO, minwidth=0, width=100)
      nxttree.column('#9', stretch=NO, minwidth=0, width=100)
      nxttree.column('#10', stretch=NO, minwidth=0, width=100)
      nxttree.column('#11', stretch=NO, minwidth=0, width=100)
      nxttree.column('#12', stretch=NO, minwidth=0, width=100)
      nxttree.column('#13', stretch=NO, minwidth=0, width=100)
      nxttree.column('#14', stretch=NO, minwidth=0, width=100)
    
      with open(name) as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
          # "PRODUCT SERVICE ID","NAME","CATEGORY","DESCRIPTION","QTY UNIT","COST","PRICE","TAX1","STOCK","LOW STOCK","LOCATION","ACTIVE","SERVICE"
          Productserviceid = row['PRODUCT SERVICE ID']
          sku = row['CODE OR SKU']
          name12 = row['NAME']
          category12 = row['CATEGORY']
          
          description = row['DESCRIPTION']
          peices = row['QTY UNIT']
          cost12 = row['COST']
          priceminuscost = row['PRICE']
          taxable = row['TAX1']
          tax2 = row['TAX2']
          stock12 = row['STOCK']
          stocklimit = row['LOW STOCK']
          warehouse = row['LOCATION']
          status = row['ACTIVE']
          serviceornot = row['SERVICE']
      

      
          nxttree.insert("", 0, values=(Productserviceid,sku,name12,category12,description,peices,cost12,  priceminuscost,taxable,tax2,stock12,stocklimit,warehouse,status,serviceornot))
       
    
      nxttree.place(x=0,y=0,height=470,width=770)
      back = Button(topp,text="back",command=lambda:topp.destroy())
      back.place(x=5,y=492)
      Finish = Button(topp,text="Finish",command=save_pro_import)
      Finish.place(x=740,y=492)
     
    
    importbutton=Button(top,command=export_product_1,text = 'Browse',compound=LEFT)
    importbutton.place(x=290,y=48,height=25,width=80)

    
    n = Button(importframe, text ="Next",command=nxtscreen).place(x=710,y=470)
  
    
    top.mainloop()
    
#########EXPORT PRODUCT#######################################################################################

  def export_product():
    cols = ["PRODUCT SERVICE ID","CODE OR SKU","NAME","CATEGORY","DESCRIPTION","QTY UNIT","COST","PRICE","TAX1","TAX2","STOCK","LOW STOCK","LOCATION","ACTIVE","SERVICE"] # Your column headings here
    path = filedialog.asksaveasfilename(initialdir=os.getcwd,title="Save File",filetypes=[('CSV File', '*.csv',)],defaultextension=".csv")
    
    lst = []
    with open(path, "w", newline='') as myfile:
        csvwriter = csv.writer(myfile, delimiter=',')
        sql = 'select Productserviceid,sku,name,category,description,peices,cost,unitprice,taxable,tax2,stock,stocklimit,warehouse,status,serviceornot from Productservice'
        fbcursor.execute(sql)
        pandsdata = fbcursor.fetchall()
        for row_id in pandsdata:
            row = row_id
            lst.append(row)
        lst = list(map(list,lst))
        lst.insert(0,cols)
        for row in lst:
            csvwriter.writerow(row)

    


######################## VIEW/EDIT PRODUCT #######################################################################

  
  def edit_product():  
    try:
      itemid = treeproducts.item(treeproducts.focus())["values"][1]
      
      global filename
      filename = ""
      
      def upload_file():
        global filename,img, b2
        f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
        filename = filedialog.askopenfilename(filetypes=f_types)
        shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
        image = Image.open(filename)
        resize_image = image.resize((350, 350))
        img = ImageTk.PhotoImage(resize_image)
        b2 = Button(imageFrame,image=img)
        b2.place(x=130, y=80)
      
      def updateproducts():
        global img , filename 
        sku = codeentry.get()
        status = checkvarStatus.get()
        catgory = n.get()
        name = nameentry.get()
        description = desentry.get()
        unitprice = uval.get()
        peices = pcsentry.get()
        cost = costval.get()
        price_cost = priceval.get()
        taxable = checkvarStatus2.get()
        tax2 = checkvarStatustax2.get()
        nostockcontrol = checkvarStatus3.get()
        stock = stockval.get()
        lowstock = lowval.get()
        warehouse = wareentry.get()
        pnotes = sctxt.get("1.0", 'end-1c')
        entries = [sku, name, unitprice, cost]
        entri = []
        for i in entries:
          if i == '':
            entri.append(i)
        if len(entri) == 0:
          if filename == "":
            sql = "update Productservice set sku=%s, category=%s, name=%s, description=%s, status=%s, unitprice=%s, peices=%s, cost=%s, taxable=%s, priceminuscost=%s, serviceornot=%s, stock=%s, stocklimit=%s, warehouse=%s, privatenote=%s,tax2=%s where Productserviceid = %s"
            val = (sku, catgory, name, description, status, unitprice, peices, cost, taxable, price_cost, nostockcontrol, stock, lowstock, warehouse, pnotes,tax2, itemid)
            fbcursor.execute(sql, val)
            fbilldb.commit()
          else:
            file = shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
            sql = "update Productservice set category=%s, name=%s, description=%s, status=%s, unitprice=%s, peices=%s, cost=%s, taxable=%s, priceminuscost=%s, serviceornot=%s, stock=%s, stocklimit=%s, warehouse=%s, image=%s, privatenote=%s,tax2=%s where Productserviceid = %s"
            val = (catgory, name, description, status, unitprice, peices, cost, taxable, price_cost, nostockcontrol, stock, lowstock, warehouse,filename.split('/')[-1], pnotes,tax2, itemid)
            fbcursor.execute(sql, val)
            fbilldb.commit()
            
          for record in treeproducts.get_children():
            treeproducts.delete(record)
          fbcursor.execute("select *  from Productservice")
          pandsdata = fbcursor.fetchall()
          countp = 0
          for i in pandsdata:
            if i[6] == '1':
              acti = 'Active'
            else:
              acti = 'Inactive' 
            sql = "select currencysign,currsignplace from company"
            fbcursor.execute(sql)
            currsymb = fbcursor.fetchone()
            if not currsymb: 
              if i[13] > i[14]:
                treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('green',))
                countp += 1              
              elif i[12] == '1':
                treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('blue',))
                countp += 1
              else:
                treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('red',))
                countp += 1
                      
            elif currsymb[1] == "before amount":
              if (i[13]) > (i[14]):
                treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('green',))
                countp += 1
              elif i[12] == '1':
                treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('blue',))
                countp += 1
              else:
                treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('red',))
                countp += 1
            elif currsymb[1] == "before amount with space":
              if i[13] > i[14]:
                treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('green',))
                countp += 1
              elif i[12] == '1':
                treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('blue',))
                countp += 1
              else:
                treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('red',))
                countp += 1
            elif currsymb[1] == "after amount":
              if i[13] > i[14]:
                treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('green',))
                countp += 1
              elif i[12] == '1':
                treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
                countp += 1
              else:
                treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('red',))
                countp += 1
            elif currsymb[1] == "after amount with space":
                if i[13] > i[14]:
                  treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('green',))
                  countp += 1
                elif i[12] == '1':
                  treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
                  countp += 1
                else:
                  treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('red',))
                  countp += 1
          top.destroy()
        else:
          messagebox.showinfo("F-Billing Revolution", "Fields name or SKU entered is already in database.")
          top.destroy()
        
         
      sql = "select * from Productservice where Productserviceid = %s"
      val = (itemid, )
      fbcursor.execute(sql, val)
      psdata = fbcursor.fetchone()
      
      
      top = Toplevel()  
      top.title("Edit Product/Service details")
      p3 = PhotoImage(file = 'images/fbicon.png')
      top.iconphoto(False, p1)
      top.geometry("600x550+390+125")
      tabControl = ttk.Notebook(top)
      s = ttk.Style()
      s.theme_use('default')
      s.configure('TNotebook.Tab', background="#999999", width=50, padding=10,bd=0)

      taba = ttk.Frame(tabControl)
      tabb = ttk.Frame(tabControl)
      
      tabControl.add(taba,compound = LEFT, text ='Product/Service')
      tabControl.add(tabb,compound = LEFT, text ='Product Image')
      
      tabControl.pack(expand = 1, fill ="both")
      
      innerFrame = Frame(taba,bg="#f5f3f2", relief=GROOVE)
      innerFrame.pack(side="top",fill=BOTH)

      updateframe = LabelFrame(innerFrame,text="Product/Service",width=580,height=485)
      updateframe.pack(side="top",fill=BOTH,padx=10)

      code1=Label(updateframe,text="Code or SKU:",fg="blue",pady=10,padx=10)
      code1.place(x=20,y=0)
      codeentry = Entry(updateframe,width=35)
      codeentry.place(x=110,y=8)
      codeentry.insert(0, psdata[2])

      checkvarStatus=IntVar()
      status1=Label(updateframe,text="Status:")
      status1.place(x=380,y=8)
      Button1 = Checkbutton(updateframe, 
                        variable = checkvarStatus,text="Active",compound="right",
                        onvalue =1,
                        offvalue =0,
                        width = 10)
      Button1.place(x=420,y=5)
      sta = psdata[6]
      if sta == '1':
        Button1.select()
      else:
        Button1.deselect()



      category1=Label(updateframe,text="Category:",pady=5,padx=10)
      category1.place(x=20,y=40)
      n = StringVar() 
      category = Entry(updateframe,width=70,textvariable=n) 
      category.place(x=110,y=45)
      category.insert(0, psdata[3])


      name1=Label(updateframe,text="Name :",fg="blue",pady=5,padx=10)
      name1.place(x=20,y=70)
      nameentry = Entry(updateframe,width=70)
      nameentry.place(x=110,y=75)
      nameentry.insert(0, psdata[4])

      des1=Label(updateframe,text="Description :",pady=5,padx=10)
      des1.place(x=20,y=100)
      desentry = Entry(updateframe,width=70)
      desentry.place(x=110,y=105)
      desentry.insert(0, psdata[5])

      def set_label(name, index, mode):
        priceval.set(float(uval.get()) - float(costval.get()))

      def prdoucts_cal(S,d):
        if d == '1': #insert
          if not S in ['.','0','1','2','3','4','5','6','7','8','9']:
            return False
          return True
        if d.isdigit():
          return True
      
      unit1=Label(updateframe,text="Unit Price:",fg="blue",pady=5,padx=10)
      unit1.place(x=20,y=130)
      
      uval = StringVar()
      unitentry = Entry(updateframe,width=20,textvariable=uval)
      unitentry.place(x=110,y=135)
      unitentry.delete(0,'end')
      unitentry.insert(0, psdata[7])
      cal_unit = (updateframe.register(prdoucts_cal),'%S','%d')
      unitentry.config(validate='key',validatecommand=(cal_unit),justify='right')
      

      pcsval = IntVar()
      pcs1=Label(updateframe,text="Pcs/Weight:",fg="blue",pady=5,padx=10)
      pcs1.place(x=320,y=130)
      pcsentry = Entry(updateframe,width=20,textvariable=pcsval)
      pcsentry.place(x=410,y=135)
      pcsentry.delete(0,'end')
      pcsentry.insert(0, psdata[8])
      

      costval = StringVar()
      cost1=Label(updateframe,text="Cost:",pady=5,padx=10)
      cost1.place(x=20,y=160)
      costentry = Entry(updateframe,width=20,textvariable=costval)
      costentry.place(x=110,y=165)
      costentry.delete(0, END)
      costentry.insert(0, psdata[9])
      cal_cost = (updateframe.register(prdoucts_cal),'%S','%d')
      costentry.config(validate='key',validatecommand=(cal_cost),justify='right')
      

      priceval = StringVar()
      price1=Label(updateframe,text="(Price-Cost):",pady=5,padx=10)
      price1.place(x=20,y=190)
      priceentry = Entry(updateframe,width=20,textvariable=priceval)
      priceentry.place(x=110,y=195)
      priceentry.delete(0,'end')
      priceentry.insert(0, psdata[11])

      uval.trace('w', set_label)
      costval.trace('w', set_label)
      

      checkvarStatus2=IntVar()
    
      Button2 = Checkbutton(updateframe,variable = checkvarStatus2, 
                        text="Taxable Tax1rate",compound="right",
                        onvalue =1 ,
                        offvalue =0,
                        height=2,
                        width = 12)
      
      checkvarStatustax2=IntVar()
      Buttontax2 = Checkbutton(updateframe,variable = checkvarStatustax2, 
                      text="Taxable Tax2rate",compound="right",
                      onvalue =1 ,
                      offvalue = 0,
                      height=2,
                      width = 12)
      
      sql = "select taxtype from company"
      fbcursor.execute(sql)
      taxchoose = fbcursor.fetchone()
      if not taxchoose:
        pass
      elif taxchoose[0] == '1':
        Button2.place_forget()
        Buttontax2.place_forget()
      elif taxchoose[0] == '2':
        Button2.place(x=415,y=153)
        Buttontax2.place_forget()
      elif taxchoose[0] == '3':
        Button2.place(x=415,y=153)
        Buttontax2.place(x=415,y=203)

   
      tax = psdata[10]
      if tax == '1':
        Button2.select()
      else:
        Button2.deselect()

      if psdata[19] == '1':
        Buttontax2.select()
      else:
        Buttontax2.deselect()

      def switch():
        if checkvarStatus3.get():
          stockentry["state"] = DISABLED
          lowentry["state"] = DISABLED
          wareentry["state"] = DISABLED
        else:
          stockentry["state"] = NORMAL
          lowentry["state"] = NORMAL
          wareentry["state"] = NORMAL
      checkvarStatus3=BooleanVar()
    
      Button3 = Checkbutton(updateframe,variable = checkvarStatus3,command=switch, 
                        text="No stock Control", 
                        onvalue =1 ,
                        offvalue = 0,
                        height=3,
                        width = 15)

      Button3.place(x=40,y=220)

      

      def stocknum(input):
        if input.isdigit():
          return True
        elif input is "":
          return True
        else:
          return False
      stockval = IntVar(updateframe)
      stock1=Label(updateframe,text="Stock:",pady=5,padx=10)
      stock1.place(x=90,y=260)
      stockentry = Entry(updateframe,width=15,textvariable=stockval)
      stockentry.place(x=140,y=265)
      stockentry.delete(0,'end')
      stockentry.insert(0, psdata[13])
      sto = updateframe.register(stocknum)
      stockentry.config(validate="key",validatecommand=(sto, '%S'))
      

      lowval = IntVar(updateframe)
      low1=Label(updateframe,text="Low Stock Warning Limit:",pady=5,padx=10)
      low1.place(x=280,y=260)
      lowentry = Entry(updateframe,width=15,textvariable=lowval)
      lowentry.place(x=435,y=265)
      lowentry.delete(0,'end')
      lowentry.insert(0, psdata[14])
      lowsto = updateframe.register(stocknum)
      lowentry.config(validate="key",validatecommand=(lowsto, '%S'))
      

    
      ware1=Label(updateframe,text="Warehouse:",pady=5,padx=10)
      ware1.place(x=60,y=290)
      wareentry = Entry(updateframe,width=64)
      wareentry.place(x=140,y=295)
      wareentry.insert(0, psdata[15])

      scr = psdata[12]
      if scr == '1':
        Button3.select()
        stockentry["state"] = DISABLED
        lowentry["state"] = DISABLED
        wareentry["state"] = DISABLED
      else:
        Button3.deselect()
        stockentry["state"] = NORMAL
        lowentry["state"] = NORMAL
        wareentry["state"] = NORMAL
      
      

      

      text1=Label(updateframe,text="Private notes(not appears on invoice):",pady=5,padx=10)
      text1.place(x=20,y=320)
      sctxt = scrolledtext.ScrolledText(updateframe, undo=True,width=62,height=4)
      sctxt.place(x=32,y=358)
      try:
        sctxt.insert("1.0", psdata[16])
      except:
        pass

      okButton = Button(innerFrame, text ="Ok",image=tick,width=70,compound = LEFT, command=updateproducts)
      okButton.pack(side=LEFT, padx=(10, 0))

      cancelButton = Button(innerFrame,image=cancel,text="Cancel",width=70,compound = LEFT, command=lambda : top.destroy())
      cancelButton.pack(side=RIGHT, padx=(0, 10))
      
      
      imageFrame = Frame(tabb, relief=GROOVE,height=580)
      imageFrame.pack(side="top",fill=BOTH)

      browseimg=Label(imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
      browseimg.place(x=15,y=35)

      browsebutton=Button(imageFrame,text = 'Browse', command=upload_file)
      browsebutton.place(x=470,y=30,height=30,width=50)

      try:
        image = Image.open("images/"+psdata[17])
        resize_image = image.resize((350, 350))
        image = ImageTk.PhotoImage(resize_image)
        b2 = Label(imageFrame,image=image,width=350,height=350)
        b2.photo = image
        b2.place(x=130, y=80)
        print(image)
      except:
        pass

      removeButton = Button(imageFrame,image=cancel,text="Remove Product Image",width=150,compound = LEFT)
      removeButton.place(x=410,y=460)
    except:
      try:
        top.destroy()
      except:
        pass
      messagebox.showerror('F-Billing Revolution', 'Select a record to edit.')
  


######################## DELETE PRODUCT #######################################################################
  def delete_product_check():
    sql = "select * from users"
    fbcursor.execute(sql)
    delexp_check_user = fbcursor.fetchall()
    if not delexp_check_user:
      delete_product()
    else:
      try:
        user_namech = username1.get()
        sql = "select 	delete_product_service from users where username = %s"
        val = (user_namech,)
        fbcursor.execute(sql,val)
        disable_del_exp = fbcursor.fetchone()
        if disable_del_exp[0] == 1:
          delete_product()
        else:
          messagebox.showerror("user","user does not have permission to perform this action")
      except:
        delete_product()

  def delete_product():
    delmess = messagebox.askyesno("Delete product/service", "Are you sure to delete this product/service?")
    if delmess == True:
      itemid = treeproducts.item(treeproducts.focus())["values"][1]
      sql = "delete from Productservice where Productserviceid = %s"
      val = (itemid, )
      fbcursor.execute(sql, val)
      fbilldb.commit()
      treeproducts.delete(treeproducts.selection()[0])
      # messagebox.showinfo("F-Billing Revolution", "Record deleted successfully.")
    else:
      pass


######################## SEARCH PRODUCT  #######################################################################

  def search_pro():
    query = searchvar.get()
    selections = []
    for child in treeproducts.get_children():
        if query in treeproducts.item(child)['values']:
            print(treeproducts.item(child)['values'])
            selections.append(child)
    treeproducts.selection_set(selections)
  

  def search_product():
    global searchvar, searchtop
    searchtop = Toplevel()  
    searchtop.title("Find Text")
    searchtop.geometry("520x200+390+250")
    
    findwhat1=Label(searchtop,text="Find What:",pady=5,padx=10)
    findwhat1.place(x=5,y=20)
    searchvar = StringVar() 
    findwhat = ttk.Combobox(searchtop, width = 50, textvariable = searchvar)
    findwhat.place(x=80,y=25) 
    

    findButton = Button(searchtop, text ="Find next",width=10, command=search_pro)
    findButton.place(x=420,y=20)
    
    findin1=Label(searchtop,text="Find in:",pady=5,padx=10)
    findin1.place(x=5,y=47)
    n = StringVar() 
    findIN = ttk.Combobox(searchtop, width = 37, textvariable = n ) 
    # Adding combobox drop down list 
    findIN['values'] = ('Product/Service id',  
                              'Category', 
                              'Active', 
                              'name', 
                              'stock', 
                              'location', 
                              'image', 
                              '<<All>>') 
      
    findIN.place(x=80,y=54) 
    findIN.current(0)

    closeButton = Button(searchtop, text ="Close",width=10, command=lambda : searchtop.destroy())
    closeButton.place(x=420,y=50)

    match1=Label(searchtop,text="Match:",pady=5,padx=10)
    match1.place(x=5,y=74)
    n = StringVar() 
    match = ttk.Combobox(searchtop, width = 27, textvariable = n ) 
      
    # Adding combobox drop down list 
    match['values'] = ('From Any part',' Whole Field',  
                              ' From the beginning of the field')
      
    match.place(x=80,y=83) 
    match.current(0)

    search1=Label(searchtop,text="Search:",pady=5,padx=10)
    search1.place(x=5,y=102)
    n = StringVar() 
    search = ttk.Combobox(searchtop, width = 27, textvariable = n ) 
      
    # Adding combobox drop down list 
    search['values'] = ('All', 'up', 
                              'Down')
      
    search.place(x=80,y=112) 
    search.current(0)


    checkvarStatus4=IntVar()
   
    Button4 = Checkbutton(searchtop,variable = checkvarStatus4, 
                      text="Match Case", 
                      onvalue =0 ,
                      offvalue = 1,
                      height=3,
                      width = 15)

    Button4.place(x=60,y=141)

    checkvarStatus5=IntVar()
   
    Button5 = Checkbutton(searchtop,variable = checkvarStatus5, 
                      text="Match Format", 
                      onvalue =0 ,
                      offvalue = 1,
                      height=3,
                      width = 15)

    Button5.place(x=270,y=141)

    searchtop.mainloop()


######################## REFRESH PRODUCT  #######################################################################

  def refresh_pro_s():
    for record in treeproducts.get_children():
      treeproducts.delete(record)
    fbcursor.execute("select *  from Productservice")
    pandsdata = fbcursor.fetchall()
    countp = 0
    for i in pandsdata:
      if i[6] == '1':
        acti = 'Active'
      else:
        acti = 'Inactive'
      sql = "select currencysign,currsignplace from company"
      fbcursor.execute(sql)
      currsymb = fbcursor.fetchone()
      if not currsymb: 
        if i[13] > i[14]:
          treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('green',))
          countp += 1              
        elif i[12] == '1':
          treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('blue',))
          countp += 1
        else:
          treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('red',))
          countp += 1
              
      elif currsymb[1] == "before amount":
        if (i[13]) > (i[14]):
          treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('green',))
          countp += 1
        elif i[12] == '1':
          treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('blue',))
          countp += 1
        else:
          treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('red',))
          countp += 1
      elif currsymb[1] == "before amount with space":
        if i[13] > i[14]:
          treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('green',))
          countp += 1
        elif i[12] == '1':
          treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('blue',))
          countp += 1
        else:
          treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('red',))
          countp += 1
      elif currsymb[1] == "after amount":
        if i[13] > i[14]:
          treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('green',))
          countp += 1
        elif i[12] == '1':
          treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
          countp += 1
        else:
          treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('red',))
          countp += 1
      elif currsymb[1] == "after amount with space":
          if i[13] > i[14]:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('red',))
            countp += 1

######################## View Image
# #######################################################################
  def psfile_image(event):
      itemid = treeproducts.item(treeproducts.focus())["values"][1]
      sql = "select * from Productservice where Productserviceid = %s"
      val = (itemid,)

      fbcursor.execute(sql, val)
      psdata = fbcursor.fetchone() 
      if psdata[17] is None:
        pass
      else:
        edit_window_img = Toplevel()
        edit_window_img.title("View Image")
        edit_window_img.geometry("700x500")
        image = Image.open("images/"+psdata[17])
        resize_image = image.resize((700, 500))
        image = ImageTk.PhotoImage(resize_image)
        psimage = Label(edit_window_img,image=image)
        psimage.photo = image
        psimage.pack()
  
######################## FRONT PAGE OF PRODUCT SERVICE SECTION #######################################################################

    
  mainFrame=Frame(tab8, relief=GROOVE, bg="#f8f8f2")
  mainFrame.pack(side="top", fill=BOTH)

  midFrame=Frame(mainFrame, bg="#f5f3f2", height=60)
  midFrame.pack(side="top", fill=X)

  lFrame=Frame(tab8, bg="#f8f8f2", height=600)
  lFrame.pack(side="top", fill=X)



  pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=(5, 2))
  pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=(0, 5))

  productLabel = Button(midFrame,compound="top", text="Add new\nProduct",relief=RAISED,command=add_product_s_connection, image=productIcon, font=("arial", 8),bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
  productLabel.pack(side="left", pady=3, ipadx=4)
  
  
  proeditLabel = Button(midFrame,compound="top", text="Edit/View\nProduct",relief=RAISED, image=proeditIcon,command=edit_product, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
  proeditLabel.pack(side="left")

  
  prodeleteLabel = Button(midFrame,compound="top", text="Delete\nSelected",relief=RAISED, command=delete_product_check,image=prodeleteIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
  prodeleteLabel.pack(side="left")

  pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=5)

  
  prosearchLabel = Button(midFrame,compound="top", text="Search in\nproducts",relief=RAISED,command=search_product, image=prosearchIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55, activebackground="red")
  prosearchLabel.pack(side="left")

  
  proimportLabel = Button(midFrame,compound="top", text="Import\nProducts",relief=RAISED,command=import_productservice_check, image=proimportIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
  proimportLabel.pack(side="left")

  pn = Canvas(midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=5)

  
  proexportLabel = Button(midFrame,compound="top",command=export_product, text="Export\nProducts",relief=RAISED, image=proexportIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
  proexportLabel.pack(side="left")


  pn = Canvas(midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
  pn.pack(side="left")

  
  productrefreshLabel = Button(midFrame,compound="top", text="Refresh\nProduct List",relief=RAISED, image=prorefreshIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55, command=refresh_pro_s)
  productrefreshLabel.pack(side="left")

  prolabel = Label(mainFrame, text="Products/Services", font=("arial", 18), bg="#f8f8f2")
  prolabel.pack(side="left", padx=(20,0))

  pr_label = Label(mainFrame, text="Category", font=("arial", 16), bg="#f8f8f2")
  pr_label.place(x=1099,y=70)

  def pro_fil(event):
    pro_f = dro.get()
    for record in treeproducts.get_children():
      treeproducts.delete(record)

    sql = "select * from Productservice where category = %s"
    val = (pro_f,)
    fbcursor.execute(sql, val)
    product_fil = fbcursor.fetchall()
    
    countp = 0
    for i in product_fil:
      if i[6] == '1':
        acti = 'Active'
      else:
        acti = 'Inactive' 
      if i[13] > i[14]:
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4] , i[7], i[13], i[15],i[17]),tags=('green',))
        countp += 1
      elif (i[12] =="0") == (i[13] <= i[14]):
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4] , i[7], i[13], i[15],i[17]),tags=('red',))
        countp += 1
      elif i[12] == '1':
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4] , i[7], i[13], i[15],i[17]),tags=('blue',))
        countp += 1
      else:
        pass

  sql = "SELECT DISTINCT category FROM Productservice"
  fbcursor.execute(sql,)
  lic = fbcursor.fetchall()
  dro = ttk.Combobox(mainFrame,)
  dro.pack(side="right", padx=(0,10))
  dro['values'] = lic
  dro.bind("<<ComboboxSelected>>", pro_fil)

  pro_label = Label(mainFrame, text="Right click on datagrid row for more options.",  bg="#f8f8f2")
  pro_label.pack(side="right", padx=(0,260))


  sql = 'select * from Productservice'
  fbcursor.execute(sql)
  pandsdata = fbcursor.fetchall()

  treeproducts=ttk.Treeview(tab8,selectmode='browse')
  treeproducts.place(x=8,y=100,height=580)
  vertical_bar=ttk.Scrollbar(tab8,orient="vertical")
  vertical_bar.place(x=1083,y=101,height=580)

  treeproducts["columns"]=("1","2","3","4","5","6","7","8","9")
  treeproducts["show"]='headings'
  treeproducts.column("1",width=0,anchor='c', stretch=False)
  treeproducts.column("2",width=160,anchor='c')
  treeproducts.column("3",width=190,anchor='c')
  treeproducts.column("4",width=120,anchor='c')
  treeproducts.column("5",width=120,anchor='c')
  treeproducts.column("6",width=120,anchor='c')
  treeproducts.column("7",width=130,anchor='c')
  treeproducts.column("8",width=120,anchor='c')
  treeproducts.column("9",width=112,anchor='c')
  treeproducts.heading("1",text="")
  treeproducts.heading("2",text="Product/Service ID")
  treeproducts.heading("3",text="Category")
  treeproducts.heading("4",text="Status")
  treeproducts.heading("5",text="Name")
  treeproducts.heading("6",text="Price")
  treeproducts.heading("7",text="Stock")
  treeproducts.heading("8",text="Location/warehouse")
  treeproducts.heading("9",text="Image")
  treeproducts.bind('<Double-Button-1>' , psfile_image)
  treeproducts.tag_configure('green', foreground='green')
  treeproducts.tag_configure('red', foreground='red')
  treeproducts.tag_configure('blue', foreground='blue')
  countp = 0
  for i in pandsdata:
    if i[6] == '1':
      acti = 'Active'
    else:
      acti = 'Inactive'
    sql = "select currencysign,currsignplace from company"
    fbcursor.execute(sql)
    currsymb = fbcursor.fetchone()
    if not currsymb: 
      if i[13] > i[14]:
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('green',))
        countp += 1              
      elif i[12] == '1':
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('blue',))
        countp += 1
      else:
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('red',))
        countp += 1
              
    elif currsymb[1] == "before amount":
      if (i[13]) > (i[14]):
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('green',))
        countp += 1
      elif i[12] == '1':
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('blue',))
        countp += 1
      else:
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('red',))
        countp += 1

    elif currsymb[1] == "before amount with space":
      if i[13] > i[14]:
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('green',))
        countp += 1
      elif i[12] == '1':
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('blue',))
        countp += 1
      else:
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('red',))
        countp += 1

    elif currsymb[1] == "after amount":
      if i[13] > i[14]:
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('green',))
        countp += 1
      elif i[12] == '1':
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
        countp += 1
      else:
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('red',))
        countp += 1

    elif currsymb[1] == "after amount with space":
      if i[13] > i[14]:
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('green',))
        countp += 1
      elif i[12] == '1':
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
        countp += 1
      else:
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('red',))
        countp += 1


  treeproducts.place(height=580, width=1070, x=10, y=101)

  ######side_Listbox##############

  treeps=ttk.Treeview(tab8,selectmode='browse')
  treeps.place(height=580,width=254,
                        x=1099,y=101
                        )
  treeps["columns"]=("1")
  treeps["show"]='headings'
  treeps.column("1",width=254,anchor='c')
  treeps.heading("1",text="View filter by category")

  def items_selected(event):
    selected_indices = listbox.curselection()
    selected_filter = ",".join([listbox.get(i) for i in selected_indices])

    sql = 'select * from Productservice'
    fbcursor.execute(sql)
    pandsdata = fbcursor.fetchall()
    psql = "select * from Productservice where serviceornot=%s"
    val = ('0', )
    fbcursor.execute(psql, val)
    pdata = fbcursor.fetchall()

    ssql = "select * from Productservice where serviceornot=%s"
    val = ('1', )
    fbcursor.execute(ssql, val)
    sdata = fbcursor.fetchall()

    # pssql = "select * from Productservice where category=%s"
    # psval = (selected_filter, )
    # fbcursor.execute(pssql, psval)
    # pssdata = fbcursor.fetchall()
    if selected_filter == "View all records":
      for record in treeproducts.get_children():
        treeproducts.delete(record)
      countp = 0
      for i in pandsdata:
        if i[6] == '1':
          acti = 'Active'
        else:
          acti = 'Inactive' 
        sql = "select currencysign,currsignplace from company"
        fbcursor.execute(sql)
        currsymb = fbcursor.fetchone()
        if not currsymb: 
          if i[13] > i[14]:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('green',))
            countp += 1              
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('red',))
            countp += 1
              
        elif currsymb[1] == "before amount":
          if (i[13]) > (i[14]):
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('red',))
            countp += 1

        elif currsymb[1] == "before amount with space":
          if i[13] > i[14]:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('red',))
            countp += 1

        elif currsymb[1] == "after amount":
          if i[13] > i[14]:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('red',))
            countp += 1

        elif currsymb[1] == "after amount with space":
          if i[13] > i[14]:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('red',))
            countp += 1

    elif selected_filter == "View all products":
      for record in treeproducts.get_children():
        treeproducts.delete(record)
      countp = 0
      for i in pdata:
        if i[6] == '1':
          acti = 'Active'
        else:
          acti = 'Inactive' 
        sql = "select currencysign,currsignplace from company"
        fbcursor.execute(sql)
        currsymb = fbcursor.fetchone()
        if not currsymb: 
          if i[13] > i[14]:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('green',))
            countp += 1              
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('red',))
            countp += 1
              
        elif currsymb[1] == "before amount":
          if (i[13]) > (i[14]):
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('red',))
            countp += 1

        elif currsymb[1] == "before amount with space":
          if i[13] > i[14]:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('red',))
            countp += 1

        elif currsymb[1] == "after amount":
          if i[13] > i[14]:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('red',))
            countp += 1

        elif currsymb[1] == "after amount with space":
          if i[13] > i[14]:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('red',))
            countp += 1
    elif selected_filter == "View all services":
      for record in treeproducts.get_children():
        treeproducts.delete(record)
      countp = 0
      for i in sdata:
        if i[6] == '1':
          acti = 'Active'
        else:
          acti = 'Inactive' 
        sql = "select currencysign,currsignplace from company"
        fbcursor.execute(sql)
        currsymb = fbcursor.fetchone()
        if not currsymb: 
          if i[13] > i[14]:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('green',))
            countp += 1              
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('red',))
            countp += 1
              
        elif currsymb[1] == "before amount":
          if (i[13]) > (i[14]):
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('red',))
            countp += 1

        elif currsymb[1] == "before amount with space":
          if i[13] > i[14]:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('red',))
            countp += 1

        elif currsymb[1] == "after amount":
          if i[13] > i[14]:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('red',))
            countp += 1

        elif currsymb[1] == "after amount with space":
          if i[13] > i[14]:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('red',))
            countp += 1
  
  listbox = Listbox(tab8,height = 8,  
                        width = 29,  
                        bg = "white",
                        activestyle = 'dotbox',  
                        fg = "black",
                        highlightbackground="white")  
  listbox.insert(0, "View all records")
  listbox.insert(1, "View all products")
  listbox.insert(2, "View all services")
 

  listbox.place(x=1099,y=118,height=564,width=255)

  listbox.bind('<<ListboxSelect>>', items_selected)
  
  stockok = Label(tab8,text="Green: Stock is Ok",foreground="green",background="white").place(x =1110,y =580)
  stocko = Label(tab8,text="Red: Limit <= Low Stock Limit",foreground="red",background="white").place(x =1110,y =600)
  stock = Label(tab8,text="Blue: Service,no Stock Control",foreground="blue",background="white").place(x =1110,y =620)
  
############################  END PRODUCT SERVICES  ############################
######################## FRONT PAGE OF Settings module  #######################################################################
  
      
  settingsframe=Frame(tab10, relief=GROOVE, bg="#f8f8f2")
  settingsframe.pack(side="top", fill=BOTH)
  
  settframe=Frame(settingsframe, bg="#f5f3f2", height=60)
  settframe.pack(side="top", fill=X)
  
  pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=(5, 2))
  pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=(0, 5))
  # def upload_filelogo():
  #   global imglogo,filename
  #   f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
  #   filena = filedialog.askopenfilename(filetypes=f_types)
  #   shutil.copyfile(filena, os.getcwd()+'/images/'+filena.split('/')[-1])
  #   print(filena.split('/')[-1])
  #   image = Image.open(filena)
  #   resize_image = image.resize((280, 160))
  #   imglogo = ImageTk.PhotoImage(resize_image)
    # b2 = Button(secondtab,image=img)
    # b2.place(x=130, y=80)
  
    # btlogo = Button(secondtab,width=280,height=160,image=imglogo)
    # btlogo.place(x=580,y=280)
  global filename
  filename = ""
  def save_company():
    company_name = comname.get()
    company_address = caddent.get(1.0,END)
    company_mail = comemail.get()
    company_salestax =comsalestax.get()
    currency = comcur.get()
    currencysign = comcursign.get()
    currencysign_placement = comcursignpla.get()
    decimal_sepator = comdecsep.get()
    currency_example = comex.get()
    date_format = comdaf.get()
    example_dateformat = exd.get_date()
    tax = radtax.get()
    tax1name = tax1namee.get()
    tax1rate = tax1ratee.get()
    printtax1 = comptax1.get()
    tax2name = tax2namee.get()
    tax2rate = tax2ratee.get()
    printtax2 = comptax2.get()
    printimage = compimg.get()
    win_menu_colour = win_menu.get()
    radiobut = radema.get()
    cbut1 = checkb1.get()
    cbut2 = checkb2.get()
    cbut3 = checkb3.get()
    cbut4 = checkb4.get()
    cbut5 = checkb5.get()
    cbut6 = checkb6.get()
    child = exctree.get_children()
    est_prefix = est_str.get()
    est_header = win_menu1.get()
    est_text1 = est_str1.get()
    est_text2 = est_str2.get()
    est_text3 = est_str3.get()
    est_text4 = est_str4.get()
    est_text5 = est_str5.get()
    est_text6 = est_str6.get()
    est_predefined = est_str7.get(1.0,END)
    est_default = win_menu2.get()
    est_spin1 = spin1.get()
    adv_default = adv_win_menu8.get()
    pord_prefix = prefix_str.get()
    pord_spin = pspin2.get()
    pord_header = pwin_menu.get()
    pord_text1 = pord_str1.get()
    pord_text2 = pord_str2.get()
    pord_text3 = pord_str3.get()
    pord_text4 = pord_str4.get()
    pord_text5 = pord_str5.get()
    pord_text6 = pord_str6.get()
    pord_text7 = pord_str7.get()
    pord_predefind = pord_str8.get(1.0,END)
    combo = em_menu.get()
    textfld = memaiframe.get(1.0,END) 

    var = json.dumps(child)
    sql = "select image from company"
    fbcursor.execute(sql)
    im = fbcursor.fetchone()
    sql = "select * from company"
    fbcursor.execute(sql)
    i = fbcursor.fetchall()
    if not i:
      if filename == "":
        print(12)
        sql = 'insert into company(name, address, email,salestaxno,currency,currencysign,currsignplace,  decimalseperator,excurrency,dateformat,exdate,taxtype,printimageornot,tax1name,tax1rate,printtax1,  tax2name,tax2rate,printtax2,attachment_file_type,miscellanoustab_cbutton1,miscellanoustab_cbutton2,miscellanoustab_cbutton3,miscellanoustab_cbutton4,miscellanoustab_cbutton5,miscellanoustab_cbutton6,Estimate_prefix,Customizeestimatetextlabels,Customizeestimatetextlabels1,Customizeestimatetextlabels2,Customizeestimatetextlabels3,Customizeestimatetextlabels4,Customizeestimatetextlabels5,Defaultestimatetemplate,Startingestimatenumber,Predefinedtextforestimates,adv_Selectedtemplatepreview,est_Headerboxbackgroundcolor,porder_prefix,headrebox_color,starting_porderno,text_label1,text_label2,text_label3,text_label4,text_label5,text_label6,text_label7,predefindterms_porder,email_template,text_field) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)'
        val = (company_name,company_address,company_mail,company_salestax,currency,currencysign,  currencysign_placement,decimal_sepator,currency_example,date_format,example_dateformat,tax,printimage,  tax1name,tax1rate,printtax1,tax2name,tax2rate,printtax2,radiobut,cbut1,cbut2,cbut3,cbut4,cbut5,cbut6,est_prefix,est_text1,est_text2,est_text3,est_text4,est_text5,est_text6,est_default,est_spin1,est_predefined,adv_default,est_header,pord_prefix,pord_spin,pord_header,pord_text1,pord_text2,pord_text3,pord_text4,pord_text5,pord_text6,pord_text7,pord_predefind,combo,textfld)
        fbcursor.execute(sql, val)
        fbilldb.commit()
      else:
        shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
        sql = 'insert into company(name, address, email,salestaxno,currency,currencysign,currsignplace,  decimalseperator,excurrency,dateformat,exdate,taxtype,printimageornot,tax1name,tax1rate,printtax1,  tax2name,tax2rate,printtax2,image,attachment_file_type,miscellanoustab_cbutton1,miscellanoustab_cbutton2,miscellanoustab_cbutton3,miscellanoustab_cbutton4,miscellanoustab_cbutton5,miscellanoustab_cbutton6,Estimate_prefix,Customizeestimatetextlabels,Customizeestimatetextlabels1,Customizeestimatetextlabels2,Customizeestimatetextlabels3,Customizeestimatetextlabels4,Customizeestimatetextlabels5,Defaultestimatetemplate,Startingestimatenumber,Predefinedtextforestimates,adv_Selectedtemplatepreview,est_Headerboxbackgroundcolor,porder_prefix,headrebox_color,starting_porderno,text_label1,text_label2,text_label3,text_label4,text_label5,text_label6,text_label7,predefindterms_porder,email_template,text_field) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        val = (company_name,company_address,company_mail,company_salestax,currency,currencysign,  currencysign_placement,decimal_sepator,currency_example,date_format,example_dateformat,tax,printimage,  tax1name,tax1rate,printtax1,tax2name,tax2rate,printtax2,filename.split('/')[-1],radiobut,cbut1,cbut2,cbut3,cbut4,cbut5,cbut6,est_prefix,est_text1,est_text2,est_text3,est_text4,est_text5,est_text6,est_default,est_spin1,est_predefined,adv_default,est_header,pord_prefix,pord_spin,pord_header,pord_text1,pord_text2,pord_text3,pord_text4,pord_text5,pord_text6,pord_text7,pord_predefind,combo,textfld)
        fbcursor.execute(sql, val)
        fbilldb.commit()
    else:
      if filename == "":
        sql = "update company set name=%s, address=%s, email=%s,salestaxno=%s,currency=%s,currencysign=%s,  currsignplace=%s,decimalseperator=%s,excurrency=%s,dateformat=%s,exdate=%s,taxtype=%s,  printimageornot=%s,tax1name=%s,tax1rate=%s,printtax1=%s,tax2name=%s,tax2rate=%s,printtax2=%s,attachment_file_type=%s,miscellanoustab_cbutton1=%s,miscellanoustab_cbutton2=%s,miscellanoustab_cbutton3=%s,miscellanoustab_cbutton4=%s,miscellanoustab_cbutton5=%s,miscellanoustab_cbutton6=%s,Estimate_prefix=%s,Customizeestimatetextlabels=%s,Customizeestimatetextlabels1=%s,Customizeestimatetextlabels2=%s,Customizeestimatetextlabels3=%s,Customizeestimatetextlabels4=%s,Customizeestimatetextlabels5=%s,Defaultestimatetemplate=%s,Startingestimatenumber=%s,Predefinedtextforestimates=%s,adv_Selectedtemplatepreview=%s,est_Headerboxbackgroundcolor=%s,porder_prefix=%s,headrebox_color=%s,starting_porderno=%s,text_label1=%s,text_label2=%s,text_label3=%s,text_label4=%s,text_label5=%s,text_label6=%s,text_label7=%s,predefindterms_porder=%s,email_template=%s,text_field=%s"
        val = (company_name,company_address,company_mail,company_salestax,currency,currencysign,  currencysign_placement,decimal_sepator,currency_example,date_format,example_dateformat,tax,printimage,  tax1name,tax1rate,printtax1,tax2name,tax2rate,printtax2,radiobut,cbut1,cbut2,cbut3,cbut4,cbut5,cbut6,est_prefix,est_text1,est_text2,est_text3,est_text4,est_text5,est_text6,est_default,est_spin1,est_predefined,adv_default,est_header,pord_prefix,pord_spin,pord_header,pord_text1,pord_text2,pord_text3,pord_text4,pord_text5,pord_text6,pord_text7,pord_predefind,combo,textfld)
        fbcursor.execute(sql, val)
        fbilldb.commit()
      else:
        shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
        sql = "update company set name=%s, address=%s, email=%s,salestaxno=%s,currency=%s,currencysign=%s,  currsignplace=%s,decimalseperator=%s,excurrency=%s,dateformat=%s,exdate=%s,taxtype=%s,  printimageornot=%s,tax1name=%s,tax1rate=%s,printtax1=%s,tax2name=%s,tax2rate=%s,printtax2=%s,image=%s,attachment_file_type=%s,miscellanoustab_cbutton1=%s,miscellanoustab_cbutton2=%s,miscellanoustab_cbutton3=%s,miscellanoustab_cbutton4=%s,miscellanoustab_cbutton5=%s,miscellanoustab_cbutton6=%s,Estimate_prefix=%s,Customizeestimatetextlabels=%s,Customizeestimatetextlabels1=%s,Customizeestimatetextlabels2=%s,Customizeestimatetextlabels3=%s,Customizeestimatetextlabels4=%s,Customizeestimatetextlabels5=%s,Defaultestimatetemplate=%s,Startingestimatenumber=%s,Predefinedtextforestimates=%s,adv_Selectedtemplatepreview=%s,est_Headerboxbackgroundcolor=%s,porder_prefix=%s,headrebox_color=%s,starting_porderno=%s,text_label1=%s,text_label2=%s,text_label3=%s,text_label4=%s,text_label5=%s,text_label6=%s,text_label7=%s,predefindterms_porder=%s,email_template=%s,text_field=%s"
        val = (company_name,company_address,company_mail,company_salestax,currency,currencysign,  currencysign_placement,decimal_sepator,currency_example,date_format,example_dateformat,tax,printimage,  tax1name,tax1rate,printtax1,tax2name,tax2rate,printtax2,filename.split('/')[-1],radiobut,cbut1,cbut2,cbut3,cbut4,cbut5,cbut6,est_prefix,est_text1,est_text2,est_text3,est_text4,est_text5,est_text6,est_default,est_spin1,est_predefined,adv_default,est_header,pord_prefix,pord_spin,pord_header,pord_text1,pord_text2,pord_text3,pord_text4,pord_text5,pord_text6,pord_text7,pord_predefind,combo,textfld)
        fbcursor.execute(sql, val)
        fbilldb.commit()
      
      
  
  
  save_setting = Button(settframe,compound="top", text="Save\nSettings",relief=RAISED,    command=save_company, image=saves, font=("arial", 8),bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
  save_setting.pack(side="left", pady=3, ipadx=4)
  pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=(0, 5))
  
  def wiz_page():
    global filname
    filname = ""
    def upload_cfilelogo():
      global filname
      f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
      filname = filedialog.askopenfilename(filetypes=f_types)
      shutil.copyfile(filname, os.getcwd()+'/images/'+filname.split('/')[-1])
      image = Image.open(filname)
      resize_image = image.resize((280, 140))
      imgclogo = ImageTk.PhotoImage(resize_image)
      btclogo = Button(wiz,width=280,height=140,image=imgclogo)
      btclogo.place(x=30,y=240)
      btclogo.photo = imgclogo
    def csave():
      company_name = company_namee.get()
      company_address = company_addresse.get('1.0', 'end-1c')
      company_email = company_emaile.get()
      salestaxregno = salestaxregnoe.get()
      cprint_logopic = cplogopic.get()
      sql = "select image from company"
      fbcursor.execute(sql)
      im = fbcursor.fetchone()
      sql = "select * from company"
      fbcursor.execute(sql)
      i = fbcursor.fetchall()
      if not i:
        if filname == "":
          sql = 'insert into company(name, address, email,salestaxno,printimageornot) values(%s, %s, %s, %s, %s)'
          val = (company_name,company_address,company_email,salestaxregno,cprint_logopic)
          fbcursor.execute(sql, val)
          fbilldb.commit()
        else:
          shutil.copyfile(filname, os.getcwd()+'/images/'+filname.split('/')[-1])
          sql = 'insert into company(name, address, email,salestaxno,printimageornot,image) values(%s, %s, %s, %s, %s, %s)'
          val = (company_name,company_address,company_email,salestaxregno,cprint_logopic,filname.split('/')[-1],)
          fbcursor.execute(sql, val)
          fbilldb.commit()
      else:
        if filname == "":
          sql = "update company set name=%s, address=%s, email=%s,salestaxno=%s,printimageornot=%s"
          val = (company_name,company_address,company_email,salestaxregno,cprint_logopic)
          fbcursor.execute(sql, val)
          fbilldb.commit()
        else:
          shutil.copyfile(filname, os.getcwd()+'/images/'+filname.split('/')[-1])
          sql = "update company set name=%s, address=%s, email=%s,salestaxno=%s,printimageornot=%s,image=%s"
          val = (company_name,company_address,company_email,salestaxregno,cprint_logopic,filname.split('/')[-1])
          fbcursor.execute(sql, val)
          fbilldb.commit()
      centry.delete(0, END)
      centry.insert(0, company_name)
      caddent.delete('1.0', END)
      caddent.insert('1.0', company_address)
      cemailentry.delete(0, END)
      cemailentry.insert(0, company_email)
      ste.delete(0, END)
      ste.insert(0, salestaxregno)
      if cprint_logopic == 1:
        primage.select()
      else:
        primage.deselect()
      try:
        image = Image.open("images/"+filname.split('/')[-1])
        resize_image = image.resize((280, 160))
        image = ImageTk.PhotoImage(resize_image)
        btlogo = Button(secondtab,width=280,height=160,image=image)
        btlogo.place(x=580,y=280)
        btlogo.photo = image
      except:
        pass
      wiz.destroy()


      
      

    
    wiz = Toplevel()
    wiz.geometry("500x449+400+167")
    wiz.title("Wellcome to Quick Start Wizard")
    sql = "select * from company"
    fbcursor.execute(sql)
    secctab = fbcursor.fetchone()
    comp_infor = Label(wiz,text="Enter Your Company Information",font='arial 13 bold',fg="blue")
    comp_infor.place(x=15,y=15)
    company_da_laframe = LabelFrame(wiz,text="Company data",height=180, width=460)
    company_da_laframe.place(x=15,y=40)
    company_name = Label(wiz,text="Company name")
    company_name.place(x=30,y=60)
    company_namee = Entry(wiz,width=50)
    company_namee.place(x=160,y=60)
    if  not secctab:
      pass
    else:
      company_namee.insert(0, secctab[1])
  
    company_address = Label(wiz,text="Company address")
    company_address.place(x=30,y=90)
    company_addresse = scrolledtext.ScrolledText(wiz,)
    company_addresse.place(x=160,y=90,width=250,height=60)
    if  not secctab:
      pass
    else:
      company_addresse.insert('1.0', secctab[2])

    company_email = Label(wiz,text="Email address")
    company_email.place(x=30,y=160)
    company_emaile = Entry(wiz,width=50)
    company_emaile.place(x=160,y=160)
    if  not secctab:
      pass
    else:
      company_emaile.insert(0, secctab[3])

    salestaxregno = Label(wiz,text="Sales Tax.Reg.No")
    salestaxregno.place(x=30,y=190)
    salestaxregnoe = Entry(wiz,width=50)
    salestaxregnoe.place(x=160,y=190)
    if  not secctab:
      pass
    else:
      salestaxregnoe.insert(0, secctab[4])
    
    
    company_da_laframe = LabelFrame(wiz,text="Company logo",height=190, width=460)
    company_da_laframe.place(x=15,y=220)
    try:
      image_wiz = Image.open("images/"+secctab[13])
      resize_image = image_wiz.resize((280, 140))
      image_wiza = ImageTk.PhotoImage(resize_image)
      btclogo = Button(wiz,width=280,height=140,image=image_wiza)
      btclogo.place(x=30,y=240)
      btclogo.photo = image_wiza
    except:
      pass
    cplogopic = BooleanVar()
    cprint_logopic = Checkbutton(wiz,text='Print logo picture',bg='white',onvalue =1,
                        offvalue = 0,variable=cplogopic)
    cprint_logopic.place(x=320,y=250)
    if  not secctab:
      pass
    else:
      if secctab[14] == 1:
        cprint_logopic.select()
      else:
        cprint_logopic.deselect()
      
    load_img = Button(wiz,text='Load logo image',command=upload_cfilelogo)
    load_img.place(x=320,y=360)
    save_com_wiz = Button(wiz,text='Save',width=10,command=csave)
    save_com_wiz.place(x=370,y=415)

  quick_start_wiz = Button(settframe,compound="top", text="Quick\nStart Wizard ",relief=RAISED,    command=wiz_page, image=photo, font=("arial", 8),bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
  quick_start_wiz.pack(side="left", pady=3, ipadx=4)
  pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=(0, 5))
  
  
  
  invoi1label = Label(settingsframe, text="Settings", font=("arial", 18), bg="#f8f8f2")
  invoi1label.pack(side="left", padx=(20,0))
  
  global tab06
  m = ttk.Style()
  m.theme_use('default')
  m.configure('one.TNotebook.Tab', background="white", width=20, padding=10)
  tabControl = ttk.Notebook(tab10,style='one.TNotebook.Tab')
  tab01 = ttk.Frame(tabControl)
  tab02 = ttk.Frame(tabControl)
  tab03=  ttk.Frame(tabControl)
  tab04 = ttk.Frame(tabControl)
  tab05 = ttk.Frame(tabControl)
  tab06=  ttk.Frame(tabControl)
  tab07 = ttk.Frame(tabControl)
  tab08 = ttk.Frame(tabControl)
  tab09 =  ttk.Frame(tabControl)
  tab010=  ttk.Frame(tabControl)
  tabControl.add(tab01,image=invoices,compound = LEFT, text ='Miscellaneous',)
  tabControl.add(tab02,image=orders,compound = LEFT, text ='Company settings')
  tabControl.add(tab03,image=estimates,compound = LEFT, text ='Invoiced settings')
  tabControl.add(tab04,image=recurring,compound = LEFT, text ='Order settings')
  tabControl.add(tab05,image=purchase,compound = LEFT, text ='Estimate settings') 
  tabControl.add(tab06,image=expenses,compound = LEFT, text ='Administrator panel')
  tabControl.add(tab07,image=customer,compound = LEFT, text ='Advanced settings')
  tabControl.add(tab08,image=product,compound = LEFT, text ='Email templates')
  tabControl.add(tab09,image=reports,compound = LEFT, text ='Payments')
  tabControl.add(tab010,image=setting,compound = LEFT, text ='Purchase Order')
  tabControl.pack(expand = 1, fill ="both")
  
  ################### tab01 ###################################
  sql = "select * from company"
  fbcursor.execute(sql)
  sectab = fbcursor.fetchone()
  
  firsttab1=Frame(tab01, relief=GROOVE, bg="#f8f8f2")
  firsttab1.pack(side="top", fill=BOTH)
  
  firsttab=Frame(firsttab1, bg="#f5f3f2", height=700)
  firsttab.pack(side="top", fill=BOTH)
  
  messagelbframe=LabelFrame(firsttab,text="Menu and Window Color Style", height=60, width=180)
  messagelbframe.place(x=5, y=15)
  
  win_menu = StringVar()
  winstyle = ttk.Combobox(firsttab,textvariable=win_menu)
  winstyle.place(x=22 ,y=40)
  winstyle['values'] = ('whidbey','windows XP','windows 7','windows 8','windows 10')
  winstyle.current(0)
  fbill = Label(firsttab,text="F-Billing Revolution 2022",font="arial 12 bold").place(x=220,y=20)
  
  dbhost=LabelFrame(firsttab,text="Database Server Hostname", height=60, width=415)
  dbhost.place(x=5, y=85)
  
  db = Label(firsttab, text="DESKTOP-2K")
  db.place(x=15,y=110)
  
  exc=LabelFrame(firsttab,text="Extra cost name", height=180, width=415)
  exc.place(x=5, y=155)
  
  
  
  def insert_valueexc():
    i = varexc.get()
    if i == "":
      pass
    else:
      entryexc.delete(0, END)
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      if not com:
        messagebox.showinfo("Alert", "Create Company Settings.")
      else:
        companyid = com[0]
        sql = 'insert into extra_cost_name(companyid,extra_cost_name) values(%s,%s)'
        val = (companyid,i)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        for record in exctree.get_children():
          exctree.delete(record)
        sql = 'select * from extra_cost_name'
        fbcursor.execute(sql)
        setexctree = fbcursor.fetchall()
        countp = 0
        for i in setexctree:
          immm = str(i[2])
          imn = str.replace(immm," ","_")
          exctree.insert(parent='', index='end', iid=countp, text='hello', values=(imn))
          countp += 1
  # new_value = String
        
        
  
  def edit_valueexc(event):
    selected_item = exctree.selection()[0]
    temp = list(exctree.item(selected_item , 'values'))
    entryexc.delete(0, END)
    entryexc.insert(0, temp)
  
  def save_valueexc():
    i = entryexc.get()
    if i == "":
      pass
    else:
      selected0 = exctree.focus()
      valuz1= exctree.item(selected0)["values"]
      idgettingextracnid=valuz1[0]
      print(i,idgettingextracnid)
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      companyid = com[0]
      if not com:
        pass
      else:
        sql = 'update extra_cost_name set extra_cost_name=%s where extra_cost_name=%s'
        val = (i,idgettingextracnid)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        entryexc.delete(0, END)
        for record in exctree.get_children():
            exctree.delete(record)
        fbcursor.execute("select *  from extra_cost_name")
        pandsdata = fbcursor.fetchall()
        countp = 0
        for i in pandsdata:
          immm = str(i[2])
          imn = str.replace(immm," ","_")
          exctree.insert('', index='end', iid=countp, text='', values=(imn))
          countp += 1
    
    
  
  def del_valueexc():
    itemid = exctree.item(exctree.focus())["values"][0]
    sql = "delete from extra_cost_name where extra_cost_name = %s"
    val = (itemid, )
    fbcursor.execute(sql, val)
    fbilldb.commit()
    exctree.delete(exctree.selection()[0])
      
      
  
    
    
    
  
  
  
  scrollbarx = Scrollbar(firsttab, orient=HORIZONTAL)
  scrollbary = Scrollbar(firsttab, orient=VERTICAL)
  exctree = ttk.Treeview(firsttab, columns=("1"),height=40,selectmode='browse', yscrollcommand=scrollbary.set,   xscrollcommand=scrollbarx.set)
  # exctree["show"]='headings'
  scrollbary.config(command=exctree.yview)
  scrollbary.place(x=394,y=200,height=125)
  scrollbarx.config(command=exctree.xview)
  scrollbarx.place(x=15,y=310, width=380)
  exctree.heading('1', text="Extra cost name",)
  # exctree.column('#0', stretch=NO, minwidth=0, width=0)
  exctree.column("#0",width=0,anchor='c', stretch=False)
  exctree.column('1',width=378,anchor='c')
  exctree.place(x=15,y=200,height=115,width=380)
  exctree.bind('<Double-Button-1>' , edit_valueexc)
  sql = 'select * from extra_cost_name'
  fbcursor.execute(sql)
  setexctree = fbcursor.fetchall()
  countp = 0
  for i in setexctree:
      print(i[2])
      immm = str(i[2])
      imn = str.replace(immm," ","_")
      exctree.insert(parent='', index='end', iid=countp, text='', values=(imn))
      countp += 1
  # new_value = StringVar()
  
  # def edit_window_box(val):
      
  #     edit_window = Toplevel(root)
  #     edit_window.title("Edit the value or cancel")
  #     edit_window.geometry("1000x250")
  #     label_edit = Label(edit_window , text='Enter value to edit or press cancel', 
  #     font = ("Times New Roman", 10)).grid(column=0,row=1,padx=0, pady = 2)
  #     #create edit box
  #     edit_box = Entry(edit_window)
  #     edit_box.insert(0,val)
  #     edit_box.grid(column=1,row=1,padx=0,pady=2)
  #     #auto select edit window 
  #     edit_window.focus()
      
  #     def value_assignment(event):
  #         printing = edit_box.get()
  #         new_value.set(printing)
  #         #only destroy will not update the value (perhaps event keeps running in background)
  #         #quit allows event to stop n update value in tree but does not close the window in single click 
  #         #rather on dbl click shuts down entire app 
  #         edit_window.quit()
  #         edit_window.destroy()
      
  #     edit_window.bind('<Return>', value_assignment )
  
  #     B1 = Button(edit_window, text="Okay")
  #     B1.bind('<Button-1>',value_assignment)
  #     B1.grid(column=0,row=10,padx=0, pady = 20)
      
  #     B2 = Button(edit_window, text="Cancel", command = edit_window.destroy).grid(column=1,row=10,padx=10,   pady = 20)
  #     edit_window.mainloop()
      
  # #will explain
  # #variable to hold col value (col clicked)
  # shape1 = IntVar()
  # #tracks both col , row on mouse click
  # def tree_click_handler(event):
  #     cur_item = exctree.item(exctree.focus())
  #     col = exctree.identify_column(event.x)[1:]
  #     rowid = exctree.identify_row(event.y)[1:]
  #     #updates list
  #     shape1.set(col)
  #     try:
  #         x,y,w,h = exctree.bbox('I'+rowid,'#'+col)
  #     except:pass
  #     #tree.tag_configure("highlight", background="yellow")
  #     return(col)
      
  # #code linked to event    
  # exctree.bind('<ButtonRelease-1>', tree_click_handler)
  
  # def edit(event):
  #     try:
  #         selected_item = exctree.selection()[0]
  #         temp = list(exctree.item(selected_item , 'values'))
  #         tree_click_handler
  #         col_selected = int(shape1.get())-1
  #         edit_window_box(temp[col_selected])
  #         #do not run if edit window is open
  #         #use edit_window.mainloop() so value assign after window closes
  #         temp[col_selected] = new_value.get()
  #         exctree.item(selected_item, values= temp)
  #     except: pass
      
      
  # #binding allows to edit on screen double click
  # exctree.bind('<Double-Button-1>' , edit)
  varexc = StringVar()
  entryexc = Entry(firsttab,width=25,textvariable=varexc)
  entryexc.place(x=15,y=173)
  
  btexcadd = Button(firsttab,text="Add new line",command=insert_valueexc)
  btexcadd.place(x=175,y=171)
  
  btexcedit = Button(firsttab,text="Edit line   ",command=save_valueexc)
  btexcedit.place(x=260,y=171)
  btexcadd = Button(firsttab,text=" Delete line  ",command=del_valueexc)
  btexcadd.place(x=330,y=171)
  
  exc=LabelFrame(firsttab,text="Predefined text records for header and footer", height=180, width=415)
  exc.place(x=5, y=350)
  
  def insert_valuepre():
    i = prestr.get()
    if i == "":
      pass
    else:
      entrypre.delete(0, END)
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      if not com:
        messagebox.showinfo("Alert", "Create Company Settings.")
      else:
        companyid = com[0]
        sql = 'insert into header_and_footer(companyid,headerandfooter) values(%s,%s)'
        val = (companyid,i)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        for record in pretree.get_children():
          pretree.delete(record)
        sql = 'select * from header_and_footer'
        fbcursor.execute(sql)
        setexctree = fbcursor.fetchall()
        countp = 0
        for i in setexctree:
          pret = str(i[2])
          pre = str.replace(pret," ","_")
          pretree.insert(parent='', index='end', iid=countp, text='hello', values=(pre))
          countp += 1
  # new_value = String
        
        
  
  def edit_valuepre(event):
    selected_item = pretree.selection()[0]
    temp = list(pretree.item(selected_item , 'values'))
    entrypre.delete(0, END)
    entrypre.insert(0, temp)
  
  def save_valuepre():
    i = prestr.get()
    if i == "":
      pass
    else:
      selected0 = pretree.focus()
      valuz1= pretree.item(selected0)["values"]
      idgettingextracnid=valuz1[0]
      print(i,idgettingextracnid)
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      companyid = com[0]
      if not com:
        pass
      else:
        sql = 'update header_and_footer set headerandfooter=%s where headerandfooter=%s'
        val = (i,idgettingextracnid)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        entryexc.delete(0, END)
        for record in pretree.get_children():
            pretree.delete(record)
        fbcursor.execute("select *  from header_and_footer")
        pandsdata = fbcursor.fetchall()
        countp = 0
        for i in pandsdata:
          pret = str(i[2])
          pre = str.replace(pret," ","_")
          pretree.insert('', index='end', iid=countp, text='', values=(pre))
          countp += 1
    
    
  
  def del_valuepre():
    itemid = pretree.item(pretree.focus())["values"][0]
    print(itemid)
    sql = "delete from header_and_footer where headerandfooter = %s"
    val = (itemid,)
    fbcursor.execute(sql, val)
    fbilldb.commit()
    for record in pretree.get_children():
      pretree.delete(record)
    fbcursor.execute("select *  from header_and_footer")
    pandsdata = fbcursor.fetchall()
    countp = 0
    for i in pandsdata:
      pret = str(i[2])
      pre = str.replace(pret," ","_")
      pretree.insert('', index='end', iid=countp, text='', values=(pre))
      countp += 1
    
      
  
  scrollbarx = Scrollbar(firsttab, orient=HORIZONTAL)
  scrollbary = Scrollbar(firsttab, orient=VERTICAL)
  pretree = ttk.Treeview(firsttab, columns=("1"),height=400,     selectmode="extended",   yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
  # exctree["show"]='headings'
  scrollbary.config(command=pretree.yview)
  scrollbary.place(x=395,y=400,height=115)
  scrollbarx.config(command=pretree.xview)
  scrollbarx.place(x=15,y=510, width=380)
  pretree.heading('1', text="header and footer",)
  pretree.column('#0', stretch=NO, minwidth=0, width=0)
  pretree.column('1', stretch=NO, width=378)
  pretree.place(x=15,y=400,height=115,width=380)
  pretree.bind('<Double-Button-1>' , edit_valuepre)
  sql = 'select * from header_and_footer'
  fbcursor.execute(sql)
  setexctree = fbcursor.fetchall()
  countp = 0
  for i in setexctree:
    pret = str(i[2])
    pre = str.replace(pret," ","_")
    pretree.insert(parent='', index='end', iid=countp, text='hello', values=(pre))
    countp += 1
  prestr = StringVar()
  entrypre = Entry(firsttab,width=25,textvariable=prestr)
  entrypre.place(x=15,y=370)
  btexcadd = Button(firsttab,text="Add new line",command=insert_valuepre)
  btexcadd.place(x=175,y=370)
  btpredit = Button(firsttab,text="Edit line   ",command=save_valuepre)
  btpredit.place(x=260,y=370)
  btexcadd = Button(firsttab,text=" Delete line   ",command=del_valuepre)
  btexcadd.place(x=330,y=370)
  
  ver = Label(firsttab,text="FREE version.Upgrade PRO version for all features and Ad free invoice")
  ver.place(x=480,y=15)
  
  
  chapass=LabelFrame(firsttab,text="Change Password", height=150, width=500)
  chapass.place(x=480, y=40)
  
  enterold = StringVar()
  lenold = Label(firsttab,text="Enter your old password")
  lenold.place(x=495,y=60)
  enold = Entry(firsttab,textvariable=enterold)
  enold.place(x=640,y=60)
  
  enternew = StringVar()
  ennew = Label(firsttab,text="New password")
  ennew.place(x=495,y=90)
  newpass = Entry(firsttab,textvariable=enternew)
  newpass.place(x=640,y=90)
  
  
  cnewpass = StringVar()
  cnp = Label(firsttab,text="Confirm new password")
  cnp.place(x=495,y=120)
  cnewp = Entry(firsttab,textvariable=cnewpass)
  cnewp.place(x=640,y=120)

  def change_pass():
    old_pass = enterold.get()
    new_pass = enternew.get()
    cnew_pass = cnewpass.get()
    usna = username1.get()
    print(usna)
    sql='SELECT * FROM users WHERE username=%s'
    val=(usna,)
    fbcursor.execute(sql,val)
    chpass = fbcursor.fetchone()
    print(chpass)
    if old_pass == "" or new_pass == "" or cnew_pass == "":
        messagebox.showerror('Password Error','Plz enter password')
    elif old_pass == chpass[4]:
      if new_pass == cnew_pass:
        sqll='UPDATE users SET password=%s,confirm_password=%s WHERE userID=%s'
        vall=(new_pass,cnew_pass,chpass[0])
        fbcursor.execute(sqll,vall,)
        fbilldb.commit()
        messagebox.showinfo('Updated','Password updated successfully')
      else:
        messagebox.showerror('Password Error','password is not match')
    else:
      messagebox.showerror('Password Error','Old Password is Incorrect')
  chabtn = Button(firsttab,text="Change password",command=change_pass)
  chabtn.place(x=840,y=150)
  
  termf=LabelFrame(firsttab,text="Terms of payment", height=150, width=500)
  termf.place(x=480, y=190)


  def insert_valueterm():
    first = entrytopstr.get()
    second = entrydsstr.get()
    if first == "" or second == "":
      pass
    else:
      entrytop.delete(0, END)
      entryds.delete(0, END)
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      if not com:
        messagebox.showinfo("Alert", "Create Company Settings.")
      else:
        companyid = com[0]
        sql = 'insert into terms_of_payment(companyid,terms_of_payment,Date_shift) values(%s,%s,%s)'
        val = (companyid,first,second)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        for record in termtree.get_children():
          termtree.delete(record)
        sql = 'select * from terms_of_payment'
        fbcursor.execute(sql)
        setexctree = fbcursor.fetchall()
        countp = 0
        for i in setexctree:
          
          termtree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[3]))
          countp += 1
  # new_value = String
        
        
  
  def edit_valueterm(event):
    itemid = termtree.item(termtree.focus())["values"][0]
    sql = "select * from terms_of_payment where terms_of_payment = %s"
    val = (itemid,)
    fbcursor.execute(sql,val)
    editterm = fbcursor.fetchone()
    entrytop.delete(0, END)
    entryds.delete(0, END)
    entrytop.insert(0, editterm[2])
    entryds.insert(0, editterm[3])
  
  def save_valueterm():
    first = entrytopstr.get()
    second = entrydsstr.get()
    if first == "" or second == "":
      pass
    else:
      itemid = termtree.item(termtree.focus())["values"][0]
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      if not com:
        pass
      else:
        sql = "select * from terms_of_payment where terms_of_payment=%s"
        val = (itemid,)
        fbcursor.execute(sql,val)
        payt = fbcursor.fetchone()
        sql2 = 'update terms_of_payment set terms_of_payment=%s,Date_shift=%s where terms_of_paymentID=%s'
        val2 = (first,second,payt[0])
        fbcursor.execute(sql2,val2)
        fbilldb.commit()
        entrytop.delete(0, END)
        entryds.delete(0, END)
        for record in termtree.get_children():
          termtree.delete(record)
        fbcursor.execute("select *  from terms_of_payment")
        pandsdata = fbcursor.fetchall()
        countp = 0
        for i in pandsdata:
          
          termtree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[3]))
          countp += 1
    
    
  
  def del_valueterm():
    itemid = termtree.item(termtree.focus())["values"][0]
    print(itemid)
    sql = "delete from terms_of_payment where terms_of_payment = %s"
    val = (itemid,)
    fbcursor.execute(sql, val)
    fbilldb.commit()
    for record in termtree.get_children():
        termtree.delete(record)
    fbcursor.execute("select *  from terms_of_payment")
    pandsdata = fbcursor.fetchall()
    countp = 0
    for i in pandsdata:
      termtree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[3]))
      countp += 1
  
  
  
  scrollbarx = Scrollbar(firsttab, orient=HORIZONTAL)
  scrollbary = Scrollbar(firsttab, orient=VERTICAL)
  termtree = ttk.Treeview(firsttab, columns=("1","2"),height=400,selectmode="extended",   yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
  # exctree["show"]='headings'
  scrollbary.config(command=termtree.yview)
  scrollbary.place(x=870,y=228,height=100)
  scrollbarx.config(command=termtree.xview)
  scrollbarx.place(x=495,y=313, width=380)
  termtree.heading('1', text="Terms of payment",)
  termtree.heading('2', text="Date shift (days)",)
  termtree.column('#0', stretch=NO, minwidth=0, width=0)
  termtree.column('1', stretch=NO, minwidth=0, width=250)
  termtree.column('2', stretch=NO, minwidth=0, width=128)
  termtree.place(x=495,y=235,height=80,width=380)
  termtree.bind('<Double-Button-1>' , edit_valueterm)

  sql = 'select * from terms_of_payment'
  fbcursor.execute(sql)
  termt = fbcursor.fetchall()
  countp = 0
  for i in termt:
      termtree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[3]))
      countp += 1
  entrytopstr = StringVar()
  entrytop = Entry(firsttab,width=25,textvariable=entrytopstr)
  entrytop.place(x=495,y=208)
  entrydsstr = StringVar()
  entryds = Entry(firsttab,textvariable=entrydsstr)
  entryds.place(x=670,y=208)
  bttermadd = Button(firsttab,text="Add new line",command=insert_valueterm)
  bttermadd.place(x=800,y=205)
  bttermedit = Button(firsttab,text="     Edit line  ",command=save_valueterm)
  bttermedit.place(x=890,y=205)
  bttermdel = Button(firsttab,text="  Delete line  ",command=del_valueterm)
  bttermdel.place(x=890,y=240)
  
  radem=LabelFrame(firsttab,text="Invoice/Oder/Estimate/P.order Email Attachment file type", height=60,   width=500)
  radem.place(x=480, y=340)
  radema = StringVar()
  radpdf = Radiobutton(firsttab,variable=radema,value="PDF",text='PDF')
  radpdf.place(x= 485, y= 360 )
  radhtml = Radiobutton(firsttab,variable=radema,value="HTML",text='HTML')
  radhtml.place(x= 660, y= 360 )
  if  not sectab:
    pass
  else:
    if sectab[22] == 'PDF':
      radpdf.select()
    elif sectab[22] == 'HTML':
      radhtml.select()
    else:
      pass
  
  checkb1 = IntVar()
  check1 = Checkbutton(firsttab,variable = checkb1, 
                        text="PDF attachment with Embedded Fonts (PDF file size will be larger,but readable on   all devices) ", 
                        onvalue =1 ,
                        offvalue = 0,
                        )
  
  check1.place(x=480,y=400)
  if  not sectab:
    pass
  else:
    if sectab[23] == 1:
      check1.select()
    else:
      check1.deselect()
  
  checkb2 = IntVar()
  check2 = Checkbutton(firsttab,variable = checkb2, 
                        text="invoice numbering with leading zero and current year", 
                        onvalue =1 ,
                        offvalue = 0,
                       )
  
  check2.place(x=480,y=420)
  if  not sectab:
    pass
  else:
    if sectab[24] == 1:
      check2.select()
    else:
      check2.deselect()
  
  checkb3 = IntVar()
  check3 = Checkbutton(firsttab,variable = checkb3, 
                        text="Order numbering with leading zero and current year", 
                        onvalue =1 ,
                        offvalue = 0,
                        )
  
  check3.place(x=480,y=440)
  if  not sectab:
    pass
  else:
    if sectab[25] == 1:
      check3.select()
    else:
      check3.deselect()
  
  checkb4 = IntVar()
  check4 = Checkbutton(firsttab,variable = checkb4, 
                        text="Estimate numbering with leading zero and current year", 
                        onvalue =1 ,
                        offvalue = 0,
                       )
  
  check4.place(x=480,y=460)
  if  not sectab:
    pass
  else:
    if sectab[26] == 1:
      check4.select()
    else:
      check4.deselect()
  
  checkb5 = IntVar()
  check5 = Checkbutton(firsttab,variable = checkb5, 
                        text="Purchsae order numbering with leading zero and current year", 
                        onvalue =1 ,
                        offvalue = 0,
                        )
  check5.place(x=480,y=480)
  if  not sectab:
    pass
  else:
    if sectab[27] == 1:
      check5.select()
    else:
      check5.deselect()
  
  checkb6 = IntVar()
  check6 = Checkbutton(firsttab,variable = checkb6, 
                        text="Confirmation before closing F-billing Revolution", 
                        onvalue =1 ,
                        offvalue = 0,
                      )
  
  check6.place(x=480,y=500)
  if  not sectab:
    pass
  else:
    if sectab[28] == 1:
      check6.select()
    else:
      check6.deselect()
  
  ################### tab02 ###################################
  sql = "select * from company"
  fbcursor.execute(sql)
  sectab = fbcursor.fetchone()
  print(sectab)
  
  
  secondtab1=Frame(tab02, relief=GROOVE, bg="#f8f8f2")
  secondtab1.pack(side="top", fill=BOTH)
  
  secondtab=Frame(secondtab1, bg="#f5f3f2", height=700)
  secondtab.pack(side="top", fill=BOTH)
  
  comdata=LabelFrame(secondtab,text="Company data", height=200, width=500)
  comdata.place(x=5, y=15)
  cname = Label(secondtab,text="Company name")
  cname.place(x=20, y =35)
  comname = StringVar()
  centry = Entry(secondtab,textvariable=comname)
  if  not sectab:
    pass
  else:
    centry.insert(0, sectab[1])
  centry.place(x=160,y=35,width=280)
  
  
  cadd = Label(secondtab,text="Company Address")
  cadd.place(x=20, y =65)
  caddent = scrolledtext.ScrolledText(secondtab)
  if  not sectab:
    pass
  else:
    caddent.insert('1.0', sectab[2])
  caddent.place(x=160,y=65,height=80,width=280)
  
  cemail = Label(secondtab,text="E-mail Address")
  cemail.place(x=20, y =160)
  comemail = StringVar()
  cemailentry = Entry(secondtab,textvariable=comemail)
  if  not sectab:
    pass
  else:
    cemailentry.insert(0, sectab[3])
  cemailentry.place(x=160,y=160,width=280)
  
  stl = Label(secondtab,text="sales Tax.Reg.No.")
  stl.place(x=20, y =185)
  comsalestax = StringVar()
  ste = Entry(secondtab,textvariable=comsalestax)
  if  not sectab:
    pass
  else:
    ste.insert(0, sectab[4])
  ste.place(x=160,y=185,width=280)
  
  
  curre=LabelFrame(secondtab,text="Currency", height=125, width=500)
  curre.place(x=5, y=220)
  currl = Label(secondtab,text="Currency")
  currl.place(x=20,y= 240)
  comcur = StringVar()
  currbox = ttk.Combobox(secondtab,width=10,textvariable=comcur)
  currbox['values'] =('ALL','AFN','ARS','AWG','AUD','AZN','BSD','BBD','BYN','BZD','BMD','BOB','BAM','BWP',  'BGN','BRL','BND','KHR','CAD','KYD','CLP','CNY','COP','CRC','HRK','CUP','CZK','DKK','DOP','XCD','EGP','SVC',  'EUR','FKP','FJD','GHS','GIP','GTQ','GGP','GYD','HNL','HKD','HUF','ISK','INR','IDR','IRR','IMP','ILS','JMD',  'JPY','JEP','KZT','KPW','KRW','KGS','LAK','LBP','LRD','MKD','MYR','MUR','MXN','MNT','MNT','MZN','NAD','NPR',  'ANG','NZD','NIO','NGN','NOK','OMR','PKR','PAB','PYG','PEN','PHP','PLN','QAR','RON','RUB','SHP','SAR','RSD',  'SCR','SGD','SBD','SOS','KRW','ZAR','LKR','SEK','CHF','SRD','SYP','TWD','THB','TTD','TRY','TVD','UAH','AED',  'GBP','USD','UYU','UZS','VEF','VND','YER','ZWD',)
  if  not sectab:
    pass
  elif sectab[5]:
    currbox.insert(0, sectab[5])
  currbox.place(x=80,y=240)
  
  def signpl(event):
    amsgpl = comcursignpla.get()
    currsign = comcursign.get()
    if amsgpl == "before amount":
      exbox.delete(0, END)
      exbox.insert(0, currsign+'8347.26')
    elif amsgpl == "after amount":
      exbox.delete(0, END)
      exbox.insert(0, '8347.26'+currsign)
    elif amsgpl == "before amount with space":
      exbox.delete(0, END)
      exbox.insert(0, currsign+'  8347.26')
    elif amsgpl == "after amount with space":
      exbox.delete(0, END)
      exbox.insert(0, '8347.26  '+currsign)
  
  
  currsignl = Label(secondtab,text="Currency sign")
  currsignl.place(x=180,y=240)
  comcursign = StringVar()
  currsignbox = ttk.Combobox(secondtab,width=10,textvariable=comcursign)
  currsignbox.bind("<<ComboboxSelected>>", signpl)
  currsignbox["values"] = ('Lek','؋','$','ƒ','$','₼','$','$','Br','BZ$','$','$b','KM','P','лв','R$','$','៛',  '$','$','$','¥','$','₡','kn','₱','Kč','kr','RD$','$','£','$','€','£','$','¢','£','Q','£','$','L','$','Ft',  'kr','₹','Rp','﷼','£','₪','J$','¥','£','лв','₩','₩','₭','£','$','ден','RM','₨','$','₮',' د.إ','MT','$','₨',  'ƒ','$','C$','₦','kr','﷼','₨','B/.','Gs','S/.','₱','zł','﷼','lei','₽','£','﷼','Дин.','₨','S','₩','R','₨',  'kr','CHF','£','NT$','฿','TT$','₺','$','₴','د.إ','$U','лв','Bs','₫','﷼','Z$')
  if  not sectab:
    pass
  elif sectab[6]:
    currsignbox.insert(0, sectab[6])
  currsignbox.place(x=265,y=240)
  
  cspl = Label(secondtab,text="Currency sign placement")
  cspl.place(x=20,y=270)
  
  def amountsignspace(event):
    amsgpl = comcursignpla.get()
    currsign = comcursign.get()
    if amsgpl == "before amount":
      exbox.delete(0, END)
      exbox.insert(0, currsign+'8347.26')
    elif amsgpl == "after amount":
      exbox.delete(0, END)
      exbox.insert(0, '8347.26'+currsign)
    elif amsgpl == "before amount with space":
      exbox.delete(0, END)
      exbox.insert(0, currsign+'  8347.26')
    elif amsgpl == "after amount with space":
      exbox.delete(0, END)
      exbox.insert(0, '8347.26  '+currsign)
    
      
      
  comcursignpla = StringVar()
  cspe = ttk.Combobox(secondtab,width=24,textvariable=comcursignpla,)
  cspe.bind("<<ComboboxSelected>>", amountsignspace)
  cspe["values"] = ("before amount","after amount",'before amount with space',"after amount with space")
  if  not sectab:
    pass
  elif sectab[7]:
    cspe.insert(0, sectab[7])
  cspe.place(x=180,y=270)
  
  def decpl(event):
    dec = comdecsep.get()
    ex = comex.get()
    if dec == ",":
      var = str.replace(ex,".",",")
      exbox.delete(0, END)
      exbox.insert(0, var)
    elif dec == ".":
      var1 = str.replace(ex,",",".")
      exbox.delete(0, END)
      exbox.insert(0, var1)
  dsl = Label(secondtab,text="Decimal separator")
  dsl.place(x=20,y=300)
  comdecsep = StringVar()
  currbox = ttk.Combobox(secondtab,width=5,textvariable=comdecsep)
  currbox.bind("<<ComboboxSelected>>",decpl)
  currbox['values'] = ('.',',')
  if  not sectab:
    pass
  elif sectab[8]:
    currbox.insert(0, sectab[8])
  currbox.place(x=130,y=300)
  
  exl = Label(secondtab,text="Example")
  exl.place(x=185,y=300)
  comex = StringVar()
  exbox = Entry(secondtab,width=15,textvariable=comex)
  if  not sectab:
    exbox.insert(0, 84367.26)
  elif sectab[9]:
    exbox.insert(0, sectab[9])
  exbox.place(x=245,y=300)
  
  btred = Button(secondtab,text="Restore Default")
  btred.place(x=400,y=270)
  btsc = Button(secondtab,text="SET CURRENCY")
  btsc.place(x=400,y=300)
  
  datef=LabelFrame(secondtab,text="Date format", height=60, width=500)
  datef.place(x=5, y=355)
  
  def daffun(event):
    dafget = daf.get()
    if dafget == "mm-dd-yyyy":
      exd._set_text(exd._date.strftime('%m-%d-%Y'))
    elif dafget == "dd-mm-yyyy":
      exd._set_text(exd._date.strftime('%d-%m-%Y'))
    elif dafget == "yyy.mm.dd":
      exd._set_text(exd._date.strftime('%Y.%m.%d'))
    elif dafget == "mm/dd/yyyy":
      exd._set_text(exd._date.strftime('%m/%d/%Y'))
    elif dafget == "dd/mm/yyy":
      exd._set_text(exd._date.strftime('%d/%m/%Y'))
    elif dafget == "dd.mm.yyyy":
      exd._set_text(exd._date.strftime('%d.%m.%Y'))
    elif dafget == "yyyy/mm/dd":
      exd._set_text(exd._date.strftime('%Y/%m/%d'))
    
  
  comdaf = StringVar()
  daf = ttk.Combobox(secondtab,textvariable=comdaf)
  daf["values"] = ("Default",'mm-dd-yyyy','dd-mm-yyyy','yyy.mm.dd','mm/dd/yyyy','dd/mm/yyy','dd.mm.yyyy','yyyy/  mm/dd')
  daf.bind("<<ComboboxSelected>>",daffun)
  if not sectab:
    pass
  elif sectab[10]:
    daf.insert(0, sectab[10])
  daf.place(x=60,y=380)
  
  
  exd = DateEntry(secondtab,)
  exd.place(x=280,y=380)
  if  not sectab:
    pass
  elif sectab[11]:
    exd.delete(0, END)
    exd.insert(0, sectab[11])
  
  tnr=LabelFrame(secondtab,text="Tax name and rate", height=200, width=500)
  tnr.place(x=560, y=15)
  
  stt=LabelFrame(secondtab,text="Select tax type", height=120, width=180)
  stt.place(x=580, y=30)
  def rtax1():
    ch = radtax.get()
    if ch == 1:
      tax1namel.place_forget()
      tax1namee.place_forget()
      tax1ratel.place_forget()
      tax1ratee.place_forget()
      tax1ratee.place_forget()
      ptax1.place_forget()
  
      tax2namel.place_forget()
      tax2namee.place_forget()
      tax2ratel.place_forget()
      tax2ratee.place_forget()
      ptax2.place_forget()
    elif ch == 2:
      tax1namel.place(x=800, y=40)
      tax1namee.place(x=880,y=40)
      tax1ratel.place(x=800, y=70)
      tax1ratee.place(x=880,y=70)
      ptax1.place(x=580,y=160)
      tax2namel.place_forget()
      tax2namee.place_forget()
      tax2ratel.place_forget()
      tax2ratee.place_forget()
      ptax2.place_forget()
    elif ch == 3:
      tax1namel.place(x=800, y=40)
      tax1namee.place(x=880,y=40)
      tax1ratel.place(x=800, y=70)
      tax1ratee.place(x=880,y=70)
      ptax1.place(x=580,y=160)
      tax2namel.place(x=800, y=110)
      tax2namee.place(x=880,y=110)
      tax2ratel.place(x=800, y=140)
      tax2ratee.place(x=880,y=140)
      ptax2.place(x=580,y=185)
    
  radtax = IntVar()
  rdnotax = Radiobutton(secondtab,text="Do not use TAX",value="1",variable=radtax,command=rtax1)
  rdnotax.place(x=590,y=50)
  
  
  rdtax1 = Radiobutton(secondtab,text="1 level of Tax",value="2",variable=radtax,command=rtax1)
  rdtax1.place(x=590,y=80)
  ptax01 = IntVar()
  tax1namel = Label(secondtab,text="Tax1 name")
  
  
  tax1namee = Entry(secondtab)
  if  not sectab:
    pass
  elif sectab[15]:
    tax1namee.insert(0, sectab[15])
  tax1namee.place(x=60,y=380)
  
  
  tax1ratel = Label(secondtab,text="Tax1 rate")
  
  
  tax1ratee = Entry(secondtab)
  if  not sectab:
    pass
  elif sectab[16]:
    tax1ratee.insert(0, sectab[16])
  
  comptax1 = BooleanVar()
  ptax1 = Checkbutton(secondtab,text="Print TAX1" ,onvalue =1 ,offvalue = 0,variable=comptax1)
  if  not sectab:
    pass
  elif sectab[17] == 1:
    ptax1.select()
  else:
    ptax1.deselect()
  
  rdtax2 = Radiobutton(secondtab,text="2 level of Tax",value="3",variable=radtax,command=rtax1)
  rdtax2.place(x=590,y=110)
  
  
  tax2namel = Label(secondtab,text="Tax2 name")
  
  
  tax2namee = Entry(secondtab)
  if  not sectab:
    pass
  elif sectab[18]:
    tax2namee.insert(0, sectab[18])
  
  tax2ratel = Label(secondtab,text="Tax2 rate")
  
  tax2ratee = Entry(secondtab)
  if  not sectab:
    pass
  elif sectab[19]:
    tax2ratee.insert(0, sectab[19])
  
  comptax2 = BooleanVar()
  ptax2 = Checkbutton(secondtab,text="Print TAX2" ,onvalue =1 ,offvalue = 0,variable=comptax2)
  if  not sectab:
    pass
  else:
    if sectab[20] == 1:
      ptax2.select()
    else:
      ptax2.deselect()
  
  if  not sectab:
    pass
  else:
    if sectab[12] == "1":
      rdnotax.select()
      tax1namel.place_forget()
      tax1namee.place_forget()
      tax1ratel.place_forget()
      tax1ratee.place_forget()
      tax1ratee.place_forget()
      ptax1.place_forget()
  
      tax2namel.place_forget()
      tax2namee.place_forget()
      tax2ratel.place_forget()
      tax2ratee.place_forget()
      ptax2.place_forget()
    elif sectab[12] == "2":
      tax1namel.place(x=800, y=40)
      tax1namee.place(x=880,y=40)
      tax1ratel.place(x=800, y=70)
      tax1ratee.place(x=880,y=70)
      ptax1.place(x=580,y=160)
      tax2namel.place_forget()
      tax2namee.place_forget()
      tax2ratel.place_forget()
      tax2ratee.place_forget()
      ptax2.place_forget()
      rdtax1.select()
    elif sectab[12] == "3":
      rdtax2.select()
      tax1namel.place(x=800, y=40)
      tax1namee.place(x=880,y=40)
      tax1ratel.place(x=800, y=70)
      tax1ratee.place(x=880,y=70)
      ptax1.place(x=580,y=160)
      tax2namel.place(x=800, y=110)
      tax2namee.place(x=880,y=110)
      tax2ratel.place(x=800, y=140)
      tax2ratee.place(x=880,y=140)
      ptax2.place(x=580,y=185)
    else:
      pass
  
  
  comlo=LabelFrame(secondtab,text="Comapny Logo", height=260, width=320)
  comlo.place(x=560, y=240)
  
  def upload_filelogo():
    global imglogo,filename
    f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
    image = Image.open(filename)
    resize_image = image.resize((280, 160))
    imglogo = ImageTk.PhotoImage(resize_image)
    # b2 = Button(secondtab,image=img)
    # b2.place(x=130, y=80)
  
    btlogo = Button(secondtab,width=280,height=160,image=imglogo)
    btlogo.place(x=580,y=280)
  
  try:
    image = Image.open("images/"+sectab[13])
    resize_image = image.resize((280, 160))
    image = ImageTk.PhotoImage(resize_image)
    btlogo = Button(secondtab,width=280,height=160,image=image)
    btlogo.place(x=580,y=280)
    btlogo.photo = image
  except:
    pass
  
    
  btloadim = Button(secondtab,text="Load logo image",command=upload_filelogo)
  btloadim.place(x=580,y=460)
  
  compimg = BooleanVar()
  primage = Checkbutton(secondtab,text="Print logo image",variable = compimg,onvalue =1 ,offvalue = 0)
  primage.place(x=740,y=460)

  
  ################### tab06 ###################################
  
  def user():
    display = displaystart.get()
    user_name = usernae.get()
    password = userpase.get()
    conformpassword = usercpase.get()
   
    create_inv = creinvbol.get()
    delete_inv = delinvbol.get()
    void_inv = voinvbol.get()
    mark_inv_as_paid = markinvbol.get()
    
    create_ord = creordbol.get()
    delete_ord = delordbol.get()
    turn_inv_ord = turninvbol.get()
    smsnofi = smsinvbol.get()
    
    create_est = creestimatebol.get()
    delete_est = delestimatebol.get()
    turn_est = turnestiinvbol.get()
  
    create_exp = creexpensebol.get()
    delete_exp = delexpensebol.get()
    rebill_exp = rebillexpebol.get()
    
    create_cus = crecusbol.get()
    delete_cus = delcusbol.get()
    imp_cus = impcusbol.get()
  
    create_pros = creprosbol.get()
    delete_pros = delprosbol.get()
    import_pros = impprosbol.get()
  
    runrep = runrepbol.get()
    gen_rec = genrecinvbol.get()
  
    create_pur = crepurbol.get()
    delete_pur = delpurbol.get()
  
    modify_inv = modifyinvbol.get()
    modify_ord = modifyordbol.get()
    modify_est = modifyestibol.get()
  
    if user_name=="" or password=="":
      messagebox.showerror('',"Please complete the form")
    else:
      sql='SELECT * FROM users WHERE username=%s'# selecting entire table from db,taking username , nd check   the existance
      val=(user_name,)
      fbcursor.execute(sql,val)
      if fbcursor.fetchone()is not None:
        sql='SELECT * FROM users WHERE username=%s'
        val=(user_name,)
        fbcursor.execute(sql,val)
        whuser = fbcursor.fetchone()
        print(whuser[0])
        if password == conformpassword:
          if user_name == "adminstator":
            sqll= 'UPDATE users SET displayloginscreen=%s,username=%s,password=%s,confirm_password=%s WHERE userID=%s'
            vall=(display,user_name,password,conformpassword,whuser[0])
            fbcursor.execute(sqll,vall)
            fbilldb.commit()
          else:
            sqll= 'UPDATE users SET displayloginscreen=%s,username=%s,password=%s,confirm_password=%s,create_invoice=%s,delete_invoice=%s,void_invoice=%s,mark_invoice_as_paid=%s,create_order=%s,delete_order=%s,turn_order_into_invoice=%s,send_sms_nofitication=%s,create_estimate=%s,delete_estimate=%s,turn_oestimate_into_invoice=%s,create_expense=%s,delete_expense=%s,rebill_exprense=%s,create_customer=%s,delete_customer=%s,import_customer=%s,	create_product_service=%s,delete_product_service=%s,import_product_service=%s,run_reports=%s,generate_recurring_invoice=%s,create_purchase_order=%s,delete_purchase_order=%s,modify_invoice_settings=%s,modify_order_settings=%s,modify_estimate_settings=%s WHERE userID=%s'
            vall=(display,user_name,password,conformpassword,create_inv,delete_inv,void_inv,mark_inv_as_paid,  create_ord,delete_ord,turn_inv_ord,smsnofi,create_est,delete_est,turn_est,create_exp,delete_exp,  rebill_exp,create_cus,delete_cus,imp_cus,create_pros,delete_pros,import_pros,runrep,gen_rec,create_pur,  delete_pur,modify_inv,modify_ord,modify_est,whuser[0])
            fbcursor.execute(sqll,vall)
            fbilldb.commit()
        else:
          messagebox.showerror('Warming','Password not match!!')
      else:
        if password == conformpassword:
          if user_name == "adminstator":
            sql="INSERT INTO users(displayloginscreen,username,password,confirm_password,create_invoice,  delete_invoice,void_invoice,mark_invoice_as_paid,create_order,delete_order,turn_order_into_invoice,  send_sms_nofitication,create_estimate,delete_estimate,turn_oestimate_into_invoice,	create_expense,	  delete_expense,rebill_exprense,create_customer,delete_customer,import_customer,	create_product_service,  delete_product_service,	import_product_service,run_reports,generate_recurring_invoice,  create_purchase_order,delete_purchase_order,modify_invoice_settings,modify_order_settings,  modify_estimate_settings) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,  %s,%s,%s,%s,%s,%s,%s,%s)" #adding values into db
            val=(display,user_name,password,conformpassword,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
            fbcursor.execute(sql,val)
            fbilldb.commit()
            for record in uactree.get_children():
              uactree.delete(record)
            sql = "select * from users"
            fbcursor.execute(sql)
            sixuactree = fbcursor.fetchall()
            coutset = 0
            for i in sixuactree:
             uactree.insert(parent='', index='end', iid=coutset, text='hello', values=(i[3]))
             coutset += 1
          else:
            sql="INSERT INTO users(displayloginscreen,username,password,confirm_password,create_invoice,  delete_invoice,void_invoice,mark_invoice_as_paid,create_order,delete_order,turn_order_into_invoice,  send_sms_nofitication,create_estimate,delete_estimate,turn_oestimate_into_invoice,	create_expense,	  delete_expense,rebill_exprense,create_customer,delete_customer,import_customer,	create_product_service,  delete_product_service,	import_product_service,run_reports,generate_recurring_invoice,  create_purchase_order,delete_purchase_order,modify_invoice_settings,modify_order_settings,  modify_estimate_settings) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,  %s,%s,%s,%s,%s,%s,%s,%s)" #adding values into db
            val=(display,user_name,password,conformpassword,create_inv,delete_inv,void_inv,mark_inv_as_paid,  create_ord,delete_ord,turn_inv_ord,smsnofi,create_est,delete_est,turn_est,create_exp,delete_exp,  rebill_exp,create_cus,delete_cus,imp_cus,create_pros,delete_pros,import_pros,runrep,gen_rec,create_pur,  delete_pur,modify_inv,modify_ord,modify_est)
            fbcursor.execute(sql,val)
            fbilldb.commit()
            for record in uactree.get_children():
              uactree.delete(record)
            sql = "select * from users"
            fbcursor.execute(sql)
            sixuactree = fbcursor.fetchall()
            coutset = 0
            for i in sixuactree:
             uactree.insert(parent='', index='end', iid=coutset, text='hello', values=(i[3]))
             coutset += 1
        else:
          messagebox.showerror('Warming','Password not match!!')
        

   
    
  
  
  
  
    
  
    
  sixtab1=Frame(tab06, relief=GROOVE, bg="#f8f8f2")
  sixtab1.pack(side="top", fill=BOTH)
  
  sixtab=Frame(sixtab1, bg="#f5f3f2", height=700)
  sixtab.pack(side="top", fill=BOTH)
  
  displaystart = BooleanVar()
  displaylocsc = Checkbutton(sixtab,text="Display Login screen startup",onvalue =1 ,offvalue = 0,  variable=displaystart)
  displaylocsc.place(x=20,y=30)
  
  userac=LabelFrame(sixtab,text="User Acounts", height=400, width=260)
  userac.place(x=20, y=55)
  
  
  selper = Label(sixtab,text="Select username to modify permissions")
  selper.place(x=30,y=75)
  
  def focususer(event):
    itemid = uactree.item(uactree.focus())["values"][0]
    sql = "select * from users where username = %s"
    val = (itemid,)
    fbcursor.execute(sql,val)
    sixtabdataback = fbcursor.fetchone()
    print(sixtabdataback)
    usernae.delete(0,END)
    usernae.insert(0,itemid)
    if itemid == "adminstator":
        usernae.delete(0,END)
        usernae.insert(0,itemid)
        usernae["state"] = DISABLED
        creinv["state"] = DISABLED
        delinv["state"] = DISABLED
        voinv["state"] = DISABLED
        markinv["state"] = DISABLED
        creord["state"] = DISABLED
        delord["state"] = DISABLED
        turninv["state"] = DISABLED
        smsinv["state"] = DISABLED
        creestimate["state"] = DISABLED
        delestimate["state"] = DISABLED
        turnestiinv["state"] = DISABLED
        creexpense["state"] = DISABLED
        delexpense["state"] = DISABLED
        rebillexpe["state"] = DISABLED
        crecus["state"] = DISABLED
        delcus["state"] = DISABLED
        impcus["state"] = DISABLED
        crepros["state"] = DISABLED
        delpros["state"] = DISABLED
        imppros["state"] = DISABLED
        runrep["state"] = DISABLED
        genrecinv["state"] = DISABLED
        crepur["state"] = DISABLED
        delpur["state"] = DISABLED
        modifyinv["state"] = DISABLED
        modifyord["state"] = DISABLED
        modifyesti["state"] = DISABLED
    else:
        userpase.delete(0, END)
        usercpase.delete(0, END)
        usernae.delete(0,END)
        usernae.insert(0,itemid)
        usernae["state"] = NORMAL
        creinv["state"] = NORMAL
        delinv["state"] = NORMAL
        voinv["state"] = NORMAL
        markinv["state"] = NORMAL
        creord["state"] = NORMAL
        delord["state"] = NORMAL
        turninv["state"] = NORMAL
        smsinv["state"] = NORMAL
        creestimate["state"] = NORMAL
        delestimate["state"] = NORMAL
        turnestiinv["state"] = NORMAL
        creexpense["state"] = NORMAL
        delexpense["state"] = NORMAL
        rebillexpe["state"] = NORMAL
        crecus["state"] = NORMAL
        delcus["state"] = NORMAL
        impcus["state"] = NORMAL
        crepros["state"] = NORMAL
        delpros["state"] = NORMAL
        imppros["state"] = NORMAL
        runrep["state"] = NORMAL
        genrecinv["state"] = NORMAL
        crepur["state"] = NORMAL
        delpur["state"] = NORMAL
        modifyinv["state"] = NORMAL
        modifyord["state"] = NORMAL
        modifyesti["state"] = NORMAL
    if not sixtabdataback:
      userpase.delete(0, END)
      usercpase.delete(0, END)
      creinv.deselect()
      delinv.deselect()
      voinv.deselect()
      markinv.deselect()
      creord.deselect()
      delord.deselect()
      turninv.deselect()
      smsinv.deselect()
      creestimate.deselect()
      delestimate.deselect()
      turnestiinv.deselect()
      creexpense.deselect()
      delexpense.deselect()
      rebillexpe.deselect()
      crecus.deselect()
      delcus.deselect()
      impcus.deselect()
      crepros.deselect()
      delpros.deselect()
      imppros.deselect()
      runrep.deselect()
      genrecinv.deselect()
      crepur.deselect()
      delpur.deselect()
      modifyinv.deselect()
      modifyord.deselect()
      modifyesti.deselect()
      if itemid == "adminstator":
        usernae.delete(0,END)
        usernae.insert(0,itemid)
        usernae["state"] = DISABLED
        creinv["state"] = DISABLED
        delinv["state"] = DISABLED
        voinv["state"] = DISABLED
        markinv["state"] = DISABLED
        creord["state"] = DISABLED
        delord["state"] = DISABLED
        turninv["state"] = DISABLED
        smsinv["state"] = DISABLED
        creestimate["state"] = DISABLED
        delestimate["state"] = DISABLED
        turnestiinv["state"] = DISABLED
        creexpense["state"] = DISABLED
        delexpense["state"] = DISABLED
        rebillexpe["state"] = DISABLED
        crecus["state"] = DISABLED
        delcus["state"] = DISABLED
        impcus["state"] = DISABLED
        crepros["state"] = DISABLED
        delpros["state"] = DISABLED
        imppros["state"] = DISABLED
        runrep["state"] = DISABLED
        genrecinv["state"] = DISABLED
        crepur["state"] = DISABLED
        delpur["state"] = DISABLED
        modifyinv["state"] = DISABLED
        modifyord["state"] = DISABLED
        modifyesti["state"] = DISABLED
      else:
        userpase.delete(0, END)
        usercpase.delete(0, END)
        usernae.delete(0,END)
        usernae.insert(0,itemid)
        usernae["state"] = NORMAL
        creinv["state"] = NORMAL
        delinv["state"] = NORMAL
        voinv["state"] = NORMAL
        markinv["state"] = NORMAL
        creord["state"] = NORMAL
        delord["state"] = NORMAL
        turninv["state"] = NORMAL
        smsinv["state"] = NORMAL
        creestimate["state"] = NORMAL
        delestimate["state"] = NORMAL
        turnestiinv["state"] = NORMAL
        creexpense["state"] = NORMAL
        delexpense["state"] = NORMAL
        rebillexpe["state"] = NORMAL
        crecus["state"] = NORMAL
        delcus["state"] = NORMAL
        impcus["state"] = NORMAL
        crepros["state"] = NORMAL
        delpros["state"] = NORMAL
        imppros["state"] = NORMAL
        runrep["state"] = NORMAL
        genrecinv["state"] = NORMAL
        crepur["state"] = NORMAL
        delpur["state"] = NORMAL
        modifyinv["state"] = NORMAL
        modifyord["state"] = NORMAL
        modifyesti["state"] = NORMAL
    else:
      userpase.delete(0, END)
      usercpase.delete(0, END)
      userpase.insert(0, sixtabdataback[4])
      usercpase.insert(0, sixtabdataback[5])
      if sixtabdataback[6] == 1:
        creinv.select()
      else:
        creinv.deselect()
      if sixtabdataback[7] == 1:
        delinv.select()
      else:
        delinv.deselect()
      if sixtabdataback[8] == 1:
        voinv.select()
      else:
        voinv.deselect()
      if sixtabdataback[9] == 1:
        markinv.select()
      else:
        markinv.deselect()
      if sixtabdataback[10] == 1:
        creord.select()
      else:
        creord.deselect()
      if sixtabdataback[11] == 1:
        delord.select()
      else:
        delord.deselect()
      if sixtabdataback[12] == 1:
        turninv.select()
      else:
        turninv.deselect()
      if sixtabdataback[13] == 1:
        smsinv.select()
      else:
        smsinv.deselect()
      if sixtabdataback[14] == 1:
        creestimate.select()
      else:
        creestimate.deselect()
      if sixtabdataback[15] == 1:
        delestimate.select()
      else:
        delestimate.deselect()
      if sixtabdataback[16] == 1:
        turnestiinv.select()
      else:
        turnestiinv.deselect()
      if sixtabdataback[17] == 1:
        creexpense.select()
      else:
        creexpense.deselect()
      if sixtabdataback[18] == 1:
        delexpense.select()
      else:
        delexpense.deselect()
      if sixtabdataback[19] == 1:
        rebillexpe.select()
      else:
        rebillexpe.deselect()
      if sixtabdataback[20] == 1:
        crecus.select()
      else:
        crecus.deselect()
      if sixtabdataback[21] == 1:
        delcus.select()
      else:
        delcus.deselect()
      if sixtabdataback[22] == 1:
        impcus.select()
      else:
        impcus.deselect()
      if sixtabdataback[23] == 1:
        crepros.select()
      else:
        crepros.deselect()
      if sixtabdataback[24] == 1:
        delpros.select()
      else:
        delpros.deselect()
      if sixtabdataback[25] == 1:
        imppros.select()
      else:
        imppros.deselect()
      if sixtabdataback[26] == 1:
        runrep.select()
      else:
        runrep.deselect()
      if sixtabdataback[27] == 1:
        genrecinv.select()
      else:
        genrecinv.deselect()
      if sixtabdataback[28] == 1:
        crepur.select()
      else:
        crepur.deselect()
      if sixtabdataback[29] == 1:
        delpur.select()
      else:
        delpur.deselect()
      if sixtabdataback[30] == 1:
        modifyinv.select()
      else:
        modifyinv.deselect()
      if sixtabdataback[31] == 1:
        modifyord.select()
      else:
        modifyord.deselect()
      if sixtabdataback[32] == 1:
        modifyesti.select()
      else:
        modifyesti.deselect()
         
  
  scrollbarx = Scrollbar(sixtab, orient=HORIZONTAL)
  scrollbary = Scrollbar(sixtab, orient=VERTICAL)
  uactree = ttk.Treeview(sixtab, columns=("1"),height=400,selectmode="extended", yscrollcommand=scrollbary.  set, xscrollcommand=scrollbarx.set)
  scrollbary.config(command=uactree.yview)
  scrollbary.place(x=245,y=100,height=300)
  uactree.heading('1', text="Username",)
  uactree.column('#0', stretch=NO, minwidth=0, width=0)
  uactree.column('1', stretch=NO, minwidth=0, width=218)
  uactree.place(x=30,y=100,height=300,width=220)
  uactree.bind('<Double-Button-1>' , focususer)
  sql = "select * from users"
  fbcursor.execute(sql)
  sixuactree = fbcursor.fetchall()
  coutset = 0
  if not sixuactree:
    uactree.insert('', index='end', text='hello', values=("adminstator"))
  else:
    for i in sixuactree:
      uactree.insert(parent='', index='end', iid=coutset, text='hello', values=(i[3]))
      coutset += 1
  
  def adduser():
    uactree.insert('', index='end', text='hello', values=("Rename User"))
  
  btadd = Button(sixtab,text="Add new User",command=adduser)
  btadd.place(x=30,y=415)
  
  def users():
    itemid = uactree.item(uactree.focus())["values"][0]
    if itemid == "adminstator":
      messagebox.showerror('F-Billing Revolution', 'Cannot delete adminstator user.')
    else:
      delusermess = messagebox.askyesno("Delete user", "Are you sure to delete this user?")
      if delusermess == True:
        sql = "delete from users where username = %s"
        val = (itemid, )
        fbcursor.execute(sql, val)
        fbilldb.commit()
        for record in uactree.get_children():
          uactree.delete(record)
        sql = "select * from users"
        fbcursor.execute(sql)
        sixuactree = fbcursor.fetchall()
        coutset = 0
        for i in sixuactree:
          uactree.insert(parent='', index='end', iid=coutset, text='hello', values=(i[3]))
          coutset += 1
      else:
        pass
        
  
  btdus = Button(sixtab,text="Delete User",command=users)
  btdus.place(x=180,y=415)
  
  userpro=LabelFrame(sixtab,text="User Profile", height=400, width=750)
  userpro.place(x=300, y=55)
  
  
  userna = Label(sixtab,text="Username")
  userna.place(x=340,y=90)
  usernae = Entry(sixtab,)
  usernae.place(x=460,y=90)
  
  userpas = Label(sixtab,text="Password")
  userpas.place(x=340,y=120)
  userpase = Entry(sixtab,)
  userpase.place(x=460,y=120)
  
  usercpas = Label(sixtab,text="Confirm Password")
  usercpas.place(x=340,y=150)
  usercpase = Entry(sixtab,)
  usercpase.place(x=460,y=150)
  
  saveuserprofile = Button(sixtab,text="save user profile",command=user)
  saveuserprofile.place(x=650,y=120)
  
  creinvbol = BooleanVar()
  creinv = Checkbutton(sixtab,text="Create invoice",onvalue= 1 ,offvalue= 0,variable=creinvbol)
  creinv.place(x=340,y=200)
  delinvbol = BooleanVar()
  delinv = Checkbutton(sixtab,text="Delete invoice",onvalue= 1 ,offvalue= 0,variable=delinvbol)
  delinv.place(x=340,y=225)
  voinvbol = BooleanVar()
  voinv = Checkbutton(sixtab,text="Void invoice",onvalue= 1 ,offvalue= 0,variable=voinvbol)
  voinv.place(x=340,y=250)
  markinvbol = BooleanVar()
  markinv = Checkbutton(sixtab,text="Mark invoice as Paid",onvalue= 1 ,offvalue= 0,variable=markinvbol)
  markinv.place(x=340,y=275)
  
  creordbol = BooleanVar()
  creord = Checkbutton(sixtab,text="Create Order",onvalue= 1 ,offvalue= 0,variable=creordbol)
  creord.place(x=500,y=200)
  delordbol = BooleanVar()
  delord = Checkbutton(sixtab,text="Delete Order",onvalue= 1 ,offvalue= 0,variable=delordbol)
  delord.place(x=500,y=225)
  turninvbol = BooleanVar()
  turninv = Checkbutton(sixtab,text="Turn order into invoice",onvalue= 1 ,offvalue= 0,variable=turninvbol)
  turninv.place(x=500,y=250)
  smsinvbol = BooleanVar()
  smsinv = Checkbutton(sixtab,text="Send sms nofitication",onvalue= 1 ,offvalue= 0,variable=smsinvbol)
  smsinv.place(x=500,y=275)
  
  creestimatebol = BooleanVar()
  creestimate = Checkbutton(sixtab,text="Create estimate",onvalue= 1 ,offvalue= 0,variable=creestimatebol)
  creestimate.place(x=680,y=200)
  delestimatebol = BooleanVar()
  delestimate = Checkbutton(sixtab,text="Delete estimate",onvalue= 1 ,offvalue= 0,variable=delestimatebol)
  delestimate.place(x=680,y=225)
  turnestiinvbol = BooleanVar()
  turnestiinv = Checkbutton(sixtab,text="Turn estimates into invoice",onvalue= 1 ,offvalue= 0,  variable=turnestiinvbol)
  turnestiinv.place(x=680,y=250)
  
  creexpensebol = BooleanVar()
  creexpense = Checkbutton(sixtab,text="Create expenses",onvalue= 1 ,offvalue= 0,variable=creexpensebol)
  creexpense.place(x=880,y=200)
  delexpensebol = BooleanVar()
  delexpense = Checkbutton(sixtab,text="Delete expenses",onvalue= 1 ,offvalue= 0,variable=delexpensebol)
  delexpense.place(x=880,y=225)
  rebillexpebol = BooleanVar()
  rebillexpe = Checkbutton(sixtab,text="Rebill expenses",onvalue= 1 ,offvalue= 0,variable=rebillexpebol)
  rebillexpe.place(x=880,y=250)
  
  crecusbol = BooleanVar()
  crecus = Checkbutton(sixtab,text="Create customer",onvalue= 1 ,offvalue= 0,variable=crecusbol)
  crecus.place(x=340,y=320)
  delcusbol = BooleanVar()
  delcus = Checkbutton(sixtab,text="Delete customer",onvalue= 1 ,offvalue= 0,variable=delcusbol)
  delcus.place(x=340,y=340)
  impcusbol = BooleanVar()
  impcus = Checkbutton(sixtab,text="Import customer",onvalue= 1 ,offvalue= 0,variable=impcusbol)
  impcus.place(x=340,y=360)
  
  creprosbol = BooleanVar()
  crepros = Checkbutton(sixtab,text="Create product\services",onvalue= 1 ,offvalue= 0,variable=creprosbol)
  crepros.place(x=500,y=320)
  delprosbol = BooleanVar()
  delpros = Checkbutton(sixtab,text="Delete product\services",onvalue= 1 ,offvalue= 0,variable=delprosbol)
  delpros.place(x=500,y=340)
  impprosbol = BooleanVar()
  imppros = Checkbutton(sixtab,text="Import product\services",onvalue= 1 ,offvalue= 0,variable=impprosbol)
  imppros.place(x=500,y=360)
  
  runrepbol = BooleanVar()
  runrep = Checkbutton(sixtab,text="Run reports",onvalue= 1 ,offvalue= 0,variable=runrepbol)
  runrep.place(x=680,y=320)
  genrecinvbol = BooleanVar()
  genrecinv = Checkbutton(sixtab,text="Generate recurring invoices",onvalue= 1 ,offvalue= 0,  variable=genrecinvbol)
  genrecinv.place(x=680,y=340)
  
  crepurbol = BooleanVar()
  crepur = Checkbutton(sixtab,text="Create Purchase order",onvalue =1 ,offvalue = 0,variable=crepurbol)
  crepur.place(x=880,y=320)
  delpurbol = BooleanVar()
  delpur = Checkbutton(sixtab,text="Delete Purchase order",onvalue =1 ,offvalue = 0,variable=delpurbol)
  delpur.place(x=880,y=340)
  
  undersetlab = Label(sixtab,text="Under Settings menu tab")
  undersetlab.place(x=340,y=400)
  
  modifyinvbol = BooleanVar()
  modifyinv = Checkbutton(sixtab,text="Modify invoice settings",onvalue =1 ,offvalue = 0,variable=modifyinvbol)
  modifyinv.place(x=340,y=425)
  
  modifyordbol = BooleanVar()
  modifyord = Checkbutton(sixtab,text="Modify order settings",onvalue =1 ,offvalue = 0,variable=modifyordbol)
  modifyord.place(x=500,y=425)
  
  modifyestibol = BooleanVar()
  modifyesti = Checkbutton(sixtab,text="Modify estimate settings",onvalue =1 ,offvalue = 0,  variable=modifyestibol)
  modifyesti.place(x=680,y=425)

  ################### tab05 ###################################
  fifthtab1=Frame(tab05, relief=GROOVE, bg="#f8f8f2")
  fifthtab1.pack(side="top", fill=BOTH)

  fifthtab=Frame(fifthtab1, bg="#f5f3f2", height=700)
  fifthtab.pack(side="top", fill=BOTH)

  sql = "select * from company"
  fbcursor.execute(sql)
  estdata = fbcursor.fetchone()
  print(estdata)



  ver = Label(fifthtab,text="Estimate# prefix")
  ver.place(x=5,y=40)

  est_str = StringVar() 
  est_entry = Entry(fifthtab, textvariable=est_str)
  est_entry.place(x=100,y=40)
  if not estdata:
    est_str.set('EST')
  else:
    est_entry.insert(0, estdata[29])

  ver = Label(fifthtab,text="Starting estimate number")
  ver.place(x=25,y=80)

  def callback(input):
      
    if input.isdigit():
        print(input)
        return True
                          
    elif input is "":
        print(input)
        return True
  
    else:
        print(input)
        return False

  spin1 = Spinbox(fifthtab,from_=0,to=1000000,width=15)
  reg = fifthtab.register(callback)
  
  spin1.config(validate ="key", 
         validatecommand =(reg, '%S'))
  if not estdata:
    pass
  else:
    spin1.delete(0, END)
    spin1.insert(0,estdata[38])
  spin1.place(x=50,y=100)

  ver = Label(fifthtab,text="Header box background color")
  ver.place(x=5,y=140)

  win_menu1 = StringVar()
  winstyle1 = ttk.Combobox(fifthtab,textvariable=win_menu1)
  #est_win1 = win_menu1.get()
  winstyle1['values'] = ('Default','Black','Maroon','Green','Olive','Navy','Purple','Teal','Gray','Silver','Red','Lime','Yellow','Blue','Fuchsia','Aqua','White','ScrollBar','Background','ActiveCaption','InactiveCaption','Menu','Window','WindowFrame','MenuText','WindowText','CaptionText','ActiveBorder','InactiveBorder','AppWorkSpace','Highlight','HighlightText','BtnFace','InactiveCaptionText','BtnHighlight','3DDkShadow','3DLight','InfoText','InfoBk','Custom')
  if not estdata:
    winstyle1.current(0)
  else:
    winstyle1.insert(0, estdata[30])
  winstyle1.place(x=6 ,y=160)
  #winstyle1.current(0)

  ver = Label(fifthtab,text="Customize Estimate text labels")
  ver.place(x=5,y=190)
  
  est_str1 = StringVar() 
  est_lbx1 = Entry(fifthtab, width=30,textvariable=est_str1)
  # est_str1.set('Estimate')
  if not estdata:
    est_str1.set('Estimate')
  else:
    est_lbx1.insert(0, estdata[31])
  est_lbx1.place(x=5,y=220)
  
  est_str2 = StringVar() 
  est_lbx2 = Entry(fifthtab, width=30,textvariable=est_str2)
  if not estdata:
    est_str2.set('Estimate#')
  else:
    est_lbx2.insert(0,estdata[33])
  est_lbx2.place(x=5,y=240)
  
  
  est_str3 = StringVar() 
  est_lbx3 = Entry(fifthtab,width=30,textvariable=est_str3)
  if not estdata:
    est_str3.set('Estimate date')
  else:
    est_lbx3.insert(0, estdata[34])
  est_lbx3.place(x=5,y=260) 

  est_str4 = StringVar() 
  est_lbx4 = Entry(fifthtab,width=30,textvariable=est_str4)
  if not estdata:
    est_str4.set('Due date')
  else:
    est_lbx4.insert(0, estdata[35])
  est_lbx4.place(x=5,y=280)

  est_str5 = StringVar() 
  est_lbx5 = Entry(fifthtab,width=30,textvariable=est_str5)
  if not estdata:
    est_str5.set('Estimate to')
  else:
    est_lbx5.insert(0, estdata[36])
  est_lbx5.place(x=5,y=300)

  est_str6 = StringVar() 
  est_lbx6 = Entry(fifthtab, width=30,textvariable=est_str6)
  if not estdata:
    est_str6.set('Estimate total')
  else:
    est_lbx6.insert(0, estdata[37])
  est_lbx6.place(x=5,y=320)


  ver = Label(fifthtab,text="Default Estimate template(example,click on preview for mouse scrolling)")
  ver.place(x=248,y=55 )

  ver = Label(fifthtab,text="Default Estimate template")
  ver.place(x=619,y=40)



  messagelbframe=LabelFrame(fifthtab,text="Predefined terms and conditions text for estimates", height=70, width=980)
  messagelbframe.place(x=248, y=396)

  
  # est_str7 = StringVar() 
  # entry1=Entry(fifthtab, width=155,textvariable=est_str7)
  # if not estdata:
  #   pass
  # else:
  #   entry1.insert(0, estdata[39])
  # entry1.place(x=260, y=415, height=36)
  
  est_str7 = scrolledtext.ScrolledText(fifthtab)
  if  not estdata:
    pass
  else:
    est_str7.insert('1.0', estdata[39])
  est_str7.place(x=260,y=415,height=38,width=950)


  def restore_defaulttt1():
        est_lbx1.delete(0, 'end')
        est_lbx1.insert(0, 'Estimate')
        est_lbx2.delete(0, 'end')
        est_lbx2.insert(0,'Estimate#')
        est_lbx3.delete(0, 'end')
        est_lbx3.insert(0, 'Estimate date')
        est_lbx4.delete(0, 'end')
        est_lbx4.insert(0, 'Due date')
        est_lbx5.delete(0, 'end')
        est_lbx5.insert(0, 'Estimate to')
        est_lbx6.delete(0, 'end')
        est_lbx6.insert(0, 'Estimate total')

  bttermadd_01 = Button(fifthtab,text="Restore defaults", command=restore_defaulttt1)
  bttermadd_01.place(x=32,y=430)


#------------Professional 1 (logo on left side)-------------
  def maindropmenu(event):
      menuvar=win_menu2.get()
      print(menuvar,"hello")
      sql = "select * from company"
      fbcursor.execute(sql)
      estdata1 = fbcursor.fetchone()

      if menuvar == 'Professional 1 (logo on left side)':
        frame = Frame(fifthtab, width=953, height=300)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=247,y=90)
        canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
              
        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
          
        canvas.config(width=953,height=300)
        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(100, 8, 850, 687 , outline='yellow',fill='white')
        canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        try:
          est_image = Image.open("images/"+estdata1[13])
          est_resize_image = est_image.resize((200,100))
          est_image = ImageTk.PhotoImage(est_resize_image)

          est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
          window_image = canvas.create_window(175, 45, anchor="nw", window=est_btlogo)
          est_btlogo.photo = est_image
        except:
          pass  
        canvas.create_text(202, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(215, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(200, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
        canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
        canvas.create_text(350, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))
          
        canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
        # canvas.create_text(700, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'), width=125)
        T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
        T_address.tag_configure('tag_name',justify='right')
        T_address.insert('1.0', estdata1[2])
        T_address.tag_add('tag_name','1.0', 'end')
        T_address_window = canvas.create_window(520, 80, anchor="nw", window=T_address)
        canvas.create_text(695, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
        canvas.create_text(700, 205, text=" "+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
        canvas.create_text(706, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
          
        canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
      
        s = ttk.Style()
        s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

        tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')

        tree.column("# 1", anchor=E, stretch=NO, width=100)
        tree.heading("# 1", text="ID/SKU")
        tree.column("# 2", anchor=E, stretch=NO, width=350)
        tree.heading("# 2", text="Product/Service - Description")
        tree.column("# 3", anchor=E, stretch=NO, width=80)
        tree.heading("# 3", text="Quantity")
        tree.column("# 4", anchor=E, stretch=NO, width=90)
        tree.heading("# 4", text="Unit Price")
        tree.column("# 5", anchor=E, stretch=NO, width=80)
        tree.heading("# 5", text="Price")
          
        window = canvas.create_window(120, 340, anchor="nw", window=tree)

        canvas.create_line(120, 390, 820, 390 )
        canvas.create_line(120, 340, 120, 365 )
        canvas.create_line(120, 365, 120, 390 )
        canvas.create_line(820, 340, 820, 540 )
        canvas.create_line(740, 340, 740, 540 )
        canvas.create_line(570, 340, 570, 540 )
        canvas.create_line(570, 415, 820, 415 )
        canvas.create_line(570, 440, 820, 440 )
        canvas.create_line(570, 465, 820, 465 )
        canvas.create_line(570, 490, 820, 490 )
        canvas.create_line(570, 515, 820, 515 )
        canvas.create_line(650, 340, 650, 390 )
        canvas.create_line(220, 340, 220, 390 )
        canvas.create_line(570, 540, 820, 540 )

        canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
        canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
    
        if comcursignpla.get() == "before amount":
          canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        elif comcursignpla.get() == "after amount":
          canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))

        else:
          pass
        # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        
        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
        else:
          pass

        # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
        
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

        canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
          
        canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas.create_line(150, 608, 795, 608)
        # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10')) 
        T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
        T.insert(END, estdata1[39])
        T_window = canvas.create_window(155, 612, anchor="nw", window=T)

        canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
          

#----------------Professional 2 (logo on right side)------------------
      elif menuvar == 'Professional 2 (logo on right side)':
        frame = Frame(fifthtab, width=953, height=300)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=247,y=90)
      
        canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
        canvas.config(width=953,height=300)
          
        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        try:
          est_image = Image.open("images/"+estdata1[13])
          est_resize_image = est_image.resize((200,100))
          est_image = ImageTk.PhotoImage(est_resize_image)

          est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
          window_image = canvas.create_window(500, 45, anchor="nw", window=est_btlogo)
          est_btlogo.photo = est_image
        except:
          pass  
        canvas.create_text(250, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
        # canvas.create_text(215, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
        T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
        T_address.tag_configure('tag_name',justify='right')
        T_address.insert('1.0', estdata1[2])
        T_address.tag_add('tag_name','1.0', 'end')
        T_address_window = canvas.create_window(100, 80, anchor="nw", window=T_address)
        #T_address_window = canvas.create_window(175, 80, anchor="nw", window=T_address)

        canvas.create_text(215, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
        canvas.create_text(225, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
        canvas.create_text(232, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
          
        canvas.create_text(502, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(515, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(500, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(491, 220, text="Terms", fill="black", font=('Helvetica 11'))
        canvas.create_text(505, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
        canvas.create_text(690, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(690, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(690, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(680, 220, text="NET 15", fill="black", font=('Helvetica 11'))      
          
        canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

        s = ttk.Style()
        s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

        tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')
          
        tree.column("# 1", anchor=E, stretch=NO, width=100)
        tree.heading("# 1", text="ID/SKU")
        tree.column("# 2", anchor=E, stretch=NO, width=350)
        tree.heading("# 2", text="Product/Service - Description")
        tree.column("# 3", anchor=E, stretch=NO, width=80)
        tree.heading("# 3", text="Quantity")
        tree.column("# 4", anchor=E, stretch=NO, width=90)
        tree.heading("# 4", text="Unit Price")
        tree.column("# 5", anchor=E, stretch=NO, width=80)
        tree.heading("# 5", text="Price")
          
        window = canvas.create_window(120, 340, anchor="nw", window=tree)

        canvas.create_line(120, 390, 820, 390 )
        canvas.create_line(120, 340, 120, 365 )
        canvas.create_line(120, 365, 120, 390 )
        canvas.create_line(820, 340, 820, 540 )
        canvas.create_line(740, 340, 740, 540 )
        canvas.create_line(570, 340, 570, 540 )
        canvas.create_line(570, 415, 820, 415 )
        canvas.create_line(570, 440, 820, 440 )
        canvas.create_line(570, 465, 820, 465 )
        canvas.create_line(570, 490, 820, 490 )
        canvas.create_line(570, 515, 820, 515 )
        canvas.create_line(650, 340, 650, 390 )
        canvas.create_line(220, 340, 220, 390 )
        canvas.create_line(570, 540, 820, 540 )

        canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
        canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
        else:
          pass

        # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
        
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

        canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

        canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas.create_line(150, 608, 795, 608)
        # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
        T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
        T.insert(END, estdata1[39])
        T_window = canvas.create_window(155, 612, anchor="nw", window=T)
        canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
#----------------Simplified 1 (logo on left side)------------------ 
      elif menuvar == 'Simplified 1 (logo on left side)':
        print('hello')
        frame = Frame(fifthtab, width=953, height=300)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=247,y=90)
        canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
        canvas.config(width=953,height=300)

        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        try:
          est_image = Image.open("images/"+estdata1[13])
          est_resize_image = est_image.resize((200,100))
          est_image = ImageTk.PhotoImage(est_resize_image)

          est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
          window_image = canvas.create_window(175, 45, anchor="nw", window=est_btlogo)
          est_btlogo.photo = est_image
        except:
          pass  
        canvas.create_text(202, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(215, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(200, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
        canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
        canvas.create_text(350, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))      

        canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
        #canvas.create_text(710, 200, text=caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
        T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
        T_address.tag_configure('tag_name',justify='right')
        T_address.insert('1.0', estdata1[2])
        T_address.tag_add('tag_name','1.0', 'end')
        T_address_window = canvas.create_window(520, 80, anchor="nw", window=T_address)

        canvas.create_text(708, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
        canvas.create_text(710, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
          
        canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

        s = ttk.Style()
        s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

        tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_1.Treeview')
          
        tree.column("# 1", anchor=E, stretch=NO, width=530)
        tree.heading("# 1", text="Product/Service - Description")
        tree.column("# 2", anchor=E, stretch=NO, width=90)
        tree.heading("# 2", text="Quantity")
        tree.column("# 3", anchor=E, stretch=NO, width=80)
        tree.heading("# 3", text="Price")
          
        window = canvas.create_window(120, 340, anchor="nw", window=tree)

        canvas.create_line(120, 390, 820, 390 )
        canvas.create_line(120, 340, 120, 365 )
        canvas.create_line(120, 365, 120, 390 )
        canvas.create_line(820, 340, 820, 540 )
        canvas.create_line(740, 340, 740, 540 )
        canvas.create_line(570, 390, 570, 540 )
        canvas.create_line(570, 415, 820, 415 )
        canvas.create_line(570, 440, 820, 440 )
        canvas.create_line(570, 465, 820, 465 )
        canvas.create_line(570, 490, 820, 490 )
        canvas.create_line(570, 515, 820, 515 )
        canvas.create_line(650, 340, 650, 390 )
        canvas.create_line(570, 540, 820, 540 )

      
        canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

        canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

        canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas.create_line(150, 608, 795, 608)
        # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
        T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
        T.insert(END, estdata1[39])
        T_window = canvas.create_window(155, 612, anchor="nw", window=T)
        canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

#----------------Simplified 2 (logo on right side)------------------ 
      elif menuvar == 'Simplified 2 (logo on right side)':
        frame = Frame(fifthtab, width=953, height=300)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=247,y=90)

        canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
        canvas.config(width=953,height=300)

        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        try:
          est_image = Image.open("images/"+estdata1[13])
          est_resize_image = est_image.resize((200,100))
          est_image = ImageTk.PhotoImage(est_resize_image)

          est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
          window_image = canvas.create_window(500, 45, anchor="nw", window=est_btlogo)
          est_btlogo.photo = est_image
        except:
          pass  
        canvas.create_text(250, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
        # canvas.create_text(224, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
        T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
        T_address.tag_configure('tag_name',justify='right')
        T_address.insert('1.0', estdata1[2])
        T_address.tag_add('tag_name','1.0', 'end')
        T_address_window = canvas.create_window(100, 80, anchor="nw", window=T_address)

        canvas.create_text(224, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
        canvas.create_text(225, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))

        canvas.create_text(502, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(515, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(500, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(491, 220, text="Terms", fill="black", font=('Helvetica 11'))
        canvas.create_text(505, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
        canvas.create_text(680, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(680, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(680, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(670, 220, text="NET 15", fill="black", font=('Helvetica 11'))      

        canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

        s = ttk.Style()
        s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

        tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_1.Treeview')
          
        tree.column("# 1", anchor=E, stretch=NO, width=530)
        tree.heading("# 1", text="Product/Service - Description")
        tree.column("# 2", anchor=E, stretch=NO, width=90)
        tree.heading("# 2", text="Quantity")
        tree.column("# 3", anchor=E, stretch=NO, width=80)
        tree.heading("# 3", text="Price")
          
        window = canvas.create_window(120, 340, anchor="nw", window=tree)

        canvas.create_line(120, 390, 820, 390 )
        canvas.create_line(120, 340, 120, 365 )
        canvas.create_line(120, 365, 120, 390 )
        canvas.create_line(820, 340, 820, 540 )
        canvas.create_line(740, 340, 740, 540 )
        canvas.create_line(570, 390, 570, 540 )
        canvas.create_line(570, 415, 820, 415 )
        canvas.create_line(570, 440, 820, 440 )
        canvas.create_line(570, 465, 820, 465 )
        canvas.create_line(570, 490, 820, 490 )
        canvas.create_line(570, 515, 820, 515 )
        canvas.create_line(650, 340, 650, 390 )
        canvas.create_line(570, 540, 820, 540 )

          
        canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

        canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

        canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas.create_line(150, 608, 795, 608)
        # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
        T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
        T.insert(END, estdata1[39])
        T_window = canvas.create_window(155, 612, anchor="nw", window=T)
        canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

#----------------Business Classic------------------ 
      elif menuvar == 'Business Classic':
        frame = Frame(fifthtab, width=953, height=300)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=247,y=90)
          
        canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
        canvas.config(width=953,height=300)
          
        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_line(150, 70, 800, 70, fill='orange')
        
        try:
          est_image = Image.open("images/"+estdata1[13])
          est_resize_image = est_image.resize((200,100))
          est_image = ImageTk.PhotoImage(est_resize_image)

          est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
          window_image = canvas.create_window(140, 120, anchor="nw", window=est_btlogo)
          est_btlogo.photo = est_image
        except:
          pass  

        canvas.create_text(500, 90, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
        # canvas.create_text(485, 220, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
        T_address = Text(canvas, height=5, width=35, font=('Helvetica 10'),borderwidth=0)
        T_address.tag_configure('tag_name',justify='right')
        T_address.insert('1.0', estdata1[2])
        T_address.tag_add('tag_name','1.0', 'end')
        T_address_window = canvas.create_window(350, 100, anchor="nw", window=T_address)
        
        canvas.create_text(480, 210, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))

        canvas.create_text(655, 100, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(696, 120, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(706, 135, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(665, 150, text="United States", fill="black", font=('Helvetica 10'))

        canvas.create_text(659, 180, text=""+est_str1.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(675, 210, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(659, 240, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))

        canvas.create_text(776, 180, text="EST1/2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(776, 210, text="05 May 2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(776, 240, text="20-05-2022", fill="black", font=('Helvetica 11'))

        s = ttk.Style()
        s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

        tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')
          
        tree.column("# 1", anchor=E, stretch=NO, width=200)
        tree.heading("# 1", text="Product/Service")
        tree.column("# 2", anchor=E, stretch=NO, width=250)
        tree.heading("# 2", text="Description")
        tree.column("# 3", anchor=E, stretch=NO, width=90)
        tree.heading("# 3", text="Unit Price")
        tree.column("# 4", anchor=E, stretch=NO, width=80)
        tree.heading("# 4", text="Quantity")
        tree.column("# 5", anchor=E, stretch=NO, width=80)
        tree.heading("# 5", text="Price")
      
        window = canvas.create_window(120, 255, anchor="nw", window=tree)

        canvas.create_line(120, 295, 820, 295 )
        canvas.create_line(120, 255, 120, 295 )
        canvas.create_line(320, 255, 320, 295 )
        canvas.create_line(570, 255, 570, 295 )
        canvas.create_line(660, 255, 660, 295 )
        canvas.create_line(740, 255, 740, 295 )
        canvas.create_line(820, 255, 820, 445 )
        canvas.create_line(570, 320, 820, 320 )
        canvas.create_line(570, 345, 820, 345 )
        canvas.create_line(570, 370, 820, 370 )
        canvas.create_line(570, 395, 820, 395 )
        canvas.create_line(570, 420, 820, 420 )
        canvas.create_line(570, 445, 820, 445 )
      
        canvas.create_text(160, 285, text="PROD-0001", fill="black", font=('Helvetica 10'))
        canvas.create_text(450, 285, text="Example product - Description text...", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(624, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(624, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(624, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(624, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(624, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(700, 285, text="1", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 310, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 310, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 310, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 310, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 310, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(789, 335, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(789, 335, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(789, 335, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(789, 335, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(789, 335, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(789, 360, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(789, 360, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(789, 360, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(789, 360, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(789, 360, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 385, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 385, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 385, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 385, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 385, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 410, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 410, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 410, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 410, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 410, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 435, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 435, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 435, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 435, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 435, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(595, 310, text="Subtotal", fill="black", font=('Helvetica 10'))
        canvas.create_text(585, 335, text="TAX1", fill="black", font=('Helvetica 10'))
        canvas.create_text(635, 360, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        canvas.create_text(615, 385, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))
        canvas.create_text(600, 410, text="Total Paid", fill="black", font=('Helvetica 10'))
        canvas.create_text(595, 435, text="Balance", fill="black", font=('Helvetica 10'))

        canvas.create_line(150, 470, 800, 470, fill='orange')
        canvas.create_text(275, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 510, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 520, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 530, text="...", fill="black", font=('Helvetica 10'))
          
        canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas.create_line(150, 608, 795, 608, fill='orange')
        # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
        T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
        T.insert(END, estdata1[39])
        T_window = canvas.create_window(155, 612, anchor="nw", window=T)
        canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
      else:
        pass

  win_menu2 = StringVar()
  winstyle2 = ttk.Combobox(fifthtab,textvariable=win_menu2)
  winstyle2.bind("<<ComboboxSelected>>", maindropmenu)
  winstyle2["values"] = ("Professional 1 (logo on left side)","Professional 2 (logo on right side)","Simplified 1 (logo on left side)","Simplified 2 (logo on right side)","Business Classic")
  if not estdata:
    winstyle2.current(0)
    frame = Frame(fifthtab, width=953, height=300)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=247,y=90)
    canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
      
    canvas.config(width=953,height=300)
    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(100, 8, 850, 687 , outline='yellow',fill='white')
    canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
  
    #canvas.create_image(120,0, anchor=NW, image=est_logo)  
    canvas.create_text(285, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
      
    canvas.create_text(202, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(215, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(200, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))
      
    canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(700, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'), width=125)
    # T_address = Text(canvas, height=5, width=20 , font=('Helvetica 10'))
    # T_address.insert(END, estdata[2])
    # T_address_window = canvas.create_window(645, 80, anchor="nw", window=T_address)
    canvas.create_text(700, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
    canvas.create_text(700, 205, text=" "+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
    canvas.create_text(706, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
      
    canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
      
    s = ttk.Style()
    s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')

    tree.column("# 1", anchor=E, stretch=NO, width=100)
    tree.heading("# 1", text="ID/SKU")
    tree.column("# 2", anchor=E, stretch=NO, width=350)
    tree.heading("# 2", text="Product/Service - Description")
    tree.column("# 3", anchor=E, stretch=NO, width=80)
    tree.heading("# 3", text="Quantity")
    tree.column("# 4", anchor=E, stretch=NO, width=90)
    tree.heading("# 4", text="Unit Price")
    tree.column("# 5", anchor=E, stretch=NO, width=80)
    tree.heading("# 5", text="Price")
      
    window = canvas.create_window(120, 340, anchor="nw", window=tree)

    canvas.create_line(120, 390, 820, 390 )
    canvas.create_line(120, 340, 120, 365 )
    canvas.create_line(120, 365, 120, 390 )
    canvas.create_line(820, 340, 820, 540 )
    canvas.create_line(740, 340, 740, 540 )
    canvas.create_line(570, 340, 570, 540 )
    canvas.create_line(570, 415, 820, 415 )
    canvas.create_line(570, 440, 820, 440 )
    canvas.create_line(570, 465, 820, 465 )
    canvas.create_line(570, 490, 820, 490 )
    canvas.create_line(570, 515, 820, 515 )
    canvas.create_line(650, 340, 650, 390 )
    canvas.create_line(220, 340, 220, 390 )
    canvas.create_line(570, 540, 820, 540 )

    canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
    
    if comcursignpla.get() == "before amount":
      canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount":
      canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    else:
      pass
    # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    
    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
    else:
      pass

    # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
    
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
      
    canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 608, 795, 608)
    # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10')) 
    # T = Text(canvas, height=3, width=105, font=('Helvetica 10'))
    # T.insert(END, estdata[39])
    # T_window = canvas.create_window(105, 612, anchor="nw", window=T)


    canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10')) 
  elif estdata[32] == 'Professional 1 (logo on left side)':
    winstyle2.insert(0, estdata[32])
    frame = Frame(fifthtab, width=953, height=300)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=247,y=90)
    canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
      
    canvas.config(width=953,height=300)
    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(100, 8, 850, 687 , outline='yellow',fill='white')
    canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      est_image = Image.open("images/"+estdata[13])
      est_resize_image = est_image.resize((200,100))
      est_image = ImageTk.PhotoImage(est_resize_image)

      est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
      window_image = canvas.create_window(175, 45, anchor="nw", window=est_btlogo)
      est_btlogo.photo = est_image
    except:
      pass  
    canvas.create_text(202, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(215, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(200, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))
      
    canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(700, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'), width=125)
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', estdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(520, 80, anchor="nw", window=T_address)
    canvas.create_text(695, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
    canvas.create_text(700, 205, text=" "+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
    canvas.create_text(706, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
      
    canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
      
    s = ttk.Style()
    s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')

    tree.column("# 1", anchor=E, stretch=NO, width=100)
    tree.heading("# 1", text="ID/SKU")
    tree.column("# 2", anchor=E, stretch=NO, width=350)
    tree.heading("# 2", text="Product/Service - Description")
    tree.column("# 3", anchor=E, stretch=NO, width=80)
    tree.heading("# 3", text="Quantity")
    tree.column("# 4", anchor=E, stretch=NO, width=90)
    tree.heading("# 4", text="Unit Price")
    tree.column("# 5", anchor=E, stretch=NO, width=80)
    tree.heading("# 5", text="Price")
      
    window = canvas.create_window(120, 340, anchor="nw", window=tree)

    canvas.create_line(120, 390, 820, 390 )
    canvas.create_line(120, 340, 120, 365 )
    canvas.create_line(120, 365, 120, 390 )
    canvas.create_line(820, 340, 820, 540 )
    canvas.create_line(740, 340, 740, 540 )
    canvas.create_line(570, 340, 570, 540 )
    canvas.create_line(570, 415, 820, 415 )
    canvas.create_line(570, 440, 820, 440 )
    canvas.create_line(570, 465, 820, 465 )
    canvas.create_line(570, 490, 820, 490 )
    canvas.create_line(570, 515, 820, 515 )
    canvas.create_line(650, 340, 650, 390 )
    canvas.create_line(220, 340, 220, 390 )
    canvas.create_line(570, 540, 820, 540 )

    canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
    
    if comcursignpla.get() == "before amount":
      canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount":
      canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    else:
      pass
    # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    
    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
    else:
      pass

    # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
    
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
      
    canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 608, 795, 608)
    # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10')) 
    T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
    T.insert(END, estdata[39])
    T_window = canvas.create_window(155, 612, anchor="nw", window=T)

    canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif estdata[32] == 'Professional 2 (logo on right side)':
    winstyle2.insert(0, estdata[32])
    frame = Frame(fifthtab, width=953, height=300)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=247,y=90)
      
    canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
      
    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=953,height=300)
      
    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
    canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      est_image = Image.open("images/"+estdata[13])
      est_resize_image = est_image.resize((200,100))
      est_image = ImageTk.PhotoImage(est_resize_image)

      est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
      window_image = canvas.create_window(500, 45, anchor="nw", window=est_btlogo)
      est_btlogo.photo = est_image
    except:
      pass  
    canvas.create_text(250, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(225, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', estdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(100, 80, anchor="nw", window=T_address)
    canvas.create_text(225, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
    canvas.create_text(225, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
    canvas.create_text(232, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
      
    canvas.create_text(502, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(515, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(500, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(491, 220, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(505, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(690, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(690, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(690, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(680, 220, text="NET 15", fill="black", font=('Helvetica 11'))      
      
    canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

    s = ttk.Style()
    s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=100)
    tree.heading("# 1", text="ID/SKU")
    tree.column("# 2", anchor=E, stretch=NO, width=350)
    tree.heading("# 2", text="Product/Service - Description")
    tree.column("# 3", anchor=E, stretch=NO, width=80)
    tree.heading("# 3", text="Quantity")
    tree.column("# 4", anchor=E, stretch=NO, width=90)
    tree.heading("# 4", text="Unit Price")
    tree.column("# 5", anchor=E, stretch=NO, width=80)
    tree.heading("# 5", text="Price")
      
    window = canvas.create_window(120, 340, anchor="nw", window=tree)

    canvas.create_line(120, 390, 820, 390 )
    canvas.create_line(120, 340, 120, 365 )
    canvas.create_line(120, 365, 120, 390 )
    canvas.create_line(820, 340, 820, 540 )
    canvas.create_line(740, 340, 740, 540 )
    canvas.create_line(570, 340, 570, 540 )
    canvas.create_line(570, 415, 820, 415 )
    canvas.create_line(570, 440, 820, 440 )
    canvas.create_line(570, 465, 820, 465 )
    canvas.create_line(570, 490, 820, 490 )
    canvas.create_line(570, 515, 820, 515 )
    canvas.create_line(650, 340, 650, 390 )
    canvas.create_line(220, 340, 220, 390 )
    canvas.create_line(570, 540, 820, 540 )

    canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
    else:
      pass

    # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
    
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 608, 795, 608)
    # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
    T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
    T.insert(END, estdata[39])
    T_window = canvas.create_window(155, 612, anchor="nw", window=T)
    canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif estdata[32] == 'Simplified 1 (logo on left side)':
    winstyle2.insert(0, estdata[32])
    frame = Frame(fifthtab, width=953, height=300)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=247,y=90)
    canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=953,height=300)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
    canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      est_image = Image.open("images/"+estdata[13])
      est_resize_image = est_image.resize((200,100))
      est_image = ImageTk.PhotoImage(est_resize_image)

      est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
      window_image = canvas.create_window(175, 45, anchor="nw", window=est_btlogo)
      est_btlogo.photo = est_image
    except:
      pass  
    canvas.create_text(202, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(215, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(200, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))      

    canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(710, 200, text=caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', estdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(520, 80, anchor="nw", window=T_address)

    canvas.create_text(708, 170, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
    canvas.create_text(710, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
      
    canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

    s = ttk.Style()
    s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_1.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=530)
    tree.heading("# 1", text="Product/Service - Description")
    tree.column("# 2", anchor=E, stretch=NO, width=90)
    tree.heading("# 2", text="Quantity")
    tree.column("# 3", anchor=E, stretch=NO, width=80)
    tree.heading("# 3", text="Price")
      
    window = canvas.create_window(120, 340, anchor="nw", window=tree)

    canvas.create_line(120, 390, 820, 390 )
    canvas.create_line(120, 340, 120, 365 )
    canvas.create_line(120, 365, 120, 390 )
    canvas.create_line(820, 340, 820, 540 )
    canvas.create_line(740, 340, 740, 540 )
    canvas.create_line(570, 390, 570, 540 )
    canvas.create_line(570, 415, 820, 415 )
    canvas.create_line(570, 440, 820, 440 )
    canvas.create_line(570, 465, 820, 465 )
    canvas.create_line(570, 490, 820, 490 )
    canvas.create_line(570, 515, 820, 515 )
    canvas.create_line(650, 340, 650, 390 )
    canvas.create_line(570, 540, 820, 540 )

      
    canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 608, 795, 608)
    # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
    T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
    T.insert(END, estdata[39])
    T_window = canvas.create_window(155, 612, anchor="nw", window=T)
    canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif estdata[32] == 'Simplified 2 (logo on right side)':
    winstyle2.insert(0, estdata[32])
    frame = Frame(fifthtab, width=953, height=300)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=247,y=90)

    canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=953,height=300)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
    canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      est_image = Image.open("images/"+estdata[13])
      est_resize_image = est_image.resize((200,100))
      est_image = ImageTk.PhotoImage(est_resize_image)

      est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
      window_image = canvas.create_window(500, 45, anchor="nw", window=est_btlogo)
      est_btlogo.photo = est_image
    except:
      pass  
    canvas.create_text(250, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(224, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', estdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(100, 80, anchor="nw", window=T_address)
    canvas.create_text(224, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
    canvas.create_text(225, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))

    canvas.create_text(502, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(515, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(500, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(491, 220, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(505, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(680, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(680, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(680, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(670, 220, text="NET 15", fill="black", font=('Helvetica 11'))      

    canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

    s = ttk.Style()
    s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_1.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=530)
    tree.heading("# 1", text="Product/Service - Description")
    tree.column("# 2", anchor=E, stretch=NO, width=90)
    tree.heading("# 2", text="Quantity")
    tree.column("# 3", anchor=E, stretch=NO, width=80)
    tree.heading("# 3", text="Price")
      
    window = canvas.create_window(120, 340, anchor="nw", window=tree)

    canvas.create_line(120, 390, 820, 390 )
    canvas.create_line(120, 340, 120, 365 )
    canvas.create_line(120, 365, 120, 390 )
    canvas.create_line(820, 340, 820, 540 )
    canvas.create_line(740, 340, 740, 540 )
    canvas.create_line(570, 390, 570, 540 )
    canvas.create_line(570, 415, 820, 415 )
    canvas.create_line(570, 440, 820, 440 )
    canvas.create_line(570, 465, 820, 465 )
    canvas.create_line(570, 490, 820, 490 )
    canvas.create_line(570, 515, 820, 515 )
    canvas.create_line(650, 340, 650, 390 )
    canvas.create_line(570, 540, 820, 540 )

      
    canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 608, 795, 608)
    # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
    T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
    T.insert(END, estdata[39])
    T_window = canvas.create_window(155, 612, anchor="nw", window=T)
    canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif estdata[32] == 'Business Classic':
    winstyle2.insert(0, estdata[32])
    frame = Frame(fifthtab, width=953, height=300)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=247,y=90)
      
    canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
      
    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=953,height=300)
      
    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
    canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 70, 800, 70, fill='orange')
    
    try:
      est_image = Image.open("images/"+estdata[13])
      est_resize_image = est_image.resize((200,100))
      est_image = ImageTk.PhotoImage(est_resize_image)

      est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
      window_image = canvas.create_window(140, 120, anchor="nw", window=est_btlogo)
      est_btlogo.photo = est_image
    except:
      pass  

    canvas.create_text(500, 90, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(480, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=35, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', estdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(350, 100, anchor="nw", window=T_address)
        
        
    canvas.create_text(480, 210, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))

    canvas.create_text(655, 100, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(696, 120, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(706, 135, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(665, 150, text="United States", fill="black", font=('Helvetica 10'))

    canvas.create_text(659, 180, text=""+est_str1.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(675, 210, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(659, 240, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))

    canvas.create_text(776, 180, text="EST1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(776, 210, text="05 May 2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(776, 240, text="20-05-2022", fill="black", font=('Helvetica 11'))

    s = ttk.Style()
    s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=200)
    tree.heading("# 1", text="Product/Service")
    tree.column("# 2", anchor=E, stretch=NO, width=250)
    tree.heading("# 2", text="Description")
    tree.column("# 3", anchor=E, stretch=NO, width=90)
    tree.heading("# 3", text="Unit Price")
    tree.column("# 4", anchor=E, stretch=NO, width=80)
    tree.heading("# 4", text="Quantity")
    tree.column("# 5", anchor=E, stretch=NO, width=80)
    tree.heading("# 5", text="Price")
      
    window = canvas.create_window(120, 255, anchor="nw", window=tree)

    canvas.create_line(120, 295, 820, 295 )
    canvas.create_line(120, 255, 120, 295 )
    canvas.create_line(320, 255, 320, 295 )
    canvas.create_line(570, 255, 570, 295 )
    canvas.create_line(660, 255, 660, 295 )
    canvas.create_line(740, 255, 740, 295 )
    canvas.create_line(820, 255, 820, 445 )
    canvas.create_line(570, 320, 820, 320 )
    canvas.create_line(570, 345, 820, 345 )
    canvas.create_line(570, 370, 820, 370 )
    canvas.create_line(570, 395, 820, 395 )
    canvas.create_line(570, 420, 820, 420 )
    canvas.create_line(570, 445, 820, 445 )
      
    canvas.create_text(160, 285, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(450, 285, text="Example product - Description text...", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(624, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(624, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(624, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(624, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(624, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(700, 285, text="1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 310, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 310, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 310, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 310, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 310, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(789, 335, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(789, 335, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(789, 335, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(789, 335, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(789, 335, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(789, 360, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(789, 360, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(789, 360, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(789, 360, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(789, 360, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 385, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 385, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 385, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 385, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 385, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 410, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 410, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 410, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 410, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 410, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 435, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 435, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 435, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 435, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 435, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(595, 310, text="Subtotal", fill="black", font=('Helvetica 10'))
    canvas.create_text(585, 335, text="TAX1", fill="black", font=('Helvetica 10'))
    canvas.create_text(635, 360, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    canvas.create_text(615, 385, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(600, 410, text="Total Paid", fill="black", font=('Helvetica 10'))
    canvas.create_text(595, 435, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_line(150, 470, 800, 470, fill='orange')
    canvas.create_text(275, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 510, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 520, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 530, text="...", fill="black", font=('Helvetica 10'))
      
    canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 608, 795, 608, fill='orange')
    # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
    T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
    T.insert(END, estdata[39])
    T_window = canvas.create_window(155, 612, anchor="nw", window=T)
    canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  else:
    pass
  winstyle2.place(x=770 ,y=40, width=220)
  #winstyle2.current(0)



################### tab07 ###################################
  seventhtab1=Frame(tab07, relief=GROOVE, bg="#f8f8f2")
  seventhtab1.pack(side="top", fill=BOTH)

  sql = "select * from company"
  fbcursor.execute(sql)
  advdata = fbcursor.fetchone()
  #print(estdata)


  seventhtab=Frame(seventhtab1, bg="#f5f3f2", height=700)
  seventhtab.pack(side="top", fill=BOTH)

  adv_messagelbframe=LabelFrame(seventhtab,text="Template advanced settings", height=250, width=1150)
  adv_messagelbframe.place(x=2, y=10)

  adv_fbill = Label(seventhtab,text="Template",font="arial 10 bold").place(x=20,y=30)

  adv_ver = Label(seventhtab,text="Professional 1 (logo on left side)")
  adv_ver.place(x=20,y=60)

  adv_ver = Label(seventhtab,text="Professional 2 (logo on right side)")
  adv_ver.place(x=20,y=90)

  adv_ver = Label(seventhtab,text="Simplified 1 (logo on left side)")
  adv_ver.place(x=20,y=120)

  adv_ver = Label(seventhtab,text="Simplified 2 (logo on right side)")
  adv_ver.place(x=20,y=150)

  adv_ver = Label(seventhtab,text="Business Classic")
  adv_ver.place(x=20,y=180)

  adv_fbill = Label(seventhtab,text="Page size",font="arial 10 bold").place(x=255,y=30)

  adv_win_menu3 = StringVar()
  adv_winstyle3 = ttk.Combobox(seventhtab,textvariable=adv_win_menu3)
  adv_winstyle3['values'] = ('Letter','A4')
  adv_win_menu3.set('Letter')
  #adv_winstyle3.current(0)
  adv_winstyle3.place(x=225 ,y=60)
    
  
  adv_win_menu4 = StringVar()
  adv_winstyle4 = ttk.Combobox(seventhtab,textvariable=adv_win_menu4)
  adv_winstyle4.place(x=225,y=90)
  adv_winstyle4['values'] = ("Letter","A4")
  adv_winstyle4.set("Letter")
  adv_winstyle4.current(0)

  adv_win_menu5 = StringVar()
  adv_winstyle5 = ttk.Combobox(seventhtab,textvariable=adv_win_menu5)
  adv_winstyle5.place(x=225,y=120)
  adv_winstyle5['values'] = ("Letter","A4")
  adv_winstyle5.set("Letter")
  adv_winstyle5.current(0)

  adv_win_menu6 = StringVar()
  adv_winstyle6 = ttk.Combobox(seventhtab,textvariable=adv_win_menu6)
  adv_winstyle6.place(x=225,y=150)
  adv_winstyle6['values'] = ("Letter","A4")
  adv_winstyle6.set("Letter")
  adv_winstyle6.current(0)

  adv_win_menu7 = StringVar()
  adv_winstyle7 = ttk.Combobox(seventhtab,textvariable=adv_win_menu7)
  adv_winstyle7.place(x=225,y=180)
  adv_winstyle7['values'] = ("Letter","A4")
  adv_winstyle7.set("Letter")
  adv_winstyle7.current(0)

  adv_fbill = Label(seventhtab,text="Right Margin(mm)",font="arial 10 bold").place(x=450,y=30)

  adv_spin00 = Spinbox(seventhtab,from_=5,to=20,width=10)
  adv_spin00.place(x=465,y=60)

  adv_spin01 = Spinbox(seventhtab,from_=5,to=20,width=10)
  adv_spin01.place(x=465,y=90)

  adv_spin02 = Spinbox(seventhtab,from_=5,to=20,width=10)
  adv_spin02.place(x=465,y=120)

  adv_spin03 = Spinbox(seventhtab,from_=5,to=20,width=10)
  adv_spin03.place(x=465,y=150)

  adv_spin04 = Spinbox(seventhtab,from_=5,to=20,width=10)
  adv_spin04.place(x=465,y=180)


  adv_fbill = Label(seventhtab,text="'Invoice to'block position shift(mm)",font="arial 10 bold").place(x=650,y=30)

  adv_lbl1 = Label(seventhtab, text="Left : ").place(x=651,y=60)
  adv_lbl1 = Label(seventhtab, text="Left : ").place(x=651,y=90)
  adv_lbl1 = Label(seventhtab, text="Left : ").place(x=651,y=120)
  adv_lbl1 = Label(seventhtab, text="Left : ").place(x=651,y=150)

  adv_spin10 = Spinbox(seventhtab,from_=-10,to=100,width=10)
  adv_spin10.place(x=685,y=60)

  adv_spin11 = Spinbox(seventhtab,from_=-10,to=100,width=10)
  adv_spin11.place(x=685,y=90)

  adv_spin12 = Spinbox(seventhtab,from_=-10,to=100,width=10)
  adv_spin12.place(x=685,y=120)

  adv_spin13 = Spinbox(seventhtab,from_=-10,to=100,width=10)
  adv_spin13.place(x=685,y=150)

  adv_lbl1 = Label(seventhtab, text="Top : ").place(x=785,y=60)
  adv_lbl1 = Label(seventhtab, text="Top : ").place(x=785,y=90)
  adv_lbl1 = Label(seventhtab, text="Top : ").place(x=785,y=120)
  adv_lbl1 = Label(seventhtab, text="Top : ").place(x=785,y=150)

  adv_spin20 = Spinbox(seventhtab,from_=0,to=100,width=10)
  adv_spin20.place(x=820,y=60)

  adv_spin21 = Spinbox(seventhtab,from_=0,to=100,width=10)
  adv_spin21.place(x=820,y=90)

  adv_spin22 = Spinbox(seventhtab,from_=0,to=100,width=10)
  adv_spin22.place(x=820,y=120)

  adv_spin23 = Spinbox(seventhtab,from_=0,to=100,width=10)
  adv_spin23.place(x=820,y=150)

  adv_bttermadd = Button(seventhtab,image=photo8,compound = LEFT,text="Refresh preview",width=115)
  adv_bttermadd.place(x=1000,y=50)

  adv_bttermadd = Button(seventhtab,image=saves,compound = LEFT,text="Save Settings",width=115)
  adv_bttermadd.place(x=1000,y=140)

  def adv_restore():
    adv_spin10.delete(0,'end')
    adv_spin10.insert(0,"0")
    adv_spin11.delete(0,'end')
    adv_spin11.insert(0,"0")
    adv_spin12.delete(0,'end')
    adv_spin12.insert(0,"0")
    adv_spin13.delete(0,'end')
    adv_spin13.insert(0,"0")
    adv_spin20.delete(0,'end')
    adv_spin20.insert(0,"0")
    adv_spin21.delete(0,'end')
    adv_spin21.insert(0,"0")
    adv_spin22.delete(0,'end')
    adv_spin22.insert(0,"0")
    adv_spin23.delete(0,'end')
    adv_spin23.insert(0,"0")
    adv_spin00.delete(0,'end')
    adv_spin00.insert(0,"10")
    adv_spin01.delete(0,'end')
    adv_spin01.insert(0,"10")
    adv_spin02.delete(0,'end')
    adv_spin02.insert(0,"10")
    adv_spin03.delete(0,'end')
    adv_spin03.insert(0,"10")
    adv_spin04.delete(0,'end')
    adv_spin04.insert(0,"10")
    adv_winstyle3.delete(0,'end')
    adv_winstyle3.insert(0,"Letter")
    adv_winstyle4.delete(0,'end')
    adv_winstyle4.insert(0,"Letter")
    adv_winstyle5.delete(0,'end')
    adv_winstyle5.insert(0,"Letter")
    adv_winstyle6.delete(0,'end')
    adv_winstyle6.insert(0,"Letter")
    adv_winstyle7.delete(0,'end')
    adv_winstyle7.insert(0,"Letter")

  adv_bttermadd = Button(seventhtab,text="Restore defaults",width=16, command=adv_restore)
  adv_bttermadd.place(x=1000,y=180)

  adv_ver = Label(seventhtab,text="By positioning 'Invoice to'block,the customer name/address can be displayed in right place in the windowed envelope. If you networking, you need to setup this on all computer.\nExample:(Left:20 and Top:10 means that shift 'Invoice to'block to right 20mm and shift down 10mm) Original position Left:0 Top:0")
  adv_ver.place(x=50,y=210)

  adv_ver = Label(seventhtab,text="Selected template preview (example, click on preview for mouse scrolling)")
  adv_ver.place(x=230,y=270)

#------------Professional 1 (logo on left side)------------- 
  def adv_maindropmenu(event):
      menuvar=adv_win_menu8.get()
      print(menuvar)
      sql = "select * from company"
      fbcursor.execute(sql)
      advdata1 = fbcursor.fetchone()

      if menuvar == 'Professional 1 (logo on left side)':
          frame = Frame(seventhtab, width=1200, height=155)
          frame.pack(expand=True, fill=BOTH)
          frame.place(x=2,y=309)
          canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

          vertibar=Scrollbar(frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=canvas.yview)
          canvas.config(width=1200,height=155)

          canvas.config(yscrollcommand=vertibar.set)
          canvas.pack(expand=True,side=LEFT,fill=BOTH)
          canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')

          canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))

          try:
            adv_image = Image.open("images/"+advdata1[13])
            adv_resize_image = adv_image.resize((200,75))
            adv_image = ImageTk.PhotoImage(adv_resize_image)

            adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
            adv_window_image = canvas.create_window(150, 30, anchor="nw", window=adv_btlogo)
            adv_btlogo.photo = adv_image
          except:
            pass  

          canvas.create_text(130, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
          canvas.create_text(141, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
          canvas.create_text(130, 160, text="Due date", fill="black", font=('Helvetica 11'))
          canvas.create_text(120, 180, text="Terms", fill="black", font=('Helvetica 11'))
          canvas.create_text(134, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
          canvas.create_text(347, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(350, 140, text="03-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(350, 160, text="18-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(340, 180, text="NET 15", fill="black", font=('Helvetica 11'))

          canvas.create_text(1050, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
          # canvas.create_text(1080, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
          T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
          T_address.tag_configure('tag_name',justify='right')
          T_address.insert('1.0', advdata[2])
          T_address.tag_add('tag_name','1.0', 'end')
          T_address_window = canvas.create_window(850, 80, anchor="nw", window=T_address)
          canvas.create_text(1050, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
          # canvas.create_text(1085, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
          # canvas.create_text(1085, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
          # canvas.create_text(1080, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          # canvas.create_text(1080, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
          canvas.create_text(1050, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))
          canvas.create_text(1050, 210, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))

          canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
          canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

          s = ttk.Style()
          s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')
              
          tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
            
          tree.column("# 1", anchor=E, stretch=NO, width=150)
          tree.heading("# 1", text="ID/SKU")
          tree.column("# 2", anchor=E, stretch=NO, width=400)
          tree.heading("# 2", text="Product/Service - Description")
          tree.column("# 3", anchor=E, stretch=NO, width=150)
          tree.heading("# 3", text="Quantity")
          tree.column("# 4", anchor=E, stretch=NO, width=150)
          tree.heading("# 4", text="Unit Price")
          tree.column("# 5", anchor=E, stretch=NO, width=150)
          tree.heading("# 5", text="Price")
            
          window = canvas.create_window(120, 290, anchor="nw", window=tree)

          canvas.create_line(120, 330, 1120, 330 )
          canvas.create_line(120, 290, 120, 330 )
          canvas.create_line(270, 290, 270, 330 )
          canvas.create_line(670, 290, 670, 330 )
          canvas.create_line(820, 290, 820, 330 )
          canvas.create_line(970, 290, 970, 330 )
          canvas.create_line(1120, 290, 1120, 330 )
          canvas.create_line(670, 330, 670, 480)
          canvas.create_line(970, 330, 970, 480)
          canvas.create_line(1120, 330, 1120, 480)
          canvas.create_line(670, 355, 1120, 355)
          canvas.create_line(670, 380, 1120, 380)
          canvas.create_line(670, 405, 1120, 405)
          canvas.create_line(670, 430, 1120, 430)
          canvas.create_line(670, 455, 1120, 455)
          canvas.create_line(670, 480, 1120, 480)

          canvas.create_text(165, 320, text="PROD-0001", fill="black", font=('Helvetica 10'))
          canvas.create_text(400, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          canvas.create_text(740, 320, text="1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(884, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(884, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(884, 320, text="$200.00", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 320, text="$200.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 345, text="$200.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1085, 370, text="$18.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1085, 395, text="$20.00", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 420, text="$238.00", fill="black", font=('Helvetica 10 bold'))
          canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 445, text="$100.00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 465, text="$138.00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))


          canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

          canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          canvas.create_line(110, 600, 1120, 600)
          canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
          canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

#------------Professional 2 (logo on right side)------------- 

      elif menuvar == 'Professional 2 (logo on right side)':
          frame = Frame(seventhtab, width=1200, height=155)
          frame.pack(expand=True, fill=BOTH)
          frame.place(x=2,y=309)
          canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

          vertibar=Scrollbar(frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=canvas.yview)
          canvas.config(width=1200,height=155)

          canvas.config(yscrollcommand=vertibar.set)
          canvas.pack(expand=True,side=LEFT,fill=BOTH)
          canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
          canvas.create_text(600, 45, text="Title text goes here...", fill="black", font=('Helvetica 10'))

          try:
            adv_image = Image.open("images/"+advdata1[13])
            adv_resize_image = adv_image.resize((200,75))
            adv_image = ImageTk.PhotoImage(adv_resize_image)

            adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
            adv_window_image = canvas.create_window(850, 25, anchor="nw", window=adv_btlogo)
            adv_btlogo.photo = adv_image
          except:
            pass  

          # canvas.create_text(1000, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

          canvas.create_text(829, 110, text="Invoice#", fill="black", font=('Helvetica 11'))
          canvas.create_text(841, 130, text="Invoice date", fill="black", font=('Helvetica 11'))
          canvas.create_text(830, 150, text="Due date", fill="black", font=('Helvetica 11'))
          canvas.create_text(820, 170, text="Terms", fill="black", font=('Helvetica 11'))
          canvas.create_text(834, 190, text="Order ref.#", fill="black", font=('Helvetica 11'))
          canvas.create_text(1047, 110, text="INV1/2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(1050, 130, text="06-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(1050, 150, text="21-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(1040, 170, text="NET 15", fill="black", font=('Helvetica 11'))

          canvas.create_text(170, 65, text=""+comname.get(), fill="black", font=('Helvetica 12 '))
          # canvas.create_text(130, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
          T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
          T_address.tag_configure('tag_name',justify='right')
          T_address.insert('1.0', advdata[2])
          T_address.tag_add('tag_name','1.0', 'end')
          T_address_window = canvas.create_window(10, 80, anchor="nw", window=T_address)
          #T_address_window = canvas.create_window(95, 80, anchor="nw", window=T_address)
          canvas.create_text(130, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
          # canvas.create_text(130, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
          # canvas.create_text(130, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
          # canvas.create_text(136, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          # canvas.create_text(136, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
          canvas.create_text(124, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

          canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
          canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

          tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
      
          tree.column("# 1", anchor=E, stretch=NO, width=150)
          tree.heading("# 1", text="ID/SKU")
          tree.column("# 2", anchor=E, stretch=NO, width=400)
          tree.heading("# 2", text="Product/Service - Description")
          tree.column("# 3", anchor=E, stretch=NO, width=150)
          tree.heading("# 3", text="Quantity")
          tree.column("# 4", anchor=E, stretch=NO, width=150)
          tree.heading("# 4", text="Unit Price")
          tree.column("# 5", anchor=E, stretch=NO, width=150)
          tree.heading("# 5", text="Price")
      
          window = canvas.create_window(120, 290, anchor="nw", window=tree)

          canvas.create_line(120, 330, 1120, 330 )
          canvas.create_line(120, 290, 120, 330 )
          canvas.create_line(270, 290, 270, 330 )
          canvas.create_line(670, 290, 670, 330 )
          canvas.create_line(820, 290, 820, 330 )
          canvas.create_line(970, 290, 970, 330 )
          canvas.create_line(1120, 290, 1120, 330 )
          canvas.create_line(670, 330, 670, 480)
          canvas.create_line(970, 330, 970, 480)
          canvas.create_line(1120, 330, 1120, 480)
          canvas.create_line(670, 355, 1120, 355)
          canvas.create_line(670, 380, 1120, 380)
          canvas.create_line(670, 405, 1120, 405)
          canvas.create_line(670, 430, 1120, 430)
          canvas.create_line(670, 455, 1120, 455)
          canvas.create_line(670, 480, 1120, 480)

          canvas.create_text(165, 320, text="PROD-0001", fill="black", font=('Helvetica 10'))
          canvas.create_text(400, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          canvas.create_text(740, 320, text="1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(884, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(884, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 320, text="$200.00", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 320, text="$200.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 345, text="$200.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1089, 370, text="$18.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1089, 395, text="$20.00", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 420, text="$238.00", fill="black", font=('Helvetica 10 bold'))
          canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 445, text="$100.00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 465, text="$138.00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

          canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

          canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          canvas.create_line(110, 600, 1120, 600)
          canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
          canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

#------------Simplified 1 (logo on left side)------------- 

      elif menuvar == 'Simplified 1 (logo on left side)':
          frame = Frame(seventhtab, width=1200, height=155)
          frame.pack(expand=True, fill=BOTH)
          frame.place(x=2,y=309)
          canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

          vertibar=Scrollbar(frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=canvas.yview)
          canvas.config(width=1200,height=155)

          canvas.config(yscrollcommand=vertibar.set)
          canvas.pack(expand=True,side=LEFT,fill=BOTH)
          canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
          canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          try:
            adv_image = Image.open("images/"+advdata1[13])
            adv_resize_image = adv_image.resize((200,75))
            adv_image = ImageTk.PhotoImage(adv_resize_image)

            adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
            adv_window_image = canvas.create_window(150, 25, anchor="nw", window=adv_btlogo)
            adv_btlogo.photo = adv_image
          except:
            pass  
          #canvas.create_text(250, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

          canvas.create_text(130, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
          canvas.create_text(141, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
          canvas.create_text(130, 160, text="Due date", fill="black", font=('Helvetica 11'))
          canvas.create_text(120, 180, text="Terms", fill="black", font=('Helvetica 11'))
          canvas.create_text(134, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
          canvas.create_text(347, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(350, 140, text="06-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(350, 160, text="21-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(340, 180, text="NET 15", fill="black", font=('Helvetica 11'))

          canvas.create_text(1050, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
          # canvas.create_text(1080, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
          T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
          T_address.tag_configure('tag_name',justify='right')
          T_address.insert('1.0', advdata[2])
          T_address.tag_add('tag_name','1.0', 'end')
          T_address_window = canvas.create_window(850, 80, anchor="nw", window=T_address)
          canvas.create_text(1050, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
          # canvas.create_text(1085, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
          # canvas.create_text(1085, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
          # canvas.create_text(1080, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          # canvas.create_text(1080, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
          canvas.create_text(1050, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

          canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
          canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

          s = ttk.Style()
          s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

          tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_2.Treeview')
      
          tree.column("# 1", anchor=E, stretch=NO, width=700)
          tree.heading("# 1", text="Product/Service - Description")
          tree.column("# 2", anchor=E, stretch=NO, width=150)
          tree.heading("# 2", text="Quantity")
          tree.column("# 3", anchor=E, stretch=NO, width=150)
          tree.heading("# 3", text="Price")
            
          window = canvas.create_window(120, 290, anchor="nw", window=tree)

          canvas.create_line(120, 330, 1120, 330 )
          canvas.create_line(120, 290, 120, 330 )
          canvas.create_line(820, 290, 820, 330 )
          canvas.create_line(970, 290, 970, 330 )
          canvas.create_line(1120, 290, 1120, 330 )
          canvas.create_line(670, 330, 670, 480)
          canvas.create_line(970, 330, 970, 480)
          canvas.create_line(1120, 330, 1120, 480)
          canvas.create_line(670, 355, 1120, 355)
          canvas.create_line(670, 380, 1120, 380)
          canvas.create_line(670, 405, 1120, 405)
          canvas.create_line(670, 430, 1120, 430)
          canvas.create_line(670, 455, 1120, 455)
          canvas.create_line(670, 480, 1120, 480)

          canvas.create_text(250, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          canvas.create_text(900, 320, text="1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1089, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1089, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
          canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

          canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

          canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          canvas.create_line(110, 600, 1120, 600)
          canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
          canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))


#------------Simplified 2 (logo on right side)-------------

      elif menuvar == 'Simplified 2 (logo on right side)':
          frame = Frame(seventhtab, width=1200, height=155)
          frame.pack(expand=True, fill=BOTH)
          frame.place(x=2,y=309)
          canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

          vertibar=Scrollbar(frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=canvas.yview)
          canvas.config(width=1200,height=155)

          canvas.config(yscrollcommand=vertibar.set)
          canvas.pack(expand=True,side=LEFT,fill=BOTH)
          canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
          canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          try:
            adv_image = Image.open("images/"+advdata1[13])
            adv_resize_image = adv_image.resize((200,75))
            adv_image = ImageTk.PhotoImage(adv_resize_image)

            adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
            adv_window_image = canvas.create_window(850, 25, anchor="nw", window=adv_btlogo)
            adv_btlogo.photo = adv_image
          except:
            pass  

          # canvas.create_text(1000, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

          canvas.create_text(829, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
          canvas.create_text(841, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
          canvas.create_text(830, 160, text="Due date", fill="black", font=('Helvetica 11'))
          canvas.create_text(820, 180, text="Terms", fill="black", font=('Helvetica 11'))
          canvas.create_text(834, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
          canvas.create_text(1047, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(1050, 140, text="06-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(1050, 160, text="21-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(1040, 180, text="NET 15", fill="black", font=('Helvetica 11'))

          canvas.create_text(170, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
          # canvas.create_text(130, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
          T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
          T_address.tag_configure('tag_name',justify='right')
          T_address.insert('1.0', advdata[2])
          T_address.tag_add('tag_name','1.0', 'end')
          T_address_window = canvas.create_window(10, 80, anchor="nw", window=T_address)
          canvas.create_text(130, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
          # canvas.create_text(130, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
          # canvas.create_text(130, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
          # canvas.create_text(136, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          # canvas.create_text(136, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
          canvas.create_text(124, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

          canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
          canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

          s = ttk.Style()
          s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

          tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_2.Treeview')
              
          tree.column("# 1", anchor=E, stretch=NO, width=700)
          tree.heading("# 1", text="Product/Service - Description")
          tree.column("# 2", anchor=E, stretch=NO, width=150)
          tree.heading("# 2", text="Quantity")
          tree.column("# 3", anchor=E, stretch=NO, width=150)
          tree.heading("# 3", text="Price")
        
          window = canvas.create_window(120, 290, anchor="nw", window=tree)

          canvas.create_line(120, 330, 1120, 330 )
          canvas.create_line(120, 290, 120, 330 )
          canvas.create_line(820, 290, 820, 330 )
          canvas.create_line(970, 290, 970, 330 )
          canvas.create_line(1120, 290, 1120, 330 )
          canvas.create_line(670, 330, 670, 480)
          canvas.create_line(970, 330, 970, 480)
          canvas.create_line(1120, 330, 1120, 480)
          canvas.create_line(670, 355, 1120, 355)
          canvas.create_line(670, 380, 1120, 380)
          canvas.create_line(670, 405, 1120, 405)
          canvas.create_line(670, 430, 1120, 430)
          canvas.create_line(670, 455, 1120, 455)
          canvas.create_line(670, 480, 1120, 480)

          canvas.create_text(250, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          canvas.create_text(900, 320, text="1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1089, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1089, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
          canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

          canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

          canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          canvas.create_line(110, 600, 1120, 600)
          canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
          canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

  #------------Business Classic------------- 

      elif menuvar == 'Business Classic':
          frame = Frame(seventhtab, width=1200, height=155)
          frame.pack(expand=True, fill=BOTH)
          frame.place(x=2,y=309)
          canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

          vertibar=Scrollbar(frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=canvas.yview)
          canvas.config(width=1200,height=155)

          canvas.config(yscrollcommand=vertibar.set)
          canvas.pack(expand=True,side=LEFT,fill=BOTH)
          canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
          canvas.create_text(600, 45, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          canvas.create_line(100, 60, 1120, 60, fill="orange")
          #canvas.create_line(1000, 60, 600, 60, fill="grey")

          try:
            adv_image = Image.open("images/"+advdata1[13])
            adv_resize_image = adv_image.resize((200,100))
            adv_image = ImageTk.PhotoImage(adv_resize_image)

            adv_btlogo = Label(canvas,width=200,height=100,image = adv_image) 
            adv_window_image = canvas.create_window(140, 100, anchor="nw", window=adv_btlogo)
            adv_btlogo.photo = adv_image
          except:
            pass  


          # canvas.create_text(250, 155, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

          canvas.create_text(560, 85, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
          # canvas.create_text(535, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
          T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
          T_address.tag_configure('tag_name',justify='right')
          T_address.insert('1.0', advdata[2])
          T_address.tag_add('tag_name','1.0', 'end')
          T_address_window = canvas.create_window(350, 100, anchor="nw", window=T_address)
          # adv_btlabel = Label(canvas,width=20,height=10,text=""+caddent.get('1.0', 'end-1c')) 
          # adv_window_label = canvas.create_window(530, 110, anchor="nw", window=adv_btlabel)
          canvas.create_text(530, 190, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
          # canvas.create_text(530, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
          # canvas.create_text(530, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
          # canvas.create_text(536, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          # canvas.create_text(536, 190, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
          canvas.create_text(524, 210, text="Invoice", fill="black", font=('Helvetica 14 bold'))

          canvas.create_text(749, 95, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(791, 110, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(800, 125, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(760, 140, text="United States", fill="black", font=('Helvetica 10'))

          canvas.create_text(745, 160, text="Invoice", fill="black", font=('Helvetica 11'))
          canvas.create_text(760, 180, text="Invoice date", fill="black", font=('Helvetica 11'))
          canvas.create_text(750, 200, text="Due date", fill="black", font=('Helvetica 11'))

          canvas.create_text(947, 160, text="INV1/2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(950, 180, text="06-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(950, 200, text="21-05-2022", fill="black", font=('Helvetica 11'))
          s = ttk.Style()
          s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

          tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
        
          tree.column("# 1", anchor=E, stretch=NO, width=150)
          tree.heading("# 1", text="Product/Service")
          tree.column("# 2", anchor=E, stretch=NO, width=400)
          tree.heading("# 2", text="Description")
          tree.column("# 3", anchor=E, stretch=NO, width=150)
          tree.heading("# 3", text="Unit Price")
          tree.column("# 4", anchor=E, stretch=NO, width=150)
          tree.heading("# 4", text="Quantity")
          tree.column("# 5", anchor=E, stretch=NO, width=150)
          tree.heading("# 5", text="Price")
              
          window = canvas.create_window(120, 230, anchor="nw", window=tree)

          canvas.create_line(120, 270, 1120, 270 )
          canvas.create_line(120, 230, 120, 270 )
          canvas.create_line(270, 230, 270, 270 )
          canvas.create_line(670, 230, 670, 270 )
          canvas.create_line(820, 230, 820, 270 )
          canvas.create_line(970, 230, 970, 270 )
          canvas.create_line(1120, 230, 1120, 270)
          canvas.create_line(1120, 270, 1120, 420)
          canvas.create_line(670, 295, 1120, 295)
          canvas.create_line(670, 320, 1120, 320)
          canvas.create_line(670, 345, 1120, 345)
          canvas.create_line(670, 370, 1120, 370)
          canvas.create_line(670, 395, 1120, 395)
          canvas.create_line(670, 420, 1120, 420)

          canvas.create_text(165, 260, text="PROD-0001", fill="black", font=('Helvetica 10'))
          canvas.create_text(400, 260, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(734, 260, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(734, 260, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(734, 260, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(734, 260, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(734, 260, text="$200.00", fill="black", font=('Helvetica 10'))
          canvas.create_text(890, 260, text="1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 260, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 260, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 260, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 260, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          # canvas.create_text(1080, 260, text="$200.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(697, 285, text="Subtotal", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 285, text="$200.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(692, 310, text="TAX1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 310, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 310, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 310, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 310, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1085, 310, text="$18.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(737, 335, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 335, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 335, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 335, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 335, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1085, 335, text="$20.00", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 360, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 360, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 360, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 360, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 360, text="$238.00", fill="black", font=('Helvetica 10 bold'))
          canvas.create_text(715, 360, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 385, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 385, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 385, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 385, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 385, text="100.00", fill="black", font=('Helvetica 10'))
          canvas.create_text(705, 385, text="Total Paid", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 410, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 410, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 410, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 410, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 410, text="$138.00", fill="black", font=('Helvetica 10'))
          canvas.create_text(700, 410, text="Balance", fill="black", font=('Helvetica 10'))

          canvas.create_line(100, 480, 1120, 480, fill="orange")
          canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

          canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          canvas.create_line(100, 600, 1120, 600, fill="orange")
          canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
          canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
      else:
          pass

  adv_win_menu8 = StringVar()
  adv_winstyle8 = ttk.Combobox(seventhtab,textvariable=adv_win_menu8)
  adv_winstyle8.bind("<<ComboboxSelected>>", adv_maindropmenu)
  adv_winstyle8["values"] = ("Professional 1 (logo on left side)","Professional 2 (logo on right side)","Simplified 1 (logo on left side)","Simplified 2 (logo on right side)","Business Classic")
  if not advdata:
    adv_winstyle8.current(0)
    frame = Frame(seventhtab, width=1200, height=155)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=2,y=309)
    canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1200,height=155)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')

    canvas.create_text(600, 45, text="Title text goes here...", fill="black", font=('Helvetica 10'))

    canvas.create_text(250, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

    canvas.create_text(130, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
    canvas.create_text(141, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
    canvas.create_text(130, 160, text="Due date", fill="black", font=('Helvetica 11'))
    canvas.create_text(120, 180, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(134, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(347, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 140, text="03-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 160, text="18-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(340, 180, text="NET 15", fill="black", font=('Helvetica 11'))

    canvas.create_text(1050, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(1080, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
    # T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    # T_address.tag_configure('tag_name',justify='right')
    # T_address.insert('1.0', advdata[2])
    # T_address.tag_add('tag_name','1.0', 'end')
    # T_address_window = canvas.create_window(850, 80, anchor="nw", window=T_address)
    canvas.create_text(1050, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
    # canvas.create_text(1085, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1085, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1080, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1080, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
    canvas.create_text(1050, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))
    canvas.create_text(1050, 210, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))

    canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

    s = ttk.Style()
    s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')
        
    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=150)
    tree.heading("# 1", text="ID/SKU")
    tree.column("# 2", anchor=E, stretch=NO, width=400)
    tree.heading("# 2", text="Product/Service - Description")
    tree.column("# 3", anchor=E, stretch=NO, width=150)
    tree.heading("# 3", text="Quantity")
    tree.column("# 4", anchor=E, stretch=NO, width=150)
    tree.heading("# 4", text="Unit Price")
    tree.column("# 5", anchor=E, stretch=NO, width=150)
    tree.heading("# 5", text="Price")
      
    window = canvas.create_window(120, 290, anchor="nw", window=tree)

    canvas.create_line(120, 330, 1120, 330 )
    canvas.create_line(120, 290, 120, 330 )
    canvas.create_line(270, 290, 270, 330 )
    canvas.create_line(670, 290, 670, 330 )
    canvas.create_line(820, 290, 820, 330 )
    canvas.create_line(970, 290, 970, 330 )
    canvas.create_line(1120, 290, 1120, 330 )
    canvas.create_line(670, 330, 670, 480)
    canvas.create_line(970, 330, 970, 480)
    canvas.create_line(1120, 330, 1120, 480)
    canvas.create_line(670, 355, 1120, 355)
    canvas.create_line(670, 380, 1120, 380)
    canvas.create_line(670, 405, 1120, 405)
    canvas.create_line(670, 430, 1120, 430)
    canvas.create_line(670, 455, 1120, 455)
    canvas.create_line(670, 480, 1120, 480)

    canvas.create_text(165, 320, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(400, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(740, 320, text="1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(884, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(884, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(884, 320, text="$200.00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 320, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 345, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1085, 370, text="$18.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1085, 395, text="$20.00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 420, text="$238.00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 445, text="$100.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 465, text="$138.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))


    canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(110, 600, 1120, 600)
    canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
    canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif advdata[32] == 'Professional 1 (logo on left side)':
    adv_winstyle8.insert(0, advdata[40])
    frame = Frame(seventhtab, width=1200, height=155)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=2,y=309)
    canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1200,height=155)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')

    canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))

    try:
      adv_image = Image.open("images/"+advdata[13])
      adv_resize_image = adv_image.resize((200,75))
      adv_image = ImageTk.PhotoImage(adv_resize_image)

      adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
      adv_window_image = canvas.create_window(150, 30, anchor="nw", window=adv_btlogo)
      adv_btlogo.photo = adv_image
    except:
      pass  

    canvas.create_text(130, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
    canvas.create_text(141, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
    canvas.create_text(130, 160, text="Due date", fill="black", font=('Helvetica 11'))
    canvas.create_text(120, 180, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(134, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(347, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 140, text="03-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 160, text="18-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(340, 180, text="NET 15", fill="black", font=('Helvetica 11'))

    canvas.create_text(1050, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(1080, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', advdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(850, 80, anchor="nw", window=T_address)
        
    canvas.create_text(1050, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
    # canvas.create_text(1085, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1085, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1080, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1080, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
    canvas.create_text(1050, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))
    canvas.create_text(1050, 210, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))

    canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

    s = ttk.Style()
    s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')
        
    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=150)
    tree.heading("# 1", text="ID/SKU")
    tree.column("# 2", anchor=E, stretch=NO, width=400)
    tree.heading("# 2", text="Product/Service - Description")
    tree.column("# 3", anchor=E, stretch=NO, width=150)
    tree.heading("# 3", text="Quantity")
    tree.column("# 4", anchor=E, stretch=NO, width=150)
    tree.heading("# 4", text="Unit Price")
    tree.column("# 5", anchor=E, stretch=NO, width=150)
    tree.heading("# 5", text="Price")
      
    window = canvas.create_window(120, 290, anchor="nw", window=tree)

    canvas.create_line(120, 330, 1120, 330 )
    canvas.create_line(120, 290, 120, 330 )
    canvas.create_line(270, 290, 270, 330 )
    canvas.create_line(670, 290, 670, 330 )
    canvas.create_line(820, 290, 820, 330 )
    canvas.create_line(970, 290, 970, 330 )
    canvas.create_line(1120, 290, 1120, 330 )
    canvas.create_line(670, 330, 670, 480)
    canvas.create_line(970, 330, 970, 480)
    canvas.create_line(1120, 330, 1120, 480)
    canvas.create_line(670, 355, 1120, 355)
    canvas.create_line(670, 380, 1120, 380)
    canvas.create_line(670, 405, 1120, 405)
    canvas.create_line(670, 430, 1120, 430)
    canvas.create_line(670, 455, 1120, 455)
    canvas.create_line(670, 480, 1120, 480)

    canvas.create_text(165, 320, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(400, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(740, 320, text="1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(884, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(884, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(884, 320, text="$200.00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 320, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 345, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1085, 370, text="$18.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1085, 395, text="$20.00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 420, text="$238.00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 445, text="$100.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 465, text="$138.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))


    canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(110, 600, 1120, 600)
    canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
    canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif advdata[32] == 'Professional 2 (logo on right side)':
    adv_winstyle8.insert(0, advdata[40])
    frame = Frame(seventhtab, width=1200, height=155)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=2,y=309)
    canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1200,height=155)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
    canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      adv_image = Image.open("images/"+advdata[13])
      adv_resize_image = adv_image.resize((200,75))
      adv_image = ImageTk.PhotoImage(adv_resize_image)

      adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
      adv_window_image = canvas.create_window(850, 25, anchor="nw", window=adv_btlogo)
      adv_btlogo.photo = adv_image
    except:
      pass  
    #canvas.create_text(1000, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

    canvas.create_text(829, 110, text="Invoice#", fill="black", font=('Helvetica 11'))
    canvas.create_text(841, 130, text="Invoice date", fill="black", font=('Helvetica 11'))
    canvas.create_text(830, 150, text="Due date", fill="black", font=('Helvetica 11'))
    canvas.create_text(820, 170, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(834, 190, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(1047, 110, text="INV1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(1050, 130, text="06-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(1050, 150, text="21-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(1040, 170, text="NET 15", fill="black", font=('Helvetica 11'))

    canvas.create_text(170, 65, text=""+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(130, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', advdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(10, 80, anchor="nw", window=T_address)
    canvas.create_text(125, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
    # canvas.create_text(130, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
    # canvas.create_text(130, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
    # canvas.create_text(136, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
    # canvas.create_text(136, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
    canvas.create_text(124, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

    canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))
    
    s = ttk.Style()
    s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=150)
    tree.heading("# 1", text="ID/SKU")
    tree.column("# 2", anchor=E, stretch=NO, width=400)
    tree.heading("# 2", text="Product/Service - Description")
    tree.column("# 3", anchor=E, stretch=NO, width=150)
    tree.heading("# 3", text="Quantity")
    tree.column("# 4", anchor=E, stretch=NO, width=150)
    tree.heading("# 4", text="Unit Price")
    tree.column("# 5", anchor=E, stretch=NO, width=150)
    tree.heading("# 5", text="Price")
      
    window = canvas.create_window(120, 290, anchor="nw", window=tree)

    canvas.create_line(120, 330, 1120, 330 )
    canvas.create_line(120, 290, 120, 330 )
    canvas.create_line(270, 290, 270, 330 )
    canvas.create_line(670, 290, 670, 330 )
    canvas.create_line(820, 290, 820, 330 )
    canvas.create_line(970, 290, 970, 330 )
    canvas.create_line(1120, 290, 1120, 330 )
    canvas.create_line(670, 330, 670, 480)
    canvas.create_line(970, 330, 970, 480)
    canvas.create_line(1120, 330, 1120, 480)
    canvas.create_line(670, 355, 1120, 355)
    canvas.create_line(670, 380, 1120, 380)
    canvas.create_line(670, 405, 1120, 405)
    canvas.create_line(670, 430, 1120, 430)
    canvas.create_line(670, 455, 1120, 455)
    canvas.create_line(670, 480, 1120, 480)

    canvas.create_text(165, 320, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(400, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(740, 320, text="1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(884, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(884, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 320, text="$200.00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 320, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 345, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1089, 370, text="$18.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1089, 395, text="$20.00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 420, text="$238.00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 445, text="$100.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 465, text="$138.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(110, 600, 1120, 600)
    canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
    canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))


  elif advdata[32] == 'Simplified 1 (logo on left side)':
    adv_winstyle8.insert(0, advdata[40])
    frame = Frame(seventhtab, width=1200, height=155)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=2,y=309)
    canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1200,height=155)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
    canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      adv_image = Image.open("images/"+advdata[13])
      adv_resize_image = adv_image.resize((200,75))
      adv_image = ImageTk.PhotoImage(adv_resize_image)

      adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
      adv_window_image = canvas.create_window(150, 25, anchor="nw", window=adv_btlogo)
      adv_btlogo.photo = adv_image
    except:
      pass  
    #canvas.create_text(250, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

    canvas.create_text(130, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
    canvas.create_text(141, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
    canvas.create_text(130, 160, text="Due date", fill="black", font=('Helvetica 11'))
    canvas.create_text(120, 180, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(134, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(347, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 140, text="06-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 160, text="21-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(340, 180, text="NET 15", fill="black", font=('Helvetica 11'))

    canvas.create_text(1050, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(1080, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', advdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(850, 80, anchor="nw", window=T_address)
    canvas.create_text(1050, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
    # canvas.create_text(1085, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1085, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1080, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1080, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
    canvas.create_text(1050, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

    canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

    s = ttk.Style()
    s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_2.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=700)
    tree.heading("# 1", text="Product/Service - Description")
    tree.column("# 2", anchor=E, stretch=NO, width=150)
    tree.heading("# 2", text="Quantity")
    tree.column("# 3", anchor=E, stretch=NO, width=150)
    tree.heading("# 3", text="Price")
      
    window = canvas.create_window(120, 290, anchor="nw", window=tree)

    canvas.create_line(120, 330, 1120, 330 )
    canvas.create_line(120, 290, 120, 330 )
    canvas.create_line(820, 290, 820, 330 )
    canvas.create_line(970, 290, 970, 330 )
    canvas.create_line(1120, 290, 1120, 330 )
    canvas.create_line(670, 330, 670, 480)
    canvas.create_line(970, 330, 970, 480)
    canvas.create_line(1120, 330, 1120, 480)
    canvas.create_line(670, 355, 1120, 355)
    canvas.create_line(670, 380, 1120, 380)
    canvas.create_line(670, 405, 1120, 405)
    canvas.create_line(670, 430, 1120, 430)
    canvas.create_line(670, 455, 1120, 455)
    canvas.create_line(670, 480, 1120, 480)

    canvas.create_text(250, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(900, 320, text="1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1089, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1089, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(110, 600, 1120, 600)
    canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
    canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif advdata[32] == 'Simplified 2 (logo on right side)':
    adv_winstyle8.insert(0, advdata[40])
    frame = Frame(seventhtab, width=1200, height=155)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=2,y=309)
    canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1200,height=155)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
    canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      adv_image = Image.open("images/"+advdata[13])
      adv_resize_image = adv_image.resize((200,75))
      adv_image = ImageTk.PhotoImage(adv_resize_image)

      adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
      adv_window_image = canvas.create_window(850, 25, anchor="nw", window=adv_btlogo)
      adv_btlogo.photo = adv_image
    except:
      pass  

    # canvas.create_text(1000, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

    canvas.create_text(829, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
    canvas.create_text(841, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
    canvas.create_text(830, 160, text="Due date", fill="black", font=('Helvetica 11'))
    canvas.create_text(820, 180, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(834, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(1047, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(1050, 140, text="06-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(1050, 160, text="21-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(1040, 180, text="NET 15", fill="black", font=('Helvetica 11'))

    canvas.create_text(170, 55, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(135, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', advdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(10, 80, anchor="nw", window=T_address)
    canvas.create_text(130, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
    # canvas.create_text(130, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
    # canvas.create_text(130, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
    # canvas.create_text(136, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
    # canvas.create_text(136, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
    canvas.create_text(124, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

    canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

    s = ttk.Style()
    s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_2.Treeview')
        
    tree.column("# 1", anchor=E, stretch=NO, width=700)
    tree.heading("# 1", text="Product/Service - Description")
    tree.column("# 2", anchor=E, stretch=NO, width=150)
    tree.heading("# 2", text="Quantity")
    tree.column("# 3", anchor=E, stretch=NO, width=150)
    tree.heading("# 3", text="Price")
        
    window = canvas.create_window(120, 290, anchor="nw", window=tree)

    canvas.create_line(120, 330, 1120, 330 )
    canvas.create_line(120, 290, 120, 330 )
    canvas.create_line(820, 290, 820, 330 )
    canvas.create_line(970, 290, 970, 330 )
    canvas.create_line(1120, 290, 1120, 330 )
    canvas.create_line(670, 330, 670, 480)
    canvas.create_line(970, 330, 970, 480)
    canvas.create_line(1120, 330, 1120, 480)
    canvas.create_line(670, 355, 1120, 355)
    canvas.create_line(670, 380, 1120, 380)
    canvas.create_line(670, 405, 1120, 405)
    canvas.create_line(670, 430, 1120, 430)
    canvas.create_line(670, 455, 1120, 455)
    canvas.create_line(670, 480, 1120, 480)

    canvas.create_text(250, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(900, 320, text="1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1089, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1089, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(110, 600, 1120, 600)
    canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
    canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif advdata[32] == 'Business Classic':
    adv_winstyle8.insert(0, advdata[40])
    frame = Frame(seventhtab, width=1200, height=155)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=2,y=309)
    canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1200,height=155)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
    canvas.create_text(600, 45, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_line(100, 60, 1120, 60, fill="orange")
    #canvas.create_line(1000, 60, 600, 60, fill="grey")

    try:
      adv_image = Image.open("images/"+advdata[13])
      adv_resize_image = adv_image.resize((200,100))
      adv_image = ImageTk.PhotoImage(adv_resize_image)

      adv_btlogo = Label(canvas,width=200,height=100,image = adv_image) 
      adv_window_image = canvas.create_window(140, 100, anchor="nw", window=adv_btlogo)
      adv_btlogo.photo = adv_image
    except:
      pass  


    # canvas.create_text(250, 155, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

    canvas.create_text(560, 85, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(535, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', advdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(350, 100, anchor="nw", window=T_address)
    # adv_btlabel = Label(canvas,width=20,height=10,text=""+caddent.get('1.0', 'end-1c')) 
    # adv_window_label = canvas.create_window(530, 110, anchor="nw", window=adv_btlabel)
    canvas.create_text(530, 190, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
    # canvas.create_text(530, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
    # canvas.create_text(530, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
    # canvas.create_text(536, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
    # canvas.create_text(536, 190, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
    canvas.create_text(524, 210, text="Invoice", fill="black", font=('Helvetica 14 bold'))

    canvas.create_text(749, 95, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(791, 110, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(800, 125, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(760, 140, text="United States", fill="black", font=('Helvetica 10'))

    canvas.create_text(745, 160, text="Invoice", fill="black", font=('Helvetica 11'))
    canvas.create_text(760, 180, text="Invoice date", fill="black", font=('Helvetica 11'))
    canvas.create_text(750, 200, text="Due date", fill="black", font=('Helvetica 11'))

    canvas.create_text(947, 160, text="INV1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(950, 180, text="06-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(950, 200, text="21-05-2022", fill="black", font=('Helvetica 11'))
    s = ttk.Style()
    s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
        
    tree.column("# 1", anchor=E, stretch=NO, width=150)
    tree.heading("# 1", text="Product/Service")
    tree.column("# 2", anchor=E, stretch=NO, width=400)
    tree.heading("# 2", text="Description")
    tree.column("# 3", anchor=E, stretch=NO, width=150)
    tree.heading("# 3", text="Unit Price")
    tree.column("# 4", anchor=E, stretch=NO, width=150)
    tree.heading("# 4", text="Quantity")
    tree.column("# 5", anchor=E, stretch=NO, width=150)
    tree.heading("# 5", text="Price")
        
    window = canvas.create_window(120, 230, anchor="nw", window=tree)

    canvas.create_line(120, 270, 1120, 270 )
    canvas.create_line(120, 230, 120, 270 )
    canvas.create_line(270, 230, 270, 270 )
    canvas.create_line(670, 230, 670, 270 )
    canvas.create_line(820, 230, 820, 270 )
    canvas.create_line(970, 230, 970, 270 )
    canvas.create_line(1120, 230, 1120, 270)
    canvas.create_line(1120, 270, 1120, 420)
    canvas.create_line(670, 295, 1120, 295)
    canvas.create_line(670, 320, 1120, 320)
    canvas.create_line(670, 345, 1120, 345)
    canvas.create_line(670, 370, 1120, 370)
    canvas.create_line(670, 395, 1120, 395)
    canvas.create_line(670, 420, 1120, 420)

    canvas.create_text(165, 260, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(400, 260, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(734, 260, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(734, 260, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(734, 260, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(734, 260, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(734, 260, text="$200.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(890, 260, text="1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 260, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 260, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 260, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 260, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(1080, 260, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(697, 285, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 285, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(692, 310, text="TAX1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 310, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 310, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 310, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 310, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1085, 310, text="$18.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(737, 335, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 335, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 335, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 335, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 335, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1085, 335, text="$20.00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 360, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 360, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 360, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 360, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 360, text="$238.00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(715, 360, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 385, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 385, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 385, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 385, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 385, text="100.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(705, 385, text="Total Paid", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 410, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 410, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 410, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 410, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 410, text="$138.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(700, 410, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_line(100, 480, 1120, 480, fill="orange")
    canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(100, 600, 1120, 600, fill="orange")
    canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
    canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  else:
    pass
  adv_winstyle8.place(x=2 ,y=270, width=220)
  #adv_winstyle8.current(0)



   ###################################tab08###########################

  eighttab1=Frame(tab08, relief=GROOVE, bg="#f8f8f2")
  eighttab1.pack(side="top", fill=BOTH)

  eighttab=Frame(eighttab1, bg="#f5f3f2", height=700)
  eighttab.pack(side="top", fill=BOTH)


  sql = "select * from company"
  fbcursor.execute(sql)
  emdata = fbcursor.fetchone()


  lbl01 = Label(eighttab,text="Purchase Order E-Mail Tmplate",font="TimesNewRoman 12 ")
  lbl01.place(x=2,y=20)

  def selected(event):
    paym=em_menu.get()
    print(paym)
    lbl01.place_forget()
    memaiframe.delete("1.0",END) 
    if paym == "Purchase Order E-Mail Template":
      lb1 = Label(eighttab,text='Purchase Order E-Mail Template',font="TimesNewRoman 12 ")
      lb1.place(x=2,y=20)

      def select_list(event):
        memaiframe.insert('1.0',lbx.get(ANCHOR))
      lbx = Listbox(eighttab,  height=29, width=34)
      lbx.insert(END, "{{Company_Name}}")
      lbx.insert(END, "{{Company_Address}}")
      lbx.insert(END, "{{Company_Email1}}")
      lbx.insert(END, "{{Customer_Name}}")
      lbx.insert(END, "{{Customer_Address}}")
      lbx.insert(END, "{{Customer_Email}}")
      lbx.insert(END, "{{Purchase_Order_Number}}")
      lbx.insert(END, "{{Purchase_Order_Date}}")
      lbx.insert(END, "{{Purchase_Order_Total}}")
      lbx.insert(END, "{{Current_date}}")
      lbx.place(x=1090, y=46)
      lbx.bind('<Double-1>', select_list)
    

    elif paym == "Estimate E-Mail Template":
      lb4 = Label(eighttab,text='Estimate E-Mail Template  ',font="TimesNewRoman 12 ")
      lb4.place(x=2,y=20)

      def select_list(event):
        memaiframe.insert('1.0',lbx.get(ANCHOR))
      lbx = Listbox(eighttab,  height=29, width=34)
      lbx.insert(END, "{{Company_Name}}")
      lbx.insert(END, "{{Company_Address}}")
      lbx.insert(END, "{{Company_Email1}}")
      lbx.insert(END, "{{Customer_Name}}")
      lbx.insert(END, "{{Customer_Address}}")
      lbx.insert(END, "{{Customer_Email}}")
      lbx.insert(END, "{{Estimate_Number}}")
      lbx.insert(END, "{{Estimate_Date}}")  
      lbx.insert(END, "{{Estimate_Total}}")
      lbx.insert(END, "{{Estimate_Balance}}")
      lbx.insert(END, "{{Current_date}}")
      lbx.place(x=1090, y=46)
      lbx.bind('<Double-1>', select_list)



    
    elif paym == "Order E-Mail Template":

      lb2 = Label(eighttab,text='Order E-Mail Template      ',font="TimesNewRoman 13 ")
      lb2.place(x=2,y=20)

      def select_list(event):
        memaiframe.insert('1.0',lbx.get(ANCHOR))
      lbx = Listbox(eighttab,  height=29, width=34)
      lbx.insert(END, "{{Company_Name}}")
      lbx.insert(END, "{{Company_Address}}")
      lbx.insert(END, "{{Company_Email1}}")
      lbx.insert(END, "{{Customer_Name}}")
      lbx.insert(END, "{{Customer_Address}}")
      lbx.insert(END, "{{Customer_Email}}")
      lbx.insert(END, "{{Order_Number}}")
      lbx.insert(END, "{{Order_Date}}")
      lbx.insert(END, "{{Order_Total}}")
      lbx.insert(END, "{{Order_Balance}}")
      lbx.insert(END, "{{Current_date}}")
      lbx.place(x=1090, y=46)
      lbx.bind('<Double-1>', select_list)
      

      
    elif paym == "Invoice E-Mail Template":
      lb3 = Label(eighttab,text='Invoice E-Mail Template     ',font="TimesNewRoman 12 ")
      lb3.place(x=2,y=20)

      def select_list(event):
        memaiframe.insert('1.0',lbx.get(ANCHOR))
      lbx = Listbox(eighttab,  height=29, width=34)
      lbx.insert(END, "{{Company_Name}}")
      lbx.insert(END, "{{Company_Address}}")
      lbx.insert(END, "{{Company_Email1}}")
      lbx.insert(END, "{{Customer_Name}}")
      lbx.insert(END, "{{Customer_Address}}")
      lbx.insert(END, "{{Customer_Email}}")
      lbx.insert(END, "{{Invoice_Number}}")
      lbx.insert(END, "{{Invoice_Date}}")
      lbx.insert(END, "{{Invoice_Due_Date}}")
      lbx.insert(END, "{{Invoice_OrderRef}}")
      lbx.insert(END, "{{Invoice_Total}}")
      lbx.insert(END, "{{Invoice_TotalPaid}}")
      lbx.insert(END, "{{Invoice_Balance}}")
      lbx.insert(END, "{{Current_date}}")
      lbx.place(x=1090, y=46)
      lbx.bind('<Double-1>', select_list)
  
     
    elif paym == "Payment Receipt Template":
      lb5 = Label(eighttab,text='Payment Receipt Template',font="TimesNewRoman 12 ")
      lb5.place(x=2,y=20)

      def select_list(event):
        memaiframe.insert('1.0',lbx.get(ANCHOR))
      lbx = Listbox(eighttab,  height=29, width=34)
      lbx.insert(END, "{{Company_Name}}")
      lbx.insert(END, "{{Company_Address}}")
      lbx.insert(END, "{{Company_Email1}}")
      lbx.insert(END, "{{Customer_Name}}")
      lbx.insert(END, "{{Customer_Address}}")
      lbx.insert(END, "{{Customer_Email}}")
      lbx.insert(END, "{{Invoice_Number}}")
      lbx.insert(END, "{{Invoice_Date}}")
      lbx.insert(END, "{{Invoice_Due_Date}}")
      lbx.insert(END, "{{Invoice_OrderRef}}")
      lbx.insert(END, "{{Invoice_Total}}")
      lbx.insert(END, "{{Invoice_TotalPaid}}")
      lbx.insert(END, "{{Invoice_Balance}}")
      lbx.insert(END, "{{Current_date}}")
      lbx.insert(END, "{{Currency_Sign}}")
      lbx.insert(END, "{{Payment_Date}}")
      lbx.insert(END, "{{Payment_Amount}}")
      lbx.insert(END, "{{Payment_Mode}}")
      lbx.insert(END, "{{Payment_Description}}")
      lbx.insert(END, "{{Payment_ID}}")
      lbx.place(x=1090, y=46)
      lbx.bind('<Double-1>', select_list)
      memaiframe.insert('1.0','Dear {{Customer_Name}},\n\nThis message is to inform you that your payment of {{Currency_Sign}}{{Payment_Amount}} {{Currency}} for Invoice# {{Invoice_Number}} has been received."\n\nInvoice ID: {{Invoice_Number}}\nPayment Date: {{Payment_Date}}\nAmount: {{Currency_Sign}}{{Payment_Amount}} {{Currency}}\nPaid by: {{Payment_Mode}}\nDescription: {{Payment_Description}}\n\nThank you for your business.\n{{Company_Name}}')


  fontSize=12
  fontStyle='arial'
  def font_style(event):
    global fontStyle
    fontStyle=font_family__variable.get()
    memaiframe.config(font=(fontStyle,fontSize))

  def font_size(event):
    global fontSize
    fontSize=size_variable.get()
    memaiframe.config(font=(fontStyle,fontSize))

  def bold_text():
    bold_font = font.Font(memaiframe, memaiframe.cget("font"))
    bold_font.configure(weight="bold")
    memaiframe.tag_configure("bold", font=bold_font)
    current_tags = memaiframe.tag_names("sel.first")
    if "bold" in current_tags:
      memaiframe.tag_remove("bold", "sel.first", "sel.last")
    else:
      memaiframe.tag_add("bold", "sel.first", "sel.last")
   
  
  def italic_text():
    italic_font = font.Font(memaiframe, memaiframe.cget("font"))
    italic_font.configure(slant="italic")
    memaiframe.tag_configure("italic", font=italic_font)
    current_tags = memaiframe.tag_names("sel.first")
    if "italic" in current_tags:
      memaiframe.tag_remove("italic", "sel.first", "sel.last")
    else:
      memaiframe.tag_add("italic", "sel.first", "sel.last")


  def underline_text():
    try:
        if memaiframe.tag_nextrange('underline_selection', 'sel.first', 'sel.last') != ():
            memaiframe.tag_remove('underline_selection', 'sel.first', 'sel.last')
        else:
            memaiframe.tag_add('underline_selection', 'sel.first', 'sel.last')
            memaiframe.tag_configure('underline_selection', underline=True)
    except TclError:
        pass

  def color_select():
    color=colorchooser.askcolor()[1]
    if color:
      color_font = font.Font(memaiframe, memaiframe.cget("font"))
      memaiframe.tag_configure("colored", font=color_font, foreground=color)
      current_tags = memaiframe.tag_names("sel.first")
      if "colored" in current_tags:
        memaiframe.tag_remove("colored", "sel.first", "sel.last")
      else:
        memaiframe.tag_add("colored", "sel.first", "sel.last")

  def align_right():
    data=memaiframe.get(0.0,END)
    memaiframe.tag_config('right',justify=RIGHT)
    memaiframe.delete(0.0,END)
    memaiframe.insert(INSERT,data,'right')

  def align_left():
    data=memaiframe.get(0.0,END)
    memaiframe.tag_config('left',justify=LEFT)
    memaiframe.delete(0.0,END)
    memaiframe.insert(INSERT,data,'left')

  def align_center():
    data=memaiframe.get(0.0,END)
    memaiframe.tag_config('center',justify=CENTER)
    memaiframe.delete(0.0,END)
    memaiframe.insert(INSERT,data,'center')

  em_menu = StringVar()
  winstyle = ttk.Combobox(eighttab,textvariable=em_menu,width=28)
  winstyle['values'] = ('Invoice E-Mail Template','Order E-Mail Template','Estimate E-Mail Template','Payment Receipt Template','Purchase Order E-Mail template')
  winstyle.bind("<<ComboboxSelected>>",selected)
  if  not emdata:
    pass
  else:
    print(emdata)
    winstyle.insert(0, emdata[2])
  winstyle.place(x=280 ,y=20)
  winstyle.current(4)



  # savebtn=Button(eighttab,image=saves,text="Save Settings",compound = LEFT, height=15, width=100)
  # savebtn.place(x=500, y=20)


    
  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", width=78, padding=10)
  mess_Notebook = ttk.Notebook(eighttab)
  emailmessage_Frame = Frame(mess_Notebook, height=430, width=1060)
  mess_Notebook.add(emailmessage_Frame, text="E-mail message")
  mess_Notebook.place(x=5, y=50)

  meframe = StringVar()
  memaiframe=Text(emailmessage_Frame,font=('arial 17'),undo=True,width=130,height=400)
  if not emdata:
    pass
  else:
    memaiframe.insert('1.0', emdata[53])
  memaiframe.pack(padx=0,pady=28,expand=False)


  scrollbar1 = Scrollbar(emailmessage_Frame,orient=VERTICAL)
  scrollbar2= Scrollbar(memaiframe,orient=HORIZONTAL,command=memaiframe.xview,width=0)
  scrollbar2.pack(fill=X,expand=True,side=BOTTOM,padx=502,pady=188)
  memaiframe.config(xscrollcommand=scrollbar2.set)
  memaiframe.config(yscrollcommand=scrollbar1.set)
  scrollbar1.config(command=memaiframe.yview)
  scrollbar1.place(x =1040, y=0, height=432)
  scrollbar2.config(command=memaiframe.xview)
  scrollbar3= Scrollbar(emailmessage_Frame,orient=HORIZONTAL,command=memaiframe.xview, width=0)
  scrollbar3.place(x=0, y=410, height=20,width=1040)

 
  

  btn1=Button(emailmessage_Frame,width=20,height=20,compound = LEFT,image=selectall,command=lambda :memaiframe.event_generate('<Control a>'))
  btn1.place(x=5, y=1)

        
  btn2=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut,command=lambda :memaiframe.event_generate('<Control x>'))
  btn2.place(x=36, y=1)

  btn3=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy,command=lambda :memaiframe.event_generate('<Control c>'))
  btn3.place(x=73, y=1)

  btn4=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste,command=lambda :memaiframe.event_generate('<Control v>'))
  btn4.place(x=105, y=1)

  btn5=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo, command=lambda:memaiframe.event_generate("<<Undo>>"))
  btn5.place(x=140, y=1)

  btn6=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo, command=lambda:memaiframe.event_generate("<<Redo>>"))
  btn6.place(x=175, y=1)

  btn7=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold,command=bold_text)
  btn7.place(x=210, y=1)

  btn8=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics,command=italic_text)
  btn8.place(x=245, y=1)

  btn9=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline,command=underline_text)
  btn9.place(x=280, y=1)

  btn10=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=left,command=align_left)
  btn10.place(x=315, y=1)

  btn11=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=right,command=align_right)
  btn11.place(x=350, y=1)

  btn12=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=center,command=align_center)
  btn12.place(x=385, y=1)

  # btn13=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink,command=open)
  # btn13.place(x=420, y=1)
        
  btn14=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove,command=lambda :memaiframe.delete(0.0,END))
  btn14.place(x=420, y=1)

  btn15=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=color,command=color_select)
  btn15.place(x=455, y=1)

  # btn16=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=save,command=save_file)
  # btn16.place(x=525, y=1)
 

  size_variable=IntVar()
  compo = ttk.Combobox(emailmessage_Frame, width=14,textvariable=size_variable,values=tuple(range(10,80)))
  compo['values'] =('11','12','13','14','15','16','17')
  compo.place(x=600, y=5)
  compo.current(4)

  compo.bind('<<ComboboxSelected>>',font_size)


  font_families=font.families()
  font_family__variable=StringVar()

  def select(event):
    memaiframe.insert('1.0',lbx01.get(ANCHOR))

  attachlbframe=LabelFrame(eighttab,text="placeholders(double click to insert)", height=500, width=233)
  attachlbframe.place(x=1080, y=22)

  lbx01 = Listbox(eighttab, height=28, width=34)
  lbx01.insert(END, "{{Company_Name}}")
  lbx01.insert(END, "{{Company_Address}}")
  lbx01.insert(END, "{{Company_Email1}}")
  lbx01.insert(END, "{{Customer_Name}}")
  lbx01.insert(END, "{{Customer_Address}}")
  lbx01.insert(END, "{{Customer_Email}}")
  lbx01.insert(END, "{{Purchase_Order_Number}}")
  lbx01.insert(END, "{{Purchase_Order_Date}}")
  lbx01.insert(END, "{{Purchase_Order_Total}}")
  lbx01.insert(END, "{{Current_date}}")
  lbx01.place(x=1090, y=46)
  lbx01.bind('<Double-1>', select)

     

################################### tab09 ###########################


  ninetab1=Frame(tab09, relief=GROOVE, bg="#f8f8f2")
  ninetab1.pack(side="top", fill=BOTH)
  ninetab=Frame(ninetab1, bg="#f5f3f2", height=700)
  ninetab.pack(side="top", fill=BOTH)

  global filename_btn,filename_logo

  filename_btn = ""
  filename_logo = ""
  def payments():
    checkbtn1 = showpaidbol.get()
    checkbtn2 = sendpaybol.get()                        
    checkbtn3 = insrtpaybol.get()
    checkbtn4 =attachupdbol.get()
    payrece = enterec.get()
    payin = enterin.get()
    amrece = camou.get()
    des = descr.get()
    paymentrece = payrec.get()
    receipt = paym.get()
    date = payd.get()
    pay_amount = payma.get()
    total = tota.get()
    total_paid = paid.get()
    balance_due = due.get()
    payment_prefix = receipt_prefix.get()

    sql = "select * from payments"
    fbcursor.execute(sql)
    i = fbcursor.fetchall()
    if not i:
      if filename_btn == "":
        print(12)
        sql = 'insert into payments(show_paid,send_payment,insert_paypal,attach_updated,payment_receipt,payment_invoice,amount_received,description,payment_received,payment_rece,payment_date,payment_amount,total_amount,total_paid,balance_due,prefix) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        val = (checkbtn1,checkbtn2,checkbtn3,checkbtn4,payrece,payin,amrece,des,paymentrece,receipt,date,pay_amount,total,total_paid,balance_due,payment_prefix)
        fbcursor.execute(sql, val)
        fbilldb.commit()
      else:
        shutil.copyfile(filename_btn, os.getcwd()+'/images/'+filename_btn.split('/')[-1])
        sql = 'insert into payments(show_paid,send_payment,insert_paypal,attach_updated,payment_receipt,payment_invoice,amount_received,description,payment_received,payment_rece,payment_date,payment_amount,total_amount,total_paid,balance_due,prefix,load_button) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        val = (checkbtn1,checkbtn2,checkbtn3,checkbtn4,payrece,payin,amrece,des,paymentrece,receipt,date,pay_amount,total,total_paid,balance_due,payment_prefix,filename_btn.split('/')[-1])
        fbcursor.execute(sql, val)
        fbilldb.commit()
        try:
          shutil.copyfile(filename_logo, os.getcwd()+'/images/'+filename_logo.split('/')[-1])
          sql = "update payments set show_paid=%s, send_payment=%s, insert_paypal=%s,attach_updated=%s,payment_receipt=%s,payment_invoice=%s,amount_received=%s,description=%s,payment_received=%s,payment_rece=%s,payment_date=%s,payment_amount=%s,total_amount=%s,total_paid=%s,balance_due=%s,prefix=%s,load_logo=%s"
          val = (checkbtn1,checkbtn2,checkbtn3,checkbtn4,payrece,payin,amrece,des,paymentrece,receipt,date,pay_amount,total,total_paid,balance_due,payment_prefix,filename_logo.split('/')[-1])
          fbcursor.execute(sql, val)
          fbilldb.commit()
        except:
          pass
    else:
      if filename_btn == "":
        sql = "update payments set show_paid=%s, send_payment=%s, insert_paypal=%s,attach_updated=%s,payment_receipt=%s,payment_invoice=%s,amount_received=%s,description=%s,payment_received=%s,payment_rece=%s,payment_date=%s,payment_amount=%s,total_amount=%s,total_paid=%s,balance_due=%s,prefix=%s"
        val = (checkbtn1,checkbtn2,checkbtn3,checkbtn4,payrece,payin,amrece,des,paymentrece,receipt,date,pay_amount,total,total_paid,balance_due,payment_prefix)
        fbcursor.execute(sql, val)
        fbilldb.commit()
      else:
        shutil.copyfile(filename_btn, os.getcwd()+'/images/'+filename_btn.split('/')[-1])
        sql = "update payments set show_paid=%s, send_payment=%s, insert_paypal=%s,attach_updated=%s,payment_receipt=%s,payment_invoice=%s,amount_received=%s,description=%s,payment_received=%s,payment_rece=%s,payment_date=%s,payment_amount=%s,total_amount=%s,total_paid=%s,balance_due=%s,prefix=%s,load_button=%s"
        val = (checkbtn1,checkbtn2,checkbtn3,checkbtn4,payrece,payin,amrece,des,paymentrece,receipt,date,pay_amount,total,total_paid,balance_due,payment_prefix,filename_btn.split('/')[-1])
        fbcursor.execute(sql, val)
        fbilldb.commit()
        try:
          shutil.copyfile(filename_logo, os.getcwd()+'/images/'+filename_logo.split('/')[-1])
          sql = "update payments set show_paid=%s, send_payment=%s, insert_paypal=%s,attach_updated=%s,payment_receipt=%s,payment_invoice=%s,amount_received=%s,description=%s,payment_received=%s,payment_rece=%s,payment_date=%s,payment_amount=%s,total_amount=%s,total_paid=%s,balance_due=%s,prefix=%s,load_logo=%s"
          val = (checkbtn1,checkbtn2,checkbtn3,checkbtn4,payrece,payin,amrece,des,paymentrece,receipt,date,pay_amount,total,total_paid,balance_due,payment_prefix,filename_logo.split('/')[-1])
          fbcursor.execute(sql, val)
          fbilldb.commit()
        except:
          pass
          

  sql = "select * from payments"
  fbcursor.execute(sql)
  padata = fbcursor.fetchone()

    
  showpaidbol =  IntVar()
  showp = Checkbutton(ninetab,variable=showpaidbol,
                      text="Show 'PAID' image on fully paid invoices",
                      onvalue= 1 ,
                      offvalue= 0,
                    )
  showp.place(x=5,y=20)
  if  not padata:
        pass
  else:
    if padata[2] == 1:
      showp.select()
    else:
      showp.deselect()



      
  sendpaybol =  IntVar()
  sendp = Checkbutton(ninetab,variable=sendpaybol,
                        text="Send payment receipt email after payment recorderd",
                        onvalue= 1 ,
                        offvalue= 0,
                    )
  sendp.place(x=5,y=50)
  if  not padata:
    pass
  else:
    if padata[3] == 1:
      sendp.select()
    else:
      sendp.deselect()


  insrtpaybol =  IntVar()
  insert = Checkbutton(ninetab,variable=insrtpaybol,
                        text="Insert PayPal 'Pay Now' button with the remaining balance on unpaid PDF invoices",
                        onvalue= 1 ,
                        offvalue= 0,
                      )
  insert.place(x=340,y=20)
  if  not padata:
        pass
  else:
    if padata[4] == 1:
      insert.select()
    else:
      insert.deselect()



  attachupdbol =  IntVar()
  attach = Checkbutton(ninetab,variable=attachupdbol,
                        text="Attach updated invoice to payment receipt email",
                        onvalue= 1 ,
                        offvalue= 0,
                      )
  attach.place(x=340,y=50)
  if  not padata:
        pass
  else:
    if padata[5] == 1:
      attach.select()
    else:
      attach.deselect()


    
  messagelbframe=LabelFrame(ninetab,text="Payment Receipt Text Labels", height=400, width=460)
  messagelbframe.place(x=5, y=100)

  enterec = StringVar()
  pnr = Label(ninetab,text="Payment Receipt")
  pnr.place(x=15,y=130)
  enrec = Entry(ninetab,textvariable=enterec,width=30)
  if  not padata:
    enterec.set('Payment Receipt')
  else:
    enrec.insert(0, padata[6])
  enrec.place(x=15,y=160)


  enterin = StringVar()
  enin = Label(ninetab,text="Payment for Invoice#")
  enin.place(x=15,y=190)
  newin = Entry(ninetab,textvariable=enterin,width=30)
  if  not padata:
    enterin.set('Payment for Invoice#')
  else:
    newin.insert(0, padata[7])
  newin.place(x=15,y=215)

    
  camou = StringVar()
  carf = Label(ninetab,text="Amount received from:")
  carf.place(x=15,y=245)
  camrf = Entry(ninetab,textvariable=camou,width=30)
  if  not padata:
    camou.set('Amount received from:')
  else:
    camrf.insert(0, padata[8])
  camrf.place(x=15,y=270)
  

  descr = StringVar()
  des = Label(ninetab,text="Description:")
  des.place(x=15,y=300)
  descrip = Entry(ninetab,textvariable=descr,width=30)
  if  not padata:
    descr.set('Description:')
  else:
    descrip.insert(0, padata[9])
  descrip.place(x=15,y=325)

  payrec = StringVar()
  pay = Label(ninetab,text="Payment Received in:")
  pay.place(x=15,y=355)
  payrecin = Entry(ninetab,textvariable=payrec,width=30)
  if  not padata:
    payrec.set('Payment Received in:')
  else:
    payrecin.insert(0, padata[10])
  payrecin.place(x=15,y=380)

  paym = StringVar()
  payr = Label(ninetab,text="Payment Receipt#:")
  payr.place(x=15,y=410)
  paymr = Entry(ninetab,textvariable=paym,width=30)
  if  not padata:
    paym.set('Payment Receipt#:')
  else:
    paymr.insert(0, padata[11])
  paymr.place(x=15,y=435)

  payd = StringVar()
  payda = Label(ninetab,text="Payment Date:")
  payda.place(x=250,y=130)
  paydate = Entry(ninetab,textvariable=payd,width=30)
  if  not padata:
    payd.set('Payment Date:')
  else:
    paydate.insert(0, padata[12])
  paydate.place(x=250,y=160)
    
  payma = StringVar()
  pya = Label(ninetab,text="Payment Amount:")
  pya.place(x=250,y=190)
  paymam = Entry(ninetab,textvariable=payma,width=30)
  if  not padata:
    payma.set('Payment Amount:')
  else:
    paymam.insert(0, padata[13])
  paymam.place(x=250,y=215)
    
    
  tota = StringVar()
  tad = Label(ninetab,text="Total Amount Due")
  tad.place(x=250,y=245)
  totamo = Entry(ninetab,textvariable=tota,width=30)
  if  not padata:
    tota.set('Total Amount Due')
  else:
    totamo.insert(0, padata[14])
  totamo.place(x=250,y=270)

  paid = StringVar()
  totp = Label(ninetab,text="Total Paid:")
  totp.place(x=250,y=300)
  totpai = Entry(ninetab,textvariable=paid,width=30)
  if  not padata:
    paid.set('Total Paid:')
  else:
    totpai.insert(0, padata[15])
  totpai.place(x=250,y=325)

  due = StringVar()
  bdue = Label(ninetab,text="Balance Due")
  bdue.place(x=250,y=355)
  badue = Entry(ninetab,textvariable=due,width=30)
  if  not padata:
    due.set('Balance Due')
  else:
    badue.insert(0, padata[16])
  badue.place(x=250,y=380)

  receipt_prefix = StringVar()
  pprefix = Label(ninetab,text="Payment Receipt Prefix")
  pprefix.place(x=250,y=410)
  prprefix = Entry(ninetab,textvariable=receipt_prefix,width=30)
  if  not padata:
    receipt_prefix.set('RCPT')
  else:
    prprefix.insert(0, padata[17])
  prprefix.place(x=250,y=435)

  savebtn = Button(ninetab,text="Save Settings",width=12,command=payments)
  savebtn.place(x=40,y=470)

  def restore():
    enterec = StringVar()
    pnr = Label(ninetab,text="Payment Receipt")
    pnr.place(x=15,y=130)
    enrec = Entry(ninetab,textvariable=enterec,width=30)
    enrec.place(x=15,y=160)
    enterec.set('Payment Receipt')


    enterin = StringVar()
    enin = Label(ninetab,text="Payment for Invoice#")
    enin.place(x=15,y=190)
    newin = Entry(ninetab,textvariable=enterin,width=30)
    newin.place(x=15,y=215)
    enterin.set('Payment for Invoice#')
  
  
    camou = StringVar()
    carf = Label(ninetab,text="Amount received from:")
    carf.place(x=15,y=245)
    camrf = Entry(ninetab,textvariable=camou,width=30)
    camrf.place(x=15,y=270)
    camou.set('Amount received from:')


    descr = StringVar()
    des = Label(ninetab,text="Description:")
    des.place(x=15,y=300)
    descrip = Entry(ninetab,textvariable=descr,width=30)
    descrip.place(x=15,y=325)
    descr.set('Description:')


    payrec = StringVar()
    pay = Label(ninetab,text="Payment Received in:")
    pay.place(x=15,y=355)
    payrecin = Entry(ninetab,textvariable=payrec,width=30)
    payrecin.place(x=15,y=380)
    payrec.set('Payment Received in:')


    paym = StringVar()
    payr = Label(ninetab,text="Payment Receipt#:")
    payr.place(x=15,y=410)
    paymr = Entry(ninetab,textvariable=paym,width=30)
    paymr.place(x=15,y=435)
    paym.set('Payment Receipt#:')


    payd = StringVar()
    payda = Label(ninetab,text="Payment Date:")
    payda.place(x=250,y=130)
    paydate = Entry(ninetab,textvariable=payd,width=30)
    paydate.place(x=250,y=160)
    payd.set('Payment Date:')
    
    payma = StringVar()
    pya = Label(ninetab,text="Payment Amount:")
    pya.place(x=250,y=190)
    paymam = Entry(ninetab,textvariable=payma,width=30)
    paymam.place(x=250,y=215)
    payma.set('Payment Amount:')
    
    
    tota = StringVar()
    tad = Label(ninetab,text="Total Amount Due")
    tad.place(x=250,y=245)
    totamo = Entry(ninetab,textvariable=tota,width=30)
    totamo.place(x=250,y=270)
    tota.set('Total Amount Due')

    paid = StringVar()
    totp = Label(ninetab,text="Total Paid:")
    totp.place(x=250,y=300)
    totpai = Entry(ninetab,textvariable=paid,width=30)
    totpai.place(x=250,y=325)
    paid.set('Total Paid:')

    due = StringVar()
    bdue = Label(ninetab,text="Balance Due")
    bdue.place(x=250,y=355)
    badue = Entry(ninetab,textvariable=due,width=30)
    badue.place(x=250,y=380)
    due.set('Balance Due')

    receipt_prefix = StringVar()
    pprefix = Label(ninetab,text="Payment Receipt Prefix")
    pprefix.place(x=250,y=410)
    prprefix = Entry(ninetab,textvariable=receipt_prefix,width=30)
    prprefix.place(x=250,y=435)
    receipt_prefix.set('RCPT')


  restrbtn = Button(ninetab,text="Restore defaults",command=restore)
  restrbtn.place(x=290,y=470)


  paidim=LabelFrame(ninetab,text="PAID Image for Invoices (max: 40mm X 25mm)", height=250, width=300)
  paidim.place(x=500, y=100)
  filename_btn=""  
  def upload_btnimg():
    global btnimg,filename_btn
    f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
    filename_btn= filedialog.askopenfilename(filetypes=f_types)
    shutil.copyfile(filename_btn, os.getcwd()+'/images/'+filename_btn.split('/')[-1])
    image = Image.open(filename_btn)
    resize_image = image.resize((280, 160))
    btnimg = ImageTk.PhotoImage(resize_image)
   # b2 = Button(ninetab,image=img)
   # b2.place(x=130, y=80)
    
    btlogo = Button(ninetab,width=280,height=160,image=btnimg)
    btlogo.place(x=505,y=120)
    
  try:
    image = Image.open("images/"+padata[19])
    resize_image = image.resize((280, 160))
    image = ImageTk.PhotoImage(resize_image)
    btlogoi = Button(ninetab,width=280,height=160,image=image)
    btlogoi.place(x=505,y=120)
    btlogoi.photo = image
  except:
    pass
 
  def paid_logo():

    paid_sett = Image.open("images/paid.png")
    resize_image_paid = paid_sett.resize((280, 160))
    paid_sett = ImageTk.PhotoImage(resize_image_paid)
    btclogo = Button(ninetab,width=280,height=160,image=paid_sett)
    btclogo.place(x=505,y=120)
    btclogo.photo = paid_sett
    
  btnimg = BooleanVar()      
  btloadima = Button(ninetab,text="Load logo image",command=upload_btnimg)
  btloadima.place(x=510,y=310)

  restrbttn = Button(ninetab,text="Restore defaults",command=paid_logo)
  restrbttn.place(x=690,y=310)


  butnimg=LabelFrame(ninetab,text="PayPal Image for Invoices (max: 40mm X 10mm)", height=130, width=300)
  butnimg.place(x=500, y=370)
    
  def upload_fileimg_logo():
    global logo_img,filename_logo
    f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
    filename_logo = filedialog.askopenfilename(filetypes=f_types)
    shutil.copyfile(filename_logo, os.getcwd()+'/images/'+filename_logo.split('/')[-1])
    image = Image.open(filename_logo)
    resize_image = image.resize((280, 55))
    logo_img = ImageTk.PhotoImage(resize_image)
    # b2 = Button(secondtab,image=img)
    # b2.place(x=130, y=80)
    
    btlogo = Button(ninetab,width=280,height=55,image=logo_img)
    btlogo.place(x=506,y=390)

  try:
    image = Image.open("images/"+padata[18])
    resize_image = image.resize((280, 55))
    image = ImageTk.PhotoImage(resize_image)
    bt_logo = Button(ninetab,width=280,height=55,image=image)
    bt_logo.place(x=506,y=390)
    bt_logo.photo = image
  except:
    pass
    

  
    
  def paynow_logo():
      image_paynow = Image.open("images/paynow.png")
      resize_image_paynow = image_paynow.resize((280, 55))
      image_paynow = ImageTk.PhotoImage(resize_image_paynow)
      btlogoi = Button(ninetab,width=280,height=55,image=image_paynow)
      btlogoi.place(x=506,y=390)
      btlogoi.photo = image_paynow

    
  btloadima = Button(ninetab,text="Load logo image",command=upload_fileimg_logo)
  btloadima.place(x=510,y=460)

  restrbttn = Button(ninetab,text="Restore defaults",command=paynow_logo)
  restrbttn.place(x=690,y=460)


  ################### tab010 ###################################

  tentab1=Frame(tab010, relief=GROOVE, bg="#f8f8f2")
  tentab1.pack(side="top", fill=BOTH)

  tentab=Frame(tentab1, bg="#f5f3f2", height=700)
  tentab.pack(side="top", fill=BOTH)


  sql = "select * from company"
  fbcursor.execute(sql)
  podata = fbcursor.fetchone()
  

  pver = Label(tentab,text="Purchase order# prefix")
  pver.place(x=15,y=25)

  prefix_str = StringVar()
  pre_entry = Entry(tentab,textvariable=prefix_str)
  pre_entry.place(x=16,y=50)
  if not podata:
    prefix_str.set('P.ORD')
  else:
    pre_entry.insert(0, podata[41])


  ver1 = Label(tentab,text="Starting purchase order number")
  ver1.place(x=15,y=75)

  def spincall(input):
        
    if input.isdigit():
      print(input)
      return True

    elif input is  "":
      print(input)
      return True

    else:
      print(input)
      return False
    

  pspin2 = Spinbox(tentab,from_=0,to=1000000,width=16)
  regi = tentab.register(spincall)

  pspin2.config(validate = "key",
               validatecommand = (regi, '%S'))
  if not podata:
    pass
  else:
    pspin2.delete(0,END)
    pspin2.insert(0,podata[43])
    pspin2.place(x=16,y=100)

    
              

  ver2 = Label(tentab,text="Header box background color")
  ver2.place(x=15,y=140)

  pwin_menu = StringVar()
  colbox = ttk.Combobox(tentab,textvariable=pwin_menu,width=27)
 # pord_win = pwin_menu.get()
  colbox['values'] = ('Default','Black','Maroon','Green','Olive','Navy','Purple','Teal','Gray','Silver','Red','Lime','Yellow','Blue','Fuchsia','Aqua','White','ScrollBar','Background','ActiveCaption','InactiveCaption','Menu','Window','WindowFrame','MenuText','WindowText','CaptionText','ActiveBorder','InactiveBorder','AppWorkSpace','Highlight','HighlightText','BtnFace','InactiveCaptionText','BtnHighlight','3DDkShadow','3DLight','InfoText','InfoBk','Custom')
  if not podata:
    colbox.current(2)
  else:
    colbox.insert(0, podata[42])
  colbox.place(x=15 ,y=160)

  ver3 = Label(tentab,text="Customize purchase order text labels")
  ver3.place(x=15,y=190)

  pord_str1 = StringVar() 
  pord_lbx1 = Entry(tentab, width=30,textvariable=pord_str1)
  if not podata:
    pord_str1.set('Purchase Order')
  else:
    pord_lbx1.insert(0, podata[44])
  pord_lbx1.place(x=15,y=220)
  

  pord_str2 = StringVar() 
  pord_lbx2 = Entry(tentab, width=30,textvariable=pord_str2)
  if not podata:
    pord_str2.set('P.Order#')
  else:
    pord_lbx2.insert(0, podata[45])
  pord_lbx2.place(x=15,y=240)

  pord_str3 = StringVar() 
  pord_lbx3 = Entry(tentab,width=30,textvariable=pord_str3)
  if not podata:
    pord_str3.set('P.Order Date')
  else:
    pord_lbx3.insert(0, podata[46])
  pord_lbx3.place(x=15,y=260)

  pord_str4 = StringVar() 
  pord_lbx4 = Entry(tentab,width=30,
  textvariable=pord_str4)
  if not podata:
    pord_str4.set('Due date')
  else:
    pord_lbx4.insert(0, podata[47])
  pord_lbx4.place(x=15,y=280)


  pord_str5 = StringVar() 
  pord_lbx5 = Entry(tentab,width=30,textvariable=pord_str5)
  if not podata:
    pord_str5.set('Vendor')
  else:
    pord_lbx5.insert(0, podata[48])
  pord_lbx5.place(x=15,y=300)

  pord_str6 = StringVar() 
  pord_lbx6 = Entry(tentab, width=30,textvariable=pord_str6)
  if not podata:
    pord_str6.set('Delivery to')
  else:
    pord_lbx6.insert(0, podata[49])
  pord_lbx6.place(x=15,y=320)

  pord_str7 = StringVar() 
  pord_lbx7 = Entry(tentab, width=30,textvariable=pord_str7)
  if not podata:
    pord_str7.set('P.Order total')
  else:
    pord_lbx7.insert(0, podata[50])
  pord_lbx7.place(x=15,y=340)


  pmessagelbframe=LabelFrame(tentab,text="Predefined terms and conditions text for purchase orders",height=70, width=980)
  pmessagelbframe.place(x=248, y=396)

  pord_str8= scrolledtext.ScrolledText(tentab)
  if not podata:
    pass
  else:
    pord_str8.insert('1.0', podata[51])
  pord_str8.place(x=260,y=415,height=38,width=950)



  def restore_default_pord():
        pord_lbx1.delete(0, 'end')
        pord_lbx1.insert(0, 'Purchase Order')
        pord_lbx2.delete(0, 'end')
        pord_lbx2.insert(0, 'P.Order#')
        pord_lbx3.delete(0, 'end')
        pord_lbx3.insert(0, 'P.Order Date')
        pord_lbx4.delete(0, 'end')
        pord_lbx4.insert(0, 'Due date')
        pord_lbx5.delete(0, 'end')
        pord_lbx5.insert(0, 'Vendor')
        pord_lbx6.delete(0, 'end')
        pord_lbx6.insert(0, 'Delivery to')
        pord_lbx7.delete(0, 'end')
        pord_lbx7.insert(0, 'P.Order total')



  bttermadd1 = Button(tentab,text="Restore defaults",command=restore_default_pord)
  bttermadd1.place(x=45,y=430)



  sql = "select * from company"
  fbcursor.execute(sql)
  podata = fbcursor.fetchone()

    
  frame = Frame(tentab, width=953, height=300)
  frame.pack(expand=True, fill=BOTH)
  frame.place(x=247,y=90)
  canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
              
  vertibar=Scrollbar(frame, orient=VERTICAL)
  vertibar.pack(side=RIGHT,fill=Y)
  vertibar.config(command=canvas.yview)
          
  canvas.config(width=953,height=300)
  canvas.config(yscrollcommand=vertibar.set)
  canvas.pack(expand=True,side=LEFT,fill=BOTH)
  canvas.create_rectangle(100, 8, 850, 687 , outline='yellow',fill='white')
  canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
  try:
    pord_image = Image.open("images/"+podata[13])
    pord_resize_image = pord_image.resize((200,100))
    pord_image = ImageTk.PhotoImage(pord_resize_image)

    pord_btlogo = Label(canvas,width=200,height=100,image = pord_image) 
    window_image = canvas.create_window(175, 45, anchor="nw", window=pord_btlogo)
    pord_btlogo.photo = pord_image
  except:
      pass  
  canvas.create_text(202, 160, text=""+pord_str2.get(), fill="black", font=('Helvetica 11'))
  canvas.create_text(215, 180, text=""+pord_str3.get(), fill="black", font=('Helvetica 11'))
  canvas.create_text(200, 200, text=""+pord_str4.get(), fill="black", font=('Helvetica 11'))
  canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
  canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
  canvas.create_text(350, 160, text="PORD/2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))
          
  canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
          # canvas.create_text(700, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'), width=125)
  PT_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
  PT_address.tag_configure('tag_name',justify='right')
  PT_address.insert('1.0', podata[2])
  PT_address.tag_add('tag_name','1.0', 'end')
  PT_address_window = canvas.create_window(520, 80, anchor="nw", window=PT_address)
  canvas.create_text(695, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
  canvas.create_text(700, 205, text=" "+pord_str1.get(), fill="black", font=('Helvetica 14 bold'))
  canvas.create_text(706, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
            
  canvas.create_text(210, 260, text=""+pord_str5.get(), fill="black", font=('Helvetica 10 underline'))
  canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
  canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
  canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
  canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
  canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
        
  s = ttk.Style()
  s.configure('mystyle_2.Treeview.Heading', background=''+pwin_menu.get(),State='DISABLE')

  tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')

  tree.column("# 1", anchor=E, stretch=NO, width=100)
  tree.heading("# 1", text="ID/SKU")
  tree.column("# 2", anchor=E, stretch=NO, width=350)
  tree.heading("# 2", text="Product/Service - Description")
  tree.column("# 3", anchor=E, stretch=NO, width=80)
  tree.heading("# 3", text="Quantity")
  tree.column("# 4", anchor=E, stretch=NO, width=90)
  tree.heading("# 4", text="Unit Price")
  tree.column("# 5", anchor=E, stretch=NO, width=80)
  tree.heading("# 5", text="Price")
            
  window = canvas.create_window(120, 340, anchor="nw", window=tree)

  canvas.create_line(120, 390, 820, 390 )
  canvas.create_line(120, 340, 120, 365 )
  canvas.create_line(120, 365, 120, 390 )
  canvas.create_line(820, 340, 820, 540 )
  canvas.create_line(740, 340, 740, 540 )
  canvas.create_line(570, 340, 570, 540 )
  canvas.create_line(570, 415, 820, 415 )
  canvas.create_line(570, 440, 820, 440 )
  canvas.create_line(570, 465, 820, 465 )
  canvas.create_line(570, 490, 820, 490 )
  canvas.create_line(570, 515, 820, 515 )
  canvas.create_line(650, 340, 650, 390 )
  canvas.create_line(220, 340, 220, 390 )
  canvas.create_line(570, 540, 820, 540 )

  canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
  canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
  canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
      
  if comcursignpla.get() == "before amount":
    canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "after amount":
    canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))

  else:
    pass
          # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
      
          # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
          # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
          # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          
  if comcursignpla.get() == "before amount":
    canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

          # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
  else:
    pass

          # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
  canvas.create_text(650, 479, text=""+pord_str6.get(), fill="black", font=('Helvetica 10 bold'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

          # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
          
  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
          # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

  canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
  canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
            
  canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
  canvas.create_line(150, 608, 795, 608)
          # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10')) 
  PT = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
  PT.insert('1.0', pord_str8.get('1.0', END))
  PT_window = canvas.create_window(155, 612, anchor="nw", window=PT)

  canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
  canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10')) 

  def refresh():
    sql = "select * from company"
    fbcursor.execute(sql)
    podata1 = fbcursor.fetchone()

    frame = Frame(tentab, width=953, height=300)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=247,y=90)
    canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
                
    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
            
    canvas.config(width=953,height=300)
    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(100, 8, 850, 687 , outline='yellow',fill='white')
    canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      pord_image = Image.open("images/"+podata1[13])
      pord_resize_image = pord_image.resize((200,100))
      pord_image = ImageTk.PhotoImage(pord_resize_image)

      pord_btlogo = Label(canvas,width=200,height=100,image = pord_image) 
      window_image = canvas.create_window(175, 45, anchor="nw", window=pord_btlogo)
      pord_btlogo.photo = pord_image
    except:
        pass  
    canvas.create_text(202, 160, text=""+pord_str2.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(215, 180, text=""+pord_str3.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(200, 200, text=""+pord_str4.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 160, text="PORD/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))
            
    canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
            # canvas.create_text(700, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'), width=125)
    PT_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    PT_address.tag_configure('tag_name',justify='right')
    PT_address.insert('1.0', podata1[2])
    PT_address.tag_add('tag_name','1.0', 'end')
    PT_address_window = canvas.create_window(520, 80, anchor="nw", window=PT_address)
    canvas.create_text(695, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
    canvas.create_text(700, 205, text=" "+pord_str1.get(), fill="black", font=('Helvetica 14 bold'))
    canvas.create_text(706, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
              
    canvas.create_text(210, 260, text=""+pord_str5.get(), fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
          
    s = ttk.Style()
    s.configure('mystyle_2.Treeview.Heading', background=''+pwin_menu.get(),State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')

    tree.column("# 1", anchor=E, stretch=NO, width=100)
    tree.heading("# 1", text="ID/SKU")
    tree.column("# 2", anchor=E, stretch=NO, width=350)
    tree.heading("# 2", text="Product/Service - Description")
    tree.column("# 3", anchor=E, stretch=NO, width=80)
    tree.heading("# 3", text="Quantity")
    tree.column("# 4", anchor=E, stretch=NO, width=90)
    tree.heading("# 4", text="Unit Price")
    tree.column("# 5", anchor=E, stretch=NO, width=80)
    tree.heading("# 5", text="Price")
              
    window = canvas.create_window(120, 340, anchor="nw", window=tree)

    canvas.create_line(120, 390, 820, 390 )
    canvas.create_line(120, 340, 120, 365 )
    canvas.create_line(120, 365, 120, 390 )
    canvas.create_line(820, 340, 820, 540 )
    canvas.create_line(740, 340, 740, 540 )
    canvas.create_line(570, 340, 570, 540 )
    canvas.create_line(570, 415, 820, 415 )
    canvas.create_line(570, 440, 820, 440 )
    canvas.create_line(570, 465, 820, 465 )
    canvas.create_line(570, 490, 820, 490 )
    canvas.create_line(570, 515, 820, 515 )
    canvas.create_line(650, 340, 650, 390 )
    canvas.create_line(220, 340, 220, 390 )
    canvas.create_line(570, 540, 820, 540 )

    canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
        
    if comcursignpla.get() == "before amount":
      canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount":
      canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    else:
      pass
            # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
        
            # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
            # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
            # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
            
    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

            # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
    else:
      pass

            # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(650, 479, text=""+pord_str6.get(), fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

            # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
            
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
            # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
              
    canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 608, 795, 608)
            # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10')) 
    PT = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
    PT.insert('1.0', pord_str8.get('1.0', END))
    PT_window = canvas.create_window(155, 612, anchor="nw", window=PT)

    canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))          

  refreshbtn = Button(tentab,text="Refresh",width=15,command=refresh)
  refreshbtn.place(x=1090,y=10)   
    

  ############################## PURCHASE ORDERS ##############################
#create new purchase order
  def purch_create():
    pop1=Toplevel(purch_midFrame)
    pop1.title("Porder")
    pop1.geometry("950x690+150+0")


    #select vendor
    def purch_sele_customer():
      global cuselection
      cuselection=Toplevel()
      cuselection.title("Select Customer")
      cuselection.geometry("930x650+240+10")
      cuselection.resizable(False, False)


      #add new customer
      def purch_create_newcust():
        global checkvar1,checkvar2,custid,bname,baddress,cat,sname,saddress,contp,cemail,ctel,cfax,cmob,scontp,scemail,sctel,scfax,ccountry,ccity,cnotes
        ven=Toplevel(purch_midFrame)
        ven.title("Add new vendor")
        ven.geometry("930x650+240+10")
        checkvar1=IntVar()
        checkvar2=IntVar()
        radio=IntVar()
        createFrame=Frame(ven, bg="#f5f3f2", height=650)
        createFrame.pack(side="top", fill="both")
        labelframe1 = LabelFrame(createFrame,text="Customer",bg="#f5f3f2",font=("arial",15))
        labelframe1.place(x=10,y=5,width=910,height=600)

        fbcursor.execute("SELECT * FROM Customer ORDER BY customerid DESC LIMIT 1")
        query = fbcursor.fetchone()

        text1=Label(labelframe1, text="Customer ID:",bg="#f5f3f2",fg="blue").place(x=5 ,y=10)
        custid=Entry(labelframe1,width=25)
        custid.place(x=150,y=10)
        if not query== None:
          id00=query[0]+1
        else:
          id00=1
        custid.insert(0, id00)

        text2=Label(labelframe1, text="Category:",bg="#f5f3f2").place(x=390 ,y=10)
        cat=ttk.Combobox(labelframe1,width=25,value="Default")
        cat.place(x=460 ,y=10)

        text3=Label(labelframe1, text="Status:",bg="#f5f3f2").place(x=710 ,y=10)
        Checkbutton(labelframe1,text="Active",variable=checkvar1,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=760 ,y=10)
        labelframe2 = LabelFrame(labelframe1,text="Invoice to (appears on invoices)",bg="#f5f3f2")
        labelframe2.place(x=5,y=40,width=420,height=150)
        name = Label(labelframe2, text="Ship to name:",bg="#f5f3f2",fg="blue").place(x=5,y=5)
        sname = Entry(labelframe2,width=28)
        sname.place(x=130,y=5)

        addr = Label(labelframe2, text="Address:",bg="#f5f3f2",fg="blue").place(x=5,y=40)
        saddress = Entry(labelframe2,width=28)
        saddress.place(x=130,y=40,height=80)

        def btncpy():
          tosp=sname.get()
          saddres=saddress.get()
          bname.delete(0, 'end')
          bname.insert(0, tosp)
          baddress.delete(0,'end')
          baddress.insert(0, saddres)

        btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>",command=btncpy).place(x=440, y=90)

        labelframe3 = LabelFrame(labelframe1,text="Ship to (appears on invoices)",bg="#f5f3f2")
        labelframe3.place(x=480,y=40,width=420,height=150)
        name = Label(labelframe3, text="Business name:",bg="#f5f3f2").place(x=5,y=5)
        bname = Entry(labelframe3,width=28)
        bname.place(x=130,y=5)

        addr = Label(labelframe3, text="Address:",bg="#f5f3f2").place(x=5,y=40)
        baddress = Entry(labelframe3,width=28)
        baddress.place(x=130,y=40,height=80)
        
        labelframe4 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
        labelframe4.place(x=5,y=195,width=420,height=150)
        name = Label(labelframe4, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
        contp = Entry(labelframe4,width=28)
        contp.place(x=130,y=5)

        email = Label(labelframe4, text="E-mail address:",bg="#f5f3f2",fg="blue").place(x=5,y=35)
        cemail = Entry(labelframe4,width=28)
        cemail.place(x=130,y=35)

        tel = Label(labelframe4, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
        ctel = Entry(labelframe4,width=11)
        ctel.place(x=130,y=65)

        fax = Label(labelframe4, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
        cfax = Entry(labelframe4,width=11)
        cfax.place(x=280,y=65)

        sms = Label(labelframe4, text="Mobile number for SMS notifications:",bg="#f5f3f2").place(x=5,y=95)
        cmob = Entry(labelframe4,width=15)
        cmob.place(x=248,y=95)   

        def btncpy1():
          cprsn1=contp.get()
          cemail1=cemail.get()
          no=ctel.get()
          fx=cfax.get()
          scontp.insert(0, cprsn1)
          scemail.insert(0, cemail1)
          sctel.insert(0, no)
          scfax.insert(0,fx)   

        btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>",command=btncpy1).place(x=440, y=250)

        labelframe5 = LabelFrame(labelframe1,text="Ship to contact",bg="#f5f3f2")
        labelframe5.place(x=480,y=195,width=420,height=125)
        name = Label(labelframe5, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
        scontp = Entry(labelframe5,width=28)
        scontp.place(x=130,y=5)

        email = Label(labelframe5, text="E-mail address:",bg="#f5f3f2").place(x=5,y=35)
        scemail = Entry(labelframe5,width=28)
        scemail.place(x=130,y=35)

        tel = Label(labelframe5, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
        sctel = Entry(labelframe5,width=11)
        sctel.place(x=130,y=65)

        fax = Label(labelframe5, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
        scfax = Entry(labelframe5,width=11)
        scfax.place(x=280,y=65)

        labelframe6 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
        labelframe6.place(x=5,y=350,width=420,height=100)
        Checkbutton(labelframe6,text="Tax Exempt",variable=checkvar2,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=5 ,y=5)
        tax = Label(labelframe6, text="Specific Tax1 %:",bg="#f5f3f2").place(x=180,y=5)
        e1tax = Entry(labelframe6,width=10)
        e1tax.place(x=290,y=5)

        discount = Label(labelframe6, text="Discount%:",bg="#f5f3f2").place(x=5,y=35)
        e2dsc = Entry(labelframe6,width=10)
        e2dsc.place(x=100,y=35)

        labelframe7 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2",)
        labelframe7.place(x=480,y=330,width=420,height=100)
        country = Label(labelframe7, text="country:",bg="#f5f3f2").place(x=5,y=5)
        ccountry = Entry(labelframe7,width=28)
        ccountry.place(x=130,y=5)

        city = Label(labelframe7, text="City:",bg="#f5f3f2").place(x=5,y=35)
        ccity = Entry(labelframe7,width=28)
        ccity.place(x=130,y=35)

        labelframe8 = LabelFrame(labelframe1,text="Customer Type",bg="#f5f3f2")
        labelframe8.place(x=5,y=460,width=420,height=100)
        R1=Radiobutton(labelframe8,text=" Client ",variable=radio,value=1,bg="#f5f3f2").place(x=5,y=15)
        R2=Radiobutton(labelframe8,text=" Vendor ",variable=radio,value=2,bg="#f5f3f2").place(x=150,y=15)
        R3=Radiobutton(labelframe8,text=" Both(client/vendor)",variable=radio,value=3,bg="#f5f3f2").place(x=250,y=15)
        

        labelframe9 = LabelFrame(labelframe1,text="Notes",bg="#f5f3f2")
        labelframe9.place(x=480,y=430,width=420,height=150)
        cnotes = Entry(labelframe9)
        cnotes.place(x=10,y=10,height=100,width=390)

        btn1=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=tick,text="OK").place(x=20, y=615)
        btn2=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=cancel,text="Cancel",command=lambda:ven.destroy()).place(x=800, y=615)
          
                

      enter=Label(cuselection, text="Enter filter text").place(x=5, y=10)
      e1=Entry(cuselection, width=20).place(x=110, y=10)
      text=Label(cuselection, text="Filtered column").place(x=340, y=10)
      e2=Entry(cuselection, width=20).place(x=450, y=10)
      global purch_cust_tree
      purch_cust_tree=ttk.Treeview(cuselection, height=27)
      purch_cust_tree["columns"]=["1","2","3", "4"]
      purch_cust_tree.column("#0", width=35)
      purch_cust_tree.column("1", width=160)
      purch_cust_tree.column("2", width=160)
      purch_cust_tree.column("3", width=140)
      purch_cust_tree.column("4", width=140)
      purch_cust_tree.heading("#0",text="")
      purch_cust_tree.heading("1",text="Customer/Ventor ID")
      purch_cust_tree.heading("2",text="Customer/Ventor Name")
      purch_cust_tree.heading("3",text="Tel.")
      purch_cust_tree.heading("4",text="Contact Person")
      purch_cust_tree.place(x=5, y=45)

      sql_sel_pord_cust = "SELECT * FROM customer"
      fbcursor.execute(sql_sel_pord_cust)
      pord_customer_details = fbcursor.fetchall()

      count=0
      for i in pord_customer_details:
        if True:
          purch_cust_tree.insert(parent='',index='end',iid=i,text='',values=(i[0],i[4],i[10],i[8]))
        else:
          pass
      count += 1

      def pordcust_tree_fetch():
        pordcust_tree_item = purch_cust_tree.item(purch_cust_tree.focus())["values"][0]
        sql = "SELECT * FROM customer WHERE customerid=%s"
        val = (pordcust_tree_item,)
        fbcursor.execute(sql,val)
        pordsel_cust_str = fbcursor.fetchone()
        vender_combo.delete(0, END)
        vender_combo.insert(0,pordsel_cust_str[4])
        paddress.delete('1.0',END)
        paddress.insert('1.0',pordsel_cust_str[5])
        # estimate_shipto3.delete(0, END)
        # estimate_shipto3.insert(0, pordsel_cust_str[6])
        # estimate_ship_address4.delete('1.0',END)
        # estimate_ship_address4.insert('1.0',pordsel_cust_str[7])
        pmail.delete(0,END)
        pmail.insert(0,pordsel_cust_str[9])
        psms.delete(0,END)
        psms.insert(0,pordsel_cust_str[12])

        cuselection.destroy()



      ctegorytree=ttk.Treeview(cuselection, height=27)
      ctegorytree["columns"]=["1"]
      ctegorytree.column("#0", width=35, minwidth=20)
      ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
      ctegorytree.heading("#0",text="", anchor=W)
      ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
      ctegorytree.place(x=660, y=45)

      scrollbar = Scrollbar(cuselection)
      scrollbar.place(x=640, y=45, height=560)
      scrollbar.config( command=purch_cust_tree.yview )

      btn1=Button(cuselection,compound = LEFT,image=tick, text="ok",width=60,command=pordcust_tree_fetch).place(x=15, y=610)
      btn1=Button(cuselection,compound = LEFT,image=tick, text="Edit selected customer", width=150,command=purch_create_newcust).place(x=250, y=610)
      btn1=Button(cuselection,compound = LEFT,image=tick,text="Add new customer", width=150,command=purch_create_newcust).place(x=435, y=610)
      btn1=Button(cuselection,compound = LEFT,image=cancel, text="Cancel", width=60).place(x=740, y=610)    



    #add new line item
    def newlineproduct():
      newselection=Toplevel()
      newselection.title("Select Customer")
      newselection.geometry("930x650+240+10")
      newselection.resizable(False, False)

#add new product
      def adda_product():
        top = Toplevel()  
        
        top.title("Add a new Product/Service")
        p2 = PhotoImage(file = 'images/fbicon.png')
        top.iconphoto(False, p1)
        top.geometry("600x550+390+125")
        
        
        tabControl = ttk.Notebook(top)
        s = ttk.Style()
        s.theme_use('default')
        s.configure('TNotebook.Tab', background="#999999", width=50, padding=10,bd=0)


        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        
        tabControl.add(tab1,compound = LEFT, text ='Product/Service')
        tabControl.add(tab2,compound = LEFT, text ='Product Image')
        
        tabControl.pack(expand = 1, fill ="both")
        
        innerFrame = Frame(tab1,bg="#f5f3f2", relief=GROOVE, height=490)
        innerFrame.pack(side="top",fill=BOTH)

        Customerlabelframe = LabelFrame(innerFrame,text="Product/Service",width=580,height=475)
        Customerlabelframe.pack(side="top",fill=BOTH,padx=10)
        
        global filename
        filename = ""
        
        def upload_file():
          global filename,img, b2
          f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
          filename = filedialog.askopenfilename(filetypes=f_types)
          shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
          image = Image.open(filename)
          resize_image = image.resize((350, 350))
          img = ImageTk.PhotoImage(resize_image)
          b2 = Button(imageFrame,image=img)
          b2.place(x=130, y=80)
        
        def addproducts():
          global img , filename 
          sku = codeentry.get()
          status = checkvarStatus.get()
          catgory = n.get()
          name = nameentry.get()
          description = desentry.get()
          unitprice = uval.get()
          peices = pcsentry.get()
          cost = costval.get()
          price_cost = priceval.get()
          taxable = checkvarStatus2.get()
          tax2 = checkvarStatustax2.get()
          nostockcontrol = checkvarStatus3.get()
          stock = stockentry.get()
          lowstock = lowentry.get()
          warehouse = wareentry.get()
          pnotes = sctxt.get("1.0",'end-1c')
          entries = [sku,name, unitprice, cost]
          entri = []
          for i in entries:
            if i == '':
              entri.append(i)
          if len(entri) == 0:
            sql = 'select * from Productservice where sku = %s or name = %s'
            val  = (sku, name)
            fbcursor.execute(sql, val)
            fbcursor.fetchall()
            row_count = fbcursor.rowcount
            if row_count == 0:
              if filename == "":
                sql = 'insert into Productservice(sku, category, name, description, status, unitprice, peices, cost, taxable, priceminuscost, serviceornot, stock, stocklimit, warehouse, privatenote,tax2) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)'
                val = (sku, catgory, name, description, status, unitprice, peices, cost, taxable, price_cost, nostockcontrol, stock, lowstock, warehouse, pnotes,tax2)
                fbcursor.execute(sql, val)
                fbilldb.commit()
              else:
                file = shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
                sql = 'insert into Productservice(sku, category, name, description, status, unitprice, peices, cost, taxable, priceminuscost, serviceornot, stock, stocklimit, warehouse, image, privatenote,tax2) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)'
                val = (sku, catgory, name, description, status, unitprice, peices, cost, taxable, price_cost, nostockcontrol, stock, lowstock, warehouse, filename.split('/')[-1], pnotes,tax2)
                fbcursor.execute(sql, val)
                fbilldb.commit()
            else:
              messagebox.showinfo("Alert", "Entry with same name or SKU already exists.\nTry again.")
              top.destroy()
            for record in treeproducts.get_children():
              treeproducts.delete(record)
            fbcursor.execute("select *  from Productservice")
            pandsdata = fbcursor.fetchall()
            countp = 0
            for i in pandsdata:
              if i[6] == '1':
                acti = 'Active'
              else:
                acti = 'Inactive' 
              sql = "select currencysign,currsignplace from company"
              fbcursor.execute(sql)
              currsymb = fbcursor.fetchone()
              if not currsymb: 
                if i[13] > i[14]:
                  treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('green',))
                  countp += 1              
                elif i[12] == '1':
                  treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('blue',))
                  countp += 1
                else:
                  treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('red',))
                  countp += 1
                  
              elif currsymb[1] == "before amount":
                if (i[13]) > (i[14]):
                  treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('green',))
                  countp += 1
                elif i[12] == '1':
                  treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('blue',))
                  countp += 1
                else:
                  treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('red',))
                  countp += 1
              elif currsymb[1] == "before amount with space":
                if i[13] > i[14]:
                  treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('green',))
                  countp += 1
                elif i[12] == '1':
                  treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('blue',))
                  countp += 1
                else:
                  treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('red',))
                  countp += 1
              elif currsymb[1] == "after amount":
                if i[13] > i[14]:
                  treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('green',))
                  countp += 1
                elif i[12] == '1':
                  treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
                  countp += 1
                else:
                  treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('red',))
                  countp += 1
              elif currsymb[1] == "after amount with space":
                if i[13] > i[14]:
                  treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('green',))
                  countp += 1
                elif i[12] == '1':
                  treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
                  countp += 1
                else:
                  treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('red',))
                  countp += 1
            top.destroy()
          else:
            messagebox.showinfo("Alert", "Fields name and SKU should not be empty.\nFill out required fields and try again")
            
    
        fbcursor.execute("SELECT * FROM Productservice ORDER BY sku DESC LIMIT 1")
        skuin = fbcursor.fetchone()
        
        
        code1=Label(Customerlabelframe,text="Code or SKU* :",fg="blue",pady=10,padx=10)
        code1.place(x=20,y=0)
        codeentry = Entry(Customerlabelframe,width=35)
        codeentry.place(x=110,y=8)
        # if not skuin == None:
        #   fk=skuin[2]+1
        # else:
        #   fk=1
        # codeentry.insert(0, fk)

        checkvarStatus=IntVar()
        status1=Label(Customerlabelframe,text="Status:")
        status1.place(x=380,y=8)
        Button1 = Checkbutton(Customerlabelframe, 
                          variable = checkvarStatus,text="Active",compound="right",
                          onvalue =1,
                          offvalue = 0,
                          width = 10)

        Button1.place(x=420,y=5)

        category1=Label(Customerlabelframe,text="Category:",pady=5,padx=10)
        category1.place(x=20,y=40)
        n = StringVar() 
        catgory = ttk.Combobox(Customerlabelframe, width = 40, textvariable = n ) 
        catgory.place(x=110,y=45)
        catgory.insert(0, 'Default')


        name1=Label(Customerlabelframe,text="Name* :",fg="blue",pady=5,padx=10)
        name1.place(x=20,y=70)
        nameentry = Entry(Customerlabelframe,width=70)
        nameentry.place(x=110,y=75)

        des1=Label(Customerlabelframe,text="Description :",pady=5,padx=10)
        des1.place(x=20,y=100)
        desentry = Entry(Customerlabelframe,width=70)
        desentry.place(x=110,y=105)

        def prdoucts_cal(S,d):
            if d == '1': #insert
              if not S in ['.','0','1','2','3','4','5','6','7','8','9']:
                return False
              return True
            if d.isdigit():
              return True

        uval = StringVar()
        unit1=Label(Customerlabelframe,text="Unit Price:",fg="blue",pady=5,padx=10)
        unit1.place(x=20,y=130)
        unitentry = Entry(Customerlabelframe,width=20,textvariable=uval)
        unitentry.place(x=110,y=135)
        cal_unit = (Customerlabelframe.register(prdoucts_cal),'%S','%d')
        unitentry.config(validate='key',validatecommand=(cal_unit),justify='right')
        

        # pcsval = IntVar()
        pcs1=Label(Customerlabelframe,text="Pcs/Weight:",fg="blue",pady=5,padx=10)
        pcs1.place(x=320,y=130)
        pcsentry = Entry(Customerlabelframe,width=20)
        pcsentry.place(x=410,y=135)

        costval = StringVar(value="0")
        cost1=Label(Customerlabelframe,text="Cost:",pady=5,padx=10)
        cost1.place(x=20,y=160)
        
        costentry = Entry(Customerlabelframe,width=20,textvariable=costval)
        costentry.place(x=110,y=165)
        cal_cost = (Customerlabelframe.register(prdoucts_cal),'%S','%d')
        costentry.config(validate='key',validatecommand=(cal_cost),justify='right')
        
        def set_label(name, index, mode):
          copr = float(uval.get()) - float(costval.get())
          priceval.set(str(copr))
          
        priceval = StringVar()
        price1=Label(Customerlabelframe,text="(Price-Cost):",pady=5,padx=10)
        price1.place(x=20,y=190)
        priceentry = Entry(Customerlabelframe,width=20,textvariable=priceval,state=DISABLED,disabledbackground="white",disabledforeground="black")
        priceentry.config(justify="right")
        priceentry.place(x=110,y=195)
        
        uval.trace('w', set_label)
        costval.trace('w', set_label)

        sql = "select taxtype from company"
        fbcursor.execute(sql)
        taxchoose = fbcursor.fetchone()

        checkvarStatus2=IntVar()
      
        Button2 = Checkbutton(Customerlabelframe,variable = checkvarStatus2, 
                          text="Taxable Tax1rate",compound="right",
                          onvalue =1 ,
                          offvalue = 0,
                          height=2,
                          width = 12)
        
        checkvarStatustax2=IntVar()
        Buttontax2 = Checkbutton(Customerlabelframe,variable = checkvarStatustax2, 
                          text="Taxable Tax2rate",compound="right",
                          onvalue =1 ,
                          offvalue = 0,
                          height=2,
                          width = 12)
        
        
        if not taxchoose:
          pass
        elif taxchoose[0] == '1':
          Button2.place_forget()
          Buttontax2.place_forget()
        elif taxchoose[0] == '2':
          Button2.place(x=415,y=153)
          Buttontax2.place_forget()
        elif taxchoose[0] == '3':
          Button2.place(x=415,y=153)
          Buttontax2.place(x=415,y=203)

        

        def switch():
          if checkvarStatus3.get():
            stockentry["state"] = DISABLED
            lowentry["state"] = DISABLED
            wareentry["state"] = DISABLED
          else:
            stockentry["state"] = NORMAL
            lowentry["state"] = NORMAL
            wareentry["state"] = NORMAL
        checkvarStatus3=BooleanVar()
        Button3 = Checkbutton(Customerlabelframe,variable = checkvarStatus3,command=switch, 
                          text="This is a service(no stock control)", 
                          onvalue =1 ,
                          offvalue = 0,
                          height=3)

        Button3.place(x=40,y=220)
    
        def stocknum(input):
          if input.isdigit():
            return True
          elif input is "":
            return True
          else:
            return False
        stock1=Label(Customerlabelframe,text="Stock:",pady=5,padx=10)
        stock1.place(x=90,y=260)
        stockentry = Entry(Customerlabelframe,width=15)
        stockentry.place(x=140,y=265)
        sto = Customerlabelframe.register(stocknum)
        stockentry.config(validate="key",validatecommand=(sto, '%S'))


        low1=Label(Customerlabelframe,text="Low Stock Warning Limit:",pady=5,padx=10)
        low1.place(x=280,y=260)
        lowentry = Entry(Customerlabelframe,width=15)
        lowentry.place(x=435,y=265)
        lowsto = Customerlabelframe.register(stocknum)
        lowentry.config(validate="key",validatecommand=(lowsto, '%S'))

      
        ware1=Label(Customerlabelframe,text="Warehouse:",pady=5,padx=10)
        ware1.place(x=60,y=290)
        wareentry = Entry(Customerlabelframe,width=64)
        wareentry.place(x=140,y=295)

        # pnoteval = StringVar()
        text1=Label(Customerlabelframe,text="Private notes(not appears on invoice):",pady=5,padx=10)
        text1.place(x=20,y=320)
        sctxt = scrolledtext.ScrolledText(Customerlabelframe, undo=True,width=62,height=4)
        sctxt.place(x=32,y=358)
        
        okButton = Button(innerFrame, text ="Ok",image=tick,width=70,compound = LEFT, command=addproducts)
        okButton.pack(side=LEFT, padx=(10, 0), pady=(5, 10))
        
        def closetab():
          top.destroy()

        cancelButton = Button(innerFrame,image=cancel,text="Cancel",width=70,compound = LEFT, command=closetab)
        cancelButton.pack(side=RIGHT, padx=(0, 10), pady=(5, 10))

        imageFrame = Frame(tab2, relief=GROOVE,height=580)
        imageFrame.pack(side="top",fill=BOTH)

        
          
        browseimg=Label(imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
        browseimg.place(x=30,y=35)
          
        browsebutton=Button(imageFrame,text = 'Browse',command=upload_file)
        browsebutton.place(x=485,y=30,height=30,width=50)

        removeButton = Button(imageFrame,image=cancel,text="Remove Product Image",width=150,compound = LEFT, command=lambda: b2.destroy())
        removeButton.place(x=410,y=460)

        top.mainloop()

      
######################## VIEW/EDIT PRODUCT #######################################################################

  
      # def edit_product():  
      #   try:
      #     itemid = treeproducts.item(treeproducts.focus())["values"][1]
          
      #     global filename
      #     filename = ""
          
      #     def upload_file():
      #       global filename,img, b2
      #       f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
      #       filename = filedialog.askopenfilename(filetypes=f_types)
      #       shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
      #       image = Image.open(filename)
      #       resize_image = image.resize((350, 350))
      #       img = ImageTk.PhotoImage(resize_image)
      #       b2 = Button(imageFrame,image=img)
      #       b2.place(x=130, y=80)
          
      #     def updateproducts():
      #       global img , filename 
      #       sku = codeentry.get()
      #       status = checkvarStatus.get()
      #       catgory = n.get()
      #       name = nameentry.get()
      #       description = desentry.get()
      #       unitprice = uval.get()
      #       peices = pcsentry.get()
      #       cost = costval.get()
      #       price_cost = priceval.get()
      #       taxable = checkvarStatus2.get()
      #       tax2 = checkvarStatustax2.get()
      #       nostockcontrol = checkvarStatus3.get()
      #       stock = stockval.get()
      #       lowstock = lowval.get()
      #       warehouse = wareentry.get()
      #       pnotes = sctxt.get("1.0", 'end-1c')
      #       entries = [sku, name, unitprice, cost]
      #       entri = []
      #       for i in entries:
      #         if i == '':
      #           entri.append(i)
      #       if len(entri) == 0:
      #         if filename == "":
      #           sql = "update Productservice set sku=%s, category=%s, name=%s, description=%s, status=%s, unitprice=%s, peices=%s, cost=%s, taxable=%s, priceminuscost=%s, serviceornot=%s, stock=%s, stocklimit=%s, warehouse=%s, privatenote=%s,tax2=%s where Productserviceid = %s"
      #           val = (sku, catgory, name, description, status, unitprice, peices, cost, taxable, price_cost, nostockcontrol, stock, lowstock, warehouse, pnotes,tax2, itemid)
      #           fbcursor.execute(sql, val)
      #           fbilldb.commit()
      #         else:
      #           file = shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
      #           sql = "update Productservice set category=%s, name=%s, description=%s, status=%s, unitprice=%s, peices=%s, cost=%s, taxable=%s, priceminuscost=%s, serviceornot=%s, stock=%s, stocklimit=%s, warehouse=%s, image=%s, privatenote=%s,tax2=%s where Productserviceid = %s"
      #           val = (catgory, name, description, status, unitprice, peices, cost, taxable, price_cost, nostockcontrol, stock, lowstock, warehouse,filename.split('/')[-1], pnotes,tax2, itemid)
      #           fbcursor.execute(sql, val)
      #           fbilldb.commit()
                
      #         for record in treeproducts.get_children():
      #           treeproducts.delete(record)
      #         fbcursor.execute("select *  from Productservice")
      #         pandsdata = fbcursor.fetchall()
      #         countp = 0
      #         for i in pandsdata:
      #           if i[6] == '1':
      #             acti = 'Active'
      #           else:
      #             acti = 'Inactive' 
      #           sql = "select currencysign,currsignplace from company"
      #           fbcursor.execute(sql)
      #           currsymb = fbcursor.fetchone()
      #           if not currsymb: 
      #             if i[13] > i[14]:
      #               treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('green',))
      #               countp += 1              
      #             elif i[12] == '1':
      #               treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('blue',))
      #               countp += 1
      #             else:
      #               treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('red',))
      #               countp += 1
                          
      #           elif currsymb[1] == "before amount":
      #             if (i[13]) > (i[14]):
      #               treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('green',))
      #               countp += 1
      #             elif i[12] == '1':
      #               treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('blue',))
      #               countp += 1
      #             else:
      #               treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('red',))
      #               countp += 1
      #           elif currsymb[1] == "before amount with space":
      #             if i[13] > i[14]:
      #               treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('green',))
      #               countp += 1
      #             elif i[12] == '1':
      #               treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('blue',))
      #               countp += 1
      #             else:
      #               treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('red',))
      #               countp += 1
      #           elif currsymb[1] == "after amount":
      #             if i[13] > i[14]:
      #               treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('green',))
      #               countp += 1
      #             elif i[12] == '1':
      #               treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
      #               countp += 1
      #             else:
      #               treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('red',))
      #               countp += 1
      #           elif currsymb[1] == "after amount with space":
      #               if i[13] > i[14]:
      #                 treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('green',))
      #                 countp += 1
      #               elif i[12] == '1':
      #                 treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
      #                 countp += 1
      #               else:
      #                 treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('red',))
      #                 countp += 1
      #         top.destroy()
      #       else:
      #         messagebox.showinfo("F-Billing Revolution", "Fields name or SKU entered is already in database.")
      #         top.destroy()
            
            
      #     sql = "select * from Productservice where Productserviceid = %s"
      #     val = (itemid, )
      #     fbcursor.execute(sql, val)
      #     psdata = fbcursor.fetchone()
          
          
      #     top = Toplevel()  
      #     top.title("Edit Product/Service details")
      #     p3 = PhotoImage(file = 'images/fbicon.png')
      #     top.iconphoto(False, p1)
      #     top.geometry("600x550+390+125")
      #     tabControl = ttk.Notebook(top)
      #     s = ttk.Style()
      #     s.theme_use('default')
      #     s.configure('TNotebook.Tab', background="#999999", width=50, padding=10,bd=0)

      #     taba = ttk.Frame(tabControl)
      #     tabb = ttk.Frame(tabControl)
          
      #     tabControl.add(taba,compound = LEFT, text ='Product/Service')
      #     tabControl.add(tabb,compound = LEFT, text ='Product Image')
          
      #     tabControl.pack(expand = 1, fill ="both")
          
      #     innerFrame = Frame(taba,bg="#f5f3f2", relief=GROOVE)
      #     innerFrame.pack(side="top",fill=BOTH)

      #     updateframe = LabelFrame(innerFrame,text="Product/Service",width=580,height=485)
      #     updateframe.pack(side="top",fill=BOTH,padx=10)

      #     code1=Label(updateframe,text="Code or SKU:",fg="blue",pady=10,padx=10)
      #     code1.place(x=20,y=0)
      #     codeentry = Entry(updateframe,width=35)
      #     codeentry.place(x=110,y=8)
      #     codeentry.insert(0, psdata[2])

      #     checkvarStatus=IntVar()
      #     status1=Label(updateframe,text="Status:")
      #     status1.place(x=380,y=8)
      #     Button1 = Checkbutton(updateframe, 
      #                       variable = checkvarStatus,text="Active",compound="right",
      #                       onvalue =1,
      #                       offvalue =0,
      #                       width = 10)
      #     Button1.place(x=420,y=5)
      #     sta = psdata[6]
      #     if sta == '1':
      #       Button1.select()
      #     else:
      #       Button1.deselect()



      #     category1=Label(updateframe,text="Category:",pady=5,padx=10)
      #     category1.place(x=20,y=40)
      #     n = StringVar() 
      #     category = Entry(updateframe,width=70,textvariable=n) 
      #     category.place(x=110,y=45)
      #     category.insert(0, psdata[3])


      #     name1=Label(updateframe,text="Name :",fg="blue",pady=5,padx=10)
      #     name1.place(x=20,y=70)
      #     nameentry = Entry(updateframe,width=70)
      #     nameentry.place(x=110,y=75)
      #     nameentry.insert(0, psdata[4])

      #     des1=Label(updateframe,text="Description :",pady=5,padx=10)
      #     des1.place(x=20,y=100)
      #     desentry = Entry(updateframe,width=70)
      #     desentry.place(x=110,y=105)
      #     desentry.insert(0, psdata[5])

      #     def set_label(name, index, mode):
      #       priceval.set(float(uval.get()) - float(costval.get()))

      #     def prdoucts_cal(S,d):
      #       if d == '1': #insert
      #         if not S in ['.','0','1','2','3','4','5','6','7','8','9']:
      #           return False
      #         return True
      #       if d.isdigit():
      #         return True
          
      #     unit1=Label(updateframe,text="Unit Price:",fg="blue",pady=5,padx=10)
      #     unit1.place(x=20,y=130)
          
      #     uval = StringVar()
      #     unitentry = Entry(updateframe,width=20,textvariable=uval)
      #     unitentry.place(x=110,y=135)
      #     unitentry.delete(0,'end')
      #     unitentry.insert(0, psdata[7])
      #     cal_unit = (updateframe.register(prdoucts_cal),'%S','%d')
      #     unitentry.config(validate='key',validatecommand=(cal_unit),justify='right')
          

      #     pcsval = IntVar()
      #     pcs1=Label(updateframe,text="Pcs/Weight:",fg="blue",pady=5,padx=10)
      #     pcs1.place(x=320,y=130)
      #     pcsentry = Entry(updateframe,width=20,textvariable=pcsval)
      #     pcsentry.place(x=410,y=135)
      #     pcsentry.delete(0,'end')
      #     pcsentry.insert(0, psdata[8])
          

      #     costval = StringVar()
      #     cost1=Label(updateframe,text="Cost:",pady=5,padx=10)
      #     cost1.place(x=20,y=160)
      #     costentry = Entry(updateframe,width=20,textvariable=costval)
      #     costentry.place(x=110,y=165)
      #     costentry.delete(0, END)
      #     costentry.insert(0, psdata[9])
      #     cal_cost = (updateframe.register(prdoucts_cal),'%S','%d')
      #     costentry.config(validate='key',validatecommand=(cal_cost),justify='right')
          

      #     priceval = StringVar()
      #     price1=Label(updateframe,text="(Price-Cost):",pady=5,padx=10)
      #     price1.place(x=20,y=190)
      #     priceentry = Entry(updateframe,width=20,textvariable=priceval)
      #     priceentry.place(x=110,y=195)
      #     priceentry.delete(0,'end')
      #     priceentry.insert(0, psdata[11])

      #     uval.trace('w', set_label)
      #     costval.trace('w', set_label)
          

      #     checkvarStatus2=IntVar()
        
      #     Button2 = Checkbutton(updateframe,variable = checkvarStatus2, 
      #                       text="Taxable Tax1rate",compound="right",
      #                       onvalue =1 ,
      #                       offvalue =0,
      #                       height=2,
      #                       width = 12)
          
      #     checkvarStatustax2=IntVar()
      #     Buttontax2 = Checkbutton(updateframe,variable = checkvarStatustax2, 
      #                     text="Taxable Tax2rate",compound="right",
      #                     onvalue =1 ,
      #                     offvalue = 0,
      #                     height=2,
      #                     width = 12)
          
      #     sql = "select taxtype from company"
      #     fbcursor.execute(sql)
      #     taxchoose = fbcursor.fetchone()
      #     if not taxchoose:
      #       pass
      #     elif taxchoose[0] == '1':
      #       Button2.place_forget()
      #       Buttontax2.place_forget()
      #     elif taxchoose[0] == '2':
      #       Button2.place(x=415,y=153)
      #       Buttontax2.place_forget()
      #     elif taxchoose[0] == '3':
      #       Button2.place(x=415,y=153)
      #       Buttontax2.place(x=415,y=203)

      
      #     tax = psdata[10]
      #     if tax == '1':
      #       Button2.select()
      #     else:
      #       Button2.deselect()

      #     if psdata[19] == '1':
      #       Buttontax2.select()
      #     else:
      #       Buttontax2.deselect()

      #     def switch():
      #       if checkvarStatus3.get():
      #         stockentry["state"] = DISABLED
      #         lowentry["state"] = DISABLED
      #         wareentry["state"] = DISABLED
      #       else:
      #         stockentry["state"] = NORMAL
      #         lowentry["state"] = NORMAL
      #         wareentry["state"] = NORMAL
      #     checkvarStatus3=BooleanVar()
        
      #     Button3 = Checkbutton(updateframe,variable = checkvarStatus3,command=switch, 
      #                       text="No stock Control", 
      #                       onvalue =1 ,
      #                       offvalue = 0,
      #                       height=3,
      #                       width = 15)

      #     Button3.place(x=40,y=220)

          

      #     def stocknum(input):
      #       if input.isdigit():
      #         return True
      #       elif input is "":
      #         return True
      #       else:
      #         return False
      #     stockval = IntVar(updateframe)
      #     stock1=Label(updateframe,text="Stock:",pady=5,padx=10)
      #     stock1.place(x=90,y=260)
      #     stockentry = Entry(updateframe,width=15,textvariable=stockval)
      #     stockentry.place(x=140,y=265)
      #     stockentry.delete(0,'end')
      #     stockentry.insert(0, psdata[13])
      #     sto = updateframe.register(stocknum)
      #     stockentry.config(validate="key",validatecommand=(sto, '%S'))
          

      #     lowval = IntVar(updateframe)
      #     low1=Label(updateframe,text="Low Stock Warning Limit:",pady=5,padx=10)
      #     low1.place(x=280,y=260)
      #     lowentry = Entry(updateframe,width=15,textvariable=lowval)
      #     lowentry.place(x=435,y=265)
      #     lowentry.delete(0,'end')
      #     lowentry.insert(0, psdata[14])
      #     lowsto = updateframe.register(stocknum)
      #     lowentry.config(validate="key",validatecommand=(lowsto, '%S'))
          

        
      #     ware1=Label(updateframe,text="Warehouse:",pady=5,padx=10)
      #     ware1.place(x=60,y=290)
      #     wareentry = Entry(updateframe,width=64)
      #     wareentry.place(x=140,y=295)
      #     wareentry.insert(0, psdata[15])

      #     scr = psdata[12]
      #     if scr == '1':
      #       Button3.select()
      #       stockentry["state"] = DISABLED
      #       lowentry["state"] = DISABLED
      #       wareentry["state"] = DISABLED
      #     else:
      #       Button3.deselect()
      #       stockentry["state"] = NORMAL
      #       lowentry["state"] = NORMAL
      #       wareentry["state"] = NORMAL
          
          

          

      #     text1=Label(updateframe,text="Private notes(not appears on invoice):",pady=5,padx=10)
      #     text1.place(x=20,y=320)
      #     sctxt = scrolledtext.ScrolledText(updateframe, undo=True,width=62,height=4)
      #     sctxt.place(x=32,y=358)
      #     try:
      #       sctxt.insert("1.0", psdata[16])
      #     except:
      #       pass
      




                      
      enter=Label(newselection, text="Enter filter text").place(x=5, y=10)
      e1=Entry(newselection, width=20).place(x=110, y=10)
      text=Label(newselection, text="Filtered column").place(x=340, y=10)
      e2=Entry(newselection, width=20).place(x=450, y=10)

      pur_add_cusventtree=ttk.Treeview(newselection, height=27)
      pur_add_cusventtree["columns"]=["1","2","3", "4","5"]
      pur_add_cusventtree.column("#0", width=35)
      pur_add_cusventtree.column("1", width=160)
      pur_add_cusventtree.column("2", width=160)
      pur_add_cusventtree.column("3", width=140)
      pur_add_cusventtree.column("4", width=70)
      pur_add_cusventtree.column("5", width=70)
      pur_add_cusventtree.heading("#0",text="")
      pur_add_cusventtree.heading("1",text="ID/SKU")
      pur_add_cusventtree.heading("2",text="Product/Service Name")
      pur_add_cusventtree.heading("3",text="Unit price")
      pur_add_cusventtree.heading("4",text="Service")
      pur_add_cusventtree.heading("5",text="Stock")
      pur_add_cusventtree.place(x=5, y=45)

      pur_add_cusventtree.tag_configure('green', foreground='green')
      pur_add_cusventtree.tag_configure('red', foreground='red')
      pur_add_cusventtree.tag_configure('blue', foreground='blue')
      pur_add_cusventtree.place(x=5, y=45)

      sql = "SELECT * FROM Productservice"
      fbcursor.execute(sql)
      add_product_detail = fbcursor.fetchall()

      count = 0
      for p in add_product_detail:
        if True:
          pur_add_cusventtree.insert(parent='',index='end',iid=p,text='',values=(p[0],p[4],p[7],p[12],p[13]))
        else:
          pass
      count += 1
      


      countp = 0
      sql = 'select * from Productservice'
      fbcursor.execute(sql)
      purch_prodata = fbcursor.fetchall()
      for i in purch_prodata:
        if i[12] == '1':
          servi = '🗹'
        else:
          servi = ''
        sql = "select currencysign,currsignplace from company"
        fbcursor.execute(sql)
        currsymb = fbcursor.fetchone()
        if not currsymb: 
          if i[13] > i[14]:
            pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('green',))
            countp += 1              
          elif i[12] == '1':
            pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('blue',))
            countp += 1
          else:
            pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('red',))
            countp += 1
                      
        elif currsymb[1] == "before amount":
          if (i[13]) > (i[14]):
            pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0]+i[7],servi,i[13]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0]+i[7],servi,i[13]),tags=('blue',))
            countp += 1
          else:
              pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0]+i[7],servi,i[13]),tags=('red',))
              countp += 1

        elif currsymb[1] == "before amount with space":
          if i[13] > i[14]:
            pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0] +" "+i[7],servi,i[13]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0] +" "+i[7],servi,i[13]),tags=('blue',))
            countp += 1
          else:
            pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0] +" "+i[7],servi,i[13]),tags=('red',))
            countp += 1

        elif currsymb[1] == "after amount":
          if i[13] > i[14]:
            pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+currsymb[0],servi,i[13]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+currsymb[0],servi,i[13]),tags=('blue',))
            countp += 1
          else:
            pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+currsymb[0],servi,i[13]),tags=('red',))
            countp += 1

        elif currsymb[1] == "after amount with space":
          if i[13] > i[14]:
            pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[4],i[7]+" "+currsymb[0],servi,i[13]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[4],i[7]+" "+currsymb[0],servi,i[13]),tags=('blue',))
            countp += 1
          else:
            pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[4],i[7]+" "+currsymb[0],servi,i[13]),tags=('red',))
            countp += 1

      
      ctegorytree=ttk.Treeview(newselection, height=27)
      ctegorytree["columns"]=["1"]
      ctegorytree.column("#0", width=35, minwidth=20)
      ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
      ctegorytree.heading("#0",text="", anchor=W)
      ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
      ctegorytree.place(x=660, y=45)

      scrollbar = Scrollbar(newselection)
      scrollbar.place(x=640, y=45, height=560)
      scrollbar.config( command=tree.yview )


     
      
     

      def purchselepro():
        global purchpriceview
        purchpriceview = Label(listFrame,bg="#f5f3f2")
        purchpriceview.place(x=850,y=200,width=78,height=18)
        proskuid = pur_add_cusventtree.item(pur_add_cusventtree.focus())["values"][0]
        sql = "SELECT * FROM productservice WHERE sku = %s"
        val = (proskuid,)
        fbcursor.execute(sql,val)
        prosele = fbcursor.fetchone()
        print(prosele)
        sql = "select * from company"
        fbcursor.execute(sql)
        create_maintree_insert = fbcursor.fetchone()
        if prosele[10] == '1':
          tax1 = 'yes'
        else:
          tax1 = ''
        if prosele[19] == '1':
          tax2 = 'yes'
        else:
          tax2 = ''
        if not create_maintree_insert:
          purch_tree.insert(parent='', index='end',text='', values=(prosele[2],prosele[4],prosele[5],prosele[7],1,prosele[8],tax1,prosele[7]*1))

        elif create_maintree_insert[12] == "1":
          purch_tree.insert(parent='', index='end',text='', values=(prosele[2],prosele[4],prosele[5],prosele[7],1,prosele[8],prosele[7]*1))
          extracs = 0.0
          discou = 0.0
          total = 0.0
          for child in purch_tree.get_children():
            total += float(purch_tree.item(child, 'values')[6])
          discou = (total*float(pdisc.get())/100)
          extracs = (extracs+float(pcost.get()))
          cost.config(text=pcost.get())
          discount1.config(text=discou)
          purchpriceview.config(text=total)
          order1.config(text=total-discou+extracs)
          # estimate_balancee1.config(text=total-discou+extracs)
          sub1.config(text=total-discou)
        elif create_maintree_insert[12] == "2":
          purch_tree.insert(parent='', index='end',text='', values=(prosele[2],prosele[4],prosele[5],prosele[7],1,prosele[8],tax1,prosele[7]*1))
          extracs = 0.0
          discou = 0.0
          total = 0.0
          for child in purch_tree.get_children():
            total += float(purch_tree.item(child, 'values')[7])
          discou = (total*float(pdisc.get())/100)
          extracs = (extracs+float(pcost.get()))
          cost.config(text=pcost.get())
          discount1.config(text=discou)
          purchpriceview.config(text=total)
          sub1.config(text=total-discou)

          tot = 0.0
          totaltax1 = 0.0
          for child in purch_tree.get_children():
            checktax1 = list(purch_tree.item(child, 'values'))
            if checktax1[6] == "yes":
              totaltax1 =(totaltax1 + float(checktax1[7]))
              tax1.config(text=(float(totaltax1)*float(porder_tax4.get())/100))
              tot = (float(totaltax1)*float(porder_tax4.get())/100)
            else:
              pass
          order1.config(text=total+tot-discou+extracs)
          # estimate_balancee1.config(text=total+tot-discou+extracs)
            
        elif create_maintree_insert[12] == "3":
          purch_tree.insert(parent='', index='end',text='', values=(prosele[2],prosele[4],prosele[5],prosele[7],1,prosele[8],tax1,tax2,prosele[7]*1))
          extracs = 0.0
          discou = 0.0
          total = 0.0
          for child in purch_tree.get_children():
            total += float(purch_tree.item(child, 'values')[8])
          extracs = (extracs+float(pcost.get()))
          cost.config(text=pcost.get())
          discou = (total*float(pdisc.get())/100)
          discount1.config(text=discou)
          purchpriceview.config(text=total)
          sub1.config(text=total-discou)
            
          tot = 0.0
          totaltax1 = 0.0
          for child in purch_tree.get_children():
            checktax1 = list(purch_tree.item(child, 'values'))
            if checktax1[6] == "yes":
              totaltax1 =(totaltax1 + float(checktax1[8]))
              tax1.config(text=(float(totaltax1)*float(porder_tax4.get())/100))
              tot = (float(totaltax1)*float(porder_tax4.get())/100)
            else:
              pass
          
          tot2 = 0.0
          totaltax2 = 0.0
          for child in purch_tree.get_children():
            checktax1 = list(purch_tree.item(child, 'values'))
            if checktax1[7] == "yes":
              totaltax2 =(totaltax2 + float(checktax1[8]))
              tax2.config(text=(float(totaltax2)*float(porder_tax5.get())/100))
              
              tot2 = (float(totaltax2)*float(porder_tax5.get())/100)
            else:
              pass

          order1.config(text=total+tot+tot2-discou+extracs)
          # estimate_balancee1.config(text=total+tot+tot2-discou+extracs)


          valu10= pur_add_cusventtree.item(proskuid)["values"][0]
          sqllll = "SELECT * FROM productservice  WHERE productserviceid= %s"
          r=(valu10,)
          fbcursor.execute(sqllll,r)
          child=fbcursor.fetchone()

          sql21= 'INSERT INTO storingproduct(Productserviceid,porderid,sku,category,name,description,status,unitprice,peices,cost,taxable,priceminuscost,serviceornot,stock,stocklimit,warehouse,privatenote,quantity,tax2) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
          vatree=(child[0],pord_no,child[2],child[3],child[4],child[5],child[6],child[7],child[8],child[9],child[10],child[11],child[12],child[13],child[14],child[15],child[16],child[17],1)
          fbcursor.execute(sql21,vatree,)
          fbilldb.commit()

        
        newselection.destroy()

    

      btn1=Button(newselection,compound = LEFT,image=tick ,text="ok", width=60,command=purchselepro).place(x=15, y=610)
      btn1=Button(newselection,compound = LEFT,image=tick , text="Edit product/Service", width=150,command=edit_product).place(x=250, y=610)
      btn1=Button(newselection,compound = LEFT,image=tick , text="Add product/Service", width=150,command=adda_product).place(x=435, y=610)
      btn1=Button(newselection,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=610)


    def add_new_porder():
      #estidd = porder_number_entry0.get()
      porderid = porder_id_entry.get()
      porderdate = pdate.get_date()
      duedate = pdue.get_date()
      status = draft.cget("text")
      emailon = nev1.cget("text")
      printon = nev2.cget("text")
      #smson = 
      pordtot =  order1.cget("text")
      # totpaid = porder_totalpaid1.cget("text")
      # balance = porder_balancee1.cget("text")
      extracostname = pextra.get()
      extracost = pcost.get()
      # template = porders_etemplate.get()
      salesper =  psale.get()
      discourate = pdisc.get()
      tax1 =  porder_tax4.get()
      tax2 =  porder_tax5.get()
      category = pact.get()
      businessname = vender_combo.get()
      businessaddress = paddress.get("1.0",END)
      delname = pdel.get()
      deladdress =  pdel_addr.get("1.0",END)
      cpemail = pmail.get()
      cpmobileforsms = psms.get()
      title_text = e1.get()
      header_text = e11.get()
      footer_text = e12.get()
      term_of_payment = e4.get()
      terms = e13.get("1.0","end-1c")
      comments = e14.get("1.0","end-1c")
      private_notes = pvt.get("1.0","end-1c")
      sum_dis = discount1.cget("text")
      sum_subtotal = sub1.cget("text")
      sum_tax1 = summery_tax1.cget("text")
      sum_tax2 = summery_tax2.cget("text")
      
      

      porder_sql="INSERT INTO porder (porder_no,porderdate,duedate,status,emailon,printon,	ordertot,extracostname,extracost, salesper,discourate,tax1,	tax2, category,businessname,businessaddress,deliveryto, deliveryaddress,cpemail,cpmobileforsms,title_text, header_text,footer_text,term_of_payment,terms,comments,privatenote,sumdiscount,sumsubtotal,sumtax1,sumtax2) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" #adding values into db
      porder_val=(porderid,porderdate,duedate,status,emailon,printon,pordtot,extracostname,extracost, salesper,discourate,tax1,	tax2, category,businessname,businessaddress,delname, deladdress,cpemail,cpmobileforsms,title_text, header_text, footer_text,term_of_payment,terms,comments,private_notes,sum_dis,sum_subtotal,sum_tax1,sum_tax2)
      fbcursor.execute(porder_sql,porder_val)
      fbilldb.commit()
      #messagebox.showinfo("F-Billing Revolution","porder saved")
      

    #preview new line
    # def previewline1():
    #   messagebox.showerror("F-Billing Revolution","line is required,please select customer for this order before printing.")
#Preview estimate
    global prev_pord
    def prev_pord():
      sql = 'select * from company'
      fbcursor.execute(sql)
      pord_compdataord = fbcursor.fetchone()

      previewcreate = Toplevel()
      previewcreate.geometry("1360x730")
      frame = Frame(previewcreate, width=953, height=300)
      frame.pack(expand=True, fill=BOTH)
      frame.place(x=5,y=30)
      canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,1200))
        
      vertibar=Scrollbar(frame, orient=VERTICAL)
      vertibar.pack(side=RIGHT,fill=Y)
      vertibar.config(command=canvas.yview)

      canvas.config(width=1315,height=640)
      canvas.config(yscrollcommand=vertibar.set)
      canvas.pack(expand=True,side=LEFT,fill=BOTH)
      canvas.create_rectangle(235, 25, 1035, 1175, outline='yellow',fill='white')

      com_label = Label(canvas,text=" "+e1.get(),font=('Helvetica 10 '),background='white')
      com_label_window = canvas.create_window(550, 65, anchor="w", window=com_label)

      try:
          image = Image.open("images/"+pord_compdataord[13])
          resize_image = image.resize((250, 125))
          loimg = ImageTk.PhotoImage(resize_image)
          b2 = Label(canvas,image=loimg, height=125, width=250,)
          b2.photo = loimg
          canvas.create_window(425, 150,window=b2)
      except:
        pass
        
      com_label = Label(canvas,text=" "+pord_str2.get(),font=('Helvetica 12 '),background='white')
      com_label_window = canvas.create_window(300, 240, anchor="w", window=com_label)
        
      com_label = Label(canvas,text=" "+pord_str3.get(),font=('Helvetica 12 '),background='white')
      com_label_window = canvas.create_window(300, 260, anchor="w", window=com_label)
        
      com_label = Label(canvas,text=" "+pord_str4.get(),font=('Helvetica 12 '),background='white')
      com_label_window = canvas.create_window(301, 280, anchor="w", window=com_label)

      com_label = Label(canvas,text=" "+porder_id_entry.get(),font=('Helvetica 12 '),background='white')
      com_label_window = canvas.create_window(471, 240, anchor="w", window=com_label)

      canvas.create_text(520, 260, text=pdate.get_date(), fill="black", font=('Helvetica 12')) 
      canvas.create_text(520, 280, text=pdue.get_date(), fill="black", font=('Helvetica 12'))

      com_label = Label(canvas,text="Terms",font=('Helvetica 12 '),background='white')
      com_label_window = canvas.create_window(303, 300, anchor="w", window=com_label)

      com_label = Label(canvas,text="Order ref.#",font=('Helvetica 12 '),background='white')
      com_label_window = canvas.create_window(303, 320, anchor="w", window=com_label)

      com_label = Label(canvas,text=" "+e4.get(),font=('Helvetica 12 '),background='white')
      com_label_window = canvas.create_window(470, 300, anchor="w", window=com_label)
      
      com_label = Label(canvas,text=" "+pref.get(),font=('Helvetica 12 '),background='white')
      com_label_window = canvas.create_window(470, 320, anchor="w", window=com_label)

        
      com_label = Label(canvas,text=" "+comname.get(),font=('Helvetica 12 '),background='white')
      com_label_window = canvas.create_window(976, 100, anchor="e", window=com_label)

      T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0,cursor="arrow")
      T_address.tag_configure('tag_name',justify='right')
      T_address.insert('1.0', pord_compdataord[2])
      T_address.tag_add('tag_name','1.0', 'end')
      T_address.config(state=DISABLED)
      T_address_window = canvas.create_window(694, 125, anchor="nw", window=T_address)

      com_label = Label(canvas,text=" "+comsalestax.get(),font=('Helvetica 10 '),background='white')
      com_label_window = canvas.create_window(976, 225, anchor="e", window=com_label)

      com_label = Label(canvas,text=" "+pord_str1.get(),font=('Helvetica 20 bold '),background='white')
      com_label_window = canvas.create_window(976, 255, anchor="e", window=com_label)

      com_label = Label(canvas,text=""+pord_str5.get(),font=('Helvetica 10 underline'),background='white')
      com_label_window = canvas.create_window(301, 345, anchor="w", window=com_label)

      com_label = Label(canvas,text="Delivery to",font=('Helvetica 10 underline'),background='white')
      com_label_window = canvas.create_window(660, 345, anchor="w", window=com_label)

      com_label = Label(canvas,text=" "+vender_combo.get(),font=('Helvetica 10'),background='white')
      com_label_window = canvas.create_window(302, 365, anchor="w", window=com_label)

      com_label = Label(canvas,text=""+pdel.get(),font=('Helvetica 10'),background='white')
      com_label_window = canvas.create_window(662, 365, anchor="w", window=com_label)

      T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0,cursor="arrow")
      T_address.tag_configure('tag_name',justify='left')
      T_address.insert('1.0', paddress.get("1.0",END))
      T_address.tag_add('tag_name','1.0', 'end')
      T_address.config(state=DISABLED)
      T_address_window = canvas.create_window(306, 380, anchor="nw", window=T_address)

      T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0,cursor="arrow")
      T_address.tag_configure('tag_name',justify='left')
      T_address.insert('1.0', pdel_addr.get("1.0",END))
      T_address.tag_add('tag_name','1.0', 'end')
      T_address.config(state=DISABLED)
      T_address_window = canvas.create_window(665, 380, anchor="nw", window=T_address)

      com_label = Label(canvas,text=" "+e11.get(),font=('Helvetica 10 '),background='white')
      com_label_window = canvas.create_window(550, 455, anchor="w", window=com_label)

      s = ttk.Style()
      s.configure('mystyle_prev_2.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

      pord_prev_tree=ttk.Treeview(canvas, show='headings',height= 11, style='mystyle_prev_2.Treeview')
      pord_prev_tree["columns"] = ["1","2","3","4","5"]
      pord_prev_tree.column("# 0",width=1)
      pord_prev_tree.column("1", anchor=CENTER, width=100)
      pord_prev_tree.column("2", anchor=CENTER, width=350)
      pord_prev_tree.column("3", anchor=CENTER, width=80)
      pord_prev_tree.column("4", anchor=CENTER, width=90)
      pord_prev_tree.column("5", anchor=E, width=85)
      pord_prev_tree.heading("#0", text="")
      pord_prev_tree.heading("1", text="ID/SKU")
      pord_prev_tree.heading("2", text="Product/Service - Description")
      pord_prev_tree.heading("3", text="Quantity")
      pord_prev_tree.heading("4", text="Unit Price")
      pord_prev_tree.heading("5", text="Price")
      window = canvas.create_window(275, 470, anchor="nw", window=pord_prev_tree)
      sql = "select * from company"
      fbcursor.execute(sql)
      taxcheck = fbcursor.fetchone()

      sql = "select currsignplace,currencysign from company"
      fbcursor.execute(sql)
      symbolcheck = fbcursor.fetchone()
        


      for record in purch_tree.get_children():
        previewdata1 = list(purch_tree.item(record, 'values'))
        if not taxcheck:
          pord_prev_tree.insert(parent='', index='end',text='', values=(previewdata1[0],previewdata1[1]+"-"+previewdata1[2],previewdata1[4],previewdata1[3],previewdata1[6]))
        elif taxcheck[12] == "1":
          pord_prev_tree.insert(parent='', index='end',text='', values=(previewdata1[0],previewdata1[1]+"-"+previewdata1[2],previewdata1[4],previewdata1[3],previewdata1[6]))
        elif taxcheck[12] == "2":
          pord_prev_tree.insert(parent='', index='end',text='', values=(previewdata1[0],previewdata1[1]+"-"+previewdata1[2],previewdata1[4],previewdata1[3],previewdata1[7]))
        elif taxcheck[12] == "3":
          pord_prev_tree.insert(parent='', index='end',text='', values=(previewdata1[0],previewdata1[1]+"-"+previewdata1[2],previewdata1[4],previewdata1[3],previewdata1[8]))
      
      if taxcheck[12] == "1":
        canvas.create_line(980, 715, 980, 815 )
        canvas.create_line(720, 715, 720, 815 )
        canvas.create_line(860, 715, 860, 815 )#1st
        canvas.create_line(980, 815, 720, 815 )
        canvas.create_line(980, 715, 720, 715 )
        canvas.create_line(980, 740, 720, 740 )
        canvas.create_line(980, 765, 720, 765 ) 
        canvas.create_line(980, 790, 720, 790 )
        canvas.create_line(980, 815, 720, 815 )

        if not symbolcheck:
          canvas.create_text(780, 730, text=str(float(pdisc.get())) + "" +"% Discount", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=str(discount1.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 729, anchor="e", window=com_label)  
  
          canvas.create_text(780, 755, text="Subtotal", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=str(sub1.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 754, anchor="e", window=com_label)  
  
            
          com_label = Label(canvas,text=str(cost.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 779, anchor="e", window=com_label)  
            
          com_label = Label(canvas,text=""+pextra.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(725, 779, anchor="w", window=com_label)  
  
          com_label = Label(canvas,text=str(order1.cget("text")),font=('Helvetica 10 bold'),background='white')
          com_label_window = canvas.create_window(975, 805, anchor="e", window=com_label)  
            
          com_label = Label(canvas,text=" "+pord_str6.get(),font=('Helvetica 10 bold'),background='white')
          com_label_window = canvas.create_window(731, 804, anchor="w", window=com_label)
        

        elif symbolcheck[0] == "before amount":
          canvas.create_text(780, 730, text=str(float(pdisc.get())) + "" +"% Discount", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=""+comcursign.get()+str(discount1.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 729, anchor="e", window=com_label)  
  
  
          canvas.create_text(780, 755, text="Subtotal", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=""+comcursign.get()+str(sub1.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 754, anchor="e", window=com_label)  
   
          com_label = Label(canvas,text=""+comcursign.get()+str(cost.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 779, anchor="e", window=com_label)  
            
          com_label = Label(canvas,text=""+pextra.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(725, 779, anchor="w", window=com_label)  
  
          com_label = Label(canvas,text=""+comcursign.get()+str(order1.cget("text")),font=('Helvetica 10 bold'),background='white')
          com_label_window = canvas.create_window(975, 804, anchor="e", window=com_label)  
            
          com_label = Label(canvas,text=" "+pord_str6.get(),font=('Helvetica 10 bold'),background='white')
          com_label_window = canvas.create_window(731, 804, anchor="w", window=com_label)
        
        elif symbolcheck[0] == "before amount with space":
          canvas.create_text(780, 730, text=str(float(pdisc.get())) + "" +"% Discount", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=""+comcursign.get()+" "+str(discount1.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 729, anchor="e", window=com_label)  
  
          canvas.create_text(780, 755, text="Subtotal", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=""+comcursign.get()+" "+str(sub1.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 754, anchor="e", window=com_label)  
  
            
          com_label = Label(canvas,text=""+comcursign.get()+" "+str(cost.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 779, anchor="e", window=com_label)  
            
          com_label = Label(canvas,text=""+pextra.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(725, 779, anchor="w", window=com_label)  
  
            
          com_label = Label(canvas,text=""+comcursign.get()+" "+str(order1.cget("text")),font=('Helvetica 10 bold'),background='white')
          com_label_window = canvas.create_window(975, 804, anchor="e", window=com_label)  
            
          com_label = Label(canvas,text=" "+pord_str6.get(),font=('Helvetica 10 bold'),background='white')
          com_label_window = canvas.create_window(731, 804, anchor="w", window=com_label)
        
        elif symbolcheck[0] == "after amount":
          canvas.create_text(780, 730, text=str(float(pdisc.get())) + "" +"% Discount", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=str(discount1.cget("text"))+""+comcursign.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 729, anchor="e", window=com_label)  
  
          canvas.create_text(780, 755, text="Subtotal", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=str(sub1.cget("text"))+""+comcursign.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 754, anchor="e", window=com_label)
  
          com_label = Label(canvas,text=str(cost.cget("text"))+""+comcursign.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 779, anchor="e", window=com_label)
            
          com_label = Label(canvas,text=""+pextra.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(725, 779, anchor="w", window=com_label)  
  
          com_label = Label(canvas,text=str(order1.cget("text"))+""+comcursign.get(),font=('Helvetica 10 bold'),background='white')
          com_label_window = canvas.create_window(975, 804, anchor="e", window=com_label)
            
          com_label = Label(canvas,text=" "+pord_str6.get(),font=('Helvetica 10 bold'),background='white')
          com_label_window = canvas.create_window(731, 804, anchor="w", window=com_label)
        
        elif symbolcheck[0] == "after amount with space":
          canvas.create_text(780, 730, text=str(float(pdisc.get())) + "" +"% Discount", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=str(discount1.cget("text"))+" "+""+comcursign.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 729, anchor="e", window=com_label)  
            
  
          canvas.create_text(780, 755, text="Subtotal", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=str(sub1.cget("text"))+" "+""+comcursign.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 754, anchor="e", window=com_label)
    
          com_label = Label(canvas,text=str(cost.cget("text"))+" "+""+comcursign.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 779, anchor="e", window=com_label)
            
          com_label = Label(canvas,text=""+pextra.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(725, 779, anchor="w", window=com_label)  
  
          com_label = Label(canvas,text=str(order1.cget("text"))+" "+""+comcursign.get(),font=('Helvetica 10 bold'),background='white')
          com_label_window = canvas.create_window(975, 804, anchor="e", window=com_label)
            
          com_label = Label(canvas,text=" "+pord_str6.get(),font=('Helvetica 10 bold'),background='white')
          com_label_window = canvas.create_window(731, 804, anchor="w", window=com_label)
        
      elif taxcheck[12] == "2":
        canvas.create_line(980, 715, 980, 840 )
        canvas.create_line(720, 715, 720, 840 )
        canvas.create_line(860, 715, 860, 840 )#1st
        canvas.create_line(980, 815, 720, 815 )
        canvas.create_line(980, 715, 720, 715 )
        canvas.create_line(980, 740, 720, 740 )
        canvas.create_line(980, 765, 720, 765 ) 
        canvas.create_line(980, 790, 720, 790 )
        canvas.create_line(980, 815, 720, 815 )
        canvas.create_line(980, 840, 720, 840 )

        if not symbolcheck:
          canvas.create_text(780, 730, text=str(float(pdisc.get())) + "" +"% Discount", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=str(discount1.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 729, anchor="e", window=com_label)  
  
  
          canvas.create_text(780, 755, text="Subtotal", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=str(sub1.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 754, anchor="e", window=com_label)
  
          canvas.create_text(780, 780, text="TAX1", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=str(summery_tax1.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 779, anchor="e", window=com_label)
  
          com_label = Label(canvas,text=str(cost.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 804, anchor="e", window=com_label)
            
          com_label = Label(canvas,text=""+pextra.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(725, 804, anchor="w", window=com_label)  
  
          com_label = Label(canvas,text=str(order1.cget("text")),font=('Helvetica 10 bold'),background='white')
          com_label_window = canvas.create_window(975, 829, anchor="e", window=com_label)
             
          com_label = Label(canvas,text=" "+pord_str6.get(),font=('Helvetica 10 bold'),background='white')
          com_label_window = canvas.create_window(731, 829, anchor="w", window=com_label)
        
        elif symbolcheck[0] == "before amount":
          canvas.create_text(780, 730, text=str(float(pdisc.get())) + "" +"% Discount", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=""+comcursign.get()+str(discount1.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 729, anchor="e", window=com_label)  
  
          canvas.create_text(780, 755, text="Subtotal", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=""+comcursign.get()+str(sub1.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 754, anchor="e", window=com_label)  
  
          canvas.create_text(780, 780, text="TAX1", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=""+comcursign.get()+str(summery_tax1.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 779, anchor="e", window=com_label)  
  
          com_label = Label(canvas,text=""+comcursign.get()+str(cost.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 804, anchor="e", window=com_label)  
            
          com_label = Label(canvas,text=""+pextra.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(725, 804, anchor="w", window=com_label)  
  
          com_label = Label(canvas,text=""+comcursign.get()+str(order1.cget("text")),font=('Helvetica 10 bold'),background='white')
          com_label_window = canvas.create_window(975, 830, anchor="e", window=com_label)  
            
          com_label = Label(canvas,text=" "+pord_str6.get(),font=('Helvetica 10 bold'),background='white')
          com_label_window = canvas.create_window(731, 829, anchor="w", window=com_label)
        
      
        elif symbolcheck[0] == "before amount with space":
          canvas.create_text(780, 730, text=str(float(pdisc.get())) + "" +"% Discount", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=""+comcursign.get()+" "+str(discount1.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 729, anchor="e", window=com_label)  

          canvas.create_text(780, 755, text="Subtotal", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=""+comcursign.get()+" "+str(sub1.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 754, anchor="e", window=com_label)

          canvas.create_text(780, 780, text="TAX1", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=""+comcursign.get()+" "+str(summery_tax1.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 779, anchor="e", window=com_label)

          com_label = Label(canvas,text=""+comcursign.get()+" "+str(cost.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 804, anchor="e", window=com_label)
            
          com_label = Label(canvas,text=""+pextra.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(725, 804, anchor="w", window=com_label)  

          com_label = Label(canvas,text=""+comcursign.get()+" "+str(order1.cget("text")),font=('Helvetica 10 bold'),background='white')
          com_label_window = canvas.create_window(975, 829, anchor="e", window=com_label)
            
          com_label = Label(canvas,text=" "+pord_str6.get(),font=('Helvetica 10 bold'),background='white')
          com_label_window = canvas.create_window(731, 829, anchor="w", window=com_label)
        
          
        elif symbolcheck[0] == "after amount":
          canvas.create_text(780, 730, text=str(float(pdisc.get())) + "" +"% Discount", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=str(discount1.cget("text"))+""+comcursign.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 729, anchor="e", window=com_label)  
  
          canvas.create_text(780, 755, text="Subtotal", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=str(sub1.cget("text"))+""+comcursign.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 754, anchor="e", window=com_label)
  
          canvas.create_text(780, 780, text="TAX1", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=str(summery_tax1.cget("text"))+""+comcursign.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 779, anchor="e", window=com_label)
  
          com_label = Label(canvas,text=str(cost.cget("text"))+""+comcursign.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 804, anchor="e", window=com_label)
            
          com_label = Label(canvas,text=""+pextra.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(725, 804, anchor="w", window=com_label)  
  
          com_label = Label(canvas,text=str(order1.cget("text"))+""+comcursign.get(),font=('Helvetica 10 bold'),background='white')
          com_label_window = canvas.create_window(975, 829, anchor="e", window=com_label)
            
          com_label = Label(canvas,text=" "+pord_str6.get(),font=('Helvetica 10 bold'),background='white')
          com_label_window = canvas.create_window(731, 829, anchor="w", window=com_label)
        
          
        elif symbolcheck[0] == "after amount with space":
          canvas.create_text(780, 730, text=str(float(pdisc.get())) + "" +"% Discount", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=str(discount1.cget("text"))+" "+""+comcursign.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 729, anchor="e", window=com_label) 
  
          canvas.create_text(780, 755, text="Subtotal", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=str(sub1.cget("text"))+" "+""+comcursign.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 754, anchor="e", window=com_label) 
  
          canvas.create_text(780, 780, text="TAX1", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=str(summery_tax1.cget("text"))+" "+""+comcursign.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 779, anchor="e", window=com_label) 
  
          com_label = Label(canvas,text=str(cost.cget("text"))+" "+""+comcursign.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 804, anchor="e", window=com_label) 
            
          com_label = Label(canvas,text=""+pextra.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(725, 804, anchor="w", window=com_label)  
  
          com_label = Label(canvas,text=str(order1.cget("text"))+" "+""+comcursign.get(),font=('Helvetica 10 bold'),background='white')
          com_label_window = canvas.create_window(975, 829, anchor="e", window=com_label) 
            
          com_label = Label(canvas,text=" "+pord_str6.get(),font=('Helvetica 10 bold'),background='white')
          com_label_window = canvas.create_window(731, 829, anchor="w", window=com_label)
        
      elif taxcheck[12] == "3":
        canvas.create_line(980, 715, 980, 865 )
        canvas.create_line(720, 715, 720, 865 )
        canvas.create_line(860, 715, 860, 865 )#1st
        canvas.create_line(980, 815, 720, 815 )
        canvas.create_line(980, 715, 720, 715 )
        canvas.create_line(980, 740, 720, 740 )
        canvas.create_line(980, 765, 720, 765 ) 
        canvas.create_line(980, 790, 720, 790 )
        canvas.create_line(980, 815, 720, 815 )
        canvas.create_line(980, 840, 720, 840 )
        canvas.create_line(980, 865, 720, 865 )


        if not symbolcheck:
          canvas.create_text(780, 730, text=str(float(pdisc.get())) + "" +"% Discount", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=str(discount1.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 729, anchor="e", window=com_label)
  
          canvas.create_text(780, 755, text="Subtotal", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=str(sub1.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 754, anchor="e", window=com_label)
  
          canvas.create_text(780, 780, text="TAX1", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=str(summery_tax1.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 779, anchor="e", window=com_label)
  
            
          com_label = Label(canvas,text=str(tax2.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 804, anchor="e", window=com_label)
          canvas.create_text(780, 805, text="TAX2", fill="black", font=('Helvetica 10 '))
  
            
          com_label = Label(canvas,text=str(cost.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 829, anchor="e", window=com_label)
            
          com_label = Label(canvas,text=""+pextra.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(725, 829, anchor="w", window=com_label)  
            
          com_label = Label(canvas,text=str(order1.cget("text")),font=('Helvetica 10 bold'),background='white')
          com_label_window = canvas.create_window(975, 854, anchor="e", window=com_label)
            
          com_label = Label(canvas,text=" "+pord_str6.get(),font=('Helvetica 10 bold'),background='white')
          com_label_window = canvas.create_window(731, 854, anchor="w", window=com_label)
        
        elif symbolcheck[0] == "before amount":
            
          canvas.create_text(780, 730, text=str(float(pdisc.get())) + "" +"% Discount", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=""+comcursign.get()+str(discount1.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 729, anchor="e", window=com_label)
  
          canvas.create_text(780, 755, text="Subtotal", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=""+comcursign.get()+str(sub1.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 754, anchor="e", window=com_label)
  
          canvas.create_text(780, 780, text="TAX1", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=""+comcursign.get()+str(summery_tax1.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 779, anchor="e", window=com_label)
    
          com_label = Label(canvas,text=""+comcursign.get()+str(summery_tax2.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 804, anchor="e", window=com_label)
          canvas.create_text(780, 805, text="TAX2", fill="black", font=('Helvetica 10 '))
  
          com_label = Label(canvas,text=""+comcursign.get()+str(cost.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 829, anchor="e", window=com_label)
            
          com_label = Label(canvas,text=""+pextra.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(725, 829, anchor="w", window=com_label)  
            
          com_label = Label(canvas,text=""+comcursign.get()+str(order1.cget("text")),font=('Helvetica 10 bold'),background='white')
          com_label_window = canvas.create_window(975, 854, anchor="e", window=com_label)
            
          com_label = Label(canvas,text=" "+pord_str6.get(),font=('Helvetica 10 bold'),background='white')
          com_label_window = canvas.create_window(731, 854, anchor="w", window=com_label)
            
          
        elif symbolcheck[0] == "before amount with space":
            
          canvas.create_text(780, 730, text=str(float(pdisc.get())) + "" +"% Discount", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=""+comcursign.get()+" "+str(discount1.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 729, anchor="e", window=com_label)
  
          canvas.create_text(780, 755, text="Subtotal", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=""+comcursign.get()+" "+str(sub1.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 754, anchor="e", window=com_label)
  
          canvas.create_text(780, 780, text="TAX1", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=""+comcursign.get()+" "+str(summery_tax1.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 779, anchor="e", window=com_label)
  
          com_label = Label(canvas,text=""+comcursign.get()+" "+str(summery_tax2.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 804, anchor="e", window=com_label)
          canvas.create_text(780, 805, text="TAX2", fill="black", font=('Helvetica 10 '))
  
          com_label = Label(canvas,text=""+comcursign.get()+" "+str(cost.cget("text")),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 829, anchor="e", window=com_label)
            
          com_label = Label(canvas,text=""+pextra.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(725, 829, anchor="w", window=com_label)  
           
          com_label = Label(canvas,text=""+comcursign.get()+" "+str(order1.cget("text")),font=('Helvetica 10 bold'),background='white')
          com_label_window = canvas.create_window(975, 854, anchor="e", window=com_label)
            
          com_label = Label(canvas,text=" "+pord_str6.get(),font=('Helvetica 10 bold'),background='white')
          com_label_window = canvas.create_window(731, 854, anchor="w", window=com_label)
            
        elif symbolcheck[0] == "after amount":
            
          canvas.create_text(780, 730, text=str(float(pdisc.get())) + "" +"% Discount", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=str(discount1.cget("text"))+""+comcursign.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 729, anchor="e", window=com_label)
  
  
          canvas.create_text(780, 755, text="Subtotal", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=str(sub1.cget("text"))+""+comcursign.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 754, anchor="e", window=com_label)
  
          canvas.create_text(780, 780, text="TAX1", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=str(summery_tax1.cget("text"))+""+comcursign.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 779, anchor="e", window=com_label)
  
          com_label = Label(canvas,text=str(summery_tax2.cget("text"))+""+comcursign.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 804, anchor="e", window=com_label)
          canvas.create_text(780, 805, text="TAX2", fill="black", font=('Helvetica 10 '))
  
          com_label = Label(canvas,text=str(cost.cget("text"))+""+comcursign.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 829, anchor="e", window=com_label)
            
          com_label = Label(canvas,text=""+pextra.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(725, 829, anchor="w", window=com_label)  
            
          com_label = Label(canvas,text=str(order1.cget("text"))+""+comcursign.get(),font=('Helvetica 10  bold'),background='white')
          com_label_window = canvas.create_window(975, 854, anchor="e", window=com_label)
            
          com_label = Label(canvas,text=" "+pord_str6.get(),font=('Helvetica 10 bold'),background='white')
          com_label_window = canvas.create_window(731, 854, anchor="w", window=com_label)
            
        elif symbolcheck[0] == "after amount with space":
            
          canvas.create_text(780, 730, text=str(float(pdisc.get())) + "" +"% Discount", fill="black", font=('Helvetica 10'))

          com_label = Label(canvas,text=str(discount1.cget("text"))+" "+""+comcursign.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 729, anchor="e", window=com_label)  
  
          canvas.create_text(780, 755, text="Subtotal", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=str(sub1.cget("text"))+" "+""+comcursign.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 754, anchor="e", window=com_label)  
  
          canvas.create_text(780, 780, text="TAX1", fill="black", font=('Helvetica 10'))
            
          com_label = Label(canvas,text=str(summery_tax1.cget("text"))+" "+""+comcursign.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 779, anchor="e", window=com_label)  
  
            
          com_label = Label(canvas,text=str(summery_tax2.cget("text"))+" "+""+comcursign.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 805, anchor="e", window=com_label)  
          canvas.create_text(780, 805, text="TAX2", fill="black", font=('Helvetica 10 '))
  
            
          com_label = Label(canvas,text=str(cost.cget("text"))+" "+""+comcursign.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(975, 829, anchor="e", window=com_label)  
            
          com_label = Label(canvas,text=""+pextra.get(),font=('Helvetica 10 '),background='white')
          com_label_window = canvas.create_window(725, 829, anchor="w", window=com_label)  
           
          com_label = Label(canvas,text=str(order1.cget("text"))+" "+""+comcursign.get(),font=('Helvetica 10 bold'),background='white')
          com_label_window = canvas.create_window(975, 854, anchor="e", window=com_label)  
            
          com_label = Label(canvas,text=" "+pord_str6.get(),font=('Helvetica 10 bold'),background='white')
          com_label_window = canvas.create_window(731, 854, anchor="w", window=com_label)
        
  
            
      pord_comments = Text(canvas,font=('Helvetica 10'),width=105,height=6,fg= "black",
      bg="white",cursor="arrow",bd=0)
      pord_comments.insert("1.0",e14.get("1.0","end-1c"))
      pord_comments.config(state=DISABLED)
      canvas.create_window(630, 950,window=pord_comments)
      canvas.create_text(620, 1020, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
      canvas.create_line(265, 1040, 1000, 1040)

      T = Text(canvas, height=3, width=105, font=('Helvetica 10'),borderwidth=0,cursor="arrow")
      T.insert(END, e13.get("1.0","end-1c"))
      T.config(state=DISABLED)
      T_window = canvas.create_window(270, 1055, anchor="nw", window=T)

      canvas.create_text(315, 1140, text="Sales Person:", fill="black", font=('Helvetica 10'))
      canvas.create_text(395, 1140, text=""+psale.get(), fill="black", font=('Helvetica 10'))

      com_label = Label(canvas,text=" "+e12.get(),font=('Helvetica 10 '),background='white')
      com_label_window = canvas.create_window(268, 1160, anchor="w", window=com_label)

      canvas.create_text(960, 1160, text="Page 1 of 1", fill="black", font=('Helvetica 10'))                 


    #sms notification
    def smspurch():
      send_SMS=Toplevel()
      send_SMS.geometry("700x480+240+150")
      send_SMS.title("Send SMS notification")

      style = ttk.Style()
      style.theme_use('default')
      style.configure('TNotebook.Tab', background="#999999", padding=5)
      sms_Notebook = ttk.Notebook(send_SMS)
      SMS_Notification = Frame(sms_Notebook, height=470, width=700)
      SMS_Service_Account = Frame(sms_Notebook, height=470, width=700)
      sms_Notebook.add(SMS_Notification, text="SMS Notification")
      sms_Notebook.add(SMS_Service_Account, text="SMS Service Account")
      sms_Notebook.place(x=0, y=0)

      numlbel=Label(SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
      numlbel.place(x=10, y=10)
      numentry=Entry(SMS_Notification, width=92).place(x=10, y=30)
      stexbel=Label(SMS_Notification, text="SMS Text").place(x=10, y=60)
      stex=Entry(SMS_Notification, width=40).place(x=10, y=85,height=120)
      
      dclbel=Label(SMS_Notification, text="Double click to insert into text")
      dclbel.place(x=410, y=60)
      dcl=Entry(SMS_Notification, width=30)
      dcl.place(x=400, y=85,height=200)

      smstype=LabelFrame(SMS_Notification, text="SMS message type", width=377, height=60)
      smstype.place(x=10, y=223)
      snuvar=IntVar()
      normal_rbtn=Radiobutton(smstype, text="Normal SMS(160 chars)", variable=snuvar, value=1)
      normal_rbtn.place(x=5, y=5)
      unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)", variable=snuvar, value=2)
      unicode_rbtn.place(x=190, y=5)
      tiplbf=LabelFrame(SMS_Notification, text="Tips", width=680, height=120)
      tiplbf.place(x=10, y=290)
      tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="Always start the SMS nymber with the country code. Do not use the + sign at the beginning(example\nUS number:8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
      tiplabl.place(x=5, y=5)

      btn1=Button(SMS_Notification, width=20, text="Send SMS notification").place(x=10, y=420)
      btn2=Button(SMS_Notification, width=25, text="Confirm SMS cost before sending").place(x=280, y=420)
      btn3=Button(SMS_Notification, width=15, text="Cancel").place(x=550, y=420)
      

      smstype=LabelFrame(SMS_Service_Account, text="Select the notification service provider", width=670, height=65)
      smstype.place(x=10, y=5)
      snumvar=IntVar()
      normal_rbtn=Radiobutton(smstype,text="BULKSMS(www.bulksms.com)",variable=snumvar,value=1,)
      normal_rbtn.place(x=5, y=5)
      unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)-Recommended", variable=snumvar, value=2)
      unicode_rbtn.place(x=290, y=5)

      sms1type=LabelFrame(SMS_Service_Account, text="Your BULKSMS.COM Account", width=670, height=100)
      sms1type.place(x=10, y=80)
      name=Label(sms1type, text="Username").place(x=10, y=5)
      na=Entry(sms1type, width=20).place(x=100, y=5)
      password=Label(sms1type, text="Password").place(x=10, y=45)
      pas=Entry(sms1type, width=20).place(x=100, y=45)
      combo=Label(sms1type, text="Route").place(x=400, y=5)
      n = StringVar()
      combo1 = ttk.Combobox(sms1type, width = 20, textvariable = n ).place(x=450,y=5)
      btn1=Button(sms1type, width=10, text="Save settings").place(x=550, y=45)

      
      tiplbf=LabelFrame(SMS_Service_Account, text="Terms of service", width=680, height=250)
      tiplbf.place(x=10, y=190)
      tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
      tiplabl.place(x=0, y=5)
      tiplabl1=Label(tiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
      tiplabl1.place(x=0, y=60)
      tiplabl2=Label(tiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
      tiplabl2.place(x=0, y=100)
      tiplabl3=Label(tiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
      tiplabl3.place(x=0, y=140)
      checkvar1=IntVar()
      chkbtn1=Checkbutton(tiplbf,text="I have read and agree to the terms of service above",variable=checkvar1,onvalue=1,offvalue=0).place(x=70, y=200) 
  

    #delete line item 
    def deletepurch():
      try:
        selected_item = purch_tree.selection()[0]
        purch_tree.delete(selected_item)
        sql = "select * from company"
        fbcursor.execute(sql)
        del_pord = fbcursor.fetchone()
        if del_pord[12] == "1":
          extracs = 0.0
          discou = 0.0
          total = 0.0
          for child in purch_tree.get_children():
            total += float(purch_tree.item(child, 'values')[6])
          discou = (total*float(pdisc.get())/100)
          extracs = (extracs+float(pcost.get()))
          cost.config(text=pcost.get())
          discount1.config(text=discou)
          pordpriceview.config(text=total)
          order1.config(text=total-discou+extracs)
          sub1.config(text=total-discou)
        elif del_pord[12] == "2":
          extracs = 0.0
          discou = 0.0
          total = 0.0
          for child in purch_tree.get_children():
            total += float(purch_tree.item(child, 'values')[7])
          discou = (total*float(pdisc.get())/100)
          extracs = (extracs+float(pcost.get()))
          cost.config(text=pcost.get())
          discount1.config(text=discou)
          pordpriceview.config(text=total)
          sub1.config(text=total-discou)

          tot = 0.0
          totaltax1 = 0.0
          for child in purch_tree.get_children():
            checktax1 = list(purch_tree.item(child, 'values'))
            if checktax1[6] == "yes":
              totaltax1 =(totaltax1 + float(checktax1[7]))
              summery_tax1.config(text=(float(totaltax1)*float(porder_tax4.get())/100))
              tot = (float(totaltax1)*float(porder_tax4.get())/100)
            else:
              pass
          order1.config(text=total+tot-discou+extracs)
        #   estimate_balancee1.config(text=total+tot-discou+extracs)
            
        elif del_pord[12] == "3":
          # purch_tree.insert(parent='', index='end',text='', values=(prosele[2],prosele[4],prosele[5],prosele[7],1,prosele[8],tax1,tax2,prosele[7]*1))
          extracs = 0.0
          discou = 0.0
          total = 0.0
          for child in purch_tree.get_children():
            total += float(purch_tree.item(child, 'values')[8])
          extracs = (extracs+float(pcost.get()))
          cost.config(text=pcost.get())
          discou = (total*float(pdisc.get())/100)
          discount1.config(text=discou)
          pordpriceview.config(text=total)
          sub1.config(text=total-discou)
            
          tot = 0.0
          totaltax1 = 0.0
          for child in purch_tree.get_children():
            checktax1 = list(purch_tree.item(child, 'values'))
            if checktax1[6] == "yes":
              totaltax1 =(totaltax1 + float(checktax1[8]))
              summery_tax1.config(text=(float(totaltax1)*float(porder_tax4.get())/100))
              tot = (float(totaltax1)*float(porder_tax4.get())/100)
            else:
              pass
          
          tot2 = 0.0
          totaltax2 = 0.0
          for child in purch_tree.get_children():
            checktax1 = list(purch_tree.item(child, 'values'))
            if checktax1[7] == "yes":
              totaltax2 =(totaltax2 + float(checktax1[8]))
              summery_tax2.config(text=(float(totaltax2)*float(porder_tax5.get())/100))
              
              tot2 = (float(totaltax2)*float(porder_tax5.get())/100)
            else:
              pass

          order1.config(text=total+tot+tot2-discou+extracs)
          
        #estimate_newselection.destroy()
      except:
        pass

    #finalize
    def finalize():  
      for x in (create, add, dele, finalize):
        x.config(state = 'disabled')
      for y in(vender_combo,pmail,pdel,psms,pdate,pdue,pextra,pcost,pdisc,porder_tax4,porder_tax5):
        y.config(state = 'disabled')
      for z in (paddress,pdel_addr):
        z.config(state = 'disabled')
      draft.config(text="Completed")
    def calcu():
      subprocess.Popen('C:\\Windows\\System32\\calc.exe')

    firFrame1=Frame(pop1, bg="#f5f3f2", height=60)
    firFrame1.pack(side="top", fill=X)

    w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    create = Button(firFrame1,compound="top", text="Select\nVendor",relief=RAISED, image=customer,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=purch_sele_customer)
    create.pack(side="left", pady=3, ipadx=4)


    w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    add= Button(firFrame1,compound="top", text="Add new\nline item",relief=RAISED, image=photo,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=newlineproduct)
    add.pack(side="left", pady=3, ipadx=4)

    dele= Button(firFrame1,compound="top", text="Delete line\nitem",relief=RAISED, image=photo2,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=deletepurch)
    dele.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    prev= Button(firFrame1,compound="top", text="Preview\nP.Order",relief=RAISED, image=photo4,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=prev_pord)
    prev.pack(side="left", pady=3, ipadx=4)

    prin= Button(firFrame1,compound="top", text="Print \nP.Order",relief=RAISED, image=photo5,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=printsele1)
    prin.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    mail= Button(firFrame1,compound="top", text="Email\nP.Order",relief=RAISED, image=photo6,bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
    mail.pack(side="left", pady=3, ipadx=4)

    sms1= Button(firFrame1,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=smspurch)
    sms1.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    finalize= Button(firFrame1,compound="top", text="Finalize\nP.Order",relief=RAISED, image=mark1,bg="#f5f3f2", fg="red", height=55, bd=1, width=55,command=finalize)
    finalize.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)


    calc= Button(firFrame1,compound="top", text="Open\nCalculator",relief=RAISED, image=photo9,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=calcu)
    calc.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="right", padx=5)

    Createorder= Button(firFrame1,compound="top", text="Save",relief=RAISED, image=tick,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=add_new_porder)
    Createorder.pack(side="right", pady=3, ipadx=4)

    fir1Frame=Frame(pop1, height=180,bg="#f5f3f2")
    fir1Frame.pack(side="top", fill=X)

    

    labelframe1 = LabelFrame(fir1Frame,text=" Vendor")
    labelframe1.place(x=10,y=5,width=640,height=160)

    def purch_to_combo(event):
      purch_to_str = purch_to.get()
      sql = "SELECT * FROM Customer WHERE businessname=%s"
      val = (purch_to_str,)
      fbcursor.execute(sql,val)
      purch_sel_combo = fbcursor.fetchone()
      print(purch_sel_combo)
      paddress.delete('1.0',END)
      paddress.insert('1.0',purch_sel_combo[5])
      pmail.delete(0,END)
      pmail.insert(0,purch_sel_combo[9])
      psms.delete(0,END)
      psms.insert(0,purch_sel_combo[12])
      sql = "select * from company"
      fbcursor.execute(sql)
      delata = fbcursor.fetchone()
      pdel.delete(0, END)
      pdel.insert(0, delata[1])
      pdel_addr.delete('1.0',END)
      pdel_addr.insert('1.0',delata[2])
      
    sql = "select businessname from Customer"
    fbcursor.execute(sql,)
    pdata = fbcursor.fetchall()

    porder = Label(labelframe1, text="Vendor to").place(x=10,y=5)
    purch_to = StringVar()
    vender_combo = ttk.Combobox(labelframe1, value="Hello",width=28,textvariable=purch_to)
    vender_combo.place(x=80,y=5)
    vender_combo['values'] = pdata
    vender_combo.bind("<<ComboboxSelected>>", purch_to_combo)
    address=Label(labelframe1,text="Address").place(x=10,y=30)
    paddress=Text(labelframe1,width=23)
    paddress.place(x=80,y=30,height=70)
    ship=Label(labelframe1,text="Delivery to").place(x=340,y=5)
    pdel=Entry(labelframe1,width=30)
    pdel.place(x=402,y=3)
    address1=Label(labelframe1,text="Address").place(x=340,y=30)
    # )pdel_addr=Entry(labelframe1)
    # pdel.place(x=408,y=30
    pdel_addr=Text(labelframe1,width=23)
    pdel_addr.place(x=402,y=30,height=70)
    
    labelframe2 = LabelFrame(fir1Frame,text="")
    labelframe2.place(x=10,y=130,width=640,height=42)
    email=Label(labelframe2,text="Email").place(x=10,y=5)
    pmail=Entry(labelframe2,width=30)
    pmail.place(x=80,y=5)

    sms=Label(labelframe2,text="SMS Number").place(x=327,y=5)
    psms=Entry(labelframe2,width=30)
    psms.place(x=402,y=5)

    labelframe = LabelFrame(fir1Frame,text="Purchase Order")
    labelframe.place(x=652,y=5,width=290,height=170)
    porder=Label(labelframe,text="P.Order#").place(x=5,y=5)
    porder_id_entry=Entry(labelframe,width=27)
    porder_id_entry.place(x=100,y=5) 
    porder_id_entry.delete(0,'end')    

    def pord_num_increment(inum):
      result = ""
      numberStr = ""
      i = len(inum) - 1
      while i > 0:
        c = inum[i]
        if not c.isdigit():
          break
        numberStr = c + numberStr
        i -= 1
      number = int(numberStr)
      number += 1
      result += inum[0 : i + 1]
      result += "000" if number < 10 else ""
      result += str(number)
      return result
    
    fbcursor.execute("SELECT * FROM porder ORDER BY porderid DESC LIMIT 1")
    pord_number_data = fbcursor.fetchone()
    
    if not pord_number_data == None:
      a = pord_number_data[39]
      print(a)
      pord_no = pord_num_increment(a)
    else:
      pord_no = 1
    porder_id_entry.insert(0,pord_no)

 
        
    porderdate=Label(labelframe,text="P.Order date").place(x=5,y=33)
    pdate=DateEntry(labelframe,width=20,date_pattern='dd.mm.yyyy')
    pdate.place(x=150,y=33)

    def porder_due_check():
      if checkvarStatus5.get() == 0:
        pdue['state'] = DISABLED
      else:
        pdue['state'] = NORMAL

    checkvarStatus5=IntVar()
    duedate=Checkbutton(labelframe,variable = checkvarStatus5,text="P.Due date",onvalue =0 ,offvalue = 1,command=porder_due_check).place(x=5,y=62)

    pdue=DateEntry(labelframe,width=20)
    pdue.place(x=150,y=62)


    terms=Label(labelframe,text="Terms").place(x=5,y=92)
    e4=ttk.Combobox(labelframe, value="",width=25)
    e4.place(x=100,y=92)
    ref=Label(labelframe,text="Order ref#").place(x=5,y=118)
    pref=Entry(labelframe,width=27)
    pref.place(x=100,y=118)

    fir2Frame=Frame(pop1, height=150,width=100,bg="#f5f3f2")
    fir2Frame.pack(side="top", fill=X)
    listFrame = Frame(fir2Frame, bg="white", height=140,borderwidth=5,  relief=RIDGE)
    
    sql = "select * from company"
    fbcursor.execute(sql)
    ptaxdata = fbcursor.fetchone()
    if not ptaxdata:
        #global purch_tree
      purch_tree=ttk.Treeview(listFrame)
      purch_tree["columns"]=["1","2","3","4","5","6","7"]

      purch_tree.column("#0", width=40)
      purch_tree.column("1", width=80)
      purch_tree.column("2", width=190)
      purch_tree.column("3", width=190)
      purch_tree.column("4", width=80)
      purch_tree.column("5", width=60)
      purch_tree.column("6", width=60)
      purch_tree.column("7", width=60)
        #purch_tree.column("8", width=80)
        
      purch_tree.heading("#0")
      purch_tree.heading("1",text="ID/SKU")
      purch_tree.heading("2",text="Product/Service")
      purch_tree.heading("3",text="Description")
      purch_tree.heading("4",text="Unit Price")
      purch_tree.heading("5",text="Quantity")
      purch_tree.heading("6",text="Pcs/Weight")
        # purch_tree.heading("7",text="Tax1")
      purch_tree.heading("7",text="Price")

      purch_tree.pack(fill="both", expand=1)
      listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

    elif ptaxdata[12] == "1":
      purch_tree=ttk.Treeview(listFrame)
      purch_tree["columns"]=["1","2","3","4","5","6","7"]

      purch_tree.column("#0", width=40)
      purch_tree.column("1", width=80)
      purch_tree.column("2", width=190)
      purch_tree.column("3", width=190)
      purch_tree.column("4", width=80)
      purch_tree.column("5", width=60)
      purch_tree.column("6", width=60)
      purch_tree.column("7", width=60)
        #purch_tree.column("8", width=80)
        
      purch_tree.heading("#0")
      purch_tree.heading("1",text="ID/SKU")
      purch_tree.heading("2",text="Product/Service")
      purch_tree.heading("3",text="Description")
      purch_tree.heading("4",text="Unit Price")
      purch_tree.heading("5",text="Quantity")
      purch_tree.heading("6",text="Pcs/Weight")
        # purch_tree.heading("7",text="Tax1")
      purch_tree.heading("7",text="Price")

      purch_tree.pack(fill="both", expand=1)
      listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

    elif ptaxdata[12] == "2":
      purch_tree=ttk.Treeview(listFrame)
      purch_tree["columns"]=["1","2","3","4","5","6","7","8"]

      purch_tree.column("#0", width=40)
      purch_tree.column("1", width=80)
      purch_tree.column("2", width=190)
      purch_tree.column("3", width=190)
      purch_tree.column("4", width=80)
      purch_tree.column("5", width=60)
      purch_tree.column("6", width=60)
      purch_tree.column("7", width=60)
      purch_tree.column("8", width=80)
        
      purch_tree.heading("#0")
      purch_tree.heading("1",text="ID/SKU")
      purch_tree.heading("2",text="Product/Service")
      purch_tree.heading("3",text="Description")
      purch_tree.heading("4",text="Unit Price")
      purch_tree.heading("5",text="Quantity")
      purch_tree.heading("6",text="Pcs/Weight")
      purch_tree.heading("7",text="Tax1")
      purch_tree.heading("8",text="Price")

      purch_tree.pack(fill="both", expand=1)
      listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

    elif ptaxdata[12] == "3":
      purch_tree=ttk.Treeview(listFrame)
      purch_tree["columns"]=["1","2","3","4","5","6","7","8","9"]

      purch_tree.column("#0", width=40)
      purch_tree.column("1", width=80)
      purch_tree.column("2", width=190)
      purch_tree.column("3", width=190)
      purch_tree.column("4", width=80)
      purch_tree.column("5", width=60)
      purch_tree.column("6", width=60)
      purch_tree.column("7", width=60)
      purch_tree.column("8", width=60)
      purch_tree.column("9", width=80)
        
      purch_tree.heading("#0")
      purch_tree.heading("1",text="ID/SKU")
      purch_tree.heading("2",text="Product/Service")
      purch_tree.heading("3",text="Description")
      purch_tree.heading("4",text="Unit Price")
      purch_tree.heading("5",text="Quantity")
      purch_tree.heading("6",text="Pcs/Weight")
      purch_tree.heading("7",text="Tax1")
      purch_tree.heading("8",text="Tax2")
      purch_tree.heading("9",text="Price")
      
      purch_tree.pack(fill="both", expand=1)
      listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

    fir3Frame=Frame(pop1,height=200,width=700,bg="#f5f3f2")
    fir3Frame.place(x=0,y=490)

    tabStyle = ttk.Style()
    tabStyle.theme_use('default')
    tabStyle.configure('TNotebook.Tab', background="#999999", width=12, padding=5)
    myNotebook=ttk.Notebook(fir3Frame)
    orderFrame = Frame(myNotebook, height=200, width=800)
    headerFrame = Frame(myNotebook, height=200, width=800)
    commentFrame = Frame(myNotebook, height=200, width=800)
    termsFrame = Frame(myNotebook, height=200, width=800)
    noteFrame = Frame(myNotebook, height=200, width=800)
    documentFrame = Frame(myNotebook, height=200, width=800)
    
    myNotebook.add(orderFrame,compound="left", text="Purchase Order")
    myNotebook.add(headerFrame,compound="left",  text="Header/Footer")
    myNotebook.add(commentFrame,compound="left",  text="Comments")
    myNotebook.add(termsFrame,compound="left", text="Terms")
    myNotebook.add(noteFrame,compound="left",  text="Private notes")
    myNotebook.add(documentFrame,compound="left",  text="Documents")
    myNotebook.pack(expand = 1, fill ="both")

    # def est_recalc_exc(event):
    #   sql = "select * from company"
    #   fbcursor.execute(sql)
    #   taxdata1 = fbcursor.fetchone()
    #   if taxdata1[12] == "1":
    #     price = 0.0
    #     total_cost = 0.0
    #     exc = float(pcost.get())
    #     dis_rate = float(pdisc.get())
    #     for i in purch_tree.get_children():
    #       price += float(purch_tree.item(i,'values')[3])
    #     discount_rate = (price*dis_rate)/100
    #     total_cost += (price - discount_rate) + exc
    #     discount.config(text= str(dis_rate) + "" +"% Discount")
    #     # estimate_totalpaid1.config(text="" +"0.00")
    #     tax1.config(text="" +"0.00")
    #     tax2.config(text="" +"0.00")
    #     discount1.config(text=round(discount_rate,2))
    #     sub_tot = round((price - discount_rate),2)
    #     sub1.config(text=sub_tot)
    #     cost.config(text=round(exc,2))
    #     order1.config(text=round(total_cost,2))
        
    #   elif taxdata1[12] == "2":
    #     price = 0.0
    #     p = 0.0
    #     total_cost = 0.0
    #     exc = float(pcost.get())
    #     dis_rate = float(pdisc.get())
    #     tx1 = float(porder_tax4.get())
    #     for i in purch_tree.get_children():
    #       if purch_tree.item(i,'values')[6] == "No":
    #         p += float(purch_tree.item(i,'values')[3])
    #       else:
    #         price += float(purch_tree.item(i,'values')[3])
    #     discount_rate = ((price + p) * dis_rate)/100
    #     dis_price = (price * dis_rate)/100
    #     dis_p = (p * dis_rate)/100
    #     tax1_rate = ((price - dis_price)*tx1)/100
    #     tx_calc = (price - dis_price) + tax1_rate
    #     tx_calc1 = p - dis_p
    #     total_cost += (tx_calc + tx_calc1) + exc 
    #     discount.config(text= str(dis_rate) + "" +"% Discount")
    #     # estimate_totalpaid1.config(text="" +"0.00")
    #     tax2.config(text="" +"0.00")
    #     discount1.config(text=round(discount_rate,2))
    #     sub_tot = round(((price + p) - discount_rate),2)
    #     sub1.config(text=sub_tot)
    #     tax1.config(text=round(tax1_rate,2))
    #     cost.config(text=round(exc,2))
    #     order1.config(text=round(total_cost,2))
        
    #   elif taxdata1[12] == "3":
    #     price = 0.0
    #     p1 = 0.0
    #     p2 = 0.0
    #     p3 = 0.0
    #     total_cost = 0.0
    #     tx1 = float(porder_tax4.get())
    #     tx2 = float(porder_tax5.get())
    #     exc = float(pcost.get())
    #     dis_rate = float(pdisc.get())
    #     for i in purch_tree.get_children():
    #       if purch_tree.item(i,'values')[6] == "No" and purch_tree.item(i,'values')[7] == "No":
    #         p1 += float(purch_tree.item(i,'values')[3])
    #       elif purch_tree.item(i,'values')[6] == "Yes" and purch_tree.item(i,'values')[7] == "No":
    #         p2 += float(purch_tree.item(i,'values')[3])
    #       elif purch_tree.item(i,'values')[6] == "No" and purch_tree.item(i,'values')[7] == "Yes":
    #         p3 += float(purch_tree.item(i,'values')[3])
    #       else:
    #         price += float(purch_tree.item(i,'values')[3])
    #     discount_rate = ((p1 + p2 + p3 + price) * dis_rate)/100
    #     dis_p2 = (p2 * dis_rate)/100
    #     tax1_rate = ((p2 - dis_p2) * tx1)/100
    #     dis_price = (price * dis_rate)/100
    #     tax2_rate = ((price - dis_price) * tx1)/100
    #     tax3_rate = ((price - dis_price) * tx2)/100
    #     dis_p3= (p3 * dis_rate)/100
    #     tax4_rate = ((p3 - dis_p3) * tx2)/100
    #     dis_p4 = (p1 * dis_rate)/100
    #     tx_calc1 = (p2 - dis_p2) + tax1_rate
    #     tx_calc2 = (price - dis_price) + tax2_rate + tax3_rate
    #     tx_calc3 = (p3 - dis_p3) + tax4_rate
    #     tx_calc4 = (p1 - dis_p4)
    #     total_cost += (tx_calc1 + tx_calc2 + tx_calc3 + tx_calc4) + exc
    #     discount.config(text= str(dis_rate) + "" +"% Discount")
    #     # estimate_totalpaid1.config(text="" +"0.00")
    #     discount1.config(text=round(discount_rate,2))
    #     sub_tot = round(((price + p1 + p2 + p3) - discount_rate),2)
    #     sub1.config(text="$" + "" + str(sub_tot))
    #     tax1.config(text=round((tax1_rate + tax2_rate),2))
    #     tax2.config(text=round((tax3_rate + tax4_rate),2))
    #     cost.config(text=round(exc,2))
    def pord_recalc_exc(event):
      sql = "select * from company"
      fbcursor.execute(sql)
      taxdata1 = fbcursor.fetchone()
      if taxdata1[12] == "1":
        price = 0.0
        total_cost = 0.0
        exc = float(pcost.get())
        dis_rate = float(pdisc.get())
        for i in purch_tree.get_children():
          price += float(purch_tree.item(i,'values')[3])
        discount_rate = (price*dis_rate)/100
        total_cost += (price - discount_rate) + exc
        discount.config(text= str(dis_rate) + "" +"% Discount")
        # estimate_totalpaid1.config(text="" +"0.00")
        summery_tax1.config(text="" +"0.00")
        summery_tax2.config(text="" +"0.00")
        discount1.config(text=round(discount_rate,2))
        sub_tot = round((price - discount_rate),2)
        sub1.config(text=sub_tot)
        cost.config(text=round(exc,2))
        order1.config(text=round(total_cost,2))
        
      elif taxdata1[12] == "2":
        price = 0.0
        p = 0.0
        total_cost = 0.0
        exc = float(pcost.get())
        dis_rate = float(pdisc.get())
        tx1 = float(porder_tax4.get())
        for i in purch_tree.get_children():
          if purch_tree.item(i,'values')[6] == "No":
            p += float(purch_tree.item(i,'values')[3])
          else:
            price += float(purch_tree.item(i,'values')[3])
        discount_rate = ((price + p) * dis_rate)/100
        dis_price = (price * dis_rate)/100
        dis_p = (p * dis_rate)/100
        tax1_rate = ((price - dis_price)*tx1)/100
        tx_calc = (price - dis_price) + tax1_rate
        tx_calc1 = p - dis_p
        total_cost += (tx_calc + tx_calc1) + exc 
        discount.config(text= str(dis_rate) + "" +"% Discount")
        # estimate_totalpaid1.config(text="" +"0.00")
        tax2.config(text="" +"0.00")
        discount1.config(text=round(discount_rate,2))
        sub_tot = round(((price + p) - discount_rate),2)
        sub1.config(text=sub_tot)
        summery_tax1.config(text=round(tax1_rate,2))
        cost.config(text=round(exc,2))
        order1.config(text=round(total_cost,2))
        
      elif taxdata1[12] == "3":
        price = 0.0
        p1 = 0.0
        p2 = 0.0
        p3 = 0.0
        total_cost = 0.0
        tx1 = float(porder_tax4.get())
        tx2 = float(porder_tax5.get())
        exc = float(pcost.get())
        dis_rate = float(pdisc.get())
        for i in purch_tree.get_children():
          if purch_tree.item(i,'values')[6] == "No" and purch_tree.item(i,'values')[7] == "No":
            p1 += float(purch_tree.item(i,'values')[3])
          elif purch_tree.item(i,'values')[6] == "Yes" and purch_tree.item(i,'values')[7] == "No":
            p2 += float(purch_tree.item(i,'values')[3])
          elif purch_tree.item(i,'values')[6] == "No" and purch_tree.item(i,'values')[7] == "Yes":
            p3 += float(purch_tree.item(i,'values')[3])
          else:
            price += float(purch_tree.item(i,'values')[3])
        discount_rate = ((p1 + p2 + p3 + price) * dis_rate)/100
        dis_p2 = (p2 * dis_rate)/100
        tax1_rate = ((p2 - dis_p2) * tx1)/100
        dis_price = (price * dis_rate)/100
        tax2_rate = ((price - dis_price) * tx1)/100
        tax3_rate = ((price - dis_price) * tx2)/100
        dis_p3= (p3 * dis_rate)/100
        tax4_rate = ((p3 - dis_p3) * tx2)/100
        dis_p4 = (p1 * dis_rate)/100
        tx_calc1 = (p2 - dis_p2) + tax1_rate
        tx_calc2 = (price - dis_price) + tax2_rate + tax3_rate
        tx_calc3 = (p3 - dis_p3) + tax4_rate
        tx_calc4 = (p1 - dis_p4)
        total_cost += (tx_calc1 + tx_calc2 + tx_calc3 + tx_calc4) + exc
        discount.config(text= str(dis_rate) + "" +"% Discount")
        # estimate_totalpaid1.config(text="" +"0.00")
        discount1.config(text=round(discount_rate,2))
        sub_tot = round(((price + p1 + p2 + p3) - discount_rate),2)
        sub1.config(text="$" + "" + str(sub_tot))
        summery_tax1.config(text=round((tax1_rate + tax2_rate),2))
        summery_tax2.config(text=round((tax3_rate + tax4_rate),2))
        cost.config(text=round(exc,2))
        order1.config(text=round(total_cost,2))  
  
    def pexta_selected(event):
      psel = etracost.get()
      print(psel)
      if psel == "Shipping and handling":
        ecost=Label(summaryfrme, text="Shipping and handling")
        ecost.place(x=0 ,y=84)
      elif psel == "Postage and handling":
        ecost=Label(summaryfrme, text="Postage and handling ")
        ecost.place(x=0 ,y=84)
      elif psel == "Delivery cost":
        ecost=Label(summaryfrme, text="Delivery cost               ")
        ecost.place(x=0 ,y=84)


    labelframe1 = LabelFrame(orderFrame,text="",font=("arial",15))
    labelframe1.place(x=1,y=1,width=800,height=170)
    cost1=Label(labelframe1,text="Extra cost name").place(x=2,y=5)
    etracost = StringVar()
    pextra=ttk.Combobox(labelframe1,width=20,textvariable=etracost)
    pextra['values'] = ('Shipping and handling','Postage and handling','Delivery cost')
    pextra.bind("<<ComboboxSelected>>",pexta_selected)
    pextra.place(x=115,y=5)
    

    

    def pord_recalc_dis(event):
      sql = "select * from company"
      fbcursor.execute(sql)
      taxdata1 = fbcursor.fetchone()
      if taxdata1[12] == "1":
        price = 0.0
        total_cost = 0.0
        exc = float(pcost.get())
        dis_rate = float(pdisc.get())
        for i in purch_tree.get_children():
          price += float(purch_tree.item(i,'values')[3])
        discount_rate = (price*dis_rate)/100
        total_cost += (price - discount_rate) + exc
        discount.config(text= str(dis_rate) + "" +"% Discount")
        # estimate_totalpaid1.config(text="" +"0.00")
        summery_tax1.config(text="" +"0.00")
        summery_tax2.config(text="" +"0.00")
        discount1.config(text=round(discount_rate,2))
        sub_tot = round((price - discount_rate),2)
        sub1.config(text=sub_tot)
        cost.config(text=round(exc,2))
        order1.config(text=round(total_cost,2))
        
      elif taxdata1[12] == "2":
        price = 0.0
        p = 0.0
        total_cost = 0.0
        exc = float(pcost.get())
        dis_rate = float(pdisc.get())
        tx1 = float(porder_tax4.get())
        for i in purch_tree.get_children():
          if purch_tree.item(i,'values')[6] == "No":
            p += float(purch_tree.item(i,'values')[3])
          else:
            price += float(purch_tree.item(i,'values')[3])
        discount_rate = ((price + p) * dis_rate)/100
        dis_price = (price * dis_rate)/100
        dis_p = (p * dis_rate)/100
        tax1_rate = ((price - dis_price)*tx1)/100
        tx_calc = (price - dis_price) + tax1_rate
        tx_calc1 = p - dis_p
        total_cost += (tx_calc + tx_calc1) + exc 
        discount.config(text= str(dis_rate) + "" +"% Discount")
        # estimate_totalpaid1.config(text="" +"0.00")
        tax2.config(text="" +"0.00")
        discount1.config(text=round(discount_rate,2))
        sub_tot = round(((price + p) - discount_rate),2)
        sub1.config(text=sub_tot)
        summery_tax1.config(text=round(tax1_rate,2))
        cost.config(text=round(exc,2))
        order1.config(text=round(total_cost,2))
        
      elif taxdata1[12] == "3":
        price = 0.0
        p1 = 0.0
        p2 = 0.0
        p3 = 0.0
        total_cost = 0.0
        tx1 = float(porder_tax4.get())
        tx2 = float(porder_tax5.get())
        exc = float(pcost.get())
        dis_rate = float(pdisc.get())
        for i in purch_tree.get_children():
          if purch_tree.item(i,'values')[6] == "No" and purch_tree.item(i,'values')[7] == "No":
            p1 += float(purch_tree.item(i,'values')[3])
          elif purch_tree.item(i,'values')[6] == "Yes" and purch_tree.item(i,'values')[7] == "No":
            p2 += float(purch_tree.item(i,'values')[3])
          elif purch_tree.item(i,'values')[6] == "No" and purch_tree.item(i,'values')[7] == "Yes":
            p3 += float(purch_tree.item(i,'values')[3])
          else:
            price += float(purch_tree.item(i,'values')[3])
        discount_rate = ((p1 + p2 + p3 + price) * dis_rate)/100
        dis_p2 = (p2 * dis_rate)/100
        tax1_rate = ((p2 - dis_p2) * tx1)/100
        dis_price = (price * dis_rate)/100
        tax2_rate = ((price - dis_price) * tx1)/100
        tax3_rate = ((price - dis_price) * tx2)/100
        dis_p3= (p3 * dis_rate)/100
        tax4_rate = ((p3 - dis_p3) * tx2)/100
        dis_p4 = (p1 * dis_rate)/100
        tx_calc1 = (p2 - dis_p2) + tax1_rate
        tx_calc2 = (price - dis_price) + tax2_rate + tax3_rate
        tx_calc3 = (p3 - dis_p3) + tax4_rate
        tx_calc4 = (p1 - dis_p4)
        total_cost += (tx_calc1 + tx_calc2 + tx_calc3 + tx_calc4) + exc
        discount.config(text= str(dis_rate) + "" +"% Discount")
        # estimate_totalpaid1.config(text="" +"0.00")
        discount1.config(text=round(discount_rate,2))
        sub_tot = round(((price + p1 + p2 + p3) - discount_rate),2)
        sub1.config(text="$" + "" + str(sub_tot))
        summery_tax1.config(text=round((tax1_rate + tax2_rate),2))
        summery_tax2.config(text=round((tax3_rate + tax4_rate),2))
        cost.config(text=round(exc,2))
        order1.config(text=round(total_cost,2))  

    rate=Label(labelframe1,text="Discount rate").place(x=370,y=5)
    pdisc=Spinbox(labelframe1,width=6,from_=0,to=100,justify=RIGHT)
    pdisc.place(x=460,y=5)
    pdisc.bind('<Button-1>',pord_recalc_dis)
    cost2=Label(labelframe1,text="Extra cost").place(x=35,y=35)
    pcost=Entry(labelframe1,width=10)
    pcost.place(x=115,y=35)
    pcost.bind('<KeyRelease>',pord_recalc_exc)
    pcost.delete(0,END)
    pcost.insert(0,"0")
    pord_comp_sql = "SELECT * FROM company"
    fbcursor.execute(pord_comp_sql,)
    pptaxdata1 = fbcursor.fetchone()
    porder_tax=Label(labelframe1,text="Tax1")
    porder_tax4=Entry(labelframe1,width=7,justify=RIGHT)
    porder_taax5=Label(labelframe1,text="Tax2")
    porder_tax5=Entry(labelframe1,width=7,justify=RIGHT)
    if pptaxdata1[12] == "1":
      porder_tax4.insert(0, 0)
      porder_tax5.insert(0, 0)
    elif pptaxdata1[12] == "2":
        
      porder_tax.place(x=420,y=35)
        
      porder_tax4.place(x=460,y=35)
      def1_val = tax1ratee.get()
      porder_tax4.delete(0, END)
      porder_tax4.insert(0, def1_val)
      porder_tax5.insert(0, 0)
    elif pptaxdata1[12] == "3":
        
      porder_tax.place(x=420,y=35)
        
      porder_tax4.place(x=460,y=35)
      def1_val = tax1ratee.get()
      porder_tax4.delete(0, END)
      porder_tax4.insert(0, def1_val)
        
      porder_taax5.place(x=420,y=65)
        
      porder_tax5.place(x=460,y=65)
      def2_val = tax2ratee.get()
      porder_tax5.delete(0, END)
      porder_tax5.insert(0, def2_val)
    # template=Label(labelframe1,text="Template").place(x=37,y=70)
    # ptemp=ttk.Combobox(labelframe1, value="",width=25)
    # ptemp.place(x=115,y=70)
    sales=Label(labelframe1,text="Sales Person")
    sales.place(x=37,y=70)
    psale=Entry(labelframe1,width=18)
    psale.place(x=115,y=70)
    category=Label(labelframe1,text="Category").place(x=25,y=100)
    pact=Entry(labelframe1,width=22)
    pact.place(x=115,y=100)

    statusfrme = LabelFrame(labelframe1,text="Status",font=("arial",15))
    statusfrme.place(x=540,y=0,width=160,height=160)
    draft=Label(statusfrme, text="Draft",font=("arial", 15, "bold"), fg="grey")
    draft.place(x=35, y=3)
    on1=Label(statusfrme, text="Emailed on:").place( y=50)
    nev1=Label(statusfrme, text="Never")
    nev1.place(x=100,y=50)
    on2=Label(statusfrme, text="Printed on:").place( y=90)
    nev2=Label(statusfrme, text="Never")
    nev2.place(x=100,y=90)

    text1=Label(headerFrame,text="Title text").place(x=50,y=5)
    e1=ttk.Combobox(headerFrame, value="",width=60)
    e1['values']=('Thank you for your purchase!','Thank you for buying!','Thank you for your businnes!','Thank you for your order!')
    e1.place(x=125,y=5)
    text2=Label(headerFrame,text="Page header text").place(x=2,y=45)
    e11=ttk.Combobox(headerFrame, value="",width=60)
    e11['values']=('Thank you for your purchase!','Thank you for buying!','Thank you for your businnes!','Thank you for your order!')
    e11.place(x=125,y=45)

    text3=Label(headerFrame,text="Footer text").place(x=35,y=85)
    e12=ttk.Combobox(headerFrame, value="",width=60)
    e12['values']=('Thank you for your purchase!','Thank you for buying!','Thank you for your businnes!','Thank you for your order!')
    e12.place(x=125,y=85)


    sql = "select * from porder"
    fbcursor.execute(sql)
    purchdata = fbcursor.fetchone()

    text=Label(noteFrame,text="Private notes(not shown on invoice/order/estemates)").place(x=10,y=10)
    pvt=Text(noteFrame,width=100,height=7)
    pvt.place(x=10,y=32)

    # pvt =scrolledtext.ScrolledText(noteFrame,width=50,height=4)
    # pvt.place(x=32,y=358)


    e13=scrolledtext.ScrolledText(termsFrame,width=100,height=9)
    e13.place(x=10,y=10)

    e14=scrolledtext.ScrolledText(commentFrame,width=100,height=9)
    e14.place(x=10,y=10)


    

    def attach_file():
      global file,file_type
      file_type = [('png files','.png'),('jpg files','.jpg'),('PDF', '.pdf',),('all files','.')]
      file = filedialog.askopenfilename(initialdir="/",filetypes=file_type)
      shutil.copyfile(file, os.getcwd()+'/images/'+file.split('/')[-1])
      file_size = convertion(os.path.getsize(file))
      purchase_doc_cusventtree.insert(parent='',index='end',iid=file.split('/')[-1],text='',values=('',file.split('/')[-1],file_size))
      

    #################### size convertion of files############################
    def convertion(B):
      BYTE = float(B)
      KB = float(1024)
      MB = float(KB**2)

      if BYTE < KB:
        return '{0} {1}'.format(BYTE,'Bytes' if 0 == B > 1 else 'Byte')
      elif KB <= BYTE < MB:
        return '{0:.2f} KB'.format(BYTE / KB)
      elif MB <= BYTE:
        return '{0:.2f} MB'.format(BYTE / MB)
    ############### delete file #################
    def delete_file():
      selected_doc_item = purchase_doc_cusventtree.selection()[0]
      purchase_doc_cusventtree.delete(selected_doc_item)


    ############## show file ###############

    def show_sele_file(event):
      selected_file = purchase_doc_cusventtree.item(purchase_doc_cusventtree.focus())["values"][1]
      show = Toplevel()
      show.geometry("700x500")
      show.title("View Files")
      if selected_file.lower().endswith(('.png','.jpg')):
        open_image = Image.open("images/"+selected_file)
        resize_img = open_image.resize((700,500))
        img = ImageTk.PhotoImage(resize_img)
        image = Label(show,image=img)
        image.photo = img
        image.pack()
      else:
        with open("images/"+selected_file,mode='r',encoding="utf-8",errors="ignore") as none_img:
          data = none_img.read()
          image = Label(show,text=data)
          image.pack()


    btn1=Button(documentFrame,height=2,width=3,text="+",command=attach_file)
    btn1.place(x=5,y=10)
    btn2=Button(documentFrame,height=2,width=3,text="-",command=delete_file)
    btn2.place(x=5,y=50)
    text=Label(documentFrame,text="Attached documents or image files.If you attach large email then email taken long time to send").place(x=50,y=10)
    global purchase_doc_cusventtree
    purchase_doc_cusventtree=ttk.Treeview(documentFrame, height=5)
    purchase_doc_cusventtree["columns"]=["1","2","3"]
    purchase_doc_cusventtree.column("#0", width=20)
    purchase_doc_cusventtree.column("1", width=250)
    purchase_doc_cusventtree.column("2", width=250)
    purchase_doc_cusventtree.column("2", width=200)
    purchase_doc_cusventtree.heading("#0",text="", anchor=W)
    purchase_doc_cusventtree.heading("1",text="Attach to Email")
    purchase_doc_cusventtree.heading("2",text="Filename")
    purchase_doc_cusventtree.heading("3",text="Filesize")  
    purchase_doc_cusventtree.place(x=50, y=45)
    purchase_doc_cusventtree.bind('<Double-Button-1>',show_sele_file)

    fir4Frame=Frame(pop1,height=190,width=210,bg="#f5f3f2")
    fir4Frame.place(x=740,y=520)
    summaryfrme = LabelFrame(fir4Frame,text="Summary",font=("arial",15))
    summaryfrme.place(x=0,y=0,width=200,height=170)
    discount=Label(summaryfrme,text="Discount")
    discount.place(x=0 ,y=0)
    discount1=Label(summaryfrme, text="$0.00")
    discount1.place(x=130 ,y=0)
    sub=Label(summaryfrme, text="Subtotal")
    sub.place(x=0 ,y=21)
    sub1=Label(summaryfrme, text="$0.00")
    sub1.place(x=130 ,y=21)
    tax=Label(summaryfrme, text="Tax1")
    tax.place(x=0 ,y=42)
    summery_tax1=Label(summaryfrme, text="$0.00")
    summery_tax1.place(x=130 ,y=42)
    taxx=Label(summaryfrme, text="Tax2")
    taxx.place(x=0 ,y=63)
    summery_tax2=Label(summaryfrme, text="$0.00")
    summery_tax2.place(x=130 ,y=63)
    ecost=Label(summaryfrme, text="Extra cost")
    ecost.place(x=0 ,y=84)
    cost=Label(summaryfrme, text="$0.00")
    cost.place(x=130 ,y=84)
    order=Label(summaryfrme, text="P.Order total")
    order.place(x=0 ,y=105)
    order1=Label(summaryfrme, text="$0.00")
    order1.place(x=130 ,y=105)

    fir5Frame=Frame(pop1,height=38,width=210)
    fir5Frame.place(x=735,y=485)
    btndown=Button(fir5Frame, compound="left", text="Line Down").place(x=75, y=0)
    btnup=Button(fir5Frame, compound="left", text="Line Up").place(x=150, y=0)

    # sql3='UPDATE porder SET  porder_no=%s, duedate=%s, businessname=%s, extracostname=%s, extracost=%s, template=%s, salesper=%s,discourate=%s, tax1=%s, tax2=%s,category=%s, deliveryto=%s,deliveryaddress=%s, cpemail=%s, cpmobileforsms=%s,title_text=%s,header_text=%s,footer_text=%s,term_of_payment=%s,terms=%s,comments=%s,privatenote=%s,ordertot=%s,sumdiscount=%s,sumtax1=%s,sumtax2=%s,sumsubtotal=%s WHERE porder_no=%s'
    # val2=(porderdate,duedate,status,emailon,printon,pordtot,extracostname,extracost, salesper,discourate,tax1,tax2, category,businessname,businessaddress,delname, deladdress,cpemail,cpmobileforsms,title_text, header_text, footer_text,term_of_payment,terms,comments,pvt,sum_dis,subtotal,sum_tax1,sum_tax2,sub1,porderid)
    # fbcursor.execute(sql3,val2,)
    # fbilldb.commit()
    # sql5='SELECT * FROM porder WHERE porder_no=%s'
    # val5=(porderid,)
    # fbcursor.execute(sql5,val5,)
    # new=fbcursor.fetchone()
    # # print(new)
    # if new[5]=="Completed":
    #   pass
    # else:
    #   sql6='UPDATE porder SET status=%s WHERE porderid=%s'
    #   val6=(ab,porder_no,)
    #   fbcursor.execute(sql6,val6,)
    #   fbilldb.commit()

  #######################END OF CREATE PORDER##############
  def purch_edit():
    # try:
    pop1=Toplevel(purch_midFrame)
    pop1.title("Porder")
    pop1.geometry("950x690+150+0")
    edit_purchase_tree_fetch = pord_tree.item(pord_tree.focus())["values"][0]
    sql="SELECT * FROM porder WHERE porderid=%s"
    val=(edit_purchase_tree_fetch,)
    fbcursor.execute(sql,val)
    global edit_pord_data
    edit_pord_data = fbcursor.fetchone()

    #select vendor
    def purch_sele_edit_customer():
      global purch_cuselection
      purch_cuselection=Toplevel()
      purch_cuselection.title("Select Customer")
      purch_cuselection.geometry("930x650+240+10")
      purch_cuselection.resizable(False, False)


      #add new customer
      def purch_edit_newcust():
        global checkvar1,checkvar2,custid,bname,baddress,cat,sname,saddress,contp,cemail,ctel,cfax,cmob,scontp,scemail,sctel,scfax,ccountry,ccity,cnotes
        ven=Toplevel(purch_midFrame)
        ven.title("Add new vendor")
        ven.geometry("930x650+240+10")
        checkvar1=IntVar()
        checkvar2=IntVar()
        radio=IntVar()
        createFrame=Frame(ven, bg="#f5f3f2", height=650)
        createFrame.pack(side="top", fill="both")
        labelframe1 = LabelFrame(createFrame,text="Customer",bg="#f5f3f2",font=("arial",15))
        labelframe1.place(x=10,y=5,width=910,height=600)

        fbcursor.execute("SELECT * FROM Customer ORDER BY customerid DESC LIMIT 1")
        query = fbcursor.fetchone()

        text1=Label(labelframe1, text="Customer ID:",bg="#f5f3f2",fg="blue").place(x=5 ,y=10)
        custid=Entry(labelframe1,width=25)
        custid.place(x=150,y=10)
        if not query== None:
          id00=query[0]+1
        else:
          id00=1
        custid.insert(0, id00)

        text2=Label(labelframe1, text="Category:",bg="#f5f3f2").place(x=390 ,y=10)
        cat=ttk.Combobox(labelframe1,width=25,value="Default")
        cat.place(x=460 ,y=10)

        text3=Label(labelframe1, text="Status:",bg="#f5f3f2").place(x=710 ,y=10)
        Checkbutton(labelframe1,text="Active",variable=checkvar1,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=760 ,y=10)
        labelframe2 = LabelFrame(labelframe1,text="Invoice to (appears on invoices)",bg="#f5f3f2")
        labelframe2.place(x=5,y=40,width=420,height=150)
        name = Label(labelframe2, text="Ship to name:",bg="#f5f3f2",fg="blue").place(x=5,y=5)
        sname = Entry(labelframe2,width=28)
        sname.place(x=130,y=5)

        addr = Label(labelframe2, text="Address:",bg="#f5f3f2",fg="blue").place(x=5,y=40)
        saddress = Entry(labelframe2,width=28)
        saddress.place(x=130,y=40,height=80)

        def btncpy():
          tosp=sname.get()
          saddres=saddress.get()
          bname.delete(0, 'end')
          bname.insert(0, tosp)
          baddress.delete(0,'end')
          baddress.insert(0, saddres)

        btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>",command=btncpy).place(x=440, y=90)

        labelframe3 = LabelFrame(labelframe1,text="Ship to (appears on invoices)",bg="#f5f3f2")
        labelframe3.place(x=480,y=40,width=420,height=150)
        name = Label(labelframe3, text="Business name:",bg="#f5f3f2").place(x=5,y=5)
        bname = Entry(labelframe3,width=28)
        bname.place(x=130,y=5)

        addr = Label(labelframe3, text="Address:",bg="#f5f3f2").place(x=5,y=40)
        baddress = Entry(labelframe3,width=28)
        baddress.place(x=130,y=40,height=80)
        
        labelframe4 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
        labelframe4.place(x=5,y=195,width=420,height=150)
        name = Label(labelframe4, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
        contp = Entry(labelframe4,width=28)
        contp.place(x=130,y=5)

        email = Label(labelframe4, text="E-mail address:",bg="#f5f3f2",fg="blue").place(x=5,y=35)
        cemail = Entry(labelframe4,width=28)
        cemail.place(x=130,y=35)

        tel = Label(labelframe4, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
        ctel = Entry(labelframe4,width=11)
        ctel.place(x=130,y=65)

        fax = Label(labelframe4, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
        cfax = Entry(labelframe4,width=11)
        cfax.place(x=280,y=65)

        sms = Label(labelframe4, text="Mobile number for SMS notifications:",bg="#f5f3f2").place(x=5,y=95)
        cmob = Entry(labelframe4,width=15)
        cmob.place(x=248,y=95)   

        def btncpy1():
          cprsn1=contp.get()
          cemail1=cemail.get()
          no=ctel.get()
          fx=cfax.get()
          scontp.insert(0, cprsn1)
          scemail.insert(0, cemail1)
          sctel.insert(0, no)
          scfax.insert(0,fx)   

        btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>",command=btncpy1).place(x=440, y=250)

        labelframe5 = LabelFrame(labelframe1,text="Ship to contact",bg="#f5f3f2")
        labelframe5.place(x=480,y=195,width=420,height=125)
        name = Label(labelframe5, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
        scontp = Entry(labelframe5,width=28)
        scontp.place(x=130,y=5)

        email = Label(labelframe5, text="E-mail address:",bg="#f5f3f2").place(x=5,y=35)
        scemail = Entry(labelframe5,width=28)
        scemail.place(x=130,y=35)

        tel = Label(labelframe5, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
        sctel = Entry(labelframe5,width=11)
        sctel.place(x=130,y=65)

        fax = Label(labelframe5, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
        scfax = Entry(labelframe5,width=11)
        scfax.place(x=280,y=65)

        labelframe6 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
        labelframe6.place(x=5,y=350,width=420,height=100)
        Checkbutton(labelframe6,text="Tax Exempt",variable=checkvar2,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=5 ,y=5)
        tax = Label(labelframe6, text="Specific Tax1 %:",bg="#f5f3f2").place(x=180,y=5)
        e1tax = Entry(labelframe6,width=10)
        e1tax.place(x=290,y=5)

        discount = Label(labelframe6, text="Discount%:",bg="#f5f3f2").place(x=5,y=35)
        e2dsc = Entry(labelframe6,width=10)
        e2dsc.place(x=100,y=35)

        labelframe7 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2",)
        labelframe7.place(x=480,y=330,width=420,height=100)
        country = Label(labelframe7, text="country:",bg="#f5f3f2").place(x=5,y=5)
        ccountry = Entry(labelframe7,width=28)
        ccountry.place(x=130,y=5)

        city = Label(labelframe7, text="City:",bg="#f5f3f2").place(x=5,y=35)
        ccity = Entry(labelframe7,width=28)
        ccity.place(x=130,y=35)

        labelframe8 = LabelFrame(labelframe1,text="Customer Type",bg="#f5f3f2")
        labelframe8.place(x=5,y=460,width=420,height=100)
        R1=Radiobutton(labelframe8,text=" Client ",variable=radio,value=1,bg="#f5f3f2").place(x=5,y=15)
        R2=Radiobutton(labelframe8,text=" Vendor ",variable=radio,value=2,bg="#f5f3f2").place(x=150,y=15)
        R3=Radiobutton(labelframe8,text=" Both(client/vendor)",variable=radio,value=3,bg="#f5f3f2").place(x=250,y=15)
        

        labelframe9 = LabelFrame(labelframe1,text="Notes",bg="#f5f3f2")
        labelframe9.place(x=480,y=430,width=420,height=150)
        cnotes = Entry(labelframe9)
        cnotes.place(x=10,y=10,height=100,width=390)

        btn1=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=tick,text="OK",command=treefthcng1).place(x=20, y=615)
        btn2=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=cancel,text="Cancel",command=lambda:ven.destroy()).place(x=800, y=615)
          
                

      enter=Label(purch_cuselection, text="Enter filter text").place(x=5, y=10)
      e1=Entry(purch_cuselection, width=20).place(x=110, y=10)
      text=Label(purch_cuselection, text="Filtered column").place(x=340, y=10)
      e2=Entry(purch_cuselection, width=20).place(x=450, y=10)
      global purch_cusventtree
      purch_cusventtree=ttk.Treeview(purch_cuselection, height=27)
      purch_cusventtree["columns"]=["1","2","3", "4"]
      purch_cusventtree.column("#0", width=35)
      purch_cusventtree.column("1", width=160)
      purch_cusventtree.column("2", width=160)
      purch_cusventtree.column("3", width=140)
      purch_cusventtree.column("4", width=140)
      purch_cusventtree.heading("#0",text="")
      purch_cusventtree.heading("1",text="Customer/Ventor ID")
      purch_cusventtree.heading("2",text="Customer/Ventor Name")
      purch_cusventtree.heading("3",text="Tel.")
      purch_cusventtree.heading("4",text="Contact Person")
      purch_cusventtree.place(x=5, y=45)

      sql_sel_pord_cust = "SELECT * FROM customer"
      fbcursor.execute(sql_sel_pord_cust)
      pord_customer_details = fbcursor.fetchall()

      count=0
      for i in pord_customer_details:
        if True:
          purch_cusventtree.insert(parent='',index='end',iid=i,text='',values=(i[0],i[4],i[10],i[8]))
        else:
          pass
      count += 1

      def pordcust_tree_fetch():
        pordcust_tree_item = purch_cusventtree.item(purch_cusventtree.focus())["values"][0]
        sql = "SELECT * FROM customer WHERE customerid=%s"
        val = (pordcust_tree_item,)
        fbcursor.execute(sql,val)
        pordsel_cust_str = fbcursor.fetchone()
        vender_combo.delete(0, END)
        vender_combo.insert(0,pordsel_cust_str[4])
        paddress.delete('1.0',END)
        paddress.insert('1.0',pordsel_cust_str[5])
        pmail.delete(0, END)
        pmail.insert(0,pordsel_cust_str[9])
        psms.delete(0,END)
        psms.insert(0,pordsel_cust_str[12])

        sql = "select * from company"
        fbcursor.execute(sql)
        delata = fbcursor.fetchone()
        pdel.delete(0, END)
        pdel.insert(0, delata[1])
        pdel_addr.delete('1.0',END)
        pdel_addr.insert('1.0',delata[2])

        purch_cuselection.destroy()


      ctegorytree=ttk.Treeview(purch_cuselection, height=27)
      ctegorytree["columns"]=["1"]
      ctegorytree.column("#0", width=35, minwidth=20)
      ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
      ctegorytree.heading("#0",text="", anchor=W)
      ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
      ctegorytree.place(x=660, y=45)

      scrollbar = Scrollbar(purch_cuselection)
      scrollbar.place(x=640, y=45, height=560)
      scrollbar.config( command=purch_cusventtree.yview )

      btn1=Button(purch_cuselection,compound = LEFT,image=tick, text="ok",command=treefthcng1, width=60).place(x=15, y=610)
      btn1=Button(purch_cuselection,compound = LEFT,image=tick, text="Edit selected customer", width=150).place(x=250, y=610)
      btn1=Button(purch_cuselection,compound = LEFT,image=tick,text="Add new customer", width=150,command=purch_create_newcust).place(x=435, y=610)
      btn1=Button(purch_cuselection,compound = LEFT,image=cancel, text="Cancel", width=60).place(x=740, y=610)   



    #add new line item
    def edit_newlineproduct():
      pnewselection=Toplevel()
      pnewselection.title("Select Customer")
      pnewselection.geometry("930x650+240+10")
      pnewselection.resizable(False, False)

      #add new product
      def product():  
        top = Toplevel()  
        top.title("Add a new Product/Service")
        p2 = PhotoImage(file = 'images/fbicon.png')
        top.iconphoto(False, p2)
      
        top.geometry("700x550+390+15")
        tabControl = ttk.Notebook(top)
        s = ttk.Style()
        s.theme_use('default')
        s.configure('TNotebook.Tab', background="#999999",padding=10,bd=0)


        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
      
        tabControl.add(tab1,compound = LEFT, text ='Product/Service')
        tabControl.add(tab2,compound = LEFT, text ='Product Image')
      
        tabControl.pack(expand = 1, fill ="both")
      
        innerFrame = Frame(tab1,bg="#f5f3f2", relief=GROOVE)
        innerFrame.pack(side="top",fill=BOTH)

        Customerlabelframe = LabelFrame(innerFrame,text="Product/Service",width=580,height=485)
        Customerlabelframe.pack(side="top",fill=BOTH,padx=10)

        code1=Label(Customerlabelframe,text="Code or SKU:",fg="blue",pady=10,padx=10)
        code1.place(x=20,y=0)
        codeentry = Entry(Customerlabelframe,width=35)
        codeentry.place(x=120,y=8)

        checkvarStatus=IntVar()
        status1=Label(Customerlabelframe,text="Status:")
        status1.place(x=500,y=8)
        Button1 = Checkbutton(Customerlabelframe,
                          variable = checkvarStatus,text="Active",compound="right",
                          onvalue =0 ,
                          offvalue = 1,
                        
                          width = 10)

        Button1.place(x=550,y=5)

        category1=Label(Customerlabelframe,text="Category:",pady=5,padx=10)
        category1.place(x=20,y=40)
        n = StringVar()
        country = ttk.Combobox(Customerlabelframe, width = 40, textvariable = n )
        
        country['values'] = ('Default',' India',' China',' Australia',' Nigeria',' Malaysia',' Italy',' Turkey',)
        
        country.place(x=120,y=45)
        country.current(0)


        name1=Label(Customerlabelframe,text="Name :",fg="blue",pady=5,padx=10)
        name1.place(x=20,y=70)
        nameentry = Entry(Customerlabelframe,width=60)
        nameentry.place(x=120,y=75)

        des1=Label(Customerlabelframe,text="Description :",pady=5,padx=10)
        des1.place(x=20,y=100)
        desentry = Entry(Customerlabelframe,width=60)
        desentry.place(x=120,y=105)

        uval = IntVar(Customerlabelframe, value='$0.00')
        unit1=Label(Customerlabelframe,text="Unit Price:",fg="blue",pady=5,padx=10)
        unit1.place(x=20,y=130)
        unitentry = Entry(Customerlabelframe,width=20,textvariable=uval)
        unitentry.place(x=120,y=135)

        pcsval = IntVar(Customerlabelframe, value='$0.00')
        pcs1=Label(Customerlabelframe,text="Pcs/Weight:",fg="blue",pady=5,padx=10)
        pcs1.place(x=320,y=140)
        pcsentry = Entry(Customerlabelframe,width=20,textvariable=pcsval)
        pcsentry.place(x=410,y=140)

        costval = IntVar(Customerlabelframe, value='$0.00')
        cost1=Label(Customerlabelframe,text="Cost:",pady=5,padx=10)
        cost1.place(x=20,y=160)
        costentry = Entry(Customerlabelframe,width=20,textvariable=costval)
        costentry.place(x=120,y=165)

        priceval = IntVar(Customerlabelframe, value='$0.00')
        price1=Label(Customerlabelframe,text="(Price Cost):",pady=5,padx=10)
        price1.place(x=20,y=190)
        priceentry = Entry(Customerlabelframe,width=20,textvariable=priceval)
        priceentry.place(x=120,y=195)

        checkvarStatus2=IntVar()
      
        Button2 = Checkbutton(Customerlabelframe,variable = checkvarStatus2,
                          text="Taxable Tax1rate",compound="right",
                          onvalue =0 ,
                          offvalue = 1,
                          height=2,
                          width = 12)

        Button2.place(x=415,y=170)


        checkvarStatus3=IntVar()
      
        Button3 = Checkbutton(Customerlabelframe,variable = checkvarStatus3,
                          text="No stock Control",
                          onvalue =1 ,
                          offvalue = 0,
                          height=3,
                          width = 15)

        Button3.place(x=40,y=220)


        stockval = IntVar(Customerlabelframe, value='0')
        stock1=Label(Customerlabelframe,text="Stock:",pady=5,padx=10)
        stock1.place(x=90,y=260)
        stockentry = Entry(Customerlabelframe,width=15,textvariable=stockval)
        stockentry.place(x=150,y=265)

        lowval = IntVar(Customerlabelframe, value='0')
        low1=Label(Customerlabelframe,text="Low Stock Warning Limit:",pady=5,padx=10)
        low1.place(x=300,y=260)
        lowentry = Entry(Customerlabelframe,width=10,textvariable=lowval)
        lowentry.place(x=495,y=265)

      
        ware1=Label(Customerlabelframe,text="Warehouse:",pady=5,padx=10)
        ware1.place(x=60,y=290)
        wareentry = Entry(Customerlabelframe,width=50)
        wareentry.place(x=150,y=295)

        text1=Label(Customerlabelframe,text="Private notes(not appears on invoice):",pady=5,padx=10)
        text1.place(x=20,y=330)

        txt = scrolledtext.ScrolledText(Customerlabelframe, undo=True,width=62,height=4)
        txt.place(x=32,y=358)

        okButton = Button(innerFrame,compound = LEFT,image=tick , text ="Ok",width=60)
        okButton.pack(side=LEFT)

        cancelButton = Button(innerFrame,compound = LEFT,image=cancel ,text="Cancel",width=60)
        cancelButton.pack(side=RIGHT)

        imageFrame = Frame(tab2, relief=GROOVE,height=580)
        imageFrame.pack(side="top",fill=BOTH)

        browseimg=Label(imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
        browseimg.place(x=15,y=35)

        browsebutton=Button(imageFrame,text = 'Browse')
        browsebutton.place(x=580,y=30,height=30,width=50)
        
        removeButton = Button(imageFrame,compound = LEFT,image=cancel, text ="Remove Product Image",width=150)
        removeButton.place(x=400,y=450)
                      
      enter=Label(pnewselection, text="Enter filter text").place(x=5, y=10)
      e1=Entry(pnewselection, width=20).place(x=110, y=10)
      text=Label(pnewselection, text="Filtered column").place(x=340, y=10)
      e2=Entry(pnewselection, width=20).place(x=450, y=10)

      pur_cusventtree=ttk.Treeview(pnewselection, height=27)
      pur_cusventtree["columns"]=["1","2","3", "4","5"]
      pur_cusventtree.column("#0", width=35)
      pur_cusventtree.column("1", width=160)
      pur_cusventtree.column("2", width=160)
      pur_cusventtree.column("3", width=140)
      pur_cusventtree.column("4", width=70)
      pur_cusventtree.column("5", width=70)
      pur_cusventtree.heading("#0",text="")
      pur_cusventtree.heading("1",text="ID/SKU")
      pur_cusventtree.heading("2",text="Product/Service Name")
      pur_cusventtree.heading("3",text="Unit price")
      pur_cusventtree.heading("4",text="Service")
      pur_cusventtree.heading("5",text="Stock")
      pur_cusventtree.place(x=5, y=45)

      ctegorytree=ttk.Treeview(pnewselection, height=27)
      ctegorytree["columns"]=["1"]
      ctegorytree.column("#0", width=35, minwidth=20)
      ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
      ctegorytree.heading("#0",text="", anchor=W)
      ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
      ctegorytree.place(x=660, y=45)

      scrollbar = Scrollbar(pnewselection)
      scrollbar.place(x=640, y=45, height=560)
      scrollbar.config( command=tree.yview )

      btn1=Button(pnewselection,compound = LEFT,image=tick ,text="ok",command=purchseleproduct, width=60).place(x=15, y=610)
      btn1=Button(pnewselection,compound = LEFT,image=tick , text="Edit product/Service", width=150).place(x=250, y=610)
      btn1=Button(pnewselection,compound = LEFT,image=tick , text="Add product/Service", width=150).place(x=435, y=610)
      btn1=Button(pnewselection,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=610)

    #preview new line
    def previewline_edit():
      messagebox.showerror("F-Billing Revolution","line is required,please select customer for this order before printing.")



    #sms notification
    def sms_edit():
      send_SMS=Toplevel()
      send_SMS.geometry("700x480+240+150")
      send_SMS.title("Send SMS notification")

      style = ttk.Style()
      style.theme_use('default')
      style.configure('TNotebook.Tab', background="#999999", padding=5)
      sms_Notebook = ttk.Notebook(send_SMS)
      SMS_Notification = Frame(sms_Notebook, height=470, width=700)
      SMS_Service_Account = Frame(sms_Notebook, height=470, width=700)
      sms_Notebook.add(SMS_Notification, text="SMS Notification")
      sms_Notebook.add(SMS_Service_Account, text="SMS Service Account")
      sms_Notebook.place(x=0, y=0)

      numlbel=Label(SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
      numlbel.place(x=10, y=10)
      numentry=Entry(SMS_Notification, width=92).place(x=10, y=30)
      stexbel=Label(SMS_Notification, text="SMS Text").place(x=10, y=60)
      stex=Entry(SMS_Notification, width=40).place(x=10, y=85,height=120)
      
      dclbel=Label(SMS_Notification, text="Double click to insert into text")
      dclbel.place(x=410, y=60)
      dcl=Entry(SMS_Notification, width=30)
      dcl.place(x=400, y=85,height=200)

      smstype=LabelFrame(SMS_Notification, text="SMS message type", width=377, height=60)
      smstype.place(x=10, y=223)
      snuvar=IntVar()
      normal_rbtn=Radiobutton(smstype, text="Normal SMS(160 chars)", variable=snuvar, value=1)
      normal_rbtn.place(x=5, y=5)
      unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)", variable=snuvar, value=2)
      unicode_rbtn.place(x=190, y=5)
      tiplbf=LabelFrame(SMS_Notification, text="Tips", width=680, height=120)
      tiplbf.place(x=10, y=290)
      tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="Always start the SMS nymber with the country code. Do not use the + sign at the beginning(example\nUS number:8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
      tiplabl.place(x=5, y=5)

      btn1=Button(SMS_Notification, width=20, text="Send SMS notification").place(x=10, y=420)
      btn2=Button(SMS_Notification, width=25, text="Confirm SMS cost before sending").place(x=280, y=420)
      btn3=Button(SMS_Notification, width=15, text="Cancel").place(x=550, y=420)
      

      smstype=LabelFrame(SMS_Service_Account, text="Select the notification service provider", width=670, height=65)
      smstype.place(x=10, y=5)
      snumvar=IntVar()
      normal_rbtn=Radiobutton(smstype,text="BULKSMS(www.bulksms.com)",variable=snumvar,value=1,)
      normal_rbtn.place(x=5, y=5)
      unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)-Recommended", variable=snumvar, value=2)
      unicode_rbtn.place(x=290, y=5)

      sms1type=LabelFrame(SMS_Service_Account, text="Your BULKSMS.COM Account", width=670, height=100)
      sms1type.place(x=10, y=80)
      name=Label(sms1type, text="Username").place(x=10, y=5)
      na=Entry(sms1type, width=20).place(x=100, y=5)
      password=Label(sms1type, text="Password").place(x=10, y=45)
      pas=Entry(sms1type, width=20).place(x=100, y=45)
      combo=Label(sms1type, text="Route").place(x=400, y=5)
      n = StringVar()
      combo1 = ttk.Combobox(sms1type, width = 20, textvariable = n ).place(x=450,y=5)
      btn1=Button(sms1type, width=10, text="Save settings").place(x=550, y=45)

      
      tiplbf=LabelFrame(SMS_Service_Account, text="Terms of service", width=680, height=250)
      tiplbf.place(x=10, y=190)
      tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
      tiplabl.place(x=0, y=5)
      tiplabl1=Label(tiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
      tiplabl1.place(x=0, y=60)
      tiplabl2=Label(tiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
      tiplabl2.place(x=0, y=100)
      tiplabl3=Label(tiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
      tiplabl3.place(x=0, y=140)
      checkvar1=IntVar()
      chkbtn1=Checkbutton(tiplbf,text="I have read and agree to the terms of service above",variable=checkvar1,onvalue=1,offvalue=0).place(x=70, y=200) 
  

    #delete line item 
    def purch_delete_edit():
      messagebox.showerror("F-Billing Revolution","Customer is required,please select customer before deleting line item.")



    #finalize
    def finalize_edit():  
      messagebox.askyesno("Finalize purchase order", "Would you like to mark this purchase order as completed ?All product will be added in to stock and purchase order will be closed")


    firFrame1=Frame(pop1, bg="#f5f3f2", height=60)
    firFrame1.pack(side="top", fill=X)

    w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    edit_create = Button(firFrame1,compound="top", text="Select\nVendor",relief=RAISED, image=customer,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=purch_sele_edit_customer)
    edit_create.pack(side="left", pady=3, ipadx=4)


    w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    edit_add= Button(firFrame1,compound="top", text="Add new\nline item",relief=RAISED, image=photo,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=edit_newlineproduct)
    edit_add.pack(side="left", pady=3, ipadx=4)

    edit_dele= Button(firFrame1,compound="top", text="Delete line\nitem",relief=RAISED, image=photo2,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=purch_delete_edit)
    edit_dele.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    edit_prev= Button(firFrame1,compound="top", text="Preview\nP.Order",relief=RAISED, image=photo4,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=previewline_edit)
    edit_prev.pack(side="left", pady=3, ipadx=4)

    edit_prin= Button(firFrame1,compound="top", text="Print \nP.Order",relief=RAISED, image=photo5,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=printsele1)
    edit_prin.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    edit_mail= Button(firFrame1,compound="top", text="Email\nP.Order",relief=RAISED, image=photo6,bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
    edit_mail.pack(side="left", pady=3, ipadx=4)

    edit_sms= Button(firFrame1,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=sms_edit)
    edit_sms.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    edit_finalize= Button(firFrame1,compound="top", text="Finalize\nP.Order",relief=RAISED, image=mark1,bg="#f5f3f2", fg="red", height=55, bd=1, width=55,command=finalize_edit)
    edit_finalize.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)


    calc= Button(firFrame1,compound="top", text="Open\nCalculator",relief=RAISED, image=photo9,bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
    calc.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="right", padx=5)

    Createorder= Button(firFrame1,compound="top", text="Save",relief=RAISED, image=tick,bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
    #,commnd=updateporder)
    Createorder.pack(side="right", pady=3, ipadx=4)
 

    fir1Frame=Frame(pop1, height=180,bg="#f5f3f2")
    fir1Frame.pack(side="top", fill=X)
    

    labelframe1 = LabelFrame(fir1Frame,text=" Vendor")
    labelframe1.place(x=10,y=5,width=640,height=160) 

    # def updateporder():
    #   businessname=vender_combo.get()
    #   businessaddress=paddress.get('1.0', 'end-1c')
    #   delname=pdel.get   #('1.0', 'end-1c')
    #   deladdress=pdel_addr.get('1.0', 'end-1c')
    #   cpemail=pmail.get    #('1.0', 'end-1c')
    #   cpmobileforsms=psms.get #('1.0', 'end-1c')
    #   private_notes = pvt.get("1.0","end-1c")
    #   porderdate = pdate.get_date()
    #   duedate = pdue.get_date()
    #   term_of_payment = e4.get()
    #   extracostname = pextra.get()
    #   porderid = porder_id.get()
    #   discourate = pdisc.get()
    #   extracost = pcost.get()
    #   tax1 =  porder_tax4.get()
    #   salesper =  psale.get()
    #   category = pact.get()
    #   status = draft.cget("text")
    #   emailon = nev1.cget("text")
    #   printon = nev2.cget("text")
    #   pordtot =  order1.cget("text")
    #   title_text = e1.get()
    #   header_text = e11.get()
    #   footer_text = e12.get()
    #   term_of_payment = e4.get()
    #   terms = e13.get("1.0","end-1c")
    #   comments = e14.get("1.0","end-1c")
    #   idporder= osdata[0]


    #   for line in purch_tree.get_children():
    #     idsave=purch_tree.item(line)['values'][0]

    #     sql1= 'SELECT * FROM  Productservice WHERE Productserviceid = %s'
    #     val=(idsave,)
    #     # print(val)
    #     fbcursor.execute(sql1,val,)
    #     child=fbcursor.fetchone()
    #   # print(child)
    #   # sql2= 'UPDATE storingproduct SET Productserviceid=%s,orderid=%s,sku=%s,category=%s,name=%s,description=%s,status=%s,unitprice=%s,peices=%s,cost=%s,taxable=%s,priceminuscost=%s,serviceornot=%s,stock=%s,stocklimit=%s,warehouse=%s,privatenote=%s'
    #   # val1=(child[0],sctxt,child[2],child[3],child[4],child[5],child[6],child[7],child[8],child[9],child[10],child[11],child[12],child[13],child[14],child[15],child[16])
    #   # fbcursor.execute(sql2,val1,)
    #   # fbilldb.commit()

    # sql3='UPDATE porder SET porder_no=%s,porderdate=%s,duedate=%s,status=%s,emailon=%s,printon=%s,ordertot=%s,extra_cost_name=%s,extra_cost=%s,sales_person=%s,discount_rate=%s,tax1=%s,category=%s,businessname=%s,businessaddress=%s,deliveryto=%s,deliveryaddress=%s,cpemail=%s,cpmobileforsms=%s,title_text=%s,header_text=%s,footer_text=%s,term_of_payment=%s,terms=%s,comments=%s,privatenote=%s WHERE porder_no=%s'
    # val2=(porderid,porderdate,duedate,status,emailon,printon,pordtot,extracostname,extracost, salesper,discourate,tax1, category,businessname,businessaddress,delname, deladdress,cpemail,cpmobileforsms,title_text, header_text, footer_text,term_of_payment,terms,comments,private_notes,idporder)
    # fbcursor.execute(sql3,val2,)
    # fbilldb.commit()

    # sqlup='UPDATE storingproduct SET porder_no=%s WHERE porder_no=%s'
    # valup=(porder_no,idporder,)
    # fbcursor.execute(sqlup,valup,)
    # fbilldb.commit()

    for record in pord_tree.get_children():
      pord_tree.delete(record)
    fbcursor.execute("select *  from porder")
    pandsdata = fbcursor.fetchall()
    countp = 0
    for i in pandsdata:
      pord_tree.insert(parent='', index='end', iid=i, text='', values=(' ',i[39], i[2], i[3], i[25],i[5], i[6], i[7], i[8], i[9], i[10]))
    countp += 1

    def purch_to_combo(event):
      purch_to_str = purch_to.get()
      sql = "SELECT * FROM Customer WHERE businessname=%s"
      val = (purch_to_str,)
      fbcursor.execute(sql,val)
      purch_sel_combo = fbcursor.fetchone()
      print(purch_sel_combo)
      pmail.delete(0,END)
      pmail.insert(0,purch_sel_combo[9])
      psms.delete(0,END)
      psms.insert(0,purch_sel_combo[12])
      sql = "select * from company"
      fbcursor.execute(sql)
      delata = fbcursor.fetchone()
      pdel.delete(0, END)
      pdel.insert(0, delata[1])
      pdel_addr.delete('1.0',END)
      pdel_addr.insert('1.0',delata[2])

    

    sql = "select businessname from Customer"
    fbcursor.execute(sql,)
    purdata = fbcursor.fetchall()
  # ##
  #   itemid = purch_tree.item(purch_tree.focus())["values"][0]
  #   sql = "select * from porder where porder_no = %s"
  #   val = (itemid, )
  #   fbcursor.execute(sql, val)
  #   global osdata
  #   osdata = fbcursor.fetchone()

    
    

    def treefthcng1():
      itemid = purch_cusventtree.item(purch_cusventtree.focus())["values"][0]
      sql = "select * from Customer where customerid = %s"
      val = (itemid, )
      fbcursor.execute(sql, val)
      slctcstr = fbcursor.fetchone()
      vender_combo.delete(0,'end')
      vender_combo.insert(0, slctcstr[4])
      paddress.delete('1.0','end')
      paddress.insert("1.0", slctcstr[5])
      pdel.delete('1.0','end')
      pdel.insert('1.0', slctcstr[24])
      pdel_addr.delete('1.0','end')
      pdel_addr.insert('1.0', slctcstr[25])
      pmail.delete('1.0','end')
      pmail.insert('1.0', slctcstr[9])
      psms.delete('1.0','end')
      psms.insert('1.0', slctcstr[10])
      cuselection.destroy()

    sql = "select businessname from Customer"
    fbcursor.execute(sql,)
    pdata = fbcursor.fetchall() 

    # itemid=pord_tree.item(pord_tree.focus())["values"][1]
    sql = "select * from porder"
    fbcursor.execute(sql)
    global osdata
    osdata = fbcursor.fetchone() 


    porder = Label(labelframe1, text="Vendor to").place(x=10,y=5)

    purch_to = StringVar()
    vender_combo = ttk.Combobox(labelframe1, value="Hello",width=28)
    vender_combo.place(x=80,y=5)
    vender_combo['values'] = purdata
    vender_combo.bind("<<ComboboxSelected>>", purch_to_combo)
    # vender_combo=Entry(labelframe1,width=31)
    # vender_combo.place(x=80,y=5)
    vender_combo.delete(0,'end')
    vender_combo.insert(0, osdata[25])

    address=Label(labelframe1,text="Address").place(x=10,y=30)
    paddress=Text(labelframe1,width=23)
    paddress.place(x=80,y=30,height=70)
    paddress.delete('1.0', END)
    paddress.insert('1.0', osdata[20])

    ship=Label(labelframe1,text="Delivery to").place(x=342,y=5)
    pdel=Entry(labelframe1,width=30)
    pdel.place(x=402,y=3)
    pdel.delete(0,'end')
    pdel.insert(0, osdata[27])

    address1=Label(labelframe1,text="Address").place(x=340,y=30)
    pdel_addr=Text(labelframe1,width=23)
    pdel_addr.place(x=402,y=30,height=70)
    pdel_addr.delete('1.0','end')
    pdel_addr.insert('1.0', osdata[28])

    
    labelframe2 = LabelFrame(fir1Frame,text="")
    labelframe2.place(x=10,y=130,width=640,height=42)
    email=Label(labelframe2,text="Email").place(x=10,y=5)
    pmail=Entry(labelframe2,width=30)
    pmail.delete(0,'end')
    pmail.place(x=80,y=5)
    pmail.insert(0, osdata[23])


    sms=Label(labelframe2,text="SMS Number").place(x=327,y=5)
    psms=Entry(labelframe2,width=28)
    psms.place(x=402,y=3)
    psms.delete(0,'end')
    psms.insert(0, osdata[24])

    labelframe = LabelFrame(fir1Frame,text="Purchase Order")
    labelframe.place(x=652,y=5,width=290,height=170)
    porder=Label(labelframe,text="P.Order#").place(x=5,y=5)
    porder_id=Entry(labelframe,width=27)
    porder_id.place(x=100,y=5,)
    porder_id.delete(0,'end')
    porder_id.insert(0, osdata[39])
        

    porderdate=Label(labelframe,text="P.Order date").place(x=5,y=33)
    pdate=DateEntry(labelframe,width=20)
    pdate.place(x=150,y=33)
    pdate.delete(0,'end')
    pdate.insert(0, osdata[2].strftime('%d/%m/%y'))


    # sql="select dateformat from company"
    # fbcursor.execute(sql)
    # date_for = fbcursor.fetchone()
     
    # if not date_for:
    #   pass
    # else:
    #   if date_for[0] == "mm-dd-yyyy":
    #     pdate._set_text(pdate._date.strftime('%m-%d-%Y'))
    #   elif date_for[0] == "dd-mm-yyyy":
    #     pdate._set_text(pdate._date.strftime('%d-%m-%Y'))
    #   elif date_for[0] == "yyy.mm.dd":
    #     pdate._set_text(pdate._date.strftime('%Y.%m.%d'))
    #   elif date_for[0] == "mm/dd/yyyy":
    #     pdate._set_text(pdate._date.strftime('%m/%d/%Y'))
    #   elif date_for[0] == "dd/mm/yyy":
    #     pdate._set_text(pdate._date.strftime('%d/%m/%Y'))
    #   elif date_for[0] == "dd.mm.yyyy":
    #     pdate._set_text(pdate._date.strftime('%d.%m.%Y'))
    #   elif date_for[0] == "yyyy/mm/dd":
    #     pdate._set_text(pdate._date.strftime('%Y/%m/%d'))
    #   else:
    #     pass
  

    def porder_due_check():
      if checkvarStatus5.get() == 0:
        pdue['state'] = DISABLED
      else:
        pdue['state'] = NORMAL

    checkvarStatus5=IntVar()
    duedate=Checkbutton(labelframe,variable = checkvarStatus5,text="P.Due date",onvalue =0 ,offvalue = 1,command=porder_due_check).place(x=5,y=62)
    pdue=DateEntry(labelframe,width=20)
    pdue.place(x=150,y=62)
    pdue.delete(0,'end')
    pdue.insert(0, osdata[3].strftime('%d/%m/%y'))


    terms=Label(labelframe,text="Terms").place(x=5,y=92)
    e4=ttk.Combobox(labelframe, value="",width=25).place(x=100,y=92)
    ref=Label(labelframe,text="Porder ref#").place(x=5,y=118)
    pref=Entry(labelframe,width=27).place(x=100,y=118)

    fir2Frame=Frame(pop1, height=150,width=100,bg="#f5f3f2")
    fir2Frame.pack(side="top", fill=X)
    listFrame = Frame(fir2Frame, bg="white", height=140,borderwidth=5,  relief=RIDGE)


    sql = "select * from company"
    fbcursor.execute(sql)
    ptaxdata = fbcursor.fetchone()
    # global purch_tree
    if not ptaxdata:
      edit_purch_tree=ttk.Treeview(listFrame)
      edit_purch_tree["columns"]=["1","2","3","4","5","6","7"]

      edit_purch_tree.column("#0", width=40)
      edit_purch_tree.column("1", width=80)
      edit_purch_tree.column("2", width=190)
      edit_purch_tree.column("3", width=190)
      edit_purch_tree.column("4", width=80)
      edit_purch_tree.column("5", width=60)
      edit_purch_tree.column("6", width=60)
      edit_purch_tree.column("7", width=60)
      #purch_tree.column("8", width=80)
      
      edit_purch_tree.heading("#0")
      edit_purch_tree.heading("1",text="ID/SKU")
      edit_purch_tree.heading("2",text="Product/Service")
      edit_purch_tree.heading("3",text="Description")
      edit_purch_tree.heading("4",text="Unit Price")
      edit_purch_tree.heading("5",text="Quantity")
      edit_purch_tree.heading("6",text="Pcs/Weight")
      # purch_tree.heading("7",text="Tax1")
      edit_purch_tree.heading("7",text="Price")

      # purch_tree.pack(fill="both", expand=1)
      # listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

    elif ptaxdata[12] == "1":
      edit_purch_tree=ttk.Treeview(listFrame)
      edit_purch_tree["columns"]=["1","2","3","4","5","6","7"]

      edit_purch_tree.column("#0", width=40)
      edit_purch_tree.column("1", width=80)
      edit_purch_tree.column("2", width=190)
      edit_purch_tree.column("3", width=190)
      edit_purch_tree.column("4", width=80)
      edit_purch_tree.column("5", width=60)
      edit_purch_tree.column("6", width=60)
      edit_purch_tree.column("7", width=60)
      #purch_tree.column("8", width=80)
      
      edit_purch_tree.heading("#0")
      edit_purch_tree.heading("1",text="ID/SKU")
      edit_purch_tree.heading("2",text="Product/Service")
      edit_purch_tree.heading("3",text="Description")
      edit_purch_tree.heading("4",text="Unit Price")
      edit_purch_tree.heading("5",text="Quantity")
      edit_purch_tree.heading("6",text="Pcs/Weight")
      # purch_tree.heading("7",text="Tax1")
      edit_purch_tree.heading("7",text="Price")

      # purch_tree.pack(fill="both", expand=1)
      # listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

    elif ptaxdata[12] == "2":
      edit_purch_tree=ttk.Treeview(listFrame)
      edit_purch_tree["columns"]=["1","2","3","4","5","6","7","8"]

      edit_purch_tree.column("#0", width=40)
      edit_purch_tree.column("1", width=80)
      edit_purch_tree.column("2", width=190)
      edit_purch_tree.column("3", width=190)
      edit_purch_tree.column("4", width=80)
      edit_purch_tree.column("5", width=60)
      edit_purch_tree.column("6", width=60)
      edit_purch_tree.column("7", width=60)
      edit_purch_tree.column("8", width=80)
      
      edit_purch_tree.heading("#0")
      edit_purch_tree.heading("1",text="ID/SKU")
      edit_purch_tree.heading("2",text="Product/Service")
      edit_purch_tree.heading("3",text="Description")
      edit_purch_tree.heading("4",text="Unit Price")
      edit_purch_tree.heading("5",text="Quantity")
      edit_purch_tree.heading("6",text="Pcs/Weight")
      edit_purch_tree.heading("7",text="Tax1")
      edit_purch_tree.heading("8",text="Price")

    # purch_tree.pack(fill="both", expand=1)
    # listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

    elif ptaxdata[12] == "3":
      edit_purch_tree=ttk.Treeview(listFrame)
      edit_purch_tree["columns"]=["1","2","3","4","5","6","7","8","9"]

      edit_purch_tree.column("#0", width=40)
      edit_purch_tree.column("1", width=80)
      edit_purch_tree.column("2", width=190)
      edit_purch_tree.column("3", width=190)
      edit_purch_tree.column("4", width=80)
      edit_purch_tree.column("5", width=60)
      edit_purch_tree.column("6", width=60)
      edit_purch_tree.column("7", width=60)
      edit_purch_tree.column("8", width=60)
      edit_purch_tree.column("9", width=80)
      
      edit_purch_tree.heading("#0")
      edit_purch_tree.heading("1",text="ID/SKU")
      edit_purch_tree.heading("2",text="Product/Service")
      edit_purch_tree.heading("3",text="Description")
      edit_purch_tree.heading("4",text="Unit Price")
      edit_purch_tree.heading("5",text="Quantity")
      edit_purch_tree.heading("6",text="Pcs/Weight")
      edit_purch_tree.heading("7",text="Tax1")
      edit_purch_tree.heading("8",text="Tax2")
      edit_purch_tree.heading("9",text="Price")
    
    edit_purch_tree.pack(fill="both", expand=1)
    listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)
    
    # ba=osdata[0]
    # sql4='SELECT * FROM storingproduct WHERE porder_no=%s'
    # val10=(ba,)
    # fbcursor.execute(sql4,val10)
    # totalpriceinput=0
    # j = 0
    # for i in fbcursor:
    #   purch_tree.insert(parent='', index='end', iid=i, text='', values=(i[4],i[6],i[7],i[9],i[22],i[10],i[12],(i[9]*i[22])))
    #   # for line in purch_tree.get_children():
    #   #   idsave1=purch_tree.item(line)['values'][7]
    #   totalpriceinput+=(i[9]*i[22])
    #   j += 1
    # pricecol.config(text=totalpriceinput)

    fir3Frame=Frame(pop1,height=200,width=700,bg="#f5f3f2")
    fir3Frame.place(x=0,y=490)

    tabStyle = ttk.Style()
    tabStyle.theme_use('default')
    tabStyle.configure('TNotebook.Tab', background="#999999", width=12, padding=5)
    myNotebook=ttk.Notebook(fir3Frame)
    orderFrame = Frame(myNotebook, height=200, width=800)
    headerFrame = Frame(myNotebook, height=200, width=800)
    commentFrame = Frame(myNotebook, height=200, width=800)
    termsFrame = Frame(myNotebook, height=200, width=800)
    noteFrame = Frame(myNotebook, height=200, width=800)
    documentFrame = Frame(myNotebook, height=200, width=800)
    
    myNotebook.add(orderFrame,compound="left", text="Purchase Order")
    myNotebook.add(headerFrame,compound="left",  text="Header/Footer")
    myNotebook.add(commentFrame,compound="left",  text="Comments")
    myNotebook.add(termsFrame,compound="left", text="Terms")
    myNotebook.add(noteFrame,compound="left",  text="Private notes")
    myNotebook.add(documentFrame,compound="left",  text="Documents")
    myNotebook.pack(expand = 1, fill ="both")


      
  ##
    # itemid = pord_tree.item(pord_tree.focus())["values"][1]
    sql = "select * from porder"
    # val = (itemid, )
    fbcursor.execute(sql)
    orbtdata = fbcursor.fetchone()

    def pord_recalc_edit_dis(event):
      sql = "select * from company"
      fbcursor.execute(sql)
      taxdata1 = fbcursor.fetchone()
      if taxdata1[12] == "1":
        price = 0.0
        total_cost = 0.0
        exc = float(edit_pcost.get())
        dis_rate = float(edit_pdisc.get())
        for i in edit_purch_tree.get_children():
          price += float(edit_purch_tree.item(i,'values')[3])
        discount_rate = (price*dis_rate)/100
        total_cost += (price - discount_rate) + exc
        edit_discount.config(text= str(dis_rate) + "" +"% Discount")
        # estimate_totalpaid1.config(text="" +"0.00")
        edit_tax1.config(text="" +"0.00")
        edit_tax2.config(text="" +"0.00")
        edit_discount1.config(text=round(discount_rate,2))
        sub_tot = round((price - discount_rate),2)
        edit_sub.config(text=sub_tot)
        edit_cost.config(text=round(exc,2))
        edit_porder1.config(text=round(total_cost,2))
        
      elif taxdata1[12] == "2":
        price = 0.0
        p = 0.0
        total_cost = 0.0
        exc = float(edit_pcost.get())
        dis_rate = float(edit_pdisc.get())
        tx1 = float(porder_tax4.get())
        for i in edit_purch_tree.get_children():
          if edit_purch_tree.item(i,'values')[6] == "No":
            p += float(edit_purch_tree.item(i,'values')[3])
          else:
            price += float(edit_purch_tree.item(i,'values')[3])
        discount_rate = ((price + p) * dis_rate)/100
        dis_price = (price * dis_rate)/100
        dis_p = (p * dis_rate)/100
        tax1_rate = ((price - dis_price)*tx1)/100
        tx_calc = (price - dis_price) + tax1_rate
        tx_calc1 = p - dis_p
        total_cost += (tx_calc + tx_calc1) + exc 
        edit_discount.config(text= str(dis_rate) + "" +"% Discount")
        # estimate_totalpaid1.config(text="" +"0.00")
        edit_tax2.config(text="" +"0.00")
        edit_discount1.config(text=round(discount_rate,2))
        sub_tot = round(((price + p) - discount_rate),2)
        edit_sub1.config(text=sub_tot)
        edit_tax1.config(text=round(tax1_rate,2))
        edit_cost.config(text=round(exc,2))
        edit_porder1.config(text=round(total_cost,2))
        
      elif taxdata1[12] == "3":
        price = 0.0
        p1 = 0.0
        p2 = 0.0
        p3 = 0.0
        total_cost = 0.0
        tx1 = float(porder_tax4.get())
        tx2 = float(porder_tax5.get())
        exc = float(edit_pcost.get())
        dis_rate = float(edit_pdisc.get())
        for i in edit_purch_tree.get_children():
          if edit_purch_tree.item(i,'values')[6] == "No" and edit_purch_tree.item(i,'values')[7] == "No":
            p1 += float(edit_purch_tree.item(i,'values')[3])
          elif edit_purch_tree.item(i,'values')[6] == "Yes" and edit_purch_tree.item(i,'values')[7] == "No":
            p2 += float(edit_purch_tree.item(i,'values')[3])
          elif edit_purch_tree.item(i,'values')[6] == "No" and v.item(i,'values')[7] == "Yes":
            p3 += float(edit_purch_tree.item(i,'values')[3])
          else:
            price += float(edit_purch_tree.item(i,'values')[3])
        discount_rate = ((p1 + p2 + p3 + price) * dis_rate)/100
        dis_p2 = (p2 * dis_rate)/100
        tax1_rate = ((p2 - dis_p2) * tx1)/100
        dis_price = (price * dis_rate)/100
        tax2_rate = ((price - dis_price) * tx1)/100
        tax3_rate = ((price - dis_price) * tx2)/100
        dis_p3= (p3 * dis_rate)/100
        tax4_rate = ((p3 - dis_p3) * tx2)/100
        dis_p4 = (p1 * dis_rate)/100
        tx_calc1 = (p2 - dis_p2) + tax1_rate
        tx_calc2 = (price - dis_price) + tax2_rate + tax3_rate
        tx_calc3 = (p3 - dis_p3) + tax4_rate
        tx_calc4 = (p1 - dis_p4)
        total_cost += (tx_calc1 + tx_calc2 + tx_calc3 + tx_calc4) + exc
        edit_discount.config(text= str(dis_rate) + "" +"% Discount")
        # estimate_totalpaid1.config(text="" +"0.00")
        edit_discount1.config(text=round(discount_rate,2))
        sub_tot = round(((price + p1 + p2 + p3) - discount_rate),2)
        edit_sub1.config(text="$" + "" + str(sub_tot))
        edit_tax1.config(text=round((tax1_rate + tax2_rate),2))
        edit_tax2.config(text=round((tax3_rate + tax4_rate),2))
        edit_cost.config(text=round(exc,2))



  
    def pord_recalc_edit_recal(event):
      sql = "select * from company"
      fbcursor.execute(sql)
      taxdata1 = fbcursor.fetchone()
      if taxdata1[12] == "1":
        price = 0.0
        total_cost = 0.0
        exc = float(edit_pcost.get())
        dis_rate = float(edit_pdisc.get())
        for i in edit_purch_tree.get_children():
          price += float(edit_purch_tree.item(i,'values')[3])
        discount_rate = (price*dis_rate)/100
        total_cost += (price - discount_rate) + exc
        edit_discount.config(text= str(dis_rate) + "" +"% Discount")
        # estimate_totalpaid1.config(text="" +"0.00")
        edit_tax1.config(text="" +"0.00")
        edit_tax2.config(text="" +"0.00")
        edit_discount1.config(text=round(discount_rate,2))
        sub_tot = round((price - discount_rate),2)
        edit_sub.config(text=sub_tot)
        edit_cost.config(text=round(exc,2))
        edit_porder1.config(text=round(total_cost,2))
        
      elif taxdata1[12] == "2":
        price = 0.0
        p = 0.0
        total_cost = 0.0
        exc = float(edit_pcost.get())
        dis_rate = float(edit_pdisc.get())
        tx1 = float(porder_tax4.get())
        for i in edit_purch_tree.get_children():
          if edit_purch_tree.item(i,'values')[6] == "No":
            p += float(edit_purch_tree.item(i,'values')[3])
          else:
            price += float(edit_purch_tree.item(i,'values')[3])
        discount_rate = ((price + p) * dis_rate)/100
        dis_price = (price * dis_rate)/100
        dis_p = (p * dis_rate)/100
        tax1_rate = ((price - dis_price)*tx1)/100
        tx_calc = (price - dis_price) + tax1_rate
        tx_calc1 = p - dis_p
        total_cost += (tx_calc + tx_calc1) + exc 
        edit_discount.config(text= str(dis_rate) + "" +"% Discount")
        # estimate_totalpaid1.config(text="" +"0.00")
        edit_tax2.config(text="" +"0.00")
        edit_discount1.config(text=round(discount_rate,2))
        sub_tot = round(((price + p) - discount_rate),2)
        edit_sub1.config(text=sub_tot)
        edit_tax1.config(text=round(tax1_rate,2))
        edit_cost.config(text=round(exc,2))
        edit_porder1.config(text=round(total_cost,2))
        
      elif taxdata1[12] == "3":
        price = 0.0
        p1 = 0.0
        p2 = 0.0
        p3 = 0.0
        total_cost = 0.0
        tx1 = float(porder_tax4.get())
        tx2 = float(porder_tax5.get())
        exc = float(edit_pcost.get())
        dis_rate = float(edit_pdisc.get())
        for i in edit_purch_tree.get_children():
          if edit_purch_tree.item(i,'values')[6] == "No" and edit_purch_tree.item(i,'values')[7] == "No":
            p1 += float(edit_purch_tree.item(i,'values')[3])
          elif edit_purch_tree.item(i,'values')[6] == "Yes" and edit_purch_tree.item(i,'values')[7] == "No":
            p2 += float(edit_purch_tree.item(i,'values')[3])
          elif edit_purch_tree.item(i,'values')[6] == "No" and v.item(i,'values')[7] == "Yes":
            p3 += float(edit_purch_tree.item(i,'values')[3])
          else:
            price += float(edit_purch_tree.item(i,'values')[3])
        discount_rate = ((p1 + p2 + p3 + price) * dis_rate)/100
        dis_p2 = (p2 * dis_rate)/100
        tax1_rate = ((p2 - dis_p2) * tx1)/100
        dis_price = (price * dis_rate)/100
        tax2_rate = ((price - dis_price) * tx1)/100
        tax3_rate = ((price - dis_price) * tx2)/100
        dis_p3= (p3 * dis_rate)/100
        tax4_rate = ((p3 - dis_p3) * tx2)/100
        dis_p4 = (p1 * dis_rate)/100
        tx_calc1 = (p2 - dis_p2) + tax1_rate
        tx_calc2 = (price - dis_price) + tax2_rate + tax3_rate
        tx_calc3 = (p3 - dis_p3) + tax4_rate
        tx_calc4 = (p1 - dis_p4)
        total_cost += (tx_calc1 + tx_calc2 + tx_calc3 + tx_calc4) + exc
        edit_discount.config(text= str(dis_rate) + "" +"% Discount")
        # estimate_totalpaid1.config(text="" +"0.00")
        edit_discount1.config(text=round(discount_rate,2))
        sub_tot = round(((price + p1 + p2 + p3) - discount_rate),2)
        edit_sub1.config(text="$" + "" + str(sub_tot))
        edit_tax1.config(text=round((tax1_rate + tax2_rate),2))
        edit_tax2.config(text=round((tax3_rate + tax4_rate),2))
        edit_cost.config(text=round(exc,2))      

    def pexta_selected(event):
          psel = edit_etracost.get()
          print(psel)
          if psel == "Shipping and handling":
            edit_ecost=Label(summaryfrme, text="Shipping and handling")
            edit_ecost.place(x=0 ,y=84)
          elif psel == "Postage and handling":
            edit_ecost=Label(summaryfrme, text="Postage and handling ")
            edit_ecost.place(x=0 ,y=84)
          elif psel == "Delivery cost":
            edit_ecost=Label(summaryfrme, text="Delivery cost               ")
            edit_ecost.place(x=0 ,y=84)




    labelframe1 = LabelFrame(orderFrame,text="",font=("arial",15))
    labelframe1.place(x=1,y=1,width=800,height=170)
    edit_etracost = StringVar()
    cost1=Label(labelframe1,text="Extra cost name").place(x=2,y=5)
    edit_pextra=ttk.Combobox(labelframe1, value="",width=20,textvariable=edit_etracost)
    edit_pextra['values'] = ('Shipping and handling','Postage and handling','Delivery cost')
    edit_pextra.bind("<<ComboboxSelected>>",pexta_selected)
    edit_pextra.place(x=115,y=5)
    edit_pextra.delete(0,'end')
    edit_pextra.insert(0, orbtdata[11])


    rate=Label(labelframe1,text="Discount rate")
    rate.place(x=370,y=5)
    edit_pdisc=Spinbox(labelframe1,width=6,  from_=0, to=100, font="italic 10")
    edit_pdisc.place(x=460,y=5)
    edit_pdisc.bind('<Button-1>',pord_recalc_edit_dis)
    edit_pdisc.delete(0,'end')
    edit_pdisc.insert(0, orbtdata[15])

    cost2=Label(labelframe1,text="Extra cost").place(x=35,y=35)
    edit_pcost=Entry(labelframe1,width=10)
    edit_pcost.place(x=115,y=35)
    edit_pcost.bind('<KeyRelease>',pord_recalc_edit_recal)
    edit_pcost.delete(0,'end')
    edit_pcost.insert(0, orbtdata[12])
    # tax=Label(labelframe1,text="Tax1").place(x=420,y=35)
    # ptax=Entry(labelframe1,width=7).place(x=460,y=35)
    # tax2=Label(labelframe1,text="Tax1").place(x=420,y=35)
    # ptax2=Entry(labelframe1,width=7).place(x=460,y=35)
    pord_comp_sql = "SELECT * FROM company"
    fbcursor.execute(pord_comp_sql,)
    ptaxdata1 = fbcursor.fetchone()
    porder_tax=Label(labelframe1,text="Tax1")
    porder_tax4=Entry(labelframe1,width=7,justify=RIGHT)
    porder_taax5=Label(labelframe1,text="Tax2")
    porder_tax5=Entry(labelframe1,width=7,justify=RIGHT)
    if ptaxdata1[12] == "1":
      porder_tax4.insert(0, 0)
      porder_tax5.insert(0, 0)
    elif ptaxdata1[12] == "2":
      
      porder_tax.place(x=420,y=35)
      
      porder_tax4.place(x=460,y=35)
      def1_val = tax1ratee.get()
      porder_tax4.delete(0, END)
      porder_tax4.insert(0, def1_val)
      porder_tax5.insert(0, 0)
    elif ptaxdata1[12] == "3":
      
      porder_tax.place(x=420,y=35)
      
      porder_tax4.place(x=460,y=35)
      def1_val = tax1ratee.get()
      porder_tax4.delete(0, END)
      porder_tax4.insert(0, def1_val)
      
      porder_taax5.place(x=420,y=65)
      
      porder_tax5.place(x=460,y=65)
      def2_val = tax2ratee.get()
      porder_tax5.delete(0, END)
      porder_tax5.insert(0, def2_val)

    # template=Label(labelframe1,text="Template").place(x=37,y=70)
    # ptemp=ttk.Combobox(labelframe1, value="",width=25).place(x=115,y=70)
    sales=Label(labelframe1,text="Sales Person").place(x=25,y=100)
    edit_psale=Entry(labelframe1,width=18)
    edit_psale.place(x=115,y=100)
    edit_psale.delete(0,'end')
    edit_psale.insert(0, orbtdata[12])

    category=Label(labelframe1,text="Category").place(x=37,y=70)
    edit_pact=Entry(labelframe1,width=22)
    edit_pact.place(x=115,y=70)
    edit_pact.delete(0,'end')
    edit_pact.insert(0, orbtdata[15])

    statusfrme = LabelFrame(labelframe1,text="Status",font=("arial",15))
    statusfrme.place(x=540,y=0,width=160,height=160)

    # itemid = purch_tree.item(purch_tree.focus())["values"][1]
    sql = "select status from porder"
    # val = (itemid, )
    fbcursor.execute(sql)
    drftinvc = fbcursor.fetchone()

    # itemid = purch_tree.item(purch_tree.focus())["values"][1]
    sql = "select emailon from porder"
    # val = (itemid, )
    fbcursor.execute(sql)
    emldon = fbcursor.fetchone()
  ##
  ##
    # itemid = purch_tree.item(purch_tree.focus())["values"][1]
    sql = "select printon from porder"
    # val = (itemid, )
    fbcursor.execute(sql)
    prntdon = fbcursor.fetchone()

    draft=Label(statusfrme, text=drftinvc,font=("arial", 15, "bold"), fg="grey").place(x=50, y=3)
    edit_on1=Label(statusfrme, text="Emailed on:").place( y=50)
    edit_nev1=Label(statusfrme, text=emldon)
    edit_nev1.place(x=100,y=50)
    edit_on2=Label(statusfrme, text="Printed on:").place( y=90)
    edit_nev2=Label(statusfrme, text=prntdon)
    edit_nev2.place(x=100,y=90)

    text1=Label(headerFrame,text="Title text").place(x=50,y=5)
    edit_e1=ttk.Combobox(headerFrame, value="",width=60)
    edit_e1['values']=('Thank you for your purchase!','Thank you for buying!','Thank you for your businnes!','Thank you for your order!')
    edit_e1.place(x=125,y=5)
    edit_e1.delete(0,'end')
    edit_e1.insert(0, orbtdata[33])

    text2=Label(headerFrame,text="Page header text").place(x=2,y=45)
    edit_e11=ttk.Combobox(headerFrame, value="",width=60)
    edit_e11['values']=('Thank you for your purchase!','Thank you for buying!','Thank you for your businnes!','Thank you for your order!')
    edit_e11.place(x=125,y=45)
    edit_e11.delete(0,'end')
    edit_e11.insert(0, orbtdata[34])

    text3=Label(headerFrame,text="Footer text").place(x=35,y=85)
    edit_e12=ttk.Combobox(headerFrame, value="",width=60)
    edit_e12['values']=('Thank you for your purchase!','Thank you for buying!','Thank you for your businnes!','Thank you for your order!')
    edit_e12.place(x=125,y=85)
    edit_e12.delete(0,'end')
    edit_e12.insert(0, orbtdata[35])


    text=Label(noteFrame,text="Private notes(not shown on invoice/order/estemates)").place(x=10,y=10)
    edit_pvt=Text(noteFrame,width=100,height=7)
    edit_pvt.place(x=10,y=32)
    edit_pvt.delete(0,'end')
    edit_pvt.insert(0, orbtdata[29])

    edit_e13=scrolledtext.ScrolledText(termsFrame,width=100,height=9)
    edit_e13.place(x=10,y=10)
    edit_e13.delete('1.0','end')
    edit_e13.insert('1.0', orbtdata[37])

    edit_e14=scrolledtext.ScrolledText(commentFrame,width=100,height=9)
    edit_e14.place(x=10,y=10)
    edit_e14.delete('1.0','end')
    edit_e14.insert('1.0', orbtdata[37])

    btn1=Button(documentFrame,height=2,width=3,text="+").place(x=5,y=10)
    btn2=Button(documentFrame,height=2,width=3,text="-").place(x=5,y=50)
    text=Label(documentFrame,text="Attached documents or image files.If you attach large email then email taken long time to send").place(x=50,y=10)
    edit_purchse_doc_tree=ttk.Treeview(documentFrame, height=5)
    edit_purchse_doc_tree["columns"]=["1","2","3"]
    edit_purchse_doc_tree.column("#0", width=20)
    edit_purchse_doc_tree.column("1", width=250)
    edit_purchse_doc_tree.column("2", width=250)
    edit_purchse_doc_tree.column("2", width=200)
    edit_purchse_doc_tree.heading("#0",text="", anchor=W)
    edit_purchse_doc_tree.heading("1",text="Attach to Email")
    edit_purchse_doc_tree.heading("2",text="Filename")
    edit_purchse_doc_tree.heading("3",text="Filesize")  
    edit_purchse_doc_tree.place(x=50, y=45)

    fir4Frame=Frame(pop1,height=190,width=210,bg="#f5f3f2")
    fir4Frame.place(x=740,y=520)
    purch_summaryfrme = LabelFrame(fir4Frame,text="Summary",font=("arial",15))
    purch_summaryfrme.place(x=0,y=0,width=200,height=170)
    edit_discount=Label(purch_summaryfrme, text="Discount")
    edit_discount.place(x=0 ,y=0)
    edit_discount1=Label(purch_summaryfrme, text="$0.00")
    edit_discount1.place(x=130 ,y=0)
    edit_sub=Label(purch_summaryfrme, text="Subtotal")
    edit_sub.place(x=0 ,y=21)
    edit_sub1=Label(purch_summaryfrme, text="$0.00")
    edit_sub1.place(x=130 ,y=21)
    edit_tax=Label(purch_summaryfrme, text="Tax1")
    edit_tax.place(x=0 ,y=42)
    edit_tax1=Label(purch_summaryfrme, text="$0.00")
    edit_tax1.place(x=130 ,y=42)
    edit_taxx=Label(purch_summaryfrme, text="Tax2")
    edit_taxx.place(x=0 ,y=63)
    edit_tax2=Label(purch_summaryfrme, text="$0.00")
    edit_tax2.place(x=130 ,y=63)
    edit_cost=Label(purch_summaryfrme, text="Extra cost")
    edit_cost.place(x=0 ,y=84)
    edit_cost1=Label(purch_summaryfrme, text="$0.00")
    edit_cost1.place(x=130 ,y=84)
    edit_porder=Label(purch_summaryfrme, text="P.Order total")
    edit_porder.place(x=0 ,y=105)
    edit_porder1=Label(purch_summaryfrme, text="$0.00")
    edit_porder1.place(x=130 ,y=105)

    fir5Frame=Frame(pop1,height=38,width=210)
    fir5Frame.place(x=735,y=485)
    btndown=Button(fir5Frame, compound="left", text="Line Down").place(x=75, y=0)
    btnup=Button(fir5Frame, compound="left", text="Line Up").place(x=150, y=0)
    # try:
    #   sql5='SELECT * FROM porder WHERE porder_no=%s'
    #   val5=(itemid,)
    #   fbcursor.execute(sql5,val5,)
    #   new=fbcursor.fetchone()
      
    #   if new[5]=="Completed":
    #     print(new[4])
    #     for x in (edit_create, edit_add, edit_dele, edit_finalize):
    #       x.config(state = 'disabled')
    #     for y in(vender_combo,pmail,psms,pdate,pdue,pextra,pcost,pdisc,porder_tax4,porder_tax5):
    #       y.config(state = 'disabled')
    #     for z in (paddress,pdel_addr):
    #       z.config(state = 'disabled')
    #   else:
    #     pass
    # except:
    #   pass



   
   

  
  #################END OF VIEW/EDIT PORDER ###########


  #print selectede purchase order
  def printsele1():

    def proper1():
      propert=Toplevel()
      propert.title("Microsoft Print To PDF Advanced Document Settings")
      propert.geometry("670x500+240+150")

      def proper2():
        propert1=Toplevel()
        propert1.title("Microsoft Print To PDF Advanced Document Settings")
        propert1.geometry("670x500+240+150")

        name=Label(propert1, text="Microsoft Print To PDF Advanced Document Settings").place(x=10, y=5)
        paper=Label(propert1, text="Paper/Output").place(x=30, y=35)
        size=Label(propert1, text="Paper size").place(x=55, y=65)
        n = StringVar()
        search = ttk.Combobox(propert1, width = 15, textvariable = n )
        search['values'] = ('letter')
        search.place(x=150,y=65)
        search.current(0)
        copy=Label(propert1, text="Copy count:").place(x=55, y=95)

        okbtn=Button(propert1,compound = LEFT,image=tick , text="Ok", width=60).place(x=460, y=450)
        canbtn=Button(propert1,compound = LEFT,image=cancel, text="Cancel", width=60).place(x=570, y=450)
        


      style = ttk.Style()
      style.theme_use('default')
      style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
      property_Notebook = ttk.Notebook(propert)
      property_Frame = Frame(property_Notebook, height=500, width=670)
      property_Notebook.add(property_Frame, text="Layout")
      property_Notebook.place(x=0, y=0)

      name=Label(property_Frame, text="Orientation:").place(x=10, y=5)
      n = StringVar()
      search = ttk.Combobox(property_Frame, width = 23, textvariable = n )
      search['values'] = ('Portrait')
      search.place(x=10,y=25)
      search.current(0)

      text=Text(property_Frame,width=50).place(x=250, y=5,height=350)

      btn=Button(property_Frame, text="Advanced",command=proper2).place(x=550, y=380)
      btn=Button(property_Frame,compound = LEFT,image=tick, text="OK", width=60,).place(x=430, y=420)
      btn=Button(property_Frame,compound = LEFT,image=tick, text="Cancel", width=60,).place(x=550, y=420)     

        
    
    if(False):
        messagebox.showwarning("FBilling Revelution 2020", "Customer is required, Please select customer for this invoice\nbefore printing")
    elif(False):
        messagebox.showinfo("FBilling Revelution 2020", "Print job has been completed.")
    else:
        print1=Toplevel()
        print1.title("Print")
        print1.geometry("670x400+240+150")
        
        printerframe=LabelFrame(print1, text="Printer", height=80, width=650)
        printerframe.place(x=7, y=5)      
        name=Label(printerframe, text="Name:").place(x=10, y=5)
        e1= ttk.Combobox(printerframe, width=40).place(x=70, y=5)
        where=Label(printerframe, text="Where:").place(x=10, y=30)
        printocheckvar=IntVar()
        printochkbtn=Checkbutton(printerframe,text="Print to file",variable=printocheckvar,onvalue=1,offvalue=0,height=1,width=10)
        printochkbtn.place(x=450, y=30)
        btn=Button(printerframe, text="Properties", width=10,command=proper1).place(x=540, y=5)

        pageslblframe=LabelFrame(print1, text="Pages", height=140, width=320)
        pageslblframe.place(x=10, y=90)
        radvar=IntVar()
        radioall=Radiobutton(pageslblframe, text="All", variable=radvar, value="1").place(x=10, y=5)
        radiocpage=Radiobutton(pageslblframe, text="Current Page", variable=radvar, value="2").place(x=10, y=25)
        radiopages=Radiobutton(pageslblframe, text="Pages: ", variable=radvar, value="3").place(x=10, y=45)
        pagecountentry = Entry(pageslblframe, width=23).place(x=80, y=47)
        pageinfolabl=Label(pageslblframe, text="Enter page numbers and/or page ranges\nseperated by commas. For example:1,3,5-12")
        pageinfolabl.place(x=5, y=75)

        copylblframe=LabelFrame(print1, text="Copies", height=140, width=320)
        copylblframe.place(x=335, y=90)
        nolabl=Label(copylblframe, text="Number of copies").place(x=5, y=5)      
        noentry = Entry(copylblframe, width=18).place(x=130, y=5)      
        one=Frame(copylblframe, width=30, height=40, bg="black").place(x=20, y=40)     
        two=Frame(copylblframe, width=30, height=40, bg="grey").place(x=15, y=45)     
        three=Frame(copylblframe, width=30, height=40, bg="white").place(x=10, y=50)      
        four=Frame(copylblframe, width=30, height=40, bg="black").place(x=80, y=40)      
        fiv=Frame(copylblframe, width=30, height=40, bg="grey").place(x=75, y=45)      
        six=Frame(copylblframe, width=30, height=40, bg="white").place(x=70, y=50)      
        collatecheckvar=IntVar()
        collatechkbtn=Checkbutton(copylblframe,text="Collate",variable=collatecheckvar,onvalue=1,offvalue=0,height=1,width=10)
        collatechkbtn.place(x=130, y=70)

        othrlblframe=LabelFrame(print1, text="Other", height=120, width=320)
        othrlblframe.place(x=10, y=235)
        printlb=Label(othrlblframe, text="Print").place(x=5, y=0)
        dropprint = ttk.Combobox(othrlblframe, width=23).place(x=80, y=0)
        orderlb=Label(othrlblframe, text="Order").place(x=5, y=25)
        dropord = ttk.Combobox(othrlblframe, width=23).place(x=80, y=25)
        duplexlb=Label(othrlblframe, text="Duplex").place(x=5, y=50)
        droplex = ttk.Combobox(othrlblframe, width=23).place(x=80, y=50)

        prmodelblframe=LabelFrame(print1, text="Print mode", height=120, width=320)
        prmodelblframe.place(x=335, y=235)
        dropscal = ttk.Combobox(prmodelblframe, width=30).place(x=5, y=5)
        poslb=Label(prmodelblframe, text="Print on sheet").place(x=5, y=35)
        droppos = ttk.Combobox(prmodelblframe, width=10).place(x=155, y=35)

        okbtn=Button(print1,compound = LEFT,image=tick,text="Ok", width=60).place(x=460, y=370)
        canbtn=Button(print1,compound = LEFT,image=tick, text="Cancel", width=60).place(x=570, y=370)
        


  #email
        
  #----------------Create Email-----------------#

    def pord_send_mail_1():

      sender_email_1 = "sagarasagu49@gmail.com" #email_from.get()                                 
      sender_password_1 = "sagara21@sagu"        #email_pswrd.get() 

      server_1 = smtplib.SMTP('smtp.gmail.com', 587)
      print("Login successful1")
      server_1.starttls()
      print("Login successful2")
      server_1.login(sender_email_1, sender_password_1)
      print("Login successful3")
      carbcopy_info_1 = "krishnasanthosh101999@gmail.com"      #carcopyem_address.get()
      print(carbcopy_info_1)
      
      
      msg_1 = MIMEMultipart()
      msg_1['Subject'] = email_subject.get() 
      mail_content  = pordmemaiframe.get('1.0','end-1c') 
      msg_1['From'] = email_from.get()
      msg_1['To'] = pord_emailtoent.get()
      
      gettingimg=pordframe.get()
      print(gettingimg)
      lst_data = gettingimg[1:-1].split(',')
      print(lst_data,"happy")
      # print(gettingimg)
      msg_1.attach(MIMEText(mail_content, 'plain'))

      for i in lst_data:
        if len(i.strip()[1:-1])>1:
        # print(i[0],"IMAGE")
          with open('images/'+ i.strip()[1:-1], "rb") as attachment:
              # MIME attachment is a binary file for that content type "application/octet-stream" is used
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
          # encode into base64 
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % 'images/'+ i.strip()[1:-1]) 

        # attach the instance 'part' to instance 'message' 
            msg_1.attach(part)
        # message_body = email_body.get()

      server_1.sendmail(email_from.get(),pord_emailtoent.get(),msg_1.as_string())
      server_1.sendmail(email_from.get(), carbcopy_info_1,msg_1.as_string())
      print("message sent")
    def pord_empsfile_image_1(event):
      global yawn
      for i in  pord_htcodeframe.curselection():
        print("hloo", pord_htcodeframe.get(i))
        yawn= pord_htcodeframe.get(i)        
        edit_window_img = Toplevel()
        edit_window_img.title("View Image")
        edit_window_img.geometry("700x500")
        image = Image.open("images/"+yawn)
        resize_image = image.resize((700, 500))
        image = ImageTk.PhotoImage(resize_image)
        psimage = Label(edit_window_img,image=image)
        psimage.photo = image
        psimage.pack()

    def pord_UploadAction_1(event=None):
      global filenamez

      filenamez = askopenfilename(filetypes=(("png file ",'.png'),("jpg file", ".jpg"), ('PDF', '.pdf',), ("All files", ".*"),))
      shutil.copyfile(filenamez, os.getcwd()+'/images/'+filenamez.split('/')[-1])
      pord_htcodeframe.insert(0, filenamez.split('/')[-1])
  def addemail_porder():
    mailDetail=Toplevel()
    mailDetail.title("Porder E-Mail")
    mailDetail.geometry("1080x550")
    mailDetail.resizable(False, False)
    # def my_SMTP():
    #     if True:
    #         em_ser_conbtn.destroy()
    #         mysmtpservercon=LabelFrame(account_Frame,text="SMTP server connection(ask your ISP for your SMTP settings)", height=165, width=380)
    #         mysmtpservercon.place(x=610, y=110)
    #         lbl_hostn=Label(mysmtpservercon, text="Hostname").place(x=5, y=10)
    #         hostnent=Entry(mysmtpservercon, width=30).place(x=80, y=10)
    #         lbl_portn=Label(mysmtpservercon, text="Port").place(x=5, y=35)
    #         portent=Entry(mysmtpservercon, width=30).place(x=80, y=35)
    #         lbl_usn=Label(mysmtpservercon, text="Username").place(x=5, y=60)
    #         unament=Entry(mysmtpservercon, width=30).place(x=80, y=60)
    #         lbl_pasn=Label(mysmtpservercon, text="Password").place(x=5, y=85)
    #         pwdent=Entry(mysmtpservercon, width=30).place(x=80, y=85)
    #         ssl_chkvar=IntVar()
    #         ssl_chkbtn=Checkbutton(mysmtpservercon, variable=ssl_chkvar, text="This server requires a secure connection(SSL)", onvalue=1, offvalue=0)
    #         ssl_chkbtn.place(x=50, y=110)
    #         em_ser_conbtn1=Button(account_Frame, text="Test E-mail Server Connection").place(x=610, y=285)
    #     else:
    #         pass

  
    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    email_Notebook = ttk.Notebook(mailDetail)
    email_Frame = Frame(email_Notebook, height=500, width=1080)
    account_Frame = Frame(email_Notebook, height=550, width=1080)
    email_Notebook.add(email_Frame, text="E-mail")
    email_Notebook.add(account_Frame, text="Account")
    email_Notebook.place(x=0, y=0)

    messagelbframe=LabelFrame(email_Frame,text="Message", height=500, width=730)
    messagelbframe.place(x=5, y=5)
    global email_address, email_subject, email_from,email_pswrd,carcopyem_address,mframe,pord_htcodeframe,lstfrm,langs
    email_address = StringVar() 
    email_subject = StringVar()
    # email_body = StringVar()
    email_from = StringVar()
    email_pswrd = StringVar()
    carcopyem_address = StringVar()
    # content_email = StringVar()
    lbl_emailtoaddr=Label(messagelbframe, text="Email to address").place(x=5, y=5)
    emailtoent=Entry(messagelbframe, width=50,textvariable=email_address)
    emailtoent.place(x=120, y=5)
    # emailtoent.delete(0,'end')
    # emailtoent.insert(0, emailnow[23])
    #email2 = email_address.get()
    #print(email2)
    sendemail_btn=Button(messagelbframe, text="Send Email", width=10, height=1, command=pord_send_mail_1).place(x=600, y=10)#,command=addacnt

    lbl_carcopyto=Label(messagelbframe, text="Carbon copy to").place(x=5, y=32)
    carcopyent=Entry(messagelbframe, width=50,textvariable=carcopyem_address)
    carcopyent.place(x=120, y=32)
    # stopemail_btn=Button(messagelbframe, text="Stop sending", width=10, height=1).place(x=600, y=40)
    lbl_subject=Label(messagelbframe, text="Subject").place(x=5, y=59)
    subent=Entry(messagelbframe, width=50, textvariable=email_subject)
    subent.place(x=120, y=59)
    subjectinsrt='PORD_'+str()
    # 
    

    
    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
    mess_Notebook = ttk.Notebook(messagelbframe)
    emailmessage_Frame =Frame(mess_Notebook, height=350, width=710)
    htmlsourse_Frame = Frame(mess_Notebook, height=350, width=710)
    mess_Notebook.add(emailmessage_Frame, text="E-mail message")
    mess_Notebook=Entry(emailmessage_Frame, width=710,height=350, textvariable=email_subject)
    mess_Notebook.place(x=120, y=59)
    mess_Notebook.add(htmlsourse_Frame, )#text="Html source code")
    mess_Notebook.place(x=5, y=90)

    # btn1=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)

    
    # btn2=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
    # btn3=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
    # btn4=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
    # btn5=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo).place(x=140, y=1)
    # btn6=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo).place(x=175, y=1)
    # btn7=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold).place(x=210, y=1)
    # btn8=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics).place(x=245, y=1)
    # btn9=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline).place(x=280, y=1)
    # btn10=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=left).place(x=315, y=1)
    # btn11=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=right).place(x=350, y=1)
    # btn12=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=center).place(x=385, y=1)
    # btn13=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink).place(x=420, y=1)
    
    # btn14=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove).place(x=455, y=1)


    # dropcomp = ttk.Combobox(emailmessage_Frame, width=12, height=3).place(x=500, y=5)
    # dropcompo = ttk.Combobox(emailmessage_Frame, width=6, height=3).place(x=600, y=5)
    mframe=scrolledtext.Text(emailmessage_Frame,  undo=True,width=88, bg="white", height=22)
    mframe.place(x=0, y=10)
    # mess_Notebook=Entry(emailmessage_Frame, width=710,height=350, textvariable=email_subject)
    # mess_Notebook.place(x=120, y=59)


    # btn1=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)

    
    # btn2=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
    # btn3=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
    # btn4=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
    # mframe1=Frame(htmlsourse_Frame, height=350, width=710, bg="white")
    # mframe1.place(x=0, y=28)
    attachlbframe=LabelFrame(email_Frame,text="Attachment(s)", height=350, width=280)
    attachlbframe.place(x=740, y=5)
    # langs=[]
    lstfrm=StringVar()  
    pord_htcodeframe=Listbox(attachlbframe, height=13, width=43,listvariable=lstfrm, bg="white")
    pord_htcodeframe.place(x=5, y=5)
    pord_htcodeframe.bind('<Double-Button-1>', pord_empsfile_image_1)

    def deslist():
        laa=pord_htcodeframe.curselection()
        print("hloo",pord_htcodeframe.get(laa))
        yawn=pord_htcodeframe.get(laa)        
        pord_htcodeframe.delete(ACTIVE)

    lbl_btn_info=Label(attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
    btn17=Button(attachlbframe, width=20, text="Add attachment file...", command=UploadAction).place(x=60, y=260)
    btn18=Button(attachlbframe, width=20, text="Remove attachment",command=deslist).place(x=60, y=295)
    lbl_tt_info=Label(email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
    lbl_tt_info.place(x=740, y=370)

    ready_frame=Frame(mailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
    
    sendatalbframe=LabelFrame(account_Frame,text="E-Mail(Sender data)",height=140, width=600)
    sendatalbframe.place(x=5, y=5)
    lbl_sendermail=Label(sendatalbframe, text="Company email address").place(x=5, y=10)
    sentent=Entry(sendatalbframe, width=40, textvariable=email_from)
    sentent.place(x=195, y=10)
    #############################################
    lbl_senderpswrd=Label(sendatalbframe, text="Email Password").place(x=5, y=40)
    pswrdent=Entry(sendatalbframe, width=40, textvariable=email_pswrd,show="*")
    pswrdent.place(x=195, y=40)  

  def addacnt():  
    messagebox.showinfo("F-Billing Revolution 2022", "No sender email address.\nPlease fill Your company email address textfield under the Account tab.")

  def savesettings():  
    messagebox.showinfo("F-Billing Revolution 2022", "Your E-mail configuration settings has been saved.")



  # sms notification order
    
  def sms():
    send_SMS=Toplevel()
    send_SMS.geometry("700x480+240+150")
    send_SMS.title("Send SMS notification")

    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    sms_Notebook = ttk.Notebook(send_SMS)
    SMS_Notification = Frame(sms_Notebook, height=470, width=700)
    SMS_Service_Account = Frame(sms_Notebook, height=470, width=700)
    sms_Notebook.add(SMS_Notification, text="SMS Notification")
    sms_Notebook.add(SMS_Service_Account, text="SMS Service Account")
    sms_Notebook.place(x=0, y=0)

    numlbel=Label(SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
    numlbel.place(x=10, y=10)
    numentry=Entry(SMS_Notification, width=92).place(x=10, y=30)
    stexbel=Label(SMS_Notification, text="SMS Text").place(x=10, y=60)
    stex=Entry(SMS_Notification, width=40).place(x=10, y=85,height=120)
    
    dclbel=Label(SMS_Notification, text="Double click to insert into text")
    dclbel.place(x=410, y=60)
    dcl=Entry(SMS_Notification, width=30)
    dcl.place(x=400, y=85,height=200)
    
    smstype=LabelFrame(SMS_Notification, text="SMS message type", width=377, height=60)
    smstype.place(x=10, y=223)
    snuvar=IntVar()
    normal_rbtn=Radiobutton(smstype, text="Normal SMS(160 chars)", variable=snuvar, value=1)
    normal_rbtn.place(x=5, y=5)
    unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)", variable=snuvar, value=2)
    unicode_rbtn.place(x=190, y=5)
    tiplbf=LabelFrame(SMS_Notification, text="Tips", width=680, height=120)
    tiplbf.place(x=10, y=290)
    tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="Always start the SMS nymber with the country code. Do not use the + sign at the beginning(example\nUS number:8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
    tiplabl.place(x=5, y=5)

    btn1=Button(SMS_Notification, width=20, text="Send SMS notification").place(x=10, y=420)
    btn2=Button(SMS_Notification, width=25, text="Confirm SMS cost before sending").place(x=280, y=420)
    btn3=Button(SMS_Notification, width=15, text="Cancel").place(x=550, y=420)
    

    smstype=LabelFrame(SMS_Service_Account, text="Select the notification service provider", width=670, height=65)
    smstype.place(x=10, y=5)
    snumvar=IntVar()
    normal_rbtn=Radiobutton(smstype,text="BULKSMS(www.bulksms.com)",variable=snumvar,value=1,)
    normal_rbtn.place(x=5, y=5)
    unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)-Recommended", variable=snumvar, value=2)
    unicode_rbtn.place(x=290, y=5)

    sms1type=LabelFrame(SMS_Service_Account, text="Your BULKSMS.COM Account", width=670, height=100)
    sms1type.place(x=10, y=80)
    name=Label(sms1type, text="Username").place(x=10, y=5)
    na=Entry(sms1type, width=20).place(x=100, y=5)
    password=Label(sms1type, text="Password").place(x=10, y=45)
    pas=Entry(sms1type, width=20).place(x=100, y=45)
    combo=Label(sms1type, text="Route").place(x=400, y=5)
    n = StringVar()
    combo1 = ttk.Combobox(sms1type, width = 20, textvariable = n ).place(x=450,y=5)
    btn1=Button(sms1type, width=10, text="Save settings").place(x=550, y=45)

    
    tiplbf=LabelFrame(SMS_Service_Account, text="Terms of service", width=680, height=250)
    tiplbf.place(x=10, y=190)
    tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
    tiplabl.place(x=0, y=5)
    tiplabl1=Label(tiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
    tiplabl1.place(x=0, y=60)
    tiplabl2=Label(tiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
    tiplabl2.place(x=0, y=100)
    tiplabl3=Label(tiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
    tiplabl3.place(x=0, y=140)
    checkvar1=IntVar()
    chkbtn1=Checkbutton(tiplbf,text="I have read and agree to the terms of service above",variable=checkvar1,onvalue=1,offvalue=0).place(x=70, y=200)  

  def printpreview():
    messagebox.showerror("F-Billing Revolution","Customer is required,please select customer for this order before printing.")


  #delete orders  
  def dele():  
    delmess = messagebox.askyesno("Delete Porder", "Are you sure to delete this Porder?")
    if delmess == True:
      itemid = purch_tree.item(purch_tree.focus())["values"][1]
      # print(itemid,)
      sql = 'DELETE FROM porder WHERE porder_no=%s'
      val = (itemid,)
      fbcursor.execute(sql, val)
      fbilldb.commit()

      # purch_tree.delete(purch_tree.selection()[0])
      # sqlstrngprdct='DELETE FROM storingproduct WHERE pord_no=%s'
      # valstpr = (itemid,)
      # fbcursor.execute(sqlstrngprdct, valstpr)
      # fbilldb.commit()

      # sqldoc='DELETE FROM documents WHERE pord_no=%s'
      # valdoc = (itemid,)
      # fbcursor.execute(sqldoc, valdoc)
      # fbilldb.commit()

      # notepriv.delete('1.0','end')
      # for record in purch_tree.get_children():
      #   purch_tree.delete(record)
      # for record in treeblw.get_children():
      #   treeblw.delete(record)
      sql = "SELECT * FROM porder"
      fbcursor.execute(sql,)
      
      a=0
      j = 0
      for i in fbcursor:
        pord_tree.insert(parent='', index='end', iid=i, text='', values=(' ',i[39], i[2], i[3], i[25],i[5], i[6], i[7], i[8], i[9]))
        for line in pord_tree.get_children():
          idsave=pord_tree.item(line)['values'][9]
        a+=idsave
      j += 1
      pordtotalrowcol.config(text=a)
    else:
      pass



  #search in orders  
  def search():
    def find_cus_row():
      print(find_txt_var.get())
      if find_txt_var.get()=="P.Order#":
        fnd_sql="select * from porder where porder_no=%s"
        fnd_sql_val=(fnd_srh_txt.get(),)
        fbcursor.execute(fnd_sql,fnd_sql_val)
        htj=fbcursor.fetchall()
        for record in pord_tree.get_children():
          pord_tree.delete(record)
        count_cus=0

        for i in htj:
          
          pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=(' ',i[39], i[2], i[3], i[25],i[5], i[6], i[7], i[8], i[9], i[10]))
          count_cus +=1
        top.destroy()
      elif find_txt_var.get()=="Order date":
        fnd_sql="select * from porder where porderdate=%s"
        fnd_sql_val=(fnd_srh_txt.get(),)
        fbcursor.execute(fnd_sql,fnd_sql_val)
        htj=fbcursor.fetchall()
        for record in pord_tree.get_children():
          pord_tree.delete(record)
        count_cus=0

        for i in htj:
        
          pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=(' ',i[39], i[2], i[3], i[25],i[5], i[6], i[7], i[8], i[9], i[10]))
          count_cus +=1
        top.destroy()
      elif find_txt_var.get()=="Due date":
        fnd_sql="select * from porder where duedate=%s"
        fnd_sql_val=(fnd_srh_txt.get(),)
        fbcursor.execute(fnd_sql,fnd_sql_val)
        htj=fbcursor.fetchall()
        for record in pord_tree.get_children():
          pord_tree.delete(record)
        count_cus=0

        for i in htj:
        
          pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=(' ',i[39], i[2], i[3], i[25],i[5], i[6], i[7], i[8], i[9], i[10]))
          count_cus +=1
        top.destroy()
      elif find_txt_var.get()=="Customer Name":
        fnd_sql="select * from porder where businessname=%s"
        fnd_sql_val=(fnd_srh_txt.get(),)
        fbcursor.execute(fnd_sql,fnd_sql_val)
        htj=fbcursor.fetchall()
        for record in pord_tree.get_children():
          pord_tree.delete(record)
        count_cus=0

        for i in htj:
          
          pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=(' ',i[39], i[2], i[3], i[25],i[5], i[6], i[7], i[8], i[9], i[10]))
          count_cus +=1
        top.destroy()
      elif find_txt_var.get()=="Status":
        fnd_sql="select * from porder where 	status=%s"
        fnd_sql_val=(fnd_srh_txt.get(),)
        fbcursor.execute(fnd_sql,fnd_sql_val)
        htj=fbcursor.fetchall()
        for record in pord_tree.get_children():
          pord_tree.delete(record)
        count_cus=0

        for i in htj:
          
          pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=(' ',i[39], i[2], i[3], i[25],i[5], i[6], i[7], i[8], i[9], i[10]))
          count_cus +=1
        top.destroy()
      elif find_txt_var.get()=="Emailed on":
        fnd_sql="select * from porder where emailon=%s"
        fnd_sql_val=(fnd_srh_txt.get(),)
        fbcursor.execute(fnd_sql,fnd_sql_val)
        htj=fbcursor.fetchall()
        for record in pord_tree.get_children():
          pord_tree.delete(record)
        count_cus=0

        for i in htj:
          
          pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=(' ',i[39], i[2], i[3], i[25],i[5], i[6], i[7], i[8], i[9], i[10]))
          count_cus +=1
        top.destroy()
      elif find_txt_var.get()=="Printed on":
        fnd_sql="select * from porder where 	printon=%s"
        fnd_sql_val=(fnd_srh_txt.get(),)
        fbcursor.execute(fnd_sql,fnd_sql_val)
        htj=fbcursor.fetchall()
        for record in pord_tree.get_children():
          pord_tree.delete(record)
        count_cus=0

        for i in htj:
          
          pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=(' ',i[39], i[2], i[3], i[25],i[5], i[6], i[7], i[8], i[9], i[10]))
          count_cus +=1
        top.destroy()
      elif find_txt_var.get()=="SMS on":
        fnd_sql="select * from porder where 	smson=%s"
        fnd_sql_val=(fnd_srh_txt.get(),)
        fbcursor.execute(fnd_sql,fnd_sql_val)
        htj=fbcursor.fetchall()
        for record in pord_tree.get_children():
          pord_tree.delete(record)
        count_cus=0

        for i in htj:
          
          pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=(' ',i[39], i[2], i[3], i[25],i[5], i[6], i[7], i[8], i[9], i[10]))
          count_cus +=1
        top.destroy()
      elif find_txt_var.get()=="Order Total":
        fnd_sql="select * from porder where 	ordertot=%s"
        fnd_sql_val=(fnd_srh_txt.get(),)
        fbcursor.execute(fnd_sql,fnd_sql_val)
        htj=fbcursor.fetchall()
        for record in pord_tree.get_children():
          pord_tree.delete(record)
        count_cus=0

        for i in htj:
          
          pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=(' ',i[39], i[2], i[3], i[25],i[5], i[6], i[7], i[8], i[9], i[10]))
          count_cus +=1
        top.destroy()  

      elif find_txt_var.get()=="<<All>>":
        fnd_sql="select * from customer"
        fnd_sql_val=(fnd_srh_txt.get(),)
        fbcursor.execute(fnd_sql,fnd_sql_val)
        htj=fbcursor.fetchall()
        for record in pord_tree.get_children():
          pord_tree.delete(record)
        count_cus=0

        for i in htj:
          
          pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=(' ',i[39], i[2], i[3], i[25],i[5], i[6], i[7], i[8], i[9], i[10]))
          count_cus +=1
        top.destroy()
    def fnd_dist():
      top.destroy()

    top = Toplevel()  
    top.title("Find Text")
    p2 = PhotoImage(file = "images/fbicon.png")
    top.iconphoto(False, p2)
    top.geometry("520x150+390+250")
    findwhat1=Label(top,text="Find What:")
    findwhat1.place(x=5,y=15)
    fnd_srh_txt = StringVar() 
    findwhat = ttk.Combobox(top, width = 50, textvariable = fnd_srh_txt )
    findwhat.place(x=85,y=15,height=23) 
    findButton = Button(top, text ="Find next",width=10, command=lambda:find_cus_row())
    findButton.place(x=420,y=15)
    findin1=Label(top,text="Find in:")
    findin1.place(x=5,y=40)
    find_txt_var = StringVar() 
    findIN = ttk.Combobox(top, width = 37, textvariable =find_txt_var )
    findIN['values'] = ('P.Order#',  
                              'Order date', 
                              'Due date', 
                              'Customer Name', 
                              'Status', 
                              'Emailed on',
                              'Printed on',
                              'SMS on',
                              'Order Total',
                              '<<All>>')        
    findIN.place(x=85,y=40,height=23) 
    findIN.current(0)
    closeButton = Button(top, text ="Close",width=10, command=lambda:fnd_dist())
    closeButton.place(x=420,y=45)
   
    up_var = StringVar() 
    checkvarStatus4=IntVar()
    Button4 = Checkbutton(top,variable = checkvarStatus4, 
                      text="Match Case", 
                      onvalue =0 ,
                      offvalue = 1,
                      height=3,
                      width = 15)
    Button4.select()
    Button4.place(x=60,y=80)
    checkvarStatus5=IntVar()  
    Button5 = Checkbutton(top,variable = checkvarStatus5, 
                      text="Match Format", 
                      onvalue =0 ,
                      offvalue = 1,
                      height=3,
                      width = 15)
    Button5.select()
    Button5.place(x=270,y=80)
    top.mainloop()







    # def find_cus_row():
    #   print(find_txt_var.get())
    #   if find_txt_var.get()=="P.Order#":
    #     fnd_sql="select * from porder where porder_no=%s"
    #     fnd_sql_val=(fnd_srh_txt.get(),)
    #     fbcursor.execute(fnd_sql,fnd_sql_val)
    #     htj=fbcursor.fetchall()
    #     for record in pord_tree.get_children():
    #       pord_tree.delete(record)
    #     count_cus=0

    #     for i in htj:
          
    #       pord_tree.insert(parent='', index='end', iid=count_cus,text='hello', values=("",i[39],i[2],i[3],i[25],i[5],i[6],i[7], i[8], i[9]))
    #       count_cus +=1
    #     top.destroy()
    #   elif find_txt_var.get()=="Order date":
    #     fnd_sql="select * from porder where porderdate=%s"
    #     fnd_sql_val=(fnd_srh_txt.get(),)
    #     fbcursor.execute(fnd_sql,fnd_sql_val)
    #     htj=fbcursor.fetchall()
    #     for record in pord_tree.get_children():
    #       pord_tree.delete(record)
    #     count_cus=0

    #     for i in htj:
          
    #       pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=("",i[39],i[2],i[3],i[25],i[5],i[6],i[7], i[8], i[9]))
    #       count_cus +=1
    #     top.destroy()
    #   elif find_txt_var.get()=="Due date":
    #     fnd_sql="select * from porder where duedate=%s"
    #     fnd_sql_val=(fnd_srh_txt.get(),)
    #     fbcursor.execute(fnd_sql,fnd_sql_val)
    #     htj=fbcursor.fetchall()
    #     for record in pord_tree.get_children():
    #       pord_tree.delete(record)
    #     count_cus=0

    #     for i in htj:
            
    #       pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=("",i[39],i[2],i[3],i[25],i[5],i[6],i[7], i[8], i[9]))
    #       count_cus +=1
    #     top.destroy()
    #   elif find_txt_var.get()=="Customer Name":
    #     fnd_sql="select * from porder where businessname=%s"
    #     fnd_sql_val=(fnd_srh_txt.get(),)
    #     fbcursor.execute(fnd_sql,fnd_sql_val)
    #     htj=fbcursor.fetchall()
    #     for record in pord_tree.get_children():
    #       pord_tree.delete(record)
    #     count_cus=0

    #     for i in htj:
            
    #       pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=("",i[39],i[2],i[3],i[25],i[5],i[6],i[7], i[8], i[9]))
    #       count_cus +=1
    #     top.destroy()
    #   elif find_txt_var.get()=="Status":
    #     fnd_sql="select * from porder where status=%s"
    #     fnd_sql_val=(fnd_srh_txt.get(),)
    #     fbcursor.execute(fnd_sql,fnd_sql_val)
    #     htj=fbcursor.fetchall()
    #     for record in pord_tree.get_children():
    #       pord_tree.delete(record)
    #     count_cus=0

    #     for i in htj:
            
    #       pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=("",i[39],i[2],i[3],i[25],i[5],i[6],i[7], i[8], i[9]))
    #       count_cus +=1
    #     top.destroy()
      
    #   elif find_txt_var.get()=="Emailed on":
    #     fnd_sql="select * from porder where emailon=%s"
    #     fnd_sql_val=(fnd_srh_txt.get(),)
    #     fbcursor.execute(fnd_sql,fnd_sql_val)
    #     htj=fbcursor.fetchall()
    #     for record in pord_tree.get_children():
    #       pord_tree.delete(record)
    #     count_cus=0

    #     for i in htj:
            
    #       pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=("",i[39],i[2],i[3],i[25],i[5],i[6],i[7], i[8], i[9]))
    #       count_cus +=1
    #     top.destroy()
    #   elif find_txt_var.get()=="Printed on":
    #     fnd_sql="select * from porder where printon=%s"
    #     fnd_sql_val=(fnd_srh_txt.get(),)
    #     fbcursor.execute(fnd_sql,fnd_sql_val)
    #     htj=fbcursor.fetchall()
    #     for record in pord_tree.get_children():
    #       pord_tree.delete(record)
    #     count_cus=0

    #     for i in htj:
            
    #       pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=("",i[39],i[2],i[3],i[25],i[5],i[6],i[7], i[8], i[9]))
    #       count_cus +=1
    #     top.destroy()  
    #   elif find_txt_var.get()=="SMS on":
    #     fnd_sql="select * from porder where smson=%s"
    #     fnd_sql_val=(fnd_srh_txt.get(),)
    #     fbcursor.execute(fnd_sql,fnd_sql_val)
    #     htj=fbcursor.fetchall()
    #     for record in pord_tree.get_children():
    #       pord_tree.delete(record)
    #     count_cus=0

    #     for i in htj:
            
    #       pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=("",i[39],i[2],i[3],i[25],i[5],i[6],i[7], i[8], i[9]))
    #       count_cus +=1
    #     top.destroy()   
    #   elif find_txt_var.get()=="Porder Total":
    #     fnd_sql="select * from porder where 	ordertot=%s"
    #     fnd_sql_val=(fnd_srh_txt.get(),)
    #     fbcursor.execute(fnd_sql,fnd_sql_val)
    #     htj=fbcursor.fetchall()
    #     for record in pord_tree.get_children():
    #       pord_tree.delete(record)
    #     count_cus=0

    #     for i in htj:
          
    #       pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=(' ',i[39], i[2], i[3], i[25],i[5], i[6], i[7], i[8], i[9], i[10]))
    #       count_cus +=1
    #     top.destroy()  

    #   elif find_txt_var.get()=="<<All>>":
    #     fnd_sql="select * from porder"
    #     fnd_sql_val=(fnd_srh_txt.get(),)
    #     fbcursor.execute(fnd_sql,fnd_sql_val)
    #     htj=fbcursor.fetchall()
    #     for record in pord_tree.get_children():
    #       pord_tree.delete(record)
    #     count_cus=0

    #     for i in htj:
          
    #       pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=(' ',i[39], i[2], i[3], i[25],i[5], i[6], i[7], i[8], i[9], i[10]))
    #       count_cus +=1
    #     top.destroy()
    # def fnd_dist():
    #   top.destroy()

    # top = Toplevel()  
    # top.title("Find Text")
    # p2 = PhotoImage(file = "images/fbicon.png")
    # top.iconphoto(False, p2)
    # top.geometry("520x150+390+250")
    # findwhat1=Label(top,text="Find What:")
    # findwhat1.place(x=5,y=15)
    # fnd_srh_txt = StringVar() 
    # findwhat = ttk.Combobox(top, width = 50, textvariable = fnd_srh_txt )
    # findwhat.place(x=85,y=15,height=23) 
    # findButton = Button(top, text ="Find next",width=10, command=lambda:find_cus_row())
    # findButton.place(x=420,y=15)
    # findin1=Label(top,text="Find in:")
    # findin1.place(x=5,y=40)
    # find_txt_var = StringVar() 
    # findIN = ttk.Combobox(top, width = 37, textvariable =find_txt_var )
    # findIN['values'] = ('P.Order#',  
    #                           'Order date', 
    #                           'Due date', 
                           
    #                           'Customer Name', 
    #                           'Status', 
    #                           'Emailed on',
    #                           'Printed on',
    #                           'SMS on',
    #                           'Order Total',
    #                           '<<All>>')    
    # findIN.place(x=85,y=40,height=23) 
    # findIN.current(0)
    # closeButton = Button(top, text ="Close",width=10, command=lambda:fnd_dist())
    # closeButton.place(x=420,y=45)
   
    # up_var = StringVar() 
    # checkvarStatus4=IntVar()
    # Button4 = Checkbutton(top,variable = checkvarStatus4, 
    #                   text="Match Case", 
    #                   onvalue =0 ,
    #                   offvalue = 1,
    #                   height=3,
    #                   width = 15)
    # Button4.select()
    # Button4.place(x=60,y=80)
    # checkvarStatus5=IntVar()  
    # Button5 = Checkbutton(top,variable = checkvarStatus5, 
    #                   text="Match Format", 
    #                   onvalue =0 ,
    #                   offvalue = 1,
    #                   height=3,
    #                   width = 15)
    # Button5.select()
    # Button5.place(x=270,y=80)
    # top.mainloop()







    # def find_cus_row():
    #   print(find_txt_var.get())
    #   if find_txt_var.get()=="P.Order#":
    #     fnd_sql="select * from porder where porder_no=%s"
    #     fnd_sql_val=(fnd_srh_txt.get(),)
    #     fbcursor.execute(fnd_sql,fnd_sql_val)
    #     htj=fbcursor.fetchall()
    #     for record in pord_tree.get_children():
    #       pord_tree.delete(record)
    #     count_cus=0

    #     for i in htj:
          
    #       pord_tree.insert(parent='', index='end', iid=count_cus,text='hello', values=("",i[39],i[2],i[3],i[25],i[5],i[6],i[7], i[8], i[9]))
    #       count_cus +=1
    #     top.destroy()
    #   elif find_txt_var.get()=="Order date":
    #     fnd_sql="select * from porder where porderdate=%s"
    #     fnd_sql_val=(fnd_srh_txt.get(),)
    #     fbcursor.execute(fnd_sql,fnd_sql_val)
    #     htj=fbcursor.fetchall()
    #     for record in pord_tree.get_children():
    #       pord_tree.delete(record)
    #     count_cus=0

    #     for i in htj:
          
    #       pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=("",i[39],i[2],i[3],i[25],i[5],i[6],i[7], i[8], i[9]))
    #       count_cus +=1
    #     top.destroy()
    #   elif find_txt_var.get()=="Due date":
    #     fnd_sql="select * from porder where duedate=%s"
    #     fnd_sql_val=(fnd_srh_txt.get(),)
    #     fbcursor.execute(fnd_sql,fnd_sql_val)
    #     htj=fbcursor.fetchall()
    #     for record in pord_tree.get_children():
    #       pord_tree.delete(record)
    #     count_cus=0

    #     for i in htj:
            
    #       pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=("",i[39],i[2],i[3],i[25],i[5],i[6],i[7], i[8], i[9]))
    #       count_cus +=1
    #     top.destroy()
    #   elif find_txt_var.get()=="Customer Name":
    #     fnd_sql="select * from porder where businessname=%s"
    #     fnd_sql_val=(fnd_srh_txt.get(),)
    #     fbcursor.execute(fnd_sql,fnd_sql_val)
    #     htj=fbcursor.fetchall()
    #     for record in pord_tree.get_children():
    #       pord_tree.delete(record)
    #     count_cus=0

    #     for i in htj:
            
    #       pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=("",i[39],i[2],i[3],i[25],i[5],i[6],i[7], i[8], i[9]))
    #       count_cus +=1
    #     top.destroy()
    #   elif find_txt_var.get()=="Status":
    #     fnd_sql="select * from porder where status=%s"
    #     fnd_sql_val=(fnd_srh_txt.get(),)
    #     fbcursor.execute(fnd_sql,fnd_sql_val)
    #     htj=fbcursor.fetchall()
    #     for record in pord_tree.get_children():
    #       pord_tree.delete(record)
    #     count_cus=0

    #     for i in htj:
            
    #       pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=("",i[39],i[2],i[3],i[25],i[5],i[6],i[7], i[8], i[9]))
    #       count_cus +=1
    #     top.destroy()
      
    #   elif find_txt_var.get()=="Emailed on":
    #     fnd_sql="select * from porder where emailon=%s"
    #     fnd_sql_val=(fnd_srh_txt.get(),)
    #     fbcursor.execute(fnd_sql,fnd_sql_val)
    #     htj=fbcursor.fetchall()
    #     for record in pord_tree.get_children():
    #       pord_tree.delete(record)
    #     count_cus=0

    #     for i in htj:
            
    #       pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=("",i[39],i[2],i[3],i[25],i[5],i[6],i[7], i[8], i[9]))
    #       count_cus +=1
    #     top.destroy()
    #   elif find_txt_var.get()=="Printed on":
    #     fnd_sql="select * from porder where printon=%s"
    #     fnd_sql_val=(fnd_srh_txt.get(),)
    #     fbcursor.execute(fnd_sql,fnd_sql_val)
    #     htj=fbcursor.fetchall()
    #     for record in pord_tree.get_children():
    #       pord_tree.delete(record)
    #     count_cus=0

    #     for i in htj:
            
    #       pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=("",i[39],i[2],i[3],i[25],i[5],i[6],i[7], i[8], i[9]))
    #       count_cus +=1
    #     top.destroy()  
    #   elif find_txt_var.get()=="SMS on":
    #     fnd_sql="select * from porder where smson=%s"
    #     fnd_sql_val=(fnd_srh_txt.get(),)
    #     fbcursor.execute(fnd_sql,fnd_sql_val)
    #     htj=fbcursor.fetchall()
    #     for record in pord_tree.get_children():
    #       pord_tree.delete(record)
    #     count_cus=0

    #     for i in htj:
            
    #       pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=("",i[39],i[2],i[3],i[25],i[5],i[6],i[7], i[8], i[9]))
    #       count_cus +=1
    #     top.destroy()   
    #   elif find_txt_var.get()=="Order Total":
    #     fnd_sql="select * from porder where 	ordertot=%s"
    #     fnd_sql_val=(fnd_srh_txt.get(),)
    #     fbcursor.execute(fnd_sql,fnd_sql_val)
    #     htj=fbcursor.fetchall()
    #     for record in pord_tree.get_children():
    #       pord_tree.delete(record)
    #     count_cus=0

    #     for i in htj:
          
    #       pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=(' ',i[39], i[2], i[3], i[25],i[5], i[6], i[7], i[8], i[9], i[10]))
    #       count_cus +=1
    #     top.destroy()  
    #   elif find_txt_var.get()=="<<All>>":
    #     fnd_sql="select * from porder"
    #     fnd_sql_val=(fnd_srh_txt.get(),)
    #     fbcursor.execute(fnd_sql,fnd_sql_val)
    #     htj=fbcursor.fetchall()
    #     for record in pord_tree.get_children():
    #       pord_tree.delete(record)
    #     count_cus=0

    #     for i in htj:
            
    #       pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=("",i[39],i[2],i[3],i[25],i[5],i[6],i[7], i[8], i[9]))
    #       count_cus +=1
    #     top.destroy()
    #   def fnd_dist():
    #     top.destroy()

    #     top = Toplevel()  
    #     top.title("Find Text")
    #     p2 = PhotoImage(file = "images/fbicon.png")
    #     top.iconphoto(False, p2)
    #     top.geometry("520x150+390+250")
    #     findwhat1=Label(top,text="Find What:")
    #     findwhat1.place(x=5,y=15)
    #     fnd_srh_txt = StringVar() 
    #     findwhat = ttk.Combobox(top, width = 50, textvariable = fnd_srh_txt )
    #     findwhat.place(x=85,y=15,height=23) 
    #     findButton = Button(top, text ="Find next",width=10, command=lambda:find_cus_row())
    #     findButton.place(x=420,y=15)
    #     findin1=Label(top,text="Find in:")
    #     findin1.place(x=5,y=40)
    #     find_txt_var = StringVar() 
    #     findIN = ttk.Combobox(top, width = 37, textvariable =find_txt_var )
    #     findIN['values'] = ('P.Order#',  
    #                               'Order date', 
    #                               'Due date', 
                              
    #                               'Contact Person', 
    #                               'Customer Tel.', 
    #                               'SMS number',
    #                               'Type',
    #                               '<<All>>')    
    #     findIN.place(x=85,y=40,height=23) 
    #     findIN.current(0)
    #     closeButton = Button(top, text ="Close",width=10, command=lambda:fnd_dist())
    #     closeButton.place(x=420,y=45)
      
    #     up_var = StringVar() 
    #     checkvarStatus4=IntVar()
    #     Button4 = Checkbutton(top,variable = checkvarStatus4, 
    #                       text="Match Case", 
    #                       onvalue =0 ,
    #                       offvalue = 1,
    #                       height=3,
    #                       width = 15)
    #     Button4.select()
    #     Button4.place(x=60,y=80)
    #     checkvarStatus5=IntVar()  
    #     Button5 = Checkbutton(top,variable = checkvarStatus5, 
    #                       text="Match Format", 
    #                       onvalue =0 ,
    #                       offvalue = 1,
    #                       height=3,
    #                       width = 15)
    #     Button5.select()
    #     Button5.place(x=270,y=80)
    #     top.mainloop()  

      # top = Toplevel()     
      # top.title("Find Text")   
      # top.geometry("600x250+390+250")
      # findwhat1=Label(top,text="Find What:",pady=5,padx=10).place(x=5,y=20)
      # n = StringVar()
      # findwhat = ttk.Combobox(top, width = 40, textvariable = n ).place(x=90,y=25)
    
      # findin1=Label(top,text="Find in:",pady=5,padx=10).place(x=5,y=47)
      # n = StringVar()
      # findIN = ttk.Combobox(top, width = 30, textvariable = n )
      # findIN['values'] = ('Product/Service id', ' Category', ' Active',' name',' stock',' location', ' image',' <<All>>')                       
      # findIN.place(x=90,y=54)
      # findIN.current(0)

      # findButton = Button(top, text ="Find next",width=10).place(x=480,y=22)
      # closeButton = Button(top,text ="Close",width=10).place(x=480,y=52)
      
      # match1=Label(top,text="Match:",pady=5,padx=10).place(x=5,y=74)
      # n = StringVar()
      # match = ttk.Combobox(top, width = 23, textvariable = n )   
      # match['values'] = ('From Any part',' Whole Field',' From the beginning of the field')                                   
      # match.place(x=90,y=83)
      # match.current(0)

      # search1=Label(top,text="Search:",pady=5,padx=10).place(x=5,y=102)
      # n = StringVar()
      # search = ttk.Combobox(top, width = 23, textvariable = n )
      # search['values'] = ('All', 'up',' Down')
      # search.place(x=90,y=112)
      # search.current(0)
      # checkvarStatus4=IntVar()  
      # Button4 = Checkbutton(top,variable = checkvarStatus4,text="Match Case",onvalue =0 ,offvalue = 1,height=3,width = 15)
      # Button4.place(x=90,y=141)
      # checkvarStatus5=IntVar()   
      # Button5 = Checkbutton(top,variable = checkvarStatus5,text="Match Format",onvalue =0 ,offvalue = 1,height=3,width = 15)
      # Button5.place(x=300,y=141)


  purch_mainFrame=Frame(tab5, relief=GROOVE, bg="#f8f8f2")
  purch_mainFrame.pack(side="top", fill=BOTH)

  purch_midFrame=Frame(purch_mainFrame, bg="#f5f3f2", height=60)
  purch_midFrame.pack(side="top", fill=X)


  def refreshbttn():
    for record in pord_tree.get_children():
      pord_tree.delete(record)
    fbcursor.execute("select * from porder")
    pandsdata = fbcursor.fetchall()
    rfrs=0
    countp = 0
    for i in pandsdata:
      pord_tree.insert(parent='', index='end', iid=i, text='', values=(' ',i[39], i[2], i[3], i[25],i[5], i[6], i[7], i[8], i[9]))
      for line in pord_tree.get_children():
        idsaverefrsh=pord_tree.item(line)['values'][9]
      rfrs+=idsaverefrsh
    countp += 1
    # pordtotalrowcol.config(text=rfrs)
    # dropordr.delete(0,END)
    # notepriv.delete('1.0','end')
    # for record in tree.get_children():
    #   tree.delete(record)
    # for record in treeblw.get_children():
    #   treeblw.delete(record)

    

  w = Canvas(purch_midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=(5, 2))
  w = Canvas(purch_midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=(0, 5))

  purch_create_label = Button(purch_midFrame,compound="top", text="Create new\nP.Order",relief=RAISED, image=photo,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=purch_create)
  purch_create_label.pack(side="left", pady=3, ipadx=4)

  purch_edit_label = Button(purch_midFrame,compound="top", text="View/Edit\nP.Orders",relief=RAISED, image=photo1,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=purch_edit)
  purch_edit_label.pack(side="left")

  purch_dele_label = Button(purch_midFrame,compound="top", text="Delete\nSelected",relief=RAISED, image=photo2,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=dele)
  purch_dele_label.pack(side="left")

  w = Canvas(purch_midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  purch_preview_label = Button(purch_midFrame,compound="top", text="Print\nPreview",relief=RAISED, image=photo4,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=printpreview)
  purch_preview_label.pack(side="left")

  purch_print_label = Button(purch_midFrame,compound="top", text="Print\nSelected",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=printsele1)
  purch_print_label.pack(side="left")

  w = Canvas(purch_midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  purch_email_label = Button(purch_midFrame,compound="top", text=" E-mail \nP.Order",relief=RAISED, image=photo6,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=addemail_porder)
  purch_email_label.pack(side="left")

  sms1Label = Button(purch_midFrame,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=sms)
  sms1Label.pack(side="left")

  w = Canvas(purch_midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  purchprdtlabel = Button(purch_midFrame,compound="top", text="Search\nP.Orders",relief=RAISED, image=photo7,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=search)
  purchprdtlabel.pack(side="left")

  # lb1frame = LabelFrame(purch_midFrame, height=60, width=200, bg="#f8f8f2")
  # lb1frame.pack(side="left", padx=10, pady=0)
  # lbl1_porddt1 = Label(lb1frame, text="Porder date from : ", bg="#f8f8f2")
  # lbl1_porddt1.grid(row=0, column=0, pady=5, padx=(5, 0))
  # lbl1_porddtt = Label(lb1frame, text="Porder date to  :  ", bg="#f8f8f2")
  # lbl1_porddtt.grid(row=1, column=0, pady=5, padx=(5, 0))
  # porddt1 = Entry(lb1frame, width=15)
  # porddt1.grid(row=0, column=1)
  # porddtt = Entry(lb1frame, width=15)
  # porddtt.grid(row=1, column=1)
  # check1var1 = IntVar()
  # chk1btn1 = Checkbutton(lb1frame, text = "Apply filter", variable = check1var1, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2")
  # chk1btn1.grid(row=0, column=2, rowspan=2, padx=(5,5))

  lb1frame = LabelFrame(purch_midFrame, height=60, width=200, bg="#f8f8f2")
  lb1frame.pack(side="left", padx=10, pady=0)
  lbl_invdt = Label(lb1frame, text="Porder date from : ", bg="#f8f8f2")
  lbl_invdt.grid(row=0, column=0, pady=5, padx=(5, 0))
  lbl_invdtt = Label(lb1frame, text="Porder date to  :  ", bg="#f8f8f2")
  lbl_invdtt.grid(row=1, column=0, pady=5, padx=(5, 0))


  def date_range(): # Start and stop dates for range
    var1=start_dte.get_date().strftime('%y/%m/%d')
    var2=stop_dte.get_date().strftime('%y/%m/%d')
    for record in pord_tree.get_children():
      pord_tree.delete(record)

    sqldate='SELECT * FROM porder WHERE porderdate BETWEEN %s AND %s'
    valuz=(var1,var2,)
    fbcursor.execute(sqldate,valuz)
    filterdate=fbcursor.fetchall()
    dt=0
    countp = 0
    for i in filterdate:
      pord_tree.insert(parent='', index='end', iid=i, text='', values=(' ',i[39], i[2], i[3], i[25],i[5], i[6], i[7], i[8], i[9]))
      for line in pord_tree.get_children():
        idsavedt=pord_tree.item(line)['values'][9]
      dt+=idsavedt
    countp += 1
    # pordtotalrowcol.config(text=dt)
    # for record in tree.get_children():
    #   tree.delete(record)
    # notepriv.delete('1.0','end')
    # for record in treeblw.get_children():
    #   treeblw.delete(record)
    
  start_dte = DateEntry(lb1frame, width=15)
  start_dte.grid(row=0, column=1)
  stop_dte = DateEntry(lb1frame, width=15)
  stop_dte.grid(row=1, column=1)
  checkvar1 = IntVar()
  chkbtn1 = Button(lb1frame, text = "Apply\nFilter",height = 2, width = 8,command=date_range,bg="#f8f8f2")
  chkbtn1.grid(row=0, column=2, rowspan=2, padx=(5,5))


  purchprdtlabel = Button(purch_midFrame,compound="top", text="Refresh\nP.Orders list",relief=RAISED, image=photo8,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=refreshbttn)
  purchprdtlabel.pack(side="left")

  w = Canvas(purch_midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  purchprdtlabel = Button(purch_midFrame,compound="top", text="Hide totals\nSum",relief=RAISED, image=photo9,bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
  purchprdtlabel.pack(side="left")


  purch1label = Label(purch_mainFrame, text="Purchase Orders(All)", font=("arial", 18), bg="#f8f8f2")
  purch1label.pack(side="left", padx=(20,0))
  drop1 = ttk.Combobox(purch_mainFrame, value="Hello")
  drop1.pack(side="right", padx=(0,10))
  purch1label = Label(purch_mainFrame, text="Category filter", font=("arial", 15), bg="#f8f8f2")
  purch1label.pack(side="right", padx=(0,10))

  class MyApp1:
    def __init__(self, parent):
      
      self.myParent = parent 

      self.myContainer1 = Frame(parent) 
      self.myContainer1.pack()
      
      self.top_frame = Frame(self.myContainer1) 
      self.top_frame.pack(side=TOP,
        fill=BOTH, 
        expand=YES,
        )  

      self.left_frame = Frame(self.top_frame, background="white",
        borderwidth=5,  relief=RIDGE,
        height=250, 
        width=2000, 
        )
      self.left_frame.pack(side=LEFT,
        fill=BOTH, 
        expand=YES,
        )

      global pord_tree
      pord_tree = ttk.Treeview(self.left_frame, columns = (1,2,3,4,5,6,7,8,9,10), height = 15, show = "headings")
      pord_tree.pack(side = 'top')
      pord_tree.heading(1)
      pord_tree.heading(2, text="P.Order#")
      pord_tree.heading(3, text="Porder date")
      pord_tree.heading(4, text="Due date")
      pord_tree.heading(5, text="Customer Name")
      pord_tree.heading(6, text="Status")
      pord_tree.heading(7, text="Emailed on")
      pord_tree.heading(8, text="Printed on")
      pord_tree.heading(9, text="SMS on")
      pord_tree.heading(10, text="Porder Total")   
      pord_tree.column(1, width = 40)
      pord_tree.column(2, width = 145)
      pord_tree.column(3, width = 140)
      pord_tree.column(4, width = 140)
      pord_tree.column(5, width = 200)
      pord_tree.column(6, width = 140)
      pord_tree.column(7, width = 150)
      pord_tree.column(8, width = 130)
      pord_tree.column(9, width = 130)
      pord_tree.column(10, width = 130)
      

      # sql = "SELECT * FROM porder"
      # fbcursor.execute(sql)
      # porder_records = fbcursor.fetchall()

      # count = 0
      # for i in porder_records:
      #   if True:
      #     purch_tree.insert(parent='',index='end',iid=i,text='',values=('',i[39],i[2],i[3],i[25],i[5],i[6],i[7],i[8],i[9]))
      #   else:
      #     pass
      # count += 1


      pordtotalrowcol = Label(tab5,bg="#f5f3f2")
      pordtotalrowcol.place(x=1260,y=400,width=80,height=20)
      hidden=True
      # def label_hide_show(text):
      #   global hidden
      #   if hidden:
      #     pordtotalrowcol.config(text=text)
      #     pordtotalrowcol.pack(side = "top", fill = tk.BOTH)
      #     hidden = False
      #   else:
      #     pordtotalrowcol.pack_forget()
      #     hidden=True


      def prdctpicker(event):
        selected = pord_tree.focus()
        selected_prdct= pord_tree.item(selected)["values"][1]
        for record in tree.get_children():
          tree.delete(record)
        sqlprdct='SELECT * FROM storingproduct WHERE porderid=%s'
        valprdct=(selected_prdct,)
        fbcursor.execute(sqlprdct,valprdct)
        prdctsltn=fbcursor.fetchall()
        j = 0
        for i in prdctsltn:
         tree.insert(parent='', index='end', iid=i, text='', values=(' ',i[21], i[6], i[7],i[9],i[22],i[12],(i[9]*i[22])))
        j += 1

      #   notefchz="SELECT * FROM porder WHERE porderid=%s"
      #   fchz = (selected_prdct,)
      #   fbcursor.execute(notefchz, fchz)
      #   zoomb=fbcursor.fetchone()   
      #   notepriv.delete('1.0','end')
      #   notepriv.insert('1.0', zoomb[29])

      #   sqldoc='SELECT * FROM documents Where porderid=%s'
      #   vall=(selected_prdct,)
      #   fbcursor.execute(sqldoc,vall)
      #   for record in treeblw.get_children():
      #       treeblw.delete(record) 
      #   j = 0
      #   for i in fbcursor:
      #    treeblw.insert(parent='', index='end', iid=i, text='', values=(' ',i[2]))
      #   j += 1

      pord_tree.bind('<Double-Button-1>' , prdctpicker)

      # fbcursor.execute('SELECT * FROM porder;')
      # pordertotalinput=0
      # j = 0
      # for i in fbcursor:
      #   purch_tree.insert(parent='', index='end', iid=i, text='', values=(' ',i[0], i[2], i[3], i[4],i[5], i[6], i[7], i[8], i[9], i[10],i[11]))
      #   for line in purch_tree.get_children():
      #     idsave1=purch_tree.item(line)['values'][9]
      #     pordertotalinput += idsave1
      #     j += 1
      # pordtotalrowcol.config(text=pordertotalinput)

      fbcursor.execute('SELECT * FROM porder;')
      pordertotalinput=0
      j = 0
      for i in fbcursor:
          pord_tree.insert(parent='', index='end', iid=i, text='', values=(' ',i[39], i[2], i[3], i[25],i[5], i[6], i[7], i[8], i[9], i[10]))
          for line in pord_tree.get_children():
            idsave1=pord_tree.item(line)['values'][9]
          pordertotalinput += idsave1
          j += 1
      pordtotalrowcol.config(text=pordertotalinput)


      scrollbar = Scrollbar(self.left_frame)
      scrollbar.place(x=990+345, y=0, height=300+20)
      scrollbar.config( command=pord_tree.yview )

      tabControl = ttk.Notebook(self.left_frame,width=1)
      tab1 = ttk.Frame(tabControl)
      tab2 = ttk.Frame(tabControl)
      tab3=  ttk.Frame(tabControl)
      tab4 = ttk.Frame(tabControl)
      tabControl.add(tab1,image=invoices,compound = LEFT, text ='P.Order Items')
      tabControl.add(tab2,image=photo11,compound = LEFT, text ='Invoice Private Notes')
      tabControl.add(tab3,image=smslog,compound = LEFT, text ='SMS log')
      tabControl.add(tab4,image=photo11,compound = LEFT, text ='Documents')
      tabControl.pack(expand = 1, fill ="both")
      
      tree = ttk.Treeview(tab1, columns = (1,2,3,4,5,6,7,8,9,), height = 15, show = "headings")
      tree.pack(side = 'top')
      tree.heading(1)
      tree.heading(2, text="Product/Service ID",)
      tree.heading(3, text="Name")
      tree.heading(4, text="Description")
      tree.heading(5, text="Price")
      tree.heading(6, text="QTY")
      tree.heading(7, text="Tax1")
      tree.heading(8, text="Tax2")
      tree.heading(9, text="Line Total")   
      tree.column(1, width = 40)
      tree.column(2, width = 260)
      tree.column(3, width = 260)
      tree.column(4, width = 300)
      tree.column(5, width = 130)
      tree.column(6, width = 100)
      tree.column(7, width = 50)
      tree.column(8, width = 50)
      tree.column(9, width = 150)

      note1=Text(tab2, width=170,height=10).place(x=10, y=10)

      note1=Text(tab3, width=170,height=10).place(x=10, y=10)

      treeblw = ttk.Treeview(tab4, columns = (1,2,3), height = 15, show = "headings")
      treeblw.pack(side = 'top')
      treeblw.heading(1)
      treeblw.heading(2, text="Attach to Email",)
      treeblw.heading(3, text="Filename")
      treeblw.column(1, width = 50)
      treeblw.column(2, width = 250)
      treeblw.column(3, width = 1000)

      scrollbar = Scrollbar(self.left_frame)
      scrollbar.place(x=990+340, y=360, height=190)
      scrollbar.config( command=tree.yview )
        
  myapp = MyApp1(tab5)




root.mainloop()

