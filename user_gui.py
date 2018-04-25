# coding: utf-8


from module.class_gui import user_input, aliment_gui
from module.classe_db import DataBaseConnection



connection = DataBaseConnection()

list_category = connection.fetchalll("select * from categorie")


for cat in list_category:
    print ('|' + str(cat[0]) +'|' + cat[1])



input_enter = True

while input_enter:

    user_choice_categorie = user_input.from_input('categorie')


    if user_choice_categorie.check_from_db(list_category) and user_choice_categorie.check_int():
        input_enter = False
    else:
        continue



print('vous avez choisi ' + str(user_choice_categorie.choice))


######################


list_aliment = connection.fetchalll("select * from aliment where IdCategorie=" + str(user_choice_categorie.choice))

print(list_aliment)
#print ('##############')
#print(str(user_choice.choice))

#print ('##############')
#print(list_aliment)
#print ('##############')

for x in list_aliment:
    print(str(x[0]) + '##' + str(x[1]))


input_enter = True

while input_enter:


    user_choice_aliment = user_input.from_input('aliment')


    if user_choice_aliment.check_from_db(list_aliment) and user_choice_aliment.check_int():
        input_enter = False
    else:
        continue

print('vous avez choisi ' + str(user_choice_aliment.choice))

aliment_from_db = connection.fetchalll("select * from aliment where Id=" + str(user_choice_aliment.choice))


aliment_select = aliment_gui(aliment_from_db)
print ('##############')



print('indice nutritionel est  ' + aliment_select.nutrition)
print(aliment_select.substitution_prompt())

print ('******************')
for x in list_aliment:
    if str(x[2]) < aliment_select.nutrition and str(x[2]) != "Unkmown":
        print(str(x[0]) + '##' + str(x[1]) + '##' + str(x[2]) + '##' + str(x[3]))
        break

print ('##############')





