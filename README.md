# Bot Discord de notification vocale

Ce bot Discord, développé en Python, est conçu pour envoyer une notification (ping) aux utilisateurs sur un serveur Discord lorsqu'une personne rejoint un salon vocal.

## Fonctionnalités

- Envoie une notification lorsqu'un utilisateur rejoint un salon vocal.
- Variables de configuration facilement modifiables en début de code.
- Léger et rapide grâce à l'utilisation de la bibliothèque `discord.py`.

## Fonctionnement du bot

Le bot écoute les événements de connexion aux salons vocaux du serveur. Lorsqu'un utilisateur rejoint un salon vocal, le bot déclenche une notification qui peut ping un rôle ou envoyer un message dans un canal textuel prédéfini.

## Installation

### Prérequis
- Python (version 3.8 ou supérieure).

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
3. Modifiez les variables de configuration en début de code dans `main.py` pour définir l'ID du salon où envoyer les messages :
    ```python
    # ID du salon où le bot doit envoyer le message (obligatoire)
    CHANNEL = 0000000000000000000
    ```
4. (Optionnel) Modifiez les autres variables de configuration en début de code dans `main.py` pour adapter le comportement du bot :
    ```python
    # Liste des ID des salons vocaux à ignorer (facultatif)
    IGNORED_CHANNELS = (0000000000000000000, 0000000000000000000)
    # ID du rôle à pinger (facultatif)
    ROLE = 0000000000000000000
    ```

## Démarrage du bot

1. Lancez le bot en exécutant le fichier `main.py` :
    ```bash
    python3 main.py
    ```

2. Pour exécuter le bot en arrière-plan (Linux) :
    ```bash
    nohup python3 main.py &
    ```
    Ou avec `tmux` :
    ```bash
    tmux new -s bot_discord "python3 main.py"
    ```

## Dépannage

Si le bot ne fonctionne pas comme prévu, voici quelques vérifications à effectuer :

1. **Vérifier le token Discord**
   - Assurez-vous que votre fichier `.env` contient bien la ligne suivante avec un token valide :
     ```
     DISCORD_TOKEN = VOTRE_TOKEN_DISCORD_ICI
     ```
   - Vérifiez que le token est toujours actif et n’a pas été révoqué dans le [portail des développeurs Discord](https://discord.com/developers/applications).

2. **Vérifier que le salon textuel est bien défini**
   - Dans `main.py`, l’ID du salon (`CHANNEL`) doit être correctement renseigné :
     ```python
     CHANNEL = 0000000000000000000
     ```
   - Assurez-vous que le bot a bien les permissions pour envoyer des messages dans ce salon.

3. **Vérifier les dépendances**
   - Assurez-vous que les modules nécessaires sont bien installés :
     ```bash
     pip install -U discord python-dotenv
     ```

4. **Regarder les logs d’erreur**
   - Si le bot plante, regardez les erreurs affichées dans le terminal pour identifier le problème.

## Compatibilité

Ce bot utilise la bibliothèque `discord.py` et est compatible avec les versions récentes de Python (3.8+). Il est recommandé d'utiliser la dernière version stable de `discord.py` pour garantir une compatibilité optimale.

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