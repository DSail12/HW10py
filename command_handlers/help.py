from telegram import Update, constants
from telegram.ext import ContextTypes
from decorators.send_action import send_typing_action


@send_typing_action
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    answer = '''Список команд :
    /help - Показать, что я умею
    <b>Сложение многочленов:</b>
    Присылайте многочлены в одном сообщении, каждый с новой строки (Shift+Enter).
    А я пришлю результат их сложения.
    Формат многочлена:
    4x^2 + 3x^7 + 8x^5 + 3x^3 + 4x + 64 = 0
    или
    3x^5 + 8x^2 + 3x^4 + 4x^2 + 7x + 57
    '''
    await update.message.reply_text(text=answer, parse_mode=constants.ParseMode.HTML)
