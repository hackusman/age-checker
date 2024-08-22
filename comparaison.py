# Demander à l'utilisateur d'entrer son âge
try:
    age = int(input("Votre âge : "))
    
    # Condition pour vérifier si l'utilisateur peut être choisi ou non
    if age > 10:
        print("Vous êtes choisi et vous avez la chance de réussir.")
    elif age == 8:
        print("Vous êtes choisi mais redoublez pleinement d'efforts pour la suite.")
    else:
        print("Désolé, cela n'a pas marché.")
except ValueError:
    print("Veuillez entrer un nombre valide.")
