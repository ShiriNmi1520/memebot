import discord
import re as regax
import meme
from pypinyin import pinyin, lazy_pinyin, Style
from requests import get
import operator
rank = {}

def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)

        meme.main()

class MyClient(discord.Client):
    count = 0
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        print(message.channel)
        # don't respond to ourselves
        if message.author == self.user:
            return
        msg = lazy_pinyin(message.content, style=Style.FIRST_LETTER)
        re = ''.join(msg)
        if message.content == '!checkrank':
            result = max(rank.items(), key=operator.itemgetter(1))[0]
            scariest = "最怕ㄉ大大4\n" + result + "\n講ㄌ" + str(rank[result]) + "次"
            await message.channel.send(scariest)

            return

        if message.content == '!checkall':
            strings = ""
            for key in rank:
                strings = strings + key + str(rank[key]) + "次" + "\n"
            await message.channel.send(strings)

        if message.channel.name == 'test':
            # 檢查是否有附件（圖片或影片）
            if message.attachments:
                await message.channel.send('好色喔')
            if message.embeds:
                if message.embeds[0].type == "link":
                    await message.channel.send('丟三小連結喔')

        if 'ddwhp' in re or 'whp' in re:
            if message.author.name in rank:
                rank[message.author.name] = rank[message.author.name] + 1
            else:
                rank[message.author.name] = 1
            result = message.author.name + '講了' +  str(rank[message.author.name]) + '次'
            await message.channel.send(result)
        emojiDetect = regax.findall(':+\d*>$', re)
        if len(emojiDetect) == 0:
            pass

        else:
            print(emojiDetect)
            emojiDetect = emojiDetect[0]
            emojiDetect = emojiDetect.strip(">")
            emojiDetect = emojiDetect.strip(":")
            emojiUrl = "https://cdn.discordapp.com/emojis/" + emojiDetect + ".png"
            print(emojiUrl)
            download(emojiUrl, './img/o.png')
            await message.channel.send(file=discord.File('./img/big_change.png'))
        # print(re)

client = MyClient()
client.run('')
