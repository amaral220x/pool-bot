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

        return

    if message.content.startswith('$$votar'):
        messages = await message.channel.send('Por favor reaja a esta mensagem quem participará da votação')
        await messages.add_reaction("✅")
        def check(reaction,user):
            return str(reaction.emoji) == '✅', user
        confirmation, user= await client.wait_for("reaction_add", check=check) 
        if confirmation: 
            users.append(user)
            await user.send("Olá, me mande o link do filme assim. '$$filme [link]'")
    if message.content.startswith('$$filme'):
        if message.author in users:
            await message.author.send("Ok")
        


client.run(tokens.gerar_token())
