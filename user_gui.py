# coding: utf-8


from module.class_gui import user_input
from module.classe_db import DataBaseConnection



connection = DataBaseConnection()

list_category = connection.fetchalll("select * from categorie")


for cat in list_category:
    print ('|' + str(cat[0]) +'|' + cat[1])



input_enter = True

while input_enter:

    user_choice = user_input.from_input()


    if user_choice.check_from_db(list_category) and user_choice.check_int():
        input_enter = False
    else:
        continue



print('vous avez choisi ' + str(user_choice.choice))


######################


list_aliment = connection.fetchalll("select * from aliment where IdCategorie=" + str(user_choice.choice))

print(list_aliment)
print ('##############')

for x in list_aliment:
    print(str(x[0]) + '##' + str(x[1]))






#-----------------------

choice_aliment = input("saisir le chiffre de l'aliment")
