# -*- coding: utf-8 -*-

"""
Funcions de la capa de presentació relacionades amb la gestió dels usuaris.
"""

from getpass import getpass

import logica.entitats
from dades import usuari_dao
from . import administracio
from .general import demanar_intro


def existeix_usuari():
    """
    Pregunta si l'usuari ja existeix o se n'ha de crear un de nou.
    :return:
    """
    te_usuari = input("Tens usuari? (S/N): ").lower()
    print()
    if te_usuari not in ["s", "n"]:
        print("Opció incorrecta.")
        demanar_intro()
        return None
    else:
        return te_usuari == "s"


def demanar_registre(tipus_usuari):
    """
    Demana les dades per registrar un nou usuari
    :return: nom i contrasenya per crear un nou usuari
    """
    print("Si us plau, introdueix les credencials per al nou usuari.")
    print()
    # No es permet registrar un nou usuari administrador
    nom = input("Nom: ")
    contrasenya = getpass("Contrasenya: ")
    contrasenya2 = getpass("Contrasenya (un altre cop): ")
    tipus_usuari.remove(logica.constants.ADMIN)
    tipus_usuari.remove(logica.constants.TOTHOM)
    tipus = input("Tipus d'usuari " + administracio.formatar_llista(tipus_usuari) + ": ").lower()
    print()
    if contrasenya != contrasenya2:
        print("Les dues contrasenyes no coincideixen.")
        demanar_intro()
        return None, None, None
    elif tipus == logica.constants.ADMIN:
        print("No es permet registrar administradors.")
        return None, None, None
    elif tipus == logica.constants.TOTHOM:
        print("Tipus d'usuari incorrecte.")
        return None, None, None
    return nom, contrasenya, tipus


def demanar_login():
    """
    Demana les dades d'un usuari per fer login
    :return: el nom i la contrasenya indicades
    """
    print("Si us plau, introdueix les teves credencials.")
    print()
    nom = input("Nom: ")
    contrasenya = getpass("Contrasenya: ")
    print()
    return nom, contrasenya


def mostrar_error_verificar_usuari():
    """
    Mostra un error que indica que l'usuari no s'ha pogut verificar correctament.
    :return:
    """
    print("Usuari incorrecte.")
    print()