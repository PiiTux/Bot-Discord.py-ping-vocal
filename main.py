# Importation des modules nécessaires
from os import getenv
from dotenv import load_dotenv
from discord import AllowedMentions, Client, Intents

# ID du salon où le bot doit envoyer le message (obligatoire)
CHANNEL = 0000000000000000000
# Liste des ID des salons vocaux à ignorer (facultatif)
IGNORED_CHANNELS = (0000000000000000000, 0000000000000000000)
# ID du rôle à pinger (facultatif)
ROLE = 0000000000000000000

# Chargement des variables d'environnement à partir du fichier .env
load_dotenv()

# Récupération du jeton d'accès Discord à partir des variables d'environnement
TOKEN = getenv("DISCORD_TOKEN")

# Création des intents pour le client Discord
intents = Intents.default()
intents.voice_states = True

# Création du client Discord
client = Client(intents=intents)


# Événement déclenché lorsque le bot est prêt
@client.event
async def on_ready():
    # Vérification que le bot est bien présent sur au moins un serveur
    if not client.guilds:
        # Déconnecte le bot proprement
        await client.close()
        raise RuntimeError("Le bot n'est présent sur aucun serveur")

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

    # Si aucun salon n'a été trouvé après la boucle
    if not found:
        # Déconnecte le bot proprement
        await client.close()
        raise RuntimeError(f"Le salon avec l'ID {CHANNEL} n'a été trouvé sur aucun serveur")
    else:
        print(f"Prêt ! Connecté en tant que {client.user} sur {guild.name}")


# Événement déclenché lorsqu'un membre change d'état vocal (rejoindre, quitter, etc.)
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
                await channel.send(f"🎙️ <@{member.id}> s'est connecté dans le salon <#{after.channel.id}>.|| *Ping {mention}*||", allowed_mentions=AllowedMentions(users=False))

# Démarrage du client Discord avec le jeton d'accès
client.run(TOKEN)
