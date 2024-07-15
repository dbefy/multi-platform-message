import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F
from config_reader import config



# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value())
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


# Функция для сохранения сообщений в текстовый файл
async def save_message_to_file(message: Message):
    with open("messages.txt", "a", encoding="utf-8") as file:
        file.write(f"{message.chat.id} - {message.from_user.id} ({message.from_user.username}): {message.text}\n")



# Хэндлер для обработки новых сообщений
#@dp.message(content_types=types.ContentType.TEXT)
@dp.message(F.text)
async def handle_message(message: types.Message):
    await save_message_to_file(message)
    await message.reply("Ваше сообщение сохранено.")





# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())