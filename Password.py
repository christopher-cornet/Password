# 1. Demander à l'utilisateur de choisir un mot de passe.
print("Veuillez choisir un mot de passe.")
password = input("")

# Il doit contenir au moins 8 caractères.
def length_pwd(password):
    while True:
        if len(password) < 8:
            print("Veuillez choisir un mot de passe valide.")
            password = input()
        if len(password) >= 8:
            print("Mot de passe valide.")
            break

length_pwd(password)

# Il doit contenir au moins une lettre majuscule.
def uppercase_pwd(password):
    uppercase = any(letter.isupper() for letter in password)
    if uppercase:
        print("Majuscule présente(s)")
    elif not uppercase:
        print("Pas de majuscule(s)")

uppercase_pwd(password)

# Il doit contenir au moins une lettre minuscule.
def lowercase_pwd(password):
    lowercase = any(letter.islower() for letter in password)
    if lowercase:
        print("Minuscule présente(s)")
    elif not lowercase:
        print("Pas de minuscule(s)")

lowercase_pwd(password)