from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime



class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1400x700+0+0")

        #====================================================variable======================================================

        
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.duedate_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()






        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",40,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)
        #===========================DataFrame Left=============================
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",15,"bold"))
        DataFrameLeft.place(x=0,y=5,width=860,height=350)
        
        lblMember=Label(DataFrameLeft,font=("arial",12,"bold"),bg="powder blue",text="Member Type",padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)
        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("arial",12,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.current(0)
        comMember.grid(row=0,column=1)

        lblPRN_No=Label(DataFrameLeft,bg="powder blue",text="PRN No:",font=("arial",12,"bold"),padx=2)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.prn_var,width=29)
        txtPRN_NO.grid(row=1,column=1)

        lblIdNo=Label(DataFrameLeft,bg="powder blue",text="ID No:",padx=2,pady=4,font=("arial",12,"bold"))
        lblIdNo.grid(row=2,column=0,sticky=W)
        txtIdNO=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.id_var,width=29)
        txtIdNO.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,bg="powder blue",text="First Name",padx=2,pady=6,font=("arial",12,"bold"))
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,bg="powder blue",text="Last Name",padx=2,pady=6,font=("arial",12,"bold"))
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=4,column=1)

        lblAddress1=Label(DataFrameLeft,bg="powder blue",text="Address1",padx=2,pady=6,font=("arial",12,"bold"))
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address1_var,width=29)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,bg="powder blue",text="Address2",padx=2,pady=6,font=("arial",12,"bold"))
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address2_var,width=29)
        txtAddress2.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,bg="powder blue",text="Post code",pady=4,font=("arial",12,"bold"),padx=2)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.postcode_var,width=29)
        txtPostCode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,bg="powder blue",text="Mobile",pady=6,font=("arial",12,"bold"),padx=2)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtMobile.grid(row=8,column=1)

        lblBookId=Label(DataFrameLeft,bg="powder blue",text="Book Id:",pady=6,font=("arial",12,"bold"),padx=2)
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.bookid_var,width=29)
        txtBookId.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,bg="powder blue",text="Book Title:",font=("arial",12,"bold"),padx=2)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.booktitle_var,width=29)
        txtBookTitle.grid(row=1,column=3)

        lblAuthorName=Label(DataFrameLeft,bg="powder blue",text="Author Name:",pady=6,font=("arial",12,"bold"),padx=2)
        lblAuthorName.grid(row=2,column=2,sticky=W)
        txtAuthorName=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.author_var,width=29)
        txtAuthorName.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,bg="powder blue",text="Date Borrowed:",pady=6,font=("arial",12,"bold"),padx=2)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtDateBorrowed.grid(row=3,column=3,sticky=W)

        lblDueDate=Label(DataFrameLeft,bg="powder blue",text="Due Date:",pady=6,font=("arial",12,"bold"),padx=2)
        lblDueDate.grid(row=4,column=2,sticky=W)
        txtDueDate=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.duedate_var,width=29)
        txtDueDate.grid(row=4,column=3)

        lblDaysOnBook=Label(DataFrameLeft,bg="powder blue",text="Days On Book:",pady=6,font=("arial",12,"bold"),padx=2)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.daysonbook_var,width=29)
        txtDaysOnBook.grid(row=5,column=3)

        lblLateReturnFine=Label(DataFrameLeft,bg="powder blue",text="Late Return Fine:",pady=6,font=("arial",12,"bold"),padx=2)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.latereturnfine_var,width=29)
        txtLateReturnFine.grid(row=6,column=3)

        lblDateOverDue=Label(DataFrameLeft,bg="powder blue",text="Date Over Due:",pady=6,font=("arial",12,"bold"),padx=2)
        lblDateOverDue.grid(row=7,column=2,sticky=W)
        txtDateOverDue=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateoverdue_var,width=29)
        txtDateOverDue.grid(row=7,column=3)

        lblActualPrice=Label(DataFrameLeft,bg="powder blue",text="Actual Price:",pady=6,font=("arial",12,"bold"),padx=2)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.finalprice_var,width=29)
        txtActualPrice.grid(row=8,column=3)
       #==================================Data Frame Right==============================================



        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",padx=20,fg="green",bd=12,relief=RIDGE,font=("arial",12,"bold"))
        DataFrameRight.place(x=870,y=5,width=580,height=350)
        
        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)
        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")
        listBooks=["Head Firt Book","Learn Python The Hard Way","Python Programming","Secrete Rahshy","Python CookBook",
                 "Intro to Machine Learning"]
        
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            X=value
            if(X=="Head Firt Book"):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Paul Berry")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.788")
            elif(X=="Learn Python The Hard Way"):
                self.bookid_var.set("BKID8796")
                self.booktitle_var.set("Basics Of Python")
                self.author_var.set("ZED A.SHAN")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.725")

            elif(X=="Python Programming"):
                self.bookid_var.set("BKID1245")
                self.booktitle_var.set("Intro to python Comp science")
                self.author_var.set("John Zhelle")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.500")
            elif(X=="Secrete Rahshy"):
                self.bookid_var.set("BKID8796")
                self.booktitle_var.set("Basic Of Python")
                self.author_var.set("Ref.Kapil Kamble")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.289")

            elif(X=="Python CookBook"):
                self.bookid_var.set("BKID2546")
                self.booktitle_var.set("Python Cookbook")
                self.author_var.set("Brian Jones")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.354")

            elif(X=="Intro to Machine Learning"):
                self.bookid_var.set("BKID8796")
                self.booktitle_var.set("Intro to Machine Learning")
                self.author_var.set("Sarah Guaido")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.725")


        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)
         
        #===============================Button Frame============================================

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1530,height=70)
        
        btnAddData=Button(Framebutton,command=self.add_data,text="AddData",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,command=self.showData,text="ShowData",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)








        #==============================Information Frame================================
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=590,width=1530,height=210)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=190)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)


        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname","address1","address2",
                                                           "postid","mobile","bookid","booktitle","auther","dateborrowed","duedate",
                                                           "days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y) 

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No.")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post Id")
        self.library_table.heading("bookid",text="Book Id")
        self.library_table.heading("mobile",text="Mobile Number")

        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("auther",text="Auther")
        self.library_table.heading("dateborrowed",text="Date Of Borrowed")
        self.library_table.heading("duedate",text="Due Date")
        self.library_table.heading("days",text="Days")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("dateoverdue",text="Date Over Due")
        self.library_table.heading("finalprice",text="Final Price")


        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        
        self.library_table.column("membertype",width=100)
        
        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("auther",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("duedate",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        
    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="karnu@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.member_var.get(),
            self.prn_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.author_var.get(),
            self.dateborrowed_var.get(),
            self.duedate_var.get(),
            self.daysonbook_var.get(),
            self.latereturnfine_var.get(),
            self.dateoverdue_var.get(),
            self.finalprice_var.get()
        ))
        conn.commit()
        self.fatch_data()
        conn.close()

        messagebox.showinfo("Success","Member Has been inserted successfully")
    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="karnu@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set MemberType=%s,IDNo=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,Post code=%s,Mobile Number=%s,Book Id=%s,BookTitle=%s,Author=%s,DateBorrowed=%s,DueDate=%s,DaysOnBook=%s,LateReturnFine=%s,DateOverDue=%s,FinalPrice=%s where PRN_No=%s",(
            self.member_var.get(),
           
            self.id_var.get(""),
            self.firstname_var.get(""),
            self.lastname_var.get(""),
            self.address1_var.get(""),
            self.address2_var.get(""),
            self.postcode_var.get(""),
            self.mobile_var.get(""),
            self.bookid_var.get(""),
            self.booktitle_var.get(""),
            self.author_var.get(""),
            self.dateborrowed_var.get(""),
            self.duedate_var.get(""),
            self.daysonbook_var.get(""),
            self.latereturnfine_var.get(""),
            self.dateoverdue_var.get(""),
            self.finalprice_var.get(""),
            self.prn_var.get(""),                     
                      
        ))
        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("Success","Member has been Updated")

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="karnu@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        
        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.duedate_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finalprice_var.set(row[17])
    def showData(self):
        self.txtBox.insert(END,"Member Type\t\t"+self.member_var.get()+"\n")
        self.txtBox.insert(END,"PRN No\t\t"+self.prn_var.get()+"\n")
        self.txtBox.insert(END,"ID No\t\t"+self.id_var.get()+"\n")
        self.txtBox.insert(END,"FirstName\t\t"+self.firstname_var.get()+"\n")
        self.txtBox.insert(END,"LastName\t\t"+self.lastname_var.get()+"\n")
        self.txtBox.insert(END,"Address1\t\t"+self.address1_var.get()+"\n")
        self.txtBox.insert(END,"Address2\t\t"+self.address2_var.get()+"\n")
        self.txtBox.insert(END,"Post Code\t\t"+self.postcode_var.get()+"\n")
        self.txtBox.insert(END,"Mobile No\t\t"+self.mobile_var.get()+"\n")
        self.txtBox.insert(END,"Book ID\t\t"+self.bookid_var.get()+"\n")
        self.txtBox.insert(END,"Book Title\t\t"+self.booktitle_var.get()+"\n")
        self.txtBox.insert(END,"Author\t\t"+self.author_var.get()+"\n")
        self.txtBox.insert(END,"DateBorrowed\t\t"+self.dateborrowed_var.get()+"\n")
        self.txtBox.insert(END,"DueDate\t\t"+self.duedate_var.get()+"\n")
        self.txtBox.insert(END,"DaysOnBook\t\t"+self.daysonbook_var.get()+"\n")
        self.txtBox.insert(END,"LateReturnFine\t\t"+self.latereturnfine_var.get()+"\n")
        self.txtBox.insert(END,"DateOverDue\t\t"+self.dateoverdue_var.get()+"\n")
        self.txtBox.insert(END,"FinalPrice\t\t"+self.finalprice_var.get()+"\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.duedate_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set(""),
        self.txtBox.delete("1.0",END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return
        
    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First Select the Member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="karnu@123",database="mydata")
            my_cursor=conn.cursor()
            query="delete from library where PRN_No=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()
            messagebox.showinfo("Success","Member has been deleted")


        



if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
