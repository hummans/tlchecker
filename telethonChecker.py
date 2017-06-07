from telethon import TelegramClient
from telethon.tl.functions.auth import check_phone
import time

api_id   = 143159
api_hash = 'e1f978e828363b22a6bd7d482c540ca8'
#phone    = '+79003845427'
phone    = '+79226727926'

client = TelegramClient('+79226727926', api_id, api_hash)
client.connect()

# Ensure you're authorized
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

f = open('phones.txt', 'r')

for phone in f:
    print(phone.strip("\n") + ";" + str(client.invoke(check_phone.CheckPhoneRequest(phone)).phone_registered))
    time(1000)


#client.disconnect()