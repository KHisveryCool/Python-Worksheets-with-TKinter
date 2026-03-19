import tkinter

window = tkinter.Tk()
window.geometry("280x220")
window.title("Layout Explorer")

frame1 = tkinter.Frame(window, bg="lightblue", height=50)
frame1.pack(fill=tkinter.X, padx=5, pady=5)
frame1.pack_propagate(False)

label1_1 = tkinter.Label(frame1, text="Label 1", bg="lightblue")
label1_1.pack(side=tkinter.LEFT)

label1_2 = tkinter.Label(frame1, text="Label 2", bg="lightblue")
label1_2.pack(side=tkinter.RIGHT)

frame2 = tkinter.Frame(window, bg="lightgreen", height=70)
frame2.pack(fill=tkinter.X, padx=5, pady=5)
frame2.pack_propagate(False)

label2_1 = tkinter.Label(frame2, text="Label A", bg="lightgreen")
label2_1.place(x=10, y=10)

label2_2 = tkinter.Label(frame2, text="Label B", bg="lightgreen")
label2_2.place(x=150, y=40)

# --- Frame 3: grid ---
frame3 = tkinter.Frame(window, bg="lightyellow", height=70)
frame3.pack(fill=tkinter.X, padx=5, pady=5)
frame3.pack_propagate(False)

label3_1 = tkinter.Label(frame3, text="A", bg="lightyellow")
label3_1.grid(row=0, column=0, padx=5, pady=5)

label3_2 = tkinter.Label(frame3, text="B", bg="lightyellow")
label3_2.grid(row=0, column=1, padx=5, pady=5)

label3_3 = tkinter.Label(frame3, text="C", bg="lightyellow")
label3_3.grid(row=1, column=0, padx=5, pady=5)

label3_4 = tkinter.Label(frame3, text="D", bg="lightyellow")
label3_4.grid(row=1, column=1, padx=5, pady=5)


window.mainloop()

#Reflection

#Q1) Which layout manager gives the most precise control? What is a disadvantage of using it?
# Answer: Place is the best layout manager as it gives us the option to specify the x and y coordinates, the disadvantage of it, is that it doesn't respond to window resizing

#Q2)2.  What does pack_propagate(False) do? When would you need it?
# Answer: Pack propogate stops automatic resizing and keeps the widget only to the size you set it to. we need for things that needs to be a fixedd size like a scrollbar