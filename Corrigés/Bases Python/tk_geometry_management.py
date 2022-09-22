# Fichier d'exemples de géomertrie Tkinter
from tkinter import Tk, ttk, BOTH

root = Tk()
# Taille fenetre x*y + posx + posy par rapport à l'écran
root.geometry('640x480+200+200')

# Geometry
# Pack
ttk.Label(root, text = 'Hello, Tkinter!', background = 'blue').pack(fill = BOTH, expand = False)
ttk.Label(root, text = 'Hello, Tkinter!', background = 'yellow').pack(fill = BOTH, expand = True)
label = ttk.Label(root, text = 'Hello, Tkinter!',background = 'green')
label.pack(fill = BOTH, expand = True)

# Grid
ttk.Label(root, text = 'Yellow', background = 'yellow').grid(row = 0, column = 0)
ttk.Label(root, text = 'Blue', background = 'Blue').grid(row = 0, column = 1)
ttk.Label(root, text = 'Green', background = 'Green').grid(row = 1, column = 0)
ttk.Label(root, text = 'Orange', background = 'Orange').grid(row = 1, column = 1)

# Place
# (Si besoin de la position exacte)
ttk.Label(root, text = 'Yellow', background = 'yellow').place(x = 100, y = 50, width = 100, height = 50)

root.mainloop()