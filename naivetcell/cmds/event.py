import discord
from discord.ext import commands
from discord.ext.commands import Bot
import json
from core.classes import Cog_Extension
with open("./cmds/setting.json", mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
class event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(720548103006060566 or 704931737800671242)
        await channel.send(f'{member} join!')
    @commands.Cog.listener()
    async def on_member_leave(self, member):
        channel = self.bot.get_channel(720548103006060566 or 704931737800671242)
        await channel.send(f'{member} left!')
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == 'hello':
            await msg.channel.send('hi')
def setup(bot):
    bot.add_cog(event(bot))