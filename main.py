import os
import discord
import responses
from keep_alive import keep_alive

my_secret = os.environ['TOKEN']

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def send_message(message,user_message,is_private):
  try:
    response=responses.handle_response(user_message)
    await message.author.send(response) if is_private else await message.channel.send(response)
  except Exception as e:
    print(e)

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
    
  username=str(message.author)
  user_message=str(message.content)
  channel=str(message.channel)

  print(f"{username} said: '{user_message}' ({channel})")

  if user_message[0]=='?':
    user_message=user_message[1:]
    await send_message(message,user_message,is_private=True)
  else:
    await send_message(message,user_message,is_private=False)

keep_alive()
client.run(my_secret)