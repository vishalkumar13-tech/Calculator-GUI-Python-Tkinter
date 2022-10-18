
from tkinter import *

master = Tk()
master.iconbitmap("calciicon.ico")
master.title("Calci by Atif")
master.configure(bg = "red")
master.geometry("220x250")
master.minsize(300, 415)
master.maxsize(300, 415)

if __name__ == '__main__':

    displayVar = StringVar()
    displayVar.set("")

def onscreen(event):
    key = event.widget.cget("text")
    str = displayVar.get() + key

    if key == "del":
        str = displayVar.get()
        str = str[0 : len(str)-1]
        displayVar.set(str)

    if key == "C":
        displayVar.set("")

    elif key == '=':
        result = eval(displayVar.get())
        displayVar.set(result)

    else:
        displayVar.set(str)

def switch():
    if onoff.get() == "ON":
        onoff.set("OFF")
        display.config(state = NORMAL)
        displayVar.set("")


    else:
        onoff.set("ON")
        display.config(state = DISABLED)
        displayVar.set("switch ON first")


header = Label(master  , text = "basic calculator" , bd = 5 ,font = "times 20 bold" , relief = SUNKEN , bg = "grey" , fg = "white" )
header.pack( fill = "x")


sbarForDisplay = Scrollbar(master , orient = HORIZONTAL )
sbarForDisplay.pack(side = TOP, fill = X)
display = Entry(master   , xscrollcommand = sbarForDisplay.set, textvar = displayVar , insertontime = 900 ,insertofftime = 600 ,insertbackground = "yellow", width = 22  , bd = 5 ,font = "system 25 bold" ,fg = "green" ,  bg = "black")
display.pack(pady = 5)
sbarForDisplay.config(command = display.xview)

f = Frame(master)
b1 = Button(f , text = "C"  , width = 8,height = 3  ,bd =5 ,bg = "pink",  cursor = "exchange")
b1.pack(side = "left"  , pady = 5)
b2 = Button(f  , text = "del", width = 8, bg = "pink" ,height = 3 ,bd =5,activebackground = "red" )
b2.pack(side = "left" ,  padx = 5 ,pady = 5)
b3 = Button(f , text = "%", width = 8 , bd = 5 ,bg = "pink",height = 3 )
b3.pack(side = "left" , pady = 5)
b4 = Button(f , text = "/", width = 8 ,bd =5 , bg = "pink",height = 3 )
b4.pack(side = "left" , pady = 5 ,padx = 5 )
b1.bind('<Button-1>' , onscreen)
b2.bind('<Button-1>' , onscreen)
b3.bind('<Button-1>' , onscreen)
b4.bind('<Button-1>'  , onscreen)
f.pack(side = "top" )

f = Frame(master)
b1 = Button(f , text = "1" , width = 8 , bd =5 ,bg = "grey",height = 2 )
b1.pack(side = "left")
b2 = Button(f  , text = "2", bg = "grey", width = 8
            ,height = 2 )
b2.pack(side = "left",  padx = 5)
b3 = Button(f , text = "3", width = 8 , bd =5 ,  bg = "grey",height = 2 )
b3.pack(side = "left")
b4 = Button(f , text = "*", width = 8 , bd =5 ,bg = "pink",height = 2 )
b4.pack(side = "left",  padx = 5)
b1.bind('<Button-1>' , onscreen)
b2.bind('<Button-1>' , onscreen)
b3.bind('<Button-1>' , onscreen)
b4.bind('<Button-1>' , onscreen)
f.pack(side = "top" )

f = Frame(master)
b1 = Button(f , text = "4" , width = 8,bd =5 , bg = "grey",height = 2 )
b1.pack(side = "left"  , pady = 5 ,)
b2 = Button(f  , text = "5", width = 8 , bd =5 ,bg = "grey",height = 2 )
b2.pack(side = "left"  , pady = 5,  padx = 5 )
b3 = Button(f , text = "6", width = 8, bd =5 ,bg = "grey",height = 2 )
b3.pack(side = "left", pady = 5)
b4 = Button(f , text = "-", width = 8 ,bd =5 , bg = "pink",height = 2 )
b4.pack(side = "left", pady = 5,  padx = 5)
b1.bind('<Button-1>' , onscreen)
b2.bind('<Button-1>' , onscreen)
b3.bind('<Button-1>' , onscreen)
b4.bind('<Button-1>' , onscreen)
f.pack(side = "top" )

f = Frame(master)
b1 = Button(f , text = "7" , bd =5 ,width = 8, bg = "grey",height = 2 )
b1.pack(side = "left")
b2 = Button(f  , text = "8",bd =5 , width = 8 , bg = "grey",height = 2 )
b2.pack(side = "left",  padx = 5)
b3 = Button(f , text = "9", width = 8,bd =5 , bg = "grey",height = 2 )
b3.pack(side = "left")
b4 = Button(f , text = "+", width = 8 , bd =5 ,bg = "pink",height = 2 )
b4.pack(side = "left",  padx = 5)
b1.bind('<Button-1>' , onscreen)
b2.bind('<Button-1>' , onscreen)
b3.bind('<Button-1>' , onscreen)
b4.bind('<Button-1>' , onscreen)
f.pack(side = "top" )

f = Frame(master)
b1 = Button(f , text = "0" , width = 9,bd =5 , bg = "grey",height = 3 )
b1.pack(side = "left", pady = 5)
b2 = Button(f  , text = ".", width = 8,bd =5 , bg = "grey" ,height = 3 )
b2.pack(side = "left", pady = 5,  padx = 5)
b3 = Button(f , text = "=", width = 17 ,bd =5 , bg = "pink" ,height = 3  ,  activebackground = "green" )
b3.pack(side = "left", pady = 5,  padx = 5
        )
b4.pack(side = "left", pady = 5)
b1.bind('<Button-1>' , onscreen)
b2.bind('<Button-1>' , onscreen)
b3.bind('<Button-1>' , onscreen)
f.pack(side = "top")
master.mainloop()
