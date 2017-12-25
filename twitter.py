#!/usr/bin/python3
import tweepy
import random
import discord
from discord.ext import commands


auth = tweepy.OAuthHandler("ROyHS7lEAKwJCoLqMX6eKeERd", "UUlfzXATRfeoAI3kXWhgzisY9WN2HHMjrgbZWXm69qQvnFhcib")
auth.set_access_token("944836647396376578-mqT8YzoX3H1bxRI0GSXe4yqDKIUgm2o", "AHwWuk4BibY1Pc0uqg5sqoRZKDnTJzE7jpzyiFcTPtGXj")

api = tweepy.API(auth)

#api.update_status(digits)
def post(message):
    status = api.update_status(message)
    link = "https://twitter.com/DiscordSpeaks/status/{}".format(status.id)
    return link
class twitter:
    """Tweets your message to twitter.com/DiscordSpeaks"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def tweet(self,ctx):
        """Tweets your message to twitter.com/DiscordSpeaks"""

        if len(ctx.message.content) > 7 and len(ctx.message.content) < 288:
            msg = ctx.message.content[6::].replace("nigger","******").replace("fag","***")
            await self.bot.say("Posted!\n{}".format(post(msg)))

        elif len(ctx.message.content) <= 7:
            msg = "`Can't send empty message`"
            await self.bot.say(msg)
        else:
            msg = "`Message too long`"
            await self.bot.say(msg)

    @commands.command()
    async def retweet(self,link):
        """retweets a message to twitter.com/DiscordSpeaks"""
        status_id = link.split("/")[-1]
        retweet = api.retweet(status_id)
        username = retweet.user.screen_name
        link = "https://twitter.com/{}/status/{}".format(username,retweet.id)
        try:
            await self.bot.say("Retweeted!\nhttps://twitter.com/DiscordSpeaks")
        except:
            await self.bot.say("`Invalid link`")
    
    @commands.command(pass_context=True)
    async def reply(self,ctx,link):
        """Reply to any post with !reply <link> <message>"""

        status_id = link.split("/")[-1]
        username = " @" + api.get_status(status_id).user.screen_name

        if len(ctx.message.content) > 7 and len(ctx.message.content) < 288 - len(username):
            try:
                msg = ctx.message.content[6::].replace("nigger","******").replace("fag","***")+username
                msg = " ".join(msg.split(" ")[2::])
                reply = api.update_status(msg, in_reply_to_status_id = status_id)
                replylink = "https://twitter.com/DiscordSpeaks/status/{}".format(reply.id)
                await self.bot.say("Posted!\n{}".format(replylink))
            except:
                await self.bot.say("`Invalid link or duplicate reply`")

        elif len(ctx.message.content) <= 7:
            msg = "`Can't send empty message`"
            await self.bot.say(msg)
        else:
            msg = "`Message too long`"
            await self.bot.say(msg)

    @commands.command()
    async def invite(self):
        """Posts link to add to your server"""
        await self.bot.say("Invite me to your server! https://t.co/PSFOhaPIcb")



def setup(bot):
    bot.add_cog(twitter(bot))
