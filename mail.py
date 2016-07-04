#!/usr/local/bin/python3.3

### surnom : Fox
### date : 29 Janvier 2016
### programme : mail.py
### Objectif : Cette classe utilisera le module smtplib pour l'envoi du mail

import smtplib


class Message:
  def __init__(self):
    # Preparation connexion Google Mail
    self.messagerie = smtplib.SMTP('smtp.gmail.com:587')
    self.messagerie.starttls()
    self.expediteur = "mk.alex1989@gmail.com"
    self.destinataire = "a.mokadem@forma-dis.com"

  def connexion(self):
    # Connexion avec mes identifiants mail + mdp
    self.messagerie.login('mk.alex1989@gmail.com','************')

  def envoi_message(self, mess=""):
    # Envoi du mail
    self.messagerie.sendmail(self.expediteur, self.destinataire, mess)

  def quit(self):
    # Fermeture de l'application
    self.messagerie.quit()
