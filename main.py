from tkinter import *
from tkinter import ttk
ventana= Tk()
ventana.geometry("700x700")
#el min size añade un tamaño mínimo y se autoexpande si lo necesitara
#ventana.minsize("500x500")
ventana.title("Master en Python--TKINTER")
ventana.resizable(0,0)

#Acceso a las variables internas de las funciones para poder borrarlas
home_label=Label(ventana,text="Inicio")
data_label=Label(ventana, text="Este programa fue engendrado no creado, la misma naturaleza que el Padre")
info_label=Label(ventana,text="Acerca de ...")
form_label=Label(ventana,text="Añade un objeto")

varLista= []
varNombre = StringVar()
varDescri = StringVar()
varPrecio = IntVar()

product_box=Frame(ventana,width=250)

#Label(product_box).grid(row=0)
products_table= ttk.Treeview(height=12,column=2)



def addObjeto() :
    objeto = {varNombre.get(),varDescri.get(),varPrecio.get()}
    
    ###Si varDescri fuera un textfield tendría que ser
    ###varDescri.get("1.0","end-1c")
    varLista.append(objeto)
    varNombre.set("")
    varDescri.set("")
    varPrecio.set("")
    ###Si varDescri fuera un textfield tendría que ser
    ###varDescri.delete("1.0",END)
    print(varLista)

    home()
       



add_frame = Frame(ventana)
nombre_label =Label(add_frame,text="Nombre de objeto")
nombre_entry=Entry(add_frame, textvariable=varNombre)
desc_label=Label(add_frame,text="Descripción")
desc_entry=Entry(add_frame, textvariable=varDescri)
precio_label = Label(add_frame,text="Precio")
precio_entry = Entry(add_frame, textvariable=varPrecio)
boton = Button(add_frame, text ="enviar",command=addObjeto )


#########################




#pantallas
def home() :
    ##Ocultar pantallas que no son home    
    data_label.grid_remove()
    info_label.grid_remove()
    form_label.grid_remove()
    add_frame.grid_remove()

    product_box.grid()

    products_table.grid(row=1, column=0,columnspan=2)
    products_table.heading("#0",text='Producto',anchor=W)
    products_table.heading("#1",text='Descripcion',anchor=W)

   

    """
    if len(varLista) !=0 :
        
        for e in varLista :

            if len(e) == 3:
                e.add("añadido")
                Label(product_box, text=e).grid()
    """              
    if len(varLista) !=0 :
        
        for e in varLista :

            if len(e) == 3:
                f = list(e)
                products_table.insert('',0,text= f[0],values=f[1])     
                e.add("añadido") 
                #e es un set e itera raro, habría que hacer un object o pasarlo a array





    home_label.config(
        bg="black",
        fg="white",
        font=("Arial",20),
      
    )
    home_label.grid(row=0,column=2)


def nuevoObjeto() :
    data_label.grid_remove()
    info_label.grid_remove()
    home_label.grid_remove()
    products_table.grid_remove()
     


    form_label.config(
        bg="black",
        fg="white",
        font=("Arial",20),
      
    )
    form_label.grid(row=0,column=2)
    product_box.grid_remove()

    #FORMULARIO
    add_frame.grid(row=1)
    nombre_label.grid(row=1,column=0)
    nombre_entry.grid(row=2,column=0)
    desc_label.grid(row=3,column=0)
    desc_entry.grid(row=4,column=0)
    precio_label.grid(row=5,column=0)
    precio_entry.grid(row=6,column=0)
    
    boton.grid(row=7,column=0)




   

def Info() :
    info_label.config(
        bg="black",
        fg="white",
        font=("Arial",20),
      
    )
    data_label.config(
        font=("Arial",10)
      
    )
    data_label.grid(row=1,column=2)
    info_label.grid(row=0,column=2)

    home_label.grid_remove()
    form_label.grid_remove()
    add_frame.grid_remove()
    product_box.grid_remove()
    products_table.grid_remove()




#Cargar pantalla inicio
home()


#menu superior
mi_menu = Menu(ventana)

#Cargar Menu
ventana.config(
    menu=mi_menu
)

#menu superior
mi_menu.add_cascade(label="Nuevo", command=nuevoObjeto)
mi_menu.add_command(label="Inicio",command = home)
mi_menu.add_command(label="Info", command=Info)
mi_menu.add_command(label="Salir",command= ventana.quit)

ventana.mainloop()