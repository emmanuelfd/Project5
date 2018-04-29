# coding: utf-8


from module.class_gui import user_input, aliment_gui
from module.classe_db import DataBaseConnection


#########load categories form Db to expose them to user##############
connection = DataBaseConnection()

list_category = connection.fetchalll("select * from categorie")


for cat in list_category:
    print ('|' + str(cat[0]) +'|' + cat[1]) # display in the console


######### user select one category#############

input_enter = True

while input_enter:

    user_choice_categorie = user_input.from_input('categorie')

##make sure user enters an id that belongs to the list and is an int
    if user_choice_categorie.check_from_db(list_category) and user_choice_categorie.check_int():
        input_enter = False#as input ok so we break the while
    else:
        continue #while untill input from user is correct



print('vous avez choisi ' + str(user_choice_categorie.choice))



######### going to fetch all aliments form the category selected and dipslay them to user############
list_aliment = connection.fetchalll("select * from aliment where IdCategorie=" + str(user_choice_categorie.choice))


print ('##############')
print(list_aliment)

for x in list_aliment:
    print(str(x[0]) + '##' + str(x[1])) # display in the console



######### user select one aliment#############
input_enter = True

while input_enter: # same as category, while untill input is correct

    user_choice_aliment = user_input.from_input('aliment')


    if user_choice_aliment.check_from_db(list_aliment) and user_choice_aliment.check_int():
        input_enter = False
    else:
        continue

print('vous avez choisi ' + str(user_choice_aliment.choice))


aliment_from_db = connection.fetchalll("select * from aliment where Id=" + str(user_choice_aliment.choice))
aliment_select = aliment_gui(aliment_from_db) # object selected by user - make it an object
print ('##############')



print('indice nutritionel est  ' + aliment_select.nutrition)
print(aliment_select.substitution_prompt())#info for user

print ('******************')

#suggestion of a new aliment with better nutrition index
new_aliment = aliment_select.substitution_aliment(list_aliment)

##display new aliment in the console for user
if new_aliment[0] == 1:
    print('Mieux vaut acheter \'' + new_aliment[2] + '\' qui a un indice \'' + new_aliment[3] + \
    '\' , allez voir sur ' + new_aliment[5] + ' et on doit pouvoir en trouver dans le magasin suivant : '\
    + new_aliment[4])
else:
    print('Rien trouve de mieux !')

######################


print ('##############')


######### save in db if required by user#############
input_enter = True

while input_enter:

    user_choice_save = user_input.from_input_save()


    if user_choice_save.choice.upper() == 'Y':
        print(aliment_select.sql_insert_substitution(new_aliment))
        connection.query_insert(aliment_select.sql_insert_substitution(new_aliment))
        print('C\'est sauve' )
        input_enter = False
    elif user_choice_save.choice.upper() == 'N':
        print('A bientot')
        input_enter = False
    else:
        print('entrer Y ou N - merci')
        continue




print ('#######byby#######')

connection.close_db()