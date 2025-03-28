# 🎤 Bot Discord de Notification Vocale 🚨

Bienvenue dans le monde magique des **pings vocaux** sur Discord ! Ce bot, créé en Python avec `discord.py`, vous alerte dès qu'un utilisateur rejoint un salon vocal sur votre serveur.

## 🎯 Fonctionnalités

- 🚪 Envoie une notification chaque fois qu’un utilisateur rejoint un salon vocal.
- 🔧 Variables de configuration ultra simples à modifier dès le début du code.
- ⚡ Léger et rapide, grâce à `discord.py` (la magie Python 🐍).

## 💡 Comment ça marche ?

Le bot écoute les événements sur les salons vocaux. Quand quelqu’un débarque dans l’un d’eux, hop ! Une notification part, soit pour pinger un rôle, soit pour envoyer un message dans un canal spécifique. Ça dépend de ta configuration.

## 📦 Installation

### 📋 Prérequis
- Python (version 3.8 ou supérieure). Si tu as une version plus vieille… c’est probablement le moment de la mettre à jour 😉

### 🚀 Étapes d'installation

1. Clone le dépôt :
    ```bash
    git clone https://github.com/PiiTux/Bot-Discord.py-ping-vocal.git
    cd Bot-Discord.py-ping-vocal
    ```

2. Crée un environnement virtuel pour que tout soit bien isolé :
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Installe les dépendances :
    ```bash
    pip install -U discord python-dotenv
    ```

### ⚙️ Configuration

1. Crée un fichier `.env` à la racine du projet.
2. Ajoute-y ton token Discord :
    ```
    DISCORD_TOKEN = VOTRE_TOKEN_DISCORD_ICI
    ```
3. Modifie les variables de configuration en haut de `main.py` pour spécifier l'ID du salon où envoyer les messages :
    ```python
    # ID du salon où le bot enverra les messages (obligatoire)
    CHANNEL = 0000000000000000000
    ```
4. (Optionnel) Modifie d’autres paramètres comme les salons vocaux à ignorer, ou le rôle à pinger :
    ```python
    # Liste des salons vocaux à ignorer (facultatif)
    IGNORED_CHANNELS = (0000000000000000000, 0000000000000000000)
    # ID du rôle à pinger (facultatif)
    ROLE = 0000000000000000000
    ```

## 🚀 Démarrage du bot

1. Une fois que tu as tout configuré, tu peux lancer ton bot avec cette commande :
    ```bash
    python3 main.py
    ```

2. Pour l’exécuter en arrière-plan (Linux) :
    ```bash
    nohup python3 main.py &
    ```
    Ou avec `tmux` (si tu es du genre à aimer organiser ta vie comme un boss) :
    ```bash
    tmux new -s bot_discord "python3 main.py"
    ```

## 🛠️ Dépannage

Si le bot joue les troubles-fêtes, voici quelques vérifications :

1. **Vérifie ton token Discord**
   - Ton fichier `.env` doit contenir la ligne suivante avec un token valide :
     ```
     DISCORD_TOKEN = VOTRE_TOKEN_DISCORD_ICI
     ```
   - Assure-toi qu'il n’a pas été révoqué via le [portail des développeurs Discord](https://discord.com/developers/applications).

2. **Le salon textuel est-il bien défini ?**
   - Dans `main.py`, vérifie l'ID du salon :
     ```python
     CHANNEL = 0000000000000000000
     ```
   - Le bot doit avoir la permission d'envoyer des messages dans ce salon.

3. **Les dépendances sont-elles installées ?**
   - Assure-toi que tous les modules nécessaires sont bien installés :
     ```bash
     pip install -U discord python-dotenv
     ```

4. **Regarde les logs**
   - Si le bot se met à ramer, consulte les erreurs dans le terminal pour identifier le problème.

## 📈 Compatibilité

Ce bot fonctionne avec `discord.py` et est compatible avec les versions de Python 3.8+.

## 🌟 Contribuer

Les contributions sont les bienvenues ! Si tu veux faire une modif’ :
1. Fork le dépôt.
2. Crée une branche pour ta feature :
    ```bash
    git checkout -b feature/nom-de-la-fonctionnalite
    ```
3. Fais tes changements, puis commit :
    ```bash
    git commit -m "Ajout d'une nouvelle fonctionnalité"
    ```
4. Pousse ta branche :
    ```bash
    git push origin feature/nom-de-la-fonctionnalite
    ```
5. Ouvre une Pull Request.

## 📜 Licence

Ce projet est sous licence Apache 2.0. Consulte le fichier [LICENSE](LICENSE) pour plus d'infos.

## 🆘 Support

Si t’as un souci ou une question, ouvre une [issue](https://github.com/PiiTux/Bot_Discord.py_ping_vocal/issues).

## 🙏 Remerciements

Merci d’utiliser ce bot ! Si t’es fan, n’oublie pas de laisser une étoile ⭐ sur le dépôt GitHub.