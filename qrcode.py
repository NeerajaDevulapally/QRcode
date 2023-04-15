from tkinter import messagebox 
from pyqrcode import create 
import tkinter 
from tkinter import *

root=tkinter.Tk()
root.title('QR Generator')
root.resizable(FALSE,FALSE)
#root.iconbitmap(r"C:\xampp\htdocs\QRCODE\favicon(1).ico")

heading=tkinter.Label(root,text="QR Code Generator",font="times 20")
heading.pack(side=TOP,pady=15)

frame=LabelFrame(root,padx=20,pady=50)
frame.pack(padx=10,pady=10)

def gen_qr():
    global dta
    dta = subtitle.get()
    dta = create(dta)
    test = dta.xbm(scale=2)
    global xbm_image
    if (subtitle.get() == "Enter URL or text here" or subtitle.get()==""):
        messagebox.showerror("ERROR", "Enter the URL or Text")
    else:
        xbm_image = BitmapImage(data=test, foreground="black", background='white')
        image_view.config(image=xbm_image)

def temp_text(e):
    subtitle.delete(0,"end")
subtitle =Entry(frame,width=35,font=("Ubuntu Mono", 16))
subtitle.pack(padx=10,pady=10,anchor=W)
subtitle.insert(0,"Enter URL or text here")
subtitle.bind("<FocusIn>", temp_text)
make_button = Button(frame, text="Generate QR", font="italic", command=gen_qr,relief=SOLID,anchor=W)
image_view =Label(frame)
statement = Label(frame)

subtitle.grid(row=1, column=0)
make_button.grid(row=50, column=0, columnspan=2)
image_view.grid(row=51, column=0, columnspan=2)
statement.grid(row=52, column=0, columnspan=2)
root.mainloop()