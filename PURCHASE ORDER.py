from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import pandas as pd
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename
import os
import webbrowser
from tkcalendar import Calendar
from tkcalendar import DateEntry
from datetime import date
from tkinter import filedialog
import mysql.connector


fbilldb = mysql.connector.connect(
  host="localhost", user="root", password="", database=" fbillingsintgrtd5(3)", port="3306"
 )
fbcursor = fbilldb.cursor(buffered=True)

root=Tk()
root.geometry("1360x730")
root.title("F-Billing Revolution 2022(FREE version) | Company database:fbillingdb | User:Administrator")
p1 = PhotoImage(file = 'images/fbicon.png')
root.iconphoto(False, p1)

s = ttk.Style()
s.theme_use('default')
s.configure('TNotebook.Tab', background="#999999", width=20, padding=10)
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
tabControl = ttk.Notebook(root)
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
    global tree
    tree=ttk.Treeview(cuselection, height=27)
    tree["columns"]=["1","2","3", "4"]
    tree.column("#0", width=35)
    tree.column("1", width=160)
    tree.column("2", width=160)
    tree.column("3", width=140)
    tree.column("4", width=140)
    tree.heading("#0",text="")
    tree.heading("1",text="Customer/Ventor ID")
    tree.heading("2",text="Customer/Ventor Name")
    tree.heading("3",text="Tel.")
    tree.heading("4",text="Contact Person")
    tree.place(x=5, y=45)

    sql_sel_pord_cust = "SELECT * FROM customer"
    fbcursor.execute(sql_sel_pord_cust)
    pord_customer_details = fbcursor.fetchall()

    count=0
    for i in pord_customer_details:
      if True:
        tree.insert(parent='',index='end',iid=i,text='',values=(i[0],i[4],i[10],i[8]))
      else:
        pass
    count += 1

    def pordcust_tree_fetch():
      pordcust_tree_item = tree.item(tree.focus())["values"][0]
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
    scrollbar.config( command=tree.yview )

    btn1=Button(cuselection,compound = LEFT,image=tick, text="ok",command=pordcust_tree_fetch, width=60).place(x=15, y=610)
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



    
                    
    enter=Label(newselection, text="Enter filter text").place(x=5, y=10)
    e1=Entry(newselection, width=20).place(x=110, y=10)
    text=Label(newselection, text="Filtered column").place(x=340, y=10)
    e2=Entry(newselection, width=20).place(x=450, y=10)

    pur_cusventtree=ttk.Treeview(newselection, height=27)
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

    sql = "SELECT * FROM Productservice"
    fbcursor.execute(sql)
    add_product_detail = fbcursor.fetchall()

    count = 0
    for p in add_product_detail:
      if True:
        pur_cusventtree.insert(parent='',index='end',iid=p,text='',values=(p[0],p[4],p[7],p[12],p[13]))
      else:
        pass
    count += 1

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
      proskuid = pur_cusventtree.item(pur_cusventtree.focus())["values"][0]
      sql = "select * from Productservice where sku = %s"
      val = (proskuid,)
      fbcursor.execute(sql,val)
      prosele = fbcursor.fetchone()
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
        
      newselection.destroy()

   

    btn1=Button(newselection,compound = LEFT,image=tick ,text="ok", width=60,command=purchselepro).place(x=15, y=610)
    btn1=Button(newselection,compound = LEFT,image=tick , text="Edit product/Service", width=150,command=product).place(x=250, y=610)
    btn1=Button(newselection,compound = LEFT,image=tick , text="Add product/Service", width=150,command=product).place(x=435, y=610)
    btn1=Button(newselection,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=610)


    def add_new_porder():
      #estidd = porder_number_entry0.get()
      porderid = porder_id_entry.get()
      pordate = pdate.get_date()
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


      

      porder_sql="INSERT INTO porder (porder_no,porderdate,duedate,status,emailon,printon,	ordertot,extracostname,extracost, salesper,discourate,tax1, category,businessname,businessaddress,deliveryto, deliveryaddress,cpemail,cpmobileforsms,title_text, header_text,footer_text,term_of_payment,terms,comments,privatenote) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" #adding values into db
      porder_val=(porderid,pordate,duedate,status,emailon,printon,pordtot,extracostname,extracost, salesper,discourate,tax1, category,businessname,businessaddress,delname, deladdress,cpemail,cpmobileforsms,title_text, header_text, footer_text,term_of_payment,terms,comments,private_notes)
      fbcursor.execute(porder_sql,porder_val)
      fbilldb.commit()
      #messagebox.showinfo("F-Billing Revolution","porder saved")
  #preview new line
  def previewline1():
    messagebox.showerror("F-Billing Revolution","line is required,please select customer for this order before printing.")



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
              tax1.config(text=(float(totaltax1)*float(porder_tax4.get())/100))
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
          
        #estimate_newselection.destroy()
      except:
        pass



  #finalize
  def finalize():  
    messagebox.askyesno("Finalize purchase order", "Would you like to mark this purchase order as completed ?All product will be added in to stock and purchase order will be closed")


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

  dele= Button(firFrame1,compound="top", text="Delete line\nitem",relief=RAISED, image=photo2,bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
  dele.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  prev= Button(firFrame1,compound="top", text="Preview\nP.Order",relief=RAISED, image=photo4,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=previewline1)
  prev.pack(side="left", pady=3, ipadx=4)

  prin= Button(firFrame1,compound="top", text="Print \nP.Order",relief=RAISED, image=photo5,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=printsele1)
  prin.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  mail= Button(firFrame1,compound="top", text="Email\nP.Order",relief=RAISED, image=photo6,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=email_invoice_recurring)
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

  Createorder= Button(firFrame1,compound="top", text="Save",relief=RAISED, image=tick,bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
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
  pdel=Text(labelframe1,width=30)
  pdel.place(x=402,y=30)
  address1=Label(labelframe1,text="Address").place(x=340,y=30)
  pdel_addr=Text(labelframe1,width=23)
  pdel.place(x=402,y=30,height=70)

  
  labelframe2 = LabelFrame(fir1Frame,text="")
  labelframe2.place(x=10,y=130,width=640,height=42)
  email=Label(labelframe2,text="Email").place(x=10,y=5)
  pmail=Entry(labelframe2,width=30)
  pmail.place(x=80,y=5)
  sms=Label(labelframe2,text="SMS Number").place(x=327,y=5)
  psms=Entry(labelframe2,width=28)
  psms.place(x=402,y=3)

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
  pdate=DateEntry(labelframe,width=20).place(x=150,y=33)

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
  e4=ttk.Combobox(labelframe, value="",width=25).place(x=100,y=92)
  ref=Label(labelframe,text="Order ref#").place(x=5,y=118)
  pref=Entry(labelframe,width=27).place(x=100,y=118)

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
      tax1.config(text="" +"0.00")
      tax2.config(text="" +"0.00")
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
      tax1.config(text=round(tax1_rate,2))
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
      tax1.config(text=round((tax1_rate + tax2_rate),2))
      tax2.config(text=round((tax3_rate + tax4_rate),2))
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
      tax1.config(text="" +"0.00")
      tax2.config(text="" +"0.00")
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
      tax1.config(text=round(tax1_rate,2))
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
      tax1.config(text=round((tax1_rate + tax2_rate),2))
      tax2.config(text=round((tax3_rate + tax4_rate),2))
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
    draft.place(x=50, y=3)
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
  tax1=Label(summaryfrme, text="$0.00")
  tax1.place(x=130 ,y=42)
  taxx=Label(summaryfrme, text="Tax2")
  taxx.place(x=0 ,y=63)
  tax2=Label(summaryfrme, text="$0.00")
  tax2.place(x=130 ,y=63)
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

#######################END OF CREATE PORDER##############



def purch_edit():
    pop1=Toplevel(purch_midFrame)
    pop1.title("Porder")
    pop1.geometry("950x690+150+0")


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

        btn1=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=tick,text="OK").place(x=20, y=615)
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

      btn1=Button(purch_cuselection,compound = LEFT,image=tick, text="ok",command=pordcust_tree_fetch, width=60).place(x=15, y=610)
      btn1=Button(purch_cuselection,compound = LEFT,image=tick, text="Edit selected customer", width=150,command=purch_create_newcust).place(x=250, y=610)
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

    edit_mail= Button(firFrame1,compound="top", text="Email\nP.Order",relief=RAISED, image=photo6,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=email_invoice_recurring)
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

    Createorder= Button(firFrame1,compound="top", text="Save",relief=RAISED, image=tick,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=create_porder)
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


    
    porder = Label(labelframe1, text="Vendor to").place(x=10,y=5)
    purch_to = StringVar()
    vender_combo = ttk.Combobox(labelframe1, value="Hello",width=28)
    vender_combo.place(x=80,y=5)
    vender_combo['values'] = purdata
    vender_combo.bind("<<ComboboxSelected>>", purch_to_combo)
    address=Label(labelframe1,text="Address").place(x=10,y=30)
    paddress=Text(labelframe1,width=23)
    paddress.place(x=80,y=30,height=70)
    ship=Label(labelframe1,text="Delivery to").place(x=342,y=5)
    pdel=Text(labelframe1,width=30)
    pdel.place(x=402,y=3)
    address1=Label(labelframe1,text="Address").place(x=340,y=30)
    pdel_addr=Text(labelframe1,width=23)
    pdel_addr.place(x=402,y=30,height=70)

    
    labelframe2 = LabelFrame(fir1Frame,text="")
    labelframe2.place(x=10,y=130,width=640,height=42)
    email=Label(labelframe2,text="Email").place(x=10,y=5)
    pmail=Entry(labelframe2,width=30)
    pmail.place(x=80,y=5)
    sms=Label(labelframe2,text="SMS Number").place(x=327,y=5)
    psms=Entry(labelframe2,width=28)
    psms.place(x=402,y=3)

    labelframe = LabelFrame(fir1Frame,text="Purchase Order")
    labelframe.place(x=652,y=5,width=290,height=170)
    porder=Label(labelframe,text="P.Order#").place(x=5,y=5)
    porder_id=Entry(labelframe,width=27)
    porder_id.place(x=100,y=5,)
    def pordid_increment(inum):
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
      result += "0" if number < 10 else ""
      result += str(number)
      return result
      
      fbcursor.execute("SELECT * FROM porder ORDER BY porderid DESC LIMIT 1")
      pord_data = fbcursor.fetchone()
          
      if not pord_data == None:
        a = pord_data[1]
        porderid = pord_id_increment(a)
      else:
        porderid = 1
        porder_id.insert(0,porderid)
        

    porderdate=Label(labelframe,text="P.Order date").place(x=5,y=33)
    pdate=DateEntry(labelframe,width=20)
    pdate.place(x=150,y=33)


    sql="select dateformat from company"
    fbcursor.execute(sql)
    date_for = fbcursor.fetchone()
     
    if not date_for:
      pass
    else:
      if date_for[0] == "mm-dd-yyyy":
        pdate._set_text(pdate._date.strftime('%m-%d-%Y'))
      elif date_for[0] == "dd-mm-yyyy":
        pdate._set_text(pdate._date.strftime('%d-%m-%Y'))
      elif date_for[0] == "yyy.mm.dd":
        pdate._set_text(pdate._date.strftime('%Y.%m.%d'))
      elif date_for[0] == "mm/dd/yyyy":
        pdate._set_text(pdate._date.strftime('%m/%d/%Y'))
      elif date_for[0] == "dd/mm/yyy":
        pdate._set_text(pdate._date.strftime('%d/%m/%Y'))
      elif date_for[0] == "dd.mm.yyyy":
        pdate._set_text(pdate._date.strftime('%d.%m.%Y'))
      elif date_for[0] == "yyyy/mm/dd":
        pdate._set_text(pdate._date.strftime('%Y/%m/%d'))
      else:
        pass
  

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
    e4=ttk.Combobox(labelframe, value="",width=25).place(x=100,y=92)
    ref=Label(labelframe,text="Order ref#").place(x=5,y=118)
    pref=Entry(labelframe,width=27).place(x=100,y=118)

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

      # purch_tree.pack(fill="both", expand=1)
      # listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

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

      # purch_tree.pack(fill="both", expand=1)
      # listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

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

    # purch_tree.pack(fill="both", expand=1)
    # listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

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
    
    # tree=ttk.Treeview(listFrame)
    # tree["columns"]=["1","2","3","4","5","6","7","8"]

    # tree.column("#0", width=40)
    # tree.column("1", width=80)
    # tree.column("2", width=190)
    # tree.column("3", width=190)
    # tree.column("4", width=80)
    # tree.column("5", width=60)
    # tree.column("6", width=60)
    # tree.column("7", width=60)
    # tree.column("8", width=80)
    
    # tree.heading("#0")
    # tree.heading("1",text="ID/SKU")
    # tree.heading("2",text="Product/Service")
    # tree.heading("3",text="Description")
    # tree.heading("4",text="Unit Price")
    # tree.heading("5",text="Quality")
    # tree.heading("6",text="Pcs/Weight")
    # tree.heading("7",text="Tax1")
    # tree.heading("8",text="Price")
    
    # tree.pack(fill="both", expand=1)
    # listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

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

    labelframe1 = LabelFrame(orderFrame,text="",font=("arial",15))
    labelframe1.place(x=1,y=1,width=800,height=170)
    cost1=Label(labelframe1,text="Extra cost name").place(x=2,y=5)
    pextra=ttk.Combobox(labelframe1, value="",width=20).place(x=115,y=5)
    rate=Label(labelframe1,text="Discount rate")
    rate.place(x=370,y=5)
    pdisc=Spinbox(labelframe1,width=6,  from_=0, to=100, font="italic 10")
    pdisc.place(x=460,y=5)
    cost2=Label(labelframe1,text="Extra cost").place(x=35,y=35)
    pcost=Entry(labelframe1,width=10)
    pcost.place(x=115,y=35)
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

    template=Label(labelframe1,text="Template").place(x=37,y=70)
    ptemp=ttk.Combobox(labelframe1, value="",width=25).place(x=115,y=70)
    sales=Label(labelframe1,text="Sales Person").place(x=25,y=100)
    psale=Entry(labelframe1,width=18).place(x=115,y=100)
    category=Label(labelframe1,text="Category").place(x=300,y=100)
    pact=Entry(labelframe1,width=22).place(x=370,y=100)

    statusfrme = LabelFrame(labelframe1,text="Status",font=("arial",15))
    statusfrme.place(x=540,y=0,width=160,height=160)
    draft=Label(statusfrme, text="Draft",font=("arial", 15, "bold"), fg="grey").place(x=50, y=3)
    on1=Label(statusfrme, text="Emailed on:").place( y=50)
    nev1=Label(statusfrme, text="Never").place(x=100,y=50)
    on2=Label(statusfrme, text="Printed on:").place( y=90)
    nev2=Label(statusfrme, text="Never").place(x=100,y=90)

    text1=Label(headerFrame,text="Title text").place(x=50,y=5)
    e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=5)
    text2=Label(headerFrame,text="Page header text").place(x=2,y=45)
    e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=45)
    text3=Label(headerFrame,text="Footer text").place(x=35,y=85)
    e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=85)

    text=Label(noteFrame,text="Private notes(not shown on invoice/order/estemates)").place(x=10,y=10)
    pvt=Text(noteFrame,width=100,height=7).place(x=10,y=32)

    e1=Text(termsFrame,width=100,height=9).place(x=10,y=10)

    e1=Text(commentFrame,width=100,height=9).place(x=10,y=10)

    btn1=Button(documentFrame,height=2,width=3,text="+").place(x=5,y=10)
    btn2=Button(documentFrame,height=2,width=3,text="-").place(x=5,y=50)
    text=Label(documentFrame,text="Attached documents or image files.If you attach large email then email taken long time to send").place(x=50,y=10)
    purchase_cusventtree=ttk.Treeview(documentFrame, height=5)
    purchase_cusventtree["columns"]=["1","2","3"]
    purchase_cusventtree.column("#0", width=20)
    purchase_cusventtree.column("1", width=250)
    purchase_cusventtree.column("2", width=250)
    purchase_cusventtree.column("2", width=200)
    purchase_cusventtree.heading("#0",text="", anchor=W)
    purchase_cusventtree.heading("1",text="Attach to Email")
    purchase_cusventtree.heading("2",text="Filename")
    purchase_cusventtree.heading("3",text="Filesize")  
    purchase_cusventtree.place(x=50, y=45)

    fir4Frame=Frame(pop1,height=190,width=210,bg="#f5f3f2")
    fir4Frame.place(x=740,y=520)
    purch_summaryfrme = LabelFrame(fir4Frame,text="Summary",font=("arial",15))
    purch_summaryfrme.place(x=0,y=0,width=200,height=170)
    purch_discount=Label(purch_summaryfrme, text="Discount").place(x=0 ,y=0)
    purch_discount1=Label(purch_summaryfrme, text="$0.00")
    purch_discount1.place(x=130 ,y=0)
    pur_sub=Label(purch_summaryfrme, text="Subtotal").place(x=0 ,y=21)
    pur_sub1=Label(purch_summaryfrme, text="$0.00")
    pur_sub1.place(x=130 ,y=21)
    pur_tax=Label(purch_summaryfrme, text="Tax1").place(x=0 ,y=42)
    pur_tax1=Label(purch_summaryfrme, text="$0.00")
    pur_tax1.place(x=130 ,y=42)
    pur_taxx=Label(purch_summaryfrme, text="Tax2").place(x=0 ,y=63)
    pur_tax2=Label(purch_summaryfrme, text="$0.00")
    pur_tax2.place(x=130 ,y=63)
    pur_cost=Label(purch_summaryfrme, text="Extra cost").place(x=0 ,y=84)
    pur_cost1=Label(purch_summaryfrme, text="$0.00")
    pur_cost1.place(x=130 ,y=84)
    porder=Label(purch_summaryfrme, text="P.Order total").place(x=0 ,y=105)
    porder1=Label(purch_summaryfrme, text="$0.00")
    porder1.place(x=130 ,y=105)

    fir5Frame=Frame(pop1,height=38,width=210)
    fir5Frame.place(x=735,y=485)
    btndown=Button(fir5Frame, compound="left", text="Line Down").place(x=75, y=0)
    btnup=Button(fir5Frame, compound="left", text="Line Up").place(x=150, y=0)


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
      
def email_invoice_recurring():
  mailDetail=Toplevel()
  mailDetail.title("Invoice E-Mail")
  mailDetail.geometry("1080x550")
  mailDetail.resizable(False, False)
  def my_SMTP():
      if True:
          em_ser_conbtn.destroy()
          mysmtpservercon=LabelFrame(account_Frame,text="SMTP server connection(ask your ISP for your SMTP settings)", height=165, width=380)
          mysmtpservercon.place(x=610, y=110)
          lbl_hostn=Label(mysmtpservercon, text="Hostname").place(x=5, y=10)
          hostnent=Entry(mysmtpservercon, width=30).place(x=80, y=10)
          lbl_portn=Label(mysmtpservercon, text="Port").place(x=5, y=35)
          portent=Entry(mysmtpservercon, width=30).place(x=80, y=35)
          lbl_usn=Label(mysmtpservercon, text="Username").place(x=5, y=60)
          unament=Entry(mysmtpservercon, width=30).place(x=80, y=60)
          lbl_pasn=Label(mysmtpservercon, text="Password").place(x=5, y=85)
          pwdent=Entry(mysmtpservercon, width=30).place(x=80, y=85)
          ssl_chkvar=IntVar()
          ssl_chkbtn=Checkbutton(mysmtpservercon, variable=ssl_chkvar, text="This server requires a secure connection(SSL)", onvalue=1, offvalue=0)
          ssl_chkbtn.place(x=50, y=110)
          em_ser_conbtn1=Button(account_Frame, text="Test E-mail Server Connection").place(x=610, y=285)
      else:
          pass
    
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
  lbl_emailtoaddr=Label(messagelbframe, text="Email to address").place(x=5, y=5)
  emailtoent=Entry(messagelbframe, width=50).place(x=120, y=5)
  sendemail_btn=Button(messagelbframe, text="Send Email", width=10, height=1,command=addacnt).place(x=600, y=10)
  lbl_carcopyto=Label(messagelbframe, text="Carbon copy to").place(x=5, y=32)
  carcopyent=Entry(messagelbframe, width=50).place(x=120, y=32)
  stopemail_btn=Button(messagelbframe, text="Stop sending", width=10, height=1).place(x=600, y=40)
  lbl_subject=Label(messagelbframe, text="Subject").place(x=5, y=59)
  subent=Entry(messagelbframe, width=50).place(x=120, y=59)

  
  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
  mess_Notebook = ttk.Notebook(messagelbframe)
  emailmessage_Frame = Frame(mess_Notebook, height=350, width=710)
  htmlsourse_Frame = Frame(mess_Notebook, height=350, width=710)
  mess_Notebook.add(emailmessage_Frame, text="E-mail message")
  mess_Notebook.add(htmlsourse_Frame, text="Html sourse code")
  mess_Notebook.place(x=5, y=90)

  btn1=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)

  
  btn2=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
  btn3=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
  btn4=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
  btn5=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo).place(x=140, y=1)
  btn6=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo).place(x=175, y=1)
  btn7=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold).place(x=210, y=1)
  btn8=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics).place(x=245, y=1)
  btn9=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline).place(x=280, y=1)
  btn10=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=left).place(x=315, y=1)
  btn11=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=right).place(x=350, y=1)
  btn12=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=center).place(x=385, y=1)
  btn13=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink).place(x=420, y=1)
  
  btn14=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove).place(x=455, y=1)


  dropcomp = ttk.Combobox(emailmessage_Frame, width=12, height=3).place(x=500, y=5)
  dropcompo = ttk.Combobox(emailmessage_Frame, width=6, height=3).place(x=600, y=5)
  mframe=Frame(emailmessage_Frame, height=350, width=710, bg="white")
  mframe.place(x=0, y=28)



  btn1=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)

  
  btn2=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
  btn3=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
  btn4=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
  mframe=Frame(htmlsourse_Frame, height=350, width=710, bg="white")
  mframe.place(x=0, y=28)

  attachlbframe=LabelFrame(email_Frame,text="Attachment(s)", height=350, width=280)
  attachlbframe.place(x=740, y=5)
  htcodeframe=Frame(attachlbframe, height=220, width=265, bg="white").place(x=5, y=5)
  lbl_btn_info=Label(attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
  btn17=Button(attachlbframe, width=20, text="Add attacment file...").place(x=60, y=260)
  btn18=Button(attachlbframe, width=20, text="Remove attacment").place(x=60, y=295)
  lbl_tt_info=Label(email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
  lbl_tt_info.place(x=740, y=370)

  ready_frame=Frame(mailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
  
  sendatalbframe=LabelFrame(account_Frame,text="E-Mail(Sender data)",height=270, width=600)
  sendatalbframe.place(x=5, y=5)
  lbl_sendermail=Label(sendatalbframe, text="Your company email address").place(x=5, y=30)
  sentent=Entry(sendatalbframe, width=40).place(x=195, y=30)
  lbl_orcompanyname=Label(sendatalbframe, text="Your name or company name").place(x=5, y=60)
  nament=Entry(sendatalbframe, width=40).place(x=195, y=60)
  lbl_reply=Label(sendatalbframe, text="Reply to email address").place(x=5, y=90)
  replyent=Entry(sendatalbframe, width=40).place(x=195, y=90)
  lbl_sign=Label(sendatalbframe, text="Signature").place(x=5, y=120)
  signent=Entry(sendatalbframe,width=50).place(x=100, y=120,height=75)
  confirm_chkvar=IntVar()
  confirm_chkbtn=Checkbutton(sendatalbframe, variable=confirm_chkvar, text="Confirmation reading", onvalue=1, offvalue=0)
  confirm_chkbtn.place(x=200, y=215)
  btn18=Button(account_Frame, width=15, text="Save settings",command=savesettings).place(x=25, y=285)

  sendatalbframe=LabelFrame(account_Frame,text="SMTP Server",height=100, width=380)
  sendatalbframe.place(x=610, y=5)
  servar=IntVar()
  SMTP_rbtn=Radiobutton(sendatalbframe, text="Use the Built-In SMTP Server Settings", variable=servar, value=1)
  SMTP_rbtn.place(x=10, y=10)
  MySMTP_rbtn=Radiobutton(sendatalbframe, text="Use My Own SMTP Server Settings(Recommended)", variable=servar, value=2, command=my_SMTP)
  MySMTP_rbtn.place(x=10, y=40)
  em_ser_conbtn=Button(account_Frame, text="Test E-mail Server Connection")
  em_ser_conbtn.place(x=710, y=110)

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
  messagebox.askyesno("Delete order", "Are you sure to delete this order? All products will be placed back into stock")



#search in orders  
def search():  
    top = Toplevel()     
    top.title("Find Text")   
    top.geometry("600x250+390+250")
    findwhat1=Label(top,text="Find What:",pady=5,padx=10).place(x=5,y=20)
    n = StringVar()
    findwhat = ttk.Combobox(top, width = 40, textvariable = n ).place(x=90,y=25)
   
    findin1=Label(top,text="Find in:",pady=5,padx=10).place(x=5,y=47)
    n = StringVar()
    findIN = ttk.Combobox(top, width = 30, textvariable = n )
    findIN['values'] = ('Product/Service id', ' Category', ' Active',' name',' stock',' location', ' image',' <<All>>')                       
    findIN.place(x=90,y=54)
    findIN.current(0)

    findButton = Button(top, text ="Find next",width=10).place(x=480,y=22)
    closeButton = Button(top,text ="Close",width=10).place(x=480,y=52)
    
    match1=Label(top,text="Match:",pady=5,padx=10).place(x=5,y=74)
    n = StringVar()
    match = ttk.Combobox(top, width = 23, textvariable = n )   
    match['values'] = ('From Any part',' Whole Field',' From the beginning of the field')                                   
    match.place(x=90,y=83)
    match.current(0)

    search1=Label(top,text="Search:",pady=5,padx=10).place(x=5,y=102)
    n = StringVar()
    search = ttk.Combobox(top, width = 23, textvariable = n )
    search['values'] = ('All', 'up',' Down')
    search.place(x=90,y=112)
    search.current(0)
    checkvarStatus4=IntVar()  
    Button4 = Checkbutton(top,variable = checkvarStatus4,text="Match Case",onvalue =0 ,offvalue = 1,height=3,width = 15)
    Button4.place(x=90,y=141)
    checkvarStatus5=IntVar()   
    Button5 = Checkbutton(top,variable = checkvarStatus5,text="Match Format",onvalue =0 ,offvalue = 1,height=3,width = 15)
    Button5.place(x=300,y=141)


purch_mainFrame=Frame(tab5, relief=GROOVE, bg="#f8f8f2")
purch_mainFrame.pack(side="top", fill=BOTH)

purch_midFrame=Frame(purch_mainFrame, bg="#f5f3f2", height=60)
purch_midFrame.pack(side="top", fill=X)


# purch_mainFrame=Frame(tab5, relief=GROOVE, bg="#f8f8f2")
# purch_mainFrame.pack(side="top", fill=BOTH)

# purch_midFrame=Frame(purch_mainFrame, bg="#f5f3f2", height=60)
# purch_midFrame.pack(side="top", fill=X)

w = Canvas(purch_midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(5, 2))
w = Canvas(purch_midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(0, 5))

purch_create_label = Button(purch_midFrame,compound="top", text="Create new\nP.Order",relief=RAISED, image=photo,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=purch_create)
purch_create_label.pack(side="left", pady=3, ipadx=4)

purch_viewedit_label = Button(purch_midFrame,compound="top", text="View/Edit\nP.Orders",relief=RAISED, image=photo1,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=purch_create)
purch_viewedit_label.pack(side="left")

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

purch_email_label = Button(purch_midFrame,compound="top", text=" E-mail \nP.Order",relief=RAISED, image=photo6,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=email_invoice_recurring)
purch_email_label.pack(side="left")

sms1Label = Button(purch_midFrame,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=sms)
sms1Label.pack(side="left")

w = Canvas(purch_midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

purchprdtlabel = Button(purch_midFrame,compound="top", text="Search\nP.Orders",relief=RAISED, image=photo7,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=search)
purchprdtlabel.pack(side="left")

lb1frame = LabelFrame(purch_midFrame, height=60, width=200, bg="#f8f8f2")
lb1frame.pack(side="left", padx=10, pady=0)
lbl1_porddt1 = Label(lb1frame, text="Porder date from : ", bg="#f8f8f2")
lbl1_porddt1.grid(row=0, column=0, pady=5, padx=(5, 0))
lbl1_porddtt = Label(lb1frame, text="Porder date to  :  ", bg="#f8f8f2")
lbl1_porddtt.grid(row=1, column=0, pady=5, padx=(5, 0))
porddt1 = Entry(lb1frame, width=15)
porddt1.grid(row=0, column=1)
porddtt = Entry(lb1frame, width=15)
porddtt.grid(row=1, column=1)
check1var1 = IntVar()
chk1btn1 = Checkbutton(lb1frame, text = "Apply filter", variable = check1var1, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2")
chk1btn1.grid(row=0, column=2, rowspan=2, padx=(5,5))

purchprdtlabel = Button(purch_midFrame,compound="top", text="Refresh\nP.Orders list",relief=RAISED, image=photo8,bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
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

    
    purchase_tree = ttk.Treeview(self.left_frame, columns = (1,2,3,4,5,6,7,8,9,10), height = 15, show = "headings")
    purchase_tree.pack(side = 'top')
    purchase_tree.heading(1)
    purchase_tree.heading(2, text="P.Order#")
    purchase_tree.heading(3, text="Porder date")
    purchase_tree.heading(4, text="Due date")
    purchase_tree.heading(5, text="Customer Name")
    purchase_tree.heading(6, text="Status")
    purchase_tree.heading(7, text="Emailed on")
    purchase_tree.heading(8, text="Printed on")
    purchase_tree.heading(9, text="SMS on")
    purchase_tree.heading(10, text="Porder Total")   
    purchase_tree.column(1, width = 40)
    purchase_tree.column(2, width = 145)
    purchase_tree.column(3, width = 140)
    purchase_tree.column(4, width = 140)
    purchase_tree.column(5, width = 200)
    purchase_tree.column(6, width = 140)
    purchase_tree.column(7, width = 150)
    purchase_tree.column(8, width = 130)
    purchase_tree.column(9, width = 130)
    purchase_tree.column(10, width = 130)

    scrollbar = Scrollbar(self.left_frame)
    scrollbar.place(x=990+345, y=0, height=300+20)
    scrollbar.config( command=purchase_tree.yview )

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

    tree = ttk.Treeview(tab4, columns = (1,2,3), height = 15, show = "headings")
    tree.pack(side = 'top')
    tree.heading(1)
    tree.heading(2, text="Attach to Email",)
    tree.heading(3, text="Filename")
    tree.column(1, width = 50)
    tree.column(2, width = 250)
    tree.column(3, width = 1000)

    scrollbar = Scrollbar(self.left_frame)
    scrollbar.place(x=990+340, y=360, height=190)
    scrollbar.config( command=tree.yview )
       
myapp = MyApp1(tab5)



root.mainloop()







