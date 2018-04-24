# coding: utf-8


class user_input:
    """ to be used when working on aliment, loading from API and inserting in DB
    """
    def __init__(self, choice):
        self.choice = choice


    @classmethod
    def from_input(cls):
        return cls(input('saisir le chiffre de la categorie: '))


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



#def check_from_db(request_from_db,user_input):
#    for element in request_from_db:
#        if int(user_input) in element:
#            check = True
#            break
#        else:
 #           check= False
  #  return check

