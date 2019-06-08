from tkinter import *
top=Tk()
top.title("Lucifier V1.0")
top.geometry("600x600")
companyInfo=Label(top, text="LARSEN & TOUBRO RUBBER PROCESSING MACHINERY", font=("TIMES NEW ROMAN",15))
Label1 = Button(top, text= "CASTING BOM")
companyInfo.pack()
Label1.place(x=270,y=300)
top.mainloop()