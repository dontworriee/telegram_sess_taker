from telethon import TelegramClient
import os

api_id = '27081922'
api_hash = '402702c34e957d67bc1a9a61925ebf72'

session_folder = 'sess'
os.makedirs(session_folder, exist_ok=True)

session_name = os.path.join(session_folder, input('Название сессии: '))

client = TelegramClient(session_name, api_id, api_hash)

async def main():
    await client.start()
    print("Вы успешно авторизованы!")

    me = await client.get_me()
    print(f'Привет, {me.first_name}!')

    await client.disconnect()

with client:
    client.loop.run_until_complete(main())