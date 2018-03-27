"""Bot flask app."""
from microsoftbotframework import MsBot
from tasks import handle_response, init_conversation, create_conversation

bot = MsBot()
bot.add_process(create_conversation)
bot.add_process(init_conversation)
bot.add_process(handle_response)

if __name__ == '__main__':
    bot.run()
