from discord_webhook import DiscordEmbed, DiscordWebhook
from pystyle import Col, Colorate, Colors
from os import name, system
from pycenter import center
import string
import random


def clear():
    system("cls" if name == 'nt' else "clear")


if name == 'nt':
    system("title Hibana & mode 180, 40")


banner = """\n
:::    ::: ::::::::::: :::::::::      :::     ::::    :::     :::     
:+:    :+:     :+:     :+:    :+:   :+: :+:   :+:+:   :+:   :+: :+:   
+:+    +:+     +:+     +:+    +:+  +:+   +:+  :+:+:+  +:+  +:+   +:+  
+#++:++#++     +#+     +#++:++#+  +#++:++#++: +#+ +:+ +#+ +#++:++#++: 
+#+    +#+     +#+     +#+    +#+ +#+     +#+ +#+  +#+#+# +#+     +#+ 
#+#    #+#     #+#     #+#    #+# #+#     #+# #+#   #+#+# #+#     #+# 
###    ### ########### #########  ###     ### ###    #### ###     ### 
"""
banner1 = """
 ________________
|                |
|    NitroGen    |
|________________|
      " 1 "
"""



print(Colorate.Vertical(Colors.red_to_black, center(banner, space=60), stop=20))
print(Colorate.Vertical(Colors.red_to_black, center(banner1, space=85), stop=20))
amount = int(input('Number of Gen: '))
for i in range(amount):
    value = 1
    nitro = ''.join([random.choice(string.digits + string.ascii_letters) for x in range(16)])
    webhook = DiscordWebhook("https://discordapp.com/api/webhooks/893240716959039578/svVmfo9YyS9AXNOG3pruEJzGR0tAu0iFfjYaREUWOzbY94swechxnakWxh0I_JQ1hEjH")
    embed = DiscordEmbed(title='Nitro', description='Gen', color='6609b3')
    embed.set_author(name='https://github.com/Kyoto1337', url='https://github.com/Kyoto1337', icon_url='https://cdn.discordapp.com/attachments/878365772752240704/893220480721514516/a_78ab6aefb57d2c3e73b3cfadf4d4c9f8.gif')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/878365772752240704/893220480721514516/a_78ab6aefb57d2c3e73b3cfadf4d4c9f8.gif')
    embed.set_image(url='https://cdn.discordapp.com/attachments/878365772752240704/893372837698605086/p1_3054850_5dd86c97.gif')
    embed.add_embed_field(name='NitroGenV1', value='https://discord.gift/'+nitro)
    embed.set_timestamp()
    webhook.add_embed(embed)
    response = webhook.execute()
print(f"Generated {amount} codes\n")    


