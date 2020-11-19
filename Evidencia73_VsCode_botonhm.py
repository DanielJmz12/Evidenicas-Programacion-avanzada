import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("prueba")
        self.boton1=tk.Button(self.ventana1, text="varon", command=self.presionvaron)
        self.boton1.grid(column=0, row=0)
        self.boton2=tk.Button(self.ventana1, text="mujer",command=self.presionmujer)
        self.boton2.grid(column=4, row=2)
        self.ventana1.mainloop()

    def presionvaron(self):
        self.ventana1.title("varon")
    def presionmujer(self):
        self.ventana1.title("mujer")
aplicacion1=Aplicacion()