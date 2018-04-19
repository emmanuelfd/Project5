# coding: utf-8

import requests
from module.classe_db import DataBaseConnection
from module.classe_API import Category,Aliment



page = True
separator = 20 # page 1 to start

##connect to openfoodfact to get list of categorie
##//fr => will be in french
request = requests.get('https://fr.openfoodfacts.org/categories.json')
return_json_API = request.json()#get json file


number_category = return_json_API["count"]#gives how many category - note used at the moment
product_JSON = return_json_API["tags"]#will be a list [] of dico with all categories with details (id, names,..)
list_category_limited = []##a supprimer




for category in product_JSON:
#filter to get only category with a limited number of product (20 and 30).

    product_dico = dict(category)#as product_JSON is a list of dico

    if product_dico["products"] < 30 and product_dico["products"] > 20:
        list_category_limited.append(product_dico["name"])
    else:
        print('skip ' + product_dico["name"] + ' because ' + str(product_dico["products"]) + ' products')



print('######################')
### Connect to the database

connection = DataBaseConnection()

##insertion categories in DB###
for cat in list_category_limited:

    #categorie = classe_API.Category(cat)#
    categorie = Category(cat)#

    print('==============')##to monitor in the console
    print(categorie.name)##to monitor in the console

    connection.query_insert(categorie.sql_insert())





##################################################
#####download categories from DB to get IDs#######
###and to retrieve aliments form those categorie##
#############from API#############################
##################################################

results = connection.fetchalll(categorie.sql_load())


for cat_tulpe in results:
    #name from category tulpe (id, name) and request for aliment for each category
    request = requests.get('https://fr.openfoodfacts.org/categorie/' + cat_tulpe[1] + '.json')
    return_json_API = request.json()  # get json file
    product_JSON = return_json_API["products"] # product_JSON is a list of dico for all aliment

    print('///////////***************/////////////')#to monitor in the console

    for product in product_JSON:
        product_dico = dict(product)
        aliment = Aliment(product_dico)
        #insertion in DB with ID of teh category
        connection.query_insert(aliment.sql_insert(cat_tulpe[0]))

        print('///////////--------------////////////')#to monitor in the console

connection.close()
