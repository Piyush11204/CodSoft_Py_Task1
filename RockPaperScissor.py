from tkinter import *
from tkinter import ttk
import random
root = Tk()  
root.title("Piyush Krishnadutt Yadav")  
root.geometry("680x500")  
root.config(bg = "#41A0F4")  
root.resizable(width = False, height = False) 
 
heading = Label(  
    root,  
    text = 'Let\'s Play Rock Paper Scissor',  
    font ="Kalnia 22 bold",  
    bg = '#41A0F4',  
    fg = 'black'  
    ).pack()  

computer_value = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor"
}
def reset_game():
    
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text="Player                ")
    l3.config(text="Computer")
    l4.config(text="")

def exitGame():  
    root.destroy()  
def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"
def isrock():
    comp = computer_value[str(random.randint(0, 2))]
    if comp == "Rock":
        match_result = "Match Draw"
    elif comp == "Scissor":
        match_result = "Victorious"
    else:
        match_result = "Defeated"
    l4.config(text=match_result)
    l1.config(text="Rock               ")
    l3.config(text=comp)
    button_disable()
def ispaper():
    comp = computer_value[str(random.randint(0, 2))]
    if comp == "Paper":
        match_result = "Match Draw"
    elif comp == "Scissor":
        match_result = "Defeated"
    else:
        match_result = "Victorious"
    l4.config(text=match_result)
    l1.config(text="Paper              ")
    l3.config(text=comp)
    button_disable()
 

def isscissor():
    comp = computer_value[str(random.randint(0, 2))]
    if comp == "Rock":
        match_result = "Defeated"
    elif comp == "Scissor":
        match_result = "Match Draw"
    else:
        match_result = "Victorious"
    l4.config(text=match_result)
    l1.config(text="Scissor            ")
    l3.config(text=comp)
    button_disable()
 
Label(root,
      text="The Game is ON!!!",
      bg = '#41A0F4',  
      font=("Helvetica", 20 ,"bold"),
      
      
      fg="black").pack(pady=20)
 
frame1 = Frame(root)
frame1.pack()
 
b1 = Button(frame1, text="Rock",
            font=10, width=15, bg="#54FF22",borderwidth=5,
            command=isrock)
 
b2 = Button(frame1, text="Paper ",
            font=10, width=15, bg="#FF2222",borderwidth=5,
            command=ispaper)
 
b3 = Button(frame1, text="Scissor",
            font=10, width=15, bg="#52FFE5",borderwidth=5,
            command=isscissor)
 
b1.pack(side=LEFT, padx=1,)
b2.pack(side=LEFT, padx=1,)
b3.pack(padx=1)


frame = Frame(root)
frame.pack(pady=30,expand=12 )


l1 = Label(frame,
           text="Player                ",borderwidth=5,
           font="normal 20 bold")
 
l2 = Label(frame,
           text="VS             ",borderwidth=5,
           font="normal 20 bold")
l2 = Label(frame,
           text="VS             ",borderwidth=5,
           font="normal 20 bold")
 
 
l3 = Label(frame, text="Computer", font="normal 20 bold",borderwidth=2,)

 
l1.pack(side=LEFT)
l2.pack(side=LEFT)


l4 = Label(root,
           text="Select One",
           font="normal 20 bold",
           bg="white",
           width=15,
           borderwidth=2,
           relief="solid")
l4.pack(pady=20,)

l3.pack(side=RIGHT)

Button(root, text="Once More",
        font ="cercive 15 bold", fg="black",borderwidth=4,
       
       bg="white", command=reset_game).pack(pady=20,)


Button(root, text="Exit Game",
         font ="cercive 15 bold", fg="red",borderwidth=4,
       
       bg="white", command=exitGame).pack(pady=20,)

root.mainloop()