from tkinter import *
from tkinter import messagebox as mb
class Modify_Student:

	def __init__(self):

		def verify_record():
			try:
				with open(self.modify.get()+".txt","r") as f:
					f.read()
				mb.showinfo("Successfull","Correct Detail. Press Enter now!")
			except FileNotFoundError:
				mb.showerror("Unsuccessfull","Incorrect Detail")


		def change_details():
			try:
				with open(self.modify.get()+".txt",'r+') as f1:
						f1.write(str(self.modified.get())+"\n")
						f1.write(str(self.modified_add.get())+"\n")
						f1.write(str(self.modified_fat.get())+"\n")
						f1.write(str(self.modified_mob.get())+"\n")
						f1.write(str(self.modified_mob.get())+"\n")
						mb.showinfo("Successfull!","Record has been modified")
						root.destroy()
			except FileNotFoundError:
				mb.showinfo("Unsuccessfull!","Record not found")
		
		def modify():

			root2=Tk()
			root2.geometry("400x400")
			root2.title("Enter the change:")
			root2.config(background="grey")


			self.label2=Label(root2)
			self.label2.place(relx=0.05, rely=0.25, height=20, width=200)
			self.label2.configure(background="dark gray",text="Enter new name:")

			self.entry2=Entry(root2)
			self.entry2.place(relx=0.05, rely=0.30, height=20, width=200)
			self.modified=StringVar()
			self.entry2.configure(background="white",textvariable=self.modified)

			self.label3=Label(root2)
			self.label3.place(relx=0.05, rely=0.35, height=20, width=200)
			self.label3.configure(background="dark gray",text="Enter new address:")

			self.entry3=Entry(root2)
			self.entry3.place(relx=0.05, rely=0.40, height=20, width=200)
			self.modified_add=StringVar()
			self.entry3.configure(background="white",textvariable=self.modified_add)

			self.label4=Label(root2)
			self.label4.place(relx=0.05, rely=0.45, height=20, width=200)
			self.label4.configure(background="dark gray",text="Enter new Father's name:")

			self.entry4=Entry(root2)
			self.entry4.place(relx=0.05, rely=0.50, height=20, width=200)
			self.modified_fat=StringVar()
			self.entry4.configure(background="white",textvariable=self.modified_fat)

			self.label5=Label(root2)
			self.label5.place(relx=0.05, rely=0.55, height=20, width=200)
			self.label5.configure(background="dark gray",text="Enter new contact number:")

			self.entry5=Entry(root2)
			self.entry5.place(relx=0.05, rely=0.60, height=20, width=200)
			self.modified_mob=StringVar()
			self.entry5.configure(background="white",textvariable=self.modified_mob)

			self.label6=Label(root2)
			self.label6.place(relx=0.05, rely=0.65, height=20, width=200)
			self.label6.configure(background="dark gray",text="Enter new E-mail:")

			self.entry2=Entry(root2)
			self.entry2.place(relx=0.05, rely=0.70, height=20, width=200)
			self.modified_mail=StringVar()
			self.entry2.configure(background="white",textvariable=self.modified_mail)

            
			self.button7=Button(root2)
			self.button7.place(relx=0.05, rely=0.80, height=20, width=50)
			self.button7.configure(background="gray",pady="0",text="Modify",command=change_details)
            
		

			root2.mainloop()
			
			

		root=Tk()
		root.geometry("580x600")
		root.title("Modify Student Records")
		root.config(background="grey")
        
		self.label=Label(root)
		self.label.place(relx=0.05, rely=0.25, height=20, width=200)
		self.label.configure(background="dark gray",text="Enter Student's name to modify:")

		self.entry=Entry(root)
		self.entry.place(relx=0.05, rely=0.30, height=20, width=200)
		self.modify=StringVar()
		self.entry.configure(background="white",textvariable=self.modify)

		self.button7=Button(root)
		self.button7.place(relx=0.05, rely=0.40, height=20, width=50)
		self.button7.configure(background="gray",pady="0",text="Verify",command=verify_record)

		self.button6=Button(root)
		self.button6.place(relx=0.15, rely=0.40, height=20, width=50)
		self.button6.configure(background="gray",pady="0",text="Enter",command=modify)


		root.mainloop()

if __name__=="__main__":
	x=Modify_Student()
