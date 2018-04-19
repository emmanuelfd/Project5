# coding: utf-8

import requests
import json
import classe_API
import classe_db
from module.classe_API import category, Aliment
from module.classe_db import DataBaseConnection
import pymysql
import pymysql.cursors



page = True


separator = 20 # page 1 to start


r = requests.get('https://fr.openfoodfacts.org/categories.json')

return_json_API = r.json()#get json file
number_produit = return_json_API["count"]#a supprimer




product_JSON = return_json_API["tags"]#get the list of product itself from JSON
print(type(product_JSON))##a supprimer
#print(product_JSON[0])

list_cate_500 = []##a supprimer

for category in product_JSON:


    product_dico = dict(category)

    if product_dico["products"] < 30 and product_dico["products"] > 20:
         #list_cate_500.append(product_dico["name"] + ' - ' + product_dico["id"])
         list_cate_500.append(product_dico["name"])
    else:
         print('skip ' + product_dico["name"] + ' car ' + str(product_dico["products"]))


print(list_cate_500)##a supprimer
print(len(list_cate_500))##a supprimer

print('######################')
### Connect to the database




connection = DataBaseConnection()

########



##insertion des categorie en DB###
for cat in list_cate_500:
    #print(cat[0:2])
    print('==============')
    categorie = classe_API.category(cat)
    print(categorie.name)

    #if categorie.lc == 'fr':


    #sql_insert = "INSERT into categorie VALUES(NULL,'" + categorie.name + "');"
    #print(categorie.SQL_insert() + ' je regarde si ca marche')


    connection.query_insert(categorie.SQL_insert())
    #cur.execute(sql_insert)





##################################################
##recuperation des categories + id (id sont inconnus########
##################################################

results = connection.fetchalll(categorie.SQL_load())

print('1111111111111111111111111111111111111111111')
print(results) # => les categories from DB en liste de tulpe
print('1111111111111111111111111111111111111111111')

for cat_tulpe in results:
    r = requests.get('https://fr.openfoodfacts.org/categorie/' + cat_tulpe[1] + '.json')
    #print(cat_tulpe[1])
    #print(type(cat_tulpe))
    return_json_API = r.json()  # get json file
    product_JSON = return_json_API["products"]
    #print(type(product_JSON))
    #print(product_JSON)

    print('///////////*************************////////////////////*************************/////////////')

    for product in product_JSON:
        product_dico = dict(product)
        aliment = classe_API.Aliment(product_dico)
        #product_name = aliment.product_name
        #print(product_name)
        #nutrition_grades = aliment.nutrition_grades
        #print(nutrition_grades)  # car nutrition_grades pas tjs la
        #url = aliment.url
        #print(url)
        #stores = aliment.stores
        #print(stores)
        #print(cat_tulpe[1] + 'categoriiiiiiiiiie')

        #print(aliment.SQL_insert(cat_tulpe[0]))

        connection.query_insert(aliment.SQL_insert(cat_tulpe[0]))

        print('///////////--------------///////////////////-----------------')




connection.close()
