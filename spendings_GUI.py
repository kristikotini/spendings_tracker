from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from regression_modul import Regression_Modul
from import_data import *

import tkinter.messagebox



class Spending_GUI:
    
   def __init__(self, root):
        self.root=root
        self.root.resizable()
        self.root.title("Savings Tracker")
        self.root.geometry("600x300+100+100")
        self.add_savings(root)
        self.show_food_chart(root)
        self.show_clothes_chart(root)
        self.show_free_time_chart(root)
        self.total_savings(root)
        self.predict_next_month(root)
          
   def add_savings(self,master):
       frame =Frame(master)
       button =Button(frame,text='Add Savings', fg='blue')
       button.grid(padx=5, pady=5)
       frame.grid(sticky="nsew")

   def show_food_chart(self,master):
       frame =Frame(master)
       button =Button(frame,text='Show Food Chart', fg='red',command=self.paint_food_data)
       button.grid(padx=5, pady=5)
       frame.grid(row=0,column=1,sticky="nsew")

   def show_clothes_chart(self,master):
       frame =Frame(master)
       button =Button(frame,text='Show Clothes Chart', fg='red',command=self.paint_clothes_data)
       button.grid(padx=5, pady=5)
       frame.grid(row=0,column=2,sticky="nsew")

   def show_free_time_chart(self,master):
       frame =Frame(master)
       button =Button(frame,text='Show Free Time Chart', fg='red',command=self.paint_free_time_data)
       button.grid(padx=5, pady=5)
       frame.grid(row=0,column=3,sticky="nsew")

   def total_savings(self,master):
       frame =Frame(master)
       button =Button(frame,text='Total Savings', fg='blue',command=self.get_total_savings)
       button.grid(padx=5, pady=5)
       frame.grid(row=1,column=0,sticky="nsew")
    
   def paint_food_data(self):
       f = Figure(figsize=(2.1,2.1))
       a = f.add_subplot(111)
       a.plot(get_food_data())
       canvas = FigureCanvasTkAgg(f, master=self.root)
       canvas.draw()
       canvas.get_tk_widget().grid(row=3,column=1,padx=5, pady=5)
   def paint_clothes_data(self):
       f = Figure(figsize=(2.1,2.1))
       a = f.add_subplot(111)
       a.plot(get_clothes_data())
       canvas = FigureCanvasTkAgg(f, master=self.root)
       canvas.draw()
       canvas.get_tk_widget().grid(row=3,column=2,padx=5, pady=5)
   def paint_free_time_data(self):
       f = Figure(figsize=(2.1,2.1))
       a = f.add_subplot(111)
       a.plot(get_free_time_data())
       canvas = FigureCanvasTkAgg(f, master=self.root)
       canvas.draw()
       canvas.get_tk_widget().grid(row=3,column=3,padx=5, pady=5)
   def get_total_savings(self):
      tkinter.messagebox.showinfo("Total Savings ", get_savings())
   
   def predict_next_month(self,master):
       frame =Frame(master)
       button =Button(frame,text='Predict Next Month', fg='green',command=self.get_prediction)
       button.grid(padx=5, pady=5)
       frame.grid(row=1,column=1,sticky="nsew")
   def get_prediction(self):
      vl1 = tkinter.simpledialog.askinteger("Income", "Put Income?",minvalue=0, maxvalue=10000)
      vl2 = tkinter.simpledialog.askinteger("Clothes", "Put Clothes Spendings",minvalue=0, maxvalue=5100)
      vl3 = tkinter.simpledialog.askinteger("Foods", "Put Foods Spendings?",minvalue=0, maxvalue=5100)
      vl4 = tkinter.simpledialog.askinteger("Free Time", "Put Free Time Spendings?",minvalue=0, maxvalue=5100)
      x=np.array([vl1,vl2,vl3,vl4],ndmin=2)
      r = Regression_Modul()
      vlera = r.prediction(x)
      tkinter.messagebox.showinfo("Predicted Value", vlera)
       
  
   
      
   

   
   
      
        

