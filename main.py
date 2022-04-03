import discord
from discord.ext import commands
from grid import gen_grid


with open('token.txt', 'r') as f:
    token = f.read()

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def grid(ctx, top_left_x: int, top_left_y: int, bottom_right_x: int, bottom_right_y: int):
    diff1 = bottom_right_x - top_left_x
    diff2 = bottom_right_y - top_left_y
    if (diff1 * diff2 > 62500):
        return await ctx.send("Area too big")
    gen_grid(top_left_x, top_left_y, bottom_right_x, bottom_right_y)
    embed = discord.Embed(color=ctx.me.color)
    file = discord.File('grid_generator.png')
    embed.set_image(url='attachment://grid_generator.png')
    await ctx.send(embed=embed, file=file)

bot.run(token)
