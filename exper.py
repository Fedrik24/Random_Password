from tkinter import *
import random
import string


class Gui_Passwd:
	def __init__(self, master):
		F1 = Frame(master)
		F1.pack(fill=BOTH, expand=1)
		master.geometry("300x280+300+300")
		master.title("Password Generator Random")

		## First Name 

		self.L1 = Label(F1, text="First Name ")
		self.L1.place(x=6,y=5)
		self.E1 = Entry(F1)
		self.E1.place(x=70, y= 8)

		## Last Name 

		self.L1 = Label(F1, text="last Name  ")
		self.L1.place(x=6,y=50)
		self.E2 = Entry(F1)
		self.E2.place(x=70, y=50)

		## Button 
		self.B1 = Button(F1, text="Submit", command=self.random_passwd)
		self.B1.place(x=80, y=70)

	def random_passwd(self,length=8):
		try:
			letters = self.E1.get()
			letter = self.E2.get()
			sym = string.punctuation
			resutl_str1 = ''.join(random.choice(letters)for i in range(2))
			resutl_str2 = ''.join(random.choice(letter)for i in range(2))
			resut = ''.join(random.choice(sym)for x in range(4))
			print(resutl_str1+resutl_str2+resut)
			text = open("Password.txt", "w")
			t = text.write(resutl_str1+resutl_str2+resut)
			text.close()
		except IndexError:
			print("Please fill...")




if __name__ == '__main__':
	root = Tk()
	app = Gui_Passwd(root)
	root.mainloop()