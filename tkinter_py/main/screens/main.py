import tkinter as tk
import screens.frame_1.main as frame_1
import screens.frame_2.main as frame_2
from screens.styles import *
from screens.att_obj import obj_att

class Tk_window:
    @staticmethod
    def setup():
        janela = tk.Tk()
        janela.title("Exemplo de Label no Tkinter")
        # janela.geometry("300x200")
        # janela.attributes('-fullscreen', True)
        janela.state('zoomed') 
        janela.configure(bg="#000000")

        #mainframe_1
        mainframe_1 = tk.Frame(janela,bg="#000000")
        mainframe_1.pack(side=tk.TOP) 

        frame_1.setup(mainframe_1)
        frame_2.setup(mainframe_1)

        Tk_window.loop(janela)

        janela.mainloop()

    @staticmethod
    def loop(janela):   
        global label_1
        time_att=300

        obj_att()

        janela.after(time_att, lambda: Tk_window.loop(janela))

