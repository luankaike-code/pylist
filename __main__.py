import tkinter as tk
from tkinter import ttk
from components.lateral_bar import LateralBar

class Window(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title('Pylist')
		self.minsize(1000, 600)
		self.def_styles()
		self.constructor()

	def def_styles(self):
		for c in range(2):
			self.columnconfigure(c, weight=1)
		for r in range(9):
			self.rowconfigure(r, weight=1)

		self.style = ttk.Style()
		self.style.configure('LateralBar.TFrame', background='red')
	
	def constructor(self):
		ttk.Button().place()
		LateralBar(self).place(rely=0, relx=0, relheight=1, relwidth=.3)

window = Window()
window.mainloop()