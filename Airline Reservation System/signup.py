import tkinter
from tkinter import messagebox
from tkinter import *
from tkcalendar import Calendar, DateEntry
from abc import ABC, abstractmethod
import random
import os
from PIL import ImageTk, Image

class booking(ABC):
	@abstractmethod
	def get_amount(self):
		pass

	@abstractmethod
	def get_details(self):
		pass

class book_reservation(booking):

	def __init__(self):

		self.root=tkinter.Tk()
		self.root.geometry("1280x720")
		self.root.title("Book your flight")
		self.root.config(background="white")

		self.frame1=Frame(self.root)
		self.frame1.place(relx=0.02, rely=0.03, relheight=0.98, relwidth=0.96)
		self.frame1.config(relief=GROOVE,background="silver",borderwidth="2")

		self.message1=Message(self.frame1)
		self.message1.place(relx=0.01, rely=0.01, relheight=0.07, relwidth=0.30)
		self.message1.config(text='''Book a flight''',width=1068,font="helvetica 18",background="silver")
        
		choose_=''
		def function():
			selection=str(btn1.get())
			if selection=='0':
				choose_='001'
			else:
				choose_='002'

			return choose_
		

		btn1=IntVar()
		self.radio1=Radiobutton(self.frame1)
		self.radio1.place(relx=0.01, rely=0.10)
		self.radio1.config(text="One Way",background="silver",value=0,variable=btn1,command=function)

		self.radio2=Radiobutton(self.frame1)
		self.radio2.place(relx=0.10, rely=0.10)
		self.radio2.config(text="Round Trip",background="silver",value=1,variable=btn1,command=function)



		self.label1=Label(self.frame1)
		self.label1.place(relx=0.01, rely=0.15, height=20, width=100)
		self.label1.configure(background="silver",text="From:")

		self.entry1=Entry(self.frame1)
		self.entry1.place(relx=0.01, rely=0.20, height=20, width=150)
		self.frm=StringVar()
		self.entry1.configure(background="white",textvariable=self.frm)


		self.label2=Label(self.frame1)
		self.label2.place(relx=0.21, rely=0.15, height=20, width=100)
		self.label2.configure(background="silver",text="To:")

		self.entry2=Entry(self.frame1)
		self.entry2.place(relx=0.21, rely=0.20, height=20, width=150)
		self.to=StringVar()
		self.entry2.configure(background="white",textvariable=self.to)

		self.label3=Label(self.frame1)
		self.label3.place(relx=0.16, rely=0.20, height=20, width=20)
		self.label3.configure(background="silver",text="<-->")

	
 
		def get_my_date():
			date= self.entry_date.get()
			return date
		
		self.entry_date_label = Label(self.frame1, text="Departure date:")
		self.entry_date_label.place(relx=0.01, rely=0.28, height=20, width=150)
		self.entry_date_label.config(background="silver")
		self.entry_date = DateEntry(self.frame1)
		self.entry_date.place(relx=0.01, rely=0.32, height=20, width=150)
		
        
		self.d1=get_my_date() 

		if choose_=='002':
			def get_my_date1():
				date1= self.entry_date1.get()
				return date1
		
			self.entry_date_label1 = Label(self.frame1, text="Return Date:")
			self.entry_date_label1.place(relx=0.21, rely=0.28, height=20, width=150)
			self.entry_date_label1.config(background="silver")
			self.entry_date1 = DateEntry(self.frame1)
			self.entry_date1.place(relx=0.21, rely=0.32, height=20, width=150)
			
			self.d2=get_my_date1()


		self.label6=Label(self.frame1)
		self.label6.place(relx=0.01, rely=0.40, height=20, width=100)
		self.label6.configure(background="silver",text="No of passengers:")

		self.entry5=Spinbox(self.frame1)
		self.entry5.place(relx=0.01, rely=0.45, height=20, width=150)
		self.entry5.configure(background="white",from_=1,to=10)
		#self.no_of_pass=self.entry5.get()

		self.label7=Label(self.frame1)
		self.label7.place(relx=0.21, rely=0.40, height=20, width=100)
		self.label7.configure(background="silver",text="Payment Mode:")
        
		self.optionlist=["Debit Card","Credit Card","UPI"]
		self.variable=StringVar()
		self.variable.set(self.optionlist[0])
		
		self.entry6=OptionMenu(self.frame1,self.variable,*self.optionlist)
		self.entry6.place(relx=0.21, rely=0.45, height=20, width=150)
		self.entry6.configure(background="white")

		self.button1=Button(self.frame1)
		self.button1.place(relx=0.13, rely=0.55, height=30, width=80)
		self.button1.configure(background="blue",pady="0",text="Search Flights",foreground="white",command=self.get_amount)

		self.message2=Message(self.frame1)
		self.message2.place(relx=0.01, rely=0.62, relheight=0.10, relwidth=0.30)
		self.message2.config(text='''Get your booking details''',width=1068,font="helvetica 18",background="silver")

		self.label8=Label(self.frame1)
		self.label8.place(relx=0.01, rely=0.75, height=20, width=110)
		self.label8.configure(background="silver",text="Enter PNR Number:")

		self.entry9=Entry(self.frame1)
		self.entry9.place(relx=0.21, rely=0.75, height=20, width=150)
		self.pnr=StringVar()
		self.entry9.configure(background="white",textvariable=self.pnr)

		self.button2=Button(self.frame1)
		self.button2.place(relx=0.01, rely=0.82, height=30, width=80)
		self.button2.configure(background="blue",pady="0",text="Submit",foreground="white",command=self.get_details)
        
		img = ImageTk.PhotoImage(Image.open("D:\\py\\tkinter projects\\Airline Reservation System\\ap.jpg"))
		self.panel = Label(self.frame1, image = img)
		self.panel.place(relx=0.45, rely=0.02, height=660, width=700)

		self.root.mainloop()



	def get_amount(self):
		if self.frm.get()=='Delhi'or'Mumbai' and self.to.get()=='Mumbai'or'Delhi':
			root2=tkinter.Tk()
			root2.geometry("480x480")
			root2.title("Available flights")
			root2.configure(background="white")
			choose_flight=''
			def function():
				selection=str(btn.get())
				if selection=='0':
					choose_flight='001'
				else:
					choose_flight='002'

				return choose_flight
			

			def save_details():
				with open("Reciept of "+self.frm.get()+"-"+self.to.get()+'.txt','w') as f3:
					f3.write("Flight"+str(function())+"\n")
					f3.write("Price:5500\n")
					f3.write("From: "+str(self.frm.get())+" to: "+str(self.to.get())+"\n")
					f3.write("PNR NO: "+str(random.randrange(10000000,100000000))+"\n")
					f3.write("Date of departure: "+str(self.d1)+"\n")
					f3.write("Return date: "+str(self.d2)+"\n")
					f3.write("No of passengers: "+str(self.entry5.get())+"\n")
					for i in range(int(self.entry5.get())):
						f3.write(f"Seat no. of the passenger {i+1} is: " +str(random.randint(1,150))+"\n")
					f3.write("Payment mode: "+str(self.variable.get())+"\n")
					messagebox.showinfo("Successfull","Booked flight"+str(function()))
					root2.destroy()


			label=Label(root2)
			label.place(relx=0.01, rely=0.05, height=20, width=100)
			label.configure(background="silver",text="Choose a flight")

			btn=IntVar()
			radio1=Radiobutton(root2)
			radio1.place(relx=0.01, rely=0.10)
			radio1.config(text="Flight 001- 8AM to 11AM",background="silver",value=0,variable=btn,command=function)
 
			radio2=Radiobutton(root2)
			radio2.place(relx=0.01, rely=0.20)
			radio2.config(text="Flight 002- 6PM to 9PM",background="silver",value=1,variable=btn,command=function)
            
			button=Button(root2)
			button.place(relx=0.01, rely=0.30)
			button.config(text="Select",command=save_details)

			root2.mainloop()
				

	def get_details(self):
		
		with open("Reciept of Delhi-Mumbai.txt",'r') as f:
			x=f.readlines()
			if ("PNR NO: "+str(self.pnr.get())+"\n") in x:
				os.startfile('D:\\py\\tkinter projects\\Airline Reservation System\\Reciept of Delhi-Mumbai.txt')
			else:
				with open("Reciept of Mumbai-Delhi.txt",'r') as f:
					x=f.readlines()
					if ("PNR NO: "+str(self.pnr.get())+"\n") in x:
						os.startfile('D:\\py\\tkinter projects\\Airline Reservation System\\Reciept of Mumbai-Delhi.txt')
					else:
						print(FileNotFoundError)
	
		

			




b=book_reservation()
