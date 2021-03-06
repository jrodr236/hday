# -*- coding: utf-8 -*-


from dades import prova_dao, repte_dao, usuari_dao
from logica.entitats import ProvaJaSuperada
from presentacio.general import *
from presentacio.joc import *


def jugar(usuari):
    while True:
        usuari_dao.obtenir_punts(usuari)
        mostra_capcalera(usuari)
        reptes = repte_dao.obtenir_reptes_i_les_seves_proves(usuari)
        mostra_reptes(reptes)
        repte = escull_repte(reptes)

        if repte is None:
            continue
        elif repte == "s":
            return

        respondre_prova(usuari, repte)


def respondre_prova(usuari, repte):
    while True:
        usuari_dao.obtenir_punts(usuari)
        mostra_capcalera(usuari)
        # S'actualitzen les proves per si hi ha hagut alguna actualització, per exemple, si s'ha resolt alguna prova
        # en un altre execució concurrent del joc.
        prova_dao.obtenir_proves_de_repte(repte, usuari)
        prova_per_resoldre = repte.dona_primera_prova_sense_resoldre()
        mostra_proves_per_superar_d_un_repte(repte)
        codi = demana_codi_per_superar_prova(repte)

        if codi == "":
            break

        try:
            # Per disseny de la BBDD, no es permet que es resolgui una prova dues vegades. Si això hagués de passar,
            # es llançarà l'excepció ProvaJaSuperada i no es realitza la transacció.
            codi_correcte = prova_dao.verificar_codi(prova_per_resoldre, usuari, codi)

            if codi_correcte:
                prova_per_resoldre.superar()

            mostra_avis_codi_correcte(codi_correcte)
        except ProvaJaSuperada:
            mostra_avis_prova_ja_superada()
            return
