import tkinter as tk
from screens.styles import *
import screens.obj as obj
from screens.create import *

def setup(frame):
    frame_1 = tk.Frame(frame,bg="#000000", pady=10, padx=10)
    frame_1.pack(side=tk.LEFT) 
    
    obj.label_1 = create_label(frame_1, "HELLO WORLD", title_style) 
    obj.label_2 = create_label(frame_1, "teste", label_style)    



