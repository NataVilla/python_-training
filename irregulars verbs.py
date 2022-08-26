"""This program help us to learn the irregulars verbs and its time"""


# imports of Python
import random


""" List are created with the time'verbs   """

form_base = ['do', 'drink', 'eat']
past_verb = ['did', 'drank', 'ate']

irregulars_verbs = {'do':'did', 'drink':'drank', 'eat':'ate'}

""" La idea es que el programa te de un verbo y tu escribas su pasado, si es correcto te lo dira, sino tambien te lo dira """

""" I use the function "choice" for print elements to random """
select_form_base = random.choice(form_base)


""" program'menu is created  """
menu = """ 
Welcome to the irregulars verbs

The program will give you a verb, your goal will to write this verb in past
1 - start
2 - Finish program

Choose an option: """

option = int(input(menu))

if option == 1:
    print(select_form_base)
    print('Please insert the past of verb')
    verb = input('The past of verb is: ')
    if a == b:
        print("Correct")
    else:
        print("It's not correct")    
# debo crear la logica para que el programa lea el diccionario y me de la respuesta.
elif option == 2:
    pass
else:
    print('choose a correct option')

