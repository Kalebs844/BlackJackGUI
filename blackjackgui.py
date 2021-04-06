from tkinter import *
import random

tk = Tk()
uval = IntVar()
deal = random.randint(1,5)
loop = 0
dval = IntVar()

#dealer's hand
while loop < 2:
	deal = deal + deal
	loop = loop + 1
	print('loop:' + str(loop))
	print('deal:' + str(deal))

#exit button
def ex():
	print('User disconnected')
	exit()

#hit
def hit():
	global uval
	x = uval.set( uval.get() + random.randint(1,11) )
	if uval.get() > 21:
		stay()
	print('user:' + str(uval.get()))

def win():
	new=Toplevel()
	Ca = Canvas(new,bg='green',width=1000,height=500)
	Ca.pack()
	use = Label(new,text='YOU WIN!!!',font=("Arial", 150),bg='green')
	use.place(x=0,y=100)
	use = Label(new,text='Dealer Hand Was',font=("Arial", 50),bg='green')
	use.place(x=0,y=300)
	use = Label(new,textvariable=dval,font=("Arial", 50),bg='green')
	use.place(x=0,y=400)

def lose():
	new=Toplevel()
	Ca = Canvas(new,bg='red',width=1000,height=500)
	Ca.pack()
	use = Label(new,text='YOU LOSE!!!',font=("Arial", 145),bg='red')
	use.place(x=0,y=100)
	use = Label(new,text='Dealer Hand Was',font=("Arial", 50),bg='red')
	use.place(x=0,y=300)
	use = Label(new,textvariable=dval,font=("Arial", 50),bg='red')
	use.place(x=0,y=400)

#stay
def stay():
	if uval.get() < 21 and uval.get() > deal: #user is less than 21 and more than dealer win
		win()
	elif uval.get() < 21 and dval.get() > 21: #user is less than 21 but dealer is greater than 21 win
		win()
	elif uval.get() > 21 : #user is greater than 21 lose
		lose()
	elif uval.get() < deal and uval.get() < 21: #user is less than dealer and user is less than 21 lose
		lose()
	elif uval.get == 21: #user is 21 win
		win()
		
#HomeScreen
tk.title('BlackJack')
Can = Canvas(bg='powderblue',width=1000,height=500)
Can.pack()

hit1 = Button(bg='grey', width=15, height=3,text='Hit',command=hit)
hit1.place(x=150,y=250)

stay2 = Button(bg='grey', width=15, height=3,text='Stay',command=stay)
stay2.place(x=750,y=250)

user = Label(text='Your hand is:',font=("Arial", 25),bg='powderblue')
user.place(x=400,y=100)
uval.set(random.randint(1,11))
dval.set(deal)

opt = Label(textvariable=uval,font=("Arial", 25),bg='powderblue')
opt.place(x=400,y=150)

opt = Label(text='Hit or Stay',font=("Arial", 25),bg='powderblue')
opt.place(x=400,y=200)

ex = Button(bg='grey' ,width=10, height=2, text='exit', command=ex)
ex.place(x=475,y=460)

tk.mainloop()
