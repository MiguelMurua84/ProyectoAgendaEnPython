import sqlite3
from peewee import *
from tkinter import Tk
import socket


# Patrón observador

from observador import Sujeto
from observador import ConcretoObserverA

# Decoradores

from decoradores import ingreso_de_nuevo_registro
from decoradores import actualizacion_de_registro
from decoradores import eliminacion_de_registro


db = SqliteDatabase("mi_base.db")

class BaseModel(Model):
    class Meta:
        database = db

class Agenda(BaseModel):
    id = IntegerField()
    alias = CharField(unique=True)
    nombre = CharField()
    apellido = CharField()
    telefono = IntegerField()
    email= CharField()

db.connect()
db.create_tables([Agenda])


class Abmc(Sujeto):
    def __init__(
        self,
    ): pass
    
    
     # Función ALTA - Con Decorador
    @ingreso_de_nuevo_registro
    def alta(self, alias, nombre, apellido, telefono, email, mitreeview):
        agenda=Agenda()
        agenda.alias=alias.get()
        agenda.nombre=nombre.get()
        agenda.apellido=apellido.get()
        agenda.telefono=telefono.get()
        agenda.email=email.get()
        agenda.save()
        self.alias = alias.get()
        self.nombre = nombre.get()
        self.apellido = apellido.get()
        self.telefono = telefono.get()
        self.email = email.get()
        
        """Puedo llamar a notificar"""
        
        self.notificar(alias.get(), nombre.get(), apellido.get(), telefono.get(), email.get())
    
        self.actualizar_treeview(mitreeview)


        
    # Función ACTUALIZAR - Con decorador
    @actualizacion_de_registro
    def actualizar_treeview(self, mitreeview):
        # limpieza de tabla
        records = mitreeview.get_children()
        for element in records:
            mitreeview.delete(element)
        # Consiguiendo datos
        for fila in Agenda.select():
            mitreeview.insert("", 0, text=fila.id, values=(fila.alias, fila.nombre, fila.apellido, fila.telefono, fila.email))
        
    
    
    # Función BORRAR - Con decorador
    @eliminacion_de_registro
    def baja(self, mitreeview):
        item_seleccionado = mitreeview.focus()
        valor_id = mitreeview.item(item_seleccionado)
        borrar=Agenda.get(Agenda.id==valor_id["text"])
        borrar.delete_instance()
        self.actualizar_treeview(mitreeview)

    def modificar(self, alias, nombre, apellido, telefono, email,  mitreeview):
        item_seleccionado = mitreeview.focus()
        valor_id = mitreeview.item(item_seleccionado)
        actualizar=Agenda.update(alias=alias.get(), nombre=nombre.get(), apellido=apellido.get(), telefono=telefono.get(), email=email.get()).where(Agenda.id==valor_id["text"])
        actualizar.execute()
        self.actualizar_treeview(mitreeview)
