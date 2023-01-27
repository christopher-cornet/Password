import string

# 1. Demander à l'utilisateur de choisir un mot de passe.
print("Veuillez choisir un mot de passe:")
password = input("")

# Il doit contenir au moins 8 caractères.
def length_pwd(password):
    while True:
        if len(password) < 8:
            print("Le mot de passe contient moins de 8 caractères.")
            password = input()
        if len(password) >= 8:
            return True

length_pwd(password)

# Il doit contenir au moins une lettre majuscule.
def uppercase_pwd(password):
    uppercase = any(i.isupper() for i in password)
    if uppercase:
        return True

uppercase_pwd(password)

# Il doit contenir au moins une lettre minuscule.
def lowercase_pwd(password):
    lowercase = any(i.islower() for i in password)
    if lowercase:
        return True

lowercase_pwd(password)

# Il doit contenir au moins un chiffre.
def number_pwd(password):
    number = any(i.isdigit() for i in password)
    if number:
        return True

number_pwd(password)

# Il doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).
def spe_char_pwd(password):
    spe_char = string.punctuation
    if any(i in spe_char for i in password):
        return True

spe_char_pwd(password)

# 2. Vérifiez si le mot de passe choisi respecte les exigences de sécurité.
def check_security():
    if length_pwd(password):
        if uppercase_pwd(password):
            if lowercase_pwd(password):
                if number_pwd(password):
                    if spe_char_pwd(password):
                        print("Le mot de passe est VALIDE.")
                        return True
                    else:
                        print("Le mot de passe ne contient pas de caractères spéciaux.")
                else:
                    print("Le mot de passe ne contient pas de nombre.")
            else:
                print("Le mot de passe ne contient pas de minuscule.")
        else:
            print("Le mot de passe ne contient pas de majuscule.")
    else:
        print("Le mot de passe est trop court.")

check_security()