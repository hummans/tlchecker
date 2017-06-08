from telethon import TelegramClient
from telethon.tl.functions.auth import check_phone
import time

def write_phones(data):
    with open('ckeck.txt', 'w', encoding='cp1251') as f:
        f.write(data)

api_id   = 143159
api_hash = 'e1f978e828363b22a6bd7d482c540ca8'
phone    = '+79003845427'
#phone    = '+79226727926'

client = TelegramClient('+79226727926', api_id, api_hash)
client.connect()

# Ensure you're authorized
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

f = open('phones.txt', 'r')
data = ''
check_result = ''
for phone in f:
    try:
        check_result = str(client.invoke(check_phone.CheckPhoneRequest(phone)).phone_registered)
    except Exception:
        check_result = 'False'
    data += phone.strip("\n") + ";" + check_result
    print(phone.strip("\n") + ";" + check_result)
    time.sleep(5)
write_phones(data)
print('***successes***')


#client.disconnect()