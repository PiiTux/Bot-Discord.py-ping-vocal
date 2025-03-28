# Bot Discord de notification vocale

Ce bot Discord, développé en Python, est conçu pour envoyer une notification (ping) aux utilisateurs sur un serveur Discord lorsqu'une personne rejoint un salon vocal.

## Fonctionnalités

- Envoie une notification lorsqu'un utilisateur rejoint un salon vocal.
- Configuration simple via un fichier `.env`.
- Léger et rapide grâce à l'utilisation de la bibliothèque `discord.py`.

## Installation

### Prérequis
- Python (version 3.8 ou supérieure) : [Télécharger ici](https://www.python.org/).

### Étapes d'installation

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/PiiTux/Bot_Discord.py_ping_vocal.git
    cd Bot_Discord.py_ping_vocal
    ```
2. Créez un environnement virtuel pour isoler les dépendances :
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
3. Installez les dépendances :
    ```bash
    pip install -U discord python-dotenv
    ```

### Configuration

1. Créez un fichier `.env` à la racine du projet.
2. Ajoutez-y votre token Discord :
    ```
    DISCORD_TOKEN = VOTRE_TOKEN_DISCORD_ICI
    ```

## Démarrage du bot

1. Lancez le bot en exécutant le fichier main.py :
    ```bash
    python3 main.py
    ```

## Contribuer

Les contributions sont les bienvenues ! Pour contribuer :
1. Forkez le dépôt.
2. Créez une branche pour vos modifications :
    ```bash
    git checkout -b feature/nom-de-la-fonctionnalite
    ```
3. Effectuez vos modifications et validez-les :
    ```bash
    git commit -m "Ajout d'une nouvelle fonctionnalité"
    ```
4. Poussez vos modifications :
    ```bash
    git push origin feature/nom-de-la-fonctionnalite
    ```
5. Ouvrez une Pull Request.

## Licence

Ce projet est sous licence Apache 2.0. Consultez le fichier [LICENSE](LICENSE) pour plus d'informations.

## Support

Si vous rencontrez des problèmes ou avez des questions, n'hésitez pas à ouvrir une [issue](https://github.com/PiiTux/Bot_Discord.py_ping_vocal/issues).

## Remerciements

Merci d'utiliser ce bot ! Si vous l'appréciez, n'hésitez pas à laisser une étoile ⭐ sur le dépôt GitHub.
