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


def nsfw(bot, update):
    send_typing_action(bot, update)

    start_text = '''
    Опять тут сеськаме чужими кидаетесь
    бестолочи окоянные!
    И как вам не стыдно то рукоблудить
    при чесном народе!!!!
    БОООХНАКАЖЕТ!!!!
          |V|
       .::| |::.
      ::__| |__::
     >____   ____<
      ::  | |  ::
       '::| |::'
          | |
          | |
          |A|
    Господи, утверди в вере сей сердце мое 
    и сердца всех православных христиан; 
    сей веры и сего чаяния жити достойно вразуми; 
    соедини в вере сей все великие 
    общества христианские, 
    бедственно отпадшие от единства 
    Святой Православной Кафолической Церкви, 
    яже есть Тело Твое и ее же Глава 
    еси Ты и Спаситель Тела; 
    низложи гордыню и противление учителей их 
    и последующих им; 
    даруй им сердцем уразуметь истину 
    и спасительность Церкви Твоей и 
    нелестно ей соединиться; 
    совокупи Твоей Святой Церкви 
    и недугующих невежеством, 
    заблуждением и упорством раскола, 
    сломив силою благодати Духа Твоего 
    упорство их и противление Истине Твоей, 
    да не погибнут люте в своем противлении, 
    якоже Корей, Дафан и Авирон, 
    противившиеся Моисею и Аарону, 
    рабам Твоим. К сей вере привлецы все языцы, 
    населяющие землю, да единым сердцем 
    и едиными усты все языцы прославят Тебя, 
    Единого всех Бога и Благодетеля; 
    в сей вере и нас всех соедини духом кротости, 
    смирения, незлобия, простоты, бесстрастия, 
    терпения, долготерпения, милосердия, 
    соболезнования и сорадования. 
    Аминь.

 
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
