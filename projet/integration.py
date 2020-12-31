from tkinter import *
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from numpy import sin ,cos,exp,log,sqrt
import matplotlib.pyplot as plt 



class Trapezoidal( object ) :
    def __init__ (self , a , b , n , f ) :
        self.a = a
        self.b = b
        self.x = np.linspace( a , b , n+1 )
        self.f = f
        self.n = n
    def integrate ( self , f ) :
        x= self.x
        y= f( x )
        h = float( x[1] - x[0] )
        s = y[0] + y[-1] + 2.0*sum(y[1:-1])
        return h * s /2.0
    def Graph ( self , f , resolution =1001 ) :
        xl = self.x
        yl = f(xl)
        xlist_fine =np.linspace( self.a , self.b , resolution )
        for i in range ( self.n ) :
            x_rect = [xl[ i ] , xl[ i ] , xl[ i + 1 ] , xl[i+1] , xl[ i ] ] # abscisses des sommets
            y_rect = [0 , yl[ i ] , yl[ i+1 ] , 0 , 0 ] # ordonnees des sommets
            plt.plot ( x_rect , y_rect , 'g' )
        yflist_fine = f ( xlist_fine )
        plt.plot ( xlist_fine , yflist_fine )
        plt.plot(xl, yl,"bo")
        plt.xlabel ( 'x' )
        plt.ylabel ( ' f ( x ) ' )
        plt.title ( ' Methode des Trapèzes' )
        plt.text( 0.5*( self.a+ self.b ) , f(self.b ) , 'I_{} ={:0.4f}'.format(self.n,self.integrate( f ) ) , fontsize =11 )
        
class RectangleG ( object ) :
    def __init__ (self , a , b , n , f ) :
        self.a = a
        self.b = b
        self.x = np.linspace( a , b , n+1 )
        self.f = f
        self.n = n
    def integrate ( self , f ) :
        x= self.x
        y= f(x)
        h = float( x[1] - x[0] )
        s = sum( y[ 0 : -1 ] )
        return h * s
    def Graph ( self , f , resolution =1001 ) :
        xl = self.x
        yl = f(xl)
        xlist_fine =np.linspace( self.a , self.b , resolution )
        for i in range ( self.n ) :
            x_rect = [xl[ i ] , xl[ i ] , xl[ i + 1 ] , xl[i+1] , xl[ i ] ] # abscisses des sommets
            y_rect = [0 , yl[ i ] , yl[ i ] , 0 , 0 ] # ordonnees des sommets
            plt.plot ( x_rect , y_rect , 'r' )
        yflist_fine = f ( xlist_fine )
        plt.plot ( xlist_fine , yflist_fine )
        plt.plot(xl, yl,"bo")
        plt.xlabel ( 'x' )
        plt.ylabel ( ' f ( x ) ' )
        plt.title ( ' Methode des rectangles gauches' )
        plt.text( 0.5*( self.a+ self.b ) , f(self.b ) , 'I_{} ={:0.4f}'.format(self.n,self.integrate( f ) ) , fontsize =11 )        
        
class RectangleM ( object ) :
    def __init__ (self , a , b , n , f ) :
        self.a = a
        self.b = b
        self.x = np.linspace( a , b , n+1 )
        self.f = f
        self.n = n
    def integrate ( self , f ) :
        x= self.x
        h = float(x[1] - x[0])
        s=0
        for i in range(self.n):
            s=s+f((x[i]+x[i+1])*0.5)
        return h * s
    def Graph (self,f,resolution =1001 ):
        xl = self.x
        yl = f(xl)
        xlist_fine =np.linspace( self.a , self.b , resolution )
        for i in range ( self.n ) :
            m=(xl[i]+xl[i+1])/2
            x_rect = [xl[ i ] , xl[ i ] , xl[ i + 1 ] , xl[i+1] , xl[ i ] ] # abscisses des sommets
            y_rect = [0 , f(m) , f(m) , 0 , 0 ] # ordonnees des sommets
            plt.plot ( x_rect , y_rect , 'r' )
        yflist_fine = f ( xlist_fine )
        plt.plot ( xlist_fine , yflist_fine )
        plt.plot(m,f(m),"bo")
        plt.xlabel ( 'x' )
        plt.ylabel ( ' f ( x ) ' )
        plt.title ( ' Methode de point milieu' )
        plt.text( 0.5*( self.a+ self.b ) , f(self.b ) , 'I_{} ={:0.4f}'.format(self.n,self.integrate( f ) ) , fontsize =11 )        

class Simpson( object ) :
    def __init__ (self , a , b , n , f ) :
        self.a = a
        self.b = b
        self.x = np.linspace( a , b , n+1 )
        self.f = f
        self.n = n
    def integrate ( self , f ) :
        x= self.x
        y= f(x)
        h = float(x[2] - x[1])
        n = len(x) - 1
        if n % 2 == 1 :
            raise ValueError("N must be an even integer.")
        s = y[0] + y[n] + 4.0 * sum(y[1:-1:2]) + 2.0 * sum(y[2:-2:2])
        return h * s / 3.0
    def Graph(self , f , resolution =1001):
        xl = self.x
        yl = f(xl)
        xlist_fine =np.linspace( self.a , self.b , resolution )
        for i in range ( self.n ) :
            xx = np.linspace(xl[ i ],xl[i + 1],resolution)
            m = (xl[i]+ xl[i + 1])/ 2
            a = xl[i]
            b = xl[i +1]
            l0  =(xx-m)/(a-m)*(xx-b)/(a-b)
            l1 =(xx-a)/(m-a)*(xx-b)/(m-b)
            l2 =(xx-a)/(b-a)*(xx-m)/(b-m)
            P = f(a)*l0 + f(m)*l1 + f(b)*l2
            plt.plot( xx , P , "r")
        yflist_fine = f(xlist_fine )
        plt.plot(xlist_fine , yflist_fine, 'g')
        plt.plot( xl , yl , "ro ")
        plt.xlabel('x')
        plt.ylabel( 'f( x )')
        plt.title( 'Methode de Simpson ')
        plt.text( 0.5*( self.a+ self.b ) , f(self.b ) , 'I_{} ={:0.4f}'.format(self.n,self.integrate( f ) ) , fontsize =11 )        
        
def designer ():
        
        f= lambda x: eval(input_F.get())
        
        aa=float(input_a.get())
        bb=float(input_b.get())
        nn=int(input_n.get())
        T=Trapezoidal(aa,bb,nn,f)
        S = Simpson(aa,bb,nn,f)
        R = RectangleG(aa,bb,nn,f)
        M=RectangleM(aa,bb,nn,f)
        fig = plt.figure()
        
        ax = fig.add_subplot(221) 
        ax.grid(True)
        R.Graph(f)
        
        ax = fig.add_subplot(222)
        ax.grid(True)
        S.Graph(f)
        
        ax = fig.add_subplot(223)
        ax.grid(True)
        T.Graph(f)
        
        ax = fig.add_subplot(224)
        M.Graph(f)
        ax.grid(True)
        fig.tight_layout()
        window.canvas = FigureCanvasTkAgg(fig, master=fr2)
        window.canvas.get_tk_widget().pack()
        window.canvas.draw()
        plt.show()
        
window = Tk() 
#window.geometry('1000x540') 
window.resizable(width=False, height=False)
window.title("Integration")

fr1 = Frame(window,highlightbackground="gray", highlightthickness=2, width=280, height=563, bd= 5)
fr2 = Frame(window,highlightbackground="darkgray", highlightthickness=2, width=550, height=563, bd= 5)

Label_F = Label(fr1,text = "Entrer la fonction : ", height=4).grid(sticky = E,row=1,column=0)     
input_F = Entry(fr1, width = 30)
input_F.grid(sticky = W,row=1,column=1)    
               
Label_a = Label(fr1, text = "a", height=4).grid(sticky = E,row=2,column=0)
input_a = Entry(fr1, width = 30)
input_a.grid(sticky = W,row=2,column=1) 


Label_b = Label(fr1, text = "b", height=4).grid(sticky = E,row=3,column=0)
input_b = Entry(fr1, width = 30)
input_b.grid(sticky = W,row=3,column=1) 

Label_n = Label(fr1, text = "N", height=4).grid(sticky = E,row=4,column=0)
input_n = Entry(fr1, width = 30)
input_n.grid(sticky = W,row=4,column=1)

submit_button = Button(fr1, text = "Calculer",bg="#fac8dd", fg="#300618",command=designer ,font='Helvetica 11 bold').grid(row=5,column=0,columnspan=3)

fr1.grid(row=1,column=0,padx=10,pady=10,sticky="ns")
fr2.grid(row=1,column=1,padx=10,pady=10) 




window.mainloop()  