from tkinter import *
import tkinter as tk
import tkinter.font as font
from tkinter import ttk
import runpy
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from numpy import sin ,cos,exp,log,sqrt
from math import pi
from math import *
import sympy as sp

 
app = Tk()
app.geometry("650x420")
app.resizable(width=False, height=False)
app.title("EasyMATH")

img = PhotoImage(file = 'capture.png')
canvas = Canvas(app, width=650, height=418)
canvas.create_image(300, 210, image=img)
canvas.grid()

menubar = Menu(app)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Créer")
menu1.add_command(label="Editer")
menu1.add_separator()
menu1.add_command(label="Quitter", command=app.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Couper")
menu2.add_command(label="Copier")
menu2.add_command(label="Coller")
menubar.add_cascade(label="Editer", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos")
menubar.add_cascade(label="Aide", menu=menu3)

app.config(menu=menubar)

def CalculInterp ():


    file_globals = runpy.run_path("interpolation.py")


def CalculInteg ():
    
    file_globals = runpy.run_path("integration.py")


def start():
    start = Tk()
    start.geometry("650x420")
    start.resizable(width=False, height=False)
    #start.sizefrom("user")
    start.title("EasyMATHt")
    htLabel = Label(start, text="L'interpolation Polynomiale",fg="Red",font='Times 18 bold')
    htLabel.place(x=8,y=8)
    
    text1 = Text(start, height=6, width=79)
    text1.place(y=48)
    quote = """"En mathématiques, en analyse numérique, l'interpolation polynomiale est une   technique d'interpolation d'un ensemble de données ou d'une fonction par un    polynôme En d'autres termes, étant donné un ensemblede points obtenu, par      exemple, à la suite d'une expérience), on cherche un polynôme qui passe par    tous ces points, et éventuellement vérifie d'autres conditions, de degré si    possible le plus bas."""
    text1.insert(tk.END, quote) 
    button = Button(start, text='Essayer!', bg='#c27b5f', fg='#fcf5f2',font='Helvetica 14 bold',command=CalculInterp)
    button.place(x = 280,y = 152)
   
    Label2 = Label(start, text="L'integration Numérique",fg="Red",font='Times 18 bold')
    Label2.place(x=8,y=212)
    
    text2 = Text(start, height=6, width=79)
    text2.place(y=252)
    fact = """L’intégration est un des problèmes les plus importants que l’on rencontre en
analyse. En effet, on rencontre souvent des intégrales dont le calcul par des
méthodes analytiques est très compliqué ou même impossible, car il n’existe
pas d’expression analytique de la primitive de la fonction à intégrer 
Dans ces cas, on peut appliquer des méthodes numériques pour évaluer la
valeur de l’intégrale donnée. """
    text2.insert(tk.END, fact) 
    button2 = Button(start, text='Essayer!', bg='#c27b5f', fg='#fcf5f2',font='Helvetica 14 bold',command=CalculInteg)
    button2.place(x = 280,y = 360)
    
    
    start.mainloop()
    
    
   

bouton_quit = Button(app, text='Quitter', font='batmfa.ttf', command=app.destroy, padx=20, pady=10, cursor="target")
bouton_quit.place(x=530, y=250)

# bouton_regle = Button(app, text='Règles', font='arial.ttf', padx=20, pady=10, cursor="target")
# bouton_regle.place(x=530, y=200)

bouton_start = Button(app, text='START', command=start, font='arial.ttf', padx=20, pady=10, cursor="target")
bouton_start.place(x=530, y=150)


	
app.mainloop()	
	