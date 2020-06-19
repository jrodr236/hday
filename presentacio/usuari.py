# -*- coding: utf-8 -*-

from getpass import getpass

from logica import constants
from . import administracio
from .general import demanar_intro


def existeix_usuari():
    te_usuari = input("Tens usuari? (S/N): ").lower()
    print()
    if te_usuari not in ["s", "n"]:
        print("Opció incorrecta.")
        demanar_intro()
        return None
    else:
        return te_usuari == "s"


def demanar_registre_de_nou_usuari(tipus_usuari):
    print("Si us plau, introdueix les credencials per al nou usuari.")
    print()
    # No es permet registrar un nou usuari administrador
    nom = input("Nom: ")
    contrasenya = getpass("Contrasenya: ")
    contrasenya2 = getpass("Contrasenya (un altre cop): ")
    tipus_usuari.remove(constants.TOTHOM)
    tipus = input("Tipus d'usuari " + administracio.formatar_llista(tipus_usuari) + ": ").lower()
    print()
    if contrasenya != contrasenya2:
        print("Les dues contrasenyes no coincideixen.")
        demanar_intro()
        return None, None, None
    elif tipus == constants.TOTHOM:
        print("Tipus d'usuari incorrecte.")
        return None, None, None
    return nom, contrasenya, tipus


def demanar_login():
    print("Si us plau, introdueix les teves credencials.")
    print()
    nom = input("Nom: ")
    contrasenya = getpass("Contrasenya: ")
    print()
    return nom, contrasenya


def mostrar_error_verificar_usuari():
    print("Usuari incorrecte.")
    print()