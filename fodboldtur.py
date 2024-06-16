import pickle
import time


# Filename for storing the data
filename = 'betalinger.pk'

# Total amount each person needs to pay
total_amount = 4500

# Dictionary to store payment information
fodboldtur = {}

def boldText(text):
    print(f"\033[1m{text}\033[0m")

def underlineText(text):
    print(f"\n\33[4m{text}\33[0m")

def newLine(text):
    print(f"\n{text}")

def newLineBold(text):
    print(f"\n\033[1m{text}\033[0m")

def afslut():
    with open(filename, 'wb') as outfile:
        pickle.dump(fodboldtur, outfile)
    newLineBold("Programmet er afsluttet!")

def menu():
    underlineText("MENU")
    print("1: Print liste")
    print("2: Gem of afslut")
    print("3: Login til indbetaling")
    valg = input("Indtast dit valg: ")
    if valg == '1':
        printliste()
    elif valg == '2':
        afslut()
    elif valg == '3':
        login()
    else:
        clear
        print("Ugyldigt valg. Prøv igen.")
        menu()


def printliste():
    # Sort the dictionary by the amount paid
    sorted_fodboldtur = dict(sorted(fodboldtur.items(), key=lambda item: item[1]))
    underlineText("Indbetalt til rejse")
    newLineBold("Medlemmer - betalt mindst")
    print(f"{"Navn":25} {"Betalt":14} Mangler")

    lavestIndbetalt = list(sorted_fodboldtur.items())[:3]
    for key, value in lavestIndbetalt:
        print(f"{key:20} : {value:6} DKK {total_amount - value:10} DKK ")

    time.sleep(1.5)
    newLineBold("Medlemmer - resterende")
    print(f"{"Navn":25} {"Betalt":14} Mangler")

    ikkeLavestIndbetalt = list(sorted_fodboldtur.items())[3:]
    for key, value in ikkeLavestIndbetalt:

        print(f"{key:20} : {value:6} DKK {total_amount - value:10} DKK ")

    time.sleep(2.5)
    menu()




def login():
    underlineText("LOGIN")
    forbogstav = input("Indtast dit navns forbogstav: ").capitalize()
    matching_names = [navn for navn in fodboldtur if navn.startswith(forbogstav)]

    if matching_names:
        boldText("Matchende navne:")
        for navn in matching_names:
            print(navn)
        valgt_navn = input("\nIndtast dit fulde navn fra listen: ")
        if valgt_navn in fodboldtur:
            indbetaling(valgt_navn)
        else:
            boldText("Navnet findes ikke i systemet - prøv igen.")
            time.sleep(1)
            menu()
    else:
        boldText("Ingen matchende navne fundet - prøv igen.")
        time.sleep(1)
        menu()


def indbetaling(navn):
    try:
        current_amount = fodboldtur.get(navn, 0)
        underlineText("Indbetaling")
        print(f"\033[1m{navn}, du har indbetalt {current_amount} DKK indtil nu.\033[0m")
        owed_amount = total_amount - current_amount
        print(f"Du mangler at indbetale {owed_amount} DKK")

        beløb = float(input(f"\nIndtast ønsket beløb at indbetale for {navn}: "))
        fodboldtur[navn] += beløb
        print(f"Ny saldo for {navn}: {fodboldtur[navn]} DKK.")
    except ValueError:
        print("Ugyldigt beløb.")
    except KeyError:
        print("Navnet findes ikke i systemet.")
    time.sleep(1.5)
    menu()


# Load the data from the file at the start
try:
    with open(filename, 'rb') as infile:
        fodboldtur = pickle.load(infile)
except FileNotFoundError:
    print("Ingen gemt data fundet. Starter en ny fil.")

# Start the menu
menu()
