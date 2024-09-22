# Создаем клавиатуру
button1 = KeyboardButton(text='Контакты')
button2 = KeyboardButton(text='Задать вопрос')
button3 = KeyboardButton(text='Помочь фонду')
button4 = KeyboardButton(text='Забрать собаку')

keyboard1 = [
    [button1, button2],
    [button3, button4]
]

kb1 = ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
