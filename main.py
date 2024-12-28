from local_setting import *
from pyrogram import Client, filters
from method import Owner, Members
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
    cli = Members()
    month = cli.get_month(n.month)
    if message.text == "تاریخ" or "date":
        await message.reply(f"امروز:\n {n.day} - {month} - {n.year} - {n.jmonth}")
    elif message.text == "ban" and admin.ban() == True:
        await message.reply("hello")
    

if __name__ == "__main__":
    app.run()