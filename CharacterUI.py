from tkinter import *
from tkinter import ttk

"""

SETUP FOR THE WINDOW:
------------------------------------
|         ROGUE TRACKER     |_|#|X||
|----------------------------------|
| |ENTER NAME|    |NAME| <- 2      |
| |*ENTRYBOX*|                     |
| |NAMEBUTTON| <-1                 |
|                                  |
| |SKILLS  | <-3   |STUFFSTUFFSTUFF|
| |STATS   |       |STUFFSTUFFSTUFF|
| |ITEMS   |       |STUFFSTUFFSTUFF|
| |CREDITS |   4-> |STUFFSTUFFSTUFF|
------------------------------------

1: Name_Frame: This frame contains a Label (ENTRY NAME) that prompts the user
to enter a name. Also contains an Entry (ENTRYBOX) to take a new name input, and
finally, a Button (NAMEBUTTON) to solidify the input as a new name.

2: Name_Label: A single Label (NAME) in the Main_Frame that shows the user's 
name. Will change if the user enters a new name in the *ENTRYBOX*.

3: Menu_Frame: A frame containing buttons pertaining to a player's Skills
(SKILLS), current attributes and statistics (STATS), inventory (ITEMS), and 
a simple set of credits listening the creator and the versions update history.

4: Content_Frame: A frame that will contains the contents of the various buttons
outlined in Menu_Frame, along with the option to add, delete, and modify the
information that falls under those options (sans CREDITS).

"""


#functions
def rename(*args):
    try:
        value = str(name_getter.get())
        player_name.set(value)
    except ValueError:
        pass
    
def flatten_buttons():
    for button in buttons:
        button.config(relief = "raised")
    
    
def make_credits(*args):
    pass

def make_stats(*args):
    pass

def make_inventory(*args):
    pass

def make_skills(*args):
    pass

"""Definitions of all widgets starts here:
____________________________________________________________________________"""
#object defintions 
stats = [] 
skills = []
inventory = []

#root frame
root = Tk()
root.title("Rogue Tracker (v0.01)")
root.resizable(0,0)
main_frame = ttk.Frame(root, padding = "3 3 48 12")
main_frame.grid(column = 0, row = 0)

#Name_Frame Definitions
name_frame = ttk.Frame(main_frame, padding = "1 1 4 4")
player_name = StringVar()#string being displayed by Name_Label
player_name.set("John Doe") #placeholder string
name_getter = StringVar() #string fetched from NAMEBUTTON
entry_name_label = ttk.Label(name_frame, text = "Enter your new name here!")
name_button = ttk.Button(name_frame, text = "Edit Name", command = rename)
entry_box = ttk.Entry(name_frame, width = 14, textvariable = name_getter)


#Name Label Definitions
name_label_frame = ttk.Frame(main_frame, padding = "1 1 4 4")
name_label = ttk.Label(name_label_frame, textvariable = player_name)
name_label_title = ttk.Label(name_label_frame, text = "CHARACTER NAME:")

#Menu Definitions
menu_frame = ttk.Frame(main_frame, padding = "2 2 8 8")
credits_button = ttk.Button(menu_frame,text = "Credits", command = make_credits)
stats_button = ttk.Button(menu_frame, text = "Stats", command = make_stats)
skills_button = ttk.Button(menu_frame, text = "Skills", command = make_skills)
inventory_button = ttk.Button(menu_frame, text = "Inventory",
                              command = make_inventory)

#placeholder frame
empty_frame = ttk.Frame(main_frame,padding = "3 3 12 12")
empty_box = ttk.Frame(empty_frame, relief = "sunken")

#"Stuff" frame
stuff_frame = ttk.Frame(main_frame, padding = "3 3 12 12")

#Credits Definition
credits_name = ttk.Label(stuff_frame, text = 
                         "Rogue Tracker (Version 0.01)")
credits_development = ttk.Label(stuff_frame, text = 
                                "Developed by Alexander Vukovic")

#Stats Definiton
list_box = ttk.Frame(stuff_frame, padding = "2 2 8 8")
stat_scroll = Scrollbar(list_box)
current_stat = ttk.Label(list_box, text = "CURRENT STATS:")
stat_list = Listbox(list_box,height = 3,yscrollcommand=stat_scroll.set)
stat_scroll.config(command=stat_list.yview)
stat_list.insert(1, "HP: 20/20")
stat_scroll = Scrollbar(list_box)
edit_box = ttk.Frame(list_box, padding = "1 1 4 4")
stat_title = ttk.Label(edit_box, text = "Stat Name:")
stat_name = StringVar()
stat_name.set("Stat")
show_stat_name =ttk.Label(edit_box, textvariable = stat_name)
current_stat = ttk.Label(edit_box,text = "Current Stat Value:") 
current_stat_value = StringVar()
current_stat_value.set("Current Value")
show_current_stat = ttk.Label(edit_box, textvariable = current_stat_value)
max_stat = ttk.Label(edit_box, text = "Max Stat Value:")
max_stat_value = StringVar()
max_stat_value.set("Max Value")
show_max_stat = ttk.Label(edit_box, textvariable = max_stat_value)




"""Grid-ing Start here
____________________________________________________________________________"""

#Name_Frame grid
name_frame.grid(column = 0, row = 0)
entry_name_label.grid(column = 0, row = 0)
entry_box.grid(column = 0, row = 1)
name_button.grid(column = 0, row = 2)

#Name_Label-_Frame grid
name_label_frame.grid(column = 1, row = 0)
name_label_title.grid(column = 0, row = 0)
name_label.grid(column = 0, row = 1)

#Menu_Frame grid
menu_frame.grid(column = 0, row = 4)
credits_button.grid(column = 0, row = 0)
stats_button.grid(column = 0, row = 1)
skills_button.grid(column = 0, row = 2)
inventory_button.grid(column = 0, row = 3)

#Placeholder grid
empty_frame.grid(column = 1, row = 1)
empty_box.grid(column = 1, row = 2)

#stuff grid
stuff_frame.grid(column = 1, row = 4)

#stats grid
list_box.grid(column = 0, row = 1)
stat_scroll.grid(row=1, column = 1)
stat_list.grid(column = 0, row = 1)
current_stat.grid(column = 0, row = 0)
edit_box.grid(column = 2, row = 1)
stat_title.grid(column = 0, row = 0)
show_stat_name.grid(column = 1, row = 0)
current_stat.grid(column = 0, row = 1)
show_current_stat.grid(column = 1, row = 1)


#credit grid
#credits_name.grid(column = 0, row = 0)
#credits_development.grid(column = 0, row = 1)


"""Reference lists:
____________________________________________________________________________"""

buttons = [credits_button,stats_button,skills_button,inventory_button]

root.mainloop()


