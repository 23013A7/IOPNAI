import telebot #импорт телеграм апи бота
import threading #это библиотека позволяет запускать несколько процесов паралельно
import random
from AI_core import zapros

# Инициализация бота
with open('config.json') as f:
    key = '2'
bot = telebot.TeleBot('████████:██████████████████████████████')

# Конфигурация
CONFIG = {
    'admin_ids': [██████████],  # Замените на ваш ID администратора
    'log_chat_id': -██████████,  # ID группы/канала для логов (замените на свой)
    'data_file': 'bot_data.json'
}

class TelegramBot:
    def __init__(self):
        self.bot = bot
#КОМАНДЫ
        #СТАРТ
        @self.bot.message_handler(commands=['start'])
        def send_welcome(message):
            #сюда добавте юзер менедржер

            welcome_text = (
                "О ПРИВЕТ Я ГЕНИРАТИВНАЯ МОДЕЛЬ ИОПН\n"
                "Я самый умный во всём спрашивай что угодно я на всё знаю ответ мой айкью оценили в 8 данцелионов килоньютонов"
            )
            self.bot.reply_to(message, welcome_text)
        #ХЭЛП
        @self.bot.message_handler(commands=['help'])
        def send_help(message):
            help_text = (
                "Доступные команды:\n"
                "/start - Старт\n"
                "/help - Показывает допступные команды\n"
                "/stats - Статистика о тебе"
            )
            self.bot.reply_to(message, help_text)

        @self.bot.message_handler(commands=['test'])
        def test_function(message):
            test_rezultat = generate_word_chain_string("гавриловна", 10)
            self.bot.reply_to(message, test_rezultat)
      # ТУТ ГЕНИРАЦИЯ ОТВЕТОВ
        @self.bot.message_handler(func=lambda message: True)
        def handle_message(message):
            try:
                # Добавление/обновление статистики
                #self.user_manager.add_user(
                #    message.from_user.id,
                #    message.from_user.username,
                #    message.from_user.first_name,
                #    message.from_user.last_name
                #)

                # Обновляем активность
                #self.user_manager.update_user_activity(message.from_user.id)

                # Генерируем ответ
                response = zapros(message.text)

                self.bot.reply_to(message, response)

                # Отправляем ответ


                # Логируем сообщение
               # self.user_manager.log_message(
               #     message.from_user.id,
               #     message.from_user.username or "Нет ника",
               #     message.text,
               #     response
               # )

                # Отправляем в лог-чат если настроен
               # if CONFIG['log_chat_id']:
               #     try:
               #         log_message = (
               #             f"Пользователь: {message.from_user.first_name} (@{message.from_user.username or 'нет'})\n"
               #             f"Id: {message.from_user.id}\n"
               #             f"Вопрос: {message.text}\n"
               #             f"Ответ: {response}"
               #         )
               #         self.bot.send_message(CONFIG['log_chat_id'], log_message)
               #     except Exception as e:
               #         print(f"Ошибка отправки в лог-чат: {e}")

            except Exception as e:
                print(f"Ошибка обработки сообщения: {e}")
                self.bot.reply_to(message, f"Произошла ошибка при обработке сообщения. {e}")

    def start(self):
        print("Бот запущен")
        self.bot.infinity_polling()

def main():
    telegram_bot = TelegramBot()
    bot_thread = threading.Thread(target=telegram_bot.start, daemon=True)
    bot_thread.start()
    bot_thread.join() #нужно что бы основной поток не останавливался и код не завершался

if __name__ == "__main__":
    main()