#Kurisu
#message.channel = ctx
#pip install -U python-dotenv

import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.utils import get


from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

import os
import requests
import json
import random
import time

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


#Stupid discord update v1.7.3 -> 2.0.0 didn't mention
#intents = discord.Intents.default()

intents = discord.Intents.all()
#intents.presences = False
#intents.typing = False
intents.members = True
intents.reactions = True
        
kurisu = commands.Bot(command_prefix="!", intents=intents)

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)


def getRandomR34():
  randomR34list = []

  req = Request('https://rule34.xxx/index.php?page=post&s=random', headers={'User-Agent': 'Mozilla/5.0'})
  htmldata = urlopen(req).read()
  soup = BeautifulSoup(htmldata, 'html.parser')
  images = soup.find_all('img')
  
  for item in images:
      randomR34list.append(item['src'])

  randomR34list = max(randomR34list, key=len)
  return(randomR34list)

def flipCoin():
  coin = random.randint(1, 2)
  if coin == 1:
      return("Heads")
  elif coin == 2:
      return("Tails")

def rollDice():
  dice = random.randint(1, 6)
  return(dice)

def getLeagueRoulette():
  roles = ["Top", "Mid", "Jungle", "Support", "ADC/Bot"]
  champions = ["Aatrox", "Ahri", "Akali", "Akshan", "Alistar", "Amumu", "Anivia", "Annie", "Aphelios", "Ashe", "Aurelion Sol", "Azir", "Bard", "Bel'Veth", "Blitzcrank", "Brand", "Braum", "Caitlyn", "Camille", "Cassiopeia", "Cho'Gath", "Corki", "Darius", "Diana", "Draven", "Dr. Mundo", "Ekko", "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Graves", "Gwen", "Hecarim", "Heimerdinger", "Illaoi", "Irelia", "Ivern", "Janna", "Jarvan IV", "Jax", "Jayce", "Jhin", "Jinx", "Kai\'Sa", "Kalista", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle", "Kayn", "Kennen", "Kha\'Zix", "Kindred", "Kled", "Kog\'Maw", "LeBlanc", "Lee Sin", "Leona", "Lillia", "Lissandra", "Lucian", "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "Master Yi", "Miss Fortune", "Mordekaiser", "Morgana", "Nami", "Nasus", "Nautilus", "Neeko", "Nidalee", "Nilah", "Nocturne", "Nunu & Willump", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy", "Pyke", "Qiyana", "Quinn", "Rakan", "Rammus", "Rek\'Sai", "Rell", "Renata Glasc", "Renekton", "Rengar", "Riven", "Rumble", "Ryze", "Samira", "Sejuani", "Senna", "Seraphine", "Sett", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Sylas", "Syndra", "Tahm Kench", "Taliyah", "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "Twisted Fate", "Twitch", "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "Vel\'Koz", "Vex", "Vi", "Viego", "Viktor", "Vladimir", "Volibear", "Warwick", "Wukong", "Xayah", "Xerath", "Xin Zhao", "Yasuo", "Yone", "Yorick", "Yuumi", "Zac", "Zed", "Zeri", "Ziggs", "Zilean", "Zoe", "Zyra"]
  keystones = ["Press the Attack", "Lethal Tempo", "Fleet Footwork", "Conqueror", "Electrocute", "Predator", "Dark Harvest", "Hail of Blades", "Summon Aery", "Acrance Comet", "Phase Rush", "Grasp of the Undying", "Aftershock", "Guardian", "Glacial Augment", "Unsealed Spellbook", "First Strike"]
  secondaryRunes = ["Precision", "Domination", "Sorcery", "Resolve", "Inspiration"]
  mythics = ["Crown of the Shattered Queen", "Divine Sunderer", "Duskblade of Draktharr", "Eclipse", "Evenshroud", "Everfrost", "Frostfire Gauntlet", "Galeforce", "Goredrinker", "Hextech Rocketbelt", "Immortal Shieldbow", "Imperial Mandate", "Kraken Slayer", "Liandry\'s Anguish", "Locket of the Iron Solari", "Luden\'s Tempest", "Moonstone Renewer", "Night Harvester", "Prowler\'s Claw", "Riftmaker", "Shurelya\'s Battlesong", "Stridebreaker", "Sunfire Aegis", "Trinity Force", "Turbo Chemtank"]
  spells = ["Heal", "Ghost", "Barrier", "Exhaust", "Flash", "Teleport", "Smite", "Cleanse", "Ignite"]
  
  randomBuild = [0, 0, 0, 0, 0, 0]
  randomBuild[0] = random.choice(roles)
  randomBuild[1] = random.choice(champions)
  randomBuild[2] = random.choice(keystones)
  randomBuild[4] = random.choice(mythics)
  randomBuild[5] = random.choice(spells)

  possibleSecondaryRunes = ["Press the Attack", "Lethal Tempo", "Fleet Footwork", "Conqueror", "Electrocute", "Predator", "Dark Harvest", "Hail of Blades", "Summon Aery", "Acrance Comet", "Phase Rush", "Grasp of the Undying", "Aftershock", "Guardian", "Glacial Augment", "Unsealed Spellbook", "First Strike"]
  if randomBuild[2] in ["Press the Attack", "Lethal Tempo", "Fleet Footwork", "Conqueror"]:
    possibleSecondaryRunes = ["Domination", "Sorcery", "Resolve", "Inspiration"]
  elif randomBuild[2] in ["Electrocute", "Predator", "Dark Harvest", "Hail of Blades"]:
    possibleSecondaryRunes = ["Precision", "Sorcery", "Resolve", "Inspiration"]
  elif randomBuild[2] in ["Summon Aery", "Arcane Comet", "Phase Rush"]:
    possibleSecondaryRunes = ["Precision", "Domination", "Resolve", "Inspiration"]
  elif randomBuild[2] in ["Grasp of the Undying", "Aftershock", "Guardian"]:
    possibleSecondaryRunes = ["Precision", "Domination", "Sorcery", "Inspiration"]
  elif randomBuild[2] in ["Glacial Augment", "Unsealed Spellbook", "First Strike"]:
    possibleSecondaryRunes = ["Precision", "Domination", "Sorcery", "Resolve"]

  randomBuild[3] = random.choice(possibleSecondaryRunes)
  
  return(randomBuild)

  
@kurisu.event #################################################################################
async def on_ready():
  print(f'{kurisu.user} is connected to the following guilds:')
  for guild in kurisu.guilds:
    if guild.name == GUILD:
      break
    
    print(f'{guild.name}(id: {guild.id})')

@kurisu.event
async def on_member_join(member):
  #await member.create_dm()
  await member.dm_channel.send(f"Hi {member.name}, welcome to {member.guild.name}!")

@kurisu.listen()
async def on_message(message):
  if "cool" in message.content:
    await message.add_reaction('\U0001F60E')#Unicode to python: '+' becomes '000' and "\" before "U"

#await kurisu.process_commands(message)
@kurisu.listen()
async def on_message(message):
  if "kurisu" in message.content:
    await message.reply("<@294325550330413056>")
    

@kurisu.command(help="ctx.author.mention")
async def hello(ctx):
  await ctx.send(f"Hello {ctx.author.mention}")

@kurisu.command(help="Get random quotes from zenquotes.io")
async def inspire(ctx):
  await ctx.send(get_quote())
    
@kurisu.command(help="heh")
@commands.is_nsfw()
async def rule34(ctx):
  await ctx.send(f"||{getRandomR34()}||")

@kurisu.command(help="Heads or tails")
async def flipcoin(ctx):
  await ctx.send(flipCoin())

@kurisu.command(help="randint(1, 6)")
async def rolldice(ctx):
  await ctx.send(rollDice())

@kurisu.command(aliases=['leagueroulette', 'lr', 'ff15'], help="Random league build")
async def league_roulette(ctx):
  leagueRoulette = getLeagueRoulette()
  await ctx.send(f"Role: {leagueRoulette[0]}\nChampion: {leagueRoulette[1]}\nKeystone: {leagueRoulette[2]}\nSecondary Runes: {leagueRoulette[3]}\nMythic: {leagueRoulette[4]}\nSummoner spell: {leagueRoulette[5]}")

@kurisu.command(help="Real music")
async def music(ctx):
  await ctx.send("https://www.youtube.com/watch?v=4Q4JRVW5BFE")

@kurisu.command(help="Never gonna gi-")
async def rick(ctx):
  await ctx.send("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
  
@kurisu.command(help="Mention someone")
async def mention(ctx, arg):
  await ctx.send(arg)

@kurisu.command(help="joe")
async def joe(ctx):
  await ctx.send("Hello <@234121525521940480>!")

@kurisu.command(help="Repeats message")
async def say(ctx, *args):
  await ctx.send("{}".format(" ".join(args)))

@kurisu.command(help="$spam {word/user} {how many times}")
async def spam(ctx, arg, numba):
  for i in range(int(numba)):
    await ctx.send(arg)
    time.sleep(0.1)

@kurisu.command()
async def join(ctx):
  channel = ctx.author.voice.channel
  await channel.connect()

@kurisu.command()
async def leave(ctx):
  await ctx.voice_client.disconnect()

@kurisu.command(help="6 digit number generator")
@commands.is_nsfw()
async def nhentai(ctx):
  num = random.randint(1, 420000)
  await ctx.send(f"https://nhentai.net/g/{num}/")


@kurisu.command(aliases=["addrole"], help="$giverole @user role") #pass_context=True
#@commands.has_role("Admin")
async def giverole(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send(f"Hey {ctx.author.name}, {user.name} has been giving a role called: {role.name}")

@kurisu.command(help="$send_dm @user msg")
async def send_dm(ctx,member:discord.Member,*,content):
  await member.send(content)

@kurisu.command(help="testing random stuff")
async def test(ctx):
  new_msg = await ctx.channel.send("hello!")
  await new_msg.add_reaction('\U0001F618')




@kurisu.command(aliases=["rr"], help="reaction roles") ####################
async def reaction_roles(ctx, role: discord.Role, emoji, *args):
  new_msg = await ctx.send("{}".format(" ".join(args)))
  await new_msg.add_reaction(emoji)

  @kurisu.listen() #I WANNA ADD MULTIPLE EMOJIES ON A MESSAGE
  async def on_reaction_add(reaction, user):
    await user.add_roles(role)
    await user.send(f"{user.name} has been giving a role called: {role.name}")


@kurisu.command(aliases=["rr2"], help="reaction roles but with 2 emojis")
async def reaction_roles2(ctx, role_1: discord.Role, role_2: discord.Role, emoji_1, emoji_2, *args):
  new_msg = await ctx.send("{}".format(" ".join(args)))
  await new_msg.add_reaction(emoji_1)
  await new_msg.add_reaction(emoji_2)

  @kurisu.listen()
  async def on_reaction_add(reaction, user):
   
    if reaction.emoji == emoji_1:
      await user.add_roles(role_1)
      await user.send(f"{user.name} has been given a role called: {role_1.name}")
    elif reaction.emoji == emoji_2:
      await user.add_roles(role_2)
      await user.send(f"{user.name} has been given a role called: {role_2.name}")
    else:
      await user.send(f"{reaction} is not a valid reaction")
      time.sleep(0.01)





kurisu.run(TOKEN)
