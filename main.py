import telebot
import config
import hot



from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):

# keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Я знаю что я хочу")



    item2 = types.KeyboardButton("Я не знаю что я хочу")

    markup.add(item1, item2)



    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, этот бот созданный чтобы помогать вам в готовке.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def x(message):
    if message.chat.type == 'private':
        if message.text == 'Я знаю что я хочу':
            bot.send_message(message.chat.id, 'что вы хотите?')




        elif message.text == 'Я не знаю что я хочу':

            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Супы", callback_data='1')
            bot.send_message(message.chat.id, 'вот что могу предложить ')
            item2 = types.InlineKeyboardButton("Горячие блюда", callback_data='2')
            item3 = types.InlineKeyboardButton("Салаты", callback_data='3')

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, 'смотри', reply_markup=markup)


        else:
            bot.send_message(message.chat.id, 'Я не знаю что вам ответить 😢')




@bot.callback_query_handler(func=lambda call: True)

def callback_inline(call):
    try:
        if call.message:

            if call.data == '1':
                markup = types.InlineKeyboardMarkup(row_width=4)
                itemz = types.InlineKeyboardButton("куриный", callback_data='444')
                itemx = types.InlineKeyboardButton("борщ", callback_data='555')
                itemc = types.InlineKeyboardButton("шурпа", callback_data='888')

                markup.add(itemz, itemx,itemc)
                bot.send_message(call.message.chat.id, 'какой суп вы хотите?', reply_markup=markup)

            elif call.data == '2':
                markup = types.InlineKeyboardMarkup(row_width=4)
                itemq = types.InlineKeyboardButton("сковорода", callback_data ='666')
                itemw = types.InlineKeyboardButton("духовка", callback_data ='777')
                markup.add(itemq, itemw)
                bot.send_message(call.message.chat.id, 'в чем будем готовить?', reply_markup=markup)
            if call.data == '666':

                markup = types.InlineKeyboardMarkup(row_width=4)
                item5 = types.InlineKeyboardButton("курица", callback_data='111')
                item6 = types.InlineKeyboardButton("говядина", callback_data='222')
                item7 = types.InlineKeyboardButton("свинина", callback_data='333')
                markup.add(item5, item6, item7)
                bot.send_message(call.message.chat.id, 'смотри', reply_markup=markup)

            if call.data =='777':
                markup = types.InlineKeyboardMarkup(row_width=4)
                item5 = types.InlineKeyboardButton("курица", callback_data='121')
                item6 = types.InlineKeyboardButton("говядина", callback_data='221')
                item7 = types.InlineKeyboardButton("свинина", callback_data='133')
                markup.add(item5, item6, item7)
                bot.send_message(call.message.chat.id, 'смотри', reply_markup=markup)
            if call.data == '133':
                bot.send_message(call.message.chat.id, str(hot.z))
            if call.data == '333':
                    bot.send_message(call.message.chat.id, str(hot.h))
            if call.data == '221':
                    bot.send_message(call.message.chat.id, str(hot.o))



            elif call.data == '3':
                markup = types.InlineKeyboardMarkup(row_width=4)
                item0 = types.InlineKeyboardButton("горячие", callback_data='424')
                item01 = types.InlineKeyboardButton("холодные", callback_data='721')

                markup.add(item0, item01)
                bot.send_message(call.message.chat.id, 'какие салаты вы хотите?', reply_markup=markup)

        if call.data == '424':
            bot.send_message(call.message.chat.id, str(hot.y))
        if call.data == '721':
            bot.send_message(call.message.chat.id, str(hot.p))

        if call.data == '222':
                bot.send_message(call.message.chat.id, str(hot.l))





        if call.data == '111':
            bot.send_message(call.message.chat.id, str(hot.a))


        if call.data == '121':
             bot.send_message(call.message.chat.id, str(hot.b))
        if call.data == '444':
                        bot.send_message(call.message.chat.id, str(hot.c))
        if call.data == '555':
            bot.send_message(call.message.chat.id, str(hot.d))
        if call.data == '888':
                bot.send_message(call.message.chat.id, str(hot.e))






    #finally:
       # pass







    except Exception as e:
                print(repr(e))


# RUNq
bot.polling(none_stop=True)

