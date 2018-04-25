# coding: utf-8


class user_input:
    """ to be used when working on aliment, loading from API and inserting in DB
    """
    def __init__(self, choice):
        self.choice = choice


    @classmethod
    def from_input(cls,table):
        return cls(input('saisir le chiffre ' + str(table) + ' : '))


    def check_from_db(self,request_from_db):
        for element in request_from_db:
            if int(self.choice) in element:
                check = True
                break
            else:
                check = False
        return check

    def check_int(self):
        checkII = True
        try:
            self.choice = int(self.choice)
        except ValueError:
            checkII = False
        return checkII



class aliment_gui:
    """ to be used when working on aliment, loading from API and inserting in DB
    """
    def __init__(self, aliment):
        self.id = aliment[0][0]
        self.name = aliment[0][1]
        self.nutrition = aliment[0][2]
        self.store = aliment[0][3]
        self.url = aliment[0][4]
        self.category = aliment[0][5]
       # self.comment =


    def substitution_prompt(self):
        if self.nutrition == 'a':
            prompt = 'Rien a dire ceci est un bon aliment'
        elif self.nutrition == 'b':
            prompt = 'Pas mal mais essayons de trouver mieux'
        else:
            prompt = 'attention a votre sante ! Achetez ceci a la place'

        return prompt


    #def substitution(self):
     #   if self.nutrition


