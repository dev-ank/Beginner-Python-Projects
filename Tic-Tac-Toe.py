from tkinter import *
from tkinter import messagebox


button_pressed=0
pressed_x=True

def play_again():
	p1.set(" ")
	p2.set(" ")
	b1["text"]=" "
	b2["text"]=" "
	b3["text"]=" "
	b4["text"]=" "
	b5["text"]=" "
	b6["text"]=" "
	b7["text"]=" "
	b8["text"]=" "
	b9["text"]=" "


def press_button(btn):

	global pressed_x,button_pressed
	

	if btn["text"]==" " and pressed_x==True:
		btn["text"]="X"
		pressed_x=False
		button_pressed+=1
		check_winner()

	elif btn["text"]==" " and pressed_x==False:
		btn["text"]="O"
		pressed_x=True
		button_pressed+=1
		check_winner()

	else:
		messagebox.showwarning("Warning","Already Pressed!")


def check_winner():

	global pressed_x,button_pressed

	if (b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X" or
	   b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X" or
	   b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X" or
	   b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X" or
	   b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X" or 
	   b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X" or 
	   b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X" or
	   b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X"):
		
	   
	   messagebox.showinfo("Congrats",p1.get()+" wins!")
	   ques=messagebox.askquestion("Play Again?","Wanna Play again?")
	   
	   if ques=="yes":
		   button_pressed=0
		   play_again()
		   pressed_x=True
	   else:
		   root.destroy()

	elif (b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O" or
	   b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O" or
	   b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O" or
	   b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O" or
	   b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O" or 
	   b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O" or 
	   b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O" or
	   b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O"):

	   
	   messagebox.showinfo("Congrats",p2.get()+" wins!")
	   ques1=messagebox.askquestion("Play Again?","Wanna Play again?")
	   

	   if ques1=="yes":
		   button_pressed=0
		   play_again()
		   pressed_x=True
	   else:
		   root.destroy()

	elif (button_pressed==8):

		messagebox.showinfo("Oops","It's a Tie!")


if __name__=="__main__":

	root=Tk()
	root.geometry("480x800")
	root.configure(bg='#856ff8')
	root.title("TIC-TAC-TOE")

	p1=StringVar()
	p2=StringVar()
	
	l1=Label(root,text="Player 1 : ").place(x=25,y=30)
	e1=Entry(root,textvariable=p1)
	e1.place(x=90,y=30)


	l2=Label(root,text="Player 2 : ").place(x=25,y=80)
	e2=Entry(root,textvariable=p2)
	e2.place(x=90,y=80)
	

	

	def show_game():
		if p1.get() and p2.get():
			messagebox.showinfo("Game says...","All the best!")
			global b1,b2,b3,b4,b5,b6,b7,b8,b9

			b1=Button(root,text=" ",font="Times 20 bold",fg="black",bg="dark gray",height=4,width=6,command=lambda: press_button(b1))
			b1.place(x=70,y=200)

			b2=Button(root,text=" ",font="Times 20 bold",fg="black",bg="dark gray",height=4,width=6,command=lambda: press_button(b2))
			b2.place(x=180,y=200)

			b3=Button(root,text=" ",font="Times 20 bold",fg="black",bg="dark gray",height=4,width=6,command=lambda: press_button(b3))
			b3.place(x=290,y=200)

			b4=Button(root,text=" ",font="Times 20 bold",fg="black",bg="dark gray",height=4,width=6,command=lambda: press_button(b4))
			b4.place(x=70,y=350)

			b5=Button(root,text=" ",font="Times 20 bold",fg="black",bg="dark gray",height=4,width=6,command=lambda: press_button(b5))
			b5.place(x=180,y=350)

			b6=Button(root,text=" ",font="Times 20 bold",fg="black",bg="dark gray",height=4,width=6,command=lambda: press_button(b6))
			b6.place(x=290,y=350)

			b7=Button(root,text=" ",font="Times 20 bold",fg="black",bg="dark gray",height=4,width=6,command=lambda: press_button(b7))
			b7.place(x=70,y=500)

			b8=Button(root,text=" ",font="Times 20 bold",fg="black",bg="dark gray",height=4,width=6,command=lambda: press_button(b8))
			b8.place(x=180,y=500)

			b9=Button(root,text=" ",font="Times 20 bold",fg="black",bg="dark gray",height=4,width=6,command=lambda: press_button(b9))
			b9.place(x=290,y=500)

	
	b=Button(root,text="Start Game",fg='yellow',bg='red',width=8,command=show_game).place(x=40,y=140)
	
	

	mainloop()