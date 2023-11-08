import discord
from discord.ext import commands
from bot_mantik import *
from BotA_ayarlar import *

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi {bot.user}! I am a chatbot!')

@bot.command()
async def help(ctx):
    await ctx.send("Try these commands: $on_ready, $hello, $password, $bye, $cool, $choose, $coin.")

@bot.command()
async def password(ctx, passs: int):
    await ctx.send(gen_pass(passs))

@bot.command()
async def bye(ctx):
    await ctx.send(":slight_smile:")

@bot.command()
async def coolbot(ctx):
    await ctx.send('Yes, the bot is cool.')

@bot.command()
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))

@bot.command()
async def coin(ctx):
    await ctx.send(yazi_tura())

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for q in range(rolls))
    await ctx.send(result)

@bot.command()
async def repeat(ctx, times: int, content: str):
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}') # type: ignore

@bot.group()
async def cool(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

bot.run(ayarlar["TOKEN"])
