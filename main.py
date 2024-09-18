import discord
from openai import OpenAI

DISCORD_TOKEN = 'MT----'

ALLOWED_CHANNEL_IDS = [1234, 12345]

client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama', 
)


intents = discord.Intents.default()
intents.messages = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.event
async def on_message(message):
    
    if message.author == bot.user:
        return


    if message.channel.id in ALLOWED_CHANNEL_IDS:
        response = client.chat.completions.create(
            model="llama3.1",
            messages=[
                {"role": "user", "content": message.content},
            ]
        )


        answer = response.choices[0].message.content
        await message.channel.send(answer)


bot.run(DISCORD_TOKEN)
