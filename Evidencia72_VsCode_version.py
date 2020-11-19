import tkinter as tk
import sys

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("version sistema")
        self.label1=tk.Label(self.ventana1, text="sisema de ventas")
        self.label1.grid(column=0, row=0)
        self.label2=tk.Label(self.ventana1, text="2020")
        self.label2.grid(column=0, row=1)
        self.boton1=tk.Button(self.ventana1, text="salir", command=self.salir)
        self.boton1.grid(column=0, row=2)
        self.ventana1.resizable(False, False)

        self.ventana1.mainloop()

    def salir(self):
        sys.exit(0)

aplicacion1=Aplicacion()