"""Bot flask app."""
from microsoftbotframework import MsBot
from tasks import handle_response

bot = MsBot()
bot.add_process(handle_response)

if __name__ == '__main__':
    bot.run()
