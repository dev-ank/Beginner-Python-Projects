from tkinter import *
from tkinter import messagebox as mb
import os
class Delete_Student:
	def __init__(self):

		def callback():
			if mb.askyesno("Caution","Do you want to delete the record?"):
				try:
					os.remove(self.delete_rec.get()+".txt")
					mb.showinfo("Successfull!","The record has been deleted.")
					root.destroy()
				except:
					mb.showwarning("Caution","No such record exists")
			else:
				mb.showinfo("Unsuccessfull!","Deletion Cancelled.")

		root=Tk()
		root.geometry("480x600")
		root.title("Delete Records")
		root.configure(background="grey")
		
		self.label=Label(root)
		self.label.place(relx=0.05, rely=0.25, height=20, width=200)
		self.label.configure(background="dark gray",text="Enter Student's name to delete:")

		self.entry=Entry(root)
		self.entry.place(relx=0.05, rely=0.35, height=20, width=400)
		self.delete_rec=StringVar()
		self.entry.configure(background="white",textvariable=self.delete_rec)

		self.button6=Button(root)
		self.button6.place(relx=0.05, rely=0.45, height=20, width=50)
		self.button6.configure(background="gray",pady="0",text="Delete",command=callback)

		root.mainloop()

if __name__=="__main__":
	z=Delete_Student()