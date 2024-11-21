import tkinter as tk
from screens.styles import *
import screens.obj as obj
from screens.create import *
import screens.frame_2.actions as actions

def setup(frame):
    frame_2 = tk.Frame(frame,bg="#000000", pady=10, padx=10)
    frame_2.pack(side=tk.LEFT) 
    
    obj.bt_1 = create_button(frame_2, "HELLO WORLD", button_style, actions.bt_1_click) 
    obj.bt_2 = create_button(frame_2, "teste", button_style, actions.bt_2_click)    



