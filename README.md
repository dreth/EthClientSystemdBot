# Ethereum client systemd process checker telegram bot

Simple telegram bot that checks whether a process is active or not and notifies if inactive

1. Create a telegram bot using @botfather and get your api key 

2. Create venv

```bash
python3 -m venv ./ethclientchecker
```

2. Activate the new env

```bash
source ./ethclientchecker/bin/activate
```

3. Install requirements

```bash
pip install -r requirements.txt
```

As well as the [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) library version v20.x:

```bash
pip install python-telegram-bot -U --pre
```

4. Add telegram API to the .env file, I provided a template, but this command will create a new one with the needed environment variables, just replace  `APIKEY` with your telegram bot API key and `CHATID` with your chat ID (this [thread](https://stackoverflow.com/questions/41664810/how-can-i-send-a-message-to-someone-with-my-telegram-bot-using-their-username) in stackoverflow details how you can get that) as well as the execution and beacon client systemd service names. Note that this command will make it so that your API key and Chat id appear in your shell history so keep this in mind when running this command. If you don't want this just run the command without your API key and chat id and edit it with an editor like nano or vim.

```bash
echo -e "TELEGRAM_BOT_API_KEY=\"APIKEY\"\nYOUR_CHAT_ID=\"CHATID\"\nEXECUTION_CLIENT=\"SERVICE_NAME\"\nBEACON_CLIENT=\"SERVICE_NAME\"" > .env && rm .env.template
```

5. Add a cron job to run this once every five minutes, when it runs, you should receive a message from the bot if any of the clients you're running are down

```bash
crontab -e
```

And add the following line editing the path to the cloned repo:

```bash
*/5 * * * * /path/to/cloned/repo/ethclientchecker/bin/python /path/to/cloned/repo/check_clients.py
```

I added a bash script to the root of the repo (`initial_setup.sh`) which runs all commands before step 6, you must run this script with `source initial_setup.sh` or `. initial_setup.sh` in bash.
