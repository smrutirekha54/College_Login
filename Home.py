from tkinter import *
import pymysql
import csv 
win1 = Tk()
conobj=pymysql.connect(host="localhost",user="root",password="",port=3306)
corobj=conobj.cursor()
corobj.execute("use myproject");
#----------------------------------------------------------
def Exit():
	win1.destroy()
#----------------------------------------------------------
def Admin():
	win1.destroy()
	win2=Tk()
	#-------------------------------------------------------
	def AdminLogin():
		aemail=AEmail.get()
		apwd=APwd.get()
		r = "Select* from ADMIN where AEmail = '{a}' and APassword = '{p}'";
		#print(r)
		r1 = r.format (a= aemail, p= apwd)
		#print (r1)
		corobj.execute(r1)
		data=corobj.fetchall()
		#print(data,len(data))
		if data : 
			win2.destroy()
			win4= Tk ()
			#--------------------------------
			def AddStudent ():
				win4.destroy()
				win6 = Tk () 
				#-----------------------------------------------------
				def Add():
					
					b=Sname.get()
					c=SDept.get()
					d=Spwd.get()
					#print(a,b,c,d) 
					r= "insert into user (UEmail, Dept,UPassword) values ('{B}','{C}','{D}');"
					r1 = r.format (B= b, C=c, D= d)
					#print (r1)
					corobj.execute(r1)
					conobj.commit ()
					win6.destroy()

				def Reset():
					
					Sname.delete(0,END)
					SDept.set ('Select Dept Name')
					Spwd.delete(0,END)
				def Exit():
					win6.destroy()
				#-----------------------------------------------------
				win6.title("Admin Page")
				win6.maxsize(600,650)
				win6.minsize(600,650)
				win6.configure(background="#78866b")


				Label(win6,text="Student Email",font=('Arial',14),width=12).place(x= 60, y= 100)
				Sname=Entry(win6,font=('Arial',14))
				Sname.place(x= 300, y=100)

				Label(win6,text="Dept",font=('Arial',14),width=12).place(x= 60, y= 150)
				SDept=StringVar()
				dropdown=OptionMenu(win6,SDept,"B.Tech","M.Tech","MCA","BCA")
				dropdown.place(x= 300, y=150)

				Label(win6,text="Password",font=('Arial',14),width=12).place(x= 60, y= 200)
				Spwd=Entry(win6,font=('Arial',14), show = "*")
				Spwd.place(x= 300, y=200)

				Button(win6,text="Add",font=('Arial',16),activebackground='Red',bg='blue',fg='white',width=8,command=Add).place(x= 70, y= 350)
				Button(win6,text="Reset",font=('Arial',16),activebackground='Red',bg='blue',fg='white',width=8,command=Reset).place(x= 200, y= 350)
				Button(win6,text="Exit",font=('Arial',16),activebackground='Red',bg='#c11b17',fg='white',width=8,command=Exit).place(x= 330, y= 350)


				win6.mainloop()
			def StudentDetails():
				fobj = open ("student.csv", "w", newline="\n")
				cobj = csv.writer (fobj)
				cobj.writerow(['UEmail', 'Dept', 'Password', 'StudentName', 'ParentName', 'ContactNumber', 'Gender'])
				corobj.execute('select * from user;')
				data = corobj.fetchall()
				x = len(data)
				for a,b,c,d,e,f,g in data:
					cobj.writerow([a,b,c,d,e,f,g])
				fobj.close()
				win4.destroy()
			def Exit () : 
				win4.destroy()
			#-------------------------------
			win4.title("Admin Page")
			win4.maxsize(600,600)
			win4.minsize(600,600)
			win4.configure(background="#78866b")



			Button(win4,text="Add New student",font=('Arial',16),activebackground='Red',bg='blue',fg='white',width=15, command =AddStudent).place(x= 210, y= 200)
			Button(win4,text="Download All Student Details",font=('Arial',16),activebackground='Red',bg='blue',fg='white',width=25, command = StudentDetails).place(x= 160, y= 300)
			Button(win4,text="Exit",font=('Arial',16),activebackground='Red',bg='#c11b17',fg='white',width=10, command = Exit).place(x= 400, y= 450)

			
			win4.mainloop()
		else : 
			print ("invalid Login")
			win2.destroy() 
		#print(aemail,apwd)
	#--------------------------------------------------------
	win2.title("Admin Page")
	win2.maxsize(600,600)
	win2.minsize(600,600)
	win2.configure(background="#78866b")
	Label(win2,text="Admin Login",font=('Arial',18),width=12).place(x= 200,y= 200)

	Label(win2,text="Email ID",font=('Arial',14),width=12).place(x= 60, y= 300)
	AEmail=Entry(win2,font=('Arial',14))
	AEmail.place(x= 300, y=300)


	Label(win2,text="Password",font=('Arial',14),width=12).place(x= 60, y= 350)
	APwd=Entry(win2,font=('Arial',14),show="*")
	APwd.place(x= 300, y=350)

	Button(win2,text="Login",font=('Arial',14),width=10,command=AdminLogin).place(x=350, y=450)
	win2.mainloop()
#----------------------------------------------------------
def User():
	win1.destroy() 
	win3=Tk()
#----------------------------------------------------------
	def UserLogin():
		uemail=UEmail.get()
		upwd=UPwd.get()
		dept=Dept.get()
		r = "Select* from USER where UEmail = '{a}' and Dept = '{d}' and UPassword = '{p}'";
		#print(r)
		r1 = r.format (a= uemail,d=dept, p= upwd)
		#print (r1)
		corobj.execute(r1) ,
		data=corobj.fetchall()
		#print(data,len(data))
		if data : 
			win3.destroy()
			win5= Tk ()
			#----------------------------------------------------------------
			def StudentUpdate():
				win5.destroy()
				win7=Tk()
				#-------------------------------------------------------------
				def Update():
					var1=Var1.get()
					val1=Val1.get()
					var2=Var2.get()
					val2=Val2.get()
					var3=Var3.get()
					val3=Val3.get()
					var4=Var4.get()
					val4=Val4.get()
					#print(var1,val1,var2,val2,var3,val3,var4,val4)
					r= " update user set StudentName = '{}', ParentName = '{}', ContactNumber = '{}', Gender = '{}' where UEmail = '{a}' ";
					r1= r.format(val1,val2,val3,val4, a=uemail)
					#print(r1)
					corobj.execute(r1)
					conobj.commit()
					win7.destroy()

				def UReset():
					Var1.set("Select Any Option")
					Val1.delete(0, END)
					Var2.set("Select Any Option")
					Val2.delete(0, END)
					Var3.set("Select Any Option")
					Val3.delete(0, END)
					Var4.set("Select Any Option")
					Val4.delete(0, END)
				def UExit():
					win7.destroy()
				#--------------------------------------------------------------
				win7.title("Update Details")
				win7.maxsize(600,600)
				win7.minsize(600,600)
				win7.configure(background="#78866b")

				Var1=StringVar()
				Var1.set("Select Any Option")
				l1= ["Student Name", "Parent Name", "Contact Number", "Gender"]
				dropdown=OptionMenu(win7,Var1,*l1)
				dropdown.place(x=100, y=100)
				Val1=Entry(win7,font=('Arial',14))
				Val1.place(x=300, y=100)

				Var2=StringVar()
				Var2.set("Select Any Option")
				l1= ["Student Name", "Parent Name", "Contact Number", "Gender"]
				dropdown=OptionMenu(win7,Var2,*l1)
				dropdown.place(x=100, y=150)
				Val2=Entry(win7,font=('Arial',14))
				Val2.place(x=300, y=150)

				Var3=StringVar()
				Var3.set("Select Any Option")
				l1= ["Student Name", "Parent Name", "Contact Number","Gender"]
				dropdown=OptionMenu(win7,Var3,*l1)
				dropdown.place(x=100, y=200)
				Val3=Entry(win7,font=('Arial',14))
				Val3.place(x=300, y=200)

				Var4=StringVar()
				Var4.set("Select Any Option")
				l1= ["Student Name", "Parent Name", "Contact Number", "Gender"]
				dropdown=OptionMenu(win7,Var4,*l1)
				dropdown.place(x=100, y=250)
				Val4=Entry(win7,font=('Arial',14))
				Val4.place(x=300, y=250)

				Button(win7,text="Update",font=('Arial',14),activebackground='Red',bg='blue',fg='white',width=8, command=Update).place(x= 60, y= 400)
				Button(win7,text="Reset",font=('Arial',14),activebackground='Red',bg='blue',fg='white',width=8, command=UReset).place(x= 260, y= 400)
				Button(win7,text="Exit",font=('Arial',14),activebackground='Red',bg='#c11b17',fg='white',width=8, command=UExit).place(x=460, y= 400)



				win7.mainloop()
			def Exit():
				win5.destroy()
			#----------------------------------------------------------------
			win5.title("Student")
			win5.maxsize(400,400)
			win5.minsize(400,400)
			win5.configure(background="#78866b")

			Button(win5,text="Update Student",font=('Arial',16),activebackground='Red',bg='blue',fg='white',width=15, command= StudentUpdate).place(x= 100, y= 100)
			Button(win5,text="Exit",font=('Arial',14),activebackground='Red',bg='#c11b17',fg='white',width=8, command=Exit).place(x= 200, y= 200)

			win5.mainloop()
		else : 
			print ("invalid Login")
			win2.destroy() 
		#print(uemail,upwd,dept)
#-----------------------------------------------------------
	win3.title("User Page")
	win3.maxsize(600,600)
	win3.minsize(600,600)
	win3.configure(background="#78866b")
	Label(win3,text="User Login",font=('Arial',18),width=12).place(x= 200,y= 100)

	Label(win3,text="Email ID",font=('Arial',14),width=12).place(x= 60, y= 200)
	UEmail=Entry(win3,font=('Arial',14))
	UEmail.place(x= 300, y=200)

	Label(win3,text="Acc Year",font=('Arial',14),width=12).place(x= 60, y= 300)
	Dept=StringVar()
	dropdown=OptionMenu(win3,Dept,"B.Tech","M.Tech","MCA","BCA")
	dropdown.place(x= 300, y=300)


	Label(win3,text="Password",font=('Arial',14),width=12).place(x= 60, y= 400)
	UPwd=Entry(win3,font=('Arial',14),show="*")
	UPwd.place(x= 300, y=400)

	Button(win3,text="Login",font=('Arial',14),width=10,command=UserLogin).place(x=350, y=450)
	win3.mainloop()
#----------------------------------------------------------
#win1.geometry('600x600')
win1.maxsize(600,600)
win1.minsize(600,600)
win1.title("Home Page")
win1.configure(background="#78866b")
Button(win1,text="Admin Login",font=('Arial',16),activebackground='Red',bg='blue',fg='white',width=10,command=Admin).place(x= 250, y= 200)
Button(win1,text="User Login",font=('Arial',16),activebackground='Red',bg='blue',fg='white',width=10,command=User).place(x= 250, y= 300)
Button(win1,text="Cancel",font=('Arial',16),activebackground='Red',bg='#c11b17',fg='white',width=10,command=Exit).place(x= 400, y= 450)
win1.mainloop()