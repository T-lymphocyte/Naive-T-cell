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
            await ctx.send(jdata['747'])
        elif string == '747400':
            await ctx.send(jdata['747400'])
        elif string == '747800':
            await ctx.send(jdata['747800'])
        elif string == '747dreamlifter':
            await ctx.send(jdata['747dreaml'])
        elif string == '737':
            await ctx.send(jdata['7377'])
        elif string == '737max':
            await ctx.send(jdata['737max'])
        elif string == '757':
            await ctx.send(jdata['7572300'])
        elif string == '767':
            await ctx.send(jdata['767400ER'])
        elif string == '777300ER':
            await ctx.send(jdata['777300Er'])
        elif string == '777X(ex)':
            await ctx.send(jdata['777xE'])
        elif string == '777X(fo)':
            await ctx.send(jdata['777xF'])
        elif string == '787':
            await ctx.send(jdata['787'])
        elif string == '777200':
            await ctx.send(jdata['777200ErLrF'])
        elif string == '777200ER':
            await ctx.send(jdata['777200ErLrF'])
        elif string == '777200LR':
            await ctx.send(jdata['777200ErLrF'])
        elif string == '777F':
            await ctx.send(jdata['777200ErLrF'])
        else:
            await ctx.send('invalid module')

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