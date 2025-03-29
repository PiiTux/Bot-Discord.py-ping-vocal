# Importation des modules nécessaires
from os import getenv, path
from dotenv import load_dotenv
from configparser import ConfigParser
from discord import AllowedMentions, Client, Intents

# Chargement du fichier de configuration
config = ConfigParser()
config.read("settings.ini")
CHANNEL = config["SETTINGS"].getint("CHANNEL")
IGNORED_CHANNELS = tuple(map(int, config["SETTINGS"]["IGNORED_CHANNELS"].split(",")))
ROLE = config["SETTINGS"].getint("ROLE")

# Si le fichier .env existe
if path.exists(".env"):
    # Chargement des variables d’environnement à partir du fichier .env
    load_dotenv()

# Récupération du jeton d’accès Discord à partir des variables d’environnement
TOKEN = getenv("DISCORD_TOKEN")

if not TOKEN:
    raise RuntimeError("Aucun jeton d’accès Discord trouvé dans le fichier .env ou dans les variables d’environnement")

# Création des intents pour le client Discord
intents = Intents.default()
intents.voice_states = True

# Création du client Discord
client = Client(intents=intents)


# Événement déclenché lorsque le bot est prêt
@client.event
async def on_ready():
    # Variable pour suivre si un salon est trouvé
    found = False

    # Boucle sur tous les serveurs où est le bot
    for guild in client.guilds:
        channel = guild.get_channel(CHANNEL)
        if channel:
            # On marque que le salon a été trouvé
            found = True
            # On sort de la boucle
            break

    # Si aucun salon n’a été trouvé après la boucle
    if not found:
        # Déconnecte le bot proprement
        await client.close()
        raise RuntimeError(f"Le salon avec l’ID {CHANNEL} n’a été trouvé sur aucun serveur")
    else:
        print(f"Connecté en tant que {client.user} sur {guild.name}")


# Événement déclenché lorsqu’un membre change d’état vocal (rejoindre, quitter, etc.)
@client.event
async def on_voice_state_update(member, before, after):
    # Vérification que le membre a rejoint ou changé de salon vocal
    if (after.channel is not None and before.channel != after.channel and not member.bot and after.channel.id not in IGNORED_CHANNELS):
        # Filtrer les membres présents pour exclure les bots
        members = [m for m in after.channel.members if not m.bot]

        # Vérification que le salon contient uniquement le membre qui vient de rejoindre
        if len(members) == 1:
            # Récupération du salon depuis son ID
            channel = after.channel.guild.get_channel(CHANNEL)
            # Récupération du rôle depuis son ID
            role = after.channel.guild.get_role(ROLE)

            # Vérification que le rôle existe
            if role:
                mention = f"<@&{ROLE}>"
            else:
                mention = "@here"

            # Vérification que le salon existe
            if channel:
                # Envoi du message dans le salon
                await channel.send(f"🎙️ <@{member.id}> s’est connecté dans le salon <#{after.channel.id}>.|| *Ping {mention}*||", allowed_mentions=AllowedMentions(users=False))

# Démarrage du client Discord avec le jeton d’accès
client.run(TOKEN)
