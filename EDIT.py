def purch_edit():
    try:
      edit_pordtree_fetch = purchase_tree.item(purchase_tree.focus())["values"][1]
      sql="SELECT * FROM porder WHERE porder_no=%s"
      val=(edit_pordtree_fetch,)
      fbcursor.execute(sql,val)
      global edit_pord_data
      edit_pord_data = fbcursor.fetchone()
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
          scrollbar.config( command=tree.yview )

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

                  
          pur_cusventtree.tag_configure('green', foreground='green')
          pur_cusventtree.tag_configure('red', foreground='red')
          pur_cusventtree.tag_configure('blue', foreground='blue')

          
          sql_sel_pro_purch = "SELECT * FROM productservice"
          fbcursor.execute(sql_sel_pro_purch)
          purchprodata = fbcursor.fetchall()
          countp = 0

          for i in purchprodata:
            if i[12] == '1':
              servi = '🗹'
            else:
              servi = ''
            sql = "select currencysign,currsignplace from company"
            fbcursor.execute(sql)
            purcurrsymb = fbcursor.fetchone()
            if not purcurrsymb: 
              if i[13] > i[14]:
                pur_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('green',))
                countp += 1              
              elif i[12] == '1':
                pur_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('blue',))
                countp += 1
              else:
                pur_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('red',))
                countp += 1
                        
            elif purcurrsymb[1] == "before amount":
              if (i[13]) > (i[14]):
                pur_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],purcurrsymb[0]+i[7],servi,i[13]),tags=('green',))
                countp += 1
              elif i[12] == '1':
                pur_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],purcurrsymb[0]+i[7],servi,i[13]),tags=('blue',))
                countp += 1
              else:
                pur_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],purcurrsymb[0]+i[7],servi,i[13]),tags=('red',))
                countp += 1

            elif purcurrsymb[1] == "before amount with space":
              if (i[13]) > (i[14]):
                pur_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],purcurrsymb[0] +" "+i[7],servi,i[13]),tags=('green',))
                countp += 1
              elif i[12] == '1':
                pur_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],purcurrsymb[0] +" "+i[7],servi,i[13]),tags=('blue',))
                countp += 1
              else:
                pur_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],purcurrsymb[0] +" "+i[7],servi,i[13]),tags=('red',))
                countp += 1

            elif purcurrsymb[1] == "after amount":
              if (i[13]) > (i[14]):
                pur_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+purcurrsymb[0],servi,i[13]),tags=('green',))
                countp += 1
              elif i[12] == '1':
                pur_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+purcurrsymb[0],servi,i[13]),tags=('blue',))
                countp += 1
              else:
                pur_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+purcurrsymb[0],servi,i[13]),tags=('red',))
                countp += 1

            elif purcurrsymb[1] == "after amount with space":
              if (i[13]) > (i[14]):
                pur_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+" "+purcurrsymb[0],servi,i[13]),tags=('green',))
                countp += 1
              elif i[12] == '1':
                pur_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+" "+purcurrsymb[0],servi,i[13]),tags=('blue',))
                countp += 1
              else:
                pur_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+" "+purcurrsymb[0],servi,i[13]),tags=('red',))
                countp += 1


          def purchseleproduct():
            global pordpriceview
            pordpriceview = Label(listFrame,bg="#f5f3f2")
            pordpriceview.place(x=850,y=200,width=78,height=18)
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
              purch_tree.insert(parent='', index='end',text='', values=(prosele[2],prosele[4],prosele[5],prosele[7],prosele[8],prosele[7]*1))
              extracs = 0.0
              discou = 0.0
              total = 0.0
              for child in purch_tree.get_children():
                total += float(purch_tree.item(child, 'values')[6])
              discou = (total*float(pdisc.get())/100)
              extracs = (extracs+float(pcost.get()))
              pur_cost1.config(text=pcost.get())
              purch_discount1.config(text=discou)
              pordpriceview.config(text=total)
              porder1.config(text=total-discou+extracs)
                # estimate_balancee1.config(text=total-discou+extracs)
              pur_sub1.config(text=total-discou)
            elif create_maintree_insert[12] == "2":
              purch_tree.insert(parent='', index='end',text='', values=(prosele[2],prosele[4],prosele[5],prosele[7],1,prosele[8],tax1,prosele[7]*1))
              extracs = 0.0
              discou = 0.0
              total = 0.0
              for child in purch_tree.get_children():
                total += float(purch_tree.item(child, 'values')[7])
              discou = (total*float(pdisc.get())/100)
              extracs = (extracs+float(pcost.get()))
              pur_cost1.config(text=pcost.get())
              purch_discount1.config(text=discou)
              pordpriceview.config(text=total)
              pur_sub1.config(text=total-discou)

              tot = 0.0
              totaltax1 = 0.0
              for child in purch_tree.get_children():
                checktax1 = list(purch_tree.item(child, 'values'))
                if checktax1[6] == "yes":
                  totaltax1 =(totaltax1 + float(checktax1[7]))
                  pur_tax1.config(text=(float(totaltax1)*float(porder_tax4.get())/100))
                  tot = (float(totaltax1)*float(porder_tax4.get())/100)
                else:
                  pass
              porder1.config(text=total+tot-discou+extracs)
                # estimate_balancee1.config(text=total+tot-discou+extracs)
                  
            elif create_maintree_insert[12] == "3":
              purch_tree.insert(parent='', index='end',text='', values=(prosele[2],prosele[4],prosele[5],prosele[7],1,prosele[8],tax1,tax2,prosele[7]*1))
              extracs = 0.0
              discou = 0.0
              total = 0.0
              for child in purch_tree.get_children():
                total += float(purch_tree.item(child, 'values')[8])
              extracs = (extracs+float(pcost.get()))
              pur_cost1.config(text=pcost.get())
              discou = (total*float(pdisc.get())/100)
              purch_discount1.config(text=discou)
              pordpriceview.config(text=total)
              pur_sub1.config(text=total-discou)
                  
              tot = 0.0
              totaltax1 = 0.0
              for child in purch_tree.get_children():
                checktax1 = list(purch_tree.item(child, 'values'))
                if checktax1[6] == "yes":
                  totaltax1 =(totaltax1 + float(checktax1[8]))
                  pur_tax1.config(text=(float(totaltax1)*float(porder_tax4.get())/100))
                  tot = (float(totaltax1)*float(porder_tax4.get())/100)
                else:
                  pass          
              tot2 = 0.0
              totaltax2 = 0.0
              for child in purch_tree.get_children():
                checktax1 = list(purch_tree.item(child, 'values'))
                if checktax1[7] == "yes":
                  totaltax2 =(totaltax2 + float(checktax1[8]))
                  pur_tax2.config(text=(float(totaltax2)*float(porder_tax5.get())/100))
                    
                  tot2 = (float(totaltax2)*float(porder_tax5.get())/100)
                else:
                  pass

              porder1.config(text=total+tot+tot2-discou+extracs)
                # estimate_balancee1.config(text=total+tot+tot2-discou+extracs)
              
              pnewselection.destroy()




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
          ship=Label(labelframe1,text="Delivery to").place(x=340,y=5)
          pdel=Entry(labelframe1)
          pdel.place(x=402,y=5)
          address1=Label(labelframe1,text="Address").place(x=340,y=30)
          pdel_addr=Entry(labelframe1,width=23)
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
        #  porder_id.place(x=100,y=5,)
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
            purch_tree1=ttk.Treeview(listFrame)
            purch_tree1["columns"]=["1","2","3","4","5","6","7"]

            purch_tree1.column("#0", width=40)
            purch_tree1.column("1", width=80)
            purch_tree1.column("2", width=190)
            purch_tree1.column("3", width=190)
            purch_tree1.column("4", width=80)
            purch_tree1.column("5", width=60)
            purch_tree1.column("6", width=60)
            purch_tree1.column("7", width=60)
            #purch_tree.column("8", width=80)
            
            purch_tree1.heading("#0")
            purch_tree1.heading("1",text="ID/SKU")
            purch_tree1.heading("2",text="Product/Service")
            purch_tree1.heading("3",text="Description")
            purch_tree1.heading("4",text="Unit Price")
            purch_tree1.heading("5",text="Quantity")
            purch_tree1.heading("6",text="Pcs/Weight")
            # purch_tree.heading("7",text="Tax1")
            purch_tree1.heading("7",text="Price")

            # purch_tree1.pack(fill="both", expand=1)
            # listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

          elif ptaxdata[12] == "1":
            purch_tree1=ttk.Treeview(listFrame)
            purch_tree1["columns"]=["1","2","3","4","5","6","7"]

            purch_tree1.column("#0", width=40)
            purch_tree1.column("1", width=80)
            purch_tree1.column("2", width=190)
            purch_tree1.column("3", width=190)
            purch_tree1.column("4", width=80)
            purch_tree1.column("5", width=60)
            purch_tree1.column("6", width=60)
            purch_tree1.column("7", width=60)
            #purch_tree.column("8", width=80)
            
            purch_tree1.heading("#0")
            purch_tree1.heading("1",text="ID/SKU")
            purch_tree1.heading("2",text="Product/Service")
            purch_tree1.heading("3",text="Description")
            purch_tree1.heading("4",text="Unit Price")
            purch_tree1.heading("5",text="Quantity")
            purch_tree1.heading("6",text="Pcs/Weight")
            # purch_tree.heading("7",text="Tax1")
            purch_tree1.heading("7",text="Price")

            # purch_tree.pack(fill="both", expand=1)
            # listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

          elif ptaxdata[12] == "2":
            purch_tree1=ttk.Treeview(listFrame)
            purch_tree1["columns"]=["1","2","3","4","5","6","7","8"]

            purch_tree1.column("#0", width=40)
            purch_tree1.column("1", width=80)
            purch_tree1.column("2", width=190)
            purch_tree1.column("3", width=190)
            purch_tree1.column("4", width=80)
            purch_tree1.column("5", width=60)
            purch_tree1.column("6", width=60)
            purch_tree1.column("7", width=60)
            purch_tree1.column("8", width=80)
            
            purch_tree1.heading("#0")
            purch_tree1.heading("1",text="ID/SKU")
            purch_tree1.heading("2",text="Product/Service")
            purch_tree1.heading("3",text="Description")
            purch_tree1.heading("4",text="Unit Price")
            purch_tree1.heading("5",text="Quantity")
            purch_tree1.heading("6",text="Pcs/Weight")
            purch_tree1.heading("7",text="Tax1")
            purch_tree1.heading("8",text="Price")

          # purch_tree1.pack(fill="both", expand=1)
          # listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

          elif ptaxdata[12] == "3":
            purch_tree1=ttk.Treeview(listFrame)
            purch_tree1["columns"]=["1","2","3","4","5","6","7","8","9"]

            purch_tree1.column("#0", width=40)
            purch_tree1.column("1", width=80)
            purch_tree1.column("2", width=190)
            purch_tree1.column("3", width=190)
            purch_tree1.column("4", width=80)
            purch_tree1.column("5", width=60)
            purch_tree1.column("6", width=60)
            purch_tree1.column("7", width=60)
            purch_tree1.column("8", width=60)
            purch_tree1.column("9", width=80)
            
            purch_tree1.heading("#0")
            purch_tree1.heading("1",text="ID/SKU")
            purch_tree1.heading("2",text="Product/Service")
            purch_tree1.heading("3",text="Description")
            purch_tree1.heading("4",text="Unit Price")
            purch_tree1.heading("5",text="Quantity")
            purch_tree1.heading("6",text="Pcs/Weight")
            purch_tree1.heading("7",text="Tax1")
            purch_tree1.heading("8",text="Tax2")
            purch_tree1.heading("9",text="Price")
          
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
          cost2=Label(labelframe1,text="Extra cost")
          cost2.place(x=35,y=35)
          pcost=Entry(labelframe1,width=10)
          pcost.place(x=115,y=35)
          # tax=Label(labelframe1,text="Tax1").place(x=420,y=35)
          # ptax=Entry(labelframe1,width=7).place(x=460,y=35)
          # tax2=Label(labelframe1,text="Tax1").place(x=420,y=35)
          # ptax2=Entry(labelframe1,width=7).place(x=460,y=35)
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
    except:
        try:
          pop1.destroy()
        except:
          pass
        messagebox.showerror('F-Billing Revolution', 'Select a record to edit.') 



#add new product
      def estimate_product():  
        pord_top = Toplevel()  
        pord_top.title("Add a new Product/Service")
        estimate_p2 = PhotoImage(file = 'images/fbicon.png')
        pord_top.iconphoto(False, estimate_p2)
      
        pord_top.geometry("600x550+390+15")
        pord_tabControl = ttk.Notebook(pord_top)
        pod_s = ttk.Style()
        pod_s.theme_use('default')
        pod_s.configure('TNotebook.Tab', background="#999999",padding=10,bd=0)


        pord_tab1 = ttk.Frame(pord_tabControl)
        pord_tab2 = ttk.Frame(pord_tabControl)
      
        pord_tabControl.add(pord_tab1,compound = LEFT, text ='Product/Service')
        pord_tabControl.add(pord_tab2,compound = LEFT, text ='Product Image')
      
        pord_tabControl.pack(expand = 1, fill ="both")

        global filename
        filename = ""

        def este_upload_file():
          global filename,img, b2
          f_types =[('Png files','.png'),('Jpg Files', '.jpg'),('PDF', '*.pdf',)]
          filename = filedialog.askopenfilename(filetypes=f_types)
          shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
          image = Image.open(filename)
          resize_image = image.resize((350, 350))
          img = ImageTk.PhotoImage(resize_image)
          b2 = Button(purchase_imageFrame,image=img)
          b2.place(x=130, y=80)
        
        def est_addproducts():
          global img , filename 
          sku = codeentry.get()
          status = checkvarStatus.get()
          catgory = n.get()
          name = nameentry.get()
          description = desentry.get()
          unitprice = unitentry.get()
          peices = pcsentry.get()
          cost = costentry.get()
          price_cost = priceentry.get()
          taxable = checkvarStatus2.get()
          tax2 = estimate_checkvarStatus_2.get()
          nostockcontrol = checkvarStatus3.get()
          stock = pod_stockentry.get()
          lowstock = lowentry.get()
          warehouse = wareentry.get()
          pnotes = txt.get("1.0",'end-1c')
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
              pord_top.destroy()

            for record in pur_add_cusventtree.get_children():
              pur_add_cusventtree.delete(record)
            fbcursor.execute("select *  from Productservice")
            pord_pandsdata = fbcursor.fetchall()
            countp = 0
            for i in pord_pandsdata:
              if i[12] == '1':
                servi = '🗹'
              else:
                servi = ''
              sql = "select currencysign,currsignplace from company"
              fbcursor.execute(sql)
              pordcurrsymb = fbcursor.fetchone()
              if not pordcurrsymb: 
                if i[13] > i[14]:
                  pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('green',))
                  countp += 1              
                elif i[12] == '1':
                  pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('blue',))
                  countp += 1
                else:
                  pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('red',))
                  countp += 1
                        
              elif pordcurrsymb[1] == "before amount":
                if (i[13]) > (i[14]):
                  pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],pordcurrsymb[0]+i[7],servi,i[13]),tags=('green',))
                  countp += 1
                elif i[12] == '1':
                  pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],pordcurrsymb[0]+i[7],servi,i[13]),tags=('blue',))
                  countp += 1
                else:
                  pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],pordcurrsymb[0]+i[7],servi,i[13]),tags=('red',))
                  countp += 1

              elif pordcurrsymb[1] == "before amount with space":
                if (i[13]) > (i[14]):
                  pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],pordcurrsymb[0] +" "+i[7],servi,i[13]),tags=('green',))
                  countp += 1
                elif i[12] == '1':
                  pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],pordcurrsymb[0] +" "+i[7],servi,i[13]),tags=('blue',))
                  countp += 1
                else:
                  pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],pordcurrsymb[0] +" "+i[7],servi,i[13]),tags=('red',))
                  countp += 1

              elif pordcurrsymb[1] == "after amount":
                if (i[13]) > (i[14]):
                  pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+pordcurrsymb[0],servi,i[13]),tags=('green',))
                  countp += 1
                elif i[12] == '1':
                  pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+pordcurrsymb[0],servi,i[13]),tags=('blue',))
                  countp += 1
                else:
                  pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+pordcurrsymb[0],servi,i[13]),tags=('red',))
                  countp += 1

              elif pordcurrsymb[1] == "after amount with space":
                if (i[13]) > (i[14]):
                  pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+" "+pordcurrsymb[0],servi,i[13]),tags=('green',))
                  countp += 1
                elif i[12] == '1':
                  pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+" "+pordcurrsymb[0],servi,i[13]),tags=('blue',))
                  countp += 1
                else:
                  pur_add_cusventtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+" "+pordcurrsymb[0],servi,i[13]),tags=('red',))
                  countp += 1

            pord_top.destroy()



#Preview estimate
    global prev_pord
    def prev_pord():
      sql = 'select * from company'
      fbcursor.execute(sql)
      pord_compdataord = fbcursor.fetchone()
      # if estimates_etemplate.get() == 'Professional 1 (logo on left side)':
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

        com_label = Label(canvas,text=" "+estimates_etitletext.get(),font=('Helvetica 10 '),background='white')
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

        canvas.create_text(520, 260, text=porderdate.get_date(), fill="black", font=('Helvetica 12')) 
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
        


        for record in purchase_tree.get_children():
          previewdata1 = list(purchase_tree.item(record, 'values'))
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
            
            com_label = Label(canvas,text=str(tax1.cget("text")),font=('Helvetica 10 '),background='white')
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
            
            com_label = Label(canvas,text=""+comcursign.get()+str(tax1.cget("text")),font=('Helvetica 10 '),background='white')
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
            
            com_label = Label(canvas,text=""+comcursign.get()+" "+str(tax1.cget("text")),font=('Helvetica 10 '),background='white')
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
            
            com_label = Label(canvas,text=str(tax1.cget("text"))+""+comcursign.get(),font=('Helvetica 10 '),background='white')
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
            
            com_label = Label(canvas,text=str(tax1.cget("text"))+" "+""+comcursign.get(),font=('Helvetica 10 '),background='white')
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
            
            com_label = Label(canvas,text=str(tax1.cget("text")),font=('Helvetica 10 '),background='white')
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
            
            com_label = Label(canvas,text=""+comcursign.get()+str(tax1.cget("text")),font=('Helvetica 10 '),background='white')
            com_label_window = canvas.create_window(975, 779, anchor="e", window=com_label)
    
            com_label = Label(canvas,text=""+comcursign.get()+str(tax2.cget("text")),font=('Helvetica 10 '),background='white')
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
            
            com_label = Label(canvas,text=""+comcursign.get()+" "+str(tax1.cget("text")),font=('Helvetica 10 '),background='white')
            com_label_window = canvas.create_window(975, 779, anchor="e", window=com_label)
  
            com_label = Label(canvas,text=""+comcursign.get()+" "+str(tax2.cget("text")),font=('Helvetica 10 '),background='white')
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
            
            com_label = Label(canvas,text=str(tax1.cget("text"))+""+comcursign.get(),font=('Helvetica 10 '),background='white')
            com_label_window = canvas.create_window(975, 779, anchor="e", window=com_label)
  
            com_label = Label(canvas,text=str(tax2.cget("text"))+""+comcursign.get(),font=('Helvetica 10 '),background='white')
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
            
            com_label = Label(canvas,text=str(tax1.cget("text"))+" "+""+comcursign.get(),font=('Helvetica 10 '),background='white')
            com_label_window = canvas.create_window(975, 779, anchor="e", window=com_label)  
  
            
            com_label = Label(canvas,text=str(tax2.cget("text"))+" "+""+comcursign.get(),font=('Helvetica 10 '),background='white')
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