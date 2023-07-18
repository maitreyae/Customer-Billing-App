import tkinter  # GuI
from tkinter import *
from tkinter import ttk
import random   #random variables for customer ref
import tkinter.messagebox
from datetime import datetime
import time
import pymongo  #driver for mongodb

class Customer:
    def __init__(self, root):
        self.root = root
        self.root.title("Book My Room")
        self.root.geometry("1350x670+0+0")
        root.minsize(1350, 670)
        root.maxsize(1350, 670)  # (x,y) parameters
        root.resizable(0, 0)
        self.root.config(background="#003333")

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient['CustomerDB']
        mycol = mydb['CustomerCol']

        #=================================================== variable declaration#

        CustomerRef = StringVar()
        Firstname = StringVar()
        Lastname = StringVar()
        Address = StringVar()
        PostCode = StringVar()
        Mobile = StringVar()
        Email = StringVar()
        Natinality = StringVar()
        DOB = StringVar()
        IDType = StringVar()
        Gender = StringVar()
        CheckInDate = StringVar()
        CheckOutDate = StringVar()
        Meal = StringVar()
        RoomType = StringVar()
        RoomNo = StringVar()
        TotalCost = StringVar()
        SubTotal = StringVar()
        PaidTax = StringVar()
        TotalDays = StringVar()

        CustomerRef.set(random.randint(1980, 9875648))
        #============================================#
        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        var6=IntVar()
        var7=IntVar()
        var8=IntVar()

        E_Sprite = StringVar()
        E_Pepsi = StringVar()
        E_Popcorn = StringVar()
        E_Sandwitch = StringVar()
        E_Nachos = StringVar()
        E_Fanta = StringVar()
        E_CocaCola = StringVar()
        E_ColdCoffee = StringVar()

        E_Sprite.set("0")
        E_Pepsi.set("0")
        E_Popcorn.set("0")
        E_Sandwitch.set("0")
        E_Nachos.set("0")
        E_Fanta.set("0")
        E_CocaCola.set("0")
        E_ColdCoffee.set("0")

        #========================================================================================#
        #<---------------------------Exit Button Functionality---------------------------------->#
        def iExit():
            iExit = tkinter.messagebox.askyesno("Exit Booking Application","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
        #========================================================================================#

        #========================================================================================#
        #<---------------------------Reset Button Functionality---------------------------------->#
        def Reset():
            Firstname.set("")
            CustomerRef.set("")
            Lastname.set("")
            Address.set("")
            PostCode.set("")
            Mobile.set("")
            Email.set("")
            Natinality.set("")
            DOB.set("")
            IDType.set("")
            Gender.set("")
            CheckInDate.set("")
            CheckOutDate.set("")
            Meal.set("")
            RoomType.set("")
            RoomNo.set("")
            TotalCost.set("")
            SubTotal.set("")
            PaidTax.set("")
            TotalDays.set("")

            txtSprite.configure(state = DISABLED)
            txtPepsi.configure(state = DISABLED)
            txtPopcorn.configure(state = DISABLED)
            txtSandwitch.configure(state = DISABLED)
            txtNachos.configure(state = DISABLED)
            txtFanta.configure(state = DISABLED)
            txtCocaCola.configure(state = DISABLED)
            txtColdCoffee.configure(state = DISABLED)  #will be changed to enabled when boolean value changes to 1

            E_Sprite.set("0")
            E_Pepsi.set("0")
            E_Popcorn.set("0")
            E_Sandwitch.set("0")
            E_Nachos.set("0")
            E_Fanta.set("0")
            E_CocaCola.set("0")
            E_ColdCoffee.set("0")

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)

            self.txtReceipt.delete("1.0","end")

        #========================================================================================#

        #========================================================================================#
        #<----------------------Menu Button Functionality---------------------------------->#
        def chkSprite():
            if(var1.get() == 1):
                txtSprite.configure(state = NORMAL)
                txtSprite.focus()
                txtSprite.delete('0',END)
                E_Sprite.set("")
            elif(var1.get() == 0):
                txtSprite.configure(state = DISABLED)
                E_Sprite.set("0")

        def chkPepsi():
            if(var2.get() == 1):
                txtPepsi.configure(state = NORMAL)
                txtPepsi.focus()
                txtPepsi.delete('0',END)
                E_Pepsi.set("")
            elif(var1.get() == 0):
                txtPepsi.configure(state = DISABLED)
                E_Pepsi.set("0")

        def chkPopcorn():
            if(var3.get() == 1):
                txtPopcorn.configure(state = NORMAL)
                txtPopcorn.focus()
                txtPopcorn.delete('0',END)
                E_Popcorn.set("")
            elif(var3.get() == 0):
                txtPopcorn.configure(state = DISABLED)
                E_Popcorn.set("0")

        def chkSandwitch():
            if(var4.get() == 1):
                txtSandwitch.configure(state = NORMAL)
                txtSandwitch.focus()
                txtSandwitch.delete('0',END)
                E_Sandwitch.set("")
            elif(var4.get() == 0):
                txtSandwitch.configure(state = DISABLED)
                E_Sandwitch.set("0")

        def chkNachos():
            if(var5.get() == 1):
                txtNachos.configure(state = NORMAL)
                txtNachos.focus()
                txtNachos.delete('0',END)
                E_Nachos.set("")
            elif(var5.get() == 0):
                txtNachos.configure(state = DISABLED)
                E_Nachos.set("")

        def chkFanta():
            if(var6.get() == 1):
                txtFanta.configure(state = NORMAL)
                txtFanta.focus()
                txtFanta.delete('0',END)
                E_Fanta.set("")
            elif(var6.get() == 0):
                txtFanta.configure(state = DISABLED)
                E_Fanta.set("")

        def chkCocaCola():
            if(var7.get() == 1):
                txtCocaCola.configure(state = NORMAL)
                txtCocaCola.focus()
                txtCocaCola.delete('0',END)
                E_CocaCola.set("")
            elif(var7.get() == 0):
                txtCocaCola.configure(state =  DISABLED)
                E_CocaCola.set("")

        def chkColdCoffee():
            if(var8.get() == 1):
                txtColdCoffee.configure(state = NORMAL)
                txtColdCoffee.focus()
                txtColdCoffee.delete('0',END)
                E_ColdCoffee.set("")
            elif(var8.get() == 0):
                txtColdCoffee.configure(state = DISABLED)
                E_ColdCoffee.set("")
        #========================================================================================#

        #========================================================================================#
        #<----------------------Total Button Functionality---------------------------------->#
        def Total():
            Item1=float(E_Sprite.get())
            Item2=float(E_Pepsi.get())
            Item3=float(E_Popcorn.get())
            Item4=float(E_Sandwitch.get())
            Item5=float(E_Nachos.get())
            Item6=float(E_Fanta.get())
            Item7=float(E_CocaCola.get())
            Item8=float(E_ColdCoffee.get())

            Tax = ((Item1 + Item2 + Item3 + Item4 + Item5 + Item6 + Item7 + Item8)*1.59)
            Tax = "Rs",str('%.2f'%(Tax))
            PaidTax.set(Tax)
            SubTotalCalc1 = (Item1 * 65) + (Item2 * 75) + (Item3 * 99) + (Item4 * 130) + (Item5 * 180) + (Item6 * 75) + (Item7 * 75) + (Item8 * 89)
            SubTotalCalc  = "Rs",str('%.2f'%(SubTotalCalc1))
            SubTotal.set(SubTotalCalc)
            TotalCalc = SubTotalCalc1 * 1.59
            TotalCalc = "Rs",str('%.2f'%(TotalCalc))
            TotalCost.set(TotalCalc)

            self.txtReceipt.insert(END,'\t\tInformation:\n')
            self.txtReceipt.insert(END,'Customer Ref:\t'+CustomerRef.get() +'\t\t\t\t'+ 'Name:\t' + Firstname.get() + ' ' + Lastname.get()  +'\n')
            self.txtReceipt.insert(END,'Address:\t'+ Address.get()+'\n')
            self.txtReceipt.insert(END,'Mobile:\t'+ Mobile.get()+'\n')
            self.txtReceipt.insert(END,'Email:\t'+ Email.get()+ '\n')
            self.txtReceipt.insert(END,'Items\t\t\t\t' + '\n')
            self.txtReceipt.insert(END,'Sprite:\t\t\t\t\t' + E_Sprite.get() +'\n')
            self.txtReceipt.insert(END,'Pepsi:\t\t\t\t\t'+ E_Pepsi.get()+'\n')
            self.txtReceipt.insert(END,'Popcorn:\t\t\t\t\t'+ E_Popcorn.get()+'\n')
            self.txtReceipt.insert(END,'Sandwitch:\t\t\t\t\t'+ E_Sandwitch.get()+'\n')
            self.txtReceipt.insert(END,'Nachos:\t\t\t\t\t'+ E_Nachos.get()+'\n')
            self.txtReceipt.insert(END,'Fanta:\t\t\t\t\t'+ E_Fanta.get()+'\n')
            self.txtReceipt.insert(END,'CocaCola:\t\t\t\t\t'+ E_CocaCola.get()+'\n')
            self.txtReceipt.insert(END,'ColdCoffee:\t\t\t\t\t'+ E_ColdCoffee.get()+'\n')
            self.txtReceipt.insert(END,'Tax Paid:\t\t\t\t'+PaidTax.get()+"\n")
            self.txtReceipt.insert(END,'SubTotal:\t\t\t\t'+str(SubTotal.get())+"\n")
            self.txtReceipt.insert(END,'Total Cost:\t\t\t\t'+str(TotalCost.get())+"\n")

        #========================================================================================#

        #========================================================================================#
        #<----------------------Save and View Button Functionality---------------------------------->#,
#dtabase
        def saveToDB():
            myData = {"CustomerRef":CustomerRef.get(),
                      "Firstname":Firstname.get(),
                      "Lastname":Lastname.get(),
                      "Address":Address.get(),
                      "Mobile":Mobile.get(),
                      "Email":Email.get(),
                      "TotalCost":TotalCost.get()}
            x = mycol.insert_one(myData) 
            #insert_one inbuilt method of pymongo

        def showFromDB():
            self.txtReceipt.delete("1.0","end")
            myShowData1 = mycol.find({}).sort('_id',-1).limit(1)
            for myShowData in myShowData1:
                self.txtReceipt.insert(END,'Customer Ref.:\t'+ myShowData['CustomerRef'] + '\n')
                self.txtReceipt.insert(END,'Name\t'+ myShowData['Firstname'] + ' ' + myShowData['Lastname'] + '\n')
                self.txtReceipt.insert(END,'Address:\t'+ myShowData['Address'] + '\n')
                self.txtReceipt.insert(END,'Mobile:\t'+ myShowData['Mobile'] + '\n')
                self.txtReceipt.insert(END,'Email:\t'+ myShowData['Email'] + '\n')
                self.txtReceipt.insert(END,'TotalCost:\t'+ myShowData['TotalCost'] + '\n')



        #========================================================================================#

        #========================================================================================#
        #<----------------------Coldrink  Button Functionality---------------------------------->#

        #Define Frames
        MainFrame = Frame(self.root, bg="#003333",bd=5, relief=RIDGE)
        MainFrame.grid()
        topFrame = Frame(MainFrame, bd=5, width=1700,height=100, padx=20,pady=20, bg="#AEC2B6",highlightbackground="red", relief=GROOVE)
        topFrame.grid(row=0,column=0, columnspan=4,sticky="W")
        MiddleLeftFrame = Frame(MainFrame, bd=5, width=450,height=488, padx=10, bg="#AEC2B6",highlightbackground="#003333", relief=GROOVE)
        MiddleLeftFrame.grid(row=1,column=0,sticky="W")
        MiddleCenterFrame = Frame(MainFrame, bd=5, width=450,height=488,pady=6, padx=10, bg="#94AF9F",highlightbackground="#003333", relief=GROOVE)
        MiddleCenterFrame.grid(row=1,column=1,sticky="W")
        MiddleRightFrame = Frame(MainFrame, bd=5, width=450,height=488, padx=10, bg="#AEC2B6",highlightbackground="#003333", relief=GROOVE)
        MiddleRightFrame.grid(row=1,column=2,sticky="W")
        MiddleRightTopFrame = Frame(MiddleRightFrame, bd=5, width=450, height=340,pady=8, padx=20, bg="#AEC2B6",highlightbackground="#003333", relief=GROOVE)
        MiddleRightTopFrame.grid(row=0,column=0,sticky="W")
        MiddleRightBottomFrame = Frame(MiddleRightFrame, bd=5, width=450, height=150,pady=8, padx=20, bg="black",highlightbackground="#003333", relief=GROOVE)
        MiddleRightBottomFrame.grid(row=1,column=0,sticky="W")

        Date1 = StringVar()
        Time1 = StringVar()
        Date1.set(time.strftime("%d/%m/%Y"))
        Time1.set(time.strftime("%H:%M:%S"))
        self.lblTitle = Label(topFrame, textvariable=Date1, font=('consolas',30,'bold'),pady=9,padx=61.5, bd=5,bg="black", fg="Cornsilk").grid(row=0,column=0)
        self.lblTitle = Label(topFrame, text="Book My Room", font=('consolas',40,'bold'),pady=9,padx=61.5, bd=5,bg="black", fg="Cornsilk").grid(row=0,column=1)
        self.lblTitle = Label(topFrame, textvariable=Time1, font=('consolas',30,'bold'),pady=9,padx=61.5, bd=5,bg="black", fg="Cornsilk").grid(row=0,column=2)

        #==================================================#

        self.lblCus_Ref = Label(MiddleLeftFrame, font=('consolas', 12,'bold'), text="Customer Ref.",padx=2, pady=2, fg="Cornsilk", bg="#2C3333")
        self.lblCus_Ref.grid(row=0,column=0, sticky=W)
        self.txtCus_Ref = Entry(MiddleLeftFrame, font=('consolas',12,'bold'),width=20, textvariable=CustomerRef)
        self.txtCus_Ref.grid(row=0,column=1,pady=3,padx=20)

        self.lblFirstname = Label(MiddleLeftFrame, font=('consolas',12,'bold'),text="Firstname",padx=2, pady=2, fg="Cornsilk", bg="#2C3333")
        self.lblFirstname.grid(row=1,column=0, sticky=W)
        self.txtFirstname = Entry(MiddleLeftFrame, font=('consolas',12,'bold'),width=20,textvariable=Firstname)
        self.txtFirstname.grid(row=1,column=1,pady=3,padx=20)

        self.lblLastname = Label(MiddleLeftFrame, font=('consolas',12,'bold'),text="Lastname",padx=2, pady=2, fg="Cornsilk", bg="#2C3333")
        self.lblLastname.grid(row=2,column=0, sticky=W)
        self.txtLastname = Entry(MiddleLeftFrame, font=('consolas',12,'bold'),width=20,textvariable=Lastname)
        self.txtLastname.grid(row=2,column=1,pady=3,padx=20)

        self.lblAddress = Label(MiddleLeftFrame, font=('consolas',12,'bold'),text="Address",padx=2, pady=2, fg="Cornsilk", bg="#2C3333")
        self.lblAddress.grid(row=3,column=0, sticky=W)
        self.txtAddress = Entry(MiddleLeftFrame, font=('consolas',12,'bold'),width=20,textvariable=Address)
        self.txtAddress.grid(row=3,column=1,pady=3,padx=20)

        self.lblPostCode = Label(MiddleLeftFrame, font=('consolas',12 ,'bold'),text="PostCode",padx=2, pady=2, fg="Cornsilk", bg="#2C3333")
        self.lblPostCode.grid(row=4,column=0, sticky=W)
        self.txtPostCode = Entry(MiddleLeftFrame, font=('consolas',12,'bold'),width=20,textvariable=PostCode)
        self.txtPostCode.grid(row=4,column=1,pady=3,padx=20)

        self.lblMobile = Label(MiddleLeftFrame, font=('consolas',12,'bold'),text="Mobile",padx=2, pady=2, fg="Cornsilk", bg="#2C3333")
        self.lblMobile.grid(row=5,column=0, sticky=W)
        self.txtMobile = Entry(MiddleLeftFrame, font=('consolas',12,'bold'),width=20,textvariable=Mobile)
        self.txtMobile.grid(row=5,column=1,pady=3,padx=20)

        self.lblEmail = Label(MiddleLeftFrame, font=('consolas',12,'bold'),text="Email",padx=2, pady=2, fg="Cornsilk", bg="#2C3333")
        self.lblEmail.grid(row=6,column=0, sticky=W)
        self.txtEmail = Entry(MiddleLeftFrame, font=('',12,'bold'),width=20,textvariable=Email)
        self.txtEmail.grid(row=6,column=1,pady=3,padx=20)

        self.lblNatinality = Label(MiddleLeftFrame, font=('consolas',12,'bold'),text="Nationality",padx=2, pady=2, fg="Cornsilk", bg="#2C3333")
        self.lblNatinality.grid(row=7,column=0, sticky=W)
        self.txtNatinality = ttk.Combobox(MiddleLeftFrame, font=('consolas',12,'bold'),textvariable=Natinality,state="readonly",width=18)
        self.txtNatinality['value'] = ('','British','Nigeria','Kenya','India','Iran','Morocco','Canada','France','Norway')
        self.txtNatinality.current(0)
        self.txtNatinality.grid(row=7,column=1,pady=3,padx=20)

        self.lblDOB = Label(MiddleLeftFrame, font=('consolas',12,'bold'),text="Date of Birthday",padx=2, pady=2, fg="Cornsilk", bg="#2C3333")
        self.lblDOB.grid(row=8,column=0, sticky=W)
        self.txtDOB = Entry(MiddleLeftFrame, font=('consolas',12,'bold'),width=20,textvariable=DOB)
        self.txtDOB.grid(row=8,column=1,pady=3,padx=20)

        self.lblIDType = Label(MiddleLeftFrame, font=('consolas',12,'bold'),text="Type of Id",padx=2, pady=2, fg="Cornsilk", bg="#2C3333")
        self.lblIDType.grid(row=9,column=0, sticky=W)
        self.txtIDType = ttk.Combobox(MiddleLeftFrame, font=('consolas',12,'bold'),textvariable=IDType,state="readonly",width=18)
        self.txtIDType['value'] = ('','Driving Licence','AdharCard','PassPort')
        self.txtIDType.current(0)
        self.txtIDType.grid(row=9,column=1,pady=3,padx=20)

        self.lblGender = Label(MiddleLeftFrame, font=('consolas',12,'bold'),text="Gender",padx=2, pady=2, fg="Cornsilk", bg="#2C3333")
        self.lblGender.grid(row=10,column=0, sticky=W)
        self.txtGender = ttk.Combobox(MiddleLeftFrame, font=('consolas',12,'bold'),textvariable=Gender,state="readonly",width=18)
        self.txtGender['value'] = ('','Male','Female')
        self.txtGender.current(0)
        self.txtGender.grid(row=10,column=1,pady=3,padx=20)

        self.lblCheckInDate = Label(MiddleLeftFrame, font=('consolas',12,'bold'),text="Check In Date",padx=2, pady=2, fg="Cornsilk", bg="#2C3333")
        self.lblCheckInDate.grid(row=11,column=0, sticky=W)
        self.txtCheckInDate = Entry(MiddleLeftFrame, font=('consolas',12,'bold'),width=20,textvariable=Date1)
        self.txtCheckInDate.grid(row=11,column=1,pady=3,padx=20)

        self.lblCheckOutDate = Label(MiddleLeftFrame, font=('consolas',12,'bold'),text="Check Out Date",padx=2, pady=2, fg="Cornsilk", bg="#2C3333")
        self.lblCheckOutDate.grid(row=12,column=0, sticky=W)
        self.txtCheckOutDate = Entry(MiddleLeftFrame, font=('consolas',12,'bold'),width=20,textvariable=Date1)
        self.txtCheckOutDate.grid(row=12,column=1,pady=3,padx=20)

        self.lblMeal = Label(MiddleLeftFrame, font=('consolas',12,'bold'),text="Meal",padx=2, pady=2, fg="Cornsilk", bg="#2C3333")
        self.lblMeal.grid(row=13,column=0, sticky=W)
        self.txtMeal = ttk.Combobox(MiddleLeftFrame, font=('consolas',12,'bold'),textvariable=Meal,width=18,state="readonly")
        self.txtMeal['value'] = ('','Breakfast','Lunch','Dinner')
        self.txtMeal.current(0)
        self.txtMeal.grid(row=13,column=1,pady=3,padx=20)

        self.lblTicketType = Label(MiddleLeftFrame, font=('consolas',12,'bold'),text="Room Type",padx=2, pady=2, fg="Cornsilk", bg="#2C3333")
        self.lblTicketType.grid(row=14,column=0, sticky=W)
        self.txtTicketType = ttk.Combobox(MiddleLeftFrame, font=('consolas',12,'bold'),textvariable=RoomType,width=18,state="readonly")
        self.txtTicketType['value'] = ('','Single','Double','Family')
        self.txtTicketType.current(0)
        self.txtTicketType.grid(row=14,column=1,pady=3,padx=20)

        self.lblScreenNo = Label(MiddleLeftFrame, font=('consolas',12,'bold'),text="Room No.",padx=2, pady=2, fg="Cornsilk", bg="#2C3333")
        self.lblScreenNo.grid(row=15,column=0, sticky=W)
        self.txtScreenNo = Entry(MiddleLeftFrame, font=('consolas',12,'bold'),width=20,textvariable=RoomNo)
        #self.txtScreenNo.grid(row=15,column=1,pady=3,padx=20)
        self.txtScreenNo.grid(row=15,column=1,pady=3,padx=20)
        #===================================================#



        Sprite=Checkbutton(MiddleCenterFrame,text='Sprite',variable=var1,onvalue=1,offvalue=0,font=('consolas',18,'bold'),
                            bg='#BBD6B8',command=chkSprite).grid(row=0,sticky=W)
        Pepsi=Checkbutton(MiddleCenterFrame,text='Pepsi',variable=var2,onvalue=1,offvalue=0,font=('consolas',18,'bold'),
                            bg='#BBD6B8',command=chkPepsi).grid(row=1,sticky=W)
        Popcorn=Checkbutton(MiddleCenterFrame,text='Popcorn',variable=var3,onvalue=1,offvalue=0,font=('consolas',18,'bold'),
                            bg='#BBD6B8',command=chkPopcorn).grid(row=2,sticky=W)
        Sandwitch=Checkbutton(MiddleCenterFrame,text='Sandwitch',variable=var4,onvalue=1,offvalue=0,font=('consolas',18,'bold'),
                            bg='#BBD6B8',command=chkSandwitch).grid(row=3,sticky=W)
        Nachos=Checkbutton(MiddleCenterFrame,text='Nachos',variable=var5,onvalue=1,offvalue=0,font=('consolas',18,'bold'),
                            bg='#BBD6B8',command=chkNachos).grid(row=4,sticky=W)
        Fanta=Checkbutton(MiddleCenterFrame,text='Fanta',variable=var6,onvalue=1,offvalue=0,font=('consolas',18,'bold'),
                            bg='#BBD6B8',command=chkFanta).grid(row=5,sticky=W)
        CocaCola=Checkbutton(MiddleCenterFrame,text='CocaCola',variable=var7,onvalue=1,offvalue=0,font=('consolas',18,'bold'),
                            bg='#BBD6B8',command=chkCocaCola).grid(row=6,sticky=W)
        ColdCoffee=Checkbutton(MiddleCenterFrame,text='ColdCoffee',variable=var8,onvalue=1,offvalue=0,font=('consolas',18,'bold'),
                            bg='#BBD6B8',command=chkColdCoffee).grid(row=7,sticky=W)
        ##############################################Drink Entry###############################################################

        txtSprite = Entry(MiddleCenterFrame,font=('consolas',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                                ,textvariable=E_Sprite)
        txtSprite.grid(row=0,column=1)

        txtPepsi = Entry(MiddleCenterFrame,font=('consolas',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                                ,textvariable=E_Pepsi)
        txtPepsi.grid(row=1,column=1)

        txtPopcorn = Entry(MiddleCenterFrame,font=('consolas',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                                ,textvariable=E_Popcorn)
        txtPopcorn.grid(row=2,column=1)

        txtSandwitch= Entry(MiddleCenterFrame,font=('consolas',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                                ,textvariable=E_Sandwitch)
        txtSandwitch.grid(row=3,column=1)

        txtNachos = Entry(MiddleCenterFrame,font=('consolas',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                                ,textvariable=E_Nachos)
        txtNachos.grid(row=4,column=1)

        txtFanta = Entry(MiddleCenterFrame,font=('consolas',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                                ,textvariable=E_Fanta)
        txtFanta.grid(row=5,column=1)

        txtCocaCola = Entry(MiddleCenterFrame,font=('consolas',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                                ,textvariable=E_CocaCola)
        txtCocaCola.grid(row=6,column=1)

        txtColdCoffee = Entry(MiddleCenterFrame,font=('consolas',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                                ,textvariable=E_ColdCoffee)
        txtColdCoffee.grid(row=7,column=1)

        self.lblTitle = Label(MiddleCenterFrame, text="Tax and Total Sum", font=('consolas',20,'bold'), bd=5,bg="black", fg="Cornsilk").grid(row=8,column=0,columnspan=2)

        self.lblPaidTax = Label(MiddleCenterFrame, font=('consolas',12,'bold'),text="Tax",padx=2, pady=2, fg="black", bg="#BBD6B8")
        self.lblPaidTax.grid(row=9,column=0, sticky=W)
        self.txtPaidTax = Entry(MiddleCenterFrame, font=('consolas',12,'bold'),width=10,textvariable=PaidTax,state="readonly")
        self.txtPaidTax.grid(row=9,column=1,pady=3,padx=20)

        self.lblSubTotal = Label(MiddleCenterFrame, font=('consolas',12,'bold'),text="Sub Total",padx=2, pady=2, fg="black", bg="#BBD6B8")
        self.lblSubTotal.grid(row=10,column=0, sticky=W)
        self.txtSubTotal = Entry(MiddleCenterFrame, font=('consolas',12,'bold'),width=10,textvariable=SubTotal,state="readonly")
        self.txtSubTotal.grid(row=10,column=1,pady=3,padx=20)

        self.lblTotalCost = Label(MiddleCenterFrame, font=('consolas',12,'bold'),text="Total Cost",padx=2, pady=2, fg="black", bg="#BBD6B8")
        self.lblTotalCost.grid(row=11,column=0, sticky=W)
        self.txtTotalCost = Entry(MiddleCenterFrame, font=('consolas',12,'bold'),width=10,textvariable=TotalCost,state="readonly")
        self.txtTotalCost.grid(row=11,column=1,pady=3,padx=20)

        #===================================================#
        self.txtReceipt = Text(MiddleRightTopFrame, height=22, width=73, bd=10, font=('consolas',9,'bold'))
        self.txtReceipt.grid(row=0,column=0)
        #===================================================#
        self.btnTotal = Button(MiddleRightBottomFrame, bd=5, fg="white", font=('consolas',16,'bold'), width=7, height=1, bg="#003333", text="Total", command=Total).grid(row=0,column=0)
        self.btnReset = Button(MiddleRightBottomFrame, bd=5, fg="white", font=('consolas',16,'bold'), width=7, height=1, bg="#003333", text="Reset", command=Reset).grid(row=0,column=1)
        self.btnExit = Button(MiddleRightBottomFrame, bd=5, fg="white", font=('consolas',16,'bold'), width=7, height=1, bg="#003333", text="Exit", command=iExit).grid(row=0,column=2)
        self.btnSave = Button(MiddleRightBottomFrame, bd=5, fg="white", font=('consolas',16,'bold'), width=7, height=1, bg="#003333", text="Save", command=saveToDB).grid(row=0,column=3)
        self.btnPreview = Button(MiddleRightBottomFrame, bd=5, fg="white", font=('consolas',16,'bold'), width=7, height=1, bg="#003333", text="View", command=showFromDB).grid(row=0,column=4)
        #===================================================#



#accessing the main function declared above
if __name__ == '__main__':
    root = Tk()  #module
    app = Customer(root)
    root.mainloop()
