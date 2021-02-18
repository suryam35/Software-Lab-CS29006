import numpy as np
from ast import literal_eval
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,  NavigationToolbar2Tk

root = Tk()
root.title('Expression Plotter')

f1 = Frame(root , background = "bisque" , width = 10 , height = 200)
f2 = Frame(root , background = "#8feb34" , width = 10 , height = 200)

f1.grid(row = 0 , column = 0 , sticky = N+S+W+E)
f2.grid(row = 0 , column = 1 , sticky = N+S+W+E)

root.grid_columnconfigure(0 , weight = 1)
root.grid_columnconfigure(1 , weight = 1)

root.grid_rowconfigure(0 , weight = 1)

label1 = Label(f1 , background = "#eb6e34", text = "Enter your expression in single variable : " , width = 40 , height =4 ,font=('​Helvetica', 12, 'bold'))
label1.grid(row = 0 , column = 0 , pady = 70 , padx = 30)
e = Text(f1 , width = 30 , height = 4 , padx = 10 , pady = 20 , background = "#eb6e34")
e.delete(1.0 , END)
e.grid(row = 0 , column = 1 , pady = 70 , padx = 30)

label2 = Label(f1 , background = "#eb6e34", text = "Enter your variable range (a , b) :  " , width = 40 , height = 4 ,font=('​Helvetica', 12, 'bold'))
label2.grid(row = 1 , column = 0 , pady = 70 , padx = 30)
f = Text(f1 , width = 30 , height = 4 , pady = 20 , padx = 10, background = "#eb6e34")
f.delete(1.0 , END)
f.grid(row = 1 , column = 1 , pady = 70 , padx = 30)

label3 = Label(f2 , background = "#34ebdc", text = "This is your plot" , width = 40 , height = 4 , font=('​Helvetica', 14, 'bold')).pack(padx = 10 , pady = 10)
fig = Figure(figsize = (5, 5),dpi = 100)
canvas = FigureCanvasTkAgg(fig, master = f2)

def plot():
    canvas.get_tk_widget().pack_forget()
    expr = e.get(1.0 , END)
    var_range = f.get(1.0 , END)
    a = literal_eval(var_range)
    x = np.linspace(a[0], a[1] , 1000)
    for value in np.linspace(a[0] , a[1] , 1000):
        expr = expr.strip('\n')
        global y
        y = eval(expr)
    plot1 = fig.add_subplot(111) 
    plot1.cla()
    plot1.plot(x,y) 
    plot1.set_xlabel('x')
    plot1.set_ylabel(expr)
    plot1.set_title('Graph')   
    canvas.draw()
    canvas.get_tk_widget().pack(pady = 30 , padx = 8)
  

plot_button = Button(master = f1,background = "#eba834",command = plot, height = 2, width = 10,text = "Plot", bd=5)
plot_button.grid(row = 2 , column = 1 , columnspan =2) 

exit_button = Button(f1 ,  background = "#eba834" ,text = "Exit" , command = root.quit , height = 2 , width = 10 , bd = 5).grid(row = 2 , column = 0)

root.mainloop()