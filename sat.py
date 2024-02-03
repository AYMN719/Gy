import telebot
from gtts import gTTS
from io import BytesIO

bot = telebot.TeleBot("6863593658:AAG_w2gQP0EqipwblNbaf_MkMSTvI-zNnow")

@bot.message_handler(commands=[ 'start' ])
def send_welcome(message):
    bot.reply_to(message, "مرحبًا بك في بوت تحويل النص إلى صوت!")

@bot.message_handler(func=lambda message: True)
def message_handler(message):

    text = message.text

    audio_file = BytesIO()
    tts = gTTS(text, lang= 'ar' )
    tts.write_to_fp(audio_file)
    audio_file.seek(0)


    bot.send_voice(chat_id=message.chat.id, voice=audio_file)


    audio_file.close()

bot.polling()