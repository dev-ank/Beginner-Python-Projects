import tkinter as tk
from tkinter import *
from tkinter import messagebox
import webbrowser
import re
from subprocess import call

alphanum=re.compile('^[a-zA-Z0-9_.-]+$')

def callback(link):
	webbrowser.open_new(link)


class login_gui:

	def __init__(self):

		def is_exist():
			try:
				with open(self.modified_usrn.get()+'.txt','r') as f2:
					f2.read()
				call(["python", r"D:\py\tkinter projects\Airline Reservation System\signup.py"])
				

			except:
				messagebox.showerror("Invalid Details","Please Signup to continue")	

		def check_usrname():
			user=str(self.modified_usrn.get())

			for u in user:
				z=alphanum.match(u)
                 
			if z is None:
				messagebox.showwarning('Invalid Format!','Please try correct format')
				return
			else:
				try:
					with open(self.modified_usrn.get()+'.txt','r') as f3:
						f3.readline()
						x=f3.readline()
						x=x.rstrip("\n")
						x=x.rstrip("\n")
					if x==self.modified_pwd.get():
						is_exist()
					else:
						messagebox.showerror("Invalid","Incorrect Password")
						print(x)
						print(self.modified_pwd.get())
				except:
					messagebox.showerror("Invalid","Incorrect Username")
					


		def file_save():
			with open(self.usrn.get()+'.txt','w') as f1:
				f1.write(str(self.usrn.get())+"\n")
				f1.write(str(self.pwd.get())+"\n")
				f1.write(str(self.add.get())+"\n")
				f1.write(str(self.cnt.get())+"\n")
				f1.write(str(self.mail.get())+"\n")
			messagebox.showinfo('Successfull','Account created')


		root=tk.Tk()
		root.geometry('1280x720')
		root.title("Online Air-Reservation System")
		root.config(background="white")

		self.frame1=Frame(root)
		self.frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.47)
		self.frame1.config(relief=GROOVE,background="silver",borderwidth="2")

		self.frame2=Frame(root)
		self.frame2.place(relx=0.51, rely=0.03, relheight=0.94, relwidth=0.47)
		self.frame2.config(relief=GROOVE,background="grey",borderwidth="2")

		self.message1=Message(self.frame1)
		self.message1.place(relx=0.005, rely=0.01, relheight=0.18, relwidth=0.99)
		self.message1.config(text='''Welcome to Airline Reservation System''',width=1068,font="helvetica 18")

		self.message2=Message(self.frame1)
		self.message2.place(relx=0.001, rely=0.28, relheight=0.15, relwidth=0.50)
		self.message2.config(background="silver",text='''Login to book your reservation''',width=1068,font="mincho 14")

		self.label1=Label(self.frame1)
		self.label1.place(relx=0.01, rely=0.50, height=20, width=100)
		self.label1.configure(background="silver",text="Username:")
		 

		self.entry1=Entry(self.frame1)
		self.entry1.place(relx=0.20, rely=0.50, height=20, width=200)
		self.modified_usrn=StringVar()
		self.entry1.configure(background="white",textvariable=self.modified_usrn)
		#self.entry1.bind("<Button-1>",lambda e: check_usrname(self.modified_usrn.get()))
		

		self.label2=Label(self.frame1)
		self.label2.place(relx=0.01, rely=0.55, height=20, width=100)
		self.label2.configure(background="silver",text="Password:")

		self.entry2=Entry(self.frame1)
		self.entry2.place(relx=0.20, rely=0.55, height=20, width=200)
		self.modified_pwd=StringVar()
		self.entry2.configure(background="white",textvariable=self.modified_pwd)

		self.button1=Button(self.frame1)
		self.button1.place(relx=0.04, rely=0.64, height=20, width=80)
		self.button1.configure(background="gray",pady="0",text="Login",command=check_usrname)

		self.link1 = Label(self.frame1)
		self.link1.place(relx=0.01, rely=0.90, height=20, width=80)
		self.link1.config(text="Contact us", fg="blue", cursor="hand2",background="silver")
		self.link1.bind("<Button-1>",lambda e: callback("test.txt"))

		self.link2 = Label(self.frame1)
		self.link2.place(relx=0.14, rely=0.90, height=20, width=80)
		self.link2.config(text="About", fg="blue", cursor="hand2",background="silver")
		self.link2.bind("<Button-1>",lambda e: callback("test1.txt"))

		self.message3=Message(self.frame2)
		self.message3.place(relx=0.005, rely=0.01, relheight=0.18, relwidth=0.99)
		self.message3.config(background="silver",text='''Get started with us!''',width=1068,font="helvetica 18")

		self.message4=Message(self.frame2)
		self.message4.place(relx=0.001, rely=0.28, relheight=0.15, relwidth=0.50)
		self.message4.config(background="grey",text='''Sign up to book your flight with us!''',width=1068,font="mincho 14")

		self.label3=Label(self.frame2)
		self.label3.place(relx=0.01, rely=0.50, height=20, width=100)
		self.label3.configure(background="silver",text="Username:")
		
		self.entry3=Entry(self.frame2)
		self.entry3.place(relx=0.20, rely=0.50, height=20, width=200)
		self.usrn=StringVar()
		self.entry3.configure(background="white",textvariable=self.usrn)

		self.label4=Label(self.frame2)
		self.label4.place(relx=0.01, rely=0.55, height=20, width=100)
		self.label4.configure(background="silver",text="Password:")

		self.entry4=Entry(self.frame2)
		self.entry4.place(relx=0.20, rely=0.55, height=20, width=200)
		self.pwd=StringVar()
		self.entry4.configure(background="white",textvariable=self.pwd)

		self.label5=Label(self.frame2)
		self.label5.place(relx=0.01, rely=0.60, height=20, width=100)
		self.label5.configure(background="silver",text="Address:")

		self.entry5=Entry(self.frame2)
		self.entry5.place(relx=0.20, rely=0.60, height=20, width=200)
		self.add=StringVar()
		self.entry5.configure(background="white",textvariable=self.add)

		self.label6=Label(self.frame2)
		self.label6.place(relx=0.01, rely=0.65, height=20, width=100)
		self.label6.configure(background="silver",text="Contact no.:")

		self.entry6=Entry(self.frame2)
		self.entry6.place(relx=0.20, rely=0.65, height=20, width=200)
		self.cnt=StringVar()
		self.entry6.configure(background="white",textvariable=self.cnt)

		self.label7=Label(self.frame2)
		self.label7.place(relx=0.01, rely=0.70, height=20, width=100)
		self.label7.configure(background="silver",text="Email:")

		self.entry7=Entry(self.frame2)
		self.entry7.place(relx=0.20, rely=0.70, height=20, width=200)
		self.mail=StringVar()
		self.entry7.configure(background="white",textvariable=self.mail)

        
		self.button2=Button(self.frame2)
		self.button2.place(relx=0.20, rely=0.80, height=20, width=80)
		self.button2.configure(background="gray",pady="0",text="Submit",command=file_save)
		

		root.mainloop()		

if __name__=='__main__':
	g=login_gui()