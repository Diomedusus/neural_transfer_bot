from typing import Text
!pip install pytelegrambotapi --upgrade
import telebot
from telebot import custom_filters
from telebot.async_telebot import AsyncTeleBot
import io
import asyncio
import model
bot = telebot.TeleBot("YourTOKEN")
content_img_bot = io.BytesIO()
style_img_bot = io.BytesIO()

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
	bot.reply_to(message, "Для изменения стиля направьте картинки в чат с ботом, для картинки со стилем используйте подпись Style, а для изменяемой картинки Content")

@bot.message_handler(content_types=['photo'])

def get_photo(message):
  global content_img_bot
  global style_img_bot
  if message.caption.lower() == 'style':
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    style_img_bot = bot.download_file(file_info.file_path)
    
    if (type(style_img_bot) is bytes and style_img_bot != 0) and (type(content_img_bot) is bytes and content_img_bot != 0):
    
      bot.reply_to(message, "Изображение на изменения и изображения стиля приняты в обработку")
      content_image = image_loader(io.BytesIO(content_img_bot))
      style_image = image_loader(io.BytesIO(style_img_bot))
      input_img = content_image.clone()
      output = run_style_transfer(cnn, cnn_normalization_mean, cnn_normalization_std, content_image, style_image, input_img)
      output_to_bot = postprocess(output)
      bot.send_photo(chat_id=message.from_user.id, photo=output_to_bot)
      content_img_bot = io.BytesIO()
      style_img_bot = io.BytesIO()
    else:
      
      bot.reply_to(message, "Направлена картинка для стиля, направьте картинку на изменение под стиль")

  elif message.caption == 'content':
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    content_img_bot = bot.download_file(file_info.file_path)
    if (type(style_img_bot) is bytes and style_img_bot != 0) and (type(content_img_bot) is bytes and content_img_bot != 0): 
      
      bot.reply_to(message, "Изображение на изменение и изображение для стиля приняты в обработку")
      content_image = image_loader(io.BytesIO(content_img_bot))
      style_image = image_loader(io.BytesIO(style_img_bot))
      input_img = content_image.clone()
      output = run_style_transfer(cnn, cnn_normalization_mean, cnn_normalization_std, content_image, style_image, input_img)
      output_to_bot = postprocess(output)  
      bot.send_photo(chat_id=message.from_user.id, photo=output_to_bot)
      content_img_bot = io.BytesIO()
      style_img_bot = io.BytesIO()
    else:
      bot.reply_to(message, "Направлена картинка для изменения, выберите картинку для стиля")
    
bot.infinity_polling()
