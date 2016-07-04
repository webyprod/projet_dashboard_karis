#!/usr/local/bin/python3.3

### surnom : Fox
### date : 29 Janvier 2016
### programme : prog_main_karis.py
### Objectif : programme principal qui utilisera les deux classes pour d'une part
###            se connecter a Semrush automatique et enregistrer le tableau de bord
###            puis enverra un message a ma boite mail pour me dire que j'ai recu
###            le tableau de bord.


import smrush as sem
import mail

def main():
  #  Instanciation classe Semrush
  karis = sem.Semrush()

  # Navigation vers page d'accueil Semrush puis clique sur Connexion
  karis.home_page()

  # Connexion Compte client  
  karis.connexion()

  # Retrouve le lien du site Karis Formation
  karis.tableauDeBord()

  # Impression d'ecran et enregistrement sur disque dur
  karis.impressionEcran()

  
  karis.close()


  #  Instanciation classe Message
  message = mail.Message()

  #  Connexion Serveur SMTP
  message.connexion()

  #  Envoi de message 
  message.envoi_message("Vous trouverez le rapport des positions de Karis Formation dans le dossier '/home/darius/karis.jpg' Merci")

  message.quit()



if __name__ == "__main__":
  main()
