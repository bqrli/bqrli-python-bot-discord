# Developer: who i am?#5867
# Bot prefix: '?':
# Help developing: vk.com/sanyadeveeeee999
# Vongex: vk.com/vongexcloudru
import discord
from discord import colour
from discord.ext import commands
from discord.flags import Intents
from discord_components import DiscordComponents, ButtonStyle, Button

Vongex = commands.Bot(command_prefix = '?', intens = discord.Intents.all())

@Vongex.event
async def on_ready():
    DiscordComponents(Vongex)
    await Vongex.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.watching, name="СТРИМ АГЕРЫ ПАРК"))
    print("Функционал бота: В скором времени!")

@Vongex.command()
async def ticket(ctx):    
    embed = discord.Embed(title = 'Выберите действие ниже↓',timestamp = ctx.message.created_at)
    await ctx.send(embed=embed, components = [Button(style = ButtonStyle.green, label = 'Создать тикет'), 
                                                Button(style = ButtonStyle.red, label = 'Удалить тикет')])

    responce = await Vongex.wait_for('button_click', check = lambda message: message.author == ctx.author)

    if responce.component.label == 'Создать тикет':
        await responce.respond(content = 'Ваш тикет создан!')
        # responce.component.disabled = False
        
    elif responce.component.label == 'Удалить тикет':
        await responce.respond(content = 'Ваш тикет удален')

@Vongex.command(aliases=[ 'purge', 'очистить' ])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int): # По дефолту value стоит None (Чтобы поставить другое, читайте документацию)
    await ctx.channel.purge( limit = amount)

    await ctx.send(embed = discord.Embed(description = f':white_check_mark: Удалено {amount} сообщений'))


@Vongex.command()
async def тест(ctx):
    await ctx.send('I am work blyat ☺')

Vongex.run("ODk2OTU4ODQyNTMxODgwOTcw.YWOsBA.o4upk1ui44XErFWSmnPrwkPnW2k")