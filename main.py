# MODULOS PARA BUSCAR ARCHIVO EN EL DISCO
import os
import tkinter as tk
from tkinter import filedialog

import recognition

class recognition_gui(tk.Tk):
    
    def __init__(self, title, width_gui, height_gui):
        self.recognition_gui = tk.Tk()

        # class recognition
        self.recognition = recognition.recognition()

        # Configurar tamaño y posicion de la recognition_gui
        # Obtener el tamaño de la pantalla
        width_screen = self.recognition_gui.winfo_screenwidth()
        height_screen = self.recognition_gui.winfo_screenheight()

        # Calcular la posición de la recognition_gui para que esté centrada
        x = int((width_screen/2) - (width_gui/2))
        y = int((height_screen/2) - (height_gui/2))

        self.recognition_gui.geometry(f'{width_gui}x{height_gui}+{x}+{y}')
        self.recognition_gui.resizable(False,False)
        self.recognition_gui.title(title)

        self.create_widgets()
        self.recognition_gui.mainloop()


    def create_widgets(self):
        self.b_buscar = tk.Button(self.recognition_gui, text="Buscar", command=self.find_file).place(x=25,y=40)

        self.file_path = tk.StringVar()
        l_direccion = tk.Label(text = "DIRECCION DEL ARCHIVO", font= ("Times New Roman",10)).place(x=100, y=20)
        e_path = tk.Entry(self.recognition_gui, textvariable = self.file_path, state="readonly", width = 40).place(x=100, y=44)

        self.b_graficar = tk.Button(self.recognition_gui, text="Graficar", command=self.graph).place(x=150,y=80)


    def find_file(self):
        # Obtener directorio de trabajo actual
        path_current = os.getcwd()
        # Se abre el explorador de archivos y se guarda la ruta
        path = filedialog.askopenfilename(initialdir = path_current, title = "Elige archivo:", filetypes = (("Ficheros de texto","*.txt"),("Todos los ficheros","*.*")))
        # Se le asigna la ruta al campo de texto
        self.file_path.set(path)

    
    def read_file(self,file_path):
     a = [] 
     with open(file_path) as file:
          line = file.readline()
          n = int(line)
     
          while line:
               line = file.readline()
               if line == '-1': break
               line = line.split(" ")
               list = []
         
               for i in range(0,n): list.append(int(line[i]))
               
               a.append(list)
        
          return [a,n]
     

    def search(self,a,n):
        for i in range(n):
            for j in range(n):
                if a[i][j] == 1:
                    self.recognition.analyze(a,i,j,n)

        self.recognition.show_graph()


    def graph(self):
        data = self.read_file(self.file_path.get())
        self.search(data[0],data[1])
        


title = "Reconocimiento de patrones"
width_recognition_gui = 370
height_recognition_gui = 120

vent = recognition_gui(title, width_recognition_gui, height_recognition_gui)
