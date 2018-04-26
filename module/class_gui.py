# coding: utf-8


class user_input:
    """ to be used when working on aliment, loading from API and inserting in DB
    """
    def __init__(self, choice):
        self.choice = choice


    @classmethod
    def from_input(cls,table):
        return cls(input('saisir le chiffre ' + str(table) + ' : '))

    @classmethod
    def from_input_save(cls):
        return cls(input('Voulez vous sauver votre recherche Y or N ?'))


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
            prompt = 'Rien a dire ceci est un bon aliment. On ne va pas trouver mieux'
        elif self.nutrition == 'b':
            prompt = 'Pas mal mais essayons de trouver mieux. Trouvons qqchose a la place'
        elif self.nutrition == 'c':
            prompt = 'On peut vraiment trouver mieux. Trouvons qqchose a la place'
        elif self.nutrition == 'd':
            prompt = 'Vous ne devriez pas manger d\'aliment dans cette categorie. Trouvons qqchose a la place'
        elif self.nutrition == 'e':
            prompt = 'attention a votre sante ! Trouvons qqchose a la place'
        else:
            prompt = 'Pas d\'info disponible ! Trouvons qqchose a la place'
        return prompt



    def substitution_aliment(self, list_aliment):
        for x in list_aliment:
#            if str(x[2]) < self.nutrition and str(x[2]) == "a":
            if str(x[2]) < self.nutrition and str(x[2]) != "Unkmown":
                substitution_result_list = [1,x[0],x[1],x[2],x[3],x[4],x[5]]
                break
            else:
                substitution_result_list = [0,'rien trouve','rien trouve','rien trouve','rien trouve',0]
        return substitution_result_list

    def sql_insert_substitution(self, new_aliment):
        """ sql to insert aliment with its 5 attributes + its category
        """
        return "INSERT into substitution VALUES(NULL," +  str(self.id) + ',' + \
               str(new_aliment[1]) + ",NOW());"
