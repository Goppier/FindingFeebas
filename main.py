from tkinter import ttk
from tkinter import *
from ttkwidgets.autocomplete import AutocompleteCombobox
from feebasCalcs import FeebasCalculator

from trendyPhrase import group_conditions, group_lifestyles, group_hobbies

# pip install pillow
from PIL import Image, ImageTk


class Route119:
	def __init__(self, root):
		self.root = root
		self.canvas = Canvas(self.root, width=320, height=560, bg="white")
		image = Image.open('./Recources/Hoenn_Route_119_E.png')
		self.render = ImageTk.PhotoImage(image)
		img = self.canvas.create_image(192, 960, image=self.render)
		self.canvas.place(relx=0.25,rely=0.5,anchor=CENTER)
		
		self.current_image_xpos = 192
		self.current_image_ypos = 960

		self.current_mouse_xpos = 0
		self.current_mouse_ypos = 0
		
		self.canvas.bind('<Button-1>', self.mousePressCanvas)
		self.canvas.bind("<B1-Motion>", self.mouseMove)

		self.trendy_1 = group_conditions.copy()
		self.trendy_1.sort()
		
		self.trendy_2 = group_lifestyles + group_hobbies
		self.trendy_2.sort()
		
		self.var = IntVar()
		self.var.set(1)
		self.ruby_sapphire_checkbox = ttk.Checkbutton(self.root, text='Ruby/Sapphire',variable=self.var, onvalue=1, offvalue=0, command=self.rs_selected)
		self.ruby_sapphire_checkbox.place(x=320*0.55/2+320, y=150, anchor="center")
		
		self.ruby_sapphire_checkbox = ttk.Checkbutton(self.root, text='Emerald',variable=self.var, onvalue=0, offvalue=1, command=self.rs_selected)
		self.ruby_sapphire_checkbox.place(x=320*1.45/2+320, y=150, anchor="center")
		# Create Dropdown menu
		self.drop1 = AutocompleteCombobox(root, completevalues=self.trendy_1)
		self.drop1.place(x=320*0.55/2+320, y=360, anchor="center")
		self.drop1.config(width = 17)
		
		self.drop2 = AutocompleteCombobox(root, completevalues=self.trendy_2)
		self.drop2.place(x=320*1.45/2+320, y=360, anchor="center")
		self.drop2.config(width = 17)
		
		vcmd = (self.root.register(self.validateNumber), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
		
		tid_label = ttk.Label(root, text='Trainer ID')
		tid_label.place(x=320*1.5/7+320, y=200, anchor="w")
		
		sv = StringVar()
		sv.trace("w", lambda name, index, mode, sv=sv: self.maxNumberCallback(sv, 0xFFFF, 0))
		self.tid_entry = ttk.Entry(root, validate="key", validatecommand=vcmd, textvariable=sv, width=10)
		self.tid_entry.place(x=320*3.5/7+320, y=200, anchor="w")
		
		lot_label = ttk.Label(root, text='Lottery No.')
		lot_label.place(x=320*1.5/7+320, y=225, anchor="w")
		
		sv = StringVar()
		sv.trace("w", lambda name, index, mode, sv=sv: self.maxNumberCallback(sv, 0xFFFF, 1))
		self.lot_enrty = ttk.Entry(root, validate="key", validatecommand=vcmd, textvariable=sv, width=10)
		self.lot_enrty.place(x=320*3.5/7+320, y=225, anchor="w")

		sid_label = ttk.Label(root, text='Secret ID')
		sid_label.place(x=320*1.5/7+320, y=250, anchor="w")
		
		self.sid_entry = ttk.Label(root, text='')
		self.sid_entry.place(x=320*3.5/7+320, y=250, anchor="w")
		
		calc_button = ttk.Button(root, text='Calculate', command=self.calculateFeebasSpots, state= NORMAL)
		calc_button.place(x=320*2/7+320, y=430, anchor="center")
		clear_button = ttk.Button(root, text='Clear', command=self.clearFeebasSpots, state= NORMAL)
		clear_button.place(x=320*5/7+320, y=430, anchor="center")
		
		self.feebas_spot_buttons = []
		
		spot_button = ttk.Button(root, text='1', command= lambda: self.goToFeebasSpot(0), state= DISABLED, width=4)
		spot_button.place(x=320/7+320, y=500, anchor="center")
		self.feebas_spot_buttons.append(spot_button)
		
		spot_button = ttk.Button(root, text='2', command= lambda: self.goToFeebasSpot(1), state= DISABLED, width=4)
		spot_button.place(x=320*2/7+320, y=500, anchor="center")
		self.feebas_spot_buttons.append(spot_button)
		
		spot_button = ttk.Button(root, text='3', command= lambda: self.goToFeebasSpot(2), state= DISABLED, width=4)
		spot_button.place(x=320*3/7+320, y=500, anchor="center")
		self.feebas_spot_buttons.append(spot_button)
		
		spot_button = ttk.Button(root, text='4', command= lambda: self.goToFeebasSpot(3), state= DISABLED, width=4)
		spot_button.place(x=320*4/7+320, y=500, anchor="center")
		self.feebas_spot_buttons.append(spot_button)
	
		spot_button = ttk.Button(root, text='5', command= lambda: self.goToFeebasSpot(4), state= DISABLED, width=4)
		spot_button.place(x=320*5/7+320, y=500, anchor="center")
		self.feebas_spot_buttons.append(spot_button)
		
		spot_button = ttk.Button(root, text='6', command= lambda: self.goToFeebasSpot(5), state= DISABLED, width=4)
		spot_button.place(x=320*6/7+320, y=500, anchor="center")
		self.feebas_spot_buttons.append(spot_button)

	def goToFeebasSpot(self, spot_id):
		calculated_spots = self.feebas_calcs.getFeebasSpotCoordinates()
		# x(0) = 480
		# x(640) = -160
		# y{0) = 1400
		# y(2240) = -840
		
		self.current_image_xpos = (640 - calculated_spots[spot_id][0] - 160)
		self.current_image_ypos = (2240 - calculated_spots[spot_id][1] - 840)
		if(self.current_image_xpos > 16*20):
			self.current_image_xpos = 16*20
		elif(self.current_image_xpos < 0):
			self.current_image_xpos = 0
		if(self.current_image_ypos > 16*60):
			self.current_image_ypos = 16*60
		elif(self.current_image_ypos < -16*12):
			self.current_image_ypos = -16*12

		img = self.canvas.create_image(self.current_image_xpos, self.current_image_ypos, image=self.render)

	def calculateFeebasSpots(self):
		self.feebas_calcs = FeebasCalculator(self.tid_entry.get(), self.lot_enrty.get(), self.drop1.get(), self.drop2.get(), self.var.get())
		
		if(self.feebas_calcs.isFeebasFound() == False):
			self.root.bell()
			return
		
		image = Image.open("./Recources/Hoenn_Route_119_E.png").convert('RGBA')
		watermark = Image.open("./Recources/Feebas_Spot_Indicator.png").convert('RGBA')
		layer = Image.new('RGBA', image.size, (0, 0, 0, 0))
		print(self.feebas_calcs.getSecretId())
		self.sid_entry.config(text=str(self.feebas_calcs.getSecretId()))
		calculated_spots = self.feebas_calcs.getFeebasSpotCoordinates()
		for xy in calculated_spots:
			layer.paste(watermark, (xy[0], xy[1]))
			xy = xy[:2]
		layer2 = layer.copy()
		layer2.putalpha(180)
		layer.paste(layer2, layer)
		result = Image.alpha_composite(image, layer)
		self.render = ImageTk.PhotoImage(result)
		img = self.canvas.create_image(self.current_image_xpos, self.current_image_ypos, image=self.render)
		
		for spot in self.feebas_spot_buttons:	
			spot['state'] = "normal"

	def clearFeebasSpots(self):
		image = Image.open('./Recources/Hoenn_Route_119_E.png')
		self.render = ImageTk.PhotoImage(image)
		img = self.canvas.create_image(self.current_image_xpos, self.current_image_ypos, image=self.render)
		
		for spot in self.feebas_spot_buttons:	
			spot['state'] = "disabled"
		
	def mousePressCanvas(self, e):
		self.current_mouse_xpos = e.x
		self.current_mouse_ypos = e.y
		
	def mouseMove(self, e):
		x_diff = self.current_mouse_xpos - e.x
		y_diff = self.current_mouse_ypos - e.y
		self.current_image_xpos -= x_diff
		self.current_image_ypos -= y_diff
		if(self.current_image_xpos > 16*20):
			self.current_image_xpos = 16*20
		elif(self.current_image_xpos < 0):
			self.current_image_xpos = 0
		if(self.current_image_ypos > 16*60):
			self.current_image_ypos = 16*60
		elif(self.current_image_ypos < -16*12):
			self.current_image_ypos = -16*12
		self.current_mouse_xpos = e.x
		self.current_mouse_ypos = e.y
		
		img = self.canvas.create_image(self.current_image_xpos, self.current_image_ypos, image=self.render)
		
	def maxNumberCallback(self, sv, max_number, id):
		current_number = 0
		try:
			current_number = int(sv.get())
		except ValueError:
			print("Nothing")

		if current_number > max_number:
			if(id == 0):
				self.tid_entry.delete(0, END)
				self.tid_entry.insert(0, "65535")
			else:
				self.lot_enrty.delete(0, END)
				self.lot_enrty.insert(0, "65535")
			current_number = max_number
			self.root.bell()
		
	def rs_selected(self):
		print("SELECTED")
		
	def validateNumber(self, d, i, P, s, S, v, V, W):
		# %d = Type of action (1=insert, 0=delete, -1 for others)
		# %i = index of char string to be inserted/deleted, or -1
		# %P = value of the entry if the edit is allowed
		# %s = value of entry prior to editing
		# %S = the text string being inserted or deleted, if any
		# %v = the type of validation that is currently set
		# %V = the type of validation that triggered the callback
		#      (key, focusin, focusout, forced)
		# %W = the tk name of the widget

		# Disallow anything that isn't a number
		if S.isnumeric():
			return True
		else:
			self.root.bell()
			return False
		
		
		
root = Tk()

root.wm_title("Finding Feebas")
root.geometry("640x560")
root.resizable(0,0)

app = Route119(root)

root.mainloop()