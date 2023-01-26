import string

# 1. Demander à l'utilisateur de choisir un mot de passe.
print("Veuillez choisir un mot de passe.")
password = input("")

# Il doit contenir au moins 8 caractères.
def length_pwd(password):
    while True:
        if len(password) < 8:
            print("Mot de passe contient moins de 8 caractères.")
            password = input()
        if len(password) >= 8:
            print("Mot de passe contient au moins 8 caractères.")
            return True

length_pwd(password)

# Il doit contenir au moins une lettre majuscule.
def uppercase_pwd(password):
    uppercase = any(i.isupper() for i in password)
    if uppercase:
        print("True maj")
        return True
    if not uppercase:
        print("False maj")

uppercase_pwd(password)

# Il doit contenir au moins une lettre minuscule.
def lowercase_pwd(password):
    lowercase = any(i.islower() for i in password)
    if lowercase:
        print("True minuscule")
        return True
    if not lowercase:
        print("False minuscule")

lowercase_pwd(password)

# Il doit contenir au moins un chiffre.
def number_pwd(password):
    number = any(i.isdigit() for i in password)
    if number:
        print("True number")
        return True
    if not number:
        print("False number")

number_pwd(password)

# Il doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).
def number_pwd(password):
    spe_char = string.punctuation
    if any(i in spe_char for i in password):
        print("True punctuation")
        return True
    if not any(i in spe_char for i in password):
        print("False punctuation")

number_pwd(password)