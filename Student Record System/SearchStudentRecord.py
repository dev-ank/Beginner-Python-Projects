from tkinter import *
from tkinter import messagebox


class Search_student:

	def __init__(self):
       
		def submit_clicked():
			try:
				with open(self.search_name.get()+".txt",'r') as f2:
					root1=Tk()
					root1.geometry("800x480")
					root1.title(self.search_name.get())
					root1.config(background="dark gray")
					self.label=Label(root1)
					self.label.place(relx=0.05, rely=0.20, height=30, width=300)
					self.label.config(background="dark gray",text="Name :  "+f2.readline())
					self.label=Label(root1)
					self.label.place(relx=0.05, rely=0.25, height=30, width=300)
					self.label.config(background="dark gray",text="Address :  "+f2.readline())
					self.label=Label(root1)
					self.label.place(relx=0.05, rely=0.30, height=30, width=300)
					self.label.config(background="dark gray",text="Father's name :  "+f2.readline())
					self.label=Label(root1)
					self.label.place(relx=0.05, rely=0.35, height=30, width=300)
					self.label.config(background="dark gray",text="Contact No. :  "+f2.readline())
					self.label=Label(root1)
					self.label.place(relx=0.05, rely=0.40, height=30, width=300)
					self.label.config(background="dark gray",text="Email ID:  "+f2.readline())
					self.submit=Button(root1)
					self.submit.place(relx=0.14, rely=0.50, height=20, width=100)
					self.submit.config(background="dark gray",pady="0",text="Done",command=root1.destroy)

					root.destroy()

					root1.mainloop()

			except FileNotFoundError:
					messagebox.showerror("Unsucessfull!","This record doesn't exists.")
					
        
		root=Tk()
		root.geometry("480x550")
		root.title("Search Student")
		root.configure(background="gray")

		self.label=Label(root)
		self.label.place(relx=0.05, rely=0.20, height=20, width=300)
		self.label.config(background="dark gray",text="ENTER THE NAME OF STUDENT TO BE SEARCHED:")

		self.entry=Entry(root)
		self.entry.place(relx=0.05, rely=0.25, height=20, width=200)
		self.search_name=StringVar()
		self.entry.config(background="white",textvariable=self.search_name)

		self.submit=Button(root)
		self.submit.place(relx=0.05, rely=0.30, height=20, width=100)
		self.submit.config(background="dark gray",pady="0",text="SUBMIT",command=submit_clicked)
		
		root.mainloop()

if __name__=="__main__":
	ss=Search_student()