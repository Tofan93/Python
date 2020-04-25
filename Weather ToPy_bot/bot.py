import pyowm
import telebot

owm = pyowm.OWM('b819a91869f45bb714b2cb0a0c647732', language = 'ru')
bot = telebot.TeleBot('1223510132:AAEg4XkxdnSa92GP4dfcamjb3uznTB9rkzM')

@bot.message_handler(content_types=['text'])
def send_echo(message):
    obs = owm.weather_at_place(message.text)
    city = obs.get_weather()
    temp = city.get_temperature('celsius')['temp']

    answer = 'В городе ' + message.text + ' сейчас ' + city.get_detailed_status()
    answer += 'Температура в районе ' + str(round(temp)) + ' градусов' + '\n\n'
    if temp<10:
        answer += 'Очень холодно, оденься потеплее))'
    elif temp<17:
        answer += 'Прохладно, лучше оденься:)'
    else:
        answer += 'Не холодно, хоть в трусах иди:)'
    bot.send_message(message.chat.id, answer)

bot.polling(none_stop = True)
