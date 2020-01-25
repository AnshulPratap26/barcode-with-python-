from barcode.writer import ImageWriter
import barcode
from tkinter import *
from PIL import ImageTk,Image


def barcodee():
    Ean = barcode.get_barcode_class('ean13')
    ean = Ean('123456789012', writer=ImageWriter())
    ean.save('barcodeimgae')



root = Tk()
root.title('barcode')
root.geometry('455x355')
text = Text(width=30,height=2,font= 18)
text.place(x=70,y=150)
button = Button(name='barcode',command=barcodee)
button.place(x=200,y=200)
num1 = text.get("1.0",'end')

root.mainloop()
