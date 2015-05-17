from tkinter import *
from tkinter import ttk
from tkinter import messagebox

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
(SKILLS), current attributes and boxistics (STATS), inventory (ITEMS), and 
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
    
    
def make_credits(*args):
    messagebox.showinfo(message=
    'Rogue Tracker (v 0.01)\nDeveloped by Alexander Vukovic', title = "Credits")
    
def get_name(thing):
    index = thing.index(":")
    return thing[0:index]
    

def make_stats(*args):
    populate(stats)
    global is_stats
    global is_items 
    global is_skills
    is_stats = True
    is_items = False
    is_skills = False

def make_inventory(*args):
    populate(items)
    global is_stats
    global is_items 
    global is_skills    
    is_stats = False
    is_items = True
    is_skills = False
    
def make_skills(*args):
    populate(skills)
    global is_stats
    global is_items 
    global is_skills    
    is_stats = False
    is_items = False
    is_skills = True

def populate(lst):
    box_list.delete(0,END)
    for x in lst:
        box_list.insert(END,x)

def add():
    if is_stats:
        stats.append("Stat: 0/0")
        make_stats()
    elif is_items:
        items.append("Item: x1")
        make_inventory()
    elif is_skills:
        skills.append("Skill: Castable")
        make_skills()
        
def make_new_stat():
    pass

def stat_edit():
    top = Toplevel()
    top.resizable(0,0)
    top.title("Edit Stat")
    global stats
    new_name = StringVar()
    string = str(box_list.get(box_list.curselection()))
    name, rest = string.split(":")
    cur_value, tot_value = rest.split("/")
    
    
    n_prompt = ttk.Label(top, text="Enter your new stat name: ", 
                    padding = "8 8 8 8")
    n_prompt.grid(column = 0, row = 0)
    
    name_entry = ttk.Entry(top, width = 15)
    name_entry.insert(0,name)
    name_entry.grid(column = 0, row = 1)
    
    c_prompt = ttk.Label(top, text="Enter your new current value: ",
                         padding = "8 8 8 8")
    c_prompt.grid(column = 0, row = 2)
    
    current_entry = ttk.Entry(top, width = 10)
    current_entry.insert(0,cur_value)
    current_entry.grid(column = 0, row = 3)
    
    t_prompt = ttk.Label(top, text="Enter your new maximum value here: ",
                         padding = "8 8 8 8")
    t_prompt.grid(column = 0, row = 4)
    
    total_entry = ttk.Entry(top, width = 10)
    total_entry.insert(0, tot_value)
    total_entry.grid(column = 0, row = 5)
    
    button_frame = ttk.Frame(top, padding = "8 8 8 8")
    button_frame.grid(column = 0, row = 7)
    
    okay = Button(button_frame, text = "Save", command = make_new_stat())
    okay.grid(column = 0, row = 0)
    
    placeholder = ttk.Label(button_frame, text = "")
    placeholder.grid(column = 1, row = 0, padx = 3)
    
    cancel = Button(button_frame, text="Cancel", command=top.destroy)
    cancel.grid(column = 2, row = 0)
    

def edit(*args):
    if is_stats:
        stat_edit()

def delete():
    idx = box_list.get(box_list.curselection())
    if is_stats:
        stats.remove(idx)
        make_stats()
    elif is_items:
        items.remove(idx)
        make_inventory()
    elif is_skills:
        skills.remove(idx)
        make_skills()
        
def get_name(info):
    index = info.index(':')
    return info[:(int(index))]
        

"""Definitions of all widgets starts here:
____________________________________________________________________________"""
#object defintions 
stats = ["HP: 20/20"]
skills = ["Haste: Castable"]
items = ["Gold: x100"]
is_stats = True
is_items = False
is_skills = False

#root frame
root = Tk()
root.title("Rogue Tracker (v0.01)")
root.resizable(0,0)
main_frame = ttk.Frame(root, padding = "12 12 12 24")
main_frame.grid(column = 0, row = 0)

#Name_Frame Definitions
name_frame = ttk.Frame(main_frame, padding = "1 1 4 4")
player_name = StringVar()#string being displayed by Name_Label
player_name.set("John Doe") #placeholder string
name_getter = StringVar() #string fetched from NAMEBUTTON
entry_name_label = ttk.Label(name_frame, text = "Enter name here:")
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
list_box = ttk.Frame(stuff_frame, padding = "2 2 8 8")
box_scroll = Scrollbar(list_box)
box_list = Listbox(list_box,height = 3,yscrollcommand= box_scroll.set)
populate(stats)
box_scroll.config(command=box_list.yview)
edit_box = ttk.Frame(list_box, padding = "6 6 4 4")
add_value = ttk.Button(edit_box, text = "Add Value", command = add)
edit_value = ttk.Button(edit_box, text = "Edit Value", command = edit)
delete_value = ttk.Button(edit_box, text = "Delete Value", command = delete)




"""Griding Start here
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

#stuff_frame
stuff_frame.grid(column = 1, row = 4)

#boxs grid
list_box.grid(column = 0, row = 1)
box_scroll.grid(column = 1, row = 1)
box_list.grid(column = 0, row = 1)
edit_box.grid(column = 2, row = 1)
add_value.grid(column = 0, row = 0)
edit_value.grid(column = 0, row = 1)
delete_value.grid(column = 0, row = 2)


"""Reference lists:
____________________________________________________________________________"""

root.mainloop()


