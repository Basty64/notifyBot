import logging
from aiogram import Bot, Dispatcher, executor, types
from conf import token_bot
from aiogram.dispatcher.filters import Text


bot = Bot(token=token_bot)
dp = Dispatcher(bot)
# Логирование
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands = "start")
async def start_command(message: types.Message):
    start_keyboard = ["Подтвердить номер"]
    keyboard = types.ReplyKeyboardMarkup(
         resize_keyboard = True)
    keyboard.add(*start_keyboard)
    await bot.send_message(message.from_user.id, "Для того, чтобы посмотреть информацию о бронировании вам нужно подтвердить свой номер телефона", reply_markup = keyboard)

@dp.message_handler(Text)
async def reply_text(message: types.Message):
    await bot.send_message(message.from_user.id, "Пожалуйста, следуйте указаниям")



if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)