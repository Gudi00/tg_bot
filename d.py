
from pyrogram import Client, filters

API_ID = '26118223'
API_HASH = '8423f1b169ea4515e0b2b5127fc92da0'
PHONE_NUMBER = '+375257661287'

RESPONSE = "Иосько Михаил Алексеевич, 428504"
RESPONSE_NOT_MY = "Марчук Кирилл Геннадьевич, 428504"

app = Client("my_account", api_id=API_ID, api_hash=API_HASH, phone_number=PHONE_NUMBER)


def message_check(message_list, message):
    for mess in message_list:
        if mess in message.text.lower():
            return True
    return False




@app.on_message(filters.text & filters.group)
async def reply1(client, message):
    greet_list = ['всем привет', 'добрый день', 'нужно', 'нужны', 'надо']
    reward_list = ['ходат', 'мероприя']
    if message_check(greet_list, message) and message_check(reward_list, message):
        await message.reply(RESPONSE)
        await message.reply(RESPONSE_NOT_MY)

app.run()

