import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from config import token

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=token)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command(commands=["start"]))
async def command_start(message: types.Message):
    logging.info("Команда /start получена")
    await message.answer("Привет! Я бот.")

# Обработчик команды /ура
@dp.message(Command(commands=["ура"]))
async def command_ura(message: types.Message):
    logging.info("Команда /ура получена")
    await message.answer("эгегей!")

# Обработчик всех остальных сообщений
@dp.message()
async def echo(message: types.Message):
    logging.info(f"Получено сообщение: {message.text}")
    if message.text.startswith("/"):
        logging.info(f"Команда пропущена: {message.text}")
        return
    logging.info(f"Ответ на сообщение: {message.text}")
    await message.answer(message.text)

# Запуск бота
async def main():
    logging.info("Запуск бота")
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.info("Программа стартует")
    asyncio.run(main())