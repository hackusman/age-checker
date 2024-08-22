# Vérification de l'âge de l'utilisateur

Ce script Python demande à l'utilisateur d'entrer son âge et affiche un message en fonction de l'âge fourni. Il inclut une gestion des erreurs pour s'assurer que l'entrée est un nombre valide.

## Fonctionnalités

- **Demande d'âge** : Le script invite l'utilisateur à entrer son âge.
- **Conditions d'affichage** :
  - Si l'âge est supérieur à 10, un message indiquant que l'utilisateur est choisi et a une chance de réussir est affiché.
  - Si l'âge est exactement 8, un message encourageant l'utilisateur à redoubler d'efforts est affiché.
  - Pour tous les autres âges, un message de désolé est affiché.
- **Gestion des erreurs** : Le script gère les entrées non numériques en affichant un message d'erreur approprié.

## Utilisation

1. **Exécutez le script Python** :
   ```bash
   python verifier_age.py
   ```

2. **Entrez votre âge lorsqu'il est demandé**.

## Exemple d'exécution

```
Votre âge : 12
Vous êtes choisi et vous avez la chance de réussir.

Votre âge : 8
Vous êtes choisi mais redoublez pleinement d'efforts pour la suite.

Votre âge : 5
Désolé, cela n'a pas marché.

Votre âge : vingt
Veuillez entrer un nombre valide.
```

## Code Source

Voici le code source du script :

```python
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
```