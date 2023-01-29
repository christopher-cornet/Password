import string

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
    if length_pwd():
        if uppercase_pwd():
            if lowercase_pwd():
                if number_pwd():
                    if spe_char_pwd():
                        print("Le mot de passe est VALIDE.")
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