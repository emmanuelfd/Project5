# coding: utf-8

import requests
from module.classe_db import DataBaseConnection
from module.classe_API import Category,Aliment




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

    if product_dico["products"] < 15 and product_dico["products"] > 10:
        list_category_limited.append(product_dico["name"])
    else:
        print('skip ' + product_dico["name"] + ' because ' + str(product_dico["products"]) + ' products')



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


    page = True
    separator = 1  # page 1 to start
    while page:


        request = requests.get('https://fr.openfoodfacts.org/categorie/' + cat_tulpe[1] + '/' + str(separator) + '.json')
        return_json_API = request.json()  # get json file
        product_JSON = return_json_API["products"] # product_JSON is a list of dico for all aliment

        number_produit_total = return_json_API["count"]
        number_produit_lu = return_json_API["skip"]

        print(str(number_produit_total) + ' count' +'--------' + ' separator is : ' + str(separator))

        if number_produit_lu - number_produit_total >= 0 or separator > 3 or number_produit_total < 20:
            # end of the list or max 3 pages or less than 20
            # as 20 is 1 page (avoid extra loop)
            page = False

        for product in product_JSON:
            product_dico = dict(product)
            aliment = Aliment(product_dico)
            #insertion in DB with ID of the category
            connection.query_insert(aliment.sql_insert(cat_tulpe[0]))

        print('///////////------end of the batch of insertion--------////////////')#to monitor in the console

        separator += 1 # new page

connection.close_db()
