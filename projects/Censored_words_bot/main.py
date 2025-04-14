import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned, help_command=None, intents=disnake.Intents.all(), test_guilds=[870303650596155464])

CENSORED_WORDS = ["пицца с ананасом"]

@bot.event
async def on_ready():
    print(f"{bot.user} is online")

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    for content in message.content.split():
        for censor in CENSORED_WORDS:
            if content.lower() == censor:
                await message.delete()
                await message.channel.send(f"{message.author.mention} такие сообщения запрещены!")

@bot.event
async def on_command_error(ctx, error):
    print(error)

    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author}, не достаточно прав!")
    elif isinstance(error, commands.UserInputError):
        await ctx.send(embed=disnake.Embed(
            description=f"Правильное использование команды: '{ctx.prefix}{ctx.command.name}' ({ctx.command.brief})\nExample: {ctx.prefix}{ctx.command.usage}"
        ))




@bot.command()

@commands.has_permissions(kick_members=True, administrator=True)
async def kick(ctx, member: disnake.Member, *, reason="Нарушил правила!"):
    await ctx.send(f"{member.mention} был исключен по инициативе {ctx.author.mention}")
    await member.kick(reason=reason)
    await ctx.message.delete()

@bot.slash_command(description="Калькулятор. Простой.")

async def calc(inter, a: int, oper: str, b: int):
    if oper == "+":
        result = a + b
    elif oper == "-":
        result = a - b
    else:
        result = "Неверно."

    await inter.send(str(result))

bot.run("token")
