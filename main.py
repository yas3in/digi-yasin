from local_setting import *
from pyrogram import Client, filters
from method import Owner
import jdatetime


app = Client("digi", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)


# for start command
@app.on_message(filters.command(['start']))
async def echo(client, message):
    print(message.chat.id)
    await message.reply("hello")
    

@app.on_message(filters.group)
async def manage(client, message):
    admin = Owner(message.from_user.id)
    n = jdatetime.date.today()
    if message.text == "تاریخ":
        await message.reply(f"امروز: {n.day} - {n.month} - {n.year}")
    elif message.text == "ban" and admin.ban() == True:
        await message.reply("hello")
    

if __name__ == "__main__":
    app.run()