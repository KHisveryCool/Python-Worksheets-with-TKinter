import tkinter

#lets create the main window

window= tkinter.Tk()

#window title
window.title("My first window")

#set window size
window.geometry("350x150")

#create a label
label_1 = tkinter.Label(window,text="Welcome to Python GUI!")
label_2 = tkinter.Label(window,text="IY499")
label_3 = tkinter.Label(window,text="Interface Design")

label_1.pack()
label_2.pack()
label_3.pack()

window.mainloop()

#Reflection

#Q1) Which layout manager gives the most precise control? What is a disadvantage of using it?
# Answer: Place is the best layout manager as it gives us the option to specify the x and y coordinates, the disadvantage of it, is that it doesn't respond to window resizing

#Q2)2.  What does pack_propagate(False) do? When would you need it?
# Answer: Pack propogate stops automatic resizing and keeps the widget only to the size you set it to. we need for things that needs to be a fixedd size like a scrollbar