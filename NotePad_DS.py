from tkinter import *
from tkinter import messagebox
import os
import tkinter.filedialog as fd

window = Tk()
window.geometry('800x500')
window.resizable(0, 0)
window.title("NotePad Diego Samayoa")
filename = None


def mostrarNombre():
    messagebox.showinfo('Compiladores II', 'Diego Alejandro Samayoa Gómez')


def abrirArchivo():
    documento = fd.askopenfilename(defaultextension='.txt', filetypes=[
        ('All Files', '*.*'), ("Text File", "*.txt*")])
    if documento != '':
        window.title(f"{os.path.basename(documento)}")
        text_field.delete(1.0, END)
        with open(documento, "r") as file_:
            text_field.insert(1.0, file_.read())
            file_.close()
    else:
        documento = None


def open_new_file():
    window.title("Untitled - Notepad")
    text_field.delete(1.0, END)


def guardarComoArchivo():
    nuevoArchivo = fd.asksaveasfilename(
        title="Guardar como",
        defaultextension=".txt",
        initialfile="SinTitulo.txt",
        filetypes=[("Text File", "*.txt*"),
                   ("Word Document", '*,docx*'),
                   ("HTML", "*.html*")])
    data = text_field.get("1.0", END)
    outfile = open(nuevoArchivo, "w")
    outfile.write(data)
    outfile.close()
    filename = nuevoArchivo
    window.title(f"{os.path.basename(data)}- NotepadDS")


# Menu supererior
menubar = Menu(window, background='#212121', foreground="white",
               activebackground='white', activeforeground='black')

archivo = Menu(menubar, tearoff=0, background='white', foreground='#212121')
# Botones dentro de "Archivo"
archivo.add_command(label="Nuevo", command=open_new_file)
archivo.add_command(label="Abrir", command=abrirArchivo)
archivo.add_command(label="Guardar como", command=guardarComoArchivo)
archivo.add_separator()
archivo.add_command(label="Diego Samayoa", command=mostrarNombre)
menubar.add_cascade(label="Archivo", menu=archivo)


# Barra de desplazamiento
scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT,
               fill=Y)


# Area de escritura de texto
bienvenidoMsg = """Editor Simple basado en NotePad++
Creado en Python por Diego Samayoa
Puede borrar este texto si lo desea"""

text_field = Text(window,
                  yscrollcommand=scrollbar.set)                  
text_field.pack(fill=BOTH)
text_field.insert('end', bienvenidoMsg)
scrollbar.config(command=text_field.yview)
window.config(menu=menubar)
window.mainloop()
