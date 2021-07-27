from telebot import types


def generate_pagination():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text='Tashkent')
    btn2 = types.KeyboardButton(text='Andijan')
    btn3 = types.KeyboardButton(text='Namangan')
    btn4 = types.KeyboardButton(text='Fergana')
    btn5 = types.KeyboardButton(text='Navoiy')
    btn6 = types.KeyboardButton(text='Bukhara')
    btn7 = types.KeyboardButton(text='Samarkand')
    btn8 = types.KeyboardButton(text='Qarshi')
    btn9 = types.KeyboardButton(text='Urgench')
    btn10 = types.KeyboardButton(text='Gulistan')
    btn11 = types.KeyboardButton(text='Jizzakh')
    btn12 = types.KeyboardButton(text='Termez')

    # menu = types.KeyboardButton(text='')

    keyboard.row(btn1, btn2, btn3)
    keyboard.row(btn4, btn5, btn6)
    keyboard.row(btn7, btn8, btn9)
    keyboard.row(btn10, btn11, btn12)

    return keyboard
