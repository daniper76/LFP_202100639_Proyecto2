import tkinter as tk
from tkinter import filedialog

def funcion1():
    print("Se presionó analizar")

def funcion2():
    print("Se presionó errores")

def finalizar_aplicacion():
    ventana.destroy()

def limpiar_texto():
    text_area.delete('1.0', 'end')

def guardar():
    contenido = text_area.get("1.0", "end-1c")
    with open("Entrada.txt", "w") as archivo:
        archivo.write(contenido)

def guardar_texto():
    contenido = text_area.get('1.0', 'end')
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text files', '*.txt'), ('All files', '*.*')))
    if archivo is not None:
        archivo.write(contenido)
        archivo.close()

def seleccionar_archivo():
    archivo = filedialog.askopenfilename()
    if archivo:
        with open(archivo, 'r') as f:
            contenido = f.read()
            text_area.delete('1.0', 'end')
            text_area.insert('end', contenido)
ventana = tk.Tk()
ventana.configure(bg='black',cursor="pirate")
ventana.geometry('1000x1000')
ventana.title('Proyecto 2 LFP')

menu_principal = tk.Menu(ventana)

menu_opciones = tk.Menu(menu_principal, tearoff=0)
menu_opciones.add_command(label="Nuevo", command=limpiar_texto)
menu_opciones.add_command(label="Abrir", command=seleccionar_archivo)
menu_opciones.add_command(label="Guardar", command=guardar)
menu_opciones.add_command(label="Guardar Como", command=guardar_texto)
menu_opciones.add_command(label="Salir", command=finalizar_aplicacion)
menu_opciones.configure(bg='skyblue')

menu_principal.add_cascade(label="Archivo", menu=menu_opciones)

ventana.config(menu=menu_principal)

boton_analisis=tk.Button(ventana, text='Análisis', command=funcion1, height=3, width=11)
boton_analisis.configure(bg='skyblue')
boton_analisis.place(x=150,y=50)

boton_analisis=tk.Button(ventana, text='Tokens', command=funcion1, height=3, width=11)
boton_analisis.configure(bg='skyblue')
boton_analisis.place(x=250,y=50)

boton_analisis=tk.Button(ventana, text='Errores', command=funcion1, height=3, width=11)
boton_analisis.configure(bg='skyblue')
boton_analisis.place(x=350,y=50)


text_area = tk.Text(ventana,width=300,height=300)
text_area.place(x=250,y=130)

ventana.mainloop()