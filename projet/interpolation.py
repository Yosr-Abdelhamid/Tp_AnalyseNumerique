from tkinter import *
from tkinter import messagebox
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from numpy import sin ,cos,exp,log,sqrt
from math import pi
from math import *
import sympy as sp

sp.var("X") # declare la variable formelle X

def lagrange(x, y):
    n = len(x) - 1
    A = np.transpose(np.tile(x, (n + 1, 1)))
    B = np.tile(range(0, n + 1), (n + 1, 1))
    M = A ** B
    a = np.linalg.solve(M, y)
    P = a[0]
    for i in range(1, n + 1):
        P = P + a[i] * X ** i
    return P

class mclass:

    def __init__(self, window):
        self.window = window
        
        self.fr1 = Frame(window,highlightbackground="gray", highlightthickness=2, width=80, height=230, bd= 5)
        self.fr2 = Frame(window,highlightbackground="darkgray", highlightthickness=2, width=450, height=300, bd= 5)
        
 
       
        labelTitle = Label(self.fr1, text="le polynôme d'interpolation de Lagrange", fg="#2F4F4F", height=2)
        labelTitle.grid(row=0, columnspan=3, sticky=S, padx=10)

        
        labelF = Label(self.fr1, text = "La fonction f(x) : ", height=2)
        labelF.grid(row=4,column=0 ,sticky=E)

        
        self.boxF = Entry(self.fr1, bd=4, width=40)
        self.boxF.grid(row=4, column=1)

        
        labelA = Label(self.fr1, text="La borne inférieur, a :", height=2)
        labelA.grid(row=5,column=0, sticky=E)

        
        self.boxA = Entry(self.fr1, bd=4, width=40)
        self.boxA.grid(row=5, column=1)

       
        labelB = Label(self.fr1, text="La borne supérieur, b :", height=2)
        labelB.grid(row=6, sticky=E,column=0)

        
        self.boxB = Entry(self.fr1, bd=4, width=40)
        self.boxB.grid(row=6, column=1)
        
        
        labelN = Label(self.fr1, text="N  :", height=2)
        labelN.grid(row=7,column=0, sticky=E)

       
        self.boxN = Entry(self.fr1, bd=4, width=40)
        self.boxN.grid(row=7, column=1)
        
        
        self.mylist = []
     
        labelX = Label(self.fr1, text="Valeurs de X :", height=2)
        labelX.grid(row=8, sticky=E,column=0)
        
        
        self.boxX = Entry(self.fr1, bd=4, width=40)
        self.boxX.grid(row=8, column=1, pady=10, padx=10)
        
        self.button1 = Button(self.fr1, text="  PLOT  ", bg="#2F4F4F", fg="white",width=20,command=self.plot)
        self.button1.grid(row=9, column=1)
        
        self.fr1.grid(row=1,column=0,padx=10,pady=10,sticky="ns")
        self.fr2.grid(row=1,column=1,padx=10,pady=10)
    
        
    def read_inputs(self):
        x_input = self.boxX.get()
        
        def convert_to_float_list(x_in):
            x_input_list = x_in.split(' ')
            x_floats = [float(x) for x in x_input_list]
            return x_floats
        
        x_array = np.array(convert_to_float_list(x_input))

        return x_array
    
   
    def plot(self):
        
            N = int(self.boxN.get())
            a = float(self.boxA.get())
            b = float(self.boxB.get())
            F = self.boxF.get().lower().replace(' ', '')
            f1= lambda x: eval(F)
            f=np.vectorize(f1)
            z = self.read_inputs()
            x_fin = np.linspace(a, b,N)
            fig = plt.figure(figsize=(4.5,4.5))
            
            plt.plot(x_fin, f(x_fin), color="red", label="$f$")

            y = f(z)

            plt.plot(z, y, marker="o", color="black", linestyle="None",
                     label="$(x_i, y_i)$")
            ax = plt.gca()
            ax.set_xlim(-2, 2.5)
            ax.set_ylim(-10, 20)
            ax.grid(True)

            P = lagrange(z, y)
            yP = [P.subs(X, c) for c in x_fin]
            plt.plot(x_fin, yP, label="$P$")
            plt.legend(loc=0, prop={'size': 18})
            self.canvas = FigureCanvasTkAgg(fig, master=self.fr2)
            self.canvas.get_tk_widget().pack()
            self.canvas.draw()
            plt.show()
            
       
           
window = Tk() 
window.resizable(width=False, height=False) 
start = mclass(window)
window.title("Interpolation")
window.mainloop() 



















