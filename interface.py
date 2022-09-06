import re

class Interface:
    question = ""
    value = ""

    def __init__(self):
        self.question = ""       
        self.value = ""
        self.cip = ""       

    def ask(self, question):
        while True:
            self.value = str(input(question))
            return self.value

    def ask_cip(self):
        while True:
            lettre = False
            nombre = False
            self.cip = input("Enter un CIP : ")
            try:
                lst_cip = [self.cip[index : index + 4] for index in range(0, len(self.cip), 4)]
                for element in lst_cip[0:1]:
                    if element.isalpha():
                        lettre = True
                        continue   

                for element in lst_cip[1:2]:
                    if element.isnumeric():
                        nombre = True
                if (lettre == True and nombre == True):
                    break
                    
            except ValueError:
                continue

        return self.cip
    
    def ask_nom(self):
        while True:
            lettre = False
            mot = False
            self.nom = input("Enter un nom : ")
            try:
                lst_nom = self.nom.split()
                for element in lst_nom:
                    if element.isalpha():
                        lettre = True
                        continue
                if len(lst_nom) >= 2:
                    mot = True

                if (lettre == True and mot == True):
                    break
                                        
            except ValueError:
                continue

        return self.nom
            
    def ask_date(self):
        while True:
            pattern = False
            jour = False
            mois = False
            annee = False
            self.date = input("Enter une date de naissance (année-mois-jour): ")
            try:
                lst_date = self.date.split("-")

                if len(lst_date) == 3:
                    pattern = True
                    
                for element in lst_date[0:1]:
                    nb = float(element) 
                    if 1900 <= nb <= 2019:
                        annee = True
                
                for element in lst_date[1:2]:
                    nb = float(element)
                    if 1 <= nb <= 12:
                        mois = True

                for element in lst_date[2:3]:
                    nb = float(element)
                    if 1 <= nb <= 31:
                        jour = True

                if (pattern == True and annee == True and mois == True and jour == True):
                    break
                       
            except ValueError:
                continue


        return self.date
    
    def ask_adresse(self):
        while True:
            self.value = str(input("Enter une adresse : "))
            return self.value

    def get_value(self):
        return self.value
    
