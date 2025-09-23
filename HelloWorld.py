import tkinter
import csv

from tkinter.constants import *
from tkinter import *
tk = tkinter.Tk()
tk.geometry("1000x720")
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=10)
frame.pack(fill=BOTH, expand=1)

with open ('JJInventoryDatabase - Sheet1.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='', quotechar='|') 
    
    for row in reader:
        print (', ',row)
        
label = tkinter.Label(frame, text="Junk Junction", )
label2 = tkinter.Label(frame, text="Sarkis was here", bg = "darkred", font = ("Arial", 32))
label.pack(fill=X, expand=1)
label2.pack(fill=X, expand=1)
button = tkinter.Button(frame, text="Destroy", command=tk.destroy)
button.pack(side=BOTTOM)
tk.mainloop()