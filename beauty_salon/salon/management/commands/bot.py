# from telegram import InlineKeyboardButton, InlineKeyboardMarkup
#
# # from tgbot.handlers.onboarding.manage_data import SECRET_LEVEL_BUTTON
# # from tgbot.handlers.onboarding.static_text import github_button_text, secret_level_button_text
#
#
# def make_keyboard_for_start_command() -> InlineKeyboardMarkup:
#     # buttons = [[
#     #     InlineKeyboardButton(github_button_text, url="https://github.com/ohld/django-telegram-bot"),
#     #     InlineKeyboardButton(secret_level_button_text, callback_data=f'{SECRET_LEVEL_BUTTON}')
#     # ]]
#     #
#     # return InlineKeyboardMarkup(buttons)
#
#
#     # markup = InlineKeyboardMarkup(row_width=2)
#     buttons = [[
#         InlineKeyboardButton('Связаться с салоном', callback_data='call_us'),
#         InlineKeyboardButton('О нас', callback_data='about_us'),
#         InlineKeyboardButton('Записаться', callback_data='sing_up'),
#         InlineKeyboardButton('Оставить отзыв', callback_data='leave_review')
#     ]]
#     # bot.send_message(message.chat.id, '\nвыбери нужный пункт', reply_markup=markup)
#     return InlineKeyboardMarkup(buttons)


from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import Bot, Update
from telegram.utils.request import Request
from telegram.ext import Updater, CallbackContext, Filters, MessageHandler
# from beauty_salon.salon.models import Clients

# def log_errors(f):
#     def inner(*args, **kwargs):
#         try:
#             return f(*args,**kwargs)
#         except Exception as e:
#             error_message = f'Произошла ошибка: {e}'
#             print(error_message)
#             raise e
#
#     return inner()
#
#
# @log_errors
# def do_echo(update: Update, context: CallbackContext):
#     chat_id = update.message.chat_id
#     text = update.message.text
#
#     p,_ = Clients.objects.get_or_create(
#         id=chat_id,
#     defaults={'name': update.message.from_user.username,
#               }
#     )
#
#     repty_text = "Ваш ID = {}\n\n\{}".format(chat_id, text)
#     update.message.reply_text(
#         text=repty_text,
#     )


class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args, **options):
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
        )
        bot = Bot(
            request=request,
            token='5270546430:AAGNCVmh3fo6HpfE98Za9Ts89hTtfOfOV6o',
            # token=settings.TOKEN,
            # base_url=settings.PROXY_URL,
        )
        print(bot.get_me())

        updater = Updater(bot=bot,use_context=True)
        message_handler = MessageHandler(Filters.text, callback='dsfdsg')
        # message_handler = MessageHandler(Filters.text, do_echo)
        updater.dispatcher.add_handler(message_handler)

        updater.start_polling()
        updater.idle()


# def main():
#     while True:
#         try:
#             bot.polling(none_stop=True)
#         except Exception as error:
#             print(error)
#             time.sleep(5)
#
#
# if __name__ == '__main__':
#     main()



# from django.core.management.base import BaseCommand
# from telegram.ext import Updater, CommandHandler
#
#
# def start(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your Telegram bot.")
#
#
# class Command(BaseCommand):
#     help = 'Starts the Telegram bot'
#
#     def handle(self, *args, **kwargs):
#         updater = Updater(token='6058652254:AAH_ztWwYLknDzhtdxysbPBxjyz0xOE4ngo', use_context=True)
#         dispatcher = updater.dispatcher
#         dispatcher.add_handler(CommandHandler('start', start))
#         print(dispatcher)
#         updater.start_polling()

# from typing import Union, Optional, Dict, List
#
# import telegram
# from telegram import MessageEntity, InlineKeyboardButton, InlineKeyboardMarkup
#
# from dtb.settings import TELEGRAM_TOKEN
# from users.models import User
#
#
# def from_celery_markup_to_markup(celery_markup: Optional[List[List[Dict]]]) -> Optional[InlineKeyboardMarkup]:
#     markup = None
#     if celery_markup:
#         markup = []
#         for row_of_buttons in celery_markup:
#             row = []
#             for button in row_of_buttons:
#                 row.append(
#                     InlineKeyboardButton(
#                         text=button['text'],
#                         callback_data=button.get('callback_data'),
#                         url=button.get('url'),
#                     )
#                 )
#             markup.append(row)
#         markup = InlineKeyboardMarkup(markup)
#     return markup