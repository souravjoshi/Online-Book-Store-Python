from tkinter import *
import mysql.connector as my
from tkinter.messagebox import *
from tkinter import ttk


#dodger blue


win=Tk()
win.geometry("1200x1200+20+20")
win.title("Admin Panel")
win.config(bg='#4169e1')


lblnm=Label(text="Admin Panel",font=("arial black",15),fg='#FFC24F',bg="#4169e1")
lblnm.grid(row=0,column=1)
lblbid=Label(text="Enter Book id ",font=("arial black",12),fg="#FFC24F",bg="#4169e1")
lblbid.grid(row=3,column=0)
lblbname=Label(text="Enter Book name ",font=("arial black",12),fg="#FFC24F",bg="#4169e1")
lblbname.grid(row=4,column=0)
lblbprice=Label(text="Enter Book price ",font=("arial black",12),fg="#FFC24F",bg="#4169e1")
lblbprice.grid(row=5,column=0)
lblauthor=Label(text="Enter Author name ",font=("arial black",12),fg="#FFC24F",bg="#4169e1")
lblauthor.grid(row=6,column=0)
lblpublish=Label(text="Enter Publish year ",font=("arial black",12),fg="#FFC24F",bg="#4169e1")
lblpublish.grid(row=7,column=0)
lblbk=Label(text="Book list",font=("arial black",15),fg="#FFC24F",bg="#4169e1")
lblbk.grid(row=22,column=1)
lblsearch=Label(text="Search book id",font=("arial black",12),fg="#FFC24F",bg="#4169e1")
lblsearch.grid(row=15,column=0)
lblsearchbook=Label(text="Search book",font=("arial black",12),fg="#FFC24F",bg="#4169e1")
lblsearchbook.grid(row=16,column=0)
lblsearchauthor=Label(text="Search author",font=("arial black",12),fg="#FFC24F",bg="#4169e1")
lblsearchauthor.grid(row=17,column=0)
space=Label(text="\n",font=("arial black",12),fg="#FFC24F",bg="#4169e1")
space.grid(row=14,column=0)



txtbid=Entry(win,font=("arial black",11),fg='#2C2C2C',width=40)
txtbid.grid(row=3,column=1)
txtbname=Entry(win,font=("arial black",11),fg='#2C2C2C',width=40)
txtbname.grid(row=4,column=1)
txtbprice=Entry(win,font=("arial black",11),fg='#2C2C2C',width=40)
txtbprice.grid(row=5,column=1)
txtauthor=Entry(win,font=("arial black",11),fg='#2C2C2C',width=40)
txtauthor.grid(row=6,column=1)
txtpublish=Entry(win,font=("arial black",11),fg='#2C2C2C',width=40)
txtpublish.grid(row=7,column=1)
txtserach=Entry(win,font=("arial black",11),fg='#2C2C2C')
txtserach.grid(row=15,column=1)
txtserachbook=Entry(win,font=("arial black",11),fg='#2C2C2C')
txtserachbook.grid(row=16,column=1)
txtserachauthor=Entry(win,font=("arial black",11),fg='#2C2C2C')
txtserachauthor.grid(row=17,column=1)



from tkinter.ttk import *

tree = ttk.Treeview(win, selectmode='browse')



frame=Frame(win)
frame.grid(row=25,column=1)



tree=Treeview(frame,columns=(1,2,3,4,5),height=25,show="headings")
tree.grid(row=25,column=1)


tree.heading(1,text="ID")
tree.heading(2,text="Name")
tree.heading(3,text="Price")
tree.heading(4,text="Author")
tree.heading(5,text="Publish Year")

tree.column(1,width=150)
tree.column(2,width=150)
tree.column(3,width=150)
tree.column(4,width=150)
tree.column(5,width=150)



db=my.connect(host='localhost',user='root',passwd='',database='bookmgmt',port='3306')
cur=db.cursor()

def saverec():
	try:
		bid=txtbid.get()
		bookname=txtbname.get()
		bookprice=txtbprice.get()
		bookauthor=txtauthor.get()
		bookpublishyear=txtpublish.get()
		sql="insert into book(bid,bookname,bookprice,bookauthor,bookpublishyear)values({},'{}',{},'{}',{})".format(bid,bookname,bookprice,bookauthor,bookpublishyear)
		cur.execute(sql)
		if cur.rowcount:
			showinfo("Save","Book is added")
			sql="select * from book ORDER BY bid ASC"
			cur.execute(sql)
			data=cur.fetchall()
			tree.delete(i)
			for val in data:
				tree.insert('','end',values=(val[0],val[1],val[2],val[3],val[4]))
				db.commit()
		else:
			showinfo("Try again")
			db.rollback()
	except Exception as e:
		print(e)	



def editrec():
	try:
		bookprice=txtbprice.get()
		bid=txtbid.get()
		sql="update book set bookprice={} where bid={}".format(bookprice,bid)
		cur.execute(sql)
		if cur.rowcount:
			showinfo("Update","Book is updated")
			sql="select * from book ORDER BY bid ASC"
			cur.execute(sql)
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
def delrec():
	try:
		bid=txtbid.get()
		sql="delete from book where bid={}".format(bid)
		cur.execute(sql)
		if cur.rowcount:
			showinfo("Delete","Book is deleted")
			sql="select * from book ORDER BY bid ASC"
			cur.execute(sql)
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

		
def clearrec():
    txtbid.delete(first=0,last=22)
    txtbname.delete(first=0,last=22)
    txtbprice.delete(first=0,last=22)
    txtauthor.delete(first=0,last=22)
    txtpublish.delete(first=0,last=22)
    txtserach.delete(first=0,last=22)
    txtserachbook.delete(first=0,last=22)
    txtserachauthor.delete(first=0,last=22)

save=Button(win,text="Add",width=12,command=saverec)
save.grid(row=11,column=0,)
edit=Button(win,text="Update",width=12,command=editrec)
edit.grid(row=11,column=1)
delete=Button(win,text="Delete",width=12,command=delrec)
delete.grid(row=12,column=0)
clear=Button(win,text="Clear",width=12,command=clearrec)
clear.grid(row=12,column=1)
search=Button(win,text="Search",width=12,command=searchrec)
search.grid(row=15,column=3)
search=Button(win,text="Search",width=12,command=searchbook)
search.grid(row=16,column=3)
search=Button(win,text="Search",width=12,command=searchbookauthor)
search.grid(row=17,column=3)
show=Button(win,text="Show all books",width=15,command=showrec)
show.grid(row=14,column=0)


win.mainloop()    						
db.close()
