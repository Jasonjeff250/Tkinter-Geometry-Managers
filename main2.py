from tkinter import *
#screen setup
root=Tk()
root.geometry("500x400")
root.title("Number Pad")
#display box
entry=Entry(root,width=20,font=('Arial',18),borderwidth=5,justify="right")
entry.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
#function to click on the numbers
def click(num):
    #get the current text inside the box
    current=entry.get()
    #clear the entry
    entry.delete(0,END) 
    #Insert the new text
    entry.insert(0,current+str(num))
#function - clear the entry box
def clear():
    entry.delete(0,END)
#buttons
buttons=[
    ('1',1,0),('2',1,1),('3',1,2),
    ('4',2,0),('5',2,1),('6',2,2),
    ('7',3,0),('8',3,1),('9',3,2),
    ('0',4,1)
]
#create the buttons
for (text,row,col) in buttons:
    Button(root,text=text,padx=20,pady=20,command=lambda t=text:click(t),relief=SUNKEN).grid(row=row,column=col)
#extra buttons
Button(root,text='C',padx=20,pady=20,command=clear,relief=SUNKEN).grid(row=4,column=0)
#exit button
Button(root,text="X",padx=20,pady=20,command=root.quit,relief=SUNKEN).grid(row=4,column=2)
root.mainloop()