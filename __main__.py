import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title('Pylist')
		self.minsize(1000, 600)

window = Window()
window.mainloop()