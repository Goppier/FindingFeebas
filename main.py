"""
main.py

This file serves as the starting point for the Finding Feebas application. 
It initialises the interface and has functions for all interactions, like moving the map,
pressing buttons and checking the input on the entry boxes.
"""

from feebasCalcs import FeebasCalculator
from trendyPhrase import group_conditions, group_lifestyles, group_hobbies

from tkinter import ttk
from tkinter import *
from ttkwidgets.autocomplete import AutocompleteCombobox
from PIL import Image, ImageTk

ROUTE119_PATH         = "./Resources/Images/Hoenn_Route_119_E.png"
FINDING_FEEBAS_ART    = "./Resources/Images/Finding_Feebas_BG.jpg"
FEEBAS_SPOT_INDICATOR = "./Resources/Images/Feebas_Spot_Indicator.png"
ROUTE119_INITAL_X_POS = 192
ROUTE119_INITAL_Y_POS = 960
HACKY_FEEBAS_BUTTON_INIT = [0, 1, 2, 3, 4, 5]

class Route119:
    """
    This class handles the entire interface and all possible inputs made by the user.
    """
    def __init__(self, root):
        """
        This function initialises the entire interface of the application.

        Args:
            self: The class itself
            root: The root of the tkinter Finding Feebas Application
        """
        self.root = root

        # Initialise the map on the left
        self.map_canvas = Canvas(self.root, width=320, height=560, bg="white")
        image = Image.open(ROUTE119_PATH)
        self.map_render = ImageTk.PhotoImage(image)
        self.map_canvas.create_image(ROUTE119_INITAL_X_POS, ROUTE119_INITAL_Y_POS, image=self.map_render)
        self.map_canvas.place(relx=0.25,rely=0.5,anchor=CENTER)

        # Initialise the art on the right
        self.art_canvas = Canvas(self.root, width=320, height=560, bg="white")
        image = Image.open(FINDING_FEEBAS_ART)
        resized_image= image.resize((325,565))
        self.art_render = ImageTk.PhotoImage(resized_image)
        self.art_canvas.create_image(160, 280, image=self.art_render)
        self.art_canvas.place(relx=0.75,rely=0.5,anchor=CENTER)

        # Initialise the current position of the map and mouse position
        self.current_image_xpos = ROUTE119_INITAL_X_POS
        self.current_image_ypos = ROUTE119_INITAL_Y_POS
        self.current_mouse_xpos = 0
        self.current_mouse_ypos = 0
        self.map_canvas.bind('<Button-1>', self.mousePressCanvas)
        self.map_canvas.bind("<B1-Motion>", self.mouseMove)

        # Initialise the checkbox for Ruby/Sapphire and Emerald. It is coded so that a variable will be 1 if Emerald is selected.
        self.is_emerald = IntVar()
        self.is_emerald.set(0)
        ruby_sapphire_checkbox = ttk.Checkbutton(self.root, text='Ruby/Sapphire',variable=self.is_emerald, onvalue=0, offvalue=1)
        ruby_sapphire_checkbox.place(x=320*0.55/2+320, y=150, anchor="center")
        emerald_checkbox = ttk.Checkbutton(self.root, text='Emerald',variable=self.is_emerald, onvalue=1, offvalue=0)
        emerald_checkbox.place(x=320*1.45/2+320, y=150, anchor="center")

        # Initialise the label and entry box for the Trainder ID and the Lottery ID
        validate_command_function = (self.root.register(self.validateNumber), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        tid_label = ttk.Label(root, text='Trainer ID')
        tid_label.place(x=320*1.5/7+320, y=200, anchor="w")

        sv = StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.maxNumberCallback(sv, 0xFFFF, 0))
        self.tid_entry = ttk.Entry(root, validate="key", validatecommand=validate_command_function, textvariable=sv, width=10)
        self.tid_entry.place(x=320*3.5/7+320, y=200, anchor="w")

        lot_label = ttk.Label(root, text='Lottery No.')
        lot_label.place(x=320*1.5/7+320, y=225, anchor="w")

        sv = StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.maxNumberCallback(sv, 0xFFFF, 1))
        self.lot_enrty = ttk.Entry(root, validate="key", validatecommand=validate_command_function, textvariable=sv, width=10)
        self.lot_enrty.place(x=320*3.5/7+320, y=225, anchor="w")
        
        # Initialise the lists for the trendhy phrase and place them in a dropdown menu   
        self.trendy_phrase_1 = group_conditions.copy()
        self.trendy_phrase_1.sort()
        
        self.trendy_phrase_2 = group_lifestyles + group_hobbies
        self.trendy_phrase_2.sort()
  
        self.drop1 = AutocompleteCombobox(root, completevalues=self.trendy_phrase_1)
        self.drop1.place(x=320*0.55/2+320, y=360, anchor="center")
        self.drop1.config(width = 17)
        
        self.drop2 = AutocompleteCombobox(root, completevalues=self.trendy_phrase_2)
        self.drop2.place(x=320*1.45/2+320, y=360, anchor="center")
        self.drop2.config(width = 17)
        
        # Initialise the buttons to calculate and clear the feebas spots 
        calculate_button = ttk.Button(root, text='Calculate', command=self.calculateFeebasSpots, state= NORMAL)
        calculate_button.place(x=320*2/7+320, y=410, anchor="center")
        clear_button = ttk.Button(root, text='Clear', command=self.clearFeebasSpots, state= NORMAL)
        clear_button.place(x=320*5/7+320, y=410, anchor="center")
        
        # Initialise label and unusable entry box for Secret ID
        secret_id_label = ttk.Label(root, text='Secret ID:')
        secret_id_label.place(x=320*1.2/7+320, y=455, anchor="center")
        
        self.secret_id_entry = ttk.Label(root, text='')
        self.secret_id_entry.place(x=320*4.15/7+320, y=455, anchor="center")
        self.secret_id_entry.config(background='#c5cedb')
        self.secret_id_entry.config(width = 33)
        
        # Initialise the 6 buttons to find the feebas spots in the map.
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
        
        
        self.is_fixed_game = IntVar()
        self.is_fixed_game.set(0)
        fixed_game_checkbox = ttk.Checkbutton(self.root, text='Fixed Game',variable=self.is_fixed_game, onvalue=1, offvalue=0)
        fixed_game_checkbox.place(x=320/7+320, y=540, anchor="center")

    def goToFeebasSpot(self, spot_id):
        """
        This function changes the position of the movable map to the desired Feebas Spot. The map is 640px wide and 2240px long. 
        The edges of the map on the canvas has the following coordinates:
         - x(0) = 480
         - x(640) = -160
         - y(0) = 1400
         - y(2240) = -840

        Args:
            self: The class itself
            spot_id: The Feebas Spot ID ranging from 0 - 5
        """
        calculated_spots = self.feebas_calcs.getFeebasSpotCoordinates()
        
        # Calculate the new position of the map
        self.current_image_xpos = (640 - calculated_spots[spot_id][0] - 160)
        self.current_image_ypos = (2240 - calculated_spots[spot_id][1] - 840)
        
        # Check if the image doesn't go past any of these set boundaries
        if(self.current_image_xpos > 16*20):
            self.current_image_xpos = 16*20
        elif(self.current_image_xpos < 0):
            self.current_image_xpos = 0
        if(self.current_image_ypos > 16*70):
            self.current_image_ypos = 16*70
        elif(self.current_image_ypos < -16*12):
            self.current_image_ypos = -16*12

        # Draw the map on its new coordinates
        self.map_canvas.create_image(self.current_image_xpos, self.current_image_ypos, image=self.map_render)

    def calculateFeebasSpots(self):
        """
        This function is called when the user clicks on the "Calculate" button. This function will try to 
        calculate the correct Feebas Spots and draw them on the map if possible.

        Args:
            self: The class itself
        """
        # Give the parameters to the FeebasCalculator and check if it could find a feebas. If not, then make a noise to let the user know about this.
        self.feebas_calcs = FeebasCalculator(self.tid_entry.get(), self.lot_enrty.get(), self.drop1.get(), self.drop2.get(), self.is_emerald.get(), self.is_fixed_game.get())
        
        if(self.feebas_calcs.isFeebasFound() == False):
            self.root.bell()
            return
        
        # Make a hacky string for the Secret IDs in case we got multiple results
        secret_id_string = ""
        for secret_id in self.feebas_calcs.getSecretIds():
            if(secret_id_string != ""):
                secret_id_string += ' / '
            secret_id_string += str(secret_id)
            
        self.secret_id_entry.config(text=str(secret_id_string))
        
        # Prepare the map and spot indicator
        map_image = Image.open(ROUTE119_PATH).convert('RGBA')
        indicator_image = Image.open(FEEBAS_SPOT_INDICATOR).convert('RGBA')
        map_layer = Image.new('RGBA', map_image.size, (0, 0, 0, 0))

        # Get the calculated spots and place the indicator in the map
        calculated_spots = self.feebas_calcs.getFeebasSpotCoordinates()
        for xy in calculated_spots:
            map_layer.paste(indicator_image, (xy[0], xy[1]))
            xy = xy[:2]
        indicator_layer = map_layer.copy()
        indicator_layer.putalpha(180)
        map_layer.paste(indicator_layer, map_layer)
        result = Image.alpha_composite(map_image, map_layer)

        # place the image with the indicators back in the tool for the user to see
        self.map_render = ImageTk.PhotoImage(result)
        self.map_canvas.create_image(self.current_image_xpos, self.current_image_ypos, image=self.map_render)
        
        # Activate the Feebas spot buttons to directly see where the spots are
        for spot in self.feebas_spot_buttons:	
            spot['state'] = "normal"

    def clearFeebasSpots(self):
        """
        This function is called when the user clicks on the "Clear" button. This function will reset the map and get rid of any Feebas Indicators placed.
        The buttons for the Feebas spots will also be disabled.

        Args:
            self: The class itself
        """
        self.secret_id_entry.config(text="")
        image = Image.open(ROUTE119_PATH)
        self.map_render = ImageTk.PhotoImage(image)
        self.map_canvas.create_image(self.current_image_xpos, self.current_image_ypos, image=self.map_render)
        
        for spot in self.feebas_spot_buttons:	
            spot['state'] = "disabled"
        
    def mousePressCanvas(self, e):
        """
        This function is called when the user does a leftbutton mouse press on the Route119 map. The current position of the mouse is stored in variables of this class.

        Args:
            self: The class itself
            e: Mouse events
        """
        self.current_mouse_xpos = e.x
        self.current_mouse_ypos = e.y
        
    def mouseMove(self, e):
        """
        This function is called when the user drags the canvas while having the leftbutton of the mouse pressed. The position of the map is updated based on which direction
        the user drags the mouse. Some limits have been set in place to make sure the dragging stops at the edges of the map and stays in the relevant areas.

        Args:
            self: The class itself
            e: Mouse events
        """
        x_diff = self.current_mouse_xpos - e.x
        y_diff = self.current_mouse_ypos - e.y
        self.current_image_xpos -= x_diff
        self.current_image_ypos -= y_diff
        if(self.current_image_xpos > 16*20):
            self.current_image_xpos = 16*20
        elif(self.current_image_xpos < 0):
            self.current_image_xpos = 0
        if(self.current_image_ypos > 16*70):
            self.current_image_ypos = 16*70
        elif(self.current_image_ypos < -16*12):
            self.current_image_ypos = -16*12
        self.current_mouse_xpos = e.x
        self.current_mouse_ypos = e.y
        
        self.map_canvas.create_image(self.current_image_xpos, self.current_image_ypos, image=self.map_render)
        
    def maxNumberCallback(self, sv, max_number, id):
        """
        This function is called whenever the user gives an input for the lottery number or the trainer ID. It will check if the value inserted is within the bounds set for it.

        Args:
            self: The class itself
            sv: Holds the input made by the user
            max_number: Hold the max number set for the input field
            id: Indicates which entry field is used. 0 for Trainer ID and 1 for Lottery Number
        """
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
        
    def validateNumber(self, d, i, P, s, S, v, V, W):
        """
        This function is called whenever the user gives an input for the lottery number or the trainer ID. It will check if the value inserted is a number.
        It will dissalow any other characters.

        Args:
            self: The class itself
            d: Type of action (1=insert, 0=delete, -1 for others)
            i: Index of char string to be inserted/deleted, or -1
            P: Value of the entry if the edit is allowed
            s: Value of entry prior to editing
            S: The text string being inserted or deleted, if any
            v: The type of validation that is currently set
            V: The type of validation that triggered the callback
                (key, focusin, focusout, forced)
            W: The tk name of the widget
        """

        # Disallow anything that isn't a number
        if S.isnumeric():
            return True
        else:
            self.root.bell()
            return False
        
        

if __name__ == "__main__":
    root = Tk()

    root.wm_title("Finding Feebas")
    root.geometry("640x560")
    root.resizable(0,0)
    root.iconbitmap(default='Resources/Icon/LogoGoppier.ico')
    
    app = Route119(root)

    root.mainloop()