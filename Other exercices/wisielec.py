#Hanggame
import faker

#function to return empty list with amoung of letters equal to the other one
def return_floor(sent):
    empty_list = []
    for x in sent:
        empty_list.append(x)
    for p in empty_list:
        print(p, end='')
    return empty_list


#Write out fields on screen
def retuner_field(obj):
    y = 0
    for x in obj:
        if obj[y] != ' ':
            obj[y] = "_"
        y += 1
    print()
    for x in obj:
        print(x, end=" ")
    print()


#Making a list with
def iterate_list(sent):
    list_letter = []
    for x in sent:
        list_letter.append(x)
    return list_letter


def create_game(list_letter, obj, load):
    x = 0
    rund = 1
    print()
    while load:
        u_letter = str(input("Try your chance and guess a letter: "))
        check_letter = isinstance(u_letter, str)
        print()
        print()
        if check_letter and u_letter in list_letter:
            for x in range(0,len(list_letter)):
                if u_letter in list_letter[x]:
                    obj[x] = u_letter
                    x += 1
                    if rund > 12:
                        print('You lost the game...')
                        load = False
        else:
            if rund <12:
                print("You're wrong ,try again!")
                drawner(rund)
                rund += 1
            else:
                print('You lost the game...')
                load = False
                exit()

        for x in obj:
            print(x, end=' ')
        print()
        print()

#Making a visualisation of our game
def drawner(number):
    if number == 1:
        print('|')
    if number == 2:
        print('|.|')
    if number == 3:
        print(' |\n' + ' |\n' + ' |\n' + ' |\n' + ' |\n' + ' |\n' + '|.|')
    if number == 4:
        print(' |/ \n' + ' |\n' + ' |\n' + ' |\n' + ' |\n' + ' |\n' + '|.|')
    if number == 5:
        print('  _________ \n' + ' |/ \n' + ' |\n' + ' |\n' + ' |\n' + ' |\n' + ' |\n' + '|.|')
    if number == 6:
        print('  _________ \n' + ' |/       |\n' + ' |        |\n' + ' |\n' + ' |\n' + ' |\n' + ' |\n' + '|.|')
    if number == 7:
        print('  _________ \n'+' |/       |\n'+' |        |\n'+' |        o\n' + ' |\n' + ' |\n' + ' |\n' + '|.|')
    if number == 8:
        print('  _________ \n'+' |/       |\n'+' |        |\n'+' |        o\n'+' |       -\n' + ' |\n' + '|.|')
    if number == 9:
        print('  _________ \n'+' |/       |\n'+' |        |\n'+' |        o\n'+' |       -0\n' + ' |\n' + '|.|')
    if number == 10:
        print('  _________ \n'+' |/       |\n'+' |        |\n'+' |        o\n'+' |       -0-\n' + ' |\n' + '|.|')
    if number == 11:
        print('  _________\n'+ ' |/       |\n'+' |        |\n'+' |        o\n'+' |       -0-\n'+' |       /\n'+' |\n'+'|.|')

#Making a fake sentence and lower chars and remove full stops
f = faker.Faker()
sentence = f.sentence()
sentence = sentence.lower()
sentence = sentence.strip('.')

obiekt = return_floor(sentence)
returner = retuner_field(obiekt)
lista = iterate_list(sentence)
loader = True
tworzenie = create_game(lista, obiekt, loader)










