import pickle

filename = 'betalinger.pk'

#Hvad turen koster i alt pr person
total_amount = 4500

# Indlæs data fra filen, hvis den findes, ellers opret en tom dictionary
try:
    with open(filename, 'rb') as infile:
        fodboldtur = pickle.load(infile)
except FileNotFoundError:
    fodboldtur = {}


def afslut():
    with open(filename, 'wb') as outfile:
        pickle.dump(fodboldtur, outfile)
    print("Programmet er afsluttet!")


def printliste():

    #Sortering af liste:
    sorted_fodboldtur = dict(sorted(fodboldtur.items(), key=lambda item: item[1]))

    print("Liste over indbetalinger til tur")

    print("Disse har betalt mindst:")
    lavestIndbetalt = list(fodboldtur.items())[:3]
    for key, value in lavestIndbetalt:
        print(f"{key}: {value} DKK   mangler",str(total_amount-value), " DKK")


    print("Liste over resterende medlemmer")
    ikkeLavestIndbetalt = list(fodboldtur.items())[4:]
    for key, value in ikkeLavestIndbetalt:
        print(f"{key}:1"
              f" {value} DKK   mangler",str(total_amount-value), " DKK")

    menu()





def menu():
    print("MENU")
    print("1: Print liste")
    print("2: Afslut program")
    print("3: Login til indbetaling")
    valg = input("Indtast dit valg: ")
    if valg == '1':
        printliste()
    elif valg == '2':
        afslut()
    elif valg == '3':
        login()
    else:
        print("Ugyldigt valg. Prøv igen.")
        menu()


def login():
    forbogstav = input("Indtast dit navns forbogstav: ").capitalize()
    matching_names = [navn for navn in fodboldtur if navn.startswith(forbogstav)]

    if matching_names:
        print("Matchende navne:")
        for navn in matching_names:
            print(navn)
        valgt_navn = input("Indtast dit fulde navn fra listen: ")
        if chosen_name in fodboldtur:
            indbetaling(valgt_navn)
        else:
            print("Navnet findes ikke i systemet.")
            menu()
    else:
        print("Ingen matchende navne fundet.")
        menu()


def indbetaling(navn):


    try:
        current_amount = fodboldtur.get(navn, 0)
        print(f"{navn}, du har indbetalt {current_amount} DKK indtil nu.")
        owed_amount = total_amount - current_amount
        print("Du mangler at indbetale", str(owed_amount), " DKK")

        beløb = float(input(f"Indtast beløb for {navn}: "))
        fodboldtur[navn] += beløb
        print(f"Ny saldo for {navn}: {fodboldtur[navn]} DKK.")
    except ValueError:
        print("Ugyldigt beløb.")
    except KeyError:
        print("Navnet findes ikke i systemet.")
    menu()


menu()
