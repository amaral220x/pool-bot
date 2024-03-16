import disnake
from disnake.ext import commands
from key import get_key

bot = commands.Bot(command_prefix='>>', intents=disnake.Intents.all())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def test(ctx):
    await ctx.send('test')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

    bot = commands.Bot(command_prefix='!')

voting_active = False
lider = ''
opts = {}
ids = []

@bot.command()
async def democracia(ctx):
    global voting_active, opts, ids, lider
    opts = {}
    ids = []
    voting_active = True
    await ctx.send('Viva a democracia!')
    msg = await ctx.send('Vamos votar? Por favor, responda essa mensagem com os filmes que vocês querem votar')
    lider = ctx.author
@bot.command()
async def opcoes(ctx, *args):
    global voting_active, opts
    if not voting_active:
        return
    join = ' '.join(args)
    filmes = join.split(',')
    for filme in filmes:
        opts[filme.strip()] = 0
    print(opts)

