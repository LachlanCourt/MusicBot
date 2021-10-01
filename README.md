# Discord Music Bot

This bot is designed to work either standalone, or as a submodule, hence the funky directory structure

## To set up standalone

1. Install requirements

        pip install -r requirements.txt

2. Create configuration file from example

        cp config.json.example config.json

3. Generate OAuth Token (see [here](https://discord.com/developers/applications)) and populate config.json

4. Run bot!

        python3 bot.py

## To set up as a submodule of an existing bot

1. Navigate to the `cogs` directory of your bot, or wherever you store your cogs

2. Add submodule

        git add submodule https://github.com/LachlanCourt/MusicBot Music

3. Update gitmodules to use release branch by adding `branch = release` to gitmodules entry or run the following command from the project root

        git config -f .gitmodules submodule.cogs/Music.branch release && git submodule update --remote

4. Install requirements

        pip install -r requirements.txt

5. Include the music cog in your program and run bot!