import tkinter as tk
import threading
import os
import sys
import recorder
import player
import webbrowser


_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

_location = os.path.dirname(os.path.abspath(__file__))
base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("400x380+958+289")
        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(0,  0)
        top.title("Macros Recorder")
        top.configure(background="#000b11")
        top.configure(highlightbackground="#000000")
        top.configure(highlightcolor="#80ff00")

        self.top = top
#Primer Recording =============================================================
        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(x=20, y=20, height=68, width=356)
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#000b11")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

#Boton Record 1 =============================================================
        self.BTN_Record_1 = tk.Button(self.Frame1, command=lambda: start_recording(1))
        self.BTN_Record_1.place(x=10, y=10, height=50, width=50)
        self.BTN_Record_1.configure(activebackground="#002d44")
        self.BTN_Record_1.configure(activeforeground="#00ff00")
        self.BTN_Record_1.configure(background="#00f88c")
        self.BTN_Record_1.configure(compound='center')
        self.BTN_Record_1.configure(disabledforeground="#a3a3a3")
        self.BTN_Record_1.configure(foreground="#000000")
        self.BTN_Record_1.configure(highlightbackground="#002d44")
        self.BTN_Record_1.configure(highlightcolor="black")
        photo_location = os.path.join(base_path, "images", "gui", "save50.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.BTN_Record_1.configure(image=_img0)
        self.BTN_Record_1.configure(pady="0")

#Boton Play 1 =============================================================
        self.BTN_Play_1 = tk.Button(self.Frame1, command=lambda: start_playing(1))
        self.BTN_Play_1.place(x=120, y=10, height=50, width=220)
        self.BTN_Play_1.configure(activebackground="beige")
        self.BTN_Play_1.configure(activeforeground="black")
        self.BTN_Play_1.configure(background="#00f88c")
        self.BTN_Play_1.configure(compound='left')
        self.BTN_Play_1.configure(disabledforeground="#a3a3a3")
        self.BTN_Play_1.configure(font="-family {Montserrat} -size 9")
        self.BTN_Play_1.configure(foreground="#002d44")
        self.BTN_Play_1.configure(highlightbackground="#d9d9d9")
        self.BTN_Play_1.configure(highlightcolor="#002d44")
        photo_location = os.path.join(base_path, "images", "gui", "play50.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.BTN_Play_1.configure(image=_img1)
        self.BTN_Play_1.configure(pady="0")
        self.BTN_Play_1.configure(text='''Reproducir Grabación''')

#Boton Stop 1 =============================================================
        self.BTN_Stop_1 = tk.Button(self.Frame1, command=stop_recording)
        self.BTN_Stop_1.place(x=60, y=10, height=50, width=60)
        self.BTN_Stop_1.configure(activebackground="beige")
        self.BTN_Stop_1.configure(activeforeground="black")
        self.BTN_Stop_1.configure(background="#00f88c")
        self.BTN_Stop_1.configure(compound='left')
        self.BTN_Stop_1.configure(disabledforeground="#a3a3a3")
        self.BTN_Stop_1.configure(foreground="#000000")
        self.BTN_Stop_1.configure(highlightbackground="#d9d9d9")
        self.BTN_Stop_1.configure(highlightcolor="black")
        photo_location = os.path.join(base_path, "images", "gui", "stop50.png")
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.BTN_Stop_1.configure(image=_img2)
        self.BTN_Stop_1.configure(pady="0")

#Menu Bar =============================================================
        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu=self.menubar)

#Record 2 =============================================================
        self.Frame2 = tk.Frame(self.top)
        self.Frame2.place(x=20, y=81, height=67, width=356)
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#000b11")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

#Boton Record 2 =============================================================
        self.BTN_Record_2 = tk.Button(self.Frame2, command=lambda: start_recording(2))
        self.BTN_Record_2.place(x=10, y=10, height=50, width=50)
        self.BTN_Record_2.configure(activebackground="#002d44")
        self.BTN_Record_2.configure(activeforeground="#00ff00")
        self.BTN_Record_2.configure(background="#00f88c")
        self.BTN_Record_2.configure(compound='center')
        self.BTN_Record_2.configure(disabledforeground="#a3a3a3")
        self.BTN_Record_2.configure(foreground="#000000")
        self.BTN_Record_2.configure(highlightbackground="#002d44")
        self.BTN_Record_2.configure(highlightcolor="black")
        photo_location = os.path.join(base_path, "images", "gui", "save50.png")
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.BTN_Record_2.configure(image=_img3)
        self.BTN_Record_2.configure(pady="0")

#Boton Play 2 =============================================================
        self.BTN_Play_2 = tk.Button(self.Frame2, command=lambda: start_playing(2))
        self.BTN_Play_2.place(x=120, y=10, height=50, width=220)
        self.BTN_Play_2.configure(activebackground="beige")
        self.BTN_Play_2.configure(activeforeground="black")
        self.BTN_Play_2.configure(background="#00f88c")
        self.BTN_Play_2.configure(compound='left')
        self.BTN_Play_2.configure(disabledforeground="#a3a3a3")
        self.BTN_Play_2.configure(font="-family {Montserrat} -size 9")
        self.BTN_Play_2.configure(foreground="#002d44")
        self.BTN_Play_2.configure(highlightbackground="#d9d9d9")
        self.BTN_Play_2.configure(highlightcolor="#002d44")
        photo_location = os.path.join(base_path, "images", "gui", "play50.png")
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.BTN_Play_2.configure(image=_img4)
        self.BTN_Play_2.configure(pady="0")
        self.BTN_Play_2.configure(text='''Reproducir Grabación''')

#Boton Stop 2 =============================================================
        self.BTN_Stop_2 = tk.Button(self.Frame2, command=stop_recording)
        self.BTN_Stop_2.place(x=60, y=10, height=50, width=60)
        self.BTN_Stop_2.configure(activebackground="beige")
        self.BTN_Stop_2.configure(activeforeground="black")
        self.BTN_Stop_2.configure(background="#00f88c")
        self.BTN_Stop_2.configure(compound='left')
        self.BTN_Stop_2.configure(disabledforeground="#a3a3a3")
        self.BTN_Stop_2.configure(foreground="#000000")
        self.BTN_Stop_2.configure(highlightbackground="#d9d9d9")
        self.BTN_Stop_2.configure(highlightcolor="black")
        photo_location = os.path.join(base_path, "images", "gui", "stop50.png")
        global _img5
        _img5 = tk.PhotoImage(file=photo_location)
        self.BTN_Stop_2.configure(image=_img5)
        self.BTN_Stop_2.configure(pady="0")

#Record 3 =============================================================
        self.Frame3 = tk.Frame(self.top)
        self.Frame3.place(x=20, y=141, height=68, width=356)
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#000b11")
        self.Frame3.configure(highlightbackground="#d9d9d9")
        self.Frame3.configure(highlightcolor="black")
#Boton Record 3 =============================================================
        self.BTN_Record_3 = tk.Button(self.Frame3, command=lambda: start_recording(3))
        self.BTN_Record_3.place(x=10, y=10, height=50, width=50)
        self.BTN_Record_3.configure(activebackground="#002d44")
        self.BTN_Record_3.configure(activeforeground="#00ff00")
        self.BTN_Record_3.configure(background="#00f88c")
        self.BTN_Record_3.configure(compound='center')
        self.BTN_Record_3.configure(disabledforeground="#a3a3a3")
        self.BTN_Record_3.configure(foreground="#000000")
        self.BTN_Record_3.configure(highlightbackground="#002d44")
        self.BTN_Record_3.configure(highlightcolor="black")
        photo_location = os.path.join(base_path, "images", "gui", "save50.png")
        global _img6
        _img6 = tk.PhotoImage(file=photo_location)
        self.BTN_Record_3.configure(image=_img6)
        self.BTN_Record_3.configure(pady="0")
#Boton Stop 3 =============================================================
        self.BTN_Stop_3 = tk.Button(self.Frame3, command=stop_recording)
        self.BTN_Stop_3.place(x=60, y=10, height=50, width=60)
        self.BTN_Stop_3.configure(activebackground="beige")
        self.BTN_Stop_3.configure(activeforeground="black")
        self.BTN_Stop_3.configure(background="#00f88c")
        self.BTN_Stop_3.configure(compound='left')
        self.BTN_Stop_3.configure(disabledforeground="#a3a3a3")
        self.BTN_Stop_3.configure(foreground="#000000")
        self.BTN_Stop_3.configure(highlightbackground="#d9d9d9")
        self.BTN_Stop_3.configure(highlightcolor="black")
        photo_location = os.path.join(base_path, "images", "gui", "stop50.png")
        global _img8
        _img8 = tk.PhotoImage(file=photo_location)
        self.BTN_Stop_3.configure(image=_img8)
        self.BTN_Stop_3.configure(pady="0")
#Boton Play 3 =============================================================
        self.BTN_Play_3 = tk.Button(self.Frame3, command=lambda: start_playing(3))
        self.BTN_Play_3.place(x=120, y=10, height=50, width=220)
        self.BTN_Play_3.configure(activebackground="beige")
        self.BTN_Play_3.configure(activeforeground="black")
        self.BTN_Play_3.configure(background="#00f88c")
        self.BTN_Play_3.configure(compound='left')
        self.BTN_Play_3.configure(disabledforeground="#a3a3a3")
        self.BTN_Play_3.configure(font="-family {Montserrat} -size 9")
        self.BTN_Play_3.configure(foreground="#002d44")
        self.BTN_Play_3.configure(highlightbackground="#d9d9d9")
        self.BTN_Play_3.configure(highlightcolor="#002d44")
        photo_location = os.path.join(base_path, "images", "gui", "play50.png")
        global _img7
        _img7 = tk.PhotoImage(file=photo_location)
        self.BTN_Play_3.configure(image=_img7)
        self.BTN_Play_3.configure(pady="0")
        self.BTN_Play_3.configure(text='''Reproducir Grabación''')

#Record 4 =============================================================
        self.Frame4 = tk.Frame(self.top)
        self.Frame4.place(x=20, y=202, height=67, width=356)
        self.Frame4.configure(relief="groove")
        self.Frame4.configure(background="#000b11")
        self.Frame4.configure(highlightbackground="#d9d9d9")
        self.Frame4.configure(highlightcolor="black")

#Boton Record 4 =============================================================
        self.BTN_Record_4 = tk.Button(self.Frame4, command=lambda: start_recording(4))
        self.BTN_Record_4.place(x=10, y=10, height=50, width=50)
        self.BTN_Record_4.configure(activebackground="#002d44")
        self.BTN_Record_4.configure(activeforeground="#00ff00")
        self.BTN_Record_4.configure(background="#00f88c")
        self.BTN_Record_4.configure(compound='center')
        self.BTN_Record_4.configure(disabledforeground="#a3a3a3")
        self.BTN_Record_4.configure(foreground="#000000")
        self.BTN_Record_4.configure(highlightbackground="#002d44")
        self.BTN_Record_4.configure(highlightcolor="black")
        photo_location = os.path.join(base_path, "images", "gui", "save50.png")
        global _img9
        _img9 = tk.PhotoImage(file=photo_location)
        self.BTN_Record_4.configure(image=_img9)
        self.BTN_Record_4.configure(pady="0")

#Boton Stop 4 =============================================================
        self.BTN_Stop_4 = tk.Button(self.Frame4, command=stop_recording)
        self.BTN_Stop_4.place(x=60, y=10, height=50, width=60)
        self.BTN_Stop_4.configure(activebackground="beige")
        self.BTN_Stop_4.configure(activeforeground="black")
        self.BTN_Stop_4.configure(background="#00f88c")
        self.BTN_Stop_4.configure(compound='left')
        self.BTN_Stop_4.configure(disabledforeground="#a3a3a3")
        self.BTN_Stop_4.configure(foreground="#000000")
        self.BTN_Stop_4.configure(highlightbackground="#d9d9d9")
        self.BTN_Stop_4.configure(highlightcolor="black")
        photo_location = os.path.join(base_path, "images", "gui", "stop50.png")
        global _img11
        _img11 = tk.PhotoImage(file=photo_location)
        self.BTN_Stop_4.configure(image=_img11)
        self.BTN_Stop_4.configure(pady="0")

#Boton Play 4 =============================================================
        self.BTN_Play_4 = tk.Button(self.Frame4, command=lambda: start_playing(4))
        self.BTN_Play_4.place(x=120, y=10, height=50, width=220)
        self.BTN_Play_4.configure(activebackground="beige")
        self.BTN_Play_4.configure(activeforeground="black")
        self.BTN_Play_4.configure(background="#00f88c")
        self.BTN_Play_4.configure(compound='left')
        self.BTN_Play_4.configure(disabledforeground="#a3a3a3")
        self.BTN_Play_4.configure(font="-family {Montserrat} -size 9")
        self.BTN_Play_4.configure(foreground="#002d44")
        self.BTN_Play_4.configure(highlightbackground="#d9d9d9")
        self.BTN_Play_4.configure(highlightcolor="#002d44")
        photo_location = os.path.join(base_path, "images", "gui", "play50.png")
        global _img10
        _img10 = tk.PhotoImage(file=photo_location)
        self.BTN_Play_4.configure(image=_img10)
        self.BTN_Play_4.configure(pady="0")
        self.BTN_Play_4.configure(text='''Reproducir Grabación''')

#Boton Logo =============================================================
        self.BTN_Logo = tk.Button(self.top, command=clickURL)
        self.BTN_Logo.place(x=190, y=270, height=100, width=200)
        self.BTN_Logo.configure(activebackground="#000000")
        self.BTN_Logo.configure(activeforeground="#000000")
        self.BTN_Logo.configure(background="#000000")
        self.BTN_Logo.configure(compound='left')
        self.BTN_Logo.configure(disabledforeground="#002d44")
        self.BTN_Logo.configure(foreground="#002d44")
        self.BTN_Logo.configure(highlightbackground="#002d44")
        self.BTN_Logo.configure(highlightcolor="#002d44")
        photo_location = os.path.join(base_path, "images", "gui", "logostarbot.png")
        global _img12
        _img12 = tk.PhotoImage(file=photo_location)
        self.BTN_Logo.configure(image=_img12)
        self.BTN_Logo.configure(justify='right')
        self.BTN_Logo.configure(pady="0")
        self.BTN_Logo.configure(relief="flat")

def start_recording(button_number):
    recorder.record_macro(f"macros/macro_data_{button_number}.pkl")

def stop_recording():
    recorder.stop_recording()

def start_playing(button_number):
    player_thread = threading.Thread(target=player.play_macro, args=(f"macros/macro_data_{button_number}.pkl",))
    player_thread.start()

def stop_playing():
    player.stop_playing()

def clickURL():
    url = "https://starbot.mx/"  # Reemplaza esta URL con la que desees abrir
    webbrowser.open(url)

def main():
    root = tk.Tk()
    root.title("Macros")

    # Crear una instancia de la clase Toplevel1
    app = Toplevel1(root)

    # Ejecutar la interfaz gráfica
    root.mainloop()

if __name__ == "__main__":
    main()
