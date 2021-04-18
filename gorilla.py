# A gorilla game. Nachiket Gokhale gokhalen@gmail.com
# A remake of the old Qbasic game in Python3
# Two gorillas throw a steel ball at each other.
# Last one standing wins

import shapely
from shapely.geometry import Polygon,MultiPolygon
from shapely.geometry.collection import GeometryCollection

import tkinter

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk 
from matplotlib.figure import Figure

# descartes 
from descartes.patch import PolygonPatch

# pillow
from PIL import Image,ImageTk

def welcome():
    print('-'*80)
    print('A gorilla game by Nachiket Gokhale gokhalen@gmail.com')
    print('-'*80)

def goodbye():
    print('-'*80)
    print('Exiting gracefully ... goodbye!.')
    print('-'*80)

class Gorilla():
    pass

class Skyline():
    pass

class Building():
    pass

class Ball():
    pass
    
class GorillaGui():
    def __init__(self,sc_width=7.0,sc_height=7.0,width=1000,height=100,refresh_rate=15):
        # sc_* , screen width, height in inches
        # width,length = actual physical length and height in meters
        
        self.sc_width  = sc_width
        self.sc_height = sc_height
        self.width     = width
        self.height    = height

        # refresh rate in milli-sec
        self.refresh_rate = refresh_rate

        # constants
        self.gg        = 9.81   # gravity

        # dimensions of all the frames
        alpha = 0.15
        self.f00_width  = self.sc_width*(1-alpha)
        self.f00_height = self.sc_height*(1-alpha)
        
        self.f10_width  = self.sc_width*(1-alpha)
        self.f10_height = self.sc_height*alpha
        
        self.f01_width  = self.sc_width*alpha
        self.f01_height = self.sc_height*(1-alpha)

        self.f11_width  = self.sc_width*alpha
        self.f11_height = self.sc_height*alpha
        
        pass

    def make_objects(self):
        skyline = Skyline()
        pass
    
    def make_gui(self):
        self.root = tkinter.Tk()
        self.root.wm_title('Gorilla')

        # make the root grid
        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_rowconfigure(1, weight=0)
        self.root.grid_columnconfigure(0, weight=0)
        self.root.grid_columnconfigure(1, weight=0)

        # make the frames
        self.Frame00 = tkinter.Frame(self.root,width=str(self.f00_width)+'i',height=str(self.f00_height)+'i',
                                     highlightbackground="black",highlightthickness=1
                                     )
        self.Frame10 = tkinter.Frame(self.root,width=str(self.f10_width)+'i',height=str(self.f10_height)+'i',
                                     highlightbackground="black",highlightthickness=1
                                     )
        self.Frame01 = tkinter.Frame(self.root,width=str(self.f01_width)+'i',height=str(self.f01_height)+'i',
                                     highlightbackground="black",highlightthickness=1
                                     )
        self.Frame11 = tkinter.Frame(self.root,width=str(self.f11_width)+'i',height=str(self.f11_height)+'i',
                                     highlightbackground="black",highlightthickness=1
                                     )

        # put frames in root grid
        self.Frame00.grid(row=0,column=0); self.Frame00.grid_propagate(False)
        self.Frame10.grid(row=1,column=0); self.Frame10.grid_propagate(False)        
        self.Frame01.grid(row=0,column=1); self.Frame01.grid_propagate(False)
        self.Frame11.grid(row=1,column=1); self.Frame11.grid_propagate(False)

        # make grids on the frames as needed
        self.Frame00.grid_rowconfigure(0,weight=0)
        self.Frame00.grid_columnconfigure(0,weight=0)        
        
        self.Frame11.grid_rowconfigure(0,weight=0)
        self.Frame11.grid_columnconfigure(0,weight=0)
        

        # make canvas
        self.fig = Figure(figsize=(self.f00_width,self.f00_height),dpi=100)
        self.ax  = self.fig.gca()
        self.canvas = FigureCanvasTkAgg(self.fig,master=self.Frame00)
        self.canvas.get_tk_widget().grid(row=0,column=0)

        # make gorilla image on lower right
        # https://stackoverflow.com/questions/23901168/how-do-i-insert-a-jpeg-image-into-a-python-tkinter-window
        # see Engineer_Chris' comment
        gorilla_img = ImageTk.PhotoImage(Image.open('images/gorilla.png'))
        label = tkinter.Label(self.Frame11, image=gorilla_img)
        label.image = gorilla_img
        label.grid(row=0,column=0)

    def gorilla_artist(self):
        # responsible for drawing on canvas
        # self.ax.set_aspect('equal')
        self.ax.plot([1,2,3],[4,5,6],'bo-')
        self.canvas.draw()
        self.root.after(self.refresh_rate,self.gorilla_artist)

    def mainloop(self):
        self.root.after(self.refresh_rate,self.gorilla_artist)
        tkinter.mainloop()
    

if __name__ == '__main__':
    welcome()
    
    g_gui = GorillaGui(sc_width=14.0,sc_height=7.0)
    g_gui.make_objects()
    g_gui.make_gui()
    g_gui.mainloop()
    
    goodbye()
