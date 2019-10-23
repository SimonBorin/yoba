from logger import log_print
from utils import send_typing_action


def start(bot, update):
    send_typing_action(bot, update)

    start_text = '''
    This is the Yet One Bot Assistant
    You can see the forked code here https://github.com/SimonBorin/yoba
    maintaining by @blooomberg
    origin by @Cuttlerat
    '''
    start_text = "\n".join([i.strip() for i in start_text.split('\n')])
    bot.send_message(chat_id=update.message.chat_id, text=start_text)


def bug(bot, update):
    send_typing_action(bot, update)

    bug_text = '''
    *Found a bug?*
    Please report it here: https://github.com/SimonBorin/yoba/issues/new
    '''
    bug_text = "\n".join([i.strip() for i in bug_text.split('\n')])
    bot.send_message(chat_id=update.message.chat_id,
                     text=bug_text,
                     parse_mode='markdown')


def chat_id(bot, update):
    send_typing_action(bot, update)

    current_chat_id = update.message.chat_id
    username = update.message.from_user.username
    bot.send_message(chat_id=current_chat_id,
                     text="`{0}`".format(current_chat_id),
                     reply_to_message_id=update.message.message_id,
                     parse_mode='markdown')
    log_print('Chat id {0}'.format(current_chat_id), username)


def prepare_message(update):

    raw_message = update.message.text
    if raw_message:
        pre_output = raw_message.lower().replace('ё', 'е')
        output = " ".join(["".join([letter for letter in word if letter.isalnum()])
                           for word in pre_output.split()])
        return output
    else:
        return ''
