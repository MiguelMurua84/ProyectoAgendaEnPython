import sqlite3
from tkinter import ttk
import re


class Agenda:
    def __init__(
        self,
    ):
        pass

    def regex_ali(alias):
        cadena = alias
        patron = "^[A-Za-z]+(?:[ _-][A-Za-z]+)*$"
        if re.match(patron, cadena):
            print(alias)
        else:
            print("alias Invalido")



