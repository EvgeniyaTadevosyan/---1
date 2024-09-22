import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import token  # Импорт токена

# Логирование
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера с машиной состояний
bot = Bot(token=token)
dp = Dispatcher(storage=MemoryStorage())  # Используем MemoryStorage для машины состояний

# Определяем состояние для машины состояний
class QuestionForm(StatesGroup):
    waiting_for_question = State()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def command_start(message: types.Message):
    user_name = message.from_user.first_name  # Получаем имя пользователя
    await message.answer(f"Привет, {user_name}!", reply_markup=kb1)

# Хэндлер на кнопку "Контакты", отправляет адрес и контактную информацию
@dp.message(F.text == 'Контакты')
async def send_contacts(message: types.Message):
    contact_info = (
        "Наши контакты:\n"
        "Телефон: +7 (911) 092-10-71\n"
        "Telegram: @spb_helpminidog\n"
        "Адрес: Октябрьская набережная, 38БМ, Санкт-Петербург"
    )
    await message.answer(contact_info)

# Хэндлер на кнопку "Задать вопрос", просит пользователя ввести вопрос
@dp.message(F.text == 'Задать вопрос')  # Хэндлер на текст "Задать вопрос"
async def ask_question(message: types.Message, state: FSMContext):
    await message.answer("Пожалуйста, введите свой вопрос:")
    await state.set_state(QuestionForm.waiting_for_question)  # Устанавливаем состояние

# Хэндлер для обработки вопроса пользователя
@dp.message(QuestionForm.waiting_for_question)
async def handle_question(message: types.Message, state: FSMContext):
    user_question = message.text  # Получаем вопрос пользователя
    await message.answer(f"Ваш вопрос принят: '{user_question}'. Мы свяжемся с вами в ближайшее время!")
    await state.clear()  # Сбрасываем состояние

# Хэндлер на кнопку "Помочь фонду", отправляет реквизиты фонда
@dp.message(F.text == 'Помочь фонду')
async def send_fund_details(message: types.Message):
    fund_details = (
        "Реквизиты фонда:\n\n"
        "Для юридических лиц:\n"
        "◾ В Рублях РФ:\n"
        "Благотворительный фонд «Мы вместе»\n"
        "ИНН: 7806583230 / КПП: 780601001\n"
        "Филиал ББР Банка (АО), г.Москва\n"
        "Р/с: 40701810202200000003\n"
        "Кор/счёт: 30101810745250000769\n"
        "БИК: 044525769\n\n"
        "Для физических лиц:\n"
        "◾ Карта Сбербанка: 5469550036899679 (Марина Ивановна Клафтон)\n"
        "Привязана к тел: 8-906-227-72-23\n\n"
        "◾ Карта Тинькофф: 4377 7237 4528 7916\n"
        "◾ Карта ВТБ: 5368 2902 5784 6982\n"
        "◾ Карта Озон банк: 2204 3201 7645 9255\n"
        "◾ Карта Альфа-банк: 4584 4328 1193 4828 (Юлия Дмитриевна Клафтон)\n"
        "Привязана к тел: 8-960-273-32-50"
    )
    await message.answer(fund_details)

# Хэндлер на нажатие кнопки "Забрать собаку"
@dp.message(F.text == 'Забрать собаку')
async def send_dog_catalog(message: types.Message):
    catalog_links = (
        "Ознакомьтесь с нашим каталогом собак по ссылкам:\n"
        "1) [Vk](https://vk.com/market-137815324?screen=group)\n"
        "2) [Internet](https://vk.link/spb_helpminidog)"
    )
    await message.answer(catalog_links, disable_web_page_preview=True)

# Запуск бота
if __name__ == "__main__":
    dp.run_polling(bot)
