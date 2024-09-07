import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def ha(ctx, count_ha = 5):
    await ctx.send("hahahahaha" * count_ha)

@bot.command()
async def Nice(ctx):
    await ctx.send(f'GG! {bot.user}!')

@bot.command()
async def wakeupf1lthy (ctx):
    await ctx.send(f'!Playboi Carti!')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Добро пожаловать дорогой друг на наш замечательный сервер!!!"""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)





bot.run("ТОКЕН ВАШЕГО БОТА")