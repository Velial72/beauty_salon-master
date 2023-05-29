from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import Bot
from telegram.ext import Updater

# from beauty_salon.beauty_salon.settings import TELEGRAM_TOKEN
# from tgbot.dispatcher import setup_dispatcher

token='5270546430:AAGNCVmh3fo6HpfE98Za9Ts89hTtfOfOV6o'
def make_keyboard_for_start_command() -> InlineKeyboardMarkup:
    # buttons = [[
    #     InlineKeyboardButton(github_button_text, url="https://github.com/ohld/django-telegram-bot"),
    #     InlineKeyboardButton(secret_level_button_text, callback_data=f'{SECRET_LEVEL_BUTTON}')
    # ]]
    #
    # return InlineKeyboardMarkup(buttons)


    # markup = InlineKeyboardMarkup(row_width=2)
    buttons = [[
        InlineKeyboardButton('Связаться с салоном', callback_data='call_us'),
        InlineKeyboardButton('О нас', callback_data='about_us'),
        InlineKeyboardButton('Записаться', callback_data='sing_up'),
        InlineKeyboardButton('Оставить отзыв', callback_data='leave_review')
    ]]
    # bot.send_message(message.chat.id, '\nвыбери нужный пункт', reply_markup=markup)
    return InlineKeyboardMarkup(buttons)

def run_polling(tg_token: str = token):
    """ Run bot in polling mode """
    updater = Updater(tg_token, use_context=True)

    # dp = updater.dispatcher
    # dp = setup_dispatcher(dp)

    bot_info = Bot(tg_token).get_me()
    bot_link = f"https://t.me/{bot_info['username']}"

    print(f"Polling of '{bot_link}' has started")
    # it is really useful to send '👋' emoji to developer
    # when you run local test
    # bot.send_message(text='👋', chat_id=<YOUR TELEGRAM ID>)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    run_polling()