#!/bin/bash

python3 -m venv ./ethclientchecker
source ./ethclientchecker/bin/activate
pip install -r requirements.txt
pip install python-telegram-bot -U --pre
echo -e "TELEGRAM_BOT_API_KEY=\"APIKEY\"\nYOUR_CHAT_ID=\"CHATID\"\nEXECUTION_CLIENT=\"SERVICE_NAME\"\nBEACON_CLIENT=\"SERVICE_NAME\"" > .env && rm .env.template
