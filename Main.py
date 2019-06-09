from PIL import ImageTk
import PIL.Image
from tkinter import *
def onClickMechanicalBOM():
    print("Mech BOM")

def onClickElectricalBOM():
    print ("Electrical BOM")

root = Tk()
root.title("LTRPM")
root.geometry("600x600")
companyName = Label(root, text="LARSEN & TOUBRO RUBBER PROCESSING MACHINERY", font=("TIMES NEW ROMAN", 15), fg="blue")
mechanicalBomButton = Button(root, text="MECHANICAL BOM", command=onClickMechanicalBOM)
mechanicalBomButton.place(x=100, y=300)
electricalBomButton = Button(root, text="ELECTRICAL BOM", command=onClickElectricalBOM)
electricalBomButton.place(x=375, y=300)
companyImage = ImageTk.PhotoImage(PIL.Image.open("LNTRT.jpg"))
companyLabel = Label(root, image=companyImage)
companyLabel.place(x=130,y=100)
companyName.pack()
root.mainloop()
