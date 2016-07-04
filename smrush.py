#!/usr/local/bin/python3.3

### surnom : Fox
### date : 29 Janvier 2016
### programme : smrush.py
### Objectif : Cette classe utilisera Selenium pour automatiser une connexion
###            sur Semrush, fera une impression d'ecran du tableau de bord de Karis
###            puis ferme l'application


from selenium import webdriver


class Semrush:
  def __init__(self):
    # Demarrage navigateur Firefox puis navigue vers 'https://fr.semrush.com'
    self.nav = webdriver.Firefox()
    self.nav.get("https://fr.semrush.com/")

  def home_page(self):
    # reperage du lien dont l'ancre est 'Se connecter' puis clique
    connexion = self.nav.find_element_by_link_text("Se connecter")
    connexion.click()

  def connexion(self):
    # Utilisation de mes identifiants pour la connexion
    email = self.nav.find_element_by_name('email')
    mdp = self.nav.find_element_by_name('password')
    validation = self.nav.find_element_by_class_name('s-btn__text')

    email.send_keys('********@******')
    mdp.send_keys('*************')

    validation.click()

  def tableauDeBord(self):
    # Trouver le lien dont l'ancre est "Karis Formation" puis clique
    karis = self.nav.find_element_by_link_text('Karis Formation')
    karis.click()

  def impressionEcran(self):
    # Prendre photo de l'ecran puis sauvegarde dans mon repertoire photo_karis 
    self.nav.save_screenshot('/home/darius/photo_karis/karis.jpg')

  def close(self):
    # quitte l'application
    self.nav.quit()
