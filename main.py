import qrcode
import os
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as mb

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

def ImgToDec(path):
    with open(path, "rb") as image:
        b = bytearray(image.read())
        s=""
        for i in b:
          s+=str(i)+" ";
        s=s.strip()
        return s

def createHexCode(decCode):
    textArr16=[]
    sep = ""
    for i in decCode.split():
        textArr16.append('0' + str(hex(int(i)))[2:] if len(str(hex(int(i)))[2:]) == 1 else str(hex(int(i)))[2:])
    return sep.join(textArr16).replace("00","z")

def createPattern(imgPath):
    pattern=r'data:text/html,<img id="a"><script>document.getElementById("a").src="data:image/png;base64," + btoa(String.fromCharCode.apply(null, new Uint8Array("'+createHexCode(ImgToDec(imgPath))+'".replace(/z/g,"00").match(/.{1,2}/g).map(x=>parseInt(x,16)))));</script>'
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