import asyncio
import telegram
import os
from dotenv import load_dotenv
import datetime as dt

# load env vars
load_dotenv()
TELEGRAM_BOT_API_KEY = os.environ["TELEGRAM_BOT_API_KEY"]
YOUR_CHAT_ID = os.environ["YOUR_CHAT_ID"]
EXECUTION_CLIENT = os.environ["EXECUTION_CLIENT"]
BEACON_CLIENT = os.environ["BEACON_CLIENT"]

# mesasge template
def prepare_message(clients_stopped):
    # messages
    messages = []

    # today's date
    NOW = dt.datetime.today().isoformat()

    # messages list
    for client in clients_stopped:
        messages.append(f"ℹ️ {client} stopped, checked on {NOW}")

    # return messages
    return messages

# process checker
def check_process():
    # stopped processes list
    stopped_processes = []
    
    # check process
    execution = True if os.system(f'systemctl is-active --quiet {EXECUTION_CLIENT}') == 0 else False
    beacon = True if os.system(f'systemctl is-active --quiet {BEACON_CLIENT}') == 0 else False
    
    # if process is stopped, return which process(es) stopped
    if not execution: stopped_processes.append(EXECUTION_CLIENT)
    if not beacon: stopped_processes.append(BEACON_CLIENT)

    # return stopped processes
    return stopped_processes

# main
async def main():
    # load bot to make requests
    bot = telegram.Bot(TELEGRAM_BOT_API_KEY)
    
    # check process
    stopped_processes = check_process()

    # prepare messages
    if stopped_processes:
        messages = prepare_message(stopped_processes)

    async with bot:
        # send messages
        if stopped_processes:
            for message in messages:
                await bot.send_message(text=message, chat_id=YOUR_CHAT_ID)

# run main
asyncio.run(main())
