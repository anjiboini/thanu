from tkinter import *
root = Tk()

def myClick1():
    myLabel1 = Label(root,text="Thanu sri , Thanu Sri",fg='Blue')
    myLabel1.pack()

def myClick2():
        myLabel2 = Label(root, text="Yesha Sri, Yesha Sri",fg='Red')
        myLabel2.pack()


myButton1 = Button(root,text="thanu--Click me!",command=myClick1,padx=50,pady=50,fg='Blue',bg='Yellow')
myButton2 = Button(root,text="yeshu-- Click me!",command=myClick2,padx=50,pady=50,fg='Red',bg='Pink')

myButton1.pack()
myButton2.pack()

root.mainloop()
#..........................................................#

#myButton = Button(root,Text="Click me!")
#myButton.pack()


#root.mainloop()

