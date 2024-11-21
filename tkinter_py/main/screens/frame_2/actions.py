import screens.obj as obj
import random

def bt_1_click():
    print("bt_1_click")

def bt_2_click():
    if(obj.label_2):
        obj.label_2.config(fg="#{:06x}".format(random.randint(0, 0xFFFFFF)))