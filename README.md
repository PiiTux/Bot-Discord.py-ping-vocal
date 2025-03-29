# 🎤 Bot Discord de Notification Vocale 🚨

Bienvenue dans le monde magique des **pings vocaux** sur Discord ! Ce bot, créé en Python avec `discord.py`, vous alerte dès qu’un utilisateur rejoint un salon vocal sur votre serveur.

## 🎯 Fonctionnalités

- 🚪 Envoie une notification chaque fois qu’un utilisateur rejoint un salon vocal.
- 🔧 Variables de configuration ultra simples à modifier dès le début du code.
- ⚡ Léger et rapide, grâce à `discord.py` (la magie Python 🐍).

## 💡 Comment ça marche ?

Le bot écoute les événements sur les salons vocaux. Quand quelqu’un débarque dans l’un d’eux, hop ! Une notification part, soit pour pinger un rôle, soit pour envoyer un message dans un canal spécifique. Ça dépend de ta configuration.

## 📦 Installation

### 📋 Prérequis
- Python (version 3.8 ou supérieure). Si tu as une version plus vieille… c’est probablement le moment de la mettre à jour 😉

### 🚀 Étapes d’installation

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

1. **Crée un fichier `.env`** : À la racine du projet, ajoute un fichier `.env` pour stocker les infos sensibles.
2. **Ajoute-y ton token Discord** :
    ```env
    DISCORD_TOKEN = VOTRE_TOKEN_DISCORD_ICI
    ```
3. **Paramètres obligatoires dans `settings.ini`** : Le bot se configure avec un fichier `settings.ini` ultra simple (presque trop facile, genre pas d’excuses !). Voilà ce que tu peux modifier pour faire tourner la bête :
- **`CHANNEL`** : L’ID du salon où le bot va balancer son message pour soûler les gens en les prévenant dès qu’un utilisateur rejoint un salon vocal 📢
4. **Paramètres optionnels** : Si tu veux rajouter des petites touches perso, tu peux modifier des trucs comme les salons vocaux à ignorer ou le rôle à pinger (si t’as envie de faire chier tout le monde, tu sais quoi faire) 😈 :
- **`IGNORED_CHANNELS`** : Liste des salons vocaux à ignorer, séparés par des virgules (exemple : `123456789, 987654321`) 🚫
- **`ROLE`** : ID du rôle à pinger (parce que parfois, faut secouer un peu les rôles dormants) ⚡

## 🚀 Démarrage du bot

1. Une fois que tu as tout configuré, tu peux lancer ton bot (pas trop violemment) avec cette commande :
    ```bash
    python3 main.py
    ```
2. Pour l’exécuter en arrière-plan sans trop de souffrance (promis, il ne criera pas), tu peux utiliser cette commande :
    ```bash
    nohup python3 main.py &
    ```
3. Ou avec `tmux` (si tu es du genre à aimer organiser ta vie comme un boss) :
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
   - Assure-toi qu’il n’a pas été révoqué via le [portail des développeurs Discord](https://discord.com/developers/applications).

2. **Le salon textuel est-il bien défini ?**
   - Dans `main.py`, vérifie l’ID du salon :
     ```python
     CHANNEL = 0000000000000000000
     ```
   - Le bot doit avoir la permission d’envoyer des messages dans ce salon.

3. **Les dépendances sont-elles installées ?**
   - Assure-toi que tous les modules nécessaires sont bien installés :
     ```bash
     pip install -U discord python-dotenv
     ```

4. **Regarde les logs**
   - Si le bot plante, regarde les erreurs affichées dans le terminal pour avoir un indice.

## 📜 Licence

Ce projet est sous licence Apache 2.0. Consulte le fichier [LICENSE](LICENSE) pour plus d’infos.