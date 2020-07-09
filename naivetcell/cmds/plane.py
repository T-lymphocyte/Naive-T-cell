import discord
from discord.ext import commands
from discord.ext.commands import Bot
import json
from core.classes import Cog_Extension
with open("./cmds/setting.json", mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class plane(Cog_Extension):
    @commands.command()
    async def info_boeing(self, ctx, string):
        if string == '747':
            embed=discord.Embed()
            embed.add_field(name=string, value=jdata['747'], inline=False)
            await ctx.send(embed=embed)
        elif string == '747400':
            embed=discord.Embed()
            embed.add_field(name=string, value=jdata['747400'], inline=False)
            await ctx.send(embed=embed)
        elif string == '747800':
            embed=discord.Embed()
            embed.add_field(name=string, value=jdata['747800'], inline=False)
            await ctx.send(embed=embed)
        elif string == '747dreamlifter':
            embed=discord.Embed()
            embed.add_field(name=string, value=jdata['747dreaml'], inline=False)
            await ctx.send(embed=embed)
        elif string == '737':
            embed=discord.Embed()
            embed.add_field(name=string, value=jdata['7377'], inline=False)
            await ctx.send(embed=embed)
        elif string == '737max':
            embed=discord.Embed()
            embed.add_field(name=string, value=jdata['737max'], inline=False)
            await ctx.send(embed=embed)
        elif string == '757':
            embed=discord.Embed()
            embed.add_field(name=string, value=jdata['7572300'], inline=False)
            await ctx.send(embed=embed)
        elif string == '767':
            embed=discord.Embed()
            embed.add_field(name=string, value=jdata['767400ER'], inline=False)
            await ctx.send(embed=embed)
        elif string == '777300ER':
            embed=discord.Embed()
            embed.add_field(name=string, value=jdata['777300Er'], inline=False)
            await ctx.send(embed=embed)
        elif string == '777X(ex)':
            embed=discord.Embed()
            embed.add_field(name=string, value=jdata['777xE'], inline=False)
            await ctx.send(embed=embed)
        elif string == '777X(fo)':
            embed=discord.Embed()
            embed.add_field(name=string, value=jdata['777xF'], inline=False)
            await ctx.send(embed=embed)
        elif string == '787':
            embed=discord.Embed()
            embed.add_field(name=string, value=jdata['787'], inline=False)
            await ctx.send(embed=embed)
        elif string == '777200':
            embed=discord.Embed()
            embed.add_field(name=string, value=jdata['777200ErLrF'], inline=False)
            await ctx.send(embed=embed)
        elif string == '777200ER':
            embed=discord.Embed()
            embed.add_field(name=string, value=jdata['777200ErLrF'], inline=False)
            await ctx.send(embed=embed)
        elif string == '777200LR':
            embed=discord.Embed()
            embed.add_field(name=string, value=jdata['777200ErLrF'], inline=False)
            await ctx.send(embed=embed)
        elif string == '777F':
            embed=discord.Embed()
            embed.add_field(name=string, value=jdata['777200ErLrF'], inline=False)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed()
            embed.add_field(name="invalid model", value="", inline=False)
            await self.bot.say(embed=embed)

    @commands.command()
    async def info_airbus(self, ctx, string):
        if string == '318':
            await ctx.send(jdata['318'])
        elif string == '319':
            await ctx.send(jdata['319'])
        elif string == '320':
            await ctx.send(jdata['319'])
        elif string == '321':
            await ctx.send(jdata['319'])
        elif string == '330':
            await ctx.send(jdata['330'])
        elif string == '340200':
            await ctx.send(jdata['330'])
        elif string == '340300':
            await ctx.send(jdata['330'])
        elif string == '340500':
            await ctx.send(jdata['340'])
        elif string == '340600':
            await ctx.send(jdata['340'])
        elif string == '350':
            await ctx.send(jdata['350'])
        else:
            await ctx.send('unavalible module')
def setup(bot):
    bot.add_cog(plane(bot))