import screens.obj as obj
import random

def obj_att():
      change_label_1()

def change_label_1():
      if(obj.label_1):
            obj.label_1.config(fg="#{:06x}".format(random.randint(0, 0xFFFFFF)))