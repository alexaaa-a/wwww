import telebot

from telebot import custom_filters
from telebot import StateMemoryStorage
from telebot.handler_backends import StatesGroup, State

#link to bot - @umschool_edu_bot

text_button_1 = "Команды"

state_storage = StateMemoryStorage()
bot = telebot.TeleBot("6613646196:AAGZ0Sz0fLrEYZVOgwB8givyDRWEvNBau5E", state_storage=state_storage, parse_mode='Markdown')

class HelpState(StatesGroup):
    wait_text = State()

menu_keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
menu_keyboard.add(telebot.types.KeyboardButton(text_button_1,))

@bot.message_handler(state="*", commands=['start'])
def start_ex(message):
    bot.send_message(message.chat.id,'Привет! Что бы увидеть все команды бота, используй кнопку ниже!', reply_markup=menu_keyboard)

@bot.message_handler(func=lambda message: text_button_1 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, "/umschool - информация о боте\n/contact - связь с создателем", reply_markup=menu_keyboard)

@bot.message_handler(state = "*", commands=['umschool'])
def readme(message):
    bot.send_message(message.chat.id,'Привет! Я тестовый бот для марафона от Умскул!', reply_markup=menu_keyboard)

@bot.message_handler(state = "*", commands=['contact'])
def creator(message):
    bot.send_message(message.chat.id,'Telegram - @K1berman ', reply_markup=menu_keyboard)

bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.TextMatchFilter())

bot.infinity_polling()