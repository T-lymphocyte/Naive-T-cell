import discord
from discord.ext import commands
from discord.ext.commands import Bot
import json
from core.classes import Cog_Extension
with open("./cmds/setting.json", mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
class help(Cog_Extension):
    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(title="Help menu(don't click me)", url="https://media.discordapp.net/attachments/626406858462068736/715141085965320222/sot8wsK.gif")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/626406858462068736/715141085965320222/sot8wsK.gif")
        embed.set_author(name=f"seems {ctx.message.author} summoned a help monster.... GRRRR")
        embed.add_field(name="plane info", value="for info of plane commands, type k.plane_help", inline=False)
        embed.add_field(name="Scary waifu", value="think before using. k.waifu ", inline=False)
        embed.add_field(name="Ping", value="just a normal ping command. k.ping", inline=True)
        embed.set_footer(text="owo is op")
        await ctx.send(embed=embed)
    @commands.command()
    async def plane_help(self, ctx):
        embed=discord.Embed(title="Help menu", description="Plane info ")
        embed.set_author(name=f"{ctx.message.author} summoned a plane... wait it's a help monster!! GRRR")
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Boeing_787-8_Dreamliner%2C_All_Nippon_Airways_-_ANA_AN2105773.jpg/435px-Boeing_787-8_Dreamliner%2C_All_Nippon_Airways_-_ANA_AN2105773.jpg")
        embed.add_field(name='command', value='boeing:k.info_boeing [module name], airbus:k.info_airbus [module name]', inline=True)
        embed.add_field(name="list of valid plane-Boeing", value="747,747400,747800,747dreamlifter,737,737max,757,767,777300ER,777X(ex),777X(fo),787,777200,777200ER,777200LR,777F  remarks: (fo)= folded, (ex)=expanded", inline=True)
        embed.add_field(name="list of valid plane-Airbus", value="318,319,320,321,330,340200,340300,340500,340600,350", inline=False)
        embed.set_footer(text="owo is op")
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(help(bot))