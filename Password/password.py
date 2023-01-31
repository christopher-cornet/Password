import string
import hashlib
import json

# 1. Demander à l'utilisateur de choisir un mot de passe.
def ask_user_pwd():
    print("Veuillez choisir un mot de passe:")
    global password
    password = input("")
    return True

ask_user_pwd()

# Il doit contenir au moins 8 caractères.
def length_pwd():
    global password
    while True:
        if len(password) < 8:
            ask_user_pwd()
        if len(password) >= 8:
            return True

# Il doit contenir au moins une lettre majuscule.
def uppercase_pwd():
    uppercase = any(i.isupper() for i in password)
    if uppercase:
        return True

# Il doit contenir au moins une lettre minuscule.
def lowercase_pwd():
    lowercase = any(i.islower() for i in password)
    if lowercase:
        return True

# Il doit contenir au moins un chiffre.
def number_pwd():
    number = any(i.isdigit() for i in password)
    if number:
        return True

# Il doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).
def spe_char_pwd():
    spe_char = string.punctuation
    if any(i in spe_char for i in password):
        return True

# 2. Vérifiez si le mot de passe choisi respecte les exigences de sécurité.
def check_security():
    while True:
        if length_pwd():
            if uppercase_pwd():
                if lowercase_pwd():
                    if number_pwd():
                        if spe_char_pwd():
                            print("Le mot de passe est valide et a été crypté puis envoyé dans le fichier des mots de passe.")
                            return True
                        else:
                            print("Le mot de passe ne contient pas de caractères spéciaux.")
                            ask_user_pwd()
                    else:
                        print("Le mot de passe ne contient pas de nombre.")
                        ask_user_pwd()
                else:
                    print("Le mot de passe ne contient pas de minuscule.")
                    ask_user_pwd()
            else:
                print("Le mot de passe ne contient pas de majuscule.")
                ask_user_pwd()
        else:
            print("Le mot de passe est trop court.")
            ask_user_pwd()

check_security()

# Gérer les mots de passe renseigné par l’utilisateur en enregistrant les mots de passe hachés dans un fichier.
def json_pwd():
    path = "Password/password_data.json"
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(saved_pwd, file, ensure_ascii=False, indent=4)

saved_pwd = {}
saved_pwd['password'] = password

# Crypte le mot de passe
def hash_pwd_sha256():
    hash_pwd = hashlib.sha256(password.encode('utf-8'))
    str_hash = hash_pwd.hexdigest()
    print("Mot de passe hash" + str_hash)
    saved_pwd['hash'] = str_hash

hash_pwd_sha256()

json_pwd()

# Le programme doit pouvoir permettre à l’utilisateur d’ajouter de nouveaux mots de passe ou d’afficher ces derniers.
print("Voulez vous ajouter un mot de passe ou afficher les mots de passe ? add/print")
add_or_print = input("")

# Ajouter un nouveau mot de passe
def add_pwd():
    global password
    print("Veuillez choisir un nouveau mot de passe:")
    password = input("")

# Afficher les mots de passe
def print_pwd():
    pwd_in_file = open("Password/password_data.json")
    pwd = pwd_in_file.readlines()
    for i in pwd:
        print(i)

# Ajout d'un mot de passe ou affichage des mots de passe
def question():
    if add_or_print == "add":
        add_pwd()
    elif add_or_print == "print":
        print_pwd()

question()