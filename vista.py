from tkinter import StringVar
from tkinter import IntVar
from tkinter import Frame
from tkinter import Entry
from tkinter import Label
from tkinter import Button
from tkinter import Radiobutton
from modelo import Abmc
from tkinter import ttk
from tktemas import temas


class Ventanita:
    def __init__(self, window):
        self.root = window
        self.ali = StringVar()
        self.nom = StringVar()
        self.ape = StringVar()
        self.tel = IntVar()
        self.ema = StringVar()
        self.a = IntVar()
        self.opcion = StringVar()
        self.f = Frame(self.root)
        self.tree = ttk.Treeview(self.f)
        self.objeto_base = Abmc()
        # Frame
        self.root.title("AGENDA VIRTUAL")
        self.root.configure(bg="#DED4B9")
        self.f.config(width=1020, height=1020)
        self.f.grid(row=11, column=0, columnspan=4)

        # Etiquetas
        self.superior = Label(
            self.root, text="INGRESE SUS DATOS",bg="#F5ECBF", fg="black", width=40
        )
        self.alias = Label(self.root, text="Alias" ,width=20, bg="#F5E1BF", fg="black")
        self.nombre = Label(self.root, text="Nombre" ,width=20, bg="#F5E1BF", fg="black")
        self.apellido = Label(self.root, text="Apellido" ,width=20, bg="#F5E1BF", fg="black")
        self.telefono = Label(self.root, text="Telefono" ,width=20, bg="#F5E1BF", fg="black")
        self.email = Label(self.root, text="Email" ,width=20, bg="#F5E1BF", fg="black")
        self.registros = Label(
            self.root, text="MOSTRAR REGISTROS EXIXTENTES", bg="#F5ECBF", width=40
        )
        self.temas = Label(
            self.root,
            text="TEMAS",
            bg="#F5ECBF",
            fg="black",
            height=1,
            width=40,
        )

        self.superior.grid(
            row=0, column=0, columnspan=4, padx=1, pady=1, sticky="w" + "e"
        )
        self.alias.grid(row=1, column=0, sticky="w")
        self.nombre.grid(row=2, column=0, sticky="w")
        self.apellido.grid(row=3, column=0, sticky="w")
        self.telefono.grid(row=4, column=0, sticky="w")
        self.email.grid(row=5, column=0, sticky="w")
        self.registros.grid(
            row=6, column=0, columnspan=4, padx=1, pady=1, sticky="w" + "e"
        )
        self.temas.grid(
            column=0, row=20, columnspan=4, padx=1, pady=1, sticky="w" + "e"
        )

        # Entradas
        self.Ent1 = Entry(self.root, textvariable=self.ali, width=30)
        self.Ent1.grid(row=1, column=1)
        self.Ent2 = Entry(self.root, textvariable=self.nom, width=30)
        self.Ent2.grid(row=2, column=1)
        self.Ent3 = Entry(self.root, textvariable=self.ape, width=30)
        self.Ent3.grid(row=3, column=1)
        self.Ent4 = Entry(self.root, textvariable=self.tel, width=30)
        self.Ent4.grid(row=4, column=1)
        self.Ent5 = Entry(self.root, textvariable=self.ema, width=30)
        self.Ent5.grid(row=5, column=1)

        # Frame Unidad 4
        self.frame_rojoizq = Frame(self.root, bg="#F5ECBF")
        self.frame_negro = Frame(self.root, bg="#F5ECBF")
        self.frame_rojoder = Frame(self.root, bg="#F5ECBF")

        self.frame_rojoizq.grid(column=0, row=21)
        self.frame_negro.grid(column=1, row=21)
        self.frame_rojoder.grid(column=2, row=21)

        # Botones
        self.boton_alta = Button(self.root, text="Alta", command=lambda: self.alta(), bg="#DED4B9", width=20)
        self.boton_alta.grid(row=7, column=0)

        self.boton_editar = Button(
            self.root, text="Actualizar", command=lambda: self.modificar(), bg="#DED4B9", fg="black", width=20)
        self.boton_editar.grid(row=7, column=1)

        self.boton_borrar = Button(
            self.root, text="Borrar", command=lambda: self.borrar(), bg="#DED4B9", fg="black", width=20)
        self.boton_borrar.grid(row=7, column=2)
        
        self.boton_tema1 = Radiobutton(
            self.frame_negro,
            text="Tema 1",
            variable=self.opcion,
            value="01",
            fg="black",
            bg="#DED4B9",
            command=lambda: temas.tema1(self, self.root),
        )
        self.boton_tema1.grid(column=30, row=20,)

        self.boton_tema2 = Radiobutton(
            self.frame_negro,
            text="Tema 2",
            variable=self.opcion,
            value="02",
            fg="black",
            bg="#DED4B9",
            command=lambda: temas.tema2(self, self.root),
        )
        self.boton_tema2.grid(column=31, row=20)

        self.boton_tema3 = Radiobutton(
            self.frame_negro,
            text="Tema 3",
            variable=self.opcion,
            value="03",
            fg="black",
            bg="#DED4B9",
            command=lambda: temas.tema3(self, self.root),
        )
        self.boton_tema3.grid(column=32, row=20,)


        # Tree
        self.tree["columns"] = ("col1", "col2" , "col3" ,"col4" ,"col5")
        self.tree.column("#0", width=90, minwidth=50, anchor="w")
        self.tree.column("col1", width=200, minwidth=80)
        self.tree.column("col2", width=200, minwidth=80)
        self.tree.column("col3", width=200, minwidth=80)
        self.tree.column("col4", width=200, minwidth=80)
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Alias")
        self.tree.heading("col2", text="Nombre")
        self.tree.heading("col3", text="Apellido")
        self.tree.heading("col4", text="Telefono")
        self.tree.heading("col5", text="Email")
        self.tree.grid(row=10, column=0, columnspan=4)

    def alta(
        self,
    ):
        self.objeto_base.alta(self.ali, self.nom, self.ape, self.tel, self.ema, self.tree)

    def borrar(
        self,
    ):
        self.objeto_base.baja(self.tree)

    def modificar(
        self,
    ):
        self.objeto_base.modificar(self.ali, self.nom, self.ape, self.tel, self.ema, self.tree)
    
    def actualizar(
        self,
    ):
        self.objeto_base.actualizar_treeview(self.tree)
