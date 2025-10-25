import telebot
import random 

bot = telebot.TeleBot('8027394157:AAFZMddRfPJKWASwi6-gPaZszi7JOQsSpXA')

adv = ["Откажитесь от одноразового. Носите с собой многоразовую сумку для покупок и кружку для кофе с собой. Это простой способ drastically сократить количество мусора.", "Экономьте ресурсы. Выключайте свет, выходя из комнаты, и не оставляйте воду течь зря. Небольшие привычки в сумме дают большой результат для планеты."]

@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id, "Привет, я бот, который расскажет тебе об окружающей среде и расскажет, как именно ТЫ можешь ей помочь! :)")

@bot.message_handler(commands=['problems'])
def send_problems(message):
    bot.send_message(message.chat.id, "Люди активно загрязняют планету: пластик и мусор заполняют леса и водоемы, а промышленные выбросы отравляют воздух. Кроме того, вырубка лесов и освоение земель уничтожают среду обитания многих животных, что ведет к сокращению биоразнообразия.")

@bot.message_handler(commands=['help'])
def send_random(message):
    bot.send_message(message.chat.id, random.choice(adv))

@bot.message_handler(commands=['commands'])
def send_help(message):
    bot.send_message(message.chat.id, "команды: /Start /problems /help")
                 
bot.polling()