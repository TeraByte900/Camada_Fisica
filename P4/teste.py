from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from aplicacaoTx import *

def filename():
    root.fileName=filedialog.askopenfilename(filetypes=(("JPg",".png"),))
    x=root.fileName
    send(x)
    exit()
print(serialName)
root=Tk()
root.geometry("200x200")
btn1=ttk.Button(root,text="escolha a imagem")
btn1.pack()
btn1.config(command=filename)
mainloop()
