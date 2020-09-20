import os
import sys
from tkinter import *
from tkinter import messagebox


class Add_student:
	def __init__(self):

		lower_c=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		upper_c=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


		def valid_number(no):
			if len(self.no.get())==10 and self.no.get() not in lower_c and self.no.get() not in upper_c and self.no.get()!='*' and self.no.get()!='#':
				return True
			else:
				messagebox.showinfo("Invalid","Please enter a valid Number")
				self.entry4=Entry(self.frame1)
				self.entry4.place(relx=0.25, rely=0.35, height=20, width=200)
				self.no=StringVar()
				self.entry4.configure(background="white",textvariable=self.no)
				
				

		def submit_clicked():
			if(valid_number(self.no.get())):
				with open(self.name.get()+".txt",'a') as f1:
					f1.write(str(self.name.get())+"\n")
					f1.write(str(self.add.get())+"\n")
					f1.write(str(self.fat.get())+"\n")
					f1.write(str(self.no.get())+"\n")
					f1.write(str(self.mail.get())+"\n")
					messagebox.showinfo("Successfull","Student record added successfully!")
					root.destroy()
			

				

		root=Tk()
		root.geometry("1280x720")
		root.title('Add Student Record:')
		root.configure(background="gray")

		self.frame1=Frame(root)
		self.frame1.place(relx=0.03, rely=0.18, relheight=0.70, relwidth=0.93)
		self.frame1.configure(relief=GROOVE,background="blue",borderwidth="2",width=925)
		
		self.message=Message(self.frame1)
		self.message.place(relx=0.005, rely=0.01, relheight=0.15, relwidth=0.99)
		self.message.config(background="gray",text="Adding Student Record",width=1068)

		self.label1=Label(self.frame1)
		self.label1.place(relx=0.05, rely=0.20, height=20, width=200)
		self.label1.configure(background="dark gray",text="ENTER THE NAME:")
		
		self.entry1=Entry(self.frame1)
		self.entry1.place(relx=0.25, rely=0.20, height=20, width=200)
		self.name=StringVar()
		self.entry1.configure(background="white",textvariable=self.name)

		self.label2=Label(self.frame1)
		self.label2.place(relx=0.05, rely=0.25, height=20, width=200)
		self.label2.configure(background="dark gray",text="ENTER THE ADDRESS:")

		self.entry2=Entry(self.frame1)
		self.entry2.place(relx=0.25, rely=0.25, height=20, width=400)
		self.add=StringVar()
		self.entry2.configure(background="white",textvariable=self.add)
		
		self.label3=Label(self.frame1)
		self.label3.place(relx=0.05, rely=0.30, height=20, width=200)
		self.label3.configure(background="dark gray",text="ENTER THE FATHER'S NAME:")

		self.entry3=Entry(self.frame1)
		self.entry3.place(relx=0.25, rely=0.30, height=20, width=200)
		self.fat=StringVar()
		self.entry3.configure(background="white",textvariable=self.fat)
		
		self.label4=Label(self.frame1)
		self.label4.place(relx=0.05, rely=0.35, height=20, width=200)
		self.label4.configure(background="dark gray",text="ENTER MOBILE NUMBER:")

		self.entry4=Entry(self.frame1)
		self.entry4.place(relx=0.25, rely=0.35, height=20, width=200)
		self.no=StringVar()
		self.entry4.configure(background="white",textvariable=self.no)
		

		self.label5=Label(self.frame1)
		self.label5.place(relx=0.05, rely=0.40, height=20, width=200)
		self.label5.configure(background="dark gray",text="ENTER EMAIL ID:")

		self.entry5=Entry(self.frame1)
		self.entry5.place(relx=0.25, rely=0.40, height=20, width=200)
		self.mail=StringVar()
		self.entry5.configure(background="white",textvariable=self.mail)

		self.button=Button(self.frame1)
		self.button.place(relx=0.22, rely=0.55, height=20, width=60)
		self.button.configure(background="dark gray",pady="0",text="SUBMIT",command=submit_clicked)
		
		root.mainloop()
		

		
if __name__=='__main__':
	stu=Add_student()
	

        


