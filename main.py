import io
import urllib.request
import PIL
import discord
import random
from discord import app_commands
from discord.ui import Button
import time
import asyncio
import datetime
import spotipy
from PIL import Image
import requests
from PIL import UnidentifiedImageError
from io import StringIO
from googleapiclient.discovery import build
import urllib3.request
from imageio import imread

# Start to add suport for command prefixes, allow user to choose a prefix

googlekey = "<TOKEN>"
cxsrc= "<CXSRC>"

# SPOTIPY_CLIENT_ID = "<TOKEN>"
# client_secret = "<TOKEN>"

TOKEN = "<TOKEN>"

'''
TODO: Improve hangman using edits, author only, E.T.C., add images to eightball. Improve reminder embed/messages.
if google limit reached, find workaround/switch to bing/scrape articvle name website and header/ req more quota.
'''


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        await tree.sync()
        print("{0.user} is now online".format(client))



client = MyClient(intents=discord.Intents.default())
tree = app_commands.CommandTree(client)

@tree.command(name="eyebleach", description="Saw something unpleasant? Forget it.")
async def eye(interaction: discord.Interaction):
    anLst = [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Sea_Otter_%28Enhydra_lutris%29_%2825169790524%29_crop.jpg/800px-Sea_Otter_%28Enhydra_lutris%29_%2825169790524%29_crop.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Fischotter%2C_Lutra_Lutra.JPG/640px-Fischotter%2C_Lutra_Lutra.JPG",
        "https://i.natgeofe.com/n/586cb658-87be-4e9c-a932-5712a033ff2c/otter-group-thumb.jpg",
        "https://i.natgeofe.com/n/b53fecf2-6d8a-46ce-884a-1ed0c64111e3/sea-otter_thumb_2x3.jpg",
        "https://i.natgeofe.com/k/5a169ee4-f413-4521-9906-dae142888bd3/river-otter-closeup_4x3.jpg",
        "https://images.immediate.co.uk/production/volatile/sites/23/2021/03/GettyImages-1345278193-0770904.jpg",
        "https://images.immediate.co.uk/production/volatile/sites/23/2018/12/P.brasiliensis_Sergio-Pitamitz_Getty-15005b8-3822ef2.jpg",
        "https://wpde.com/resources/media/4a70b26d-b2cd-4f6d-b1e7-3e990ee6ad54-Otterpups.jpg",
        "https://www.reconnectwithnature.org/getmedia/098e120e-c025-4a93-901c-cd398b72915e/River-Otter-Shutterstock.jpg?width=2000&height=1333&ext=.jpg",
        "https://static01.nyt.com/images/2021/07/08/science/08TB-OTTERS1/merlin_190551999_3680585e-dbdd-4bff-96ad-0d74d1239df8-superJumbo.jpg",
        "https://spca.bc.ca/wp-content/uploads/WS2020_227762_Karac-Lindsay_Sea-Otter-Grooming-825x510.jpg",
        "https://www.thoughtco.com/thmb/wp5NJvalXvhNwyRNT6LgZAcg9R0=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-176608558-81ad368fc1a7438c96c5ee2959758f3c.jpg",
        "https://cdn.vox-cdn.com/thumbor/HifvBWnOw3GhSBI3vezlJkvBjos=/1400x788/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/23661899/sn_2.jpeg",
        "https://d3ftabzjnxfdg6.cloudfront.net/app/uploads/2020/05/18-10-28_0002-sea-otter-BB-web-1024x512.jpg",
        "https://www.treehugger.com/thmb/iayN8kOoAdb190hXrlG9KdZEb8Q=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/__opt__aboutcom__coeus__resources__content_migration__mnn__images__2015__09__river-otters-lead-photo-86eef01e35714da9a6dd974f321e3504.jpg",
        "https://www.nature.scot/sites/default/files/styles/max_1300x1300/public/2017-07/Otter-01v2.jpg?itok=uXYAOY2K",
        "https://animals.sandiegozoo.org/sites/default/files/2016-09/animals_hero_otter.jpg",
        "https://img.atlasobscura.com/DGerDsV8EO72e2yr2bLGpWwN5Dc6dO0DAIboDo6ETZ8/rs:fill:1280:720:1/g:ce/q:81/sm:1/scp:1/ar:1/aHR0cHM6Ly9hdGxh/cy1kZXYuczMuYW1h/em9uYXdzLmNvbS91/cGxvYWRzL2Fzc2V0/cy8xMzUzNTYxNzRi/Y2Y0N2Q2YzlfR2V0/dHlJbWFnZXMtNTIw/NDQyODE4LmpwZw.jpg",
        "https://blogger.googleusercontent.com/img/a/AVvXsEhFCgYEnFhF1xZJGN3w6BIdcpKHKFaLZyCGi5mRYcIkno5nhhT__TT20aTYt9f9cnVRxDTFbQatDK9DF421IK1l5AorlWpH6y-GZxeMHW7j_HITC1Vk-LCrTQWadS9HAPNq3_5-KrURX5dv0AFMIXtMrK-fvHjk5JFoPoVZ23gLALdrqxoDGodAIpz2=w640-h426",
        "https://www.earthrangers.com/public/content/wildwire/riverOtter-1.jpg",
        "https://i.pinimg.com/originals/68/8f/38/688f387a6f806fd1201259b551691a34.jpg",
        "https://cdn-attachments.timesofmalta.com/0cdc92b998bd53978579a226486b6721a2f1dff8-1566393707-5d5d456b-1920x1280.jpg",
    "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/cute-photos-of-cats-in-grass-1593184777.jpg",
    "https://i.guim.co.uk/img/media/43352be36da0eb156e8551d775a57fadba8ae6d7/0_0_1440_864/master/1440.jpg?width=1200&height=900&quality=85&auto=format&fit=crop&s=184376f73721b565014f1d24e5bf645c"]
    imgUrl = anLst[random.randint(0, len(anLst) - 1)]
    response = requests.get(imgUrl, stream=True)
    image = Image.open(io.BytesIO(response.content))

    # Get the color of the top left pixel
    try:
        pixel = image.getpixel((0, 0))
    except UnidentifiedImageError:
        pixel = (0, 0, 0)

    if type(pixel) == int:
        pixel = (pixel, pixel, pixel)
    # Convert the pixel color to a hex code
    hex_code = '0x{:02x}{:02x}{:02x}'.format(*pixel)
    embed = discord.Embed(
        colour=int(hex_code, 0),
        url=imgUrl
    )
    if anLst.index(imgUrl) >= 0 and anLst.index(imgUrl) <= 20:
        embed.title = "Cute Otter 🦦"
    else:
        embed.title = "Cute."
    embed.set_author(name="\u200b", icon_url=interaction.user.display_avatar)
    embed.set_footer(text="BluugBot", icon_url=client.user.display_avatar)
    embed.set_image(url=imgUrl)
    await interaction.response.send_message(embed=embed)

@tree.command(name="av", description="Show a users avatar.")
async def av(interaction: discord.Interaction, user: discord.Member = None):
    if user == None:
        response = requests.get(interaction.user.display_avatar.url, stream=True)
        image = Image.open(io.BytesIO(response.content))

        # Get the color of the top left pixel
        try:
            pixel = image.getpixel((0, 0))
        except UnidentifiedImageError:
            pixel = (0, 0, 0)

        if type(pixel) == int:
            pixel = (pixel, pixel, pixel)
        # Convert the pixel color to a hex code
        hex_code = '0x{:02x}{:02x}{:02x}'.format(*pixel)
        embed = discord.Embed(
            title=interaction.user.display_name + "'s Avatar",
            colour= int(hex_code,0),
            url = interaction.user.display_avatar.url
        )
        embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar)
        embed.set_image(url=interaction.user.display_avatar.url)
        embed.set_footer(text=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
        await interaction.response.send_message(embed=embed)
    else:
        response = requests.get(user.display_avatar.url, stream=True)
        image = Image.open(io.BytesIO(response.content))

        # Get the color of the top left pixel
        try:
            pixel = image.getpixel((0, 0))
        except UnidentifiedImageError:
            pixel = (0, 0, 0)

        if type(pixel) == int:
            pixel = (pixel, pixel, pixel)
        # Convert the pixel color to a hex code
        hex_code = '0x{:02x}{:02x}{:02x}'.format(*pixel)
        embed = discord.Embed(
            title=user.display_name + "'s Avatar",
            colour=int(hex_code, 0),
            url=user.display_avatar.url
        )
        embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar)
        embed.set_image(url=user.display_avatar.url)
        embed.set_footer(text=user.display_name, icon_url=user.display_avatar.url)
        await interaction.response.send_message(embed=embed)
@tree.command(name="ping", description="Test the bots response time in ms.")
async def ping(interaction: discord.Interaction):


    response = requests.get(interaction.user.display_avatar.url, stream=True)
    image = Image.open(io.BytesIO(response.content))

    # Get the color of the top left pixel
    try:
        pixel = image.getpixel((0, 0))
    except UnidentifiedImageError:
        pixel = (0, 0, 0)

    if type(pixel) == int:
        pixel = (pixel, pixel, pixel)
    # Convert the pixel color to a hex code
    hex_code = '0x{:02x}{:02x}{:02x}'.format(*pixel)
    embed = discord.Embed(
        title=f"Bot Latency: {round(client.latency * 1000)} ms",
        colour=int(hex_code, 0)
    )
    embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar)
    await interaction.response.send_message(embed=embed)

@tree.command(name="helpbluug", description="Provides a list of all commands with their descriptions.")
async def helpbluug(interaction: discord.Interaction):
    embed = discord.Embed (
        title="BluugBot's Commands:",
        colour= discord.Colour.yellow(),
    )
    userIMG = interaction.user.avatar
    userName = interaction.user.display_name
    embed.set_author(name=userName, icon_url=userIMG)
    embed.add_field(name="/eightball ```question:```", value="Randomly selects a response from a list of pre-determined responses to a required question parameter.")
    embed.add_field(name="/hangman", value="Start a game of hangman, add reactions to the embed to start guessing."
                                           " The reaction emojis MUST be the BLUE letters.", inline=False)
    embed.add_field(name="/helpbluug", value="Provides a list of all commands with their descriptions.", inline=False)
    embed.add_field(name="/test", value="React to the message and the bot will respond. This is quick way to test if the bot is functioning.", inline=False)

    embed.add_field(name="/remind ```user:``` ```message:``` ```time:```", value="Pings and reminds the selected user after the selected time."
                                          " NOTE: The time format must be as follows: 'Xd' for X days,"
                                          " 'Xh' for X hours, 'Xm' for X minutes, and 'Xs' for X seconds. (Ex: 3h = 3 hours). \n**Min. time is 1 minute, max. time is 90 days.**", inline=False)
    embed.add_field(name="/searchsong ```song:``` ```searchrange:```", value="Allows the user to search a song on spotify using keywords, such as the song name, artist, or a combination of both. This command will return a number of search results specified by the user using the 'searchrange' parameter, sorted by keywork similarity and song popualrity.")
    embed.add_field(name=":tools: SUPPORT :tools:", value="If you have any questions, suggestions or bug reports, join my support **[Discord Server](LINK)**", inline=False)
    embed.set_footer(text=client.user.display_name, icon_url=client.user.avatar.url)
    await interaction.response.send_message(embed=embed, ephemeral=True)

@tree.command( name="remind", description="Set a reminder.")
async def reminder(interaction: discord.Interaction, user: discord.Member,  message: str, time: str):
    embed = discord.Embed(title=":x: ERROR :x:", colour= 0xff1a1a)
    embed.set_footer(
        text=" - ERROR", icon_url=client.user.display_avatar)
    userIMG = interaction.user.avatar
    userName = interaction.user.display_name

    seconds = 0
    if time.lower().endswith("d"):
        seconds += int(time[:-1]) * 60 * 60 * 24
        counter = f"{seconds // 60 // 60 // 24} day(s)"
    if time.lower().endswith("h"):
        seconds += int(time[:-1]) * 60 * 60
        counter = f"{seconds // 60 // 60} hour(s)"
    elif time.lower().endswith("m"):
        seconds += int(time[:-1]) * 60
        counter = f"{seconds // 60} minute(s)"
    elif time.lower().endswith("s"):
        seconds += int(time[:-1])
        counter = f"{seconds} second(s)"
    if seconds == 0:
        embed.add_field(name=':warning: Error Message :warning:',
                        value='**Please specify a proper duration, use `/helpbluug` for more information.**')
    elif seconds < 60:
        embed.add_field(name=':warning: Error Message :warning:',
                        value='**Duration is too short!\nMinimum duration is 1 minute.**')
    elif seconds > 7776000:
        embed.add_field(name=':warning: Error Message :warning:', value='**Duration is too long!\nMaximum duration is 90 days.**')
    else:
        await interaction.response.send_message("Alright, I will remind " + user.mention +  f" about {message} in {counter}.")
        await asyncio.sleep(seconds)
        await interaction.followup.send(user.mention + "\nHi, you asked me to remind you about " + message + f" {counter} ago.")
        return
    await interaction.response.send_message(embed=embed, ephemeral=True)
    '''
    embed1 = discord.Embed (
        title = ":white_check_mark: :alarm_clock: Reminding in " + str(time_in_minutes) + " minute(s) :alarm_clock: :white_check_mark:",
        colour = discord.Colour.dark_purple()
    )
    await interaction.response.send_message(embed=embed1)
    seconds = time_in_minutes * 60
    endTime = time.time() + seconds
    embed2 = discord.Embed(
        title=message,
        colour=discord.Colour.dark_blue(),
    )
    embed2.set_footer(text="Your reminder")
    for x in range(0, 9999999999):
        sendTime = time.time()
        if sendTime >= endTime - 1 and sendTime <= endTime + 1:
            await interaction.followup.send(user1.mention + " Reminder:", embed=embed2)
            break
'''
@tree.command(name="8ball", description="Ask upon the magic 8 ball.")
async def ball(interaction: discord.Interaction, question: str):
    userIMG = interaction.user.avatar
    userName = interaction.user.display_name
    answers = ["It is certain.", "It is decidedly so. 🤓", "Without a doubt.", "Yes-definitely.",
               "You may rely on it.", "As I see it, yes.", "Most likely.", "The outlook is good.",
               "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.",
               "Better not tell you now. 🤓", "Cannot predict now.", "Concentrate and ask again.",
               "Don't count on it.", "My reply is no.", "My sources say no. 🤓", "The outlook is not so good.",
               "Very doubtful.", "No.", "Only on Tuesdays."]
    choice = random.randint(0, len(answers)-1)
    embed = discord.Embed(
        title='Magic 8 Ball',
        colour=discord.Colour.dark_purple()
    )
    embed.set_author(name=userName, icon_url=userIMG)
    embed.add_field(name="Question: ", value=question, inline=False)
    embed.add_field(name=answers[choice], value="🎱🎱🎱🎱🎱🎱🎱", inline=False)
    await interaction.response.send_message(embed=embed)


@tree.command(name="test", description="Quickly test the bot for proper function.")
async def testreact(interaction):
    await interaction.response.send_message("Plz react :3")
    reaction = await client.wait_for("reaction_add")
    await interaction.followup.send(f"You reacted with: {reaction[0]}")


@tree.command(name="hangman", description="Play some hangman :/.")
async def hangman(interaction: discord.Interaction):
    words = ["🇦🇵🇵🇱🇪", "🇩🇮🇸🇨🇴🇷🇩", "🇫🇴🇷🇹🇳🇮🇹🇪"]
    userIMG = interaction.user.display_avatar
    userName = interaction.user.display_name
    embed = discord.Embed(
        title='Hangman',
        colour=0xff0000

    )

    embed.set_author(name=userName, icon_url=userIMG)

    await interaction.response.send_message("Playing: Hangman")

    a = '🇦'
    b = '🇧'
    c = '🇨'
    d = '🇩'
    e = '🇪'
    f = '🇫'
    g = '🇬'
    h = '🇭'
    i = '🇮'
    j = '🇯'
    k = '🇰'
    l = '🇱'
    m = '🇲'
    n = '🇳'
    o = '🇴'
    p = '🇵'
    q = '🇶'
    r = '🇷'
    s = '🇸'
    t = '🇹'
    u = '🇺'
    v = '🇻'
    w = '🇼'
    x = '🇽'
    y = '🇾'
    z = '🇿'

    valid_letters = ['🇦', '🇧', '🇨', '🇩', '🇪', '🇫'
        , '🇬'
        , '🇭'
        , '🇮'
        , '🇯'
        , '🇰'
        , '🇱'
        , '🇲'
        , '🇳'
        , '🇴'
        , '🇵'
        , '🇶'
        , '🇷'
        , '🇸'
        , '🇹'
        , '🇺'
        , '🇻'
        , '🇼'
        , '🇽'
        , '🇾'
        , '🇿']

    wordArr = []
    theWord = words[random.randrange(0, len(words))]
    guesses = ['_'] * len(theWord)
    incorrect = 0
    stopper = 0
    used = []
    lives = 4
    # Append each letter of the word to wordArr
    for x in theWord:
        wordArr.append(x)

    # First instance of the game, 0 incorrect guesses
    while stopper == 0:
        displayGuesses = ""
        for z in range(0, len(guesses)):
            displayGuesses += guesses[z] + " "
        embed = discord.Embed(
            title='Hangman',
            colour=0xff0000

        )

        embed.set_author(name=userName, icon_url=userIMG)
        embed.add_field(name="Lives Remaining: " + str(lives - incorrect) + " ♥♥♥♥",
                        value='```      ------------------ \n      |        |       \n      |             \n      |             \n      |             \n      |             \n     ___           ```')
        embed.add_field(name="Progress: ", value="```" + displayGuesses + "```", inline=False)
        embed.set_footer(text="Make a guess by reacting to this message.")

        await interaction.edit_original_response(embed=embed)
        embed.remove_field(0)
        embed.remove_field(0)
        embed.remove_footer()

        reaction = await client.wait_for("reaction_add")

        guess1 = str(reaction[0])

        if valid_letters.count(guess1) >= 1:

            if wordArr.count(guess1) >= 1:
                for x in range(0, len(wordArr)):
                    if wordArr[x] == guess1:
                        guesses[x] = guess1
                embed.title = ":white_check_mark: Correct Guess :white_check_mark:"
                embed.add_field(name="Lives Remaining: " + str(lives - incorrect) + " ♥♥♥♥",
                                value='```      ------------------ \n      |        |       \n      |             \n      |             \n      |             \n      |             \n     ___           ```')
                embed.add_field(name="Progress: ", value="```" + displayGuesses + "```", inline=False)
                embed.colour = discord.Colour.green()
                await interaction.edit_original_response(embed=embed)
                await asyncio.sleep(0.3)
            else:
                embed.title = ":x: Incorrect Guess :x:"
                embed.add_field(name="Lives Remaining: " + str(lives - incorrect) + " ♥♥♥♥",
                                value='```      ------------------ \n      |        |       \n      |             \n      |             \n      |             \n      |             \n     ___           ```')
                embed.add_field(name="Progress: ", value="```" + displayGuesses + "```", inline=False)
                await interaction.edit_original_response(embed=embed)
                await asyncio.sleep(0.3)
                used.append(guess1)
                incorrect += 1
            if guesses == wordArr:
                embed.remove_footer()
                embed.remove_field(0)
                embed.remove_field(0)
                displayGuesses = " ".join(wordArr)
                embed.set_footer(text="The word was: " + theWord)
                embed.title= ":trophy: WINNER :trophy:"
                embed.add_field(name="Lives Remaining: " + str(lives - incorrect) + " ♥♥♥♥",
                                value='```      ------------------ \n      |        |       \n      |             \n      |             \n      |             \n      |             \n     ___           ```')
                embed.add_field(name="Progress: ", value="```" + displayGuesses + "```", inline=False)
                embed.colour = discord.Colour.yellow()
                await interaction.edit_original_response(embed=embed)
                stopper = 1

        else:
            await interaction.followup.send(":x: Incorrect Reaction Type (Must be a letter) :x:", ephemeral=True)
        if incorrect == 1:
            while stopper == 0:

                displayGuesses = ""
                for z in range(0, len(guesses)):
                    displayGuesses += guesses[z] + " "
                embed = discord.Embed(
                    title="Hangman",
                    colour=0xad0000
                )
                embed.set_author(name=userName, icon_url=userIMG)
                displayUsed = ""
                for i in range(0, len(used)):
                    displayUsed += used[i] + ", "
                embed.add_field(name="Lives Remaining: " + str(lives - incorrect) + " ♥♥♥🖤",
                                value='```      ------------------ \n      |        |       \n      |        O    \n      |             \n      |             \n      |             \n     ___           ```')
                embed.add_field(name="Progress: ", value="```" + displayGuesses + "```", inline=False)
                embed.add_field(name="Incorrect: ", value="```" + displayUsed + "```", inline=False)
                embed.set_footer(text="Make a guess by reacting to this message.")

                await interaction.edit_original_response(embed=embed)
                embed.remove_field(0)
                embed.remove_field(0)
                embed.remove_field(0)
                embed.remove_footer()

                reaction = await client.wait_for("reaction_add")

                guess1 = str(reaction[0])

                if valid_letters.count(guess1) >= 1:

                    if wordArr.count(guess1) >= 1:
                        for x in range(0, len(wordArr)):
                            if wordArr[x] == guess1:
                                guesses[x] = guess1
                        embed.title = ":white_check_mark: Correct Guess :white_check_mark:"
                        embed.add_field(name="Lives Remaining: " + str(lives - incorrect) + " ♥♥♥🖤",
                                        value='```      ------------------ \n      |        |       \n      |        O    \n      |             \n      |             \n      |             \n     ___           ```')
                        embed.add_field(name="Progress: ", value="```" + displayGuesses + "```", inline=False)
                        embed.add_field(name="Incorrect: ", value="```" + displayUsed + "```", inline=False)
                        embed.colour = discord.Colour.green()
                        await interaction.edit_original_response(embed=embed)
                        await asyncio.sleep(0.3)
                    else:
                        used.append(guess1)
                        incorrect += 1
                        embed.title = ":x: Incorrect Guess :x:"
                        embed.add_field(name="Lives Remaining: " + str(lives - incorrect) + " ♥♥♥🖤",
                                        value='```      ------------------ \n      |        |       \n      |        O    \n      |             \n      |             \n      |             \n     ___           ```')
                        embed.add_field(name="Progress: ", value="```" + displayGuesses + "```", inline=False)
                        embed.add_field(name="Incorrect: ", value="```" + displayUsed + "```", inline=False)

                        await interaction.edit_original_response(embed=embed)
                        await asyncio.sleep(0.3)

                    if guesses == wordArr:
                        embed.remove_footer()
                        embed.set_footer(text="The word was: " + theWord)
                        embed.title = ":trophy: WINNER :trophy:"
                        embed.colour = discord.Colour.yellow()

                        await interaction.edit_original_response(embed=embed)
                        stopper = 1
                        break
                else:
                    await interaction.followup.send(":x: Incorrect Reaction Type (Must be a letter) :x:", ephemeral=True)
                if incorrect == 2:
                    while stopper == 0:

                        embed = discord.Embed(
                            title="Hangman",
                            colour=0x850000
                        )
                        embed.set_author(name=userName, icon_url=userIMG)
                        displayGuesses = ""
                        for z in range(0, len(guesses)):
                            displayGuesses += guesses[z] + " "

                        displayUsed = ""
                        for i in range(0, len(used)):
                            displayUsed += used[i] + ", "
                        embed.add_field(name="Lives Remaining: " + str(lives - incorrect) + " ♥♥🖤🖤",
                                        value='```      ------------------ \n      |        |       \n      |        O    \n      |       /|\   \n      |             \n      |             \n     ___           ```')
                        embed.add_field(name="Progress: ", value="```" + displayGuesses + "```", inline=False)
                        embed.add_field(name="Incorrect: ", value="```" + displayUsed + "```", inline=False)
                        embed.set_footer(text="Make a guess by reacting to this message.")

                        await interaction.edit_original_response(embed=embed)
                        embed.remove_field(0)
                        embed.remove_field(0)
                        embed.remove_field(0)
                        embed.remove_footer()

                        reaction = await client.wait_for("reaction_add")

                        guess1 = str(reaction[0])

                        if valid_letters.count(guess1) >= 1:

                            if wordArr.count(guess1) >= 1:
                                for x in range(0, len(wordArr)):
                                    if wordArr[x] == guess1:
                                        guesses[x] = guess1
                                embed.title = ":white_check_mark: Correct Guess :white_check_mark:"
                                embed.add_field(name="Lives Remaining: " + str(lives - incorrect) + " ♥♥🖤🖤",
                                                value='```      ------------------ \n      |        |       \n      |        O    \n      |       /|\   \n      |             \n      |             \n     ___           ```')
                                embed.add_field(name="Progress: ", value="```" + displayGuesses + "```", inline=False)
                                embed.add_field(name="Incorrect: ", value="```" + displayUsed + "```", inline=False)
                                embed.colour = discord.Colour.green()
                                await interaction.edit_original_response(embed=embed)
                                await asyncio.sleep(0.3)
                            else:
                                used.append(guess1)
                                incorrect += 1
                                embed.title = ":x: Incorrect Guess :x:"
                                embed.add_field(name="Lives Remaining: " + str(lives - incorrect) + " ♥♥🖤🖤",
                                                value='```      ------------------ \n      |        |       \n      |        O    \n      |       /|\   \n      |             \n      |             \n     ___           ```')
                                embed.add_field(name="Progress: ", value="```" + displayGuesses + "```", inline=False)
                                embed.add_field(name="Incorrect: ", value="```" + displayUsed + "```", inline=False)
                                await interaction.edit_original_response(embed=embed)
                                await asyncio.sleep(0.3)

                            if guesses == wordArr:
                                embed.remove_footer()
                                embed.set_footer(text="The word was: " + theWord)
                                embed.title = ":trophy: WINNER :trophy:"
                                embed.colour = discord.Colour.yellow()
                                embed.add_field(name="Lives Remaining: " + str(lives - incorrect) + " ♥♥🖤🖤",
                                                value='```      ------------------ \n      |        |       \n      |        O    \n      |       /|\   \n      |             \n      |             \n     ___           ```')
                                embed.add_field(name="Progress: ", value="```" + displayGuesses + "```", inline=False)
                                embed.add_field(name="Incorrect: ", value="```" + displayUsed + "```", inline=False)
                                await interaction.edit_original_response(embed=embed)
                                stopper = 1
                                break
                        else:
                            await interaction.followup.send(":x: Incorrect Reaction Type (Must be a letter) :x:", ephemeral=True)
                        if incorrect == 3:
                            while stopper == 0:
                                embed = discord.Embed(
                                    title="Hangman",
                                    colour=0x380000
                                )
                                embed.set_author(name=userName, icon_url=userIMG)
                                displayGuesses = ""
                                for z in range(0, len(guesses)):
                                    displayGuesses += guesses[z] + " "

                                displayUsed = ""
                                for i in range(0, len(used)):
                                    displayUsed += used[i] + ", "
                                embed.add_field(name="Lives Remaining: " + str(lives - incorrect) + " ♥🖤🖤🖤",
                                                value='```      ------------------ \n      |        |       \n      |        O    \n      |       /|\   \n      |       /     \n      |             \n     ___           ```')
                                embed.add_field(name="Progress: ", value="```" + displayGuesses + "```", inline=False)
                                embed.add_field(name="Incorrect: ", value="```" + displayUsed + "```", inline=False)
                                embed.set_footer(text="Make a guess by reacting to this message.")

                                await interaction.edit_original_response(embed=embed)
                                embed.remove_field(0)
                                embed.remove_field(0)
                                embed.remove_field(0)
                                embed.remove_footer()

                                reaction = await client.wait_for("reaction_add")

                                guess1 = str(reaction[0])

                                if valid_letters.count(guess1) >= 1:

                                    if wordArr.count(guess1) >= 1:
                                        for x in range(0, len(wordArr)):
                                            if wordArr[x] == guess1:
                                                guesses[x] = guess1
                                        embed.title = ":white_check_mark: Correct Guess :white_check_mark:"
                                        embed.add_field(name="Lives Remaining: " + str(lives - incorrect) + " ♥🖤🖤🖤",
                                                        value='```      ------------------ \n      |        |       \n      |        O    \n      |       /|\   \n      |       /     \n      |             \n     ___           ```')
                                        embed.add_field(name="Progress: ", value="```" + displayGuesses + "```",
                                                        inline=False)
                                        embed.add_field(name="Incorrect: ", value="```" + displayUsed + "```",
                                                        inline=False)
                                        embed.colour = discord.Colour.green()
                                        await interaction.edit_original_response(embed=embed)
                                        await asyncio.sleep(0.3)
                                    else:
                                        used.append(guess1)
                                        incorrect += 1
                                        embed.title = ":x: Incorrect Guess :x:"
                                        embed.add_field(name="Lives Remaining: " + str(lives - incorrect) + " ♥🖤🖤🖤",
                                                        value='```      ------------------ \n      |        |       \n      |        O    \n      |       /|\   \n      |       /     \n      |             \n     ___           ```')
                                        embed.add_field(name="Progress: ", value="```" + displayGuesses + "```",
                                                        inline=False)
                                        embed.add_field(name="Incorrect: ", value="```" + displayUsed + "```",
                                                        inline=False)
                                        await interaction.edit_original_response(embed=embed)
                                        await asyncio.sleep(0.3)

                                    if guesses == wordArr:
                                        embed.remove_footer()
                                        embed.set_footer(text="The word was: " + theWord)
                                        embed.title = ":trophy: WINNER :trophy:"
                                        embed.colour = discord.Colour.yellow()
                                        embed.add_field(name="Lives Remaining: " + str(lives - incorrect) + " ♥🖤🖤🖤",
                                                        value='```      ------------------ \n      |        |       \n      |        O    \n      |       /|\   \n      |       /     \n      |             \n     ___           ```')
                                        embed.add_field(name="Progress: ", value="```" + displayGuesses + "```",
                                                        inline=False)
                                        embed.add_field(name="Incorrect: ", value="```" + displayUsed + "```",
                                                        inline=False)
                                        await interaction.edit_original_response(embed=embed)
                                        stopper = 1
                                        break
                                else:
                                    await interaction.followup.send(
                                        ":x: Incorrect Reaction Type (Must be a letter) :x:", ephemeral=True)
                                if incorrect == 4:
                                    while stopper == 0:
                                        embed = discord.Embed(
                                            title="Hangman",
                                            colour=0x000000
                                        )
                                        embed.set_author(name=userName, icon_url=userIMG)
                                        displayGuesses = ""
                                        for z in range(0, len(guesses)):
                                            displayGuesses += guesses[z] + " "

                                        displayUsed = ""
                                        for i in range(0, len(used)):
                                            displayUsed += used[i] + ", "
                                        embed.add_field(name=":x: LOSER :x: 🖤🖤🖤🖤",
                                                        value='```      -------------------- \n      |        |       \n      |        O    \n      |       /|\   \n      |       / \   \n      |             \n     ___           ```')
                                        embed.add_field(name="Progress: ", value="```" + displayGuesses + "```",
                                                        inline=False)
                                        embed.add_field(name="Incorrect: ", value="```" + displayUsed + "```",
                                                        inline=False)
                                        embed.set_footer(text="The word was: " + theWord)

                                        await interaction.edit_original_response(embed=embed)

                                        stopper = 1
                                        break
'''
import time
from pprint import pprint
import spotipy
SPOTIPY_CLIENT_ID = "<TOKEN>"
client_secret = "SPOTIPY_CLIENT_ID = "<TOKEN>"
"
scopes = 'user-read-playback-state'
@tree.command(name="spotify", description="Displays what you are currently listening to on Spotify.")
async def getTrack(interaction):
    embed = discord.Embed(
        title='Listening To:',
        colour=discord.Colour.dark_green()
    )
    sp = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(client_id="SPOTIPY_CLIENT_ID = "<TOKEN>"
",
                                                           client_secret="SPOTIPY_CLIENT_ID = "<TOKEN>"
",
                                                          redirect_uri="https://github.com/EliyaFarhat", scope=scopes))
    try:
        current_track_info = sp.currently_playing()
        artists = current_track_info['item']['artists']
        artist_name = ', '.join([artist['name'] for artist in artists])
        embed.add_field(name=current_track_info['item']['name'], value=artist_name)
        await interaction.response.send_message(embed=embed)
    except spotipy.SpotifyOauthError as e:
        sp = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(client_id="SPOTIPY_CLIENT_ID = "<TOKEN>"
", client_secret="SPOTIPY_CLIENT_ID = "<TOKEN>"
", redirect_uri="https://github.com/EliyaFarhat",scope=scopes))
'''


scopes = 'user-read-playback-state'
@tree.command(name="searchsong", description="Search for songs on Spotify.")
async def searchsong(interaction: discord.Interaction, song: str, searchrange: int):
    sp = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(client_id="SPOTIPY_CLIENT_ID = "<TOKEN>"
",
                                                               client_secret="SPOTIPY_CLIENT_ID = "<TOKEN>"
",
                                                               redirect_uri="https://github.com/EliyaFarhat",
                                                              scope=scopes))

    try:
        searchQuery = song

        embed = discord.Embed(
            title='Showing ' + str(searchrange) + ' results for: ' + song,
            color=0x1ED760
        )
        userIMG = interaction.user.avatar
        userName = interaction.user.display_name
        embed.set_author(name=userName, icon_url=userIMG)
        count = 1
        searchResults = sp.search(q=searchQuery, type="track" , market= "US", limit=searchrange)
        error = discord.Embed(title=":x: ERROR :x:", color=0xff1a1a)

        error.add_field(name=':warning: Error Message :warning:',
                        value="**Can't find the song: " + song + ".**\n\n Check the spelling and try again.\n\n         ",
                        inline=False)
        error.add_field(name=":tools: SUPPORT :tools:",
                        value="If you have any questions, suggestions or bug reports, join my support **[Discord Server](LINK)**",
                        inline=False)
        error.set_author(name=userName, icon_url=userIMG)
        error.set_footer(text=" - ERROR.",
                         icon_url="https://www.freepnglogos.com/uploads/spotify-logo-png/file-spotify-logo-png-4.png")

        if len(searchResults) == 0:
            raise IndexError
        # artists = searchResults['tracks']['items'][0]['artists']
        # allArtists = ', '.join([artists[x]['name'] for x in range(len(artists))])
        # track_name = searchResults['tracks']['items'][0]['name']
        image = searchResults['tracks']['items'][0]['album']['images'][0]['url']
        embed.set_thumbnail(url=image)


        for x in range(0,searchrange):
            artistURL = searchResults['tracks']['items'][x]['album']['artists'][0]['external_urls']['spotify']
            trackURL = searchResults['tracks']['items'][x]['external_urls']['spotify']
            artists = searchResults['tracks']['items'][x]['artists']
            allArtists = ', '.join([artists[x]['name'] for x in range(len(artists))])
            track_name = searchResults['tracks']['items'][x]['name']
            duration = searchResults['tracks']['items'][x]['duration_ms']
            sec1, mill1 = divmod(duration, 1000)
            min1, sec1 = divmod(sec1, 60)
            duration = "%d:%d" % (min1, sec1)
            if duration[0] != 0 and len(duration) == 3:
                duration = "%d:0%d" % (min1, sec1)
            embed.add_field(name= "```" + str(count) + "``` " + track_name + " - " + allArtists + " (" + str(duration) + ")", value= f"**[[Track]]({trackURL})" + f" :link: [[Artist]]({artistURL})**", inline=False)


            count += 1
        embed.set_footer(text=" - Tracks are sorted by keyword similarity and track popularity.",
                         icon_url="https://www.freepnglogos.com/uploads/spotify-logo-png/file-spotify-logo-png-4.png")


        await interaction.response.send_message(embed=embed)
    except spotipy.SpotifyOauthError as e:
        sp = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(client_id="SPOTIPY_CLIENT_ID = "<TOKEN>"
",
                                                               client_secret="<TOKEN>",
                                                               redirect_uri="https://github.com/EliyaFarhat",
                                                               scope=scopes))
    except IndexError:
        await interaction.response.send_message(embed=error, ephemeral=True)

@tree.command(name="searchalbum", description="Search for an album on Spotify.")
async def searchalbum(interaction: discord.Interaction, album: str):
    sp = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(client_id="<TOKEN>",
                                                           client_secret="<TOKEN>",
                                                           redirect_uri="https://github.com/EliyaFarhat",
                                                           scope=scopes))

    try:

        searchQuery = album

        if len(searchQuery) == 0:
            raise IndexError
        userIMG = interaction.user.avatar
        userName = interaction.user.display_name
        error = discord.Embed(title=":x: ERROR :x:", color=0xff1a1a)

        error.add_field(name=':warning: Error Message :warning:',
                        value="**Can't find the album: " + album + ".**\n\n Check the spelling and try again.\n\n         ",
                        inline=False)
        error.add_field(name=":tools: SUPPORT :tools:",
                        value="If you have any questions, suggestions or bug reports, join my support **[Discord Server](LINK)**",
                        inline=False)
        error.set_author(name=userName, icon_url=userIMG)
        error.set_footer(text=" - ERROR.",
                         icon_url="https://www.freepnglogos.com/uploads/spotify-logo-png/file-spotify-logo-png-4.png")


        searchResults = sp.search(q=searchQuery, type="album", market="US", limit=1)

        alb_name = searchResults['albums']['items'][0]['name']
        image = searchResults['albums']['items'][0]['images'][1]['url']


        artistURL = searchResults['albums']['items'][0]['artists'][0]['external_urls']['spotify']
        albURL = searchResults['albums']['items'][0]['external_urls']['spotify']
        artists = searchResults['albums']['items'][0]['artists']
        allArtists = ', '.join([artists[x]['name'] for x in range(len(artists))])
        trackAmt = searchResults['albums']['items'][0]['total_tracks']
        albRelease = searchResults['albums']['items'][0]['release_date']
        if trackAmt == 1:
            userIMG = interaction.user.avatar
            userName = interaction.user.display_name

            embed = discord.Embed(
                title=alb_name + " - " + allArtists,
                description=f"**[[Album]]({albURL})" + f" :link: [[Artist]]({artistURL})**\n\n**" + str(
                    trackAmt) + " Track**\n\n" + "(" + albRelease + ")",
                color=0x1ED760
            )
            embed.set_author(name=userName, icon_url=userIMG)
        else:
            userIMG = interaction.user.avatar
            userName = interaction.user.display_name

            embed = discord.Embed(
                title=alb_name + " - " + allArtists,
                description=f"**[[Album]]({albURL})" + f" :link: [[Artist]]({artistURL})**\n\n**" + str(
                    trackAmt) + " Tracks**\n\nReleased on " +  albRelease ,
                color=0x1ED760
            )
            embed.set_author(name=userName, icon_url=userIMG)
        embed.set_image(url=image)

        embed.set_author(name=userName, icon_url=userIMG)

        embed.set_footer(text=" - Showing results for: " + album,
                         icon_url="https://www.freepnglogos.com/uploads/spotify-logo-png/file-spotify-logo-png-4.png")

        await interaction.response.send_message(embed=embed)
    except spotipy.SpotifyOauthError as e:
        sp = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(client_id="",
                                                               client_secret="",
                                                               redirect_uri="https://github.com/EliyaFarhat",
                                                               scope=scopes))
    except IndexError:
        await interaction.response.send_message(embed=error, ephemeral=True)

@tree.command(name="searchartist", description="Search for an artist on Spotify.")
async def searchart(interaction: discord.Interaction, artist: str):
    sp = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(client_id="",
                                                           client_secret="",
                                                           redirect_uri="https://github.com/EliyaFarhat",
                                                           scope=scopes))
    userIMG = interaction.user.avatar
    userName = interaction.user.display_name
    error = discord.Embed(title=":x: ERROR :x:", color=0xff1a1a)

    error.add_field(name=':warning: Error Message :warning:',
                    value="**Can't find the artist: " + artist + ".**\n\n Check the spelling and try again.\n\n         ",
                    inline=False)
    error.add_field(name=":tools: SUPPORT :tools:",
                    value="If you have any questions, suggestions or bug reports, join my support **[Discord Server](LINK)**",
                    inline=False)
    error.set_author(name=userName, icon_url=userIMG)
    error.set_footer(text=" - ERROR.",
                     icon_url="https://www.freepnglogos.com/uploads/spotify-logo-png/file-spotify-logo-png-4.png")
    try:
        searchQuery = artist


        searchResults = sp.search(q=searchQuery, type="artist", market="US", limit=1)
        if len(searchResults) == 0:
            raise IndexError

        art_name = searchResults['artists']['items'][0]['name']
        image = searchResults['artists']['items'][0]['images'][0]['url']
        followers = searchResults['artists']['items'][0]['followers']['total']
        artistURL = searchResults['artists']['items'][0]['external_urls']['spotify']
        artPop = searchResults['artists']['items'][0]['popularity']

        embed = discord.Embed(
            title=art_name,
            url=artistURL,
            description="**Followers: " + str(followers) + "**",
            colour= 0x1ED760
        )
        embed.set_author(name=userName, icon_url=userIMG)








        embed.set_image(url=image)

        embed.set_author(name=userName, icon_url=userIMG)

        embed.set_footer(text=" - Showing results for: " + artist, icon_url="https://www.freepnglogos.com/uploads/spotify-logo-png/file-spotify-logo-png-4.png")
        if artPop > 93 and artPop <= 100:
            embed.add_field(name="Popularity:", value=":star: :star: :star: :star: :star: :star: :star: :star: :star: :star: **(10/10)**")
        elif artPop > 85 and artPop <= 93:
            embed.add_field(name="Popularity:", value=":star: :star: :star: :star: :star: :star: :star: :star: :star: :black_medium_square: **(9/10)**")
        elif artPop > 75 and artPop <= 85:
            embed.add_field(name="Popularity:", value=":star: :star: :star: :star: :star: :star: :star: :star: :black_medium_square: :black_medium_square:  **(8/10)**")
        elif artPop > 65 and artPop <= 75:
            embed.add_field(name="Popularity:", value=":star: :star: :star: :star: :star: :star: :star: :black_medium_square: :black_medium_square: :black_medium_square: **(7/10)**")
        elif artPop > 55 and artPop <= 65:
            embed.add_field(name="Popularity:", value=":star: :star: :star: :star: :star: :star: :black_medium_square: :black_medium_square: :black_medium_square: :black_medium_square: **(6/10)**")
        elif artPop > 45 and artPop <= 55:
            embed.add_field(name="Popularity:", value=":star: :star: :star: :star: :star: :black_medium_square: :black_medium_square: :black_medium_square: :black_medium_square: :black_medium_square: **(5/10)**")
        elif artPop > 35 and artPop <= 45:
            embed.add_field(name="Popularity:", value=":star: :star: :star: :star: :black_medium_square: :black_medium_square: :black_medium_square: :black_medium_square: :black_medium_square: :black_medium_square: **(4/10)**")
        elif artPop > 25 and artPop <= 35:
            embed.add_field(name="Popularity:", value=":star: :star: :star: :black_medium_square: :black_medium_square: :black_medium_square: :black_medium_square: :black_medium_square: :black_medium_square: :black_medium_square: **(3/10)**")
        elif artPop > 15 and artPop <= 25:
            embed.add_field(name="Popularity:", value=":star: :star: :black_medium_square: :black_medium_square: :black_medium_square: :black_medium_square: :black_medium_square: :black_medium_square: :black_medium_square: :black_medium_square: **(2/10)**")
        elif artPop > 5 and artPop <= 15:
            embed.add_field(name="Popularity:", value=":star: :black_medium_square: :black_medium_square: :black_medium_square: :black_medium_square: :black_medium_square: :black_medium_square: :black_medium_square: :black_medium_square: :black_medium_square: **(1/10)**")
        elif artPop > 0 and artPop <= 5:
            embed.add_field(name="Popularity:",
                            value=":black_medium_square: :black_medium_square: :black_medium_square: :black_medium_square: :black_medium_square: :black_medium_square: :black_medium_square: :black_medium_square: :black_medium_square: :black_medium_square: **(0/10)**")
        await interaction.response.send_message(embed=embed)

    except spotipy.SpotifyOauthError as e:
        sp = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(client_id="",
                                                               client_secret="",
                                                               redirect_uri="https://github.com/EliyaFarhat",
                                                               scope=scopes))
    except IndexError:
        await interaction.response.send_message(embed=error, ephemeral=True)

# bing is way too slow, lets use the google API
# from bing_image_urls import bing_image_urls

get_curr_id = ""
get_curr_secret = ""
scopeTwo = "user-read-currently-playing"

def getCurrentTrack(sp):
    try:
        curr = sp.currently_playing()
        # Album img, track name, artist name(s), track url, artist url, duration, progress ms, song %
        info = []
        # albimg 0
        info.append( curr['item']['album']['images'][1]['url'])
        # track name 1
        info.append(curr['item']['name'])
        # artists 2
        artists = curr['item']['artists']
        allArtists = ', '.join([artists[x]['name'] for x in range(len(artists))])
        info.append(allArtists)
        # track url 3
        info.append(curr['item']['external_urls']['spotify'])
        # first artist url 4
        info.append(artists[0]['external_urls']['spotify'])
        # duration 5
        duration = curr['item']['duration_ms']
        sec1, mill1 = divmod(duration, 1000)
        min1, sec1 = divmod(sec1, 60)
        duration = "%d:%d" % (min1, sec1)
        if duration[0] != 0 and len(duration) == 3:
            duration = "%d:0%d" % (min1, sec1)
        info.append(duration)
        # progress 6
        duration1 = curr['progress_ms']
        sec2, mill2 = divmod(duration1, 1000)
        min2, sec2 = divmod(sec2, 60)
        duration1 = "%d:%d" % (min2, sec2)
        if duration1[0] != 0 and len(duration1) == 3:
            duration1 = "%d:0%d" % (min2, sec2)
        info.append(duration1)
        # song % 7
        prog = (curr['progress_ms']/curr['item']['duration_ms']) * 100
        info.append(prog)
        return info
    except TypeError:
        return "EMPTY"
@tree.command(name="stalk", description="See what my creator is listening to.")
async def stalk(interaction: discord.Interaction):
    sp = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(client_id="", client_secret="",
                                                           redirect_uri="https://github.com/EliyaFarhat", scope=scopes))
    embed = discord.Embed(
        title="temp",
        color=0x1ED760
    )
    userIMG = interaction.user.avatar
    userName = interaction.user.display_name
    error = discord.Embed(title=":x: My creator is not listening to anything. :x:", color=0xff1a1a)

    error.add_field(name=":tools: SUPPORT :tools:",
                    value="If you have any questions, suggestions, bug reports, or may believe this message is an error, join my support **[Discord Server](LINK)**",
                    inline=False)
    error.set_author(name=userName, icon_url=userIMG)
    error.set_footer(text="Check again later.",
                     icon_url="https://www.freepnglogos.com/uploads/spotify-logo-png/file-spotify-logo-png-4.png")

    embed.set_author(name="cup#8942 is listening to: ", icon_url=userIMG)
    if getCurrentTrack(sp) == "EMPTY":
        await interaction.response.send_message(embed=error)
    else:
        try:
            lst = getCurrentTrack(sp)
            embed.set_thumbnail(url=lst[0])
            embed.title = lst[1] + " - " + lst[2]
            song_progress = lst[7]
            scroll = ["─", "─", "─", "─", "─", "─", "─", "─", "─","─", "─", "─", "─", "─", "─", "─", "─", "─"]
            if song_progress <= 5:
                scroll.insert(0,"|")
            elif song_progress > 5 and song_progress <= 15:
                scroll.insert(2, "|")
            elif song_progress > 15 and song_progress <= 25:
                scroll.insert(4, "|")
            elif song_progress > 25 and song_progress <= 35:
                scroll.insert(6, "|")
            elif song_progress > 35 and song_progress <= 45:
                scroll.insert(8, "|")
            elif song_progress > 45 and song_progress <= 55:
                scroll.insert(10, "|")
            elif song_progress > 55 and song_progress <= 65:
                scroll.insert(12, "|")
            elif song_progress > 65 and song_progress <= 75:
                scroll.insert(14, "|")
            elif song_progress > 75 and song_progress <= 85:
                scroll.insert(16, "|")
            elif song_progress > 85 and song_progress <= 95:
                scroll.insert(18, "|")
            elif song_progress <= 100 and song_progress >= 95:
                scroll.insert(19, "|")
            finalScroll = ''.join(scroll)
            embed.add_field(name="\u200b", value=f"**[[Track]]({lst[3]}) :link: [[Artist]]({lst[4]})**\n\u200b")
            embed.add_field(name=f"{lst[6]} {finalScroll} {lst[5]}",value="\u200b", inline= False)
            embed.set_footer(text="Viewed best on desktop.",
                             icon_url="https://www.freepnglogos.com/uploads/spotify-logo-png/file-spotify-logo-png-4.png")
            await interaction.response.send_message(embed=embed)
        except spotipy.SpotifyOauthError as e:
            sp = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(client_id="",
                                                                   client_secret="",
                                                                   redirect_uri="https://github.com/EliyaFarhat",
                                                                   scope=scopes))
            lst = getCurrentTrack(sp)
            embed.set_thumbnail(url=lst[0])
            embed.title = lst[1] + " - " + lst[2]
            song_progress = lst[7]
            scroll = ["─", "─", "─", "─", "─", "─", "─", "─", "─", "─", "─", "─", "─", "─", "─", "─", "─", "─"]
            if song_progress <= 5:
                scroll.insert(0, "|")
            elif song_progress > 5 and song_progress <= 15:
                scroll.insert(2, "|")
            elif song_progress > 15 and song_progress <= 25:
                scroll.insert(4, "|")
            elif song_progress > 25 and song_progress <= 35:
                scroll.insert(6, "|")
            elif song_progress > 35 and song_progress <= 45:
                scroll.insert(8, "|")
            elif song_progress > 45 and song_progress <= 55:
                scroll.insert(10, "|")
            elif song_progress > 55 and song_progress <= 65:
                scroll.insert(12, "|")
            elif song_progress > 65 and song_progress <= 75:
                scroll.insert(14, "|")
            elif song_progress > 75 and song_progress <= 85:
                scroll.insert(16, "|")
            elif song_progress > 85 and song_progress <= 95:
                scroll.insert(18, "|")
            elif song_progress <= 100 and song_progress >= 95:
                scroll.insert(19, "|")
            finalScroll = ''.join(scroll)
            embed.add_field(name="\u200b", value=f"**[[Track]]({lst[3]}) :link: [[Artist]]({lst[4]})**\n\u200b")
            embed.add_field(name=f"{lst[6]} {finalScroll} {lst[5]}", value="\u200b", inline=False)
            embed.set_footer(text="Viewed best on desktop.",
                             icon_url="https://www.freepnglogos.com/uploads/spotify-logo-png/file-spotify-logo-png-4.png")
            await interaction.response.send_message(embed=embed)

@tree.command(name="img", description="Search for an image on the internet.")
async def searchimg(interaction: discord.Interaction, search: str):
    global index
    index = 0

    hidden = discord.Embed(
        title=":warning: Only the user of the command can interact with this embed. :warning:",
        color=discord.Colour.yellow()
    )

    hidden.set_footer(text="BluugBot", icon_url=client.user.display_avatar)
    try:
        resource = build("customsearch", "v1", developerKey = googlekey).cse()
        result = resource.list(q=f"{search}", cx=cxsrc, searchType="image").execute()



        response = requests.get(result['items'][index]["link"], stream=True)
        image = Image.open(io.BytesIO(response.content))


        # Get the color of the top left pixel
        try:
            pixel = image.getpixel((0, 0))
        except UnidentifiedImageError:
            pixel = (0,0,0)

        if type(pixel) == int:
            pixel = (pixel, pixel, pixel)
        # Convert the pixel color to a hex code
        hex_code = '0x{:02x}{:02x}{:02x}'.format(*pixel)

        left = Button(style=discord.ButtonStyle.primary, emoji="<:2052whiteleft:1061296822984912936>")
        right = Button(style=discord.ButtonStyle.primary, emoji="<:9847whiteright:1061296811257634957>")
        close = Button(style=discord.ButtonStyle.red, emoji="✖")
        imgURL = result['items'][index]['image']['contextLink']
        embed = discord.Embed(
            title="Showing Image 1/10",
            description=f"**[{result['items'][index]['title']}]({imgURL})**",
            colour=int(hex_code, 0)
        )
        userIMG = interaction.user.avatar
        userName = interaction.user.display_name
        embed.set_author(name=userName, icon_url=userIMG)
        embed.set_image(url=result['items'][index]['link'])
        embed.set_footer(text=" - Showing images for: " + search, icon_url= "https://companieslogo.com/img/orig/GOOG-0ed88f7c.png?t=1633218227")
        async def button_callback(interaction2: discord.Interaction):
            global index
            if interaction.user == interaction2.user:
                try:

                    if index > 0:
                        index -= 1

                    response = requests.get(result['items'][index]["link"], stream=True)
                    image = Image.open(io.BytesIO(response.content))


                    # Get the color of the top left pixel
                    pixel = image.getpixel((0, 0))
                    if type(pixel) == int:
                        pixel = (pixel, pixel, pixel)

                    # Convert the pixel color to a hex code
                    hex_code = '0x{:02x}{:02x}{:02x}'.format(*pixel)

                    prevImg = discord.Embed(title="Showing Image " + str(index + 1) + "/10",
                    description=f"**[{result['items'][index]['title']}]({result['items'][index]['image']['contextLink']})**",colour= int(hex_code, 0))
                    prevImg.set_footer(text=" - Showing images for: " + search, icon_url="https://companieslogo.com/img/orig/GOOG-0ed88f7c.png?t=1633218227")
                    prevImg.set_image(url=result['items'][index]["link"])
                    prevImg.set_author(name=userName, icon_url=userIMG)

                    await interaction.edit_original_response(view=view, embed=prevImg)
                    await interaction2.response.defer()
                except UnidentifiedImageError:
                    newIn = index + 1



                    response = requests.get(result['items'][newIn]["link"], stream=True)
                    image = Image.open(io.BytesIO(response.content))


                    # Get the color of the top left pixel
                    pixel = image.getpixel((0, 0))
                    if type(pixel) == int:
                        pixel = (pixel, pixel, pixel)

                    # Convert the pixel color to a hex code
                    hex_code = '0x{:02x}{:02x}{:02x}'.format(*pixel)
                    prevImg = discord.Embed(title="Showing Image " + str(index + 1) + "/10",
                                            description=f"**[{result['items'][index]['title']}]({result['items'][index]['image']['contextLink']})**",
                                            colour=int(hex_code, 0))
                    prevImg.set_footer(text=" - Showing images for: " + search, icon_url="https://companieslogo.com/img/orig/GOOG-0ed88f7c.png?t=1633218227")
                    prevImg.set_image(url=result['items'][newIn]["link"])
                    prevImg.set_author(name=userName, icon_url=userIMG)

                    await interaction.edit_original_response(view=view, embed=prevImg)
                    await interaction2.response.defer()
            else:
                hidden.set_author(name=interaction2.user.display_name, icon_url=interaction2.user.display_avatar)
                await interaction2.response.send_message(embed=hidden, ephemeral=True)


        async def button_callback2(interaction3: discord.Interaction):
            global index
            if interaction.user == interaction3.user:
                try:
                    if index < 9:
                        index += 1

                    response = requests.get(result['items'][index]["link"], stream=True)
                    image = Image.open(io.BytesIO(response.content))


                    # Get the color of the top left pixel
                    pixel = image.getpixel((0, 0))
                    if type(pixel) == int:
                        pixel = (pixel, pixel, pixel)

                    # Convert the pixel color to a hex code
                    hex_code = '0x{:02x}{:02x}{:02x}'.format(*pixel)

                    nextImg = discord.Embed(title="Showing Image " + str(index + 1) + "/10",
                    description=f"**[{result['items'][index]['title']}]({result['items'][index]['image']['contextLink']})**", colour= int(hex_code, 0))
                    nextImg.set_image(url=result['items'][index]["link"])
                    nextImg.set_footer(text=" - Showing images for: " + search, icon_url="https://companieslogo.com/img/orig/GOOG-0ed88f7c.png?t=1633218227")
                    nextImg.set_author(name=userName, icon_url=userIMG)
                    await interaction.edit_original_response(embed=nextImg, view=view)
                    await interaction3.response.defer()
                except UnidentifiedImageError:
                    if index < 9:
                        newIn = index + 1
                    else:
                        newIn = index - 1




                    response = requests.get(result['items'][newIn]["link"], stream=True)
                    image = Image.open(io.BytesIO(response.content))


                    # Get the color of the top left pixel
                    pixel = image.getpixel((0, 0))
                    if type(pixel) == int:
                        pixel = (pixel, pixel, pixel)

                    # Convert the pixel color to a hex code
                    hex_code = '0x{:02x}{:02x}{:02x}'.format(*pixel)
                    prevImg = discord.Embed(title="Showing Image " + str(index + 1) + "/10",
                                            description=f"**[{result['items'][index]['title']}]({result['items'][index]['image']['contextLink']})**",
                                            colour=int(hex_code, 0))
                    prevImg.set_footer(text=" - Showing images for: " + search, icon_url="https://companieslogo.com/img/orig/GOOG-0ed88f7c.png?t=1633218227")
                    prevImg.set_image(url=result['items'][newIn]["link"])
                    prevImg.set_author(name=userName, icon_url=userIMG)

                    await interaction.edit_original_response(view=view, embed=prevImg)
                    await interaction3.response.defer()
            else:
                hidden.set_author(name=interaction3.user.display_name, icon_url=interaction3.user.display_avatar)
                await interaction3.response.send_message(embed=hidden, ephemeral=True)


        async def button_callback3(interaction4: discord.Interaction):
            if interaction.user == interaction4.user:
                await interaction.delete_original_response()
                await interaction4.response.defer()
            else:
                hidden.set_author(name=interaction4.user.display_name, icon_url=interaction4.user.display_avatar)
                await interaction4.response.send_message(embed=hidden, ephemeral=True)
        left.callback = button_callback
        right.callback = button_callback2
        close.callback = button_callback3
        view = discord.ui.View(timeout=90)

        view.add_item(left)
        view.add_item(right)
        view.add_item(close)


        await interaction.response.send_message(embed=embed, view=view)

        async def on_timeout():
            timeout = discord.Embed(title="Showing Image " + str(index + 1) + "/10",
                                    description=f"**[{result['items'][index]['title']}]({result['items'][index]['image']['contextLink']})**", colour=int(hex_code, 0))
            timeout.set_image(url=result['items'][index]["link"])
            timeout.set_footer(text=" - Showing images for: " + search, icon_url="https://companieslogo.com/img/orig/GOOG-0ed88f7c.png?t=1633218227")
            timeout.set_author(name=userName, icon_url=userIMG)
            await interaction.edit_original_response(embed=timeout, view=None)

        view.on_timeout = on_timeout

    except UnidentifiedImageError:
        # If the first image is bad, try the next, if it is bad again, keep incrementing it.
        index = 1

        resource = build("customsearch", "v1", developerKey=googlekey).cse()
        result = resource.list(q=f"{search}", cx=cxsrc, searchType="image").execute()

        response = requests.get(result['items'][1]["link"], stream=True)
        image = Image.open(io.BytesIO(response.content))

        # Get the color of the top left pixel
        pixel = image.getpixel((0, 0))

        if type(pixel) == int:
            pixel = (pixel, pixel, pixel)
        # Convert the pixel color to a hex code
        hex_code = '0x{:02x}{:02x}{:02x}'.format(*pixel)

        left = Button(style=discord.ButtonStyle.primary, emoji="⬅")
        right = Button(style=discord.ButtonStyle.primary, emoji="➡")
        close = Button(style=discord.ButtonStyle.red, emoji="✖")
        imgURL = result['items'][1]['link']
        embed = discord.Embed(
            title="Showing Image 1/10",
            description=f"**[{result['items'][index]['title']}]({result['items'][index]['image']['contextLink']})**",
            colour=int(hex_code, 0)
        )
        userIMG = interaction.user.avatar
        userName = interaction.user.display_name
        embed.set_author(name=userName, icon_url=userIMG)
        embed.set_image(url=imgURL)
        embed.set_footer(text=" - Showing images for: " + search,
                         icon_url="https://companieslogo.com/img/orig/GOOG-0ed88f7c.png?t=1633218227")
        async def button_callback(interaction2: discord.Interaction):
            global index
            if interaction.user == interaction2.user:
                try:

                    if index > 0:
                        index -= 1

                    response = requests.get(result['items'][index]["link"], stream=True)
                    image = Image.open(io.BytesIO(response.content))


                    # Get the color of the top left pixel
                    pixel = image.getpixel((0, 0))
                    if type(pixel) == int:
                        pixel = (pixel, pixel, pixel)

                    # Convert the pixel color to a hex code
                    hex_code = '0x{:02x}{:02x}{:02x}'.format(*pixel)

                    prevImg = discord.Embed(title="Showing Image " + str(index + 1) + "/10",
                    description=f"**[{result['items'][index]['title']}]({result['items'][index]['image']['contextLink']})**",colour= int(hex_code, 0))
                    prevImg.set_footer(text=" - Showing images for: " + search, icon_url="https://companieslogo.com/img/orig/GOOG-0ed88f7c.png?t=1633218227")
                    prevImg.set_image(url=result['items'][index]["link"])
                    prevImg.set_author(name=userName, icon_url=userIMG)

                    await interaction.edit_original_response(view=view, embed=prevImg)
                    await interaction2.response.defer()
                except UnidentifiedImageError:
                    newIn = index + 1



                    response = requests.get(result['items'][newIn]["link"], stream=True)
                    image = Image.open(io.BytesIO(response.content))


                    # Get the color of the top left pixel
                    pixel = image.getpixel((0, 0))
                    if type(pixel) == int:
                        pixel = (pixel, pixel, pixel)

                    # Convert the pixel color to a hex code
                    hex_code = '0x{:02x}{:02x}{:02x}'.format(*pixel)
                    prevImg = discord.Embed(title="Showing Image " + str(index + 1) + "/10",
                                            description=f"**[{result['items'][index]['title']}]({result['items'][index]['image']['contextLink']})**",
                                            colour=int(hex_code, 0))
                    prevImg.set_footer(text=" - Showing images for: " + search, icon_url="https://companieslogo.com/img/orig/GOOG-0ed88f7c.png?t=1633218227")
                    prevImg.set_image(url=result['items'][newIn]["link"])
                    prevImg.set_author(name=userName, icon_url=userIMG)

                    await interaction.edit_original_response(view=view, embed=prevImg)
                    await interaction2.response.defer()
            else:
                hidden.set_author(name=interaction2.user.display_name, icon_url=interaction2.user.display_avatar)
                await interaction2.response.send_message(embed=hidden, ephemeral=True)


        async def button_callback2(interaction3: discord.Interaction):
            global index
            if interaction.user == interaction3.user:
                try:
                    if index < 9:
                        index += 1

                    response = requests.get(result['items'][index]["link"], stream=True)
                    image = Image.open(io.BytesIO(response.content))


                    # Get the color of the top left pixel
                    pixel = image.getpixel((0, 0))
                    if type(pixel) == int:
                        pixel = (pixel, pixel, pixel)

                    # Convert the pixel color to a hex code
                    hex_code = '0x{:02x}{:02x}{:02x}'.format(*pixel)

                    nextImg = discord.Embed(title="Showing Image " + str(index + 1) + "/10",
                    description=f"**[{result['items'][index]['title']}]({result['items'][index]['image']['contextLink']})**", colour= int(hex_code, 0))
                    nextImg.set_image(url=result['items'][index]["link"])
                    nextImg.set_footer(text=" - Showing images for: " + search, icon_url="https://companieslogo.com/img/orig/GOOG-0ed88f7c.png?t=1633218227")
                    nextImg.set_author(name=userName, icon_url=userIMG)
                    await interaction.edit_original_response(embed=nextImg, view=view)
                    await interaction3.response.defer()
                except UnidentifiedImageError:
                    if index < 9:
                        newIn = index + 1
                    else:
                        newIn = index - 1




                    response = requests.get(result['items'][newIn]["link"], stream=True)
                    image = Image.open(io.BytesIO(response.content))


                    # Get the color of the top left pixel
                    pixel = image.getpixel((0, 0))
                    if type(pixel) == int:
                        pixel = (pixel, pixel, pixel)

                    # Convert the pixel color to a hex code
                    hex_code = '0x{:02x}{:02x}{:02x}'.format(*pixel)
                    prevImg = discord.Embed(title="Showing Image " + str(index + 1) + "/10",
                                            description=f"**[{result['items'][index]['title']}]({result['items'][index]['image']['contextLink']})**",
                                            colour=int(hex_code, 0))
                    prevImg.set_footer(text=" - Showing images for: " + search, icon_url="https://companieslogo.com/img/orig/GOOG-0ed88f7c.png?t=1633218227")
                    prevImg.set_image(url=result['items'][newIn]["link"])
                    prevImg.set_author(name=userName, icon_url=userIMG)

                    await interaction.edit_original_response(view=view, embed=prevImg)
                    await interaction3.response.defer()
            else:
                hidden.set_author(name=interaction3.user.display_name, icon_url=interaction3.user.display_avatar)
                await interaction3.response.send_message(embed=hidden, ephemeral=True)


        async def button_callback3(interaction4: discord.Interaction):
            if interaction.user == interaction4.user:
                await interaction.delete_original_response()
                await interaction4.response.defer()
            else:
                hidden.set_author(name=interaction4.user.display_name, icon_url=interaction4.user.display_avatar)
                await interaction4.response.send_message(embed=hidden, ephemeral=True)
        left.callback = button_callback
        right.callback = button_callback2
        close.callback = button_callback3
        view = discord.ui.View(timeout=90)

        view.add_item(left)
        view.add_item(right)
        view.add_item(close)


        await interaction.response.send_message(embed=embed, view=view)

        async def on_timeout():
            timeout = discord.Embed(title="Showing Image " + str(index + 1) + "/10",
                                    description=f"**[{result['items'][index]['title']}]({result['items'][index]['image']['contextLink']})**", colour=int(hex_code, 0))
            timeout.set_image(url=result['items'][index]["link"])
            timeout.set_footer(text=" - Showing images for: " + search, icon_url="https://companieslogo.com/img/orig/GOOG-0ed88f7c.png?t=1633218227")
            timeout.set_author(name=userName, icon_url=userIMG)
            await interaction.edit_original_response(embed=timeout, view=None)

        view.on_timeout = on_timeout





# weatherkey = "981049732b67de408f8c936087425a9c" using web scraping instead
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

@tree.command(name="weather", description="Get the current weather status of any city.")
async def weather(interaction: discord.Interaction, location: str):


    city2 = location+ " weather"
    userName = interaction.user.display_name
    userIMG = interaction.user.display_avatar
    error = discord.Embed(title=":x: ERROR :x:", color=0xff1a1a)

    error.add_field(name=':warning: Error Message :warning:',
                    value="**Can't find the city: " + location + ".**\n\n Check the spelling and try again, or specify the country.\n\n         ",
                    inline=False)
    error.add_field(name=":tools: SUPPORT :tools:",
                    value="If you have any questions, suggestions or bug reports, join my support **[Discord Server](LINK)**",
                    inline=False)
    error.set_author(name=userName, icon_url=userIMG)
    error.set_footer(text=" - ERROR.",
                     icon_url="https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_3-512.png")


    city2 = city2.replace(" ", "+")
    try:
        res = requests.get(
            f'https://www.google.com/search?q={city2}&oq={city2}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
            headers=headers)
        # print("Searching...\n")
        soup = BeautifulSoup(res.text, 'html.parser')

        location = soup.select('#wob_loc')[0].getText().strip()
        time = soup.select('#wob_dts')[0].getText().strip()
        info = soup.select('#wob_dc')[0].getText().strip()
        weather = soup.select('#wob_tm')[0].getText().strip()
        status = soup.select('#wob_pp')[0].getText().strip()
        humidity = soup.select('#wob_hm')[0].getText().strip()
        # nextTimes = soup.find_all('div', attrs={'class': 'QrNVmd wob_hw'})
        nextDay = soup.find_all('div', attrs={'class': 'Z1VzSb'})
        gross = soup.find_all('span', attrs={'class': 'wob_t'})

        # Fetch the next 3 times in the day (they increment by 3 hrs)
        # t1 = nextTimes[0].getText()
        # t2 = nextTimes[1].getText()
        # t3 = nextTimes[2].getText()

        # Fetch the next 3 days
        d1 = nextDay[1].getText()
        d2 = nextDay[2].getText()
        d3 = nextDay[3].getText()


        # Fetch the next 3 days H/L
        lowC1 = gross[-30].getText()
        lowF1 = gross[-29].getText()

        highC1 = gross[-32].getText()
        highF1 = gross[-31].getText()

        lowC2 = gross[-26].getText()
        lowF2 = gross[-25].getText()

        highC2 = gross[-28].getText()
        highF2 = gross[-27].getText()

        lowC3 = gross[-22].getText()
        lowF3 = gross[-21].getText()

        highC3 = gross[-24].getText()
        highF3 = gross[-23].getText()

        cloudy = "https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_1-512.png"
        sunny = "https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_3-512.png"
        weatherEmbed = discord.Embed(
            title=f"Weather in {location}",
            url=f'https://www.google.com/search?q={city2}&oq={city2}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
            description=f"**{info}\n\u200b**",
            colour=discord.Colour.yellow()
        )
        userIMG = interaction.user.avatar
        userName = interaction.user.display_name

        weatherEmbed.set_author(name=userName, icon_url=userIMG)
        # Add images and support for day/night cycle
        revTime = time[::-1]
        hour = int(revTime[8])
        if hour == 0:
            hour = int(revTime[9] + "0")
        elif hour == 1 and revTime[9] == "1":
            hour = int(revTime[9] + "1")
        elif hour == 1 and revTime[9] == "2":
            hour = int(revTime[9] + "2")

        if info == "Cloudy" or info == "Mostly cloudy":
            weatherEmbed.set_thumbnail(url="https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_1-512.png")
            weatherEmbed.colour = 0xd9d9d9
        elif info == "Sunny":
            weatherEmbed.set_thumbnail(url=sunny)
            weatherEmbed.colour = 0xffdb29
        elif info == "Clear":
            if revTime[0:4] == ".m.a" and ((hour >= 1 and hour <= 6) or hour == 12):
                weatherEmbed.set_thumbnail(url="https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_4-512.png")
            elif revTime[0:4] == ".m.p" and (hour >= 9 and hour <= 11):
                weatherEmbed.set_thumbnail(
                    url="https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_4-512.png")
            else:
                weatherEmbed.set_thumbnail(url="https://cdn4.iconfinder.com/data/icons/weatherful/72/Sunny-512.png")
            weatherEmbed.colour = 0xffdb29
        elif info == "Clear with periodic clouds" or info == "Partly cloudy" or info == "Mostly sunny":
            if revTime[0:4] == ".m.a" and ((hour >= 1 and hour <= 6) or hour == 12):
                weatherEmbed.set_thumbnail(url="https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_50-512.png")
            elif revTime[0:4] == ".m.p" and (hour >= 9 and hour <= 11):
                weatherEmbed.set_thumbnail(
                    url="https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_50-512.png")
            else:
                weatherEmbed.set_thumbnail(url="https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_49-512.png")
            weatherEmbed.colour = 0xf0e6b2
        elif info == "Cloudy with brief rain":
            weatherEmbed.set_thumbnail(url="https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_13-512.png")
            weatherEmbed.colour = 0xc3e9f9
        elif info == "Snow" or info == "Snow showers" or info == "Light snow" or info =="Snow with brief sleet":
            weatherEmbed.set_thumbnail(url="https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_35-512.png")
            weatherEmbed.colour= 0xf5f5f5
        elif info == "Rain" or info == "Wind and rain":
            weatherEmbed.set_thumbnail(
                url="https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_16-512.png")
            weatherEmbed.colour = 0x2d60d7
        elif info == "Showers" or info == "Scattered showers" or info == "Light rain showers" or info =="Light drizzle":
            weatherEmbed.set_thumbnail(
                url="https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_6-512.png")
            weatherEmbed.colour = 0x93aeeb
        elif info == "Icy" or info == "Hail" or info == "Freezing drizzle" or info == "Chance of snow showers":
            weatherEmbed.set_thumbnail(
                url="https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_32-512.png")
            weatherEmbed.colour = 0xd4def7
        elif info == "Rain and snow":
            weatherEmbed.set_thumbnail(
                url="https://ssl.gstatic.com/onebox/weather/128/snow_s_rain.png")
            weatherEmbed.colour = 0xd4def7
        elif info == "Thunderstorm" or info == "Storm" or info =="Scattered thunderstorms" or info == "Heavy thunderstorm":
            weatherEmbed.set_thumbnail(
                url="https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_23-512.png")
            weatherEmbed.colour = 0x333333
        elif info == "Haze" or info == "Fog" or info == "Mist" or info =="Foggy" or info == "Smoke":
            weatherEmbed.set_thumbnail(
                url="https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_30-512.png")
            weatherEmbed.colour = 0xc2c2c2
        elif info == "Wind" or info == "Windy":
            weatherEmbed.set_thumbnail(
                url="https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_9-512.png")
            weatherEmbed.colour = 0xe0e0e0
        else:
            weatherEmbed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png")



        far1 = (int(weather)*(9/5)) + 32
        far = round(far1)
        weatherEmbed.add_field(name=f":thermometer: Temperature: {far}°F ({weather}°C)", value="\n\u200b")
        weatherEmbed.add_field(name=f":umbrella: Chance of Precipitation: {status}", value=f"\n\u200b", inline=False)
        weatherEmbed.set_footer(text=f"Retrieved weather information at {time} (Local Time).",icon_url="https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_3-512.png")
        weatherEmbed.add_field(name=f":fog: Humidity: {humidity}", value=f"\u200b\n\n**:small_red_triangle::small_red_triangle_down: High and Low (H/L) (Next 3 Days):**", inline=False)

        weatherEmbed.add_field(name=f":calendar_spiral:  {d1}.", value=f"**{highF1}°F/{lowF1}°F**\n({highC1}°C/{lowC1}°C)", inline=True)
        weatherEmbed.add_field(name=f":calendar_spiral:  {d2}.", value=f"**{highF2}°F/{lowF2}°F**\n({highC2}°C/{lowC2}°C)", inline=True)
        weatherEmbed.add_field(name=f":calendar_spiral:  {d3}.", value=f"**{highF3}°F/{lowF3}°F**\n({highC3}°C/{lowC3}°C)", inline=True)




        # print(location)
        # print("Hourly report at: " + time)
        # print(info)
        # print(weather + "°C")
        # print(high)
        # print(low)

        hidden = discord.Embed(
            title=":warning: Only the user of the command can interact with this embed. :warning:",
            color=discord.Colour.yellow()
        )

        hidden.set_footer(text="BluugBot", icon_url=client.user.display_avatar)
        async def button_callback3(interaction4: discord.Interaction):
            if interaction.user == interaction4.user:
                await interaction.delete_original_response()
                await interaction4.response.defer()
            else:
                hidden.set_author(name=interaction4.user.display_name, icon_url=interaction4.user.display_avatar)
                await interaction4.response.send_message(embed=hidden, ephemeral=True)

        close = Button(style=discord.ButtonStyle.red, emoji="✖")
        view = discord.ui.View(timeout=90)
        view.add_item(close)
        close.callback = button_callback3
        async def on_timeout():
            await interaction.edit_original_response(embed=weatherEmbed, view=None)

        view.on_timeout = on_timeout
        await interaction.response.defer()
        await asyncio.sleep(0.5)
        await interaction.followup.send(embed=weatherEmbed, view=view)
    except IndexError:
        await interaction.response.send_message(embed=error, ephemeral=True)

@tree.command(name="wikihow", description="Search for wikihow articles, presented to you in a list of steps, because why not...")
async def wikihow(interaction: discord.Interaction, search: str):

    userName = interaction.user.display_name
    userIMG = interaction.user.display_avatar
    error = discord.Embed(title=":x: ERROR :x:", color=0xff1a1a)

    error.add_field(name=':warning: Error Message :warning:',
                    value="**Can't find any article titled: " + search + ".**\n\n Check the spelling and try again, or be more specific.\n\n         ",
                    inline=False)
    error.add_field(name=":tools: SUPPORT :tools:",
                    value="If you have any questions, suggestions or bug reports, join my support **[Discord Server](LINK)**",
                    inline=False)
    error.set_author(name=userName, icon_url=userIMG)
    error.set_footer(text=" - ERROR.",
                     icon_url="https://upload.wikimedia.org/wikipedia/commons/f/fb/WikiHow_initials.png")
    # Make it fit the URL structure
    term = search.replace(' ', '+')
    try:
        res = requests.get(
            f'https://www.wikihow.com/wikiHowTo?search={term}',
            headers=headers)
        # print("Searching...\n")
        soup1 = BeautifulSoup(res.text, 'html.parser')


        firstURL = soup1.find('a', href=True, attrs= {'class': 'result_link'})

        clickURL = firstURL['href']
        getfirstURL = requests.get(firstURL['href'], headers=headers)
        thumbnailURL = soup1.find('div', attrs={'class': 'result_thumb'})
        removeExcess = str(thumbnailURL).replace('<div class="result_thumb" style="background-image: url(', "")
        removeExcess2 = removeExcess.replace(')">', "")
        IMAGEURL = removeExcess2.replace('</div>', "")


        soup2 = BeautifulSoup(getfirstURL.text, 'html.parser')
        embedTitle = soup2.find('h1', attrs={'id': 'section_0'})

        embed = discord.Embed(
            title=embedTitle.getText(),
            url=clickURL,
            colour=0x93B874
        )
        embed.set_thumbnail(url=IMAGEURL)



        stepsFind = soup2.findAll('div', {"id": "steps_1"})
        counter = 0
        save = "**Brief Steps:**\n"
        for textss in stepsFind:
            texts = textss.findAll("b", {"class": "whb"})
            for textss in texts:
                # print(textss)
                if textss.text == "." or textss.text[0] == " ":

                    pass
                elif textss.text[0] != (textss.text[0]).upper():

                    pass

                elif (textss.text[-1] != ".") and ((textss.text[0]).upper() == textss.text[0]):
                    counter += 1

                    save += "**" + str(counter) + "** • " + textss.text + ".\n"

                    embed.description = save
                else:

                    counter += 1
                    save += "**"+ str(counter) + "** • " + textss.text + "\n"
                    embed.description = save

        embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar)
        embed.set_footer(text=" - Information provided by WikiHow", icon_url="https://upload.wikimedia.org/wikipedia/commons/f/fb/WikiHow_initials.png")


        #printer = stepsFind.findChildren()
        #print(printer[0])
        #texts = printer[0].getText()
        #print(texts)
        # print(getfirstURL)
        # print(soup2)
        hidden = discord.Embed(
            title=":warning: Only the user of the command can interact with this embed. :warning:",
            color=discord.Colour.yellow()
        )

        hidden.set_footer(text="BluugBot", icon_url=client.user.display_avatar)

        async def button_callback3(interaction4: discord.Interaction):
            if interaction.user == interaction4.user:
                await interaction.delete_original_response()
                await interaction4.response.defer()
            else:
                hidden.set_author(name=interaction4.user.display_name, icon_url=interaction4.user.display_avatar)
                await interaction4.response.send_message(embed=hidden, ephemeral=True)

        close = Button(style=discord.ButtonStyle.red, emoji="✖")
        view = discord.ui.View(timeout=90)
        view.add_item(close)
        close.callback = button_callback3

        async def on_timeout():
            await interaction.edit_original_response(embed=embed, view=None)

        view.on_timeout = on_timeout
        await interaction.response.send_message(embed=embed, view=view)
    except IndexError:
        await interaction.response.send_message(embed=error, ephemeral=True)
    except AttributeError:
        await interaction.response.send_message(embed=error, ephemeral=True)


gglpng = "https://www.freepnglogos.com/uploads/google-logo-png/google-logo-png-suite-everything-you-need-know-about-google-newest-0.png"

@tree.command(name="google", description="Google things without leaving Discord.")
async def lu(interaction: discord.Interaction, search: str):

    userName = interaction.user.display_name
    userIMG = interaction.user.display_avatar
    error = discord.Embed(title=":x: ERROR :x:", color=0xff1a1a)

    error.add_field(name=':warning: Error Message :warning:',
                    value="**Can't find anything useful about: " + search + ".**\n\n Check the spelling and try again, or be more specific. (or just use Google :skull:)\n\n         ",
                    inline=False)
    error.add_field(name=":tools: SUPPORT :tools:",
                    value="If you have any questions, suggestions or bug reports, join my support **[Discord Server](LINK)**",
                    inline=False)
    error.set_author(name=userName, icon_url=userIMG)
    error.set_footer(text=" - ERROR.",
                     icon_url=gglpng)
    formatted = search.replace(" ", "+")
    url = f"https://www.google.com/search?q={formatted}&rlz=1C1CHBF_enCA917CA917&oq={formatted}&aqs=chrome.0.69i59l4j69i64j69i60l3.659j0j7&sourceid=chrome&ie=UTF-8"

    res = requests.get(
        url, headers=headers
    )

    soup = BeautifulSoup(res.text, 'html.parser')

    try:
        pageTitle = soup.findAll('div', attrs={'data-attrid': 'title'})

        subTitle = soup.findAll('div', attrs={'data-attrid': 'subtitle'})

        try:
            desc = soup.findAll('div', attrs={'class': 'kno-rdesc'})
            # gets title/header
            testExceptionTitle = pageTitle[0].getText()
            try:

                delete = (desc[0].getText()).replace("Description", "")
                formattedDesc = delete.replace("Wikipedia", "")

            except IndexError:
                otherDesc = soup.findAll('span', attrs= {'class': 'hgKElc'})
                delete = otherDesc[0].getText()
                formattedDesc = delete

            wikiLink = soup.findAll('a', attrs={'class': 'ruhjFe NJLBac fl'})

            try:
                #print("it is here")
                wikiURL = wikiLink[0]['href']
            except IndexError:

                fixTitle = (pageTitle[0].getText()).replace(" ", "_")
                wikiURL = f"https://en.wikipedia.org/wiki/{fixTitle}"



            embed = discord.Embed(
                title=pageTitle[0].getText(),
                url=wikiURL,
                colour=0xffa200,
                description=f"**{subTitle[0].getText()}**"
            )
            embed.set_author(name=userName, icon_url=userIMG)
            embed.set_footer(text="Showing results for: " + search, icon_url=gglpng)

            embed.add_field(name="\u200b", value=f"{formattedDesc} [Wikipedia]({wikiURL})")
            await interaction.response.send_message(embed=embed)
        except IndexError:

            try:
                pageTitle = soup.findAll('h2', attrs={'data-attrid': 'title'})
                desc = soup.findAll('div', attrs={'class': 'kno-rdesc'})

                delete = (desc[0].getText()).replace("Description", "")
                formattedDesc = delete.replace("Wikipedia", "")

                # REMOVE the --Google at the end of the info !!
                if formattedDesc[-1] == 'e':
                    formattedDesc = formattedDesc[:len(formattedDesc)-8]
                wikiLink = soup.findAll('a', attrs={'class': 'ruhjFe NJLBac fl'})
                try:
                    wikiURL = wikiLink[0]['href']
                except IndexError:

                    fixTitle = (pageTitle[0].getText()).replace(" ", "_")
                    wikiURL = f"https://en.wikipedia.org/wiki/{fixTitle}"
                embed = discord.Embed(
                    title=pageTitle[0].getText(),
                    url=wikiURL,
                    colour=0xffa200
                )
                embed.set_author(name=userName, icon_url=userIMG)
                embed.set_footer(text="Showing results for: " + search, icon_url=gglpng)

                embed.add_field(name="\u200b", value=f"{formattedDesc} [Wikipedia]({wikiURL})")
                await interaction.response.send_message(embed=embed)
            except IndexError:

                pageTitle = soup.findAll('div', attrs={'data-attrid': 'title'})
                subTitle = soup.findAll('div', attrs={'data-attrid': 'subtitle'})
                context = soup.findAll('h3', attrs={'class': 'LC20lb MBeuO MMgsKf'})
                ytlink = soup.findAll('h3', attrs={'class': 'H1u2de'})
                embed = discord.Embed(
                    title=pageTitle[0].getText(),
                    description= f"**{subTitle[0].getText()}**",
                    colour=0xffa200
                )
                for href in ytlink:
                    hrefurl = href.findAll('a', href=True)
                    finalURL = hrefurl[0]['href']
                    embed.url = finalURL

                embed.set_author(name=userName, icon_url=userIMG)
                embed.set_footer(text="Showing results for: " + search, icon_url=gglpng)

                embed.add_field(name="\u200b", value=f"[{context[0].getText()}]({finalURL})")
                await interaction.response.send_message(embed=embed)
    except IndexError:

        try:
            header = soup.findAll('span', attrs={'class': 'yKMVIe'})
            subHead = soup.findAll('div', attrs={'class': 'wx62f PZPZlf x7XAkb'})
            desc = soup.findAll('div', attrs={'class': 'kno-rdesc'})
            delete = (desc[0].getText()).replace("Description", "")
            formattedDesc = delete.replace("Wikipedia", "")

            wikiLink = soup.findAll('a', attrs={'class': 'ruhjFe NJLBac fl'})

            wikiURL = wikiLink[0]['href']
            embed = discord.Embed(
                title=header[0].getText(),
                description=f"**{subHead}**",
                url=wikiURL,
                colour=0xffa200
            )
            embed.set_author(name=userName, icon_url=userIMG)
            embed.set_footer(text="Showing results for: " + search, icon_url=gglpng)

            embed.add_field(name="\u200b", value=f"{formattedDesc} [Wikipedia]({wikiURL})")
            await interaction.response.send_message(embed=embed)
            try:
                pageTitle = soup.findAll('h2', attrs={'data-attrid': 'title'})
                desc = soup.findAll('div', attrs={'class': 'kno-rdesc'})

                delete = (desc[0].getText()).replace("Description", "")
                formattedDesc = delete.replace("Wikipedia", "")

                wikiLink = soup.findAll('a', attrs={'class': 'ruhjFe NJLBac fl'})

                wikiURL = wikiLink[0]['href']
                embed = discord.Embed(
                    title=pageTitle[0].getText(),
                    url=wikiURL,
                    colour=0xffa200
                )
                embed.set_author(name=userName, icon_url=userIMG)
                embed.set_footer(text="Showing results for: " + search, icon_url=gglpng)

                embed.add_field(name="\u200b", value=f"{formattedDesc} [Wikipedia]({wikiURL})")
                await interaction.response.send_message(embed=embed)
            except IndexError:
                await interaction.response.send_message(embed=error, ephemeral=True)
        except IndexError:
            await interaction.response.send_message(embed=error, ephemeral=True)


# make embed maker for servers
@tree.command(name="time", description="Get the current time of any location.")
async def lu(interaction: discord.Interaction, location: str):

    userName = interaction.user.display_name
    userIMG = interaction.user.display_avatar
    error = discord.Embed(title=":x: ERROR :x:", color=0xff1a1a)

    error.add_field(name=':warning: Error Message :warning:',
                    value="**Can't find this location: " + location + ".**\n\n Check the spelling and try again, or be more specific.\n\n",
                    inline=False)
    error.add_field(name=":tools: SUPPORT :tools:",
                    value="If you have any questions, suggestions or bug reports, join my support **[Discord Server](LINK)**",
                    inline=False)
    error.set_author(name=userName, icon_url=userIMG)
    error.set_footer(text=" - ERROR.",
                     icon_url=gglpng)
    if " " in location:
        fix = location.replace(" ", "+")
    else:
        fix = location
    formatted = fix + "+time"
    url = f"https://www.google.com/search?q={formatted}&rlz=1C1CHBF_enCA917CA917&ei=ysbAY7PvM6ylptQPh_mZmAw&ved=0ahUKEwiz_NLKxMP8AhWskokEHYd8BsMQ4dUDCA8&uact=5&oq={formatted}&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIHCAAQsQMQQzIKCAAQsQMQgwEQQzIFCAAQkQIyCwgAELEDEIMBEJECMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOg0IABCPARDqAhC0AhgBOg0ILhCPARDqAhC0AhgBOhEILhCABBCxAxCDARDHARDRAzoOCC4QgAQQsQMQxwEQ0QM6CwguEIAEELEDEIMBOggIABCABBCxAzoICAAQsQMQgwE6CgguEMcBEK8BEEM6BAgAEEM6BwguELEDEEM6DQguELEDEMcBENEDEEM6BwguENQCEEM6DAguEMcBEK8BEAoQQzoKCC4QsQMQ1AIQQzoECC4QQzoLCAAQgAQQsQMQgwE6DQguEMcBENEDENQCEEM6CAgAELEDEJECOhMILhCxAxCDARDHARDRAxDUAhBDOg4ILhDHARCxAxDRAxCABDoLCC4QgAQQxwEQrwFKBAhBGABKBAhGGABQAFiUCWDoCWgBcAF4AIABpwGIAYQJkgEDMy43mAEAoAEBsAEKwAEB2gEECAEYCg&sclient=gws-wiz-serp"

    res = requests.get(
        url, headers=headers
    )

    try:
        soup = BeautifulSoup(res.text, 'html.parser')
        timeFinder = soup.findAll('div', attrs={'class': 'gsrt vk_bk FzvWSb YwPhnf'})
        time = timeFinder[0].getText()
        place = (soup.findAll('span', attrs={'class':'vk_gy vk_sh'}))[0].getText()
        date = (soup.findAll('div', attrs={'class':'vk_gy vk_sh'}))[0].getText()
        response = requests.get(interaction.user.display_avatar.url, stream=True)
        image = Image.open(io.BytesIO(response.content))


        # Get the color of the top left pixel
        try:
            pixel = image.getpixel((0, 0))
        except UnidentifiedImageError:
            pixel = (0, 0, 0)

        if type(pixel) == int:
            pixel = (pixel, pixel, pixel)
        # Convert the pixel color to a hex code
        hex_code = '0x{:02x}{:02x}{:02x}'.format(*pixel)
        embed = discord.Embed(
            title=time,
            colour=int(hex_code, 0)
        )
        embed.set_author(name=place, icon_url=interaction.user.display_avatar,url=url)
        embed.set_footer(text=date)
        await interaction.response.send_message(embed=embed)
    except IndexError:
        await interaction.response.send_message(embed=error, ephemeral=True)

        
client.run(TOKEN)
