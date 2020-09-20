from tkinter import *

expression=""


def press_num(num):
	global expression
	expression+=str(num)
	entry_text.set(expression)


def press_eq():
	global expression
	try:
		total=eval(entry_text.get())
		entry_text.set(total)
	except:
		expression="error!"
		entry_text.set(expression)


def press_clear():
	global expression
	expression=""
	entry_text.set(expression)
	
	

if __name__=="__main__":
	root=Tk()
	root.geometry("250x250")
	root.configure(bg="light gray")
	root.title("Calculator")

	entry_text=StringVar()

	entry=Entry(root,textvariable=entry_text)
	entry.place(height=30,width=250)

	one=Button(root,text="1",command=lambda: press_num(1))
	one.place(relx=0.02,rely=0.67,height=40,width=40)

	two=Button(root,text="2",command=lambda: press_num(2))
	two.place(relx=0.25,rely=0.67,height=40,width=40)

	three=Button(root,text="3",command=lambda: press_num(3))
	three.place(relx=0.49,rely=0.67,height=40,width=40)

	four=Button(root,text="4",command=lambda: press_num(4))
	four.place(relx=0.02,rely=0.49,height=40,width=40)

	five=Button(root,text="5",command=lambda: press_num(5))
	five.place(relx=0.25,rely=0.49,height=40,width=40)

	six=Button(root,text="6",command=lambda: press_num(6))
	six.place(relx=0.49,rely=0.49,height=40,width=40)

	seven=Button(root,text="7",command=lambda: press_num(7))
	seven.place(relx=0.02,rely=0.31,height=40,width=40)

	eight=Button(root,text="8",command=lambda: press_num(8))
	eight.place(relx=0.25,rely=0.31,height=40,width=40)

	nine=Button(root,text="9",command=lambda: press_num(9))
	nine.place(relx=0.49,rely=0.31,height=40,width=40)

	zero=Button(root,text="0",command=lambda: press_num(0))
	zero.place(relx=0.02,rely=0.84,height=40,width=40)


	plus=Button(root,text="+",command=lambda: press_num('+'))
	plus.place(relx=0.82,rely=0.13,height=40,width=40)

	minus=Button(root,text="-",command=lambda: press_num('-'))
	minus.place(relx=0.82,rely=0.31,height=40,width=40)

	multiply=Button(root,text="*",command=lambda: press_num('*'))
	multiply.place(relx=0.82,rely=0.49,height=40,width=40)

	divide=Button(root,text="/",command=lambda: press_num('/'))
	divide.place(relx=0.82,rely=0.67,height=40,width=40)

	dot=Button(root,text=".",command=lambda: press_num('.'))
	dot.place(relx=0.49,rely=0.84,height=40,width=40)

	clear=Button(root,text="Clear",command=lambda: press_clear())
	clear.place(relx=0.02,rely=0.12,height=40,width=40)

	submit=Button(root,text="=",command=lambda: press_eq())
	submit.place(relx=0.82,rely=0.84,height=40,width=40)


	root.mainloop()