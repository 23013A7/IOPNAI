from telegram4 import TelegramBot
import threading

def main():
    telegram_bot = TelegramBot() #создания экзэмпляра
    bot_thread = threading.Thread(target=telegram_bot.start, daemon=True)
    bot_thread.start()
    bot_thread.join()  # нужно что бы основной поток не останавливался и код не завершался

    try:
        while True:
            command = input("Что бы остоновить программу нужно написать \"стоп\" без кавычек")
            if command.lower() == 'стоп':
                print("Завершино")
                break
    except KeyboardInterrupt:
        print("\nВыключения Ctrl+C")

if __name__ == "__main__":
    main()