import discord
from discord import app_commands 


class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False 

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: 
            await tree.sync() 
            self.synced = True
        print(f"Logged in as {self.user}.")

aclient = client()
tree = app_commands.CommandTree(aclient)

@tree.command(name = 'github', description='Check out my GitHub') 
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"https://github.com/NyctoRAA", ephemeral = True) 
    
  

aclient.run('MTA0NTgzNDE3NTE0OTc4MTA3Mg.Gk3q73.a2Tq9obod8TuUqz9gbvCU7iph_Z1RzHlCI5AKI')