from tkinter import *

root = Tk()

valor = IntVar()


V1 = Radiobutton(root, text="Opção 1", variable=valor, value=1)
V2 = Radiobutton(root, text="Opção 2", variable=valor, value=2)
V3 = Radiobutton(root, text="Opção 3", variable=valor, value=3)
V4 = Radiobutton(root, text="Opção 4", variable=valor, value=4)
V5 = Radiobutton(root, text="Opção 5", variable=valor, value=5)
V6 = Radiobutton(root, text="Opção 6", variable=valor, value=6)
V7 = Radiobutton(root, text="Opção 7", variable=valor, value=7)
V8 = Radiobutton(root, text="Opção 8", variable=valor, value=8)
V9 = Radiobutton(root, text="Opção 9", variable=valor, value=9)
V10 = Radiobutton(root, text="Opção 10", variable=valor, value=10)
V1.pack()
V2.pack()
V3.pack()
V4.pack()
V5.pack()
V6.pack()
V7.pack()
V8.pack()
V9.pack()
V10.pack()

V3.select()

def ver_radio():
    print(valor.get())

cmd = Button(root, text="Executar", command=ver_radio)
cmd.pack()


root.mainloop()