import os
import discord
from discord.ext import commands
from random import randint as salla
from kal import kal

intents = discord.Intents.all()
Bot = commands.Bot(command_prefix="!fm ", intents=intents)
token = os.environ['bakma_lan_gevşek']


def zar_at():
    return salla(0, 6)


"""
@Bot.event
async def on_member_join(member):
    channel = await Bot.fetch_channel (merhaba)
    await channel.send(f"{member.mention} aramıza katıldı, hoş geldi :)")
    print(f"{member} aramıza katıldı, hoş geldi :)")


@Bot.event
async def on_member_remove(member):
    channel = await Bot.fetch_channel(merhaba)
    await channel.send(f"{member.mention} aramızdan ayrıldı, güle güle :(")
    print(f"{member} aramızdan ayrıldı, güle güle :(")
"""


@Bot.event
async def on_ready():
    print("hello world I was open")


@Bot.command()
async def kurallar(ctx):
    await ctx.send("yok")


@Bot.command(aliases=["nasılsın"])
async def naber(ctx):
    await ctx.send("iyi, sen ?")


@Bot.command()
async def iyi(ctx, args1):
    if "misin" in args1:
        await ctx.send("evet iyiyim, peki sen nasılsın ?")


@Bot.command()
async def sa(ctx):
    await ctx.send("as gardaş")


@Bot.command()
async def eyvallah(ctx):
    await ctx.send("sana da eyvallah")


@Bot.command()
async def oyun(ctx, args1, args2):
    if "zar" in args1 and "at" in args2:
        await ctx.send(zar_at())
    else:
        await ctx.send("""
    geçerli değer girmediniz, 
geçerli değerler:
        
1- zar at
         """)


@Bot.command()
#@commands.has_permissions(manage_channels=True)| erişim kontrolü
async def sil(ctx, amount=2):
    await ctx.channel.purge(limit=amount)


@Bot.command(aliases=["copy"])
async def kopyala(ctx, amount=1):
    for i in range(amount):
        await ctx.channel.clone()


@Bot.command()
#@commands.has_permissions(kick_members=True)
async def at(ctx, member=discord.Member, *args, reason="Yok"):
    await member.kick(reason=reason)


@Bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *args, reason="Yok"):
    await member.ban(reason=reason)


@Bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    for bans in banned_users:
        user = bans.user
        if (user.name, user.discriminator) == (member_name,
                                               member_discriminator):
            await ctx.send(f"{user} adlı kişinin banı kaldırıldı")
            await ctx.guild.unban(user)
            print(user.name, user.discriminator)
            return


@Bot.command(help="| belirli bir isme sahip ses ya da yazı kanalı açar "
             )  #istenilen isimde kanal oluşturur
async def kanal_aç(
    ctx,
    type="yazı",
    *,
    name=None,
):
    guild = ctx.message.guild
    if name == None:
        await ctx.send(
            "üzgünüm bir isim girmelisin. tekrar dene, mesela bunun gibi: !fm kanal_aç kanal_türü kanal_adı"
        )
    else:
        if type == "yazı":
            await guild.create_text_channel(name)
            await ctx.send(f"{name} isminde bir konuşma kanalı oluşturuldu")
        elif type == "ses":
            await guild.create_voice_channel(name)
            await ctx.send(f"{name} isminde bir ses  kanalı oluşturuldu")
        else:
            await ctx.send(
                f"tür doğru değil lütfen geçerli bir tür giriniz. geçerli türler: \" ses , yazı \""
            )


@Bot.command(help='| belirli bir isme sahip kanalı siler')
async def kanal_sil(ctx, *, name):
    guild = ctx.message.guild
    existing_channel = discord.utils.get(guild.channels, name=name)

    if existing_channel is not None:
        await existing_channel.delete()

    else:
        await ctx.send(f' {name} isminde bir kanal yoktur')


@Bot.tree.command(name="deneme")
async def deneme(interaction: discord.interactions):
    await interaction.response.send_message(f"Hey {interaction.user.mention}! bu bir eğik çizgi komutudur!", ephemeral=True)


@Bot.tree.command(name="söyle")
@discord.app_commands.describe(thing_to_say = "What should I say?")
async def say(interaction: discord.Interaction, thing_to_say: str):
    await interaction.response.send_message(f"{interaction.user.name} said: {thing_to_say}")











kal()
Bot.run(token)
