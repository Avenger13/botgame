import telebot
import config
from telebot import types
from gamesingle import GameSingle

bot = telebot.TeleBot(config.token)

games_map = {}

mrk_create_game = types.ReplyKeyboardMarkup()
mrk_create_game.row('/game')

mrk_hide = types.ReplyKeyboardHide()


def make_mrk(q):
    mrk = types.ReplyKeyboardMarkup()
    for k in q.vargs:
        mrk.row(k)
    mrk.row('/end')
    return mrk


def usr_null(chatid):
    bot.send_message(chatid, 'Ассаламалейкум'
                     + '. Давай проверим твои знания !\n'
                     + 'Но я не знаю как тебя зовут :(.'
                     + '\nДля того, чтобы играть, ты должен выбрать себе ник в настройках Телеграм.'
                     + '\nПожалуйста, зайди в настройки, заполни поле \"Имя пользователя\" и начни играть ! '
                     ,
                     reply_markup=mrk_create_game)


@bot.message_handler(commands=['start', 'game', 'end'])
def echo_commands(cmd):
    user = cmd.chat.username
    chatid = cmd.chat.id
    if user is None:
        usr_null(chatid)
        return
    if cmd.text == '/start':
        bot.send_message(cmd.chat.id, 'Ассаламалейкум, ' + user + '. Давай проверим твои знания !',
                         reply_markup=mrk_create_game)
    # Начать новую игру
    elif cmd.text == '/game':
        if check_game(user):
            bot.send_message(cmd.chat.id, 'Вы уже играете !')
        else:
            bot.send_message(cmd.chat.id, 'Игра началась.')
            g = setup_game(user, chatid)
            _next(g)

    elif cmd.text == '/end':
        games_map[user] = None
        bot.send_message(cmd.chat.id, 'Вы завершили игру', reply_markup=types.ReplyKeyboardHide())


def _next(g):
    g.next()
    if g.status == 2:
        games_map[g.uname] = None
        bot.send_message(g.chatid, 'Поздравляем, '
                         + g.uname
                         + ', Вы выиграли ! ! !'
                         + '\n'
                         + 'И набрали '
                         + str(g.score)
                         + ' балла', reply_markup=mrk_create_game)
        return
    reply_markup = make_mrk(g.cq)
    bot.send_message(g.chatid, g.cq.q, reply_markup=reply_markup)


@bot.message_handler(content_types=['text'])
def handler_game_answers(ans):
    user = ans.chat.username
    chatid = ans.chat.id
    if user is None:
        usr_null(chatid)
        return
    game = None
    if check_game(user):
        game = games_map[user]
        print('your ans is ' + ans.text)
        if game.cq.is_right(ans.text):
            bot.send_message(chatid, 'Правильно ! Ответ - ' + game.cq.right + '\n\n')
            game.score += 1
            print('your ans is correct')
            _next(game)
            return
        else:
            for v in game.cq.vargs:
                if v == ans.text:
                    games_map[user] = None
                    bot.send_message(chatid,
                                     'К сожалению, Вы ответили неверно. Правильный ответ - '
                                     + game.cq.right
                                     + '\nВы набрали '
                                     + str(game.score)
                                     + ' балл(а, ов)',
                                     reply_markup=mrk_create_game)
                    return

            bot.send_message(chatid, 'Пожалуйста, выберите один из предложенных вариантов, либо завершите текущую игру, отправив команду /end')
            return

    else:
        bot.send_message(chatid, 'Вы еще не играете? Создайте игру, Вам понравится !',
                         reply_markup=mrk_create_game)
        return


def setup_game(uname, chatid):
    g = GameSingle(uname, chatid)
    games_map[uname] = g
    g.start_game()
    return g


def check_game(key):
    for k in games_map.keys():
        if key == k and games_map[key] is not None:
            return True
    return False


if __name__ == '__main__':
    bot.polling(none_stop=True)
