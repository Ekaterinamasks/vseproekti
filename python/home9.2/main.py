
import telebot
from telebot import types

TOKEN = ""
bot=telebot.TeleBot(TOKEN)

num_1 =''
num_2 =''
symbol=''
result=None

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 начать вычесления")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот,умею мало но я очень перспективный,мной активно занимаются".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "👋 начать вычесления"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id ,  "введи число", reply_markup=markup)
        bot.register_next_step_handler(msg,proces_num1_step)
    elif(message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Когда будет функция для работы с рациональными и комплексными числами?")
        btn2 = types.KeyboardButton("Что я могу?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
    
    elif(message.text == "Когда будет функция для работы с рациональными и комплексными числами?"):
        bot.send_message(message.chat.id, "тогда когда мои создатели разберутся с этой темой...")
    
    elif message.text == "Что я могу?":
        bot.send_message(message.chat.id, text="вычилсять выражения + - / * ** % ")
    
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
        button1 = types.KeyboardButton("👋 начать вычесления")
        button2 = types.KeyboardButton("❓ Задать вопрос")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")
        return

@bot.message_handler(message='начать вычесления')


def proces_num1_step(message,result=None):
    try:
        global num_1
     
        if result==None:
            num_1 = str(message.text) 
        else:
            num_1 = str(result)

        markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=4)
        itembtn1=types.KeyboardButton('+')
        itembtn2=types.KeyboardButton('-')
        itembtn3=types.KeyboardButton('*')
        itembtn4=types.KeyboardButton('/')
        itembtn5=types.KeyboardButton('**')
        itembtn6=types.KeyboardButton('%')

        markup.add(itembtn1,itembtn2,itembtn3,itembtn4,itembtn5,itembtn6)

        msg=bot.send_message(message.chat.id,"Выберите операцию", reply_markup=markup)
        bot.register_next_step_handler(msg,proces_proc_step)
    except :
        bot.reply_to(message,'Не понимаю, что это значит.')
        return
    
# выбобр операции

def proces_proc_step(message):
    try:
        global symbol

        symbol = message.text
        markup = types.ReplyKeyboardRemove(selective=False)

        msg=bot.send_message(message.chat.id,"Введите еще число", reply_markup=markup)
        bot.register_next_step_handler(msg, proces_num2_step)
    except :
        bot.reply_to(message,'Не понимаю, что это значит.')
        return
# получение второго числа

def proces_num2_step(message):
    try:
        global num_2
        num_2=str(message.text)
     
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=4)
        itembtn1=types.KeyboardButton('результат')
        itembtn2=types.KeyboardButton('продолжить')
        markup.add(itembtn1,itembtn2)

        msg=bot.send_message(message.chat.id,"Показать результат или продолжить операцию", reply_markup=markup)
        bot.register_next_step_handler(msg,proces_alternativ_step)
    except Exception as e:
        bot.reply_to(message,'Не понимаю, что это значит.')
        return 

def proces_alternativ_step(message):    
    try:
        # процесс вычисления
        calc()
        markup=types.ReplyKeyboardRemove(selective=False)

        if message.text.lower()=='результат':
            bot.send_message(message.chat.id, resultcalcPrint(), reply_markup=markup)
        elif message.text.lower()=='продолжить вычисления':
            proces_num1_step(message,result)
    except Exception as e:
        bot.reply_to(f'{message} Не понимаю, что это значит.')
        return


def resultcalcPrint():
    global num_1, num_2, symbol, result

    return "получилось: " + str(num_1) +' ' + symbol + ' ' + str(num_2) + '=' + str(result)

def calc():
    global num_1, num_2, symbol, result

    result = eval((num_1.replace(",",".")) + symbol + (num_2.replace(",",".")))

    return result

bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()

bot.polling()
