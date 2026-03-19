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

#Q1)What happens if you comment out window.mainloop() and run the program?
# Answer: The program will exit and the window will close instantly

#Q2)What are the two numbers in window.geometry('300x150')? What do they control?
# Answer: These are height and width of the window, first one is the x coordinate and or width and second one is the y coordinate or height
