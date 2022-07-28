import qrcode
import os
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as mb
import base64



formWidth=170
formHeight=90
root=Tk()
root.title("p")
root.geometry(str(formWidth)+"x"+str(formHeight))
labelImg=Label(root,text="image")
labelImg.place(x=0,y=8)

labelSize=Label(root,text="size(max 2331):")
labelSize.place(x=0,y=28)

inputImg=Entry(root)
inputImg.place(x=40,y=8)
inputImg.bind("<Double-Button-1>",lambda event:getImgWay())

def printFileSize():
    labelSize.config(text="size(max 2331): {size}".format(size=str(len(createPattern(inputImg.get())))if os.path.exists(inputImg.get()) else "file not exist"))

def getImgWay():
    way = filedialog.askopenfilename()
    inputImg.delete(0,"e")
    inputImg.insert(0,way)
    printFileSize()

def createBase64(path):
    with open(path, "rb") as image:
        b = base64.b64encode(image.read())
    return b


def createPattern(imgPath):
    pattern=r'data:text/html,<img id="a" src="data:image/png;base64,'+str(createBase64(imgPath))[2:-1]+"\">"
    return pattern

def createQRCode(text,saveWay):
    img = qrcode.make(text)
    img.save(saveWay+".png" if ".png" not in saveWay else saveWay, "PNG")

def workPreparation():
    prevImgWay=str(inputImg.get())
    if os.path.exists(prevImgWay):
        if(len(createPattern(inputImg.get())) >2331):
            mb.showerror("Ошибка", "file is too big")
            return
        saveWay=filedialog.asksaveasfilename()
        createQRCode(createPattern(prevImgWay),saveWay)

buttonResult = Button(root,text="QRCODE",width=10,command=workPreparation)
buttonResult.place(x=45,y=55)
root.mainloop()