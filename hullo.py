import discord
import asyncio
import random
import json
import time
#import secreto
#import json
import requests
import youtube_dl
from datetime import datetime, timedelta
import time
import psutil
import os
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont, ImageOps

#Id dos Banidos de Utilizar o BOT
bp = []
global pro
pro = [369962464613367811, 313794294647488513, 413370252919832576]

global players
players = {}
prefix = '!!'

amarelo = 0xFFCC00
vermelho = 0xbb0021
discordcolor = 0x36393f
client = discord.Client()
#client = discord.AutoShardedClient(shard_count=2)

is_prod = os.environ.get('IS_HEROKU', None)
if is_prod:
    token = os.environ.get('TOKEN')
    
@client.event
async def on_ready():
    print("=================================")
    print("Nome: %s"%client.user.name)
    print("ID: %s"%client.user.id)
    print("Online em : {} Serves".format(str(len(client.guilds))))
    print('Em contato com : ' + str(len(set(client.get_all_members()))) + ' usuarios')
    print('Link de convite do {}:'.format(client.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
    print("=================================")

    while True:
        ebservers = str(len(client.guilds))
        ebplayers = str(len(set(client.get_all_members())))
        game = discord.Game("Hullo Is Back")
        await client.change_presence(status=discord.Status.idle, activity=game)
        canalservers = client.get_channel(475432717031440395)
        await canalservers.edit(name='📝| Servidores: ' + (str(len(client.guilds))))
        await asyncio.sleep(10)
        game = discord.Game("Hullo24h")
        await client.change_presence(status=discord.Status.idle, activity=game)
        canalusers = client.get_channel(475440504457396224)
        await canalusers.edit(name='📝| Usuários: ' + str(len(set(client.get_all_members()))))
        await asyncio.sleep(10)
        game = discord.Game("!!ajuda")
        await client.change_presence(status=discord.Status.idle, activity=game)
        await canalservers.edit(name='📝| Servidores: ' + (str(len(client.guilds))))
        await asyncio.sleep(10)
        game = discord.Game("Totalmente Reformulado")
        await client.change_presence(status=discord.Status.idle, activity=game)
        await canalusers.edit(name='📝| Usuários: ' + str(len(set(client.get_all_members()))))
        await asyncio.sleep(10)

@client.event
async def on_member_join(member):
    try:
        embedbemvindo = discord.Embed(
            title=None,
            color=amarelo,
            description='Seja Bem Vindo ao Servidor ' + member.guild.name + ' ' + member.mention + ' \n',
        )
        embedbemvindo.set_author(name='Bem Vindo ao ' + member.guild.name, icon_url='http://bit.ly/2JEDsjf')
        role = discord.utils.find(lambda r: r.name == "Membro", member.guild.roles)
        await member.add_roles(role)
        channelbv = discord.utils.find(lambda c: c.name == '🔀entrada-e-saida', member.guild.text_channels)
        url = requests.get(member.avatar_url)
        avatar = Image.open(BytesIO(url.content))
        avatar = avatar.resize((110, 110));
        bigsize = (avatar.size[0] * 3, avatar.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(avatar.size, Image.ANTIALIAS)
        avatar.putalpha(mask)

        output = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
        output.putalpha(mask)
        output.save('avatar.png')

        fundo = Image.open('bemvindonovo.png')
        fonte = ImageFont.truetype('Technoma.otf', 30)
        escrever = ImageDraw.Draw(fundo)
        escrever.text(xy=(165, 45), text=member.name, fill=(211, 95, 0), font=fonte, align="center")

        fundo.paste(avatar, (39, 8), avatar)
        fundo.save('toperzon.png')
        await channelbv.send(file=discord.File(fp="toperzon.png"))
        await channelbv.send('Seja Bem-Vindo ' + member.mention)
        #await member.send(embed= embedbemvindo) FUNÇÃO OFF PORCAUSA DO LORITTA BOT LIST
    except:
        try:
            embedbemvindo = discord.Embed(
                title=None,
                color=amarelo,
                description='Seja Bem Vindo ao Servidor ' + member.guild.name + ' ' + member.mention + ' \n',
            )
            embedbemvindo.set_author(name='Bem Vindo ao ' + member.guild.name, icon_url='http://bit.ly/2JEDsjf')
            # await client.send_message(member, embed=embedbemvindo)
            channelmr = discord.utils.find(lambda c: c.name == '🔀entrada-e-saida', member.guild.text_channels)
            url = requests.get(member.avatar_url)
            avatar = Image.open(BytesIO(url.content))
            avatar = avatar.resize((110, 110));
            bigsize = (avatar.size[0] * 3, avatar.size[1] * 3)
            mask = Image.new('L', bigsize, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + bigsize, fill=255)
            mask = mask.resize(avatar.size, Image.ANTIALIAS)
            avatar.putalpha(mask)

            output = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
            output.putalpha(mask)
            output.save('avatar.png')

            fundo = Image.open('bemvindonovo.png')
            fonte = ImageFont.truetype('Technoma.otf', 30)
            escrever = ImageDraw.Draw(fundo)
            escrever.text(xy=(165, 45), text=member.name, fill=(211, 95, 0), font=fonte, align="center")

            fundo.paste(avatar, (39, 8), avatar)
            fundo.save('toperzon.png')
            await channelmr.send(file=discord.File(fp="toperzon.png"))
            await channelmr.send('Seja Bem-Vindo ' + member.mention)
        except:
            pass
@client.event
async def on_member_remove(member):
    embedsaida = discord.Embed(
        title=None,
        color=amarelo,
        description=member.mention + ' Saiu do Servidor'
    )
    embedsaida.set_author(name='🤔 Saiu do Servidor')
    embedsaida.set_footer(text='se não quer ficar aqui, saia mesmo :v')
    try:
        try:
            channel = discord.utils.find(lambda c: c.name == '🔀entrada-e-saida')
            await channel.send_message(embed=embedsaida)
        except:
            canaldomr = discord.utils.find(lambda c: c.name == '💥inferno-dos-bots')
            await canaldomr.send_message(embed=embedsaida)
    except:
        pass

@client.event
async def on_message(message):
    embedbanidobot = discord.Embed(
        title=None,
        color=amarelo,
        description='' + message.author.mention + '\n'
                                                   'Você Foi Banido Permanentemente de Utilizar o HULLO\n'
                                                   'Você não poderá Utilizar meus Comandos'
    )
    embedbanidobot.set_author(name= 'Banimento')
    embedbanidobot.set_footer(text= 'que pena :(')
    errorembedpermi = discord.Embed(
        title=None,
        color=vermelho,
        description='Você não tem permissão para executar esse comando',
    )
    errorembedpermi.set_author(name='Error')
    errorembedpermi.set_thumbnail(url='http://pizzarialukas.com.br/app/webroot/img/erro.png')
    boterrorembedpermi = discord.Embed(
        title=None,
        color=vermelho,
        description='O Bot não tem permissão para executar essa ação',
    )
    boterrorembedpermi.set_author(name='Error')
    boterrorembedpermi.set_thumbnail(url='http://pizzarialukas.com.br/app/webroot/img/erro.png')

#EVAL, Infuncional

    if message.content.lower().startswith(prefix+"eval"):
        if message.author.id == 369962464613367811:
          try:
            messagem = await message.channel(message.channel, str(eval(message.content[7:])))
            await messagem.add_reaction("🤔")
          except Exception as e:
              messagem = await message.channel.send(repr(e))
              await messagem.add_reaction("😅")
        else:
            await message.channel.send(embed=errorembedpermi)

#Jogos
    #Moeda
    if message.content.lower().startswith(prefix + 'moeda'):
        if message.author.id in bp:
            return await message.channel.send(message.channel, embed=embedbanidobot)
        choice = random.randint(1, 2)
        if choice == 1:
            await message.add_reaction('😀')
        if choice == 2:
            await message.add_reaction('👑')

    #Verdade ou Mentira

    if message.content.lower().startswith(prefix + 'vm'):
        if message.author.id in bp:
            return await message.channel.send(embed=embedbanidobot)
        choice = random.randint(1,2)
        if choice == 1:
            msg1 = await message.channel.send(message.content[5:])
            await msg1.add_reaction(':errado:490653378423291933')
            await message.delete()
        if choice == 2:
            msg2 = await message.channel.send(message.content[5:])
            await msg2.add_reaction(':correto:490653354272358410')
            await message.delete()

    #Perfil

    if message.content.lower().startswith(prefix + 'perfil'):
        if message.author.id in bp:
            return await message.channel.send(embed=embedbanidobot)
        url = requests.get(message.author.avatar_url)
        avatar = Image.open(BytesIO(url.content))
        avatar = avatar.resize((160, 160));
        bigsize = (avatar.size[0] * 3, avatar.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(avatar.size, Image.ANTIALIAS)
        avatar.putalpha(mask)

        output = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
        output.putalpha(mask)
        output.save('perfilavatar.png')

        fundo = Image.open('perfil.png')
        fonte = ImageFont.truetype('Technoma.otf', 30)
        escrever = ImageDraw.Draw(fundo)
        escrever.text(xy=(20, 225), text=message.author.name, fill=(211, 95, 0), font=fonte, align="center")
        escrever.text(xy=(20, 270), text="Rep: 000", fill=(211, 95, 0), font=fonte, align="center")
        escrever.text(xy=(20, 313), text="Coins: 000", fill=(211, 95, 0), font=fonte, align="center")
        fundo.paste(avatar, (26, 30), avatar)
        fundo.save('perfilpronto.png')
        await message.channel.send(file=discord.File(fp="perfilpronto.png"))
    #Ship

    if message.content.lower().startswith(prefix + 'ship'):
        if message.author.id in bp:
            return await message.channel.send(embed=embedbanidobot)
        url = requests.get(message.mentions[1].avatar_url)
        avatar = Image.open(BytesIO(url.content))
        avatar = avatar.resize((50, 50));
        bigsize = (avatar.size[0] * 3, avatar.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(avatar.size, Image.ANTIALIAS)
        avatar.putalpha(mask)

        output = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
        output.putalpha(mask)
        output.save('shipavatar1.png')

        url2 = requests.get(message.mentions[0].avatar_url)
        avatar2 = Image.open(BytesIO(url2.content))
        avatar2 = avatar2.resize((50, 50));
        bigsize2 = (avatar.size[0] * 3, avatar2.size[1] * 3)
        mask2 = Image.new('L', bigsize2, 0)
        draw2 = ImageDraw.Draw(mask2)
        draw2.ellipse((0, 0) + bigsize2, fill=255)
        mask2 = mask2.resize(avatar2.size, Image.ANTIALIAS)
        avatar2.putalpha(mask2)

        output2 = ImageOps.fit(avatar2, mask2.size, centering=(0.5, 0.5))
        output2.putalpha(mask2)
        output2.save('shipavatar2.png')


        fundo = Image.open('novo ship.png')
        fonte = ImageFont.truetype('Technoma.otf', 25)
        fonte2 = ImageFont.truetype('Technoma.otf', 40)
        escrever = ImageDraw.Draw(fundo)
        escrever.text(xy=(60, 50), text=message.mentions[1].name, fill=(211, 95, 0), font=fonte, align="center")
        escrever.text(xy=(60, 130), text=message.mentions[0].name, fill=(211, 95, 0), font=fonte, align="center")
        ship = random.randint(1, 4)
        if ship == 1:
            escrever.text(xy=(135, 82), text='20%', fill=(255, 255, 255), font=fonte2, align="center")
        if ship == 2:
            escrever.text(xy=(135, 82), text='45%', fill=(255, 255, 255), font=fonte2, align="center")
        if ship == 3:
            escrever.text(xy=(135, 82), text='65%', fill=(255, 255, 255), font=fonte2, align="center")
        if ship == 4:
            escrever.text(xy=(135, 82), text='99%', fill=(255, 255, 255), font=fonte2, align="center")
        fundo.paste(avatar, (5, 34), avatar2)
        fundo.paste(avatar2, (5, 120), avatar)
        fundo.save('shipinho.png')
        await message.channel.send(file=discord.File(fp="shipinho.png"))
#Utilidades
    #BotInfo
    if message.content.lower().startswith(prefix + 'botinfo'):
        if message.author.id in bp:
            return await client.send_message(message.channel, embed=embedbanidobot)
        embedbotinfo = discord.Embed(
            title=None,
            color=amarelo,
            description=None
        )
        embedbotinfo.set_author(name='🤔 Minhas Informaçoes')
        embedbotinfo.add_field(name='Meu Criador:',value='jo0hn#3931')
        embedbotinfo.add_field(name='Meu Nome:',value=client.user.name)
        embedbotinfo.add_field(name='Online em:', value=(str(len(client.guilds))) + ' Servers')
        embedbotinfo.add_field(name='Usuários:', value=str(len(set(client.get_all_members()))) + ' usuarios')
        embedbotinfo.add_field(name='Meu Niver:', value='01/06/2018')
        embedbotinfo.add_field(name='Ultima Att:',value='16/09/2018')
        embedbotinfo.add_field(name='Programado em:',value='Py')
        embedbotinfo.add_field(name='Biblioteca',value='discord.py Rewrite')
        embedbotinfo.set_thumbnail(url=client.user.avatar_url)
        embedbotinfo.set_footer(text='2018 © Hullo')
        await message.channel.send(embed=embedbotinfo)

    #Sugestão

    if message.content.lower().startswith(prefix + "sugestao"):
        if message.author.id in bp:
            return await client.send_message(message.channel, embed=embedbanidobot)
        server = client.get_guild(464919864570806297)
        channell = discord.utils.find(lambda c: c.id == 464924857809764372, server.channels)
        embedsugestao = discord.Embed(
            title=None,
            color=amarelo,
            description="Sugestão enviada por: " + message.author.name + '\n'
                        "Do Servidor: " + message.guild.name + '\n'
                        "Sugestão: " + '``' + message.content[10:] + '``'
        )
        embedsugestao.set_author(name='🤔 Sugestão')
        embedsugestao.set_footer(text='2018 © Hullo')
        embedsugestaoserver = discord.Embed(
            title=None,
            color=amarelo,
            description="Sugestão Enviada"
        )
        embedsugestaoserver.set_author(name='🤔 Sugestão')
        embedsugestaoserver.set_footer(text='2018 © Hullo')
        msgsuges = await channell.send(embed=embedsugestao)
        await message.channel.send(embed=embedsugestaoserver)
        try:
            await message.delete()
        except:
            pass
        await msgsuges.add_reaction('👍')
        await msgsuges.add_reaction('👎')
        await msgsuges.add_reaction('❤')

    #Mention

    if message.content.lower().startswith("<@431800868585865219>"):
        if message.author.id in bp:
            return await message.channel.send(embed=embedbanidobot)
        embedmention = discord.Embed(
            title=None,
            color=amarelo,
            description="🤔 Meu Prefix nesse Servidor é ``" + prefix + "``" + " e Meu Comando de Ajuda ``" + prefix + "ajuda``"
        )
        embedmention.set_author(name='🤔 Hullo!!')
        embedmention.set_footer(text='2018 © Hullo')
        await message.channel.send(embed=embedmention)
        try:
            await message.delete()
        except:
            pass

    #Ajuda

    if message.content.lower().startswith(prefix + "ajuda"):
        if message.author.id in bp:
            return await message.channel.send(embed=embedbanidobot)
        embedserverajuda = discord.Embed(
            title=None,
            color=amarelo,
            description='📮 Enviei meus comandos para o seu privado'
        )
        embedserverajuda.set_author(name='🤔 Hullo!! - Ajuda 🤔')
        embedserverajuda.set_footer(text='2018 © Hullo')
        await message.channel.send(embed=embedserverajuda)
        global embednajuda
        embednajuda = discord.Embed(
            title=None,
            color=amarelo,
            description='Clique no Emoji\n'
                        'Para Abrir meus Comandos\n'
                        '    \n'
                        '🎮 - Jogos\n'
                        '🥊 - Moderação\n'
                        '🤔 - Utilidades\n'
                        '🎵 - Musica'
        )
        embednajuda.set_author(name='🤔 Hullo!! - Ajuda 🤔')
        embednajuda.set_footer(text='2018 © Hullo')
        global botmsg
        botmsg = await message.author.send(embed=embednajuda)
        global msg_id
        msg_id = botmsg.id
        await botmsg.add_reaction("🎮")
        await botmsg.add_reaction("🥊")
        await botmsg.add_reaction("🤔")
        await botmsg.add_reaction("🎵")
        await botmsg.add_reaction("⬅")
        global embednajudajogo
        embednajudajogo = discord.Embed(
            title=None,
            color=amarelo,
            description='Meus Joguinhos :D\n'
                        '   \n'
                        '💸 !!Moeda - Cara ou Coroa\n'
                        '🗣️ !!ss {Pergunta} - Ele te responde :V\n'
                        '🗣️ !!addss {Pergunta} - Add uma Resposta ao !!ss\n '
                        '🗣️ !!ship {@user} {@user} - Ship❗'
                        '   \n'
        )
        embednajudajogo.set_author(name= '🎮 Hullo!! - Jogo 🎮')
        embednajudajogo.set_footer(text='2018 © Hullo')
        global embednajudamoderacao
        embednajudamoderacao = discord.Embed(
            title=None,
            color=amarelo,
            description='Meus Comandos de Moderação :D\n'
                        '   \n'
                        '🥊 !!Kick (player) (motivo) - Expulsar pessoas :D\n'
                        '🥊 !!Ban (player) (motivo) - Banir pessoas :D\n'
                        '🥊 !!Mutar (player) (motivo) - Mutar pessoas :D'
                        '   \n'
        )
        embednajudamoderacao.set_author(name= '🥊 Hullo!! - Jogo 🥊')
        embednajudamoderacao.set_footer(text='2018 © Hullo')
        global embednajudautilidades
        embednajudautilidades = discord.Embed(
            title=None,
            color=amarelo,
            description='Minha Utilidades :D\n'
                        '   \n'
                        '🤔 !!Avatar - Seu Avatar (ou mention)\n'
                        '🤔 !!ServerInfo - Info do Server\n'
                        '🤔 !!Perfil - Suas Informações\n'
                        '🤔 !!BotInfo - Minha Informações\n'
                        '🤔 !!Info - Minha Informações\n'
        )
        embednajudautilidades.set_author(name= '🤔 Hullo!! - Utilidades 🤔')
        embednajudautilidades.set_footer(text='2018 © Hullo')
        global embednajudamusica
        embednajudamusica = discord.Embed(
            title=None,
            color=amarelo,
            description='Meus Comandos de Musica :D\n'
                        '   \n'
                        '🎵 Infelizmente\n'
                        '🎵 Pra eu poder ficar 24hr\n'
                        '🎵 Não posso ter musica ;-;\n'
                        '   '
        )
        embednajudamusica.set_author(name='🎵 Hullo!! - Musica 🎵')
        embednajudamusica.set_footer(text='2018 © Hullo')
        global ajudamsg
        ajudamsg = botmsg.id

        global sirajudamsg
        sirajudamsg = message.author

    #Shards

    if message.content.lower().startswith(prefix+'shard'):
        tutorial = '\n'.join(f'ID {shard} -- **' + str(round(client.latencies[shard][1] * 1000)) + '**ms'for shard in client.shards)
        await message.channel.send("**Shards Rodando**\n"+tutorial)

    #Avatar

    if message.content.lower().startswith(prefix + 'avatar'):
        if message.author.id in bp:
            return await message.channel.send(embed=embedbanidobot)
        try:
            mentionavatar = message.mentions[0]
            embedavatar2 = discord.Embed(
                title=None,
                color=amarelo,
                description=None
            )
            embedavatar2.set_image(url=mentionavatar.avatar_url)
            embedavatar2.set_author(name='Avatar do ' + mentionavatar.name)
            embedavatar2.set_footer(text='reaja ao avatar do ' + mentionavatar.name)
            msgavatarsecond = await message.channel.send(embed=embedavatar2)
            await msgavatarsecond.add_reaction('👍')
            await msgavatarsecond.add_reaction('👎')
            await msgavatarsecond.add_reaction('❤')
        except:
            embedavatar = discord.Embed(
                title=None,
                color=amarelo,
                description=None
            )
            embedavatar.set_image(url=message.author.avatar_url)
            embedavatar.set_author(name='Seu Avatar - ' + message.author.name)
            embedavatar.set_footer(text='reaja ao avatar do ' + message.author.name)
            msgavatarfirst = await message.channel.send(embed=embedavatar)
            await msgavatarfirst.add_reaction('👍')
            await msgavatarfirst.add_reaction('👎')
            await msgavatarfirst.add_reaction('❤')

    #Servers
    if message.content.lower().startswith(prefix+'servers'):
        if message.author.id in bp:
            return await message.channel.send(embed=embedbanidobot)
        servidores = '\n'.join([s.name for s in client.guilds])
        await message.channel.send(servidores)
    #info

    if message.content.lower().startswith(prefix + 'info'):
        if message.author.id in bp:
            return await message.channel.send(embed=embedbanidobot)
        usuario = message.author
        entrou_servidor = str(usuario.joined_at.strftime("%d/%m/20%y - %H:%M:%S"))
        conta_criada = str(usuario.created_at.strftime("%d/%m/20%y - %H:%M:%S"))
        apelido = usuario.display_name
        #jogando = str(usuario.activity.name).replace("None", "Nada")
        cargos = ",".join([r.name for r in usuario.roles if r.name != "@everyone"])
        status = str(usuario.status).replace("streaming", "streamando").replace("online", "Online").replace("dnd",
                                                                                                                "Ocupado").replace(
            "idle", "Ausente").replace("offline", "Offline")
        embedinfo = discord.Embed(
            title=None,
            color=amarelo,
            description=None
        )
        embedinfo.set_author(name='Suas Informações', icon_url=message.author.avatar_url)
        embedinfo.add_field(name='Nome:',value=usuario.name)
        embedinfo.add_field(name='ID:',value=usuario.id)
        embedinfo.add_field(name='Tag:',value=usuario.discriminator)
        embedinfo.add_field(name='Apelido:',value=apelido)
        embedinfo.add_field(name='Maior Cargo:',value=usuario.top_role)
        embedinfo.add_field(name='Cor:',value=usuario.color)
        embedinfo.add_field(name='Jogando:',value="Em Breve")
        embedinfo.add_field(name='Status:',value=status)
        embedinfo.add_field(name='Entrou em:',value=entrou_servidor)
        embedinfo.add_field(name='Conta Criada:',value=conta_criada)
        embedinfo.set_footer(text='2018 © Hullo')
        embedinfo.set_thumbnail(url=usuario.avatar_url)
        await message.channel.send(embed=embedinfo)

    #ServerInfo

    if message.content.lower().startswith(prefix + 'serverinfo'):
        if message.author.id in bp:
            return await message.channel.send(embed=embedbanidobot)
        server = message.guild
        embedserverinfo = discord.Embed(
            title=None,
            color=amarelo,
            description=None
        )
        embedserverinfo.set_author(name='Informações do servidor ' + server.name, icon_url=server.icon_url)
        embedserverinfo.add_field(name='Nome:', value=server.name)
        embedserverinfo.add_field(name='ID:', value=server.id)
        embedserverinfo.add_field(name='Dono:', value=server.owner)
        embedserverinfo.add_field(name='Criado:', value=server.created_at.strftime("%d %b %Y %H:%M"))
        embedserverinfo.add_field(name='Região:', value=server.region)
        embedserverinfo.add_field(name='Cargos:', value=len(server.roles))
        embedserverinfo.add_field(name='Membros:', value=message.guild.member_count, inline=True)
        embedserverinfo.add_field(name='Bots:', value=len([user.mention for user in message.guild.members if user.bot]))
        embedserverinfo.add_field(name='<:online:472579974197411850> online', value=len([m.status for m in message.guild.members if m.status == discord.Status.online]))
        embedserverinfo.add_field(name='<:ocupado:472580211536297985> ocupado', value=len([m.status for m in message.guild.members if m.status == discord.Status.do_not_disturb]))
        embedserverinfo.add_field(name='<:idle:472580185984860160> ausente', value=len([m.status for m in message.guild.members if m.status == discord.Status.idle]))
        embedserverinfo.add_field(name='<:offline:472580249146884097> offline', value=len([m.status for m in message.guild.members if m.status == discord.Status.offline]))
        embedserverinfo.set_footer(text='2018 © Hullo')
        embedserverinfo.set_thumbnail(url=server.icon_url)
        await message.channel.send(embed=embedserverinfo)

    #Falar

    if message.content.lower().startswith(prefix + 'falar'):
        if message.author.id in bp:
            return await client.send_message(message.channel, embed=embedbanidobot)
        embedfalar = discord.Embed(
            title=None,
            color=amarelo,
            description=message.content[8:]
        )
        embedfalar.set_footer(text='Mensagem enviada por ' + message.author.name, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embedfalar)

    #ping

    if message.content.lower().startswith(prefix + 'ping'):
        if message.author.id in bp:
            return await message.channel.send(embed=embedbanidobot)
        #d = datetime.utcnow() - message.timestamp
        #s = d.seconds * 1000 + d.microseconds // 1000
        message.channel.send('🏓 Pong! 0ms')#.format)(s))

    #SS

    if message.content.lower().startswith(prefix + 'ss'):
        if message.author.id in bp:
            return await message.channel.send(embed=embedbanidobot)
        pergunta = message.content[5:]
        r = requests.get('https://dogewebsite.glitch.me/api/v1/responses/get-question&question=' + pergunta)
        resposta = json.loads(r.text)
        lista = ["@here", "@everyone"]
        await message.channel.send('{}, {}'.format(message.author.mention, resposta['response']))

    #ADDSS

    if message.content.lower().startswith(prefix + 'addss'):
        if message.author.id in bp:
            return await message.channel.send(embed=embedbanidobot)
        await message.channel.send('Quando alguem me Perguntar "{}", Oque eu devo Responder?? '.format(
            message.content[8:]))

        def pred(m):
            return m.author == message.author and m.channel == message.channel
        lololo = await client.wait_for('message', check=pred)
        lista = ["@here", "@everyone"]
        for palavra in lista:
            if palavra in lololo.content.lower():
                await message.channel.send('😅 Você não pode Adicionar uma mensagem que contenha o termo "here" ou "everyone"!!')
                return
        r = requests.get('https://dogewebsite.glitch.me/api/v1/responses/set-response&question={}&answer={}'.format(
            message.content[8:], lololo.content[0:]
        ))
        await message.channel.send('Sucesso :D,\n'
                                   'Quando Alguem me Perguntar: {}\n'
                                   'Eu Irei Responder: {}'.format(message.content[8:], lololo.content[0:]))
        resposta = json.loads(r.text)

    #AVISO INFUNCIONAL

    if message.content.lower().startswith(prefix + 'aviso'):
        if not message.author.server_permissions.administrator:
            return await message.channel.send(embed=errorembedpermi)
        avisoembed = discord.Embed(
            title=None,
            color=amarelo,
            description=message.content[8:]
        )
        avisoembed.set_author(name='📣 Aviso 📣')
        avisoembed.set_footer(text='Aviso enviado por ' + message.author.name)
        await message.channel.send(embed=avisoembed)
        await message.delete()

#Moderação

    #Mutar

    if message.content.lower().startswith(prefix + 'mutar'):
        if message.author.id in bp:
            return await client.send_message(message.channel, embed=embedbanidobot)
        if not message.author.guild_permissions.administrator:
            return await client.send_message(message.channel,embed=errorembedpermi)
        mention1 = message.mentions[0]
        cargo = discord.utils.get(message.author.guild.roles,name='Mutado')
        log = discord.utils.find(lambda c: c.name == 'log', message.author.guild.channels)
        muteembed = discord.Embed(
            title=None,
            color=amarelo,
            description='Nome: ' + mention1.name + '\n'
                                                   'Motivo: ' + message.content[30:] + '\n'
                                                                                       'Por: ' + message.author.name
        )
        muteembed.set_author(name='Hullo!! - Mute', icon_url=message.author.avatar_url)
        muteembed.set_thumbnail(
            url='https://images.vexels.com/media/users/3/134546/isolated/preview/b1b61276fef1c4a683aabaa53833c7ca-emoticon-emoji-rosto-triste-by-vexels.png')
        muteembed.set_footer(text='2018 © Hullo')
        muteembedlog = discord.Embed(
            title=None,
            color=amarelo,
            description='Nome: ' + mention1.name + '\n'
                                                   'Motivo: ' + message.content[30:] + '\n'
                                                                                       'Por: ' + message.author.name
        )
        muteembedlog.set_author(name='Hullo!! - Mute', icon_url=message.author.avatar_url)
        muteembedlog.set_thumbnail(
            url='https://images.vexels.com/media/users/3/134546/isolated/preview/b1b61276fef1c4a683aabaa53833c7ca-emoticon-emoji-rosto-triste-by-vexels.png')
        muteembedlog.set_footer(text='2018 © Hullo')

        await mention1.add_roles(cargo)
        await message.channel.send(embed=muteembed)
        await log.send(embed=muteembedlog)
    #if message.content.lower().startswith(prefix + 'unmute'):
        #mention1 = message.mentions[0]
        #await mention1.remove_roles('Mutado')

    #Ban

    if message.content.lower().startswith(prefix + 'ban'):
        if not message.author.guild_permissions.administrator:
            return await message.channel.send(embed=errorembedpermi)

        mentionban = message.mentions[0]
        embedban = discord.Embed(
            title=None,
            color=amarelo,
            description='Usuário: ' + mentionban.name + '\n'
                    'Motivo: ' + message.content[28:] + '\n'
                    'Staff: ' + message.author.name + '\n'
        )
        embedban.set_author(name='Banimento - ' + mentionban.name, icon_url='http://bit.ly/2JEDsjf')
        embedban.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/1/14/Ban_sign.png')
        embeddmban = discord.Embed(
            title=None,
            color=amarelo,
            description='Você foi banido do Servidor ' + message.author.guild.name + '\n' 
                        'Motivo: ' + message.content[28:] + '\n'
                        'Staff: ' + message.author.name
        )
        embeddmban.set_author(name='Banimento', icon_url='http://bit.ly/2JEDsjf')
        logban = discord.utils.find(lambda c: c.name == 'log', message.author.guild.channels)
        await mentionban.send(embed=embeddmban)
        try:
            await mentionban.ban()
        except:
            await message.channel.send(embed=boterrorembedpermi)
            return
        try:
            await logban.send(embed=embedban)
        except:
            pass
        try:
            await message.channel.send(embed=embedban)
        except:
            pass
    #Kick

    if message.content.lower().startswith(prefix + 'kick'):
        if not message.author.guild_permissions.administrator:
            return await message.channel.send(embed=errorembedpermi)
        mentionkick = message.mentions[0]
        embedkick = discord.Embed(
            title=None,
            color=amarelo,
            description='Usuário: ' + mentionkick.name + '\n'
                        'Motivo: ' + message.content[28:] + '\n'
                        'Staff: ' + message.author.name
        )
        embedkick.set_author(name='Kickado - ' + mentionkick.name, icon_url='http://bit.ly/2JEDsjf')
        embedkick.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/1/14/Ban_sign.png')
        embeddmkick = discord.Embed(
            title=None,
            color=amarelo,
            description='Você foi kickado do Servidor ' + message.author.guild.name + '\n' 
                        'Motivo: ' + message.content[28:] + '\n'
                        'Staff: ' + message.author.name
        )
        embeddmkick.set_author(name='Kick', icon_url='http://bit.ly/2JEDsjf')
        logkick = discord.utils.find(lambda c: c.name == 'log', message.author.guild.channels)
        await mentionkick.send(embed=embeddmkick)
        try:
            await mentionkick.kick()
        except:
            await message.channel.send(embed=boterrorembedpermi)
            return
        try:
            await logkick.send(embed=embedkick)
        except:
            pass
        try:
            await message.channel.send(embed=embedkick)
        except:
            pass

    @client.event
    async def on_reaction_add(reaction, user):
        msg = reaction.message
        chat = reaction.message.channel
        if reaction.emoji == "🎮" and msg.id == msg_id:
            try:
                await botmsg.edit(embed=embednajudajogo)
            except:
                pass
        if reaction.emoji == "⬅" and msg.id == msg_id:
            try:
                await botmsg.edit(embed=embednajuda)
            except:
                pass
        if reaction.emoji == "🥊" and msg.id == msg_id:
            try:
                await botmsg.edit(embed=embednajudamoderacao)
            except:
                pass
        if reaction.emoji == "🎵" and msg.id == msg_id:
            try:
                await botmsg.edit(embed=embednajudamusica)
            except:
                pass
        if reaction.emoji == "🤔" and msg.id == msg_id:
            try:
                await botmsg.edit(embed=embednajudautilidades)
            except:
                pass

@client.event
async def on_message_edit(before, after):
    try:
        logserverdomr = discord.utils.find(lambda c: c.name == '💥inferno-dos-bots', before.guild.channels)
        embededit = discord.Embed(
            title=None,
            color=amarelo,
            description=None,
        )
        embededit.set_author(name='Mensagem Editada - ' + before.author.name, icon_url=before.author.avatar_url)
        embededit.add_field(name='Autor:', value=after.author.name, inline=False)
        embededit.add_field(name='Canal:', value=before.channel.mention, inline=False)
        embededit.add_field(name='Antes:', value=before.content, inline=False)
        embededit.add_field(name='Depois:', value=after.content, inline=False)
        embededit.set_footer(text='2018 © Hullo!!')
    except:
        pass
    try:
        log = discord.utils.find(lambda c: c.name == 'log', before.guild.channels)
        await log.send(embed=embededit)
    except:
        try:
            await logserverdomr.send(embed=embededit)
        except:
            pass
        pass

@client.event
async def on_message_delete(message):
    logserverdomr = discord.utils.find(lambda c: c.name == '💥inferno-dos-bots', message.guild.channels)
    embeddelet = discord.Embed(
        title=None,
        color=amarelo,
        description=None,
    )
    embeddelet.set_author(name='Mensagem Deletada - ' + message.author.name)
    embeddelet.add_field(name='Autor:', value=message.author.name, inline=False)
    embeddelet.add_field(name='Canal:', value=message.channel.mention, inline=False)
    embeddelet.add_field(name='Msg:', value='```' + message.content + '```', inline=False)
    embeddelet.set_footer(text='2018 © Hullo!!')
    try:
        log = discord.utils.find(lambda c: c.name == 'log', message.guild.channels)
        await log.send(embed=embeddelet)
    except:
        try:
            await logserverdomr.send(embed=embeddelet)
        except:
            pass
        pass
client.run(token)
