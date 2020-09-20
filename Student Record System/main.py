import os
from subprocess import call
from AddStudentRecord import Add_student
from tkinter import *



def click_add_student():
	call(["python","AddStudentRecord.py"])

def click_search_student():
	call(["python","SearchStudentRecord.py"])

def click_modify_student():
	call(["python","ModifyStudentRecord.py"])

def click_delete_student():
	call(["python","DeleteStudentRec.py"])




class Gui:
	def __init__(self):
		root=Tk()
		root.geometry("1280x720")
		root.title("Student Record System")
		root.configure(background="grey")
		
		self.frame1=Frame(root)
		self.frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
		self.frame1.configure(relief=GROOVE,background="blue",borderwidth="2",width=925)

		self.message=Message(self.frame1)
		self.message.place(relx=0.005, rely=0.01, relheight=0.15, relwidth=0.99)
		self.message.config(background="gray",text='''WELCOME''',width=1068)

		self.button1=Button(self.frame1)
		self.button1.place(relx=0.28, rely=0.17, height=80, width=580)
		self.button1.configure(background="gray",pady="0",text="Add Student Record",command=click_add_student)
		
		self.button2=Button(self.frame1)
		self.button2.place(relx=0.28, rely=0.29, height=80, width=580)
		self.button2.configure(background="gray",pady="0",text="Search Student Record",command=click_search_student)
        
		self.button3=Button(self.frame1)
		self.button3.place(relx=0.28, rely=0.41, height=80, width=580)
		self.button3.configure(background="gray",pady="0",text="Modify Student Record",command=click_modify_student)

		self.button5=Button(self.frame1)
		self.button5.place(relx=0.28, rely=0.53, height=80, width=580)
		self.button5.configure(background="gray",pady="0",text="Delete Student Record",command=click_delete_student)

		self.button6=Button(self.frame1)
		self.button6.place(relx=0.28, rely=0.65, height=80, width=580)
		self.button6.configure(background="gray",pady="0",text="Exit",command=quit)


		root.mainloop()



g=Gui()
