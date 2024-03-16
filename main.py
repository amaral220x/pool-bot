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

@bot.command()
async def votar(ctx, *args):
    global voting_active, opts, ids
    if not voting_active:
        return
    option = ' '.join(args)
    if ctx.author.id in ids:
        await ctx.send(f"{ctx.author.name}, você já votou!")
        return
    if option in opts:
        opts[option] += 1
        ids.append(ctx.author.id)
        await ctx.send(f"Voto computado para {option}")
    else:
        await ctx.send(f"Opção {option} não existe")

@bot.command()
async def resultado(ctx):
    global voting_active, opts
    if not voting_active:
        return
    if ctx.author != lider:
        await ctx.send('Apenas o lider pode encerrar a votação')
        return
    if not voting_active:
        return
    voting_active = False
    await ctx.send(f"Resultado: {opts}")
    await ctx.send(f"Vencedor: {max(opts, key=opts.get)}")
    opts.clear()
    ids.clear()

bot.run(get_key())