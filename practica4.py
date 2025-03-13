from tkinter import *

def open_file():
    pass  # Marcador de posición para la funcionalidad de apertura
#esta funcion solo sirve para abrir el archivo, pero no se utiliza en este programa

def save_file():
    pass  # Marcador de posición para la funcionalidad de guardar
#esta funcion solo sirve para guardar el archivo, pero no se utiliza en este programa
def delete_text():
    text_area.delete(1.0, END)  # borrar el texto del area de texto
#esta funcion solo sirve para borrar el texto del area de texto, pero no se utiliza en este programa
def change_color():
    pass  # Marcador de posición para la funcionalidad de cambiar el color de fondo
#esta funcion solo sirve para cambiar el color del texto, pero no se utiliza en este programa
def search_and_replace():
    pass  #Marcador de posición para  la funcionalidad de buscar y reemplazar
#esta funcion solo sirve para buscar y reemplazar texto, pero no se utiliza en este programa

#Aqui esta el cuerpo base de la ventana principal
ventana_principal = Tk()
ventana_principal.title("Ventana principal")
ventana_principal.minsize(width=400, height=300)
ventana_principal.config(padx=35, pady=35)

# se crear el area de texto
text_area = Text(ventana_principal, wrap='word', width=50, height=15)
text_area.pack()

# aqui se crear la barra de menu 
menu_bar = Menu(ventana_principal)

# aqui añades las opciones del menu y archivos (open,save,delete,file)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_command(label="Delete", command=delete_text, accelerator="Ctrl+D")
menu_bar.add_cascade(label="File", menu=file_menu)

# Aqui se añade el boton  cambio de color de texto 
color_button = Button(ventana_principal, text="cambio de color de texto", command=change_color)
color_button.pack()

# se agregar el boton de buscar y reemplazar texto
search_button = Button(ventana_principal, text="buscar y remplazar texto", command=search_and_replace)
search_button.pack()
# aqui se muestra la ventana principal
ventana_principal.config(menu=menu_bar)

# Vincular atajos de teclado
ventana_principal.bind('<Control-o>', lambda event: open_file())
ventana_principal.bind('<Control-s>', lambda event: save_file())
ventana_principal.bind('<Control-d>', lambda event: delete_text())
#aqui es el bucle para mantener abierto la ventana principal
ventana_principal.mainloop()
