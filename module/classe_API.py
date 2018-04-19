# coding: utf-8

import json


class category:

    def __init__(self, categorie):

        if categorie[2:3] == ':':
            self.name = categorie[3:].replace("'", "''")
            self.modified = 'yes'
        else:
            self.name = categorie[:].replace("'", "''")
            self.modified = 'no'

    def SQL_insert(self):

        return "INSERT into categorie VALUES(NULL,'" + self.name + "');"


    def SQL_load(self):

        return "select * from categorie"


class Aliment:

    def __init__(self, produit_charge):
        if  produit_charge["product_name"] == '':
            self.product_name = 'product name missing'
        else:
            self.product_name = produit_charge["product_name"].replace("'",'-')
        if "nutrition_grades" in produit_charge:
            self.nutrition_grades = produit_charge["nutrition_grades"]
        else:
            self.nutrition_grades = "Unkmown"
        #self.nutrition_grades_tags = produit_charge.get(["nutrition_grades"],"Unknown")
        self.url = produit_charge["url"]
        if "stores" in produit_charge:
            self.stores = produit_charge["stores"].replace("'",'-')
        else:
            self.stores = "Unknown"

    def SQL_insert(self, categorie):

        return "INSERT into aliment VALUES(NULL,'" +  self.product_name + "','" + self.nutrition_grades + "','"\
               + self.stores + "','" + self.url + "','" + str(categorie) + "');"
#+ "'

    def ExploseCategorie(self):
        i = 0
        IdCategorie0, IdCategorie1, IdCategorie2 = '','',''
        while i < 3:
            IdCategorie0 = self.categories_tags[0].split(':')
            IdCategorie1 = self.categories_tags[1].split(':')
            IdCategorie2 = self.categories_tags[2].split(':')
            i += 1
        return (IdCategorie0,IdCategorie1,IdCategorie2)

#### autre solution pour prendre le max de groupo et non pas  que 3
    def ExploseCategorie2(self,*cate):
        group = []#list qu on va remplir de group

        for x in cate:
            numberOfTags = len(x)
            group.append(x)
           # for y in x:
           #     kk = y.split(':')##on enleve le en:
            #    group.append(kk[1])##et on prend que la deuxieme partie le groupe et non pas en:

        return numberOfTags, group

    #def csv_write(self,file, groupcategory):#utilisation de format !! a verifier
     #   opfile = open(file, 'a')
      #  opfile.write(self.product_name + ',' + self.nutrition_grades + ',' + self.url + ',' + \
       # self.stores + ',' + groupcategory[0] + ',' + groupcategory[1]+ '\n')
        #opfile.close()

    def csv_write(self, file, groupcategory):  # utilisation de format !! a verifier
        opfile = open(file, 'a')
        opfile.write("{0},{1},{2},{3}".format(self.product_name,self.nutrition_grades,self.url,\
        self.stores))
        for grp in groupcategory:
            opfile.write(',' + str(grp))

        opfile.write('\n')
        opfile.close()