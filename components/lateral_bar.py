import tkinter as tk
from tkinter import ttk
from components.component import component_fac

class LateralBar(component_fac(ttk.Frame)):
	def __init__(self, root):
		super().__init__(root, style="LateralBar.TFrame")
		self.constructor()
	
	def constructor(self):
		ttk.Label(self, text="oi").pack()