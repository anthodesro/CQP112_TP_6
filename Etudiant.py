# Anthony Desrochers, Julien Lemieux, Amélie Larcher, Maude Beauregard

import os, sys
from interface import Interface
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from colorama import Fore, Back, Style

student = []

clear = lambda: os.system('cls')

class Etudiant:
        def __init__(self):
            self.cip = 0
            self.nom = ""
            self.date = ""
            self.adresse = ""
            self.cours = Cours()

class Cours:
        def __init__(self):
            self.lst_cours = []

        def add_cours(self,add_cours):
            self.lst_cours.append(add_cours)

        def supp_cours(self,supp_cours):
            try:
                self.lst_cours.remove(supp_cours)
            except ValueError:
                pass

class Database:

    def __init__(self):
        self.lst_etudiant = []


    def save(self):
        print(Style.BRIGHT + Fore.LIGHTCYAN_EX + "Student DataBase Compilation \n" + Fore.RESET + Style.RESET_ALL) 
        for etudiant in self.lst_etudiant:
            with open(".\etudiants\%s.txt" % etudiant.cip, "w+") as fichier_etudiant:
                fichier_etudiant.write("CIP: " + str(etudiant.cip) + "\n")
                fichier_etudiant.write("Nom: " + str(etudiant.nom) + "\n")
                fichier_etudiant.write("Date: " + str(etudiant.date) + "\n")
                fichier_etudiant.write("Adresse: " + str(etudiant.adresse) + "\n")
                fichier_etudiant.write("Liste_de_cours: ")
                for cours in etudiant.cours.lst_cours:
                   fichier_etudiant.write(str(cours) + ",")          
            print("Étudiant #" + Fore.LIGHTMAGENTA_EX + etudiant.cip + Fore.RESET + " " + Back.GREEN + "sauvgarder" + Back.RESET)
        return
    
    def get_value(self, value = ""):
        self.value = self.value.split(None, 1)
        return self.value

    def get_cips(self):
        self.lst_cip = os.listdir(".\etudiants")
        for i, file_name in enumerate(self.lst_cip):
            self.lst_cip[i] = file_name[:-4] 
 
    def get_student(self):

        self.get_cips()
        for cip in self.lst_cip:

            with open(".\etudiants\%s.txt" % cip, "r") as fichier_student:
                etudiant = Etudiant()
                fichier_student.seek(0)
                data = fichier_student.readlines()
                for line in data:
                    line = line.split(" ",1)
                    if(len(line) == 1):
                        break
                    line[1] = line[1].rstrip("\n")

                    if line[0] == "CIP:":
                        etudiant.cip = line[1]
                    if line[0] == "Nom:":
                        etudiant.nom = line[1]
                    if line[0] == "Date:":
                        etudiant.date = line[1]
                    if line[0] == "Adresse:":
                        etudiant.adresse = line[1]
                    if line[0] == "Liste_de_cours:":
                        
                        line[1] = line[1].split(",")
                        for i, cours in enumerate(line[1]):
                            if(cours.strip() == ""):
                                line[1].remove(cours) 
                            else:
                                line[1][i] = cours.strip()
                        etudiant.cours.lst_cours = line[1]

            self.lst_etudiant.append(etudiant)

interface = Interface()
database = Database()
database.get_student()

while True:

    option1 = interface.ask("Choisir une option (Nouveau (n), MAJ (m) ou Quitter (q)) : ")
    clear()
    if option1 == "n":
        etudiant = Etudiant()
        
        while True:
            etudiant.cip = interface.ask_cip()
            if etudiant.cip in database.lst_cip:
                print("Le CIP existe déjà")
            else:
                break

        etudiant.nom = interface.ask_nom()
        etudiant.date = interface.ask_date()
        etudiant.adresse = interface.ask_adresse()

        database.lst_etudiant.append(etudiant)
        database.lst_cip.append(etudiant.cip)

        clear()

        pass

    if option1 == "m":
        while True:

            CIP = interface.ask("Entrer le CIP de l'étudiant :  ")

            for etudiant in database.lst_etudiant:
                if(etudiant.cip == CIP):
                    clear()
                    while True:
                        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "Mode édition du dossier étudiant de ==>>", Fore.MAGENTA + etudiant.cip + Fore.RESET + Back.RESET + Style.RESET_ALL)
                        option2 = interface.ask("Choisir une option (Ajouter (a), Retirer (r) ou Terminer (t)) : ")
                        clear()
                        if option2 == "a":
                            print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "Mode édition du dossier étudiant de ==>>", Fore.MAGENTA + etudiant.cip + Fore.RESET + Back.RESET + Style.RESET_ALL)
                            print(Fore.CYAN + "Cours aux quels", etudiant.cip, "l'étudiant est inscrit ==>>", Fore.RESET, etudiant.cours.lst_cours)
                            etudiant.cours.add_cours(interface.ask("Enter un cours à ajouter : "))
                            clear()
                            pass

                        if option2 == "r":
                            print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "Mode édition du dossier étudiant de ==>>", Fore.MAGENTA + etudiant.cip + Fore.RESET + Back.RESET + Style.RESET_ALL)
                            print(Fore.CYAN + "Cours aux quels", etudiant.cip, "l'étudiant est inscrit ==>>", Fore.RESET, etudiant.cours.lst_cours)
                            etudiant.cours.supp_cours(interface.ask("Enter un cours à retirer : "))
                            clear()
                            pass

                        if option2 == "t":
                            clear()
                            break
            break

    if option1 == "q":

        database.save()

        print("\nPress Enter to leave ...")
        input()

        break