# coding: utf-8


class Category:
    """ to be used when working on category, loading form API and inserting in DB
    """

    def __init__(self, categorie):
        """ to sanitize categories. will remove extra fr: or en: at the beginning of the name
        if exist.
        and handle  apostrophe
        """
        if categorie[2:3] == ':':
            self.name = categorie[3:].replace("'", "''")
            self.modified = 'yes'
        else:
            self.name = categorie[:].replace("'", "''")
            self.modified = 'no'

    def sql_insert(self):
        """ insert category in DB
        """
        return "INSERT into categorie VALUES(NULL,'" + self.name + "');"

    def sql_load(self):
        """ sql to load category
        """
        return "select * from categorie"


class Aliment:
    """ to be used when working on aliment, loading from API and inserting in DB
    """
    def __init__(self, produit_charge):
        """ to sanitize aliment. will remove apostrophe, set default value (unknown) when missing
        in the openFactfood site. aliment has 5 attributes that will be saved in db
        """
        if  produit_charge["product_name"] == '':
            self.product_name = 'product name missing'
        else:
            self.product_name = produit_charge["product_name"].replace("'", '-')
        if "nutrition_grades" in produit_charge:
            self.nutrition_grades = produit_charge["nutrition_grades"]
        else:
            self.nutrition_grades = "Unknown"
        self.url = produit_charge["url"]
        if "stores" in produit_charge:
            self.stores = produit_charge["stores"].replace("'", '-')
        else:
            self.stores = "Unknown"

    def sql_insert(self, category):
        """ sql to insert aliment with its 5 attributes + its category
        """
        return "INSERT into aliment VALUES(NULL,'" +  self.product_name + "','" +\
               self.nutrition_grades + "','" + self.stores + "','" + self.url +\
               "','" + str(category) + "');"
