import argparse, discord
from discord.ext import commands

# To hold global configuration and variables
from cogs.GlobalConfig import GlobalConfig

# Import cogs
from cogs.Music import Music

# Intents give us access to some additional discord moderation features
intents = discord.Intents.all()
client = commands.Bot(command_prefix="+", intents=intents)

# Load the global config which will run some file reads and set default variables
config = GlobalConfig()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# Add each of the cogs, passing in the configuration
client.add_cog(Music(client, config))

# Start bot
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process command line arguments')
    parser.add_argument("-C", "--config-file", action="store", dest="configFilePath", default="config.json", required=False, help="File to load config from")
    args = parser.parse_args()

    try:
        config.parseAll(args.configFilePath)
        client.run(config.OAuthToken)
        print('Closed')
    except Exception as e:
        print(e)
