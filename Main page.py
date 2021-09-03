from tkinter import *
from tkinter import ttk
import mysql.connector as my
from tkinter.messagebox import *
import math, random


win=Tk()
win.geometry("1200x1200+20+20")
win.title("Online Book Store")
win.config(bg='#4169e1')
i = None
total = None
k = None
l = None
m = None
x = 0
bookList = [];

#win.resizable(False, False)

def openNewWindow():
        newWindow = Toplevel(win)
        newWindow.title("Buy a Book")
        newWindow.geometry("640x480")
        newWindow.config(bg="#4169e1")

        style = ttk.Style()
        style.configure("BW.TLabel", background="#4169e1")
        
        
        title=ttk.Label(newWindow,text ="Cart",style="BW.TLabel",font=("arial black", 15))
        title.grid(row = 0,column=0)
        global i
        global bookList
        print(bookList)
        
        at2=Label(newWindow,text =("\n"),style="BW.TLabel",font=("arial black", 15))
        at2.grid(row=4,column=0)

        frame=Frame(newWindow)
        frame.grid(row=6,column=0)

        tree=Treeview(frame,columns=(1,2,3,4,5),height=25,show="headings")
        tree.grid(row=6,column=1)
        tree.heading(1,text="ID")
        tree.heading(2,text="Name")
        tree.heading(3,text="Price")
        tree.heading(4,text="Author")
        tree.heading(5,text="Publish Year")

        tree.column(1,width=175)
        tree.column(2,width=175)
        tree.column(3,width=175)
        tree.column(4,width=175)
        tree.column(5,width=175)
        total = 0;
        for val in bookList:
                total = total+int(val[2])
                tree.insert('','end',values=(val[0],val[1],val[2],val[3],val[4]))
        print("total is ",total)




        def deletebook():
                selected_item = tree.selection()[0]
                tree.delete(selected_item)


        def generateOTP() :
                digits = "0123456789"
                OTP = ""

                for i in range(4) :
                        OTP += digits[math.floor(random.random() * 10)]
                return OTP

        if __name__ == "__main__" :
                print("OTP of 4 digits:", generateOTP())

        
        def paynow():
                newWindow2 = Toplevel(win)
                newWindow2.title("payment with Card")
                newWindow2.geometry("640x480")
                newWindow2.config(bg="#4169e1")

                style = ttk.Style()
                style.configure("BW.TLabel", background="#4169e1")

                Title=Label(newWindow2,text="Payment",style="BW.TLabel",font=("arial black",15))
                Title.grid(row=0,column=1)

                amt=Label(newWindow2,text=("Total Amount:",total),style="BW.TLabel",font=("arial black",15))
                amt.grid(row=1,column=1)

                a1=Label(newWindow2,text="Enter Card Number",style="BW.TLabel",font=("arial black",12))
                a1.grid(row=5,column=0)

                a2=Label(newWindow2,text="Enter CVV",style="BW.TLabel",font=("arial black",12))
                a2.grid(row=6,column=0)

                a3=Label(newWindow2,text="Enter Name",style="BW.TLabel",font=("arial black",12))
                a3.grid(row=7,column=0)

                a4=Label(newWindow2,text="Expiry Date",style="BW.TLabel",font=("arial black",12))
                a4.grid(row=8,column=0)

                a5=Label(newWindow2,text="Address",style="BW.TLabel",font=("arial black",12))
                a5.grid(row=9,column=0)

                a6=Label(newWindow2,text="Phone No.",style="BW.TLabel",font=("arial black",12))
                a6.grid(row=10,column=0)

                a2e=Entry(newWindow2,font=("arial black",11),width=70)
                a2e.grid(row=5,column=1)

                a1e=Entry(newWindow2,font=("arial black",11),show='*',width=70)
                a1e.grid(row=6,column=1)

                a3e=Entry(newWindow2,font=("arial black",11),width=70)
                a3e.grid(row=7,column=1)

                a4e=Entry(newWindow2,font=("arial black",11),width=70)
                a4e.grid(row=8,column=1)

                a5e=Entry(newWindow2,font=("arial black",11),width=70)
                a5e.grid(row=9,column=1)

                a6e=Entry(newWindow2,font=("arial black",11),width=70)
                a6e.grid(row=10,column=1)

                a7=Label(newWindow2,text="\n",style="BW.TLabel",font=("arial black",12))
                a7.grid(row=15,column=0)

                def paydonecard():
                        showinfo("Payment","payment is done")
                        newWindow3 = Toplevel(win)
                        newWindow3.title("payment")
                        newWindow3.geometry("1080x1920")
                        newWindow3.config(bg="#4169e1")

                        style = ttk.Style()
                        style.configure("BW.TLabel", background="#4169e1")
                        
                        Title=Label(newWindow3,text="Payment Receipt",style="BW.TLabel",font=("arial black",20))
                        Title.grid(row=1,column=1)
                        
                        name=a3e.get()
                        add=a5e.get()
                        phone=a6e.get()
                        
                        Name=Label(newWindow3,text="Name:",style="BW.TLabel",font=("arial black",15))
                        Name.grid(row=3,column=0)
                        
                        namegt=Label(newWindow3,text=("",name),style="BW.TLabel",font=("arial black",15))
                        namegt.grid(row=3,column=1)

                        address=Label(newWindow3,text="Address:",style="BW.TLabel",font=("arial black",15))
                        address.grid(row=5,column=0)
                        
                        addressgt=Label(newWindow3,text=("",add),style="BW.TLabel",font=("arial black",15))
                        addressgt.grid(row=5,column=1)

                        phoneno=Label(newWindow3,text="Phone No:",style="BW.TLabel",font=("arial black",15))
                        phoneno.grid(row=7,column=0)
                        
                        phonenogt=Label(newWindow3,text=("",phone),style="BW.TLabel",font=("arial black",15))
                        phonenogt.grid(row=7,column=1)

                        delvtime=Label(newWindow3,text="Delivery Time:",style="BW.TLabel",font=("arial black",15))
                        delvtime.grid(row=9,column=0)
                        
                        delvtime=Label(newWindow3,text=("The package says it's out for delivery and it's 10 PM"),style="BW.TLabel",font=("arial black",15))
                        delvtime.grid(row=9,column=1)

                        delvtime=Label(newWindow3,text="Delivery Code:",style="BW.TLabel",font=("arial black",15))
                        delvtime.grid(row=10,column=0)
                        
                        delvtime=Label(newWindow3,text=("Your Delivery Code is:",generateOTP()),style="BW.TLabel",font=("arial black",15))
                        delvtime.grid(row=10,column=1)

                bookselect2=Button(newWindow2,text="Order Now",width=20,command=paydonecard)
                bookselect2.grid(row=25,column=1)


        def cod():
                newWindow5 = Toplevel(win)
                newWindow5.title("Cash On Delivery")
                newWindow5.geometry("640x480")
                newWindow5.config(bg="#4169e1")

                style = ttk.Style()
                style.configure("BW.TLabel", background="#4169e1")

                Title=Label(newWindow5,text="Cash On Delivery",style="BW.TLabel",font=("arial black",15))
                Title.grid(row=0,column=1)

                amt=Label(newWindow5,text=("Total Amount:",total),style="BW.TLabel",font=("arial black",15))
                amt.grid(row=1,column=1)

                a3=Label(newWindow5,text="Enter Name",style="BW.TLabel",font=("arial black",12))
                a3.grid(row=7,column=0)

                a4=Label(newWindow5,text="Expiry Date",style="BW.TLabel",font=("arial black",12))
                a4.grid(row=8,column=0)

                a5=Label(newWindow5,text="Address",style="BW.TLabel",font=("arial black",12))
                a5.grid(row=9,column=0)

                a6=Label(newWindow5,text="Phone No.",style="BW.TLabel",font=("arial black",12))
                a6.grid(row=10,column=0)

                a7=Label(newWindow5,text="\n",style="BW.TLabel",font=("arial black",12))
                a7.grid(row=15,column=0)

                a3e=Entry(newWindow5,font=("arial black",11),width=70)
                a3e.grid(row=7,column=1)

                a4e=Entry(newWindow5,font=("arial black",11),width=70)
                a4e.grid(row=8,column=1)

                a5e=Entry(newWindow5,font=("arial black",11),width=70)
                a5e.grid(row=9,column=1)

                a6e=Entry(newWindow5,font=("arial black",11),width=70)
                a6e.grid(row=10,column=1)               
                        
                
                def paymentdone():
                        showinfo("Payment","payment is done")
                        newWindow3 = Toplevel(win)
                        newWindow3.title("payment")
                        newWindow3.geometry("1080x1920")
                        newWindow3.config(bg="#4169e1")

                        style = ttk.Style()
                        style.configure("BW.TLabel", background="#4169e1")
                        
                        Title=Label(newWindow3,text="Payment Receipt",style="BW.TLabel",font=("arial black",20))
                        Title.grid(row=1,column=1)
                        
                        name=a3e.get()
                        add=a5e.get()
                        phone=a6e.get()
                        
                        Name=Label(newWindow3,text="Name:",style="BW.TLabel",font=("arial black",15))
                        Name.grid(row=3,column=0)
                        
                        namegt=Label(newWindow3,text=("",name),style="BW.TLabel",font=("arial black",15))
                        namegt.grid(row=3,column=1)

                        address=Label(newWindow3,text="Address:",style="BW.TLabel",font=("arial black",15))
                        address.grid(row=5,column=0)
                        
                        addressgt=Label(newWindow3,text=("",add),style="BW.TLabel",font=("arial black",15))
                        addressgt.grid(row=5,column=1)

                        phoneno=Label(newWindow3,text="Phone No:",style="BW.TLabel",font=("arial black",15))
                        phoneno.grid(row=7,column=0)
                        
                        phonenogt=Label(newWindow3,text=("",phone),style="BW.TLabel",font=("arial black",15))
                        phonenogt.grid(row=7,column=1)

                        delvtime=Label(newWindow3,text="Delivery Time:",style="BW.TLabel",font=("arial black",15))
                        delvtime.grid(row=9,column=0)
                        
                        delvtime=Label(newWindow3,text=("The package says it's out for delivery and it's 10 PM"),style="BW.TLabel",font=("arial black",15))
                        delvtime.grid(row=9,column=1)

                        delvtime=Label(newWindow3,text="Delivery Code:",style="BW.TLabel",font=("arial black",15))
                        delvtime.grid(row=10,column=0)
                        
                        delvtime=Label(newWindow3,text=("Your Delivery Code is:",generateOTP()),style="BW.TLabel",font=("arial black",15))
                        delvtime.grid(row=10,column=1)

                bookselect=Button(newWindow5,text="Order Now",width=20,command=paymentdone)
                bookselect.grid(row=50,column=1)

                


        bookselect=Button(newWindow,text="Credit Card",width=20,command=paynow)
        bookselect.grid(row=51,column=1)

        bookselect=Button(newWindow,text="Debit Card",width=20,command=paynow)
        bookselect.grid(row=52,column=1)

        bookselect=Button(newWindow,text="Cash on delivery",width=20,command=cod)
        bookselect.grid(row=53,column=1)              
               
        bookselect=Button(newWindow,text="Delete",width=20,command=deletebook)
        bookselect.grid(row=54,column=1)


        
        #print("values addToCartObj",addToCartObj['values'])
        #print("addToCartObj inside openNewWindow()",addToCartObj)
        

lblnm=Label(text="Welcome to Online Book Store",font=("arial black",15),bg="#4169e1")
lblnm.grid(row=0,column=1)

lblsearchbook=Label(text="Search book",font=("arial black",15),fg="#FFC24F",bg="#4169e1")
lblsearchbook.grid(row=3,column=0)

lblsearchbook=Label(text="Search author",font=("arial black",15),fg="#FFC24F",bg="#4169e1")
lblsearchbook.grid(row=4,column=0)

space=Label(text="\n",font=("arial black",15),fg="#FFC24F",bg="#4169e1")
space.grid(row=3,column=1)

space=Label(text="\n",font=("arial black",15),fg="#FFC24F",bg="#4169e1")
space.grid(row=5,column=1)

txtserachbook=Entry(win,font=("arial black",12),fg="black",width=70)
txtserachbook.grid(row=3,column=1)

space=Label(text="\n",font=("arial black",15),fg="#FFC24F",bg="#4169e1")
space.grid(row=5,column=1)

txtserachauthor=Entry(win,font=("arial black",12),fg="black",width=70)
txtserachauthor.grid(row=4,column=1)

from tkinter.ttk import *


frame=Frame(win)
frame.grid(row=6,column=1)

tree=Treeview(frame,columns=(1,2,3,4,5),height=25,show="headings")
tree.grid(row=6,column=1)


tree.heading(1,text="ID")
tree.heading(2,text="Name")
tree.heading(3,text="Price")
tree.heading(4,text="Author")
tree.heading(5,text="Publish Year")

tree.column(1,width=175)
tree.column(2,width=175)
tree.column(3,width=175)
tree.column(4,width=175)
tree.column(5,width=175)




db=my.connect(host='localhost',user='root',passwd='',database='bookmgmt',port='3306')
cur=db.cursor()

def showrec():
	try:
		sql="select * from book ORDER BY bid ASC"
		cur.execute(sql)
		data=cur.fetchall()
		for i in tree.get_children():
			tree.delete(i)
		for val in data:
			tree.insert('','end',values=(val[0],val[1],val[2],val[3],val[4]))	
			db.commit() 
	except Exception as e:
		print(e)

def searchrec():
	try:
		bid=txtserach.get()
		sql="select * from book where bid={}".format(bid)
		cur.execute(sql)
		if cur.rowcount:
			showinfo("search","Id is search")
			data=cur.fetchall()
			for i in tree.get_children():
				tree.delete(i)
			for val in data:
				tree.insert('','end',values=(val[0],val[1],val[2],val[3],val[4]))	
				db.commit()
		else:
			showinfo("Try again")
			db.rollback()     
	except Exception as e:
		print(e)

def searchbook():
	try:
		book=txtserachbook.get()
		sql="SELECT * FROM book where bookname=?",(book)
		print(book)
		print("Serach",sql)
		cur.execute("SELECT * FROM book where bookname like '%%%s%%'"%(book))
		if cur.rowcount:
			showinfo("search","book is search")
			data=cur.fetchall()
			for i in tree.get_children():
				tree.delete(i)
			for val in data:
				tree.insert('','end',values=(val[0],val[1],val[2],val[3],val[4]))	
				db.commit()
		else:
			showinfo("Try again")
			db.rollback()     
	except Exception as e:
		print(e)

def searchbookauthor():
	try:
		serachauthor=txtserachauthor.get()
		sql="SELECT * FROM book where bookauthor={}".format(serachauthor)
		cur.execute("SELECT * FROM book where bookauthor like '%%%s%%'"%(serachauthor))
		if cur.rowcount:
			showinfo("search","book author is search")
			data=cur.fetchall()
			for i in tree.get_children():
				tree.delete(i)
			for val in data:
				tree.insert('','end',values=(val[0],val[1],val[2],val[3],val[4]))	
				db.commit()
		else:
			showinfo("Try again")
			db.rollback()     
	except Exception as e:
		print(e)



        
def addtocart():
        row_id= tree.focus()
        tree.selection_set(row_id)
        global i
        i = tree.item(row_id)
        global bookList
        bookList.append(i['values'])

        
        

		
showrec()

search1=Button(win,text="Search",width=12,command=searchbook)
search1.grid(row=3,column=3)

search2=Button(win,text="Search",width=12,command=searchbookauthor)
search2.grid(row=4,column=3)

search=Button(win,text="Refresh Book List",width=12,command=showrec)
search.grid(row=55,column=0)

buyabook=Button(win,text="Goto Cart",width=12,command=openNewWindow)
buyabook.grid(row=0,column=3)

bookselect=Button(win,text="Add to Cart",width=12,command=addtocart)
bookselect.grid(row=55,column=3)


win.mainloop()    						
db.close()
