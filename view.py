
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from bd import connect, cursor


root = Tk()
root.title('Gestor de Clientes')
root.geometry("650x300")

def mostrar():
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    tree.delete(*tree.get_children())

    for cliente in clientes:        
        tree.insert('',END, cliente[0] , values = (cliente[1], cliente[2], cliente[3]))
    

def crear():
    def guardar():
        nombre = e_nombre.get()
        telefono = e_telefono.get()
        empresa = e_empresa.get()
        
        if nombre and telefono and empresa:
            cursor.execute("INSERT INTO clientes(nombre, telefono, empresa) VALUES (%s, %s, %s)", (nombre, telefono, empresa))
            connect.commit()
            nueva_ventana.destroy()
            
        else:
            messagebox.showerror(message='Llene todos los campos', title='Datos vacios')
        mostrar()

    nueva_ventana = Toplevel(root)
    nueva_ventana.title('Registro Cliente')
    nueva_ventana.geometry('300x100')

    l_nombre = Label(nueva_ventana, text='Nombre')
    l_nombre.grid(column = 0, row = 0)

    e_nombre = Entry(nueva_ventana, width=39 )
    e_nombre.grid(column = 1, row = 0)
    

    l_telefono = Label(nueva_ventana, text = 'Telefono')
    l_telefono.grid(column = 0, row = 1)

    e_telefono = Entry(nueva_ventana, width = 39)
    e_telefono.grid(column = 1, row = 1)


    l_empresa = Label(nueva_ventana, text = 'Empresa')
    l_empresa.grid(column = 0, row = 2)

    e_empresa = Entry(nueva_ventana, width = 39)
    e_empresa.grid(column = 1, row = 2)

    btn_guardar = Button(nueva_ventana, text='Guardar', command=guardar)
    btn_guardar.grid(column = 1, row = 3)





def eliminar():
    item = tree.selection()

    if item:
        borrar = messagebox.askokcancel(message="¿Desea Eliminar el registro?", title='Borrar Cliente')
        if borrar:
            for i in item:
                cursor.execute("DELETE FROM clientes WHERE id=%s", (i, ))
                connect.commit()
            mostrar()
    else:
        label = Label(root, text="Seleccione el cliente que desea eliminar", fg="#f00")
        label.grid(column=0, row=3, columnspan=3)


btn_crear = Button(root, text='Agregar Cliente', command=crear)
btn_crear.grid(column=0, row=0)

btn_eliminar = Button(root, text='Eliminar Cliente', command=eliminar)
btn_eliminar.grid(column=2, row=0)

tree = ttk.Treeview(root)

tree['columns'] = ('Nombre', 'Telefono', 'Empresa')

tree.column('#0', width = 0, stretch = NO) #para desaparecer esta columna ya que no se utilizara
tree.column('Nombre')
tree.column('Telefono')
tree.column('Empresa')

tree.heading('#0')
tree.heading('Nombre', text = 'Nombre')
tree.heading('Telefono', text = 'Telefono')
tree.heading('Empresa', text='Empresa')

tree.grid(column=0, row=2, columnspan = 4)


mostrar()


root.mainloop()