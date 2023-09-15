from pytgbot import Bot
import subprocess
import logging


logger = logging.getLogger(__name__)

API_KEY='6378447719:AAE1zkspCK7T2uiJcXhHQnfRntiNOHrRnBU'  # change this to the token you get from @BotFather
CHAT_ID=''  # can be a @username or a id, change this to your own @username or id for example.

bot = Bot(API_KEY)

# get uptime of server
def uptime():
    upTime = subprocess.check_output(['uptime']).decode('UTF-8')
    return upTime

# send message on start bot
def start_bot():
    bot.send_message(CHAT_ID, "Example Text!")

# help messages
def help():
    msg = '''
Server Uptime Bot
---------
Uptime  → /uptime
---------
    '''
    return msg

# Check if we have connection to internet
def ping_check():
    for ping in range(1,100):
        address = "https://last-version.lon99999999.repl.co/"
        res = subprocess.call(['ping', '-c', '5', address])
        if res == 0:
            print ("ping to", address, "OK")
            return True
        else:
            print ("ping to", address, "failed!")
    return False


# reply to message
def request_bot():
    last_update_id = -1
    while True:
        # loop forever.
        for update in bot.get_updates(limit=100, offset=last_update_id+1, poll_timeout=30):
            last_update_id = update.update_id
            print("got message: {msg}".format(msg=update))
            if not "message" in update:
                continue
            message = update.message
            if not "text" in message:
                continue
            logger.debug("got text: {msg}".format(msg=message.text.encode("utf-8")))
            if not message.text == "/uptime":
                bot.send_message(CHAT_ID, help())
                continue
            #origin = message.chat.id if "chat" in message else message.from_peer.id
            bot.send_message (CHAT_ID, uptime())

def main():
    if ping_check():
        start_bot()
        request_bot()

if __name__ == '__main__':
    main()

