import discord
import tokens
client = discord.Client()
users = []
@client.event
async def on_ready():
    print('Logado como {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
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
